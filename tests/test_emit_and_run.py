import subprocess
import sys
import pathlib


def test_emit_and_run_demo(tmp_path):
    repo = pathlib.Path(__file__).resolve().parent.parent
    binary = repo / 'cpj_compiler'
    assert binary.exists(), "cpj_compiler binary not built"

    out_dir = tmp_path / 'generated'
    out_dir.mkdir()

    # Run the compiler to emit Python into the temporary generated dir
    cmd = [str(binary), '-v', '-o', str(out_dir), 'samples/demo.cpj']
    proc = subprocess.run(cmd, capture_output=True, text=True)
    print(proc.stdout)
    print(proc.stderr, file=sys.stderr)
    assert proc.returncode == 0, f"cpj_compiler failed: {proc.stderr}"

    # Find emitted python file
    emitted = out_dir / 'python' / 'demo.cpj.py'
    assert emitted.exists(), f"Emitted python file not found: {emitted}"

    # Run the emitted python and capture stdout
    proc2 = subprocess.run([sys.executable, str(emitted)], capture_output=True, text=True)
    print(proc2.stdout)
    print(proc2.stderr, file=sys.stderr)
    assert proc2.returncode == 0, f"Emitted python failed: {proc2.stderr}"
    # Expect the demo program to print 12
    assert '12' in proc2.stdout.strip()
