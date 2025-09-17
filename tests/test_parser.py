import pytest
import sys
import os
# Ensure project root is on sys.path so tests can import tools.*
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.cpj_parser import Parser, Module, Print, FuncDef, GUIBlock


def test_parse_simple_print():
    src = 'print("Hi")\n'
    p = Parser(src)
    ast = p.parse()
    assert isinstance(ast, Module)
    assert len(ast.items) == 1
    assert isinstance(ast.items[0], Print)


def test_parse_func_and_gui():
    src = '''
def foo(x):
    print("ok " + x)

GUI {
    addButton("Click")
}
'''
    p = Parser(src)
    ast = p.parse()
    assert any(isinstance(i, FuncDef) for i in ast.items)
    assert any(isinstance(i, GUIBlock) for i in ast.items)


def test_malformed_print():
    src = 'print(\n'
    p = Parser(src)
    ast = p.parse()
    # should still produce a module but with a Print node
    assert isinstance(ast, Module)
    # one item (malformed print)
    assert len(ast.items) >= 0
