"""
Comprehensive test suite for the CPJ lexer.
"""
import unittest
from antlr4 import InputStream
from antlr4.Token import Token
from cpj_parser import CPJIndentAwareLexer
from typing import List, Tuple

class TestCPJLexer(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        pass
        
    def tokenize(self, text: str) -> List[Tuple[int, str]]:
        """Helper to get tokens from text"""
        input_stream = InputStream(text)
        lexer = CPJIndentAwareLexer(input_stream)
        tokens = []
        while True:
            token = lexer.nextToken()
            if token.type == Token.EOF:
                break
            tokens.append((token.type, token.text))
        return tokens
        
    def test_basic_tokens(self):
        """Test basic token recognition"""
        code = """
function test() {
    print("Hello")
}
"""
        tokens = self.tokenize(code)
        self.assertIn(('function', 'function'), tokens)
        self.assertIn(('print', 'print'), tokens)
        self.assertIn(('"Hello"', '"Hello"'), tokens)
        
    def test_indentation(self):
        """Test indentation handling"""
        code = """
def test():
    x = 1
        y = 2
    z = 3
"""
        tokens = self.tokenize(code)
        indent_count = sum(1 for t in tokens if t[0] == 1000)  # INDENT = 1000
        dedent_count = sum(1 for t in tokens if t[0] == 1001)  # DEDENT = 1001
        self.assertEqual(indent_count, 2)  # One for first indent, one for nested
        self.assertEqual(dedent_count, 2)  # Matching dedents
        
    def test_mixed_syntax(self):
        """Test mixed language syntax"""
        code = """
class Test {
    def python_method():
        return 1
    
    void cpp_method() {
        return 2;
    }
}
"""
        tokens = self.tokenize(code)
        # Verify both Python and C++ style tokens
        self.assertTrue(any(t[1] == 'def' for t in tokens))
        self.assertTrue(any(t[1] == 'void' for t in tokens))
        self.assertTrue(any(t[1] == '{' for t in tokens))
        self.assertTrue(any(t[1] == ';' for t in tokens))
        
    def test_string_literals(self):
        """Test string literal handling"""
        code = r'''
x = "normal string"
y = 'single quotes'
z = """triple quoted
multiline string"""
w = r"raw\nstring"
'''
        tokens = self.tokenize(code)
        string_tokens = [t for t in tokens if t[1].startswith(('"', "'"))]
        self.assertEqual(len(string_tokens), 4)
        
    def test_comments(self):
        """Test comment handling"""
        code = """
// C++ style comment
# Python style comment
/* C style
   multiline comment */
"""
        tokens = self.tokenize(code)
        # Comments should be filtered by lexer
        comment_tokens = [t for t in tokens if '//' in t[1] or '#' in t[1] or '/*' in t[1]]
        self.assertEqual(len(comment_tokens), 0)
        
    def test_numeric_literals(self):
        """Test numeric literal handling"""
        code = """
x = 42
y = 3.14
z = 0xFF
w = 1_000_000
v = 1.2e-10
"""
        tokens = self.tokenize(code)
        numeric_tokens = [t for t in tokens if any(c.isdigit() for c in t[1])]
        self.assertEqual(len(numeric_tokens), 5)
        
    def test_operators(self):
        """Test operator handling"""
        code = """
a = b + c
d = e * f
g = h & i
j = k | l
m = n ^ o
"""
        tokens = self.tokenize(code)
        operators = ['+', '*', '&', '|', '^']
        for op in operators:
            self.assertTrue(any(t[1] == op for t in tokens))
            
    def test_error_recovery(self):
        """Test lexer error recovery"""
        code = """
def test():
    x = @invalid
    y = valid
"""
        tokens = self.tokenize(code)
        # Should continue lexing after invalid token
        self.assertTrue(any(t[1] == 'valid' for t in tokens))
        
    def test_nested_structures(self):
        """Test deeply nested structures"""
        code = """
def outer():
    def inner1():
        if True:
            while True:
                x = 1
        y = 2
    def inner2():
        z = 3
"""
        tokens = self.tokenize(code)
        indent_levels = []
        current_level = 0
        for token_type, _ in tokens:
            if token_type == 'INDENT':
                current_level += 1
            elif token_type == 'DEDENT':
                current_level -= 1
            indent_levels.append(current_level)
        self.assertEqual(max(indent_levels), 4)  # Maximum nesting depth
        self.assertEqual(indent_levels[-1], 0)  # Should end at base level
        
    def test_line_continuation(self):
        """Test line continuation handling"""
        code = """
x = 1 + \\
    2 + \\
    3
"""
        tokens = self.tokenize(code)
        # Should be treated as a single line
        numeric_tokens = [t for t in tokens if t[1].isdigit()]
        self.assertEqual(len(numeric_tokens), 3)
        
    def test_special_characters(self):
        """Test special character handling"""
        code = """
s = "\n\t\r\\"
"""
        tokens = self.tokenize(code)
        string_token = next(t[1] for t in tokens if t[1].startswith('"'))
        self.assertIn('\\n', string_token)
        self.assertIn('\\t', string_token)
        self.assertIn('\\r', string_token)
        self.assertIn('\\\\', string_token)

if __name__ == '__main__':
    unittest.main()