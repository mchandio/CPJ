from pygls.server import LanguageServer
from lsprotocol.types import (
    TEXT_DOCUMENT_DID_OPEN, TEXT_DOCUMENT_DID_CHANGE, TEXT_DOCUMENT_COMPLETION, TEXT_DOCUMENT_DOCUMENT_SYMBOL, TEXT_DOCUMENT_DEFINITION,
    DidOpenTextDocumentParams, DidChangeTextDocumentParams,
    Diagnostic, DiagnosticSeverity, Range, Position,
    CompletionItem, CompletionList, CompletionItemKind, CompletionParams,
    DocumentSymbol, SymbolKind, DocumentSymbolParams,
    Location, TextDocumentPositionParams
)


# --- Language Server Class/Instance ---
class CPJLanguageServer(LanguageServer):
    CMD_SHOW = 'cpj.show'

ls = CPJLanguageServer('cpj-ls', '1.0.0')

import logging
LOGGER = logging.getLogger(__name__)
@ls.feature(TEXT_DOCUMENT_DEFINITION)
def goto_definition(ls: CPJLanguageServer, params: TextDocumentPositionParams):
    uri = params.text_document.uri
    pos = params.position
    text = None
    if uri and uri in ls.workspace.documents:
        text = ls.workspace.documents[uri].source
    if not text:
        return None
    import re
    lines = text.splitlines()
    word = None
    # Find word at cursor
    if 0 <= pos.line < len(lines):
        line = lines[pos.line]
        idx = pos.character
        # Expand left/right to get word
        left = idx
        while left > 0 and (line[left-1].isalnum() or line[left-1] == '_'):
            left -= 1
        right = idx
        while right < len(line) and (line[right].isalnum() or line[right] == '_'):
            right += 1
        word = line[left:right]
    if not word:
        return None
    # Search for function or variable definition
    for i, l in enumerate(lines):
        if re.match(rf'\s*def\s+{re.escape(word)}\b', l):
            return Location(uri=uri, range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(l))))
        if re.match(rf'\s*class\s+{re.escape(word)}\b', l):
            return Location(uri=uri, range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(l))))
        # Widget/variable: look for addTextField/addButton/etc
        if re.search(rf'add(?:TextField|Button|CheckBox|Slider)\(["\\']{re.escape(word)}["\\']', l):
            return Location(uri=uri, range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(l))))
    return None
@ls.feature(TEXT_DOCUMENT_DOCUMENT_SYMBOL)
def document_symbols(ls: CPJLanguageServer, params: DocumentSymbolParams):
    uri = params.text_document.uri if hasattr(params, 'text_document') else None
    text = None
    if uri and uri in ls.workspace.documents:
        text = ls.workspace.documents[uri].source
    symbols = []
    if text:
        import re
        lines = text.splitlines()
        for i, line in enumerate(lines):
            m_func = re.match(r'\s*def\s+([A-Za-z_][A-Za-z0-9_]*)', line)
            if m_func:
                symbols.append(DocumentSymbol(
                    name=m_func.group(1),
                    kind=SymbolKind.Function,
                    range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line))),
                    selection_range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line)))
                ))
            m_class = re.match(r'\s*class\s+([A-Za-z_][A-Za-z0-9_]*)', line)
            if m_class:
                symbols.append(DocumentSymbol(
                    name=m_class.group(1),
                    kind=SymbolKind.Class,
                    range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line))),
                    selection_range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line)))
                ))
            m_gui = re.match(r'\s*GUI\b', line)
            if m_gui:
                symbols.append(DocumentSymbol(
                    name='GUI',
                    kind=SymbolKind.Struct,
                    range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line))),
                    selection_range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line)))
                ))
    return symbols
"""Minimal CPJ Language Server (pygls)

Provides basic initialize, textDocument/didOpen, didChange handlers and a simple
syntax diagnostic that flags lines longer than 200 chars and ensures `.cpj` files
are recognized. This is a lightweight scaffold for future diagnostics and integration
with the ANTLR grammar.
"""
 # ...existing code...

# --- Completion Provider ---
@ls.feature(TEXT_DOCUMENT_COMPLETION)
def completions(ls: CPJLanguageServer, params: CompletionParams):
    # Basic completions: keywords, builtins, widget types
    keywords = [
        'def', 'class', 'GUI', 'types', 'addTextField', 'addButton', 'addCheckBox', 'addSlider', 'show',
        'int', 'float', 'bool', 'string', 'True', 'False', 'None', 'return', 'if', 'else', 'for', 'while', 'try', 'except'
    ]
    items = [CompletionItem(label=kw, kind=CompletionItemKind.Keyword) for kw in keywords]
    # Optionally: parse document for function names and widget variables
    uri = params.text_document.uri if hasattr(params, 'text_document') else None
    text = None
    if uri and uri in ls.workspace.documents:
        text = ls.workspace.documents[uri].source
    if text:
        import re
        # Add function names
        for m in re.finditer(r'def\s+([A-Za-z_][A-Za-z0-9_]*)', text):
            items.append(CompletionItem(label=m.group(1), kind=CompletionItemKind.Function))
        # Add widget names from addTextField/addButton/etc
        for m in re.finditer(r'add(?:TextField|Button|CheckBox|Slider)\(["\\\']([A-Za-z0-9_]+)["\"])', text):
            items.append(CompletionItem(label=m.group(1), kind=CompletionItemKind.Variable))
    return CompletionList(is_incomplete=False, items=items)

import logging
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
import importlib
import sys
sys.path.insert(0, '.')
try:
    from tools.type_checker import TypeChecker
except ImportError:
    TypeChecker = None



@ls.feature(TEXT_DOCUMENT_DID_OPEN)
def did_open(ls: CPJLanguageServer, params: DidOpenTextDocumentParams):
    uri = params.text_document.uri
    text = params.text_document.text
    LOGGER.debug('did_open: %s', uri)
    diags = []


    # 1) Use ANTLR generated parser if available to collect syntax diagnostics
    try:
        CPJLexer = importlib.import_module('generated.grammar.CPJLexer').CPJLexer
        CPJParser = importlib.import_module('generated.grammar.CPJParser').CPJParser

        class CaptureErrors(ErrorListener):
            def __init__(self):
                super().__init__()
                self.errors = []

            def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                self.errors.append((line - 1, column, msg))

        stream = InputStream(text)
        lexer = CPJLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = CPJParser(tokens)

        listener = CaptureErrors()
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        # attempt a parse of the top-level rule 'program'
        try:
            parser.program()
        except Exception:
            # parser may raise on severe problems; we capture what we can from listener
            pass

        for (line, col, msg) in listener.errors:
            diag = Diagnostic(range=Range(start=Position(line=line, character=col),
                                         end=Position(line=line, character=col + 1)),
                              message=f'Parser: {msg}',
                              severity=DiagnosticSeverity.Error)
            diags.append(diag)

    except ModuleNotFoundError:
        # If generated parser is not available, fall back to conservative checks
        for i, line in enumerate(text.splitlines()):
            if len(line) > 200:
                diag = Diagnostic(range=Range(start=Position(line=i, character=200),
                                             end=Position(line=i, character=len(line))),
                                  message='Line exceeds 200 characters',
                                  severity=DiagnosticSeverity.Warning)
                diags.append(diag)

    # 2) Type checker diagnostics (handler/type errors)
    if TypeChecker is not None:
        try:
            checker = TypeChecker(text)
            errors = checker.check()
            for err in errors:
                # Try to find the line number for the error (best effort)
                lineno = 0
                for i, l in enumerate(text.splitlines()):
                    if err.split("'")[1] in l:
                        lineno = i
                        break
                diag = Diagnostic(range=Range(start=Position(line=lineno, character=0),
                                             end=Position(line=lineno, character=len(l))),
                                  message=f'TypeChecker: {err}',
                                  severity=DiagnosticSeverity.Error)
                diags.append(diag)
        except Exception as e:
            diag = Diagnostic(range=Range(start=Position(line=0, character=0), end=Position(line=0, character=1)),
                              message=f'TypeChecker error: {e}',
                              severity=DiagnosticSeverity.Warning)
            diags.append(diag)

    # Basic file-extension check diagnostic (kept regardless)
    if not uri.endswith('.cpj'):
        diag = Diagnostic(range=Range(start=Position(line=0, character=0), end=Position(line=0, character=1)),
                          message='Not a .cpj file',
                          severity=DiagnosticSeverity.Information)
        diags.append(diag)

    ls.publish_diagnostics(uri, diags)


@ls.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls: CPJLanguageServer, params: DidChangeTextDocumentParams):
    uri = params.text_document.uri
    text = params.content_changes[0].text
    LOGGER.debug('did_change: %s', uri)
    # Reuse open logic for diagnostics
    did_open(ls, DidOpenTextDocumentParams(text_document=params.text_document))


def start_io():
    """Start the server using stdio (for integration with editors).
    """
    ls.start_io()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_io()
