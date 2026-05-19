# CPJ Web Engineering Capability Matrix

CPJ is now a standalone web engineering target. It is not a clone of every
legacy ecosystem, but it now covers both the core end-to-end workflow and the
major framework-level primitives expected from PHP, ASP.NET, JavaScript,
HTML5/CSS, Django, Flask, Figma-style design handoff, and WordPress-style CMS
workflows.

## Current Coverage

| Area | CPJ support | Status |
| --- | --- | --- |
| HTML5 | Semantic sections, headings, links, buttons, images, lists, forms, inputs, selects, textareas | Implemented |
| CSS | Theme tokens, responsive layout, cards, grids, forms, custom single-line CSS | Implemented |
| JavaScript | Embedded CPJ runtime, state, custom events, forms, counters, custom single-line JS | Implemented |
| PHP / ASP-style server pages | Generated dependency-free `server.py` with server-rendered routes, middleware headers, guards, uploads, and SQLite stores | Implemented |
| Flask / Django-style routing | `route "/path" { ... }` and `api "/path" { ... }` blocks | Implemented |
| JSON APIs | Generated method-aware API routes and `openapi.json` | Implemented |
| Forms / POST handling | Browser form runtime, `fetch()` submission, generated server `POST`/`PUT`/`PATCH`/`DELETE` parsing | Implemented |
| Binary uploads | `upload` endpoints with multipart parsing, content-type/size checks, and generated upload storage | Implemented |
| Middleware / auth guards | `middleware` response headers/CORS and token `guard` path protection | Implemented |
| Production middleware pipelines | `pipeline` blocks compose middleware, request IDs, headers, and request header enforcement | Implemented |
| Dependency injection | `service` blocks resolve constants and environment-backed values; APIs can `inject` services | Implemented |
| Components / templates | `component name { ... }`, `template name { slot content }`, `use name`, and `route ... extends template` | Implemented |
| Data models / stores | `model Name { field ... }` metadata and SQLite-backed `store Name { ... }` APIs | Implemented |
| ORM migrations | `migration` blocks add SQLite-backed fields and indexes with `cpj_migrations` tracking | Implemented |
| Figma-style handoff | `design.tokens.json` and `components.json` | Implemented |
| TypeScript-facing bundling | `bundle` blocks emit ESM browser bundles, `.d.ts`, and `tsconfig.json` | Implemented |
| Plugin marketplace | `marketplace` blocks emit plugin registries, hooks, `plugins.marketplace.json`, and `/__cpj/plugins` | Implemented |
| Progressive web app baseline | `pwa "Name"` emits `manifest.webmanifest`, `sw.js`, manifest metadata, and service worker registration | Implemented |
| CSS container/animation syntax | `container` and `animation` blocks emit first-class CSS container queries and keyframes | Implemented |
| Accessibility / SEO diagnostics | `diagnostics.json` reports missing title/description, h1 issues, image alt text, and upload security warnings | Implemented |
| WordPress-style CMS | CPJPress posts, pages, users, sessions, comments, media metadata, plugin records, search, RSS, sitemap, admin UI, and JSON APIs | Implemented |
| Standalone deployment | Static `index.html` or dependency-free Python stdlib server project | Implemented |

## Ecosystem Notes

CPJ now implements the missing ecosystem primitives at a standalone baseline:
SQLite migrations, dependency injection, template inheritance, browser bundling
with TypeScript declarations, plugin marketplace metadata/hooks, and composed
middleware pipelines. It still intentionally avoids claiming compatibility with
the package ecosystems or runtime ABIs of PHP, ASP.NET, Django, Flask, Node, or
WordPress PHP plugins.

## Definition Of "Standalone Web Engineering Language"

For CPJ, standalone means:

- One CPJ source can generate a browser UI, CSS, JavaScript runtime, server
  routes, method-aware JSON APIs, API contracts, PWA files, and design-token
  handoff files.
- The generated server uses only Python's standard library.
- A static-only app can still run as a single HTML file.
- No Node, Flask, Django, ASP.NET, PHP, or external web framework is required
  for the generated baseline project.

## Example

```cpj
web {
    title "CPJ Web Engineering"
    server port 8080

    component stack_badge {
        badge "HTML5 + CSS + JS + API + Design Tokens"
    }

    model Contact {
        field name string required
        field email email required
    }

    api "/api/health" {
        json status "ok"
        json cpj true
    }

    route "/dashboard" {
        h1 "CPJ server route"
        p "Rendered by the generated CPJ server."
    }

    hero {
        use stack_badge
        h1 "Build browser apps in CPJ"
    }
}
```

Generate the full project:

```bash
python -m tools.cpj_web_emitter samples/web_app.cpj \
  -o generated/web/web_app.html \
  --project-dir generated/web/web_app_project
```

Run it:

```bash
python generated/web/web_app_project/server.py
```
