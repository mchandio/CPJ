"""CPJ House AI Runtime
Provides runtime integration for AI features in the house metaphor.
"""

from typing import Dict, List, Optional, Any, Tuple
from cpj_house_ai import (
    AIKind, LearningType, MemoryType, AIConfig,
    NeuralNetwork, MLModel, Agent, Sensor, Actuator
)
from cpj_type_system import TypeSystem
from cpj_runtime import Runtime
from cpj_enums import AccessLevel

class AIRuntime:
    """Runtime manager for AI features"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._networks: Dict[str, NeuralNetwork] = {}
        self._models: Dict[str, MLModel] = {}
        self._agents: Dict[str, Agent] = {}
        self._sensors: Dict[str, Sensor] = {}
        self._actuators: Dict[str, Actuator] = {}
        
    def create_neural_network(self, name: str, config: Optional[AIConfig] = None) -> NeuralNetwork:
        """Create a new neural network"""
        network = NeuralNetwork(
            type_system=self._type_system,
            name=name,
            config=config or AIConfig()
        )
        self._networks[name] = network
        return network
        
    def create_model(self, name: str, config: Optional[AIConfig] = None) -> MLModel:
        """Create a new ML model"""
        model = MLModel(
            type_system=self._type_system,
            name=name,
            config=config or AIConfig()
        )
        self._models[name] = model
        return model
        
    def create_agent(self, name: str, config: Optional[AIConfig] = None) -> Agent:
        """Create a new AI agent"""
        agent = Agent(
            type_system=self._type_system,
            name=name,
            config=config or AIConfig()
        )
        self._agents[name] = agent
        return agent
        
    def create_sensor(self, name: str) -> Sensor:
        """Create a new sensor"""
        sensor = Sensor(type_system=self._type_system, name=name)
        self._sensors[name] = sensor
        return sensor
        
    def create_actuator(self, name: str) -> Actuator:
        """Create a new actuator"""
        actuator = Actuator(type_system=self._type_system, name=name)
        self._actuators[name] = actuator
        return actuator
        
    def get_network(self, name: str) -> Optional[NeuralNetwork]:
        """Get a neural network by name"""
        return self._networks.get(name)
        
    def get_model(self, name: str) -> Optional[MLModel]:
        """Get a model by name"""
        return self._models.get(name)
        
    def get_agent(self, name: str) -> Optional[Agent]:
        """Get an agent by name"""
        return self._agents.get(name)
        
    def get_sensor(self, name: str) -> Optional[Sensor]:
        """Get a sensor by name"""
        return self._sensors.get(name)
        
    def get_actuator(self, name: str) -> Optional[Actuator]:
        """Get an actuator by name"""
        return self._actuators.get(name)
        
    def list_components(self, kind: Optional[AIKind] = None) -> List[str]:
        """List AI components, optionally filtered by kind"""
        components = []
        if kind is None or kind == AIKind.NEURAL:
            components.extend(self._networks.keys())
        if kind is None or kind == AIKind.MODEL:
            components.extend(self._models.keys())
        if kind is None or kind == AIKind.AGENT:
            components.extend(self._agents.keys())
        if kind is None or kind == AIKind.SENSOR:
            components.extend(self._sensors.keys())
        if kind is None or kind == AIKind.ACTUATOR:
            components.extend(self._actuators.keys())
        return components
        
    def remove_component(self, name: str) -> bool:
        """Remove an AI component by name"""
        for collection in [self._networks, self._models, self._agents, 
                         self._sensors, self._actuators]:
            if name in collection:
                del collection[name]
                return True
        return False
        
    def clear(self):
        """Remove all AI components"""
        self._networks.clear()
        self._models.clear()
        self._agents.clear()
        self._sensors.clear()
        self._actuators.clear()

class HouseAISystem:
    """Integration system for house AI features"""
    
    def __init__(self, runtime: Runtime):
        self._runtime = runtime
        self._ai_runtime = AIRuntime(runtime.type_system)
        self._setup_default_components()
        
    def _setup_default_components(self):
        """Set up default AI components for the house"""
        # Create environmental sensors
        temp_sensor = self._ai_runtime.create_sensor("temperature")
        light_sensor = self._ai_runtime.create_sensor("light")
        motion_sensor = self._ai_runtime.create_sensor("motion")
        
        # Create control actuators
        hvac = self._ai_runtime.create_actuator("hvac")
        lighting = self._ai_runtime.create_actuator("lighting")
        security = self._ai_runtime.create_actuator("security")
        
        # Create comfort optimization agent
        comfort_agent = self._ai_runtime.create_agent(
            "comfort_optimizer",
            AIConfig(
                learning_rate=0.001,
                batch_size=32,
                hidden_layers=[64, 32],
                memory_size=5000
            )
        )
        
        # Create security monitoring agent
        security_agent = self._ai_runtime.create_agent(
            "security_monitor",
            AIConfig(
                learning_rate=0.002,
                batch_size=16,
                hidden_layers=[32, 16],
                memory_size=1000
            )
        )
        
        # Set up neural networks for agents
        comfort_net = self._ai_runtime.create_neural_network("comfort_net")
        comfort_net.add_layer(3, 64)  # 3 inputs: temp, light, motion
        comfort_net.add_layer(64, 32)
        comfort_net.add_layer(32, 2)  # 2 outputs: hvac, lighting
        comfort_agent.set_network(comfort_net)
        
        security_net = self._ai_runtime.create_neural_network("security_net")
        security_net.add_layer(1, 32)  # 1 input: motion
        security_net.add_layer(32, 16)
        security_net.add_layer(16, 1)  # 1 output: security level
        security_agent.set_network(security_net)
        
    def get_runtime(self) -> AIRuntime:
        """Get the AI runtime"""
        return self._ai_runtime
        
    def process_sensor_data(self) -> Dict[str, Any]:
        """Process all sensor data"""
        results = {}
        for name, sensor in self._ai_runtime._sensors.items():
            results[name] = sensor.process(self._get_sensor_data(name))
        return results
        
    def execute_actions(self, actions: Dict[str, Tuple[str, Any]]):
        """Execute actions through actuators"""
        for actuator_name, (action_name, params) in actions.items():
            actuator = self._ai_runtime.get_actuator(actuator_name)
            if actuator:
                actuator.execute(action_name, **params)
                
    def _get_sensor_data(self, sensor_name: str) -> Any:
        """Get raw data for a sensor"""
        # In a real implementation, this would interface with actual sensors
        # For now, return mock data
        if sensor_name == "temperature":
            return 22.0  # 22°C
        elif sensor_name == "light":
            return 0.7   # 70% brightness
        elif sensor_name == "motion":
            return 0.0   # No motion
        return None
        
    def update(self):
        """Update AI systems"""
        # Process sensor data
        sensor_data = self.process_sensor_data()
        
        # Update comfort agent
        comfort_agent = self._ai_runtime.get_agent("comfort_optimizer")
        if comfort_agent:
            state = [
                sensor_data["temperature"],
                sensor_data["light"],
                sensor_data["motion"]
            ]
            actions = comfort_agent.act(state)
            
            # Execute comfort-related actions
            self.execute_actions({
                "hvac": ("set_temperature", {"temp": 20 + actions[0] * 5}),
                "lighting": ("set_brightness", {"level": max(0, min(1, actions[1]))})
            })
            
        # Update security agent
        security_agent = self._ai_runtime.get_agent("security_monitor")
        if security_agent:
            state = [sensor_data["motion"]]
            security_level = security_agent.act(state)[0]
            
            # Execute security-related actions
            if security_level > 0.8:  # High security alert
                self.execute_actions({
                    "security": ("trigger_alert", {"level": "high"})
                })