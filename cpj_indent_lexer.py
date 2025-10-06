"""
CPJ Python-style lexer that handles indentation correctly.
"""
from antlr4 import *
from antlr4.Token import Token, CommonToken
from typing import List, Set
import sys

from CPJLexer import CPJLexer as BaseLexer


class CPJIndentLexer(Lexer):
    INDENT_TYPE = 1000
    DEDENT_TYPE = 1001
    
    def __init__(self, input_stream: InputStream):
        # Initialize the base lexer
        Lexer.__init__(self, input=input_stream)
        
        # Indentation state
        self.indentations: List[int] = [0]  # Start with 0 indentation level
        self.tokens: List[Token] = []  # Queue of tokens to emit
        self.reached_eof = False
        
        self.first_token = True
        self.last_token = None
        self.current_indent = 0
        self.in_string = False
        
        # Internal state
        self._tokenStartCharIndex = 0
        self._tokenStartLine = 1
        self._tokenStartColumn = 0
        
        # Token factory for creating tokens
        self.token_factory = CommonToken

    def nextToken(self) -> Token:
        # First return any tokens we've queued up
        if self.tokens:
            next_token = self.tokens.pop(0)
            self.last_token = next_token
            return next_token

        # Mark when we've reached EOF
        if self.reached_eof:
            return super().nextToken()

        # Get the next token from the input stream
        token = super().nextToken()

        # Handle EOL if needed
        if token.type == Token.EOF:
            self.reached_eof = True
            # Clear any remaining indentation levels
            while self.indentations[-1] > 0:
                self.emit_dedent()
            return token

        # Handle newlines and indentation
        if token.text and token.text.strip() == '\n':
            # Get next character for indentation
            next_char = token.text.replace('\n', '')
            indent = len(next_char) - len(next_char.lstrip())
            
            if indent > self.current_indent:
                # Emit INDENT
                self.indentations.append(indent)
                self.current_indent = indent
                self.tokens.append(self.create_indent())
            elif indent < self.current_indent:
                # Emit one or more DEDENTs
                while indent < self.current_indent:
                    self.indentations.pop()
                    self.current_indent = self.indentations[-1]
                    self.tokens.append(self.create_dedent())

        return token

    def create_indent(self) -> CommonToken:
        return self.create_token(self.INDENT_TYPE, "INDENT", self._tokenStartCharIndex)

    def create_dedent(self) -> CommonToken:
        return self.create_token(self.DEDENT_TYPE, "DEDENT", self._tokenStartCharIndex)

    def create_token(self, type_: int, text: str, pos: int) -> CommonToken:
        token = self.token_factory()
        token.type = type_
        token.text = text
        token.line = self._tokenStartLine
        token.column = self._tokenStartColumn
        token.start = pos
        token.stop = pos + len(text) - 1
        token.channel = Token.DEFAULT_CHANNEL
        return token

    def emit_dedent(self):
        self.tokens.append(self.create_dedent())
        self.indentations.pop()
        if self.indentations:
            self.current_indent = self.indentations[-1]
        else:
            self.current_indent = 0