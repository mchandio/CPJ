from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict, Type, Any, Union

class TypeKind(Enum):
    PRIMITIVE = auto()
    COMPOUND = auto()
    FUNCTION = auto()
    CLASS = auto()
    MODULE = auto()
    VARIABLE = auto()
    UNDEFINED = auto()

@dataclass
class WallSection:
    """Type information for a node"""
    kind: TypeKind
    name: str
    constraints: Dict[str, Any] = field(default_factory=dict)

class TypeSystem:
    """Type system implementation"""
    def __init__(self):
        self.types: Dict[str, WallSection] = {}
        self.setup_primitives()
    
    def setup_primitives(self):
        """Set up primitive types"""
        primitives = ['int', 'float', 'str', 'bool', 'void']
        for p in primitives:
            self.types[p] = WallSection(TypeKind.PRIMITIVE, p)
    
    def get_type(self, name: str) -> Optional[WallSection]:
        return self.types.get(name)
    
    def add_type(self, wall: WallSection):
        self.types[wall.name] = wall