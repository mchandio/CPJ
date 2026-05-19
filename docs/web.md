# CPJ Standalone Web Target

CPJ can emit standalone browser applications from `web { ... }` blocks. The
web target produces a single HTML file with embedded CSS and JavaScript, so the
output can be opened directly in a browser without Node, a bundler, a web
server, or a CDN. It can also emit a dependency-free server project with
server-rendered routes, JSON APIs, OpenAPI metadata, and Figma-style design
tokens.

## Quick Start

Generate the sample web app:

```bash
python -m tools.cpj_web_emitter samples/web_app.cpj -o generated/web/web_app.html
```

Generate the full standalone project:

```bash
python -m tools.cpj_web_emitter samples/web_app.cpj \
  -o generated/web/web_app.html \
  --project-dir generated/web/web_app_project
```

Or emit it through the CPJ compiler:

```bash
./cpj_compiler --web-only -o generated samples/web_app.cpj
```

Open `generated/web/web_app.cpj.html` when using `cpj_compiler`, or
`generated/web/web_app.html` when using the Python emitter directly.

## Web Block Syntax

```cpj
web {
    title "CPJ Web Engineering"
    meta description "A standalone CPJ web application."
    pwa "CPJ Web Engineering"
    theme primary "#2457c5"
    theme accent "#b25519"

    nav "Home" "#hero"

    hero {
        badge "Standalone Web Target"
        h1 "Build browser apps in CPJ"
        p "Describe web interfaces and emit one browser-ready file."
        button "Explore" -> "#features"
    }

    section features {
        h2 "Language-level web primitives"
        grid {
            card "Single-file output" "No external runtime is required."
            card "Structured UI" "Sections, cards, forms, and fields compile to HTML."
        }
    }
}
```

Supported statements include `title`, `meta description`, `pwa`, `theme`, `server`,
`state`, `css`, `js`, `html`, `nav`, `h1` through `h4`, `p`, `small`, `badge`,
`button`, `link`, `image`, `card`, `input`, `textarea`, `select`, `list`, and
`counter`.

Supported blocks include `hero`, `section`, `grid`, `card`, `form`,
`component`, `template`, `route`, `api`, `model`, `store`, `upload`,
`middleware`, `guard`, `container`, `animation`, `cms`, `header`, `main`,
`footer`, `aside`, and `nav`.

## Full Project Output

When `--project-dir` is used, CPJ emits:

- `index.html` - standalone browser UI
- `server.py` - PHP/ASP/Flask/Django-style local routes and APIs using only the
  Python standard library
- `openapi.json` - API contract for generated JSON routes
- `design.tokens.json` - Figma-style token handoff
- `components.json` - component, route, and API inventory
- `diagnostics.json` - accessibility, SEO, and security diagnostics
- `README.md` - run instructions for the generated project
- `manifest.webmanifest` and `sw.js` when `pwa "Name"` is declared

When a `cms { ... }` block is present, CPJ also emits `cpjpress_runtime.py`,
JSON content storage, login/session support, comments, media metadata, plugin
records, search, feeds, sitemap, admin screens, and WordPress-style JSON APIs.
See `docs/CPJPRESS.md`.

Forms can submit directly to generated APIs:

```cpj
api "/api/contact" {
    method POST
    json status "received"
}

form contact -> "/api/contact" POST {
    input email "Email" email required
    textarea message "Message" required
    button "Send"
}
```

SQLite stores are declared with `store` blocks and are exposed at
`/api/store/<name>`:

```cpj
store Lead {
    field name text required
    field email text required
    seed name "Ada" email "ada@example.com"
}
```

Binary upload endpoints are declared with `upload` blocks. Use `guard` for
token protection and `multipart` on forms that submit files:

```cpj
guard upload_token {
    path "/api/uploads/media"
    token "dev-token"
}

upload media {
    path "/api/uploads/media"
    dir "uploads/media"
    accept "image/png,image/jpeg"
    max-bytes 5242880
}

form media -> "/api/uploads/media" POST multipart {
    input file "File" file required accept "image/png,image/jpeg"
    button "Upload"
}
```

Middleware and first-class CSS engineering primitives:

```cpj
middleware security {
    header "X-Content-Type-Options" "nosniff"
    cors "*"
}

container cards {
    selector ".cpj-card"
    min-width "360px"
    css ".cpj-card { border-color: var(--cpj-primary); }"
}

animation rise_in {
    duration "360ms"
    from "opacity: 0; transform: translateY(10px);"
    to "opacity: 1; transform: translateY(0);"
    apply ".cpj-card"
}
```

## Runtime

Generated pages include a small `window.CPJ` runtime:

- `CPJ.state` stores values declared with `state name value`.
- `CPJ.event(name, detail)` dispatches browser `CustomEvent`s named
  `cpj:<name>`.
- Forms dispatch `cpj:form-submit`; forms with an endpoint also submit with
  `fetch()` and dispatch `cpj:form-response` or `cpj:form-error`.
- Counters dispatch `cpj:counter-change`.
- PWA-enabled pages register the generated `sw.js` service worker.
- Upload forms submit `FormData` instead of JSON.

This keeps the first web target fully standalone while leaving a clean hook for
future HTTP, routing, component, and server-side backends.

See `docs/WEB_ENGINEERING_MATRIX.md` for the detailed capability matrix and
remaining roadmap items.
