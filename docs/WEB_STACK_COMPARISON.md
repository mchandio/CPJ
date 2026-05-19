# CPJ Web Stack Comparison

This audit compares CPJ's standalone web target with the major web engineering
families it is meant to cover: PHP, ASP.NET, JavaScript, Python web frameworks,
HTML5, CSS, and design handoff tools.

## Comparison

| Stack | Strong native surface | CPJ equivalent now | Remaining CPJ gap |
| --- | --- | --- | --- |
| PHP | Server-rendered pages, forms, sessions, uploads, simple deployment | Generated `server.py`, CPJPress sessions/login, form parsing, guarded multipart uploads, CMS storage | PHP compatibility, package ecosystem, upload progress |
| ASP.NET / ASPX | Routing, middleware, DI, controllers/pages, auth | `route`, method-aware `api`, generated server, middleware headers/CORS, token guards, CPJPress auth baseline | DI container, compiled controller model, full middleware composition |
| JavaScript | DOM, events, fetch, modules, PWA/service workers | Embedded `window.CPJ`, events, counters, form fetch, generated PWA files | Module bundling, TypeScript-grade typing, client router |
| Python / Flask / Django | Routing, templates, models, admin, auth, migrations | Dependency-free server, routes/APIs, models metadata, SQLite-backed stores, CPJPress admin | ORM relationships, migrations, template inheritance, production middleware |
| HTML5 | Semantic document structure, forms, media, metadata | Sections, nav, headings, forms, inputs, textareas, images, manifest metadata | Rich media primitives, accessibility linting |
| CSS | Responsive layouts, variables, media/container queries, animation | Theme tokens, responsive grid/cards/forms, custom CSS lines, first-class `container` and `animation` blocks | Preprocessor mixins/functions and advanced cascade tooling |
| Figma / design systems | Tokens, components, reusable UI inventory | `design.tokens.json`, `components.json`, theme metadata | Figma API sync and editable canvas import/export |

## Implemented From This Audit

- Method-aware API dispatch for generated servers.
- Form endpoint syntax with generated browser `fetch()` submission.
- PWA baseline through `pwa "Name"`, `manifest.webmanifest`, and `sw.js`.
- Binary `upload` endpoints with multipart parsing and size/content-type checks.
- Token `guard` blocks and `middleware` response headers/CORS.
- SQLite-backed `store` blocks.
- First-class `container` and `animation` CSS blocks.
- `diagnostics.json` for accessibility, SEO, and security warnings.

## Next Best CPJ Additions

1. Upload progress, streaming, and image transforms.
2. Full middleware chaining with request/response transforms.
3. Relational store declarations, indexes, migrations, and query syntax.
4. Theme modes, CSS layers, and reusable style mixins.
5. Browser-run accessibility audits in addition to generated static diagnostics.
