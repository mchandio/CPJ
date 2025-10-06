"""
CPJ Parser with custom lexer to handle Python-style indentation.
"""
from antlr4 import Lexer, InputStream
from antlr4.Token import Token, CommonToken
from typing import List, Optional
from io import StringIO

class CPJIndentLexer(Lexer):
    INDENT = 1000
    DEDENT = 1001
    
    def __init__(self, input_stream: InputStream):
        """Initialize lexer with input stream"""
            
        super().__init__(input_stream)
        self.indentStack = [0]
        self.pendingTokens = []
        self.tokens = []
        self.current_indent = 0
        self._tokenStartCharIndex = 0
        self._tokenStartLine = 1
        self._tokenStartColumn = 0
        
    def nextToken(self):
        if self.pendingTokens:
            return self.pendingTokens.pop(0)

        token = super().nextToken()
        text = token.text or ""

        if token.type == Token.EOF:
            while self.indentStack[-1] > 0:
                self.pendingTokens.append(self.createDedent())
                self.indentStack.pop()
            return token

        if text.strip() and text[0].isspace():
            spaces = len(text) - len(text.lstrip())
            if spaces > self.current_indent:
                self.indentStack.append(spaces)
                self.pendingTokens.append(self.createIndent())
            elif spaces < self.current_indent:
                while spaces < self.current_indent:
                    self.indentStack.pop()
                    self.pendingTokens.append(self.createDedent())
                    self.current_indent = self.indentStack[-1]

        return token

    def createIndent(self):
        token = CommonToken()
        token.type = self.INDENT
        token.text = "INDENT"
        token.channel = Token.DEFAULT_CHANNEL
        token.start = -1
        token.stop = -1
        return token

    def createDedent(self):
        token = CommonToken()
        token.type = self.DEDENT
        token.text = "DEDENT"
        token.channel = Token.DEFAULT_CHANNEL
        token.start = -1
        token.stop = -1
        return token