CPJ Project Status
==================

As of 2025-09-15 — concise project status.

Completed
---------
- Core parser and emitter (recursive-descent) with comprehensive pytest suite.
- ANTLR grammar draft (`grammar/CPJ.g4`) and generated parser under `generated/grammar/` used by tests.
- Runtime helpers in `cpj_runtime.py` and Python emitter in `tools/cpj_emitter.py`.
- Java Swing codegen for GUI blocks and a working `cpj_compiler` prototype with `--no-run` and `--no-compile`.
- Headless testing support and CI workflow for Python tests.
- LSP scaffold (`lsp/server.py`) wired to ANTLR-generated parser when available.
- Documentation site under `docs/` with getting-started, developer guide, grammar notes, and drafts for type-mapping and event model.

Pending / In-progress
---------------------
- Formalize and finalize ANTLR grammar and add CI regeneration step (not yet automated).
- Implement optional/static type checker for GUI blocks and handler signatures (draft doc exists).
- Formalize event model and connector robustness for cross-runtime handlers.
- Design an internal IR and prototype a native backend for `@native` functions.
- Expand LSP features beyond syntax diagnostics (completion, document symbols) and enable LSP tests in CI.

Next steps (recommended order)
-----------------------------
1. Finalize ANTLR grammar and add CI step to regenerate and validate generated parser files. (2-4d)
2. Implement GUI-block static type-checker and tests. (2-5d)
3. Harden event model and connector tests. (3-7d)
4. Expand LSP and enable `pygls` in CI. (3-7d)
5. Design IR and prototype native backend for a small subset. (7-20d)

See `docs/CHANGES.md` for a changelog of recent repository edits.
