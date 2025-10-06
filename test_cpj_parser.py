"""
Comprehensive test suite for the CPJ parser.
"""
import unittest
from antlr4 import InputStream, CommonTokenStream
from cpj_parser import (
    CPJIndentAwareLexer, CPJParser, CPJErrorListener,
    CPJContextAnalyzer
)
from typing import Any, Optional

class TestCPJParser(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.error_listener = CPJErrorListener()
        
    def parse(self, code: str) -> Optional[Any]:
        """Helper to parse code and return AST"""
        input_stream = InputStream(code)
        lexer = CPJIndentAwareLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CPJParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)
        return parser.program()
        
    def test_basic_structure(self):
        """Test basic program structure parsing"""
        code = """
class Test {
    def method():
        return 1
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_function_definitions(self):
        """Test function definition parsing"""
        code = """
def python_func():
    pass

function js_func() {
    return;
}

void cpp_func() {
    return 0;
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_class_definitions(self):
        """Test class definition parsing"""
        code = """
class PythonStyle:
    def __init__(self):
        pass
        
class JavaStyle {
    public JavaStyle() {
        super();
    }
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_expressions(self):
        """Test expression parsing"""
        code = """
x = 1 + 2 * 3
y = (a + b) * c
z = func(x, y, z=3)
w = obj.method().field
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_statements(self):
        """Test statement parsing"""
        code = """
if x > 0:
    print(x)
elif x < 0:
    print(-x)
else:
    print(0)

while True:
    if done:
        break
    continue
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_error_recovery(self):
        """Test parser error recovery"""
        code = """
def test():
    if x > 0
        print(x)  # Missing colon
    y = 1  # Should continue here
"""
        ast = self.parse(code)
        self.assertTrue(self.error_listener.had_error)
        # Should have partial AST
        self.assertIsNotNone(ast)
        
    def test_mixed_language_features(self):
        """Test mixed language feature parsing"""
        code = """
class Test {
    private int cpp_field;
    public str python_field
    
    def python_method():
        return self.python_field
        
    int cpp_method() {
        return this->cpp_field;
    }
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_decorators(self):
        """Test decorator parsing"""
        code = """
@decorator1
@decorator2(arg1, arg2=value)
def test():
    pass

@Component({
    selector: 'app-root'
})
class AppComponent {
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_imports(self):
        """Test import statement parsing"""
        code = """
import module1
from module2 import name1, name2
import module3 as alias
from module4 import *

#include <vector>
#include "local.h"

import java.util.List;
import static java.lang.Math.*;
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_context_analysis(self):
        """Test context analyzer"""
        analyzer = CPJContextAnalyzer()
        
        # Python style
        python_code = """
def test():
    if x > 0:
        return x
"""
        analyzer.analyze(python_code)
        self.assertTrue(analyzer.has_python_style)
        
        # C++ style
        cpp_code = """
int test() {
    if (x > 0) {
        return x;
    }
}
"""
        analyzer.analyze(cpp_code)
        self.assertTrue(analyzer.has_cpp_style)
        
    def test_nested_blocks(self):
        """Test nested block parsing"""
        code = """
def outer():
    def inner1():
        class Inner:
            def nested():
                if True:
                    while True:
                        try:
                            x = 1
                        except:
                            pass
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)
        
    def test_language_specific_features(self):
        """Test language-specific feature parsing"""
        code = """
// C++ templates
template<typename T>
class Container {
    T value;
};

// Python list comprehension
x = [i * 2 for i in range(10)]

// Java generics
class Box<T> {
    private T value;
}
"""
        ast = self.parse(code)
        self.assertIsNotNone(ast)
        self.assertFalse(self.error_listener.had_error)

if __name__ == '__main__':
    unittest.main()