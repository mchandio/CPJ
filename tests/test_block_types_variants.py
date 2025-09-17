import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def run_and_ns(src):
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    return ns, src_py


def test_token_style_types_and_override():
    src = '''GUI {
    types a:int b:bool
    addTextField("a")
    addTextField("b")
    addTextField("c", "float")
    addButton("Do", show(a, b, c))
    show()
}
'''
    ns, src_py = run_and_ns(src)
    # block-level should have set types for a and b; c has per-field override
    assert "widget_types['a']" in src_py
    assert "widget_types['b']" in src_py
    assert "widget_types['c']" in src_py


def test_multiline_dict_types():
    src = '''GUI {
    types {
        "x": "int",
        'y': 'float'
    }
    addTextField("x")
    addTextField("y")
    addButton("Do", show(x, y))
    show()
}
'''
    ns, src_py = run_and_ns(src)
    assert "widget_types['x']" in src_py
    assert "widget_types['y']" in src_py


def test_invalid_entries_emit_diagnostics():
    src = '''GUI {
    types { 123: 'int', z: 999 }
    addTextField("z")
    addButton("Do", show(z))
    show()
}
'''
    ns, src_py = run_and_ns(src)
    # should include diagnostic comments about ignored entries
    assert '# types:' in src_py
