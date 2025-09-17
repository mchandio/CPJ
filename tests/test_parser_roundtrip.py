import sys
import os
from pathlib import Path
import pytest

# Add generated parser to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = PROJECT_ROOT / "generated" / "grammar"
sys.path.insert(0, str(GENERATED_DIR))

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
try:
    from CPJLexer import CPJLexer
    from CPJParser import CPJParser
except Exception:
    pytest.skip("generated parser not present - skip parser roundtrip tests", allow_module_level=True)

def parse_file(path):
    fs = FileStream(str(path), encoding="utf-8")
    lexer = CPJLexer(fs)
    stream = CommonTokenStream(lexer)
    parser = CPJParser(stream)
    tree = parser.program()
    return tree

def test_parse_types_demo_sample():
    sample = PROJECT_ROOT / "samples" / "types_demo.pre.cpj"
    assert sample.exists(), "Preprocessed sample missing; run grammar/indent_preprocessor.py to generate it"
    tree = parse_file(sample)
    # The parse tree should have at least one child (program rule)
    assert tree.getChildCount() > 0

def test_parse_error_diagnostics():
    # Intentionally malformed input
    from antlr4.error.ErrorListener import ErrorListener
    class CollectingErrorListener(ErrorListener):
        def __init__(self):
            self.errors = []
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            self.errors.append((line, column, msg))
    src = 'GUI { addTextField("x"  addButton("oops") }'  # missing comma/paren
    from antlr4 import InputStream
    lexer = CPJLexer(InputStream(src))
    stream = CommonTokenStream(lexer)
    parser = CPJParser(stream)
    err_listener = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)
    parser.program()
    assert err_listener.errors, "Malformed input should produce syntax errors"
