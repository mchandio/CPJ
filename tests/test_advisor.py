import json
import subprocess
import sys


def run_advisor_json():
    cmd = [sys.executable, 'tools/cpj_advisor.py', '--json']
    p = subprocess.run(cmd, capture_output=True, text=True)
    assert p.returncode == 0
    return json.loads(p.stdout)


def test_advisor_runs_and_outputs_json():
    out = run_advisor_json()
    assert 'detected_features' in out
    assert 'choice' in out
    # expect choices for each language
    assert set(out['choice'].keys()) == {'cpp', 'python', 'java'}
