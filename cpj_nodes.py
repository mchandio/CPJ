"""CPJ Parser - AST Generation and Full Language Support using house metaphor"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict, Union, Any, TypeVar, ForwardRef

from cpj_type_system import WallSection, TypeSystem, TypeKind
from cpj_parser_helpers import Variable, Expression, ParseError

T = TypeVar('T')

Room = ForwardRef('Room')
Blueprint = ForwardRef('Blueprint')
Utility = ForwardRef('Utility')

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
    AI = auto()

@dataclass
class Node:
    node_type: NodeType
    location: tuple = field(default_factory=lambda: (1, 1))  # (line, column)
    name: str = field(default="")