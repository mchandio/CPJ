import subprocess
import pathlib
import sys


def test_types_demo_emits_and_runs(tmp_path):
    repo = pathlib.Path(__file__).resolve().parent.parent
    binary = repo / 'cpj_compiler'
    assert binary.exists()

    out_dir = tmp_path / 'generated'
    out_dir.mkdir()
    cmd = [str(binary), '-v', '-o', str(out_dir), 'samples/types_demo.cpj']
    proc = subprocess.run(cmd, capture_output=True, text=True)
    print(proc.stdout)
    print(proc.stderr, file=sys.stderr)
    assert proc.returncode == 0

    emitted = out_dir / 'python' / 'types_demo.cpj.py'
    assert emitted.exists(), f"Emitted file not found: {emitted}"

    content = emitted.read_text()
    assert "widget_types" in content or "widget_types" in content
    assert "def _on_click_" in content or "def _on_click_" in content

    # execute the emitted python
    proc2 = subprocess.run([sys.executable, str(emitted)], capture_output=True, text=True)
    print(proc2.stdout)
    print(proc2.stderr, file=sys.stderr)
    assert proc2.returncode == 0
