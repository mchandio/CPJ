import subprocess
import sys
import os


def test_cpj_compiler_runs_on_types_demo():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Prefer a no-run wrapper if present (keeps tests fast and non-interactive)
    exe = os.path.join(repo_root, 'cpj_compiler_no_run')
    if not os.path.exists(exe):
        exe = os.path.join(repo_root, 'cpj_compiler')
    sample = os.path.join(repo_root, 'samples', 'types_demo.cpj')
    assert os.path.exists(exe), f"cpj_compiler not found at {exe}"
    assert os.path.exists(sample), f"sample not found at {sample}"
    # run the compiler on the sample; it should exit quickly and not crash
    p = subprocess.run([exe, sample], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
    out = p.stdout.decode('utf-8', errors='replace')
    err = p.stderr.decode('utf-8', errors='replace')
    assert p.returncode == 0, f"cpj_compiler failed (rc={p.returncode})\nSTDOUT:\n{out}\nSTDERR:\n{err}" 
