import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser
from tools.cpj_emitter import Emitter


def test_emitter_runs_sample(tmp_path, capsys):
    sample = tmp_path / 'sample.cpj'
    sample.write_text('''print("Hello from emitted code")\n\ndef add(a, b):\n    return a + b\n''')
    p = Parser(str(sample))
    ast = p.parse()
    em = Emitter()
    em.emit(ast)
    src = em.to_source()
    # execute the generated code and capture output
    ns = {}
    exec(src, ns, ns)
    # Now call add
    assert ns['add'](2,3) == 5
