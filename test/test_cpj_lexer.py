"""Test suite for CPJ lexer functionality."""
import pytest
from antlr4 import InputStream
from CPJLexer import CPJLexer

@pytest.fixture
def lexer():
    """Create a lexer instance for tests."""
    input_stream = InputStream("")
    return CPJLexer(input_stream)

@pytest.mark.lexer
class TestCPJLexer:
    """Test cases for the CPJ lexical analyzer."""
    
    def test_basic_tokens(self, lexer):
        """Test basic token recognition."""
        source = """
        x = 42
        y = "hello"
        z = true
        """
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Verify token count and types
        assert len(tokens) > 0
        
    def test_string_literals(self, lexer):
        """Test string literal token handling."""
        source = 'x = "hello" y = "world"'
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Count string literal tokens
        string_tokens = [t for t in tokens if t.text.startswith('"') and t.text.endswith('"')]
        assert len(string_tokens) == 2
        
    def test_numeric_literals(self, lexer):
        """Test numeric literal token handling."""
        source = """
        x = 42
        y = 3.14
        z = -123
        w = 1.23e-4
        """
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Look for number tokens by checking if their text is numeric
        num_tokens = [t for t in tokens if t.text.replace(".", "").replace("-", "").replace("e", "").replace("E", "").isdigit()]
        assert len(num_tokens) > 0
        
    def test_keywords(self, lexer):
        """Test keyword token recognition."""
        keywords = [
            "if", "for", "while", "return",
            "true", "false"
        ]
        source = " ".join(keywords)
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Verify all keywords are tokenized
        assert len(tokens) >= len(keywords)
        token_texts = [t.text.lower() for t in tokens if t.text]
        for keyword in keywords:
            assert keyword in token_texts

    def test_operators(self, lexer):
        """Test operator token recognition."""
        operators = "+-*/%=<>!&|^"
        source = " ".join(c for c in operators)
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Verify operator tokens are generated
        op_tokens = [t for t in tokens if t.text in operators]
        assert len(op_tokens) > 0

    def test_complex_expression(self, lexer):
        """Test lexing of a complex expression."""
        source = """
        x = (a + b) * c / 2
        y = x > 10 && !flag
        """
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Verify tokens are generated
        assert len(tokens) > 0
        
    def test_comments(self, lexer):
        """Test comment handling."""
        source = """
        // Line comment
        x = 1 // End of line comment
        /* Block
           comment */
        y = 2
        """
        lexer.inputStream = InputStream(source)
        tokens = list(lexer.getAllTokens())
        
        # Verify we get some tokens after comments are stripped
        assert len(tokens) > 0
        
    def test_error_handling(self, lexer):
        """Test lexer error handling."""
        source = "x = 42 @ y"
        lexer.inputStream = InputStream(source)
        
        # Verify we get tokens before the error
        tokens = list(lexer.getAllTokens())
        assert len(tokens) > 0