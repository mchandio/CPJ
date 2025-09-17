import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def test_gui_emitter_contains_tkinter(tmp_path):
    src = '''GUI {
    addLabel("Title")
    addTextField("name")
    addButton("Say Hi")
    show()
}
'''
    p = Parser(src)
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src = em.to_source()
    assert 'import tkinter' in src
    assert 'Button' in src or 'btn0' in src
    # ensure the runtime invoke helper is referenced in emitted code
    assert 'invoke_or_emit_event' in src
