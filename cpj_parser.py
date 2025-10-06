"""
CPfrom antlr4 import InputStream, CommonTokenStream
from antlr4.Token import Token, CommonToken
from antlr4.error.ErrorListener import ErrorListener
from typing import Optional, List, Dict, Any
import sys
from collections import Counterser Integration with indent-aware lexer.

This module provides an indent-aware parser for the CPJ language, handling both
Python-style indentation and mixed-language syntax parsing through ANTLR4.
"""
from antlr4 import InputStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener
from typing import Optional, List, Dict, Any, Union
import sys
from collections import Counter

from CPJLexer import CPJLexer as BaseLexer
from CPJParser import CPJParser
from CPJListener import CPJListener
from cpj_indent_lexer import CPJIndentLexer

class CPJParseError(Exception):
    """Custom exception for CPJ parsing errors"""
    pass

class CPJParserIntegration:
    """Integration class for CPJ parsing"""
    def __init__(self):
        self.error_listener = CPJErrorListener()
        
    def parse_code(self, code: str) -> Optional[Any]:
        """Parse CPJ code and return AST"""
        input_stream = InputStream(code)
        lexer = CPJIndentAwareLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CPJParser(token_stream)
        
        # Configure error handling
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)
        
        try:
            tree = parser.program()
            if self.error_listener.had_error:
                raise CPJParseError(self.error_listener.error_msg)
            return tree
        except Exception as e:
            raise CPJParseError(str(e))


class CPJIndentAwareLexer(BaseLexer):
    """Custom lexer that combines ANTLR-generated lexer with indentation handling"""
    def __init__(self, input_stream: InputStream):
        super().__init__(input_stream)
        self.indentations = [0]
        self.tokens = []
        self.current_indent = 0
        self.in_string = False
        
    def nextToken(self) -> Token:
        if self.tokens:
            return self.tokens.pop(0)
            
        # Get the next token
        token = super().nextToken()
        
        # Special handling for indentation
        if token.text and token.text.strip() == '\n':
            next_line = token.text[1:]  # Skip the newline
            indent = len(next_line) - len(next_line.lstrip())
            if indent > self.current_indent:
                self.indentations.append(indent)
                self.current_indent = indent
                self.tokens.append(self.create_token(1000, "INDENT"))  # INDENT = 1000
            elif indent < self.current_indent:
                while indent < self.current_indent:
                    self.indentations.pop()
                    self.current_indent = self.indentations[-1]
                    self.tokens.append(self.create_token(1001, "DEDENT"))  # DEDENT = 1001
                    
        return token
    
    def create_token(self, type_: int, text: str) -> Token:
        token = CommonToken()
        token.type = type_
        token.text = text
        token.channel = Token.DEFAULT_CHANNEL
        token.line = -1
        token.column = -1
        token.start = -1
        token.stop = -1
        return token


class CPJErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.had_error = False
        self.error_msg = ""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.had_error = True
        self.error_msg = f"line {line}:{column} {msg}"


class CPJContextAnalyzer:
    """Analyzes code context to determine language features and style"""
    def __init__(self):
        self.has_python_style = False
        self.has_cpp_style = False
        self.has_java_style = False
        self.indentation_style = None  # 'spaces' or 'braces'
        
    def analyze(self, code: str):
        """Analyze code to determine language features used"""
        # Check for Python-style features
        if ':' in code and 'def' in code:
            self.has_python_style = True
            
        # Check for C++-style features
        if '{' in code and ('class' in code or 'struct' in code):
            self.has_cpp_style = True
            
        # Check for Java-style features
        if 'public class' in code or 'interface' in code:
            self.has_java_style = True
            
        # Determine primary indentation style
        if code.count(':') > code.count('{'):
            self.indentation_style = 'spaces'
        else:
            self.indentation_style = 'braces'


class SymbolTable:
    """Tracks symbols, types, and scopes during parsing"""
    def __init__(self):
        self.scopes: List[Dict[str, Any]] = [{}]
        self.current_scope = self.scopes[0]
        
    def enter_scope(self):
        """Enter a new scope level"""
        new_scope = {}
        self.scopes.append(new_scope)
        self.current_scope = new_scope
        
    def exit_scope(self):
        """Exit current scope"""
        if len(self.scopes) > 1:
            self.scopes.pop()
            self.current_scope = self.scopes[-1]
            
    def add_symbol(self, name: str, info: dict):
        """Add a symbol to current scope"""
        self.current_scope[name] = info
        
    def lookup(self, name: str) -> Optional[dict]:
        """Look up a symbol in all accessible scopes"""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None


class IndentAwareParser:
    def __init__(self):
        self.error_listener = CPJErrorListener()
        self.context_analyzer = CPJContextAnalyzer()
        self.symbol_table = SymbolTable()
        self.indent_size = 4  # Default Python-style indentation

    def detect_indent_size(self, code: str) -> int:
        """Detect the indentation size used in the code"""
        indent_sizes = []
        prev_indent = 0
        
        for line in code.split('\n'):
            if not line.strip():  # Skip empty lines
                continue
                
            spaces = len(line) - len(line.lstrip())
            if spaces > prev_indent:
                indent_sizes.append(spaces - prev_indent)
            prev_indent = spaces
            
        if not indent_sizes:
            return self.indent_size
            
        # Return most common indent size
        from collections import Counter
        return Counter(indent_sizes).most_common(1)[0][0]

    def count_dedents(self, prev_indent: int, new_indent: int) -> int:
        """Calculate number of dedents needed"""
        if new_indent > prev_indent:
            return 0
        return (prev_indent - new_indent) // self.indent_size

    def preprocess_input(self, code: str) -> str:
        """
        Preprocess the input code to handle indentation.
        This converts spaces to INDENT/DEDENT tokens while preserving semantics.
        """
        self.indent_size = self.detect_indent_size(code)
        
        lines = code.split('\n')
        processed_lines = []
        indent_stack = [0]  # Track indentation levels
        
        for line in lines:
            # Handle empty lines
            if not line.strip():
                processed_lines.append('')
                continue
                
            # Calculate current indentation level
            spaces = len(line) - len(line.lstrip())
            cur_indent = spaces // self.indent_size
            
            # Handle DEDENT tokens
            while cur_indent < indent_stack[-1]:
                indent_stack.pop()
                processed_lines.append('DEDENT')
                
            # Handle INDENT tokens
            if cur_indent > indent_stack[-1]:
                indent_stack.append(cur_indent)
                processed_lines.append('INDENT')
            
            # Add the actual code line (stripped of indentation)
            processed_lines.append(line.lstrip())
        
        # Add any remaining DEDENTs at end of file
        while len(indent_stack) > 1:
            processed_lines.append('DEDENT')
            indent_stack.pop()
            
        return '\n'.join(processed_lines)

    def parse_code(self, code: str) -> CPJParser.ProgramContext:
        """Parse CPJ code and return the parse tree"""
        processed_code = self.preprocess_input(code)
        input_stream = InputStream(processed_code)
        
        lexer = CPJIndentAwareLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(self.error_listener)

        stream = CommonTokenStream(lexer)
        parser = CPJParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)

        try:
            tree = parser.program()
            if self.error_listener.had_error:
                raise Exception(self.error_listener.error_msg)
            return tree
        except Exception as e:
            raise Exception(f"Failed to parse CPJ code: {str(e)}")

# The code below has been refactored into the improved indent-aware implementation above
"""
from antlr4 import InputStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import LexerNoViableAltException
from typing import Optional, Union, Dict, Any, List
import sys

from CPJLexer import CPJLexer
from CPJParser import CPJParser
from CPJListener import CPJListener


class CPJParseError(Exception):
    # Raised when parsing CPJ code fails
    pass


# Legacy error listener now replaced by CPJErrorListener above
"""
class ParserErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.had_error = False
        self.error_msg = ""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.had_error = True
        self.error_msg = f"line {line}:{column} {msg}"
"""

class CPJParserIntegration:
    def __init__(self):
        self.error_listener = ParserErrorListener()

    def parse_code(self, code: str) -> CPJParser.ProgramContext:
        # Parse CPJ code and return the parse tree - Legacy implementation
        # Now replaced by indent-aware version above
        input_stream = InputStream(code)
        lexer = CPJLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(self.error_listener)

        stream = CommonTokenStream(lexer)
        parser = CPJParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)

        try:
            tree = parser.program()
            if self.error_listener.had_error:
                raise CPJParseError(self.error_listener.error_msg)
            return tree
        except Exception as e:
            raise CPJParseError(f"Failed to parse CPJ code: {str(e)}")
"""