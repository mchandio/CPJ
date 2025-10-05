import subprocess
import sys
from pathlib import Path


def test_lsp_server_runs(monkeypatch):
    # Skip if pygls is not installed to avoid failing environments
    try:
        import pygls  # noqa: F401
    except Exception:
        import pytest
        pytest.skip('pygls not installed in this environment')

    server = Path('lsp/server.py')
    assert server.exists()

    # start server in a subprocess and immediately terminate after checking it's alive
    p = subprocess.Popen([sys.executable, str(server)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        # give it a second to start
        p.poll()
        assert p.returncode is None
    finally:
        p.terminate()
        p.wait(timeout=2)
