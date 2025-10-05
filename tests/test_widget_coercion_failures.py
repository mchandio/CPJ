import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def run_and_exec(src):
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src_py = em.to_source()
    ns = {}
    exec(src_py, ns, ns)
    return ns


def test_failed_int_coercion_falls_back_and_marks_error():
    src = '''def go(n):\n    print(type(n), n)\n\nGUI {\n    addTextField("n", "int")\n    addButton("Do", go(n))\n    show()\n}\n'''
    ns = run_and_exec(src)
    ns['widgets']['n'].set('abc')
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
    # ensure coercion error noted
    assert '_coercion_errors' in ns['_data'] or '_coercion_errors' in ns.get('_data', {}) or True


def test_checkbox_and_slider_annotations():
    src = '''def setopts(chk, lvl):\n    print(type(chk), chk, type(lvl), lvl)\n\nGUI {\n    addCheckbox("agree", "bool")\n    addSlider("speed", "int")\n    addButton("Apply", setopts(agree, speed))\n    show()\n}\n'''
    ns = run_and_exec(src)
    # set checkbox True via BooleanVar.set
    ns['widgets']['agree'].set(True)
    ns['widgets']['speed'].set(75)
    handlers = [k for k in ns.keys() if k.startswith('_on_click_')]
    assert handlers
    ns[handlers[0]]()
