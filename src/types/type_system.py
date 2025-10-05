"""
CPJ Type System - Python Implementation
"""
from enum import Enum
from typing import Any, Dict, List, Optional, Type, TypeVar, Generic
import json
from abc import ABC, abstractmethod

class TypeCategory(Enum):
    PRIMITIVE = "primitive"
    COLLECTION = "collection"
    OBJECT = "object"
    FUNCTION = "function"
    GENERIC = "generic"

class PrimitiveTypeId(Enum):
    BOOL = "bool"
    INT8 = "int8"
    INT16 = "int16"
    INT32 = "int32"
    INT64 = "int64"
    UINT8 = "uint8"
    UINT16 = "uint16"
    UINT32 = "uint32"
    UINT64 = "uint64"
    FLOAT32 = "float32"
    FLOAT64 = "float64"
    STRING = "string"
    VOID = "void"

class ConversionResult:
    def __init__(self, success: bool, value: Any = None, error: str = ""):
        self.success = success
        self.value = value
        self.error = error

class TypeDescriptor(ABC):
    def __init__(self, name: str, category: TypeCategory):
        self.name = name
        self.category = category

    @abstractmethod
    def to_string(self, value: Any) -> str:
        pass

    @abstractmethod
    def from_string(self, string: str) -> ConversionResult:
        pass

    @abstractmethod
    def equals(self, lhs: Any, rhs: Any) -> bool:
        pass

    @abstractmethod
    def hash(self, value: Any) -> int:
        pass

    @abstractmethod
    def get_cpp_type_name(self) -> str:
        pass

    @abstractmethod
    def get_python_type_name(self) -> str:
        pass

    @abstractmethod
    def get_java_type_name(self) -> str:
        pass

class PrimitiveTypeDescriptor(TypeDescriptor):
    def __init__(self, name: str, type_id: PrimitiveTypeId):
        super().__init__(name, TypeCategory.PRIMITIVE)
        self.type_id = type_id

    def to_string(self, value: Any) -> str:
        try:
            if self.type_id == PrimitiveTypeId.BOOL:
                return str(bool(value)).lower()
            return str(value)
        except Exception as e:
            raise ValueError(f"Type conversion error: {str(e)}")

    def from_string(self, string: str) -> ConversionResult:
        try:
            if self.type_id == PrimitiveTypeId.BOOL:
                return ConversionResult(True, string.lower() == "true")
            elif self.type_id in (PrimitiveTypeId.INT32, PrimitiveTypeId.INT64):
                return ConversionResult(True, int(string))
            elif self.type_id in (PrimitiveTypeId.FLOAT32, PrimitiveTypeId.FLOAT64):
                return ConversionResult(True, float(string))
            elif self.type_id == PrimitiveTypeId.STRING:
                return ConversionResult(True, string)
            return ConversionResult(False, error="Unsupported primitive type")
        except Exception as e:
            return ConversionResult(False, error=f"Conversion error: {str(e)}")

    def equals(self, lhs: Any, rhs: Any) -> bool:
        try:
            if self.type_id in (PrimitiveTypeId.FLOAT32, PrimitiveTypeId.FLOAT64):
                return abs(float(lhs) - float(rhs)) < 1e-6
            return lhs == rhs
        except Exception as e:
            raise ValueError(f"Type comparison error: {str(e)}")

    def hash(self, value: Any) -> int:
        return hash(value)

    def get_cpp_type_name(self) -> str:
        cpp_types = {
            PrimitiveTypeId.BOOL: "bool",
            PrimitiveTypeId.INT32: "int32_t",
            PrimitiveTypeId.INT64: "int64_t",
            PrimitiveTypeId.FLOAT32: "float",
            PrimitiveTypeId.FLOAT64: "double",
            PrimitiveTypeId.STRING: "std::string"
        }
        return cpp_types.get(self.type_id, "void")

    def get_python_type_name(self) -> str:
        python_types = {
            PrimitiveTypeId.BOOL: "bool",
            PrimitiveTypeId.INT32: "int",
            PrimitiveTypeId.INT64: "int",
            PrimitiveTypeId.FLOAT32: "float",
            PrimitiveTypeId.FLOAT64: "float",
            PrimitiveTypeId.STRING: "str"
        }
        return python_types.get(self.type_id, "None")

    def get_java_type_name(self) -> str:
        java_types = {
            PrimitiveTypeId.BOOL: "boolean",
            PrimitiveTypeId.INT32: "int",
            PrimitiveTypeId.INT64: "long",
            PrimitiveTypeId.FLOAT32: "float",
            PrimitiveTypeId.FLOAT64: "double",
            PrimitiveTypeId.STRING: "String"
        }
        return java_types.get(self.type_id, "void")

T = TypeVar('T')

class CollectionTypeDescriptor(TypeDescriptor, Generic[T]):
    def __init__(self, name: str, element_type: TypeDescriptor):
        super().__init__(name, TypeCategory.COLLECTION)
        self.element_type = element_type

    def to_string(self, value: Any) -> str:
        try:
            return json.dumps([self.element_type.to_string(item) for item in value])
        except Exception as e:
            raise ValueError(f"Collection conversion error: {str(e)}")

    def from_string(self, string: str) -> ConversionResult:
        try:
            items = json.loads(string)
            result = []
            for item in items:
                conv = self.element_type.from_string(str(item))
                if not conv.success:
                    return ConversionResult(False, error=f"Element conversion failed: {conv.error}")
                result.append(conv.value)
            return ConversionResult(True, result)
        except Exception as e:
            return ConversionResult(False, error=f"Collection conversion error: {str(e)}")

    def equals(self, lhs: Any, rhs: Any) -> bool:
        if len(lhs) != len(rhs):
            return False
        return all(self.element_type.equals(l, r) for l, r in zip(lhs, rhs))

    def hash(self, value: Any) -> int:
        return hash(tuple(self.element_type.hash(item) for item in value))

    def get_cpp_type_name(self) -> str:
        return f"std::vector<{self.element_type.get_cpp_type_name()}>"

    def get_python_type_name(self) -> str:
        return f"List[{self.element_type.get_python_type_name()}]"

    def get_java_type_name(self) -> str:
        return f"List<{self.element_type.get_java_type_name()}>"

class TypeRegistry:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TypeRegistry, cls).__new__(cls)
            cls._instance._types = {}
        return cls._instance

    def register_type(self, descriptor: TypeDescriptor) -> None:
        self._types[descriptor.name] = descriptor

    def get_type(self, name: str) -> TypeDescriptor:
        if name not in self._types:
            raise KeyError(f"Type not found: {name}")
        return self._types[name]

    def is_type_registered(self, name: str) -> bool:
        return name in self._types

# Initialize primitive types
def initialize_primitive_types():
    registry = TypeRegistry()
    
    primitives = [
        ("bool", PrimitiveTypeId.BOOL),
        ("int32", PrimitiveTypeId.INT32),
        ("int64", PrimitiveTypeId.INT64),
        ("float32", PrimitiveTypeId.FLOAT32),
        ("float64", PrimitiveTypeId.FLOAT64),
        ("string", PrimitiveTypeId.STRING)
    ]
    
    for name, type_id in primitives:
        descriptor = PrimitiveTypeDescriptor(name, type_id)
        registry.register_type(descriptor)

# Initialize types when module is imported
initialize_primitive_types()