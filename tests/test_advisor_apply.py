import json
import subprocess
import sys
import os


def test_advisor_apply_creates_backups(tmp_path):
    # run advisor in a temporary copy of the repo root
    repo_root = tmp_path / 'repo'
    os.makedirs(repo_root, exist_ok=True)
    # create minimal files
    (repo_root / 'requirements.txt').write_text('astroid\n')
    (repo_root / 'pyproject.toml').write_text('[project]\nname = "cpj"\ndependencies = [\n]\n')
    (repo_root / 'Makefile').write_text('all:\n\t@echo build\n')

    cmd = [sys.executable, str(os.path.join(os.getcwd(), 'tools', 'cpj_advisor.py')), '--feature', 'lsp', '--apply', '--root', str(repo_root), '--json']
    p = subprocess.run(cmd, capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    # Check backups
    assert (repo_root / 'requirements.txt.bak').exists()
    assert (repo_root / 'pyproject.toml.bak').exists()
    assert (repo_root / 'Makefile.bak').exists()
    # Check lib dir
    assert (repo_root / 'lib').exists()
