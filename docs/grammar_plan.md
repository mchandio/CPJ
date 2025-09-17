CPJ grammar plan (short-term)

Goal: produce a first-pass ANTLR4 grammar that fully captures the v0.1 language subset used by the existing
recursive-descent parser and tests. This will enable generated parsers, syntax highlighting, and easier
language evolution.

Short-term scope (2-4 days):
- Converge the `grammar/CPJ.g4` file to cover:
  - module-level statements: function defs, GUI blocks, imports (if present), and top-level expressions
  - GUI block forms (both `GUI { ... }` and `GUI:` indented form)
  - widget calls: addTextField, addButton, addCheckBox, addSlider (args can be string literals or expressions)
  - `types` support: token-style `types a:int b:bool` and dict-style `types {"x":"int"}`
  - expressions with dotted names, calls, literals, and basic operators (the current parser grammar is a reference)
- Add `tests/test_grammar_parsing.py` with a couple of smoke parses using `antlr4-python3-runtime` to ensure the grammar compiles.

Acceptance criteria:
- `grammar/CPJ.g4` builds with ANTLR4 and `python -m antlr4` (CI will validate using `antlr4-python3-runtime`).
- Existing tests continue to pass; the grammar file is present and referenced by a new lightweight test that checks its presence.

Notes:
- This is an iterative process; the initial grammar will be conservative and mirror the current parser behavior.
- The ANTLR tokenization of indentation will use the existing `grammar/indent_preprocessor.py` which emits explicit INDENT/DEDENT markers for now.
