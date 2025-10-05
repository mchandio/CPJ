Grammar & ANTLR

The repository contains an ANTLR grammar at `grammar/CPJ.g4`. A generated Python parser is included under `generated/grammar` to allow runtime parsing in tests and tooling.

Regenerating the parser

If you update `grammar/CPJ.g4`, regenerate the parser with the ANTLR jar bundled in `grammar/`:

```bash
# from repo root
java -jar grammar/antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated/grammar grammar/CPJ.g4
```

Notes

- The grammar currently expects the indent preprocessor to run before feeding text into ANTLR; use `grammar/indent_preprocessor.py` to convert indentation into explicit INDENT/DEDENT tokens used by the grammar and tests.
- See `docs/grammar_plan.md` for the roadmap to improving the grammar and migrating the parser.
