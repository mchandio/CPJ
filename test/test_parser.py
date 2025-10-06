"""
Test for CPJ parser integration.
"""
import pytest
from cpj_runtime import parse_cpj_code
from cpj_parser import CPJParseError

def test_basic_parsing():
    # Test basic function definition
    code = """
def greet(name: str) -> str:
    return "Hello, " + name
"""
    tree = parse_cpj_code(code)
    assert tree is not None

def test_gui_block():
    # Test GUI block parsing
    code = """
gui:
    button "Click me" -> handleClick
"""
    tree = parse_cpj_code(code)
    assert tree is not None

def test_type_definition():
    # Test type definition parsing
    code = """
type Person {
    name: str,
    age: int
}
"""
    tree = parse_cpj_code(code)
    assert tree is not None

def test_event_handler():
    # Test event handler parsing
    code = """
on click from button do:
    print("Button clicked!")
"""
    tree = parse_cpj_code(code)
    assert tree is not None

def test_invalid_code():
    # Test invalid code handling
    code = """
def missing_colon
    print("This is invalid")
"""
    with pytest.raises(CPJParseError):
        parse_cpj_code(code)