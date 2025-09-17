import os
import sys
import subprocess


def test_emitter_smoke(tmp_path, monkeypatch):
    # use sys.executable so test uses same python interpreter (venv in CI)
    py = sys.executable
    src = os.path.join(os.getcwd(), 'samples', 'demo.cpj')
    out = tmp_path / 'demo.cpj.py'

    env = os.environ.copy()
    # make sure 'tools' package is importable by the emitter
    env['PYTHONPATH'] = os.getcwd()

    # run the emitter
    r = subprocess.run([py, 'tools/cpj_emitter.py', src, '-o', str(out)], env=env, capture_output=True, text=True)
    assert r.returncode == 0, f"Emitter failed: {r.stderr}\n{r.stdout}"
    assert out.exists(), "Emitter did not create output file"

    # run the generated program and capture stdout
    r2 = subprocess.run([py, str(out)], capture_output=True, text=True, env=env)
    assert r2.returncode == 0, f"Generated program failed: {r2.stderr}\n{r2.stdout}"
    # demo.cpj prints 12 (from add(5,7)) and also prints Hello, CPJ World!
    assert '12' in r2.stdout.strip() or 'Hello, CPJ World!' in r2.stdout, f"Unexpected output: {r2.stdout}"
