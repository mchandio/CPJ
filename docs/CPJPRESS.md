# CPJPress

CPJPress is a CPJ-native, WordPress-style CMS baseline. It is not a PHP
WordPress port. Instead, it brings the essential publishing architecture into
CPJ so one `.cpj` file can generate a standalone CMS project.

## Why Not A Direct WordPress Port?

The local WordPress archive includes the expected PHP application structure:
entrypoints like `index.php`, `wp-login.php`, `wp-settings.php`, `xmlrpc.php`,
and a `wp-content` tree with themes, templates, patterns, assets, and
`theme.json` files. Recreating that entire ecosystem would require a PHP
runtime, database layer, plugin API, admin system, auth, migrations, and years
of compatibility behavior.

CPJPress takes the practical path: it implements the core web engineering
capabilities in CPJ-native generated artifacts.

## CPJ Syntax

```cpj
web {
    title "CPJPress"
    server port 8090
    pwa "CPJPress"

    cms CPJPress {
        site "CPJPress"
        blog "/blog"
        admin "/admin"
        storage "cpjpress_content.json"
        category "Announcements"
        user admin admin admin "Administrator"
        plugin seo "SEO Helper" "Adds metadata hooks."
        media hero "Hero" "/static/hero.png" "Hero image"
        post "hello" "Hello CPJPress" "This is a CPJ CMS post."
        page "about" "About CPJPress" "A CPJ-native CMS baseline."
        comment "hello" "First Reader" "This is generated from CPJ."
    }

    hero {
        h1 "WordPress-style publishing in CPJ"
        button "View Posts" -> "/blog"
        button "Open Admin" -> "/admin"
    }
}
```

## Generated CMS Features

- Blog index at `/blog`
- Single post pages at `/blog/<slug>`
- Login at `/login` and logout at `/logout`
- Session-protected admin publishing form at `/admin`
- Admin post creation at `/admin/post`
- JSON post list at `/api/posts`
- JSON single post at `/api/posts/<slug>`
- JSON comments at `/api/comments`
- JSON media metadata at `/api/media`
- JSON plugin metadata at `/api/plugins`
- Public comments through `/comments`
- Search at `/search`
- RSS feed at `/feed.xml`
- XML sitemap at `/sitemap.xml`
- PWA manifest and service worker when `pwa "Name"` is present
- Shared CPJ web primitives such as `middleware`, `guard`, `store`, `upload`,
  `container`, `animation`, and `diagnostics.json`
- JSON content persistence, defaulting to `cpjpress_content.json`
- OpenAPI entries for CMS APIs
- Design-token and component inventory metadata

The generated sample seeds `admin` / `admin` as the default login unless a
different `user` directive is provided.

## Generate And Run

```bash
python -m tools.cpj_web_emitter samples/cpjpress.cpj \
  -o generated/web/cpjpress.html \
  --project-dir generated/web/cpjpress_project
```

```bash
python generated/web/cpjpress_project/server.py
```

Open:

```text
http://127.0.0.1:8090
```

## Honest Scope

CPJPress makes CPJ a standalone CMS-capable web engineering language baseline.
It does not yet include full WordPress compatibility, themes/plugins marketplace
support, binary media upload streaming, multisite, database migrations,
production-grade permissions, CSRF protection, or the WordPress PHP plugin API.
Those are roadmap items built on top of this CMS foundation.
