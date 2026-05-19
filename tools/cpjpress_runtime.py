#!/usr/bin/env python3
"""Runtime copied into generated CPJPress projects.

The module uses only Python's standard library. It provides a WordPress-style
CMS baseline for CPJ: users, sessions, posts/pages, comments, media metadata,
search, feeds, plugin metadata/hooks, and JSON APIs.
"""

from __future__ import annotations

from datetime import datetime, timezone
from html import escape
from http import cookies
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse
import hashlib
import json
import mimetypes
import os
import re
import secrets
import sqlite3
import uuid


def slugify(value: object, fallback: str = "item") -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", str(value).strip().lower()).strip("-")
    return slug or fallback


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def password_hash(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(8)
    digest = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return f"sha256${salt}${digest}"


def password_ok(password: str, stored: str) -> bool:
    try:
        _, salt, digest = stored.split("$", 2)
    except ValueError:
        return False
    return password_hash(password, salt).split("$", 2)[2] == digest


class CPJPressSite:
    def __init__(
        self,
        *,
        routes: dict[str, str],
        api_routes: dict[str, dict[str, object]],
        cms_config: dict[str, object],
        cms_seed: dict[str, object],
        theme: dict[str, str],
        components: dict[str, str],
        assets: dict[str, dict[str, str]] | None = None,
        stores: dict[str, dict[str, object]] | None = None,
        uploads: list[dict[str, object]] | None = None,
        middleware: list[dict[str, object]] | None = None,
        pipelines: list[dict[str, object]] | None = None,
        guards: list[dict[str, object]] | None = None,
        migrations: list[dict[str, object]] | None = None,
        services: dict[str, dict[str, object]] | None = None,
        marketplace: dict[str, object] | None = None,
        host: str = "127.0.0.1",
        port: int = 8090,
    ):
        self.routes = routes
        self.api_routes = api_routes
        self.config = cms_config
        self.seed = cms_seed
        self.theme = theme
        self.components = components
        self.assets = assets or {}
        self.stores = stores or {}
        self.uploads = uploads or []
        self.middleware = middleware or []
        self.pipelines = pipelines or []
        self.guards = guards or []
        self.migrations = migrations or []
        self.services = services or {}
        self.marketplace = marketplace or {"name": "CPJ Marketplace", "registry": "local", "plugins": [], "hooks": {}}
        self.host = host
        self.port = int(port)
        self.storage = Path(str(self.config.get("storage", "cpjpress_content.json")))
        self.store_db = Path(str(self.config.get("store_db", "cpj_store.sqlite3")))
        self.admin_path = str(self.config.get("admin_path", "/admin")).rstrip("/") or "/admin"
        self.blog_path = str(self.config.get("blog_path", "/blog")).rstrip("/") or "/blog"

    def load(self) -> dict[str, object]:
        if not self.storage.exists():
            self.save(self.seed_store())
        try:
            data = json.loads(self.storage.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = self.seed_store()
            self.save(data)
        return self.normalize(data)

    def save(self, data: dict[str, object]) -> None:
        self.storage.write_text(json.dumps(self.normalize(data), indent=2), encoding="utf-8")

    def seed_store(self) -> dict[str, object]:
        users = list(self.seed.get("users", []))
        if not users:
            users.append(
                {
                    "username": "admin",
                    "display_name": "Administrator",
                    "role": "admin",
                    "password_hash": password_hash("admin"),
                    "created_at": now_iso(),
                }
            )
        else:
            for user in users:
                if "password_hash" not in user:
                    user["password_hash"] = password_hash(str(user.pop("password", "admin")))
                user.setdefault("created_at", now_iso())

        return {
            "posts": list(self.seed.get("posts", [])),
            "comments": list(self.seed.get("comments", [])),
            "media": list(self.seed.get("media", [])),
            "users": users,
            "sessions": {},
            "settings": dict(self.seed.get("settings", {})),
            "plugins": list(self.seed.get("plugins", [])),
        }

    def normalize(self, data: dict[str, object]) -> dict[str, object]:
        data.setdefault("posts", [])
        data.setdefault("comments", [])
        data.setdefault("media", [])
        data.setdefault("sessions", {})
        data.setdefault("settings", {})
        data.setdefault("plugins", [])
        users = data.setdefault("users", [])
        if not users:
            users.append(
                {
                    "username": "admin",
                    "display_name": "Administrator",
                    "role": "admin",
                    "password_hash": password_hash("admin"),
                    "created_at": now_iso(),
                }
            )
        for user in users:
            if "password_hash" not in user:
                user["password_hash"] = password_hash(str(user.pop("password", "admin")))
            user.setdefault("display_name", user.get("username", "User"))
            user.setdefault("role", "editor")
            user.setdefault("created_at", now_iso())
        return data

    def layout(self, title: str, body: str, user: dict[str, object] | None = None) -> str:
        site = escape(str(self.config.get("name", "CPJPress")))
        nav_auth = (
            f'<span class="meta">Signed in as {escape(str(user.get("display_name") or user.get("username")))}</span> '
            f'<a href="/logout">Logout</a>'
            if user
            else '<a href="/login">Login</a>'
        )
        theme_vars = "\n".join(
            f"      --cpj-{escape(str(key).replace('_', '-'))}: {escape(str(value))};"
            for key, value in self.theme.items()
        )
        return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} - {site}</title>
  <style>
    :root {{
{theme_vars}
      --cpj-bg: var(--cpj-background, #f6f8fb);
      --cpj-radius: 8px;
      --cpj-shadow: 0 18px 48px rgba(24, 33, 47, 0.10);
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--cpj-bg); color: var(--cpj-text, #18212f); font-family: Inter, ui-sans-serif, system-ui, sans-serif; line-height: 1.55; }}
    header, main {{ width: min(1120px, calc(100% - 32px)); margin: 0 auto; }}
    header {{ display: flex; align-items: center; justify-content: space-between; gap: 18px; padding: 18px 0; border-bottom: 1px solid var(--cpj-border, #d8dee8); }}
    nav {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }}
    a {{ color: var(--cpj-primary, #2457c5); font-weight: 700; }}
    main {{ padding: 44px 0 80px; }}
    article, form, .cpj-panel {{ background: var(--cpj-surface, #fff); border: 1px solid var(--cpj-border, #d8dee8); border-radius: var(--cpj-radius); padding: 22px; box-shadow: var(--cpj-shadow); margin-bottom: 16px; }}
    h1 {{ font-size: clamp(2rem, 6vw, 4rem); line-height: 1.02; margin-top: 0; letter-spacing: 0; }}
    input, textarea, select {{ display: block; width: 100%; margin: 6px 0 14px; padding: 11px 12px; border: 1px solid var(--cpj-border, #d8dee8); border-radius: var(--cpj-radius); font: inherit; }}
    textarea {{ min-height: 160px; }}
    button {{ min-height: 42px; padding: 0 16px; border: 0; border-radius: var(--cpj-radius); background: var(--cpj-primary, #2457c5); color: white; font-weight: 800; cursor: pointer; }}
    table {{ width: 100%; border-collapse: collapse; }}
    td, th {{ border-bottom: 1px solid var(--cpj-border, #d8dee8); padding: 10px; text-align: left; }}
    .meta {{ color: var(--cpj-muted, #617085); }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 16px; }}
    .toolbar {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 16px; }}
  </style>
</head>
<body>
  <header>
    <strong>{site}</strong>
    <nav>
      <a href="/">Home</a>
      <a href="{escape(self.blog_path)}">Posts</a>
      <a href="/search">Search</a>
      <a href="/feed.xml">Feed</a>
      <a href="{escape(self.admin_path)}">Admin</a>
      <a href="/api/posts">API</a>
      {nav_auth}
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""

    def current_user(self, handler: BaseHTTPRequestHandler) -> dict[str, object] | None:
        cookie = cookies.SimpleCookie(handler.headers.get("Cookie", ""))
        sid = cookie.get("cpjpress_session")
        if not sid:
            return None
        data = self.load()
        username = data.get("sessions", {}).get(sid.value)
        for user in data.get("users", []):
            if user.get("username") == username:
                return user
        return None

    def require_user(self, handler: BaseHTTPRequestHandler) -> dict[str, object] | None:
        user = self.current_user(handler)
        if user:
            return user
        handler.send_response(302)
        handler.send_header("Location", "/login")
        handler.end_headers()
        return None

    def send(self, handler: BaseHTTPRequestHandler, status: int, body: str | bytes, content_type: str) -> None:
        payload = body.encode("utf-8") if isinstance(body, str) else body
        handler.send_response(status)
        handler.send_header("Content-Type", content_type)
        handler.send_header("Content-Length", str(len(payload)))
        handler.send_header("Cache-Control", "no-store")
        for name, value in self.middleware_headers().items():
            handler.send_header(name, value)
        handler.end_headers()
        handler.wfile.write(payload)

    def send_json(self, handler: BaseHTTPRequestHandler, status: int, payload: object) -> None:
        self.send(handler, status, json.dumps(payload, indent=2), "application/json; charset=utf-8")

    def middleware_entries(self) -> list[dict[str, object]]:
        named = {item.get("name"): item for item in self.middleware}
        entries = list(self.middleware)
        for pipeline in self.pipelines:
            for name in pipeline.get("uses", []):
                if name in named:
                    entries.append(named[name])
            entries.append(pipeline)
        return entries

    def middleware_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {}
        for item in self.middleware_entries():
            headers.update(item.get("headers", {}))
            cors = item.get("cors")
            if cors:
                headers["Access-Control-Allow-Origin"] = str(cors)
                headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
                headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-CPJ-Token"
            if item.get("request_id"):
                headers.setdefault("X-CPJ-Request-ID", uuid.uuid4().hex)
        return headers

    def middleware_allows(self, handler: BaseHTTPRequestHandler, path: str) -> bool:
        for item in self.middleware_entries():
            for rule in item.get("require_headers", []):
                rule_path = str(rule.get("path", "")).rstrip("/")
                if rule_path and not path.startswith(rule_path):
                    continue
                header = str(rule.get("header", ""))
                expected = str(rule.get("value", ""))
                if header and handler.headers.get(header, "") != expected:
                    self.send_json(
                        handler,
                        403,
                        {"error": "middleware_rejected", "pipeline": item.get("name"), "required_header": header},
                    )
                    return False
        return True

    def resolve_services(self) -> dict[str, dict[str, object]]:
        resolved = {}
        for name, service in self.services.items():
            values = dict(service.get("values", {}))
            for key, env_spec in service.get("env", {}).items():
                env_name = str(env_spec.get("name", ""))
                values[key] = os.environ.get(env_name, env_spec.get("default", ""))
            resolved[name] = values
        return resolved

    def guard_allows(self, handler: BaseHTTPRequestHandler, path: str) -> bool:
        for guard in self.guards:
            guard_path = str(guard.get("path", "")).rstrip("/")
            if not guard_path or not path.startswith(guard_path):
                continue
            expected = str(guard.get("token", ""))
            provided = handler.headers.get("X-CPJ-Token", "")
            auth = handler.headers.get("Authorization", "")
            if auth.startswith("Bearer "):
                provided = auth.split(" ", 1)[1]
            if not expected or provided == expected:
                return True
            self.send_json(handler, 401, {"error": "unauthorized", "path": path})
            return False
        return True

    def send_api(
        self,
        handler: BaseHTTPRequestHandler,
        path: str,
        method: str,
        data: dict[str, str] | None = None,
    ) -> bool:
        route = self.api_routes.get(path)
        if not route:
            return False
        allowed = str(route.get("method", "GET")).upper()
        if allowed != method:
            self.send_json(handler, 405, {"error": "method_not_allowed", "allowed": allowed, "method": method})
            return True
        payload = dict(route.get("json", {}))
        inject = route.get("inject", [])
        if inject:
            resolved = self.resolve_services()
            payload["services"] = {name: resolved.get(name, {}) for name in inject}
        if data is not None:
            payload["request"] = data
        self.send_json(handler, 200, payload)
        return True

    def sql_type(self, field_type: object) -> str:
        lowered = str(field_type).lower()
        if lowered in {"int", "integer", "bool", "boolean"}:
            return "INTEGER"
        if lowered in {"float", "double", "decimal", "number", "real"}:
            return "REAL"
        if lowered in {"bytes", "blob", "binary", "file"}:
            return "BLOB"
        return "TEXT"

    def safe_identifier(self, value: object) -> str:
        name = str(value)
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
            raise ValueError(f"Unsafe SQL identifier: {name}")
        return name

    def existing_columns(self, db, table: str) -> set[str]:
        table = self.safe_identifier(table)
        return {row[1] for row in db.execute(f"PRAGMA table_info({table})").fetchall()}

    def apply_migrations(self, db) -> None:
        if not self.migrations:
            return
        db.execute("CREATE TABLE IF NOT EXISTS cpj_migrations (name TEXT PRIMARY KEY, applied_at TEXT NOT NULL)")
        applied = {row[0] for row in db.execute("SELECT name FROM cpj_migrations").fetchall()}
        for migration in self.migrations:
            name = str(migration.get("name", "migration"))
            store = self.safe_identifier(migration.get("store", name))
            if name in applied:
                continue
            current_columns = self.existing_columns(db, store)
            for field in migration.get("add_fields", []):
                field_name = self.safe_identifier(field.get("name"))
                if field_name in current_columns:
                    continue
                required = " NOT NULL DEFAULT ''" if field.get("required") else ""
                db.execute(f"ALTER TABLE {store} ADD COLUMN {field_name} {self.sql_type(field.get('type', 'text'))}{required}")
                current_columns.add(field_name)
            for index in migration.get("indexes", []):
                field_name = self.safe_identifier(index.get("field"))
                unique = "UNIQUE " if index.get("unique") else ""
                index_name = self.safe_identifier(f"idx_{store}_{field_name}")
                db.execute(f"CREATE {unique}INDEX IF NOT EXISTS {index_name} ON {store} ({field_name})")
            db.execute("INSERT OR REPLACE INTO cpj_migrations (name, applied_at) VALUES (?, ?)", [name, now_iso()])

    def init_stores(self) -> None:
        if not self.stores and not self.migrations:
            return
        db = sqlite3.connect(self.store_db)
        try:
            for name, store in self.stores.items():
                table_name = self.safe_identifier(name)
                columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT", "created_at TEXT NOT NULL"]
                for field in store.get("fields", []):
                    field_name = self.safe_identifier(field["name"])
                    required = " NOT NULL" if field.get("required") else ""
                    columns.append(f"{field_name} {self.sql_type(field.get('type', 'text'))}{required}")
                db.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
            self.apply_migrations(db)
            for name, store in self.stores.items():
                table_name = self.safe_identifier(name)
                count = db.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
                if count == 0:
                    for row in store.get("seed", []):
                        self.store_create(name, row, db=db)
            db.commit()
        finally:
            db.close()

    def store_create(self, name: str, data: dict[str, object], db=None) -> dict[str, object]:
        close = db is None
        db = db or sqlite3.connect(self.store_db)
        try:
            table_name = self.safe_identifier(name)
            fields = [self.safe_identifier(field["name"]) for field in self.stores[name].get("fields", [])]
            row: dict[str, object] = {"created_at": now_iso()}
            for field in fields:
                row[field] = data.get(field, "")
            columns = list(row.keys())
            placeholders = ", ".join("?" for _ in columns)
            db.execute(
                f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})",
                [row[column] for column in columns],
            )
            row["id"] = db.execute("SELECT last_insert_rowid()").fetchone()[0]
            if close:
                db.commit()
            return row
        finally:
            if close:
                db.close()

    def store_rows(self, name: str) -> list[dict[str, object]]:
        db = sqlite3.connect(self.store_db)
        db.row_factory = sqlite3.Row
        try:
            table_name = self.safe_identifier(name)
            rows = db.execute(f"SELECT * FROM {table_name} ORDER BY id DESC").fetchall()
            return [dict(row) for row in rows]
        finally:
            db.close()

    def store_update(self, name: str, row_id: str, data: dict[str, object]) -> dict[str, object] | None:
        db = sqlite3.connect(self.store_db)
        db.row_factory = sqlite3.Row
        try:
            table_name = self.safe_identifier(name)
            fields = [self.safe_identifier(field["name"]) for field in self.stores[name].get("fields", []) if field["name"] in data]
            if fields:
                assignments = ", ".join(f"{field} = ?" for field in fields)
                db.execute(f"UPDATE {table_name} SET {assignments} WHERE id = ?", [data[field] for field in fields] + [row_id])
                db.commit()
            row = db.execute(f"SELECT * FROM {table_name} WHERE id = ?", [row_id]).fetchone()
            return dict(row) if row else None
        finally:
            db.close()

    def store_delete(self, name: str, row_id: str) -> dict[str, object]:
        db = sqlite3.connect(self.store_db)
        try:
            table_name = self.safe_identifier(name)
            db.execute(f"DELETE FROM {table_name} WHERE id = ?", [row_id])
            db.commit()
        finally:
            db.close()
        return {"deleted": True, "id": row_id}

    def handle_store(self, handler: BaseHTTPRequestHandler, path: str, method: str, data: dict[str, object] | None = None) -> bool:
        for name, store in self.stores.items():
            base = str(store.get("path", f"/api/store/{name}")).rstrip("/")
            if path == base:
                if method == "GET":
                    self.send_json(handler, 200, self.store_rows(name))
                    return True
                if method == "POST":
                    self.send_json(handler, 201, self.store_create(name, data or {}))
                    return True
            if path.startswith(base + "/"):
                row_id = path.rsplit("/", 1)[-1]
                if method in {"PUT", "PATCH"}:
                    self.send_json(handler, 200, self.store_update(name, row_id, data or {}) or {"error": "not_found"})
                    return True
                if method == "DELETE":
                    self.send_json(handler, 200, self.store_delete(name, row_id))
                    return True
        return False

    def parse_multipart(self, content_type: str, body: bytes) -> dict[str, object]:
        marker = "boundary="
        if marker not in content_type:
            return {"__invalid_multipart__": True}
        boundary = content_type.split(marker, 1)[1].split(";", 1)[0].strip().strip('"').encode("utf-8")
        fields: dict[str, object] = {}
        files = []
        for part in body.split(b"--" + boundary):
            part = part.strip(b"\r\n")
            if not part or part == b"--" or b"\r\n\r\n" not in part:
                continue
            raw_headers, content = part.split(b"\r\n\r\n", 1)
            headers = raw_headers.decode("utf-8", "replace").split("\r\n")
            disposition = next((header for header in headers if header.lower().startswith("content-disposition:")), "")
            content_type_header = next((header for header in headers if header.lower().startswith("content-type:")), "")
            attrs = {}
            for chunk in disposition.split(";"):
                if "=" in chunk:
                    key, value = chunk.strip().split("=", 1)
                    attrs[key.lower()] = value.strip().strip('"')
            field_name = attrs.get("name", "")
            filename = attrs.get("filename")
            content = content.rstrip(b"\r\n")
            if filename:
                files.append(
                    {
                        "field": field_name,
                        "filename": filename,
                        "content_type": content_type_header.split(":", 1)[1].strip() if ":" in content_type_header else "application/octet-stream",
                        "content": content,
                        "size": len(content),
                    }
                )
            elif field_name:
                fields[field_name] = content.decode("utf-8", "replace")
        fields["__files__"] = files
        return fields

    def handle_upload(self, handler: BaseHTTPRequestHandler, path: str, method: str, data: dict[str, object]) -> bool:
        if method != "POST":
            return False
        for upload in self.uploads:
            if path != str(upload.get("path")):
                continue
            saved = []
            target_dir = Path(str(upload.get("dir", "uploads")))
            target_dir.mkdir(parents=True, exist_ok=True)
            accepts = set(upload.get("accept", []))
            max_bytes = int(upload.get("max_bytes", 5 * 1024 * 1024))
            for item in data.get("__files__", []):
                if item["size"] > max_bytes:
                    self.send_json(handler, 413, {"error": "file_too_large", "filename": item["filename"]})
                    return True
                if accepts and item["content_type"] not in accepts and mimetypes.guess_type(item["filename"])[0] not in accepts:
                    self.send_json(handler, 415, {"error": "unsupported_media_type", "filename": item["filename"]})
                    return True
                safe = re.sub(r"[^a-zA-Z0-9._-]+", "-", Path(item["filename"]).name).strip(".-") or "upload.bin"
                destination = target_dir / f"{uuid.uuid4().hex}-{safe}"
                destination.write_bytes(item["content"])
                saved.append(
                    {
                        "field": item["field"],
                        "filename": item["filename"],
                        "stored_as": str(destination).replace("\\", "/"),
                        "url": "/" + str(destination).replace("\\", "/"),
                        "content_type": item["content_type"],
                        "size": item["size"],
                    }
                )
            self.send_json(handler, 201, {"files": saved, "fields": {k: v for k, v in data.items() if k != "__files__"}})
            return True
        return False

    def redirect(self, handler: BaseHTTPRequestHandler, location: str) -> None:
        handler.send_response(302)
        handler.send_header("Location", location)
        handler.end_headers()

    def published_posts(self, include_pages: bool = True) -> list[dict[str, object]]:
        posts = [
            post
            for post in self.load().get("posts", [])
            if post.get("status", "published") == "published"
            and (include_pages or post.get("type", "post") == "post")
        ]
        return sorted(posts, key=lambda item: str(item.get("created_at", "")), reverse=True)

    def post_card(self, post: dict[str, object]) -> str:
        slug = escape(str(post.get("slug", "")))
        title = escape(str(post.get("title", "Untitled")))
        body = escape(str(post.get("body", "")))
        created = escape(str(post.get("created_at", "")))
        return f"""<article>
  <p class="meta">{created} - {escape(str(post.get("author", "CPJ")))}</p>
  <h2><a href="{self.blog_path}/{slug}">{title}</a></h2>
  <p>{body[:280]}</p>
</article>"""

    def find_post(self, slug: str) -> dict[str, object] | None:
        for post in self.load().get("posts", []):
            if str(post.get("slug")) == slug:
                return post
        return None

    def comments_for(self, slug: str) -> list[dict[str, object]]:
        return [comment for comment in self.load().get("comments", []) if comment.get("post") == slug]

    def page_home(self, user: dict[str, object] | None) -> str:
        if "/" in self.routes:
            return self.routes["/"]
        cards = "".join(self.post_card(post) for post in self.published_posts(include_pages=False)[:6])
        body = f"<h1>{escape(str(self.config.get('name', 'CPJPress')))}</h1><p class='meta'>Generated CPJ standalone CMS.</p>{cards}"
        return self.layout("Home", body, user)

    def page_blog(self, user: dict[str, object] | None) -> str:
        cards = "".join(self.post_card(post) for post in self.published_posts(include_pages=False))
        body = "<h1>Posts</h1>" + (cards or '<p class="meta">No posts yet.</p>')
        return self.layout("Posts", body, user)

    def page_single(self, slug: str, user: dict[str, object] | None) -> str:
        post = self.find_post(slug)
        if not post:
            return self.layout("Not found", '<div class="cpj-panel"><h1>Post not found</h1></div>', user)
        title = escape(str(post.get("title", "Untitled")))
        body = escape(str(post.get("body", ""))).replace("\n", "<br>")
        comments = "".join(
            f"<article><strong>{escape(str(c.get('author', 'Anonymous')))}</strong><p>{escape(str(c.get('body', '')))}</p></article>"
            for c in self.comments_for(slug)
        )
        form = f"""<form method="post" action="/comments">
  <input type="hidden" name="post" value="{escape(slug)}">
  <label>Name<input name="author" required></label>
  <label>Comment<textarea name="body" required></textarea></label>
  <button type="submit">Comment</button>
</form>"""
        html = f"<article><p class='meta'>{escape(str(post.get('created_at', '')))}</p><h1>{title}</h1><p>{body}</p></article><h2>Comments</h2>{comments}{form}"
        return self.layout(title, html, user)

    def page_search(self, query: str, user: dict[str, object] | None) -> str:
        q = query.strip().lower()
        matches = []
        if q:
            for post in self.published_posts():
                text = f"{post.get('title', '')} {post.get('body', '')}".lower()
                if q in text:
                    matches.append(post)
        form = f"""<form method="get" action="/search">
  <label>Search<input name="q" value="{escape(query)}"></label>
  <button type="submit">Search</button>
</form>"""
        body = "<h1>Search</h1>" + form + "".join(self.post_card(post) for post in matches)
        return self.layout("Search", body, user)

    def page_admin(self, user: dict[str, object], message: str = "") -> str:
        data = self.load()
        posts = "".join(
            f"<tr><td>{escape(str(p.get('title', '')))}</td><td>{escape(str(p.get('type', 'post')))}</td><td>{escape(str(p.get('status', '')))}</td><td>{escape(str(p.get('slug', '')))}</td></tr>"
            for p in data.get("posts", [])
        )
        media = "".join(
            f"<tr><td>{escape(str(m.get('title', '')))}</td><td><a href='{escape(str(m.get('url', '')))}'>{escape(str(m.get('url', '')))}</a></td></tr>"
            for m in data.get("media", [])
        )
        plugins = "".join(
            f"<li><strong>{escape(str(p.get('name', p.get('slug', ''))))}</strong> - {escape(str(p.get('description', '')))}</li>"
            for p in data.get("plugins", [])
        )
        notice = f'<p class="meta">{escape(message)}</p>' if message else ""
        body = f"""<h1>CPJPress Admin</h1>
{notice}
<div class="grid">
  <form method="post" action="{self.admin_path}/post">
    <h2>Publish</h2>
    <label>Title<input name="title" required></label>
    <label>Slug<input name="slug"></label>
    <label>Type<select name="type"><option value="post">post</option><option value="page">page</option></select></label>
    <label>Status<select name="status"><option value="published">published</option><option value="draft">draft</option></select></label>
    <label>Body<textarea name="body" required></textarea></label>
    <button type="submit">Save</button>
  </form>
  <form method="post" action="{self.admin_path}/media">
    <h2>Media</h2>
    <label>Title<input name="title" required></label>
    <label>URL<input name="url" required></label>
    <label>Alt text<input name="alt"></label>
    <button type="submit">Add Media</button>
  </form>
</div>
<section class="cpj-panel"><h2>Content</h2><table><tr><th>Title</th><th>Type</th><th>Status</th><th>Slug</th></tr>{posts}</table></section>
<section class="cpj-panel"><h2>Media Library</h2><table><tr><th>Title</th><th>URL</th></tr>{media}</table></section>
<section class="cpj-panel"><h2>Plugins</h2><ul>{plugins or '<li>No plugins configured.</li>'}</ul></section>"""
        return self.layout("Admin", body, user)

    def page_login(self, message: str = "") -> str:
        notice = f'<p class="meta">{escape(message)}</p>' if message else ""
        body = f"""<h1>Login</h1>
{notice}
<form method="post" action="/login">
  <label>Username<input name="username" required></label>
  <label>Password<input name="password" type="password" required></label>
  <button type="submit">Login</button>
</form>"""
        return self.layout("Login", body)

    def handle_get(self, handler: BaseHTTPRequestHandler) -> bool:
        parsed = urlparse(handler.path)
        path = parsed.path.rstrip("/") or "/"
        query = parse_qs(parsed.query)
        user = self.current_user(handler)
        if not self.middleware_allows(handler, path):
            return True
        if not self.guard_allows(handler, path):
            return True
        if path in self.assets:
            asset = self.assets[path]
            self.send(handler, 200, asset["body"], asset["content_type"])
            return True
        if path == "/__cpj/services":
            self.send_json(handler, 200, self.resolve_services())
            return True
        if path == "/__cpj/plugins":
            self.send_json(handler, 200, self.marketplace)
            return True
        if self.handle_store(handler, path, "GET"):
            return True
        if self.send_api(handler, path, "GET"):
            return True
        if path == "/":
            self.send(handler, 200, self.page_home(user), "text/html; charset=utf-8")
            return True
        if path == self.blog_path:
            self.send(handler, 200, self.page_blog(user), "text/html; charset=utf-8")
            return True
        if path.startswith(self.blog_path + "/"):
            self.send(handler, 200, self.page_single(path[len(self.blog_path) + 1 :], user), "text/html; charset=utf-8")
            return True
        if path == "/search":
            self.send(handler, 200, self.page_search(query.get("q", [""])[0], user), "text/html; charset=utf-8")
            return True
        if path == "/login":
            self.send(handler, 200, self.page_login(), "text/html; charset=utf-8")
            return True
        if path == "/logout":
            handler.send_response(302)
            handler.send_header("Set-Cookie", "cpjpress_session=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax")
            handler.send_header("Location", "/")
            handler.end_headers()
            return True
        if path == self.admin_path:
            user = self.require_user(handler)
            if user:
                self.send(handler, 200, self.page_admin(user), "text/html; charset=utf-8")
            return True
        if path == "/api/posts":
            self.send_json(handler, 200, self.load().get("posts", []))
            return True
        if path.startswith("/api/posts/"):
            self.send_json(handler, 200, self.find_post(path.rsplit("/", 1)[-1]) or {"error": "not_found"})
            return True
        if path == "/api/comments":
            self.send_json(handler, 200, self.load().get("comments", []))
            return True
        if path == "/api/media":
            self.send_json(handler, 200, self.load().get("media", []))
            return True
        if path == "/api/plugins":
            self.send_json(handler, 200, self.load().get("plugins", []))
            return True
        if path == "/feed.xml":
            self.send(handler, 200, self.feed_xml(), "application/rss+xml; charset=utf-8")
            return True
        if path == "/sitemap.xml":
            self.send(handler, 200, self.sitemap_xml(), "application/xml; charset=utf-8")
            return True
        if path in self.routes:
            self.send(handler, 200, self.routes[path], "text/html; charset=utf-8")
            return True
        return False

    def handle_post(self, handler: BaseHTTPRequestHandler, data: dict[str, str]) -> bool:
        path = urlparse(handler.path).path.rstrip("/") or "/"
        if not self.middleware_allows(handler, path):
            return True
        if not self.guard_allows(handler, path):
            return True
        if self.handle_upload(handler, path, "POST", data):
            return True
        if self.handle_store(handler, path, "POST", data):
            return True
        if self.send_api(handler, path, "POST", data):
            return True
        if path == "/login":
            store = self.load()
            username = data.get("username", "")
            password = data.get("password", "")
            for user in store.get("users", []):
                if user.get("username") == username and password_ok(password, str(user.get("password_hash", ""))):
                    sid = secrets.token_urlsafe(24)
                    store.setdefault("sessions", {})[sid] = username
                    self.save(store)
                    handler.send_response(302)
                    handler.send_header("Set-Cookie", f"cpjpress_session={sid}; Path=/; HttpOnly; SameSite=Lax")
                    handler.send_header("Location", self.admin_path)
                    handler.end_headers()
                    return True
            self.send(handler, 401, self.page_login("Invalid credentials"), "text/html; charset=utf-8")
            return True
        if path in {self.admin_path + "/post", "/api/posts"}:
            user = self.current_user(handler) if path.startswith(self.admin_path) else None
            if path.startswith(self.admin_path) and not user:
                self.redirect(handler, "/login")
                return True
            post = self.save_post(data, user)
            if path == "/api/posts":
                self.send_json(handler, 201, post)
            else:
                self.send(handler, 200, self.page_admin(user or {}, f"Saved {post['title']}"), "text/html; charset=utf-8")
            return True
        if path in {self.admin_path + "/media", "/api/media"}:
            user = self.current_user(handler) if path.startswith(self.admin_path) else None
            if path.startswith(self.admin_path) and not user:
                self.redirect(handler, "/login")
                return True
            media = self.save_media(data)
            if path == "/api/media":
                self.send_json(handler, 201, media)
            else:
                self.send(handler, 200, self.page_admin(user or {}, f"Added media {media['title']}"), "text/html; charset=utf-8")
            return True
        if path in {"/comments", "/api/comments"}:
            comment = self.save_comment(data)
            if path == "/api/comments":
                self.send_json(handler, 201, comment)
            else:
                self.redirect(handler, f"{self.blog_path}/{comment['post']}")
            return True
        return False

    def handle_data_method(self, handler: BaseHTTPRequestHandler, method: str, data: dict[str, str]) -> bool:
        path = urlparse(handler.path).path.rstrip("/") or "/"
        if not self.middleware_allows(handler, path):
            return True
        if not self.guard_allows(handler, path):
            return True
        if self.handle_store(handler, path, method, data):
            return True
        return self.send_api(handler, path, method, data)

    def save_post(self, data: dict[str, str], user: dict[str, object] | None = None) -> dict[str, object]:
        store = self.load()
        title = data.get("title", "Untitled").strip() or "Untitled"
        slug = slugify(data.get("slug") or title, "post")
        post = {
            "slug": slug,
            "title": title,
            "body": data.get("body", ""),
            "type": data.get("type", "post"),
            "status": data.get("status", "published"),
            "author": str((user or {}).get("display_name") or (user or {}).get("username") or data.get("author", "CPJ")),
            "created_at": now_iso(),
        }
        store["posts"] = [item for item in store.get("posts", []) if item.get("slug") != slug] + [post]
        self.save(store)
        return post

    def save_media(self, data: dict[str, str]) -> dict[str, object]:
        store = self.load()
        title = data.get("title", "Media").strip() or "Media"
        media = {
            "slug": slugify(data.get("slug") or title, "media"),
            "title": title,
            "url": data.get("url", ""),
            "alt": data.get("alt", ""),
            "created_at": now_iso(),
        }
        store["media"] = [item for item in store.get("media", []) if item.get("slug") != media["slug"]] + [media]
        self.save(store)
        return media

    def save_comment(self, data: dict[str, str]) -> dict[str, object]:
        store = self.load()
        comment = {
            "id": secrets.token_hex(8),
            "post": data.get("post", ""),
            "author": data.get("author", "Anonymous"),
            "body": data.get("body", ""),
            "status": "approved",
            "created_at": now_iso(),
        }
        store["comments"] = store.get("comments", []) + [comment]
        self.save(store)
        return comment

    def feed_xml(self) -> str:
        items = "".join(
            f"<item><title>{escape(str(post.get('title', '')))}</title><link>{self.blog_path}/{escape(str(post.get('slug', '')))}</link><description>{escape(str(post.get('body', '')))}</description></item>"
            for post in self.published_posts(include_pages=False)[:20]
        )
        return f'<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel><title>{escape(str(self.config.get("name", "CPJPress")))}</title>{items}</channel></rss>'

    def sitemap_xml(self) -> str:
        urls = ["/", self.blog_path, self.admin_path]
        urls.extend(f"{self.blog_path}/{post.get('slug')}" for post in self.published_posts())
        body = "".join(f"<url><loc>{escape(str(url))}</loc></url>" for url in urls)
        return f'<?xml version="1.0" encoding="utf-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>'

    def make_handler(self):
        site = self

        class Handler(BaseHTTPRequestHandler):
            server_version = "CPJPress/1.0"

            def do_GET(self):
                if not site.handle_get(self):
                    site.send_json(self, 404, {"error": "not_found", "path": urlparse(self.path).path})

            def do_POST(self):
                data = self._read_data()
                if data.get("__invalid_json__"):
                    site.send_json(self, 400, {"error": "invalid_json"})
                    return
                if data.get("__invalid_multipart__"):
                    site.send_json(self, 400, {"error": "invalid_multipart"})
                    return
                if not site.handle_post(self, data):
                    site.send_json(self, 200, {"ok": True, "path": urlparse(self.path).path, "data": data})

            def do_PUT(self):
                self._handle_data_method("PUT")

            def do_PATCH(self):
                self._handle_data_method("PATCH")

            def do_DELETE(self):
                self._handle_data_method("DELETE")

            def do_OPTIONS(self):
                site.send(self, 204, "", "text/plain; charset=utf-8")

            def _read_data(self):
                size = int(self.headers.get("Content-Length", "0") or 0)
                raw_bytes = self.rfile.read(size) if size else b""
                content_type = self.headers.get("Content-Type", "")
                if "multipart/form-data" in content_type:
                    return site.parse_multipart(content_type, raw_bytes)
                raw = raw_bytes.decode("utf-8") if raw_bytes else ""
                if "application/json" in content_type and raw:
                    try:
                        payload = json.loads(raw)
                    except json.JSONDecodeError:
                        return {"__invalid_json__": True}
                    return payload if isinstance(payload, dict) else {"value": payload}
                return {key: values[-1] if values else "" for key, values in parse_qs(raw).items()}

            def _handle_data_method(self, method):
                data = self._read_data()
                if data.get("__invalid_json__"):
                    site.send_json(self, 400, {"error": "invalid_json"})
                    return
                if data.get("__invalid_multipart__"):
                    site.send_json(self, 400, {"error": "invalid_multipart"})
                    return
                if not site.handle_data_method(self, method, data):
                    site.send_json(self, 200, {"ok": True, "path": urlparse(self.path).path, "method": method, "data": data})

            def log_message(self, fmt, *args):
                print("CPJPress", self.address_string(), "-", fmt % args)

        return Handler

    def run(self):
        self.init_stores()
        server = ThreadingHTTPServer((self.host, self.port), self.make_handler())
        print(f"CPJPress running at http://{self.host}:{self.port}")
        server.serve_forever()


def run_site(**kwargs):
    CPJPressSite(**kwargs).run()
