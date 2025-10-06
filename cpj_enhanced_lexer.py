"""
CPJ Enhanced Lexer with support for all language constructs.
This lexer forms the foundation of our CPJ house, handling all core language features
and multi-language integration.
"""
from antlr4 import Lexer, Token
from typing import List, Set, Dict, Optional, Tuple, Union
from cpj_enums import TokenType




from typing import Optional, Tuple

class CPJEnhancedLexer:
    """Extends the base ANTLR4 generated lexer with advanced features.
    Serves as the foundation layer of our CPJ programming house."""
    
    # Operator precedence levels
    PRECEDENCE = {
        '()[]{}': 1,     # Parentheses, brackets, braces
        '.': 2,          # Member access
        '++--': 3,       # Post-increment/decrement
        '!~+-': 4,       # Unary operators
        '**': 5,         # Power
        '*/%': 6,        # Multiplicative
        '+-': 7,         # Additive
        '<<>>': 8,       # Shift
        '<><=>=': 9,     # Relational
        '==!=': 10,      # Equality
        '&': 11,         # Bitwise AND
        '^': 12,         # Bitwise XOR
        '|': 13,         # Bitwise OR
        '&&': 14,        # Logical AND
        '||': 15,        # Logical OR
        '?:': 16,        # Ternary
        '=+=-=*=': 17,   # Assignment
        ',': 18          # Comma
    }
    
    # Special token types
    SPECIAL_TOKENS = {
        'INDENT', 'DEDENT', 'EOF', 'ERROR',
        'NEWLINE', 'WS', 'COMMENT', 'LINE_COMMENT'
    }
    
    def __init__(self, source: str = ''):
        super().__init__()
        self.source = source
        self.indentation_stack: List[int] = [0]
        self.tokens_queue: List[Token] = []
        self.brace_level = 0
        self.in_string = False
        self.string_delimiter = ''
        self.current_indent = 0
        self.pending_dedents = 0
        self.current = 0
        self.start = 0
        self.line = 1
        
        # Keywords mapping for our house foundation
        self.keywords = {
            'fn': TokenType.FUNCTION,
            'type': TokenType.TYPE,
            'memory': TokenType.MEMORY,
            'cpp': TokenType.CPP_BLOCK,
            'python': TokenType.PYTHON_BLOCK,
            'java': TokenType.JAVA_BLOCK,
            'int': TokenType.INT,
            'float': TokenType.FLOAT,
            'string': TokenType.STRING_TYPE,
            'bool': TokenType.BOOL,
            'void': TokenType.VOID
        }
        
    def handle_indentation(self, text: str, line: int, column: int) -> List[Token]:
        """Handle Python-style indentation tokens"""
        tokens = []
        
        # Skip empty lines
        if not text.strip():
            return tokens
            
        # Calculate indentation
        indent = len(text) - len(text.lstrip())
        
        if indent > self.indentation_stack[-1]:
            # Indent
            self.indentation_stack.append(indent)
            tokens.append(self.create_token(TokenType.INDENT.value, text, line, column))
            
        elif indent < self.indentation_stack[-1]:
            # Dedent (possibly multiple levels)
            while indent < self.indentation_stack[-1]:
                self.indentation_stack.pop()
                tokens.append(self.create_token(TokenType.DEDENT, text, line, column))
                
            if indent != self.indentation_stack[-1]:
                # Indentation error
                self.report_error(f"Inconsistent indentation at line {line}")
                
        return tokens
        
    def handle_string_literals(self, char: str, line: int, column: int) -> List[Token]:
        """Handle string literals including triple quotes"""
        tokens = []
        
        if not self.in_string and char in '"\'':
            self.in_string = True
            self.string_delimiter = char
            # Check for triple quotes
            if self.peek(2) == char * 2:
                self.string_delimiter = char * 3
                
        elif self.in_string and self.string_delimiter and char == self.string_delimiter[-1]:
            if len(self.string_delimiter) == 3:
                if self.peek(2) == char * 2:
                    self.in_string = False
                    self.string_delimiter = ''
            else:
                self.in_string = False
                self.string_delimiter = ''
                
        return tokens
        
    def handle_interpolation(self, text: str, line: int, column: int) -> List[Token]:
        """Handle string interpolation"""
        tokens = []
        
        if self.in_string and '{' in text:
            # Handle string interpolation
            parts = text.split('{')
            for i, part in enumerate(parts):
                if i > 0:
                    tokens.append(self.create_token(TokenType.STRING_INTERP_START, '{', line, column))
                if '}' in part:
                    expr, rest = part.split('}', 1)
                    # Process expression inline
                    tokens.append(self.create_token(TokenType.IDENTIFIER, expr.strip(), line, column))
                    tokens.append(self.create_token(TokenType.STRING_INTERP_END, '}', line, column))
                    # Add rest of string
                    if rest:
                        tokens.append(self.create_token(TokenType.STRING, rest, line, column))
                else:
                    tokens.append(self.create_token(TokenType.STRING, part, line, column))
                    
        return tokens
        
    def handle_preprocessor(self, line: str, line_num: int, column: int) -> List[Token]:
        """Handle C++ style preprocessor directives"""
        tokens = []
        
        if line.strip().startswith('#'):
            directive = line.strip().split()[0]
            if directive in ['#include', '#define', '#ifdef', '#ifndef', '#endif']:
                tokens.append(self.create_token(TokenType.PREPROCESSOR, line.strip(), line_num, column))
                
        return tokens
        
    def report_error(self, message: str):
        """Report lexical errors"""
        print(f"Lexical Error: {message}")
        
    def peek(self, n: int = 1) -> str:
        """Peek ahead n characters in input stream"""
        pos = self.current + n - 1
        if pos >= len(self.source):
            return '\0'
        return self.source[pos]
        
    def create_token(self, type_: Union[TokenType, int], text: str, line: int, column: int) -> Token:
        """Create a new token with the proper type"""
        token = Token()
        if isinstance(type_, TokenType):
            token.type = type_.value
        else:
            token.type = type_
        token.text = text
        # Store line and column in token's hidden state
        setattr(token, 'line', line)
        setattr(token, 'column', column)
        return token