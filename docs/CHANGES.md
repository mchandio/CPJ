Changelog (recent notable edits)

2025-09-15
- Added docs/ with index, getting-started, installation, usage, CLI, language reference, grammar notes, LSP guide, type-mapping (draft), event-model (draft), developer guide, and contributing.
- Updated README.md to link to docs.
- Added LSP scaffold `lsp/server.py` and tests for LSP smoke and ANTLR diagnostics.
- Added requirements (`pygls`, `antlr4-python3-runtime`) and updated pyproject.toml.
- Implemented `--no-run` and `--no-compile` support in `cpj_compiler` and added headless wrapper `cpj_compiler_no_run` previously.
- Created `tests/test_grammar_exists.py`, `tests/test_lsp_smoke.py`, and `tests/test_lsp_antlr_diagnostics.py`.

2025-09-15 (later)
- Redesigned `cpj_compiler.cpp` to improve CLI, add output directory support, safer Java emission/compilation/run, manifest output, and verbose logging.

(For a full list of edits see git history.)
