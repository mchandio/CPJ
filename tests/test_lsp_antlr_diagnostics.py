import pytest
from pathlib import Path


def test_antlr_parser_available():
    # Ensure the generated parser module is present
    gp = Path('generated/grammar/CPJParser.py')
    if not gp.exists():
        pytest.skip('Generated ANTLR parser not found')


def test_lsp_publishes_antlr_diagnostic(monkeypatch):
    # Skip if pygls or antlr runtime not installed
    try:
        import antlr4  # noqa: F401
        import pygls  # noqa: F401
    except Exception:
        pytest.skip('antlr4 or pygls not available')

    # import server and construct a fake DidOpenTextDocumentParams
    from lsp import server
    from lsprotocol.types import TextDocumentItem, DidOpenTextDocumentParams

    # a CPJ input with a clear syntax error (unclosed brace in GUI block)
    text = 'GUI {\n  types {"x":"int"\n  addTextField("x")\n'
    uri = 'file:///' + str(Path('samples/broken.cpj').absolute())
    item = TextDocumentItem(uri=uri, language_id='cpj', version=1, text=text)
    params = DidOpenTextDocumentParams(text_document=item)

    # capture published diagnostics by monkeypatching the server's publish_diagnostics
    published = {}

    def fake_publish(uri_arg, diags):
        published['uri'] = uri_arg
        published['diags'] = diags

    monkeypatch.setattr(server.ls, 'publish_diagnostics', fake_publish)

    server.did_open(server.ls, params)

    assert 'diags' in published
    assert len(published['diags']) >= 1
    # at least one diagnostic should be an error from the parser
    assert any(d.severity == 1 for d in published['diags'])
