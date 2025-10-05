import os
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
# generated/grammar is where the ANTLR Python runtime files are placed
GENERATED_DIR = PROJECT_ROOT / "generated" / "grammar"
sys.path.insert(0, str(GENERATED_DIR))

from antlr4 import FileStream, CommonTokenStream

try:
    from CPJLexer import CPJLexer
except Exception:
    pytest.skip("generated parser not present - skip tokenization tests", allow_module_level=True)


def test_show_call_tokenized_in_sample():
    pre = PROJECT_ROOT / "samples" / "types_demo.pre.cpj"
    assert pre.exists(), "Preprocessed sample missing; run grammar/indent_preprocessor.py to generate it"

    fs = FileStream(str(pre), encoding="utf-8")
    lexer = CPJLexer(fs)
    stream = CommonTokenStream(lexer)
    stream.fill()

    # Look for at least one sequence Identifier '(' ')', e.g. show()
    types = [ (t.type, t.text) for t in stream.tokens ]

    import re

    # Check INDENT/DEDENT markers exist (be tolerant: either token type or raw text)
    has_indent = any((getattr(CPJLexer, 'INDENT', None) == t.type) or ('<INDENT>' in (t.text or '')) for t in stream.tokens)
    has_dedent = any((getattr(CPJLexer, 'DEDENT', None) == t.type) or ('<DEDENT>' in (t.text or '')) for t in stream.tokens)
    assert has_indent, 'INDENT token not produced by preprocessor/lexer'
    assert has_dedent, 'DEDENT token not produced by preprocessor/lexer'

    # Check a bare call like show() tokenization exists by looking for an identifier-like
    # token text followed by literal '(' and ')'. We avoid relying on symbolicNames which
    # may be unreliable in some generated files during tests.
    ident_re = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
    found = False
    for i in range(len(stream.tokens)-2):
        t0 = stream.tokens[i]
        t1 = stream.tokens[i+1]
        t2 = stream.tokens[i+2]
        t0text = (t0.text or '').strip()
        if ident_re.match(t0text) and (t1.text == '(') and (t2.text == ')'):
            found = True
            break

    assert found, 'No bare call token sequence Identifier ( ) found in tokens (e.g. show())'
