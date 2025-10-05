import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def emit_and_run(src):
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    return ns


def test_unary_minus_in_handler_arg():
    src = """def show(v):
    print('val', v)

GUI {
    addTextField('n')
    addButton('Do', show(-n))
    show()
}
"""
    ns = emit_and_run(src)
    ns['widgets']['n'].set('3')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()


def test_comparison_and_boolean():
    src = """def check(x,y):
    print('ok', x, y)

GUI {
    addTextField('a')
    addTextField('b')
    addButton('Test', check(a == b, a < b or a > b))
    show()
}
"""
    ns = emit_and_run(src)
    ns['widgets']['a'].set('1')
    ns['widgets']['b'].set('2')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
