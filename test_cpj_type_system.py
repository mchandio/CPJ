"""
Comprehensive test suite for the CPJ type system.
"""
import unittest
from cpj_type_system import TypeSystem, TypeKind, WallSection
from typing import Dict, Any

class TestCPJTypeSystem(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.type_system = TypeSystem()
        
    def test_primitive_types(self):
        """Test primitive type handling"""
        primitives = ['int', 'float', 'str', 'bool', 'void']
        for p in primitives:
            t = self.type_system.get_type(p)
            self.assertIsNotNone(t)
            self.assertEqual(t.kind, TypeKind.PRIMITIVE)
            self.assertEqual(t.name, p)
            
    def test_custom_types(self):
        """Test custom type definitions"""
        # Define a custom class type
        class_type = WallSection(
            kind=TypeKind.CLASS,
            name='MyClass',
            constraints={'fields': {'x': 'int', 'y': 'float'}}
        )
        self.type_system.add_type(class_type)
        
        # Retrieve and verify
        t = self.type_system.get_type('MyClass')
        self.assertIsNotNone(t)
        self.assertEqual(t.kind, TypeKind.CLASS)
        self.assertEqual(t.constraints['fields']['x'], 'int')
        
    def test_function_types(self):
        """Test function type handling"""
        func_type = WallSection(
            kind=TypeKind.FUNCTION,
            name='my_func',
            constraints={
                'params': [{'name': 'x', 'type': 'int'}],
                'return_type': 'float'
            }
        )
        self.type_system.add_type(func_type)
        
        t = self.type_system.get_type('my_func')
        self.assertIsNotNone(t)
        self.assertEqual(t.kind, TypeKind.FUNCTION)
        self.assertEqual(t.constraints['return_type'], 'float')
        
    def test_compound_types(self):
        """Test compound type handling"""
        # Define a compound type (e.g., array or tuple)
        array_type = WallSection(
            kind=TypeKind.COMPOUND,
            name='Array<int>',
            constraints={'element_type': 'int'}
        )
        self.type_system.add_type(array_type)
        
        t = self.type_system.get_type('Array<int>')
        self.assertIsNotNone(t)
        self.assertEqual(t.kind, TypeKind.COMPOUND)
        self.assertEqual(t.constraints['element_type'], 'int')
        
    def test_module_types(self):
        """Test module type handling"""
        module_type = WallSection(
            kind=TypeKind.MODULE,
            name='MyModule',
            constraints={
                'exports': {
                    'func1': 'Function',
                    'Class1': 'Class'
                }
            }
        )
        self.type_system.add_type(module_type)
        
        t = self.type_system.get_type('MyModule')
        self.assertIsNotNone(t)
        self.assertEqual(t.kind, TypeKind.MODULE)
        self.assertIn('func1', t.constraints['exports'])
        
    def test_variable_types(self):
        """Test variable type handling"""
        var_type = WallSection(
            kind=TypeKind.VARIABLE,
            name='my_var',
            constraints={'type': 'int', 'mutable': True}
        )
        self.type_system.add_type(var_type)
        
        t = self.type_system.get_type('my_var')
        self.assertIsNotNone(t)
        self.assertEqual(t.kind, TypeKind.VARIABLE)
        self.assertTrue(t.constraints['mutable'])
        
    def test_undefined_type(self):
        """Test undefined type handling"""
        t = self.type_system.get_type('NonExistentType')
        self.assertIsNone(t)
        
    def test_type_constraints(self):
        """Test type constraint handling"""
        # Define a constrained type
        constrained_type = WallSection(
            kind=TypeKind.CLASS,
            name='Vector',
            constraints={
                'type_params': ['T'],
                'bounds': {'T': ['Numeric']},
                'methods': {
                    'add': {
                        'params': [{'name': 'other', 'type': 'Vector<T>'}],
                        'return_type': 'Vector<T>'
                    }
                }
            }
        )
        self.type_system.add_type(constrained_type)
        
        t = self.type_system.get_type('Vector')
        self.assertIsNotNone(t)
        self.assertIn('T', t.constraints['type_params'])
        self.assertEqual(t.constraints['bounds']['T'], ['Numeric'])
        
    def test_type_relationships(self):
        """Test type relationship handling"""
        # Define related types
        parent = WallSection(
            kind=TypeKind.CLASS,
            name='Parent',
            constraints={'methods': {'speak': 'void'}}
        )
        child = WallSection(
            kind=TypeKind.CLASS,
            name='Child',
            constraints={
                'extends': 'Parent',
                'methods': {'cry': 'void'}
            }
        )
        
        self.type_system.add_type(parent)
        self.type_system.add_type(child)
        
        child_type = self.type_system.get_type('Child')
        self.assertEqual(child_type.constraints['extends'], 'Parent')
        
    def test_type_system_reset(self):
        """Test type system reset functionality"""
        # Add a custom type
        custom_type = WallSection(
            kind=TypeKind.CLASS,
            name='Custom',
            constraints={}
        )
        self.type_system.add_type(custom_type)
        
        # Reset type system
        self.type_system = TypeSystem()
        
        # Verify only primitives exist
        self.assertIsNone(self.type_system.get_type('Custom'))
        self.assertIsNotNone(self.type_system.get_type('int'))

if __name__ == '__main__':
    unittest.main()