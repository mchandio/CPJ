from typing import List, Optional
from cpj_type_system import WallSection
from dataclasses import dataclass, field

class ParseError(Exception):
    """Exception raised for parsing errors"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

@dataclass
class Variable:
    """Parameter variable for functions/rooms"""
    name: str
    type: Optional['WallSection'] = None
    default_value: Optional['Expression'] = None

@dataclass 
class Expression:
    """Base class for expressions"""
    pass