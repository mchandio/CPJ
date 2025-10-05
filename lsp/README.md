CPJ Language Server (scaffold)

This folder contains a minimal pygls-based language server for CPJ. It is a scaffold
for building diagnostics, completion, and other LSP features.

Running locally

1. Create a virtualenv and install dev deps (or use existing `cpj_venv`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the server directly (stdio mode):

```bash
python lsp/server.py
```

3. Connect from an LSP-capable editor (VSCode with a small client) or run tests:

```bash
python -m pytest tests/test_lsp_smoke.py -q
```

Notes

- The server currently emits a trivial diagnostic for non-`.cpj` files and warns on very long lines.
- This is intentionally minimal — next steps are to integrate the ANTLR grammar for real syntax checks,
  add completions, and wire up workspace/document symbols.
