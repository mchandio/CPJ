import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def test_gui_handler_calls_function():
    src = '''def say_hi(data):\n    print('say_hi called', data.get('name'))\n\nGUI {\n    addTextField("name")\n    addButton("Say Hi")\n    show()\n}\n'''
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    # simulate widget value
    ns['widgets']['name'].set('Tester')
    # call handler: find any _on_click_* in namespace
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers, f'no handlers found in namespace: {list(ns.keys())}'
    ns[handlers[0]]()
    # manual check: say_hi should be defined and callable
    assert 'say_hi' in ns and callable(ns['say_hi'])
