"""Test suite for CPJ type system functionality."""
import pytest
from cpj_type_system import TypeSystem, TypeKind, Type, TypeDef
from typing import Any, Dict, List, Optional

@pytest.mark.type_system
class TestCPJTypeSystem:
    """Test cases for the CPJ type system."""
    
    @pytest.fixture
    def type_system(self) -> TypeSystem:
        """Create a fresh type system instance for each test."""
        return TypeSystem()
        
    def test_basic_types(self, type_system):
        """Test handling of basic types."""
        basic_types = [
            ("int", TypeKind.INT),
            ("float", TypeKind.FLOAT),
            ("str", TypeKind.STRING),
            ("bool", TypeKind.BOOL),
            ("void", TypeKind.VOID)
        ]
        
        for name, kind in basic_types:
            type_obj = type_system.get_type(name)
            assert type_obj is not None
            assert type_obj.kind == kind
            
    def test_custom_type_definition(self, type_system):
        """Test definition and usage of custom types."""
        type_def = """
        type Point {
            x: float
            y: float
        }
        """
        type_system.define_type("Point", type_def)
        point_type = type_system.get_type("Point")
        assert point_type is not None
        assert point_type.kind == TypeKind.CUSTOM
        assert "x" in point_type.fields
        assert "y" in point_type.fields
        
    def test_type_inference(self, type_system):
        """Test type inference capabilities."""
        expressions = [
            ("42", "int"),
            ("3.14", "float"),
            ('"hello"', "str"),
            ("true", "bool"),
            ("Point(1.0, 2.0)", "Point"),
            ("[1, 2, 3]", "List[int]"),
            ('{"a": 1}', "Dict[str, int]")
        ]
        
        # Define Point type first
        type_system.define_type("Point", "type Point { x: float, y: float }")
        
        for expr, expected_type in expressions:
            inferred = type_system.infer_type(expr)
            assert str(inferred) == expected_type
            
    def test_type_checking(self, type_system):
        """Test type checking functionality."""
        type_system.define_type("Point", "type Point { x: float, y: float }")
        
        valid_assignments = [
            ("x: int = 42", True),
            ("y: float = 3.14", True),
            ('s: str = "hello"', True),
            ("p: Point = Point(1.0, 2.0)", True)
        ]
        
        invalid_assignments = [
            ("x: int = 3.14", False),
            ("y: float = 42", False),
            ('s: str = 123', False),
            ("p: Point = (1, 2)", False)
        ]
        
        for assignment, expected in valid_assignments + invalid_assignments:
            result = type_system.check_types(assignment)
            assert result == expected
            
    def test_function_types(self, type_system):
        """Test function type checking and inference."""
        function_def = """
        function add(x: int, y: int) -> int {
            return x + y
        }
        """
        
        func_type = type_system.get_function_type(function_def)
        assert func_type is not None
        assert len(func_type.params) == 2
        assert func_type.return_type.kind == TypeKind.INT
        
        # Test invalid function calls
        invalid_calls = [
            "add(1.0, 2)",
            'add("1", 2)',
            "add(1)",
            "add(1, 2, 3)"
        ]
        
        for call in invalid_calls:
            with pytest.raises(Exception):
                type_system.check_function_call(call)
                
    def test_generic_types(self, type_system):
        """Test handling of generic types."""
        type_system.define_type("Box", "type Box[T] { value: T }")
        
        # Test generic instantiation
        box_int = type_system.instantiate_generic("Box", ["int"])
        assert box_int is not None
        assert box_int.fields["value"].kind == TypeKind.INT
        
        box_str = type_system.instantiate_generic("Box", ["str"])
        assert box_str is not None
        assert box_str.fields["value"].kind == TypeKind.STRING
        
    def test_type_compatibility(self, type_system):
        """Test type compatibility checks."""
        compatibilities = [
            ("int", "float", True),
            ("int", "str", False),
            ("float", "int", False),
            ("bool", "int", False),
            ("Point", "Point", True),
            ("List[int]", "List[float]", False)
        ]
        
        type_system.define_type("Point", "type Point { x: float, y: float }")
        
        for type1, type2, expected in compatibilities:
            t1 = type_system.get_type(type1)
            t2 = type_system.get_type(type2)
            assert type_system.is_compatible(t1, t2) == expected
            
    def test_type_system_errors(self, type_system):
        """Test error handling in type system."""
        with pytest.raises(Exception):
            type_system.get_type("NonExistentType")
            
        with pytest.raises(Exception):
            type_system.define_type("int", "type int { x: int }")  # Redefining builtin
            
        with pytest.raises(Exception):
            type_system.define_type("Invalid", "type Invalid { 123: int }")  # Invalid field name
            
    def test_type_system_inheritance(self, type_system):
        """Test type inheritance functionality."""
        type_system.define_type("Shape", """
        type Shape {
            color: str
            area: float
        }
        """)
        
        type_system.define_type("Circle", """
        type Circle extends Shape {
            radius: float
        }
        """)
        
        circle_type = type_system.get_type("Circle")
        assert circle_type is not None
        assert "color" in circle_type.fields
        assert "area" in circle_type.fields
        assert "radius" in circle_type.fields
        
    @pytest.mark.parametrize("type_expr,valid", [
        ("List[int]", True),
        ("Dict[str, int]", True),
        ("Set[bool]", True),
        ("List[List[int]]", True),
        ("Dict[int, List[str]]", True),
        ("List", False),
        ("Dict[str]", False),
        ("Set[Unknown]", False)
    ])
    def test_container_types(self, type_system, type_expr: str, valid: bool):
        """Test handling of container types."""
        if valid:
            type_obj = type_system.parse_type_expression(type_expr)
            assert type_obj is not None
        else:
            with pytest.raises(Exception):
                type_system.parse_type_expression(type_expr)