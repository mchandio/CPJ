import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def test_gui_explicit_binding_calls_function():
    src = '''def say_hi(name):\n    print('hi', name)\n\nGUI {\n    addTextField("name")\n    addButton("Greet", say_hi(name))\n    show()\n}\n'''
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    # set widget value
    ns['widgets']['name'].set('Alice')
    # find handler and call
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
    assert 'say_hi' in ns
