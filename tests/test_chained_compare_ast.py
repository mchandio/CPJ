import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser, Compare


def test_chained_compare_ast_structure():
    src = 'x = a < b < c'
    p = Parser(src)
    mod = p.parse()
    # find the assign node
    assigns = [n for n in mod.items if getattr(n, '__class__').__name__ == 'Assign']
    assert assigns, 'no assign'
    assign = assigns[0]
    cmp = assign.expr
    assert isinstance(cmp, Compare), f'expected Compare, got {type(cmp)}'
    # should have two ops and two comparators for a < b < c
    assert len(cmp.ops) == 2
    assert len(cmp.comparators) == 2
    assert cmp.ops[0] == '<' and cmp.ops[1] == '<'
