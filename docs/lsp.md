LSP & Editor Integration

The project includes a minimal pygls-based language server at `lsp/server.py`.

Features

- Basic diagnostics using the generated ANTLR parser (when available).
- Skeleton handlers for `textDocument/didOpen` and `textDocument/didChange`.

Running locally

```bash
pip install -r requirements.txt
python lsp/server.py
```

Testing

- `tests/test_lsp_smoke.py` — ensures the server starts (skips if `pygls` missing)
- `tests/test_lsp_antlr_diagnostics.py` — ensures parser diagnostics are produced (skips if generated parser or `pygls` missing)

Next steps

- Map parser errors to more precise ranges and messages.
- Provide completions and document symbols from the parse tree.
- Add a small VSCode client to launch the server in stdio mode for local dev.
