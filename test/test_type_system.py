"""Test suite for CPJ's type system.
Tests type checking, inference, validation and AI-specific types.
"""

import unittest
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node, NodeType
from cpj_house_ai import AIKind, NeuralNetwork, MLModel, Agent, Sensor, Actuator

class TestTypeSystem(unittest.TestCase):
    def setUp(self):
        self.type_system = TypeSystem()

    def test_basic_types(self):
        """Test basic type definitions and checking"""
        # Test primitive types
        self.assertEqual(self.type_system.get_type("int").kind, TypeKind.INT)
        self.assertEqual(self.type_system.get_type("float").kind, TypeKind.FLOAT)
        self.assertEqual(self.type_system.get_type("str").kind, TypeKind.STRING)
        self.assertEqual(self.type_system.get_type("bool").kind, TypeKind.BOOL)

    def test_compound_types(self):
        """Test compound type definitions"""
        # Define a compound type
        self.type_system.define_type("Point", {
            "x": self.type_system.get_type("float"),
            "y": self.type_system.get_type("float")
        })

        point_type = self.type_system.get_type("Point")
        self.assertIsNotNone(point_type)
        self.assertEqual(point_type.fields["x"].kind, TypeKind.FLOAT)
        self.assertEqual(point_type.fields["y"].kind, TypeKind.FLOAT)

    def test_ai_types(self):
        """Test AI-specific type handling"""
        # Test neural network type
        nn = NeuralNetwork(type_system=self.type_system, name="TestNN")
        nn_type = self.type_system.get_node_type(nn)
        self.assertEqual(nn_type.kind, TypeKind.AI)
        self.assertEqual(nn.kind, AIKind.NEURAL)

        # Test ML model type
        model = MLModel(type_system=self.type_system, name="TestModel")
        model_type = self.type_system.get_node_type(model)
        self.assertEqual(model_type.kind, TypeKind.AI)
        self.assertEqual(model.kind, AIKind.MODEL)

    def test_type_inference(self):
        """Test type inference capabilities"""
        # Test basic inference
        expr = Node(node_type=NodeType.BINARY_OP)
        expr.left = Node(node_type=NodeType.LITERAL, value=5)
        expr.right = Node(node_type=NodeType.LITERAL, value=3.14)
        expr.operator = "+"

        result_type = self.type_system.infer_type(expr)
        self.assertEqual(result_type.kind, TypeKind.FLOAT)

        # Test AI-related inference
        nn_node = NeuralNetwork(type_system=self.type_system)
        nn_node.add_layer(2, 1, "sigmoid")
        input_type = self.type_system.infer_input_type(nn_node)
        output_type = self.type_system.infer_output_type(nn_node)
        
        self.assertEqual(input_type.dimensions[0], 2)
        self.assertEqual(output_type.dimensions[0], 1)

    def test_type_validation(self):
        """Test type validation rules"""
        # Test basic validation
        valid_assign = Node(node_type=NodeType.ASSIGNMENT)
        valid_assign.target = Node(node_type=NodeType.IDENTIFIER, name="x")
        valid_assign.value = Node(node_type=NodeType.LITERAL, value=42)
        
        self.assertTrue(self.type_system.validate_node(valid_assign))

        # Test invalid assignment
        invalid_assign = Node(node_type=NodeType.ASSIGNMENT)
        invalid_assign.target = Node(node_type=NodeType.IDENTIFIER, name="x")
        invalid_assign.value = Node(node_type=NodeType.IDENTIFIER, name="undefined_var")
        
        with self.assertRaises(TypeError):
            self.type_system.validate_node(invalid_assign)

    def test_ai_component_compatibility(self):
        """Test compatibility between AI components"""
        # Create AI components
        sensor = Sensor(type_system=self.type_system, name="camera")
        nn = NeuralNetwork(type_system=self.type_system, name="vision")
        agent = Agent(type_system=self.type_system, name="controller")
        actuator = Actuator(type_system=self.type_system, name="motor")

        # Test component connections
        nn.add_layer(784, 128, "relu")  # Image input size
        nn.add_layer(128, 10, "softmax")  # Classification output
        agent.set_network(nn)

        # Validate connections
        self.assertTrue(self.type_system.validate_connection(sensor, nn))
        self.assertTrue(self.type_system.validate_connection(nn, agent))
        self.assertTrue(self.type_system.validate_connection(agent, actuator))

    def test_wall_section_types(self):
        """Test wall section specific types"""
        # Create wall section with AI
        wall = Node(node_type=NodeType.WALL_SECTION)
        wall.sensor = Sensor(type_system=self.type_system, name="temp_sensor")
        wall.controller = Agent(type_system=self.type_system, name="temp_control")
        wall.actuator = Actuator(type_system=self.type_system, name="heater")

        # Validate wall section
        self.assertTrue(self.type_system.validate_wall_section(wall))

        # Test invalid configuration
        invalid_wall = Node(node_type=NodeType.WALL_SECTION)
        invalid_wall.sensor = Agent(type_system=self.type_system, name="wrong_type")
        
        with self.assertRaises(TypeError):
            self.type_system.validate_wall_section(invalid_wall)

    def test_memory_management(self):
        """Test type system memory management"""
        # Test type registration
        self.type_system.register_type("CustomVec", {
            "elements": self.type_system.get_type("float"),
            "size": self.type_system.get_type("int")
        })
        
        # Test type lookup and caching
        t1 = self.type_system.get_type("CustomVec")
        t2 = self.type_system.get_type("CustomVec")
        self.assertIs(t1, t2)  # Should return cached instance

        # Test type deletion
        self.type_system.unregister_type("CustomVec")
        with self.assertRaises(KeyError):
            self.type_system.get_type("CustomVec")

    def test_type_conversion(self):
        """Test type conversion rules"""
        # Test numeric conversions
        int_type = self.type_system.get_type("int")
        float_type = self.type_system.get_type("float")
        
        self.assertTrue(self.type_system.can_convert(int_type, float_type))
        self.assertFalse(self.type_system.can_convert(float_type, int_type))

        # Test AI type conversions
        sensor_data = np.random.randn(28, 28)  # Image data
        nn = NeuralNetwork(type_system=self.type_system)
        nn.add_layer(784, 10)  # Expecting flattened input
        
        converted_data = self.type_system.convert_for_neural_net(sensor_data, nn)
        self.assertEqual(converted_data.shape, (1, 784))

    def test_type_hierarchies(self):
        """Test type inheritance and hierarchies"""
        # Define base type
        self.type_system.define_type("AIComponent", {
            "name": self.type_system.get_type("str"),
            "kind": self.type_system.get_type("str")
        })

        # Define derived type
        self.type_system.define_type("NeuralNet", {
            "name": self.type_system.get_type("str"),
            "kind": self.type_system.get_type("str"),
            "layers": self.type_system.get_type("int")
        }, parent="AIComponent")

        # Test inheritance
        nn_type = self.type_system.get_type("NeuralNet")
        self.assertTrue(self.type_system.is_subtype(nn_type, 
                                                  self.type_system.get_type("AIComponent")))

if __name__ == '__main__':
    unittest.main()