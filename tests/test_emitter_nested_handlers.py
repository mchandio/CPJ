import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def run_and_capture(src):
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    return ns


def test_handler_with_binop_arg():
    src = '''def show_sum(x):\n    print('sum', x)\n\nGUI {\n    addTextField("a")\n    addTextField("b")\n    addButton("Sum", show_sum(a + b))\n    show()\n}\n'''
    ns = run_and_capture(src)
    # set widget values
    ns['widgets']['a'].set('2')
    ns['widgets']['b'].set('3')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()


def test_handler_with_nested_call_arg():
    src = '''def inner(x):\n    return int(x) * 2\n\ndef outer(v):\n    print('outer', v)\n\nGUI {\n    addTextField("val")\n    addButton("DoIt", outer(inner(val)))\n    show()\n}\n'''
    ns = run_and_capture(src)
    ns['widgets']['val'].set('5')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
