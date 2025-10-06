"""Test script for the CPJ House AI system."""

import unittest
import numpy as np
from cpj_type_system import TypeSystem
from cpj_runtime import Runtime
from cpj_house_main_runtime import HouseRuntime
from cpj_house_ai import (
    AIKind, LearningType, MemoryType, AIConfig,
    NeuralNetwork, MLModel, Agent, Sensor, Actuator,
    Layer, Experience
)
from cpj_house_ai_runtime import AIRuntime, HouseAISystem

class TestHouseAI(unittest.TestCase):
    """Test cases for the House AI system."""
    
    def setUp(self):
        """Set up test environment."""
        self.runtime = HouseRuntime()
        self.ai_system = self.runtime.ai
        self.ai_runtime = self.ai_system.get_runtime()
        
    def test_neural_network(self):
        """Test neural network creation and operation."""
        # Create network
        network = self.ai_runtime.create_neural_network(
            "test_net",
            AIConfig(learning_rate=0.01)
        )
        
        # Add layers
        network.add_layer(2, 4)  # Input layer
        network.add_layer(4, 3)  # Hidden layer
        network.add_layer(3, 1)  # Output layer
        
        # Test forward pass
        input_data = np.array([[1.0, 2.0]])
        output = network.forward(input_data)
        self.assertEqual(output.shape, (1, 1))
        
    def test_agent_learning(self):
        """Test agent learning capabilities."""
        # Create agent
        agent = self.ai_runtime.create_agent(
            "test_agent",
            AIConfig(
                learning_rate=0.01,
                batch_size=4,
                memory_size=100
            )
        )
        
        # Create and set neural network
        net = self.ai_runtime.create_neural_network("agent_net")
        net.add_layer(2, 4)
        net.add_layer(4, 2)
        agent.set_network(net)
        
        # Add experiences
        for _ in range(5):
            exp = Experience(
                state=np.array([1.0, 0.0]),
                action=np.array([0.5, 0.5]),
                reward=1.0,
                next_state=np.array([0.8, 0.2]),
                done=False
            )
            agent.memory.add(exp)
            
        # Test learning
        experiences = agent.memory.sample(4)
        agent.learn(experiences)
        
    def test_sensor_processing(self):
        """Test sensor data processing."""
        # Create sensor
        sensor = self.ai_runtime.create_sensor("test_sensor")
        
        # Add preprocessors
        sensor.add_preprocessor(lambda x: x * 2)
        sensor.add_preprocessor(lambda x: x + 1)
        
        # Test processing
        result = sensor.process(5)
        self.assertEqual(result, 11)  # (5 * 2) + 1
        
    def test_actuator_execution(self):
        """Test actuator action execution."""
        # Create actuator
        actuator = self.ai_runtime.create_actuator("test_actuator")
        
        # Register action
        def test_action(value):
            return value * 2
        actuator.register_action("double", test_action)
        
        # Test execution
        result = actuator.execute("double", 5)
        self.assertEqual(result, 10)
        
    def test_model_integration(self):
        """Test ML model integration."""
        # Create model
        model = self.ai_runtime.create_model(
            "test_model",
            AIConfig(learning_rate=0.01)
        )
        
        # Implement test model
        class TestModel(Model):
            def train(self, x, y):
                pass
                
            def predict(self, x):
                return x * 2
                
            def save(self, path):
                pass
                
            def load(self, path):
                pass
        
        # Set and test model
        model.set_model(TestModel())
        result = model.predict(np.array([1, 2, 3]))
        np.testing.assert_array_equal(result, np.array([2, 4, 6]))
        
    def test_system_integration(self):
        """Test overall system integration."""
        # Process sensor data
        sensor_data = self.ai_system.process_sensor_data()
        self.assertIn("temperature", sensor_data)
        self.assertIn("light", sensor_data)
        self.assertIn("motion", sensor_data)
        
        # Test system update
        self.ai_system.update()
        
        # Verify components exist
        self.assertIsNotNone(self.ai_runtime.get_agent("comfort_optimizer"))
        self.assertIsNotNone(self.ai_runtime.get_agent("security_monitor"))
        self.assertIsNotNone(self.ai_runtime.get_sensor("temperature"))
        self.assertIsNotNone(self.ai_runtime.get_actuator("hvac"))

if __name__ == '__main__':
    unittest.main()