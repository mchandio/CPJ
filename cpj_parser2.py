"""CPJ Parser - AST Generation and Full Language Support using house metaphor"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict, Union, Any, TypeVar, Tuple
from abc import ABC, abstractmethod

from cpj_type_system import WallSection, TypeSystem, TypeKind
from cpj_parser_helpers import Expression, ParseError
from cpj_enums import NodeType, TokenType, AccessLevel

T = TypeVar('T')

@dataclass
class Node(ABC):
    """Base class for all AST nodes"""
    node_type: NodeType
    location: Tuple[int, int] = field(default=(0, 0))
    name: str = field(default="")

@dataclass 
class Variable(Node):
    """A variable node in the AST"""
    wall_section: Optional[WallSection] = None
    
    def __init__(self, **kwargs):
        node_type = kwargs.pop('node_type', NodeType.VARIABLE)
        super().__init__(node_type=node_type, **kwargs)
        self.wall_section = kwargs.get('wall_section', None)

@dataclass
class House(Node):
    """Represents a complete CPJ program as a house"""
    foundation: Optional['Foundation'] = field(default=None)
    rooms: List['Room'] = field(default_factory=list)
    blueprints: List['Blueprint'] = field(default_factory=list)
    utilities: List['Utility'] = field(default_factory=list)
    public_areas: List[str] = field(default_factory=list)  # Public interface

    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.HOUSE, **kwargs)
        self.foundation = kwargs.get('foundation', None)
        self.rooms = kwargs.get('rooms', [])
        self.blueprints = kwargs.get('blueprints', [])
        self.utilities = kwargs.get('utilities', [])
        self.public_areas = kwargs.get('public_areas', [])

@dataclass
class Foundation(Node):
    """Core language functionality and configuration"""
    memory_config: Dict[str, Any] = field(default_factory=dict)
    type_system: TypeSystem = field(default_factory=TypeSystem)
    utilities: List['Utility'] = field(default_factory=list)

    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.FOUNDATION, **kwargs)
        self.memory_config = kwargs.get('memory_config', {})
        self.type_system = kwargs.get('type_system', TypeSystem())
        self.utilities = kwargs.get('utilities', [])

@dataclass
class Room(Node):
    """A function/module implementation"""
    purpose: str = field(default="")  # Function's role
    entrances: List[Variable] = field(default_factory=list)  # Parameters 
    exits: WallSection = field(default_factory=lambda: WallSection(TypeKind.UNDEFINED, 'void'))  # Return type
    contents: Optional['Block'] = field(default=None)  # Function body
    is_async: bool = field(default=False)
    access_level: AccessLevel = field(default=AccessLevel.PUBLIC)

    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.ROOM, **kwargs)
        self.purpose = kwargs.get('purpose', "")
        self.entrances = kwargs.get('entrances', [])
        self.exits = kwargs.get('exits', WallSection(TypeKind.UNDEFINED, 'void'))
        self.contents = kwargs.get('contents', None)
        self.is_async = kwargs.get('is_async', False)
        self.access_level = kwargs.get('access_level', AccessLevel.PUBLIC)

@dataclass
class Blueprint(Node):
    """A type definition"""
    sections: List[Variable] = field(default_factory=list)  # Fields
    access_level: AccessLevel = field(default=AccessLevel.PUBLIC)
    
    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.BLUEPRINT, **kwargs)
        self.sections = kwargs.get('sections', [])
        self.access_level = kwargs.get('access_level', AccessLevel.PUBLIC)

@dataclass
class Utility(Node):
    """Built-in functionality"""
    interface: Dict[str, WallSection] = field(default_factory=dict)
    access_level: AccessLevel = field(default=AccessLevel.PUBLIC)
    
    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self.interface = kwargs.get('interface', {})
        self.access_level = kwargs.get('access_level', AccessLevel.PUBLIC)

@dataclass
class Block(Node):
    """A sequence of statements"""
    statements: List[Node] = field(default_factory=list)
    
    def __init__(self, **kwargs):
        super().__init__(node_type=NodeType.BLOCK, **kwargs)
        self.statements = kwargs.get('statements', [])
