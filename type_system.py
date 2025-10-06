"""
CPJ Type System - The Strong Walls of Our Programming House
This module implements a robust type system that provides structural integrity
to our CPJ language, ensuring type safety and proper construction.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Any
from enum import Enum, auto

class TypeKind(Enum):
    """Types of materials used in our walls"""
    PRIMITIVE = auto()     # Basic building blocks (int, float, bool, etc.)
    COMPOSITE = auto()     # Structured types (classes, structs)
    FUNCTION = auto()      # Room blueprints (function types)
    GENERIC = auto()       # Adaptable materials (generic types)
    INTERFACE = auto()     # Connection points (interfaces)
    FOREIGN = auto()       # Imported materials (types from other languages)

@dataclass
class TypeConstraint:
    """Constraints on how materials can be used"""
    kind: str  # Type of constraint
    params: Dict[str, Any] = field(default_factory=dict)
    message: str = ""  # Error message when constraint is violated

@dataclass
class WallSection:
    """A section of our type system wall"""
    name: str
    kind: TypeKind
    constraints: List[TypeConstraint] = field(default_factory=list)
    members: Dict[str, 'WallSection'] = field(default_factory=dict)
    methods: Dict[str, 'FunctionType'] = field(default_factory=dict)
    parent: Optional['WallSection'] = None
    interfaces: List['WallSection'] = field(default_factory=list)

@dataclass
class FunctionType:
    """Type information for room connections (function types)"""
    params: List[WallSection]
    return_type: WallSection
    is_async: bool = False
    constraints: List[TypeConstraint] = field(default_factory=list)

class TypeSystem:
    """The complete type system forming our house's walls"""
    
    def __init__(self):
        self.types: Dict[str, WallSection] = {}
        self.type_stack: List[WallSection] = []
        self.errors: List[str] = []
        
        # Initialize primitive types
        self._init_primitive_types()
    
    def _init_primitive_types(self):
        """Initialize basic building materials"""
        primitives = [
            ("int", "Integer values"),
            ("float", "Floating-point values"),
            ("bool", "Boolean values"),
            ("str", "String values"),
            ("void", "No value"),
            ("any", "Any type - use with caution")
        ]
        
        for name, desc in primitives:
            self.types[name] = WallSection(
                name=name,
                kind=TypeKind.PRIMITIVE,
                constraints=[TypeConstraint(
                    kind="primitive",
                    params={"description": desc}
                )]
            )
    
    def define_type(self, name: str, kind: TypeKind) -> WallSection:
        """Define a new type in our wall structure"""
        if name in self.types:
            self.errors.append(f"Type '{name}' is already defined")
            return self.types[name]
            
        wall_section = WallSection(name=name, kind=kind)
        self.types[name] = wall_section
        return wall_section
    
    def get_type(self, name: str) -> Optional[WallSection]:
        """Get type information from our wall"""
        return self.types.get(name)
    
    def enter_type(self, section: WallSection):
        """Enter a type's scope"""
        self.type_stack.append(section)
    
    def exit_type(self):
        """Exit current type scope"""
        if self.type_stack:
            self.type_stack.pop()
    
    def current_type(self) -> Optional[WallSection]:
        """Get current type scope"""
        return self.type_stack[-1] if self.type_stack else None
    
    def check_compatibility(self, source: WallSection, target: WallSection) -> bool:
        """Check if two types are compatible"""
        # Same type is always compatible
        if source.name == target.name:
            return True
        
        # Any type accepts everything
        if target.name == "any":
            return True
        
        # Check inheritance
        current = source
        while current.parent:
            if current.parent.name == target.name:
                return True
            current = current.parent
        
        # Check interfaces
        for interface in source.interfaces:
            if interface.name == target.name:
                return True
            
        return False
    
    def apply_constraints(self, value: Any, type_: WallSection) -> List[str]:
        """Apply type constraints to a value"""
        errors = []
        
        for constraint in type_.constraints:
            if constraint.kind == "primitive":
                if not self._check_primitive_constraint(value, type_.name):
                    errors.append(constraint.message or f"Value does not match type {type_.name}")
            elif constraint.kind == "range":
                if not self._check_range_constraint(value, constraint.params):
                    errors.append(constraint.message or "Value out of allowed range")
            elif constraint.kind == "pattern":
                if not self._check_pattern_constraint(value, constraint.params):
                    errors.append(constraint.message or "Value does not match required pattern")
        
        return errors
    
    def _check_primitive_constraint(self, value: Any, type_name: str) -> bool:
        """Check if value matches primitive type"""
        if type_name == "int":
            return isinstance(value, int)
        elif type_name == "float":
            return isinstance(value, (int, float))
        elif type_name == "bool":
            return isinstance(value, bool)
        elif type_name == "str":
            return isinstance(value, str)
        elif type_name == "void":
            return value is None
        elif type_name == "any":
            return True
        return False
    
    def _check_range_constraint(self, value: Any, params: Dict[str, Any]) -> bool:
        """Check if value is within allowed range"""
        min_val = params.get("min")
        max_val = params.get("max")
        
        if min_val is not None and value < min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        return True
    
    def _check_pattern_constraint(self, value: str, params: Dict[str, Any]) -> bool:
        """Check if value matches required pattern"""
        import re
        pattern = params.get("pattern")
        if not pattern:
            return True
        return bool(re.match(pattern, value))
    
    def create_function_type(self, params: List[WallSection], 
                           return_type: WallSection) -> FunctionType:
        """Create a function type"""
        return FunctionType(params=params, return_type=return_type)
    
    def check_function_call(self, func_type: FunctionType, 
                          arg_types: List[WallSection]) -> List[str]:
        """Check function call type safety"""
        errors = []
        
        if len(arg_types) != len(func_type.params):
            errors.append(f"Expected {len(func_type.params)} arguments, got {len(arg_types)}")
            return errors
        
        for i, (param_type, arg_type) in enumerate(zip(func_type.params, arg_types)):
            if not self.check_compatibility(arg_type, param_type):
                errors.append(f"Argument {i+1}: Cannot use {arg_type.name} where {param_type.name} is expected")
        
        return errors

# Example usage
if __name__ == "__main__":
    # Create type system
    type_system = TypeSystem()
    
    # Define a composite type
    room_type = type_system.define_type("Room", TypeKind.COMPOSITE)
    room_type.members["size"] = type_system.get_type("int")
    room_type.members["name"] = type_system.get_type("str")
    
    # Add constraints
    room_type.constraints.append(
        TypeConstraint(
            kind="range",
            params={"min": 1, "max": 100},
            message="Room size must be between 1 and 100"
        )
    )
    
    # Define a function type
    create_room_params = [type_system.get_type("int"), type_system.get_type("str")]
    create_room_type = type_system.create_function_type(create_room_params, room_type)
    
    # Test type checking
    arg_types = [type_system.get_type("int"), type_system.get_type("str")]
    errors = type_system.check_function_call(create_room_type, arg_types)
    
    if errors:
        print("Type Errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Type check passed successfully!")