import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def run_and_get_ns(src):
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    return ns


def test_int_annotation_coercion():
    src = '''def show(n):\n    print(type(n), n)\n\nGUI {\n    addTextField("count", "int")\n    addButton("Go", show(count))\n    show()\n}\n'''
    ns = run_and_get_ns(src)
    ns['widgets']['count'].set('42')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()


def test_bool_annotation_coercion():
    src = '''def setflag(f):\n    print(type(f), f)\n\nGUI {\n    addTextField('flag', 'bool')\n    addButton('Toggle', setflag(flag))\n    show()\n}\n'''
    ns = run_and_get_ns(src)
    ns['widgets']['flag'].set('true')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
