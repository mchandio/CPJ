from enum import Enum, auto

class NodeType(Enum):
    HOUSE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    MATERIAL = auto()
    LANGUAGE_BLOCK = auto()
    LITERAL = auto()
    VARIABLE = auto()
    WINDOW = auto()
    DOOR = auto()
    LIGHT = auto()

class AccessLevel(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()

class TokenType(Enum):
    # House structure tokens
    PUBLIC = auto()
    PRIVATE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    
    # Basic tokens
    IDENTIFIER = auto()
    STRING = auto()
    LBRACE = auto()
    RBRACE = auto()
    LPAREN = auto()
    RPAREN = auto()
    COLON = auto()
    COMMA = auto()
    ARROW = auto()
    EQUAL = auto()
    SEMI = auto()
    DOT = auto()
    EOF = auto()  # End of file marker
    
    # House features
    WINDOW = auto()
    DOOR = auto()
    LIGHT = auto()