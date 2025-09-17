import os
from pathlib import Path


def test_grammar_file_exists():
    p = Path('grammar/CPJ.g4')
    assert p.exists(), "grammar/CPJ.g4 must exist"


def test_indent_preprocessor_runs():
    # ensure the indent preprocessor can run on the types_demo sample and produce output
    pre = Path('grammar/indent_preprocessor.py')
    sample = Path('samples/types_demo.cpj')
    assert pre.exists(), "indent_preprocessor.py missing"
    assert sample.exists(), "samples/types_demo.cpj missing"
    out = sample.parent / (sample.stem + '.pre.cpj')
    # run the preprocessor in a subprocess to avoid importing side-effects
    import subprocess
    # the preprocessor expects a filename argument; call it with the sample path
    proc = subprocess.run(["python3", str(pre), str(sample)], capture_output=True, timeout=5)
    stdout = proc.stdout
    assert proc.returncode == 0, f"preprocessor failed: {proc.stderr.decode('utf8', 'replace')}"
    assert stdout, "preprocessor produced no output"
