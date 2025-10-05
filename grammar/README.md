CPJ grammar directory
=====================

This folder contains an initial ANTLR4 grammar draft `CPJ.g4` that models the current CPJ syntax surface used by the emitter and tests.

Scope of this draft
- GUI blocks (`gui Name:` with an indented body)
- `types` declarations (token-style and dict-style)
- Widget statements: `addTextField`, `addButton`, `addCheckBox`, `addSlider`
- Expressions including dotted identifiers, function calls, literals, and basic operators

Next steps
- Replace the placeholder INDENT/DEDENT tokens with a proper indentation handling strategy:
  - Either reuse the Python ANTLR approach (a preprocessor that emits INDENT/DEDENT tokens),
  - Or move GUI blocks to explicit `{}` braces in the language to avoid indentation sensitivity.
- Add missing statements and full CPJ constructs (classes, imports, connectors) as needed.
- Map the current recursive-descent parser tests to the grammar and iterate until parity.

Indentation preprocessor
- A helper script `indent_preprocessor.py` is included to convert indentation into literal
  `<INDENT>` and `<DEDENT>` markers which the draft grammar currently expects. This is
  useful for prototyping parser generation without migrating to a full-fledged indentation lexer.

Usage
- Preprocess a CPJ file:

```bash
python3 grammar/indent_preprocessor.py samples/types_demo.cpj > samples/types_demo.pre.cpj
```

- The resulting file will contain `<INDENT>` and `<DEDENT>` markers. You can then feed
  that file to a generated parser which uses the placeholder tokens.

Generating parsers
- To generate a parser using ANTLR4 (once INDENT/DEDENT are handled):
  - Install Java (required to run the ANTLR jar).
  - Download the ANTLR4 complete jar from https://www.antlr.org/download.html and place it at `grammar/antlr-4.12.0-complete.jar`.
  - Run the helper script to generate a Python3 parser:

```bash
chmod +x grammar/generate_parser.sh
./grammar/generate_parser.sh grammar/antlr-4.12.0-complete.jar generated
```

- After that, add the `generated` directory to `PYTHONPATH` or move generated files into your toolchain.

This is a working draft intended to speed up migration to a generator-based parser. It is not yet a drop-in replacement for the existing parser; treat it as a reference and starting point.
