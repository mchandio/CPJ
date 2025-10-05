Developer Guide

This guide helps contributors understand the codebase and extend CPJ.

Repo layout (high-level)

- `cpj_compiler.cpp`, `cpj_cpp/`, `cpp/`: C++ compiler core and helpers
- `grammar/`: ANTLR grammar and helpers
- `generated/grammar/`: generated ANTLR parser files (Python)
- `python/` and `java/`: codegen backends and runtime integration
- `lsp/`: language server scaffold
- `tests/`: pytest suite
- `samples/`: CPJ example programs

Common tasks

- Run tests:

```bash
python -m pytest -q
```

- Build compiler:

```bash
make clean && make
```

Extending the grammar

1. Update `grammar/CPJ.g4`
2. Regenerate parser with ANTLR:

```bash
java -jar grammar/antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated/grammar grammar/CPJ.g4
```

3. Run tests and adjust emitter or parser-driven code as needed.

Adding an LSP feature

- Update `lsp/server.py` to include handlers for the feature (completion/documentSymbols/etc.)
- Add tests under `tests/` that cover server behavior (they should skip gracefully if `pygls` isn't installed)

Testing and CI

- CI runs pytest via `.github/workflows/python-tests.yml` which installs `requirements.txt` and runs tests.
- For full LSP tests, ensure `pygls` is installed in the runner.
