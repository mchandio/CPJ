import os
import sys
import subprocess


def emit(src, out):
    env = os.environ.copy()
    env['PYTHONPATH'] = os.getcwd()
    r = subprocess.run([sys.executable, 'tools/cpj_emitter.py', src, '-o', out], env=env, capture_output=True, text=True)
    assert r.returncode == 0, f"Emitter failed for {src}: {r.stderr}\n{r.stdout}"


def read(out):
    with open(out, 'r') as f:
        return f.read()


def test_demo_exact(tmp_path):
    src = os.path.join(os.getcwd(), 'samples', 'demo.cpj')
    out = tmp_path / 'demo.cpj.py'
    emit(src, str(out))
    s = read(str(out))
    # expect class HelloWorld with main and top-level add function
    assert 'class HelloWorld:' in s
    assert "def main():" in s
    assert 'def add(a: int, b: int):' in s or 'def add(a, b):' in s
    # top-level invocation of add should be present
    assert 'x = add(5, 7)' in s


def test_hello_exact(tmp_path):
    src = os.path.join(os.getcwd(), 'samples', 'hello.cpj')
    out = tmp_path / 'hello.cpj.py'
    emit(src, str(out))
    s = read(str(out))
    # the print line should be preserved
    assert "print('Hello from CPJ!')" in s or 'print("Hello from CPJ!")' in s


def test_types_demo_exact(tmp_path):
    src = os.path.join(os.getcwd(), 'samples', 'types_demo.cpj')
    out = tmp_path / 'types_demo.cpj.py'
    emit(src, str(out))
    s = read(str(out))
    # types[] parsing should emit widget_types entries
    assert "widget_types['count'] = 'int'" in s
    assert "widget_types['flag'] = 'bool'" in s
    # dict-style types
    assert "widget_types['x'] = 'int'" in s
    assert "widget_types['y'] = 'float'" in s
    # per-field override for c
    assert "widget_types['c'] = 'str'" in s or "# Entry widget placeholder for c" in s
