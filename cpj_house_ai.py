"""CPJ House AI System
Provides artificial intelligence features for the house metaphor.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Set, Callable, TypeVar, Generic, Union, Tuple
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node
from cpj_enums import AccessLevel, NodeType
import numpy as np
from abc import ABC, abstractmethod

T = TypeVar('T')

class AIKind(Enum):
    """Types of AI features"""
    NEURAL = auto()      # Neural Networks
    MODEL = auto()       # Machine Learning Models
    AGENT = auto()       # AI Agents
    SENSOR = auto()      # Input Processing
    ACTUATOR = auto()    # Output Actions

class LearningType(Enum):
    """Types of learning mechanisms"""
    SUPERVISED = auto()
    UNSUPERVISED = auto()
    REINFORCEMENT = auto()
    TRANSFER = auto()
    META = auto()

class MemoryType(Enum):
    """Types of AI memory"""
    SHORT_TERM = auto()
    LONG_TERM = auto()
    WORKING = auto()
    EPISODIC = auto()
    SEMANTIC = auto()

@dataclass
class AIConfig:
    """Configuration for AI components"""
    learning_rate: float = 0.001
    batch_size: int = 32
    hidden_layers: List[int] = field(default_factory=lambda: [64, 32])
    activation: str = "relu"
    optimizer: str = "adam"
    memory_size: int = 10000
    exploration_rate: float = 0.1

@dataclass
class Experience:
    """Single experience unit for learning"""
    state: Any
    action: Any
    reward: float
    next_state: Any
    done: bool
    metadata: Dict[str, Any] = field(default_factory=dict)

class Layer:
    """Neural network layer"""
    def __init__(self, input_size: int, output_size: int, activation: str = "relu"):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))
        self.activation = activation
        
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """Forward pass through the layer"""
        self.inputs = inputs
        self.z = np.dot(inputs, self.weights) + self.biases
        self.a = self._activate(self.z)
        return self.a
        
    def _activate(self, x: np.ndarray) -> np.ndarray:
        """Apply activation function"""
        if self.activation == "relu":
            return np.maximum(0, x)
        elif self.activation == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif self.activation == "tanh":
            return np.tanh(x)
        return x

@dataclass
class NeuralNetwork(Node):
    """Neural network implementation"""
    kind: AIKind = field(default=AIKind.NEURAL)
    config: AIConfig = field(default_factory=AIConfig)
    _layers: List[Layer] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        location = kwargs.pop('location', (0, 0))
        name = kwargs.pop('name', 'neural_network')
        super().__init__(node_type=NodeType.AI, location=location, name=name)
        self._type_system = type_system
        self.config = kwargs.get('config', AIConfig())
        
    def add_layer(self, input_size: int, output_size: int, activation: str = "relu"):
        """Add a layer to the network"""
        layer = Layer(input_size, output_size, activation)
        self._layers.append(layer)
        
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """Forward pass through the network"""
        x = inputs
        for layer in self._layers:
            x = layer.forward(x)
        return x
        
    def train(self, x: np.ndarray, y: np.ndarray, epochs: int = 100) -> List[float]:
        """Train the network"""
        losses = []
        for epoch in range(epochs):
            # Mini-batch training
            indices = np.random.permutation(len(x))
            for i in range(0, len(x), self.config.batch_size):
                batch_idx = indices[i:i + self.config.batch_size]
                x_batch = x[batch_idx]
                y_batch = y[batch_idx]
                
                # Forward pass
                output = self.forward(x_batch)
                
                # Compute loss
                loss = np.mean((output - y_batch) ** 2)
                losses.append(loss)
                
                # Backward pass (simplified)
                error = output - y_batch
                for layer in reversed(self._layers):
                    grad = np.dot(layer.inputs.T, error)
                    layer.weights -= self.config.learning_rate * grad
                    error = np.dot(error, layer.weights.T)
                    
        return losses

class Model(ABC):
    """Abstract base class for machine learning models"""
    @abstractmethod
    def train(self, x: np.ndarray, y: np.ndarray) -> None:
        pass
        
    @abstractmethod
    def predict(self, x: np.ndarray) -> np.ndarray:
        pass
        
    @abstractmethod
    def save(self, path: str) -> None:
        pass
        
    @abstractmethod
    def load(self, path: str) -> None:
        pass

@dataclass
class MLModel(Node):
    """Machine learning model implementation"""
    name: str = field(default="")
    kind: AIKind = field(default=AIKind.MODEL)
    model: Optional[Model] = None
    config: AIConfig = field(default_factory=AIConfig)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.AI, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.config = kwargs.get('config', AIConfig())
        
    def set_model(self, model: Model):
        """Set the underlying model"""
        self.model = model
        
    def train(self, x: np.ndarray, y: np.ndarray) -> None:
        """Train the model"""
        if self.model:
            self.model.train(x, y)
            
    def predict(self, x: np.ndarray) -> np.ndarray:
        """Make predictions"""
        if self.model:
            return self.model.predict(x)
        return np.array([])

@dataclass
class Memory:
    """Memory storage for AI agents"""
    capacity: int
    _buffer: List[Experience] = field(default_factory=list)
    
    def add(self, experience: Experience):
        """Add an experience to memory"""
        if len(self._buffer) >= self.capacity:
            self._buffer.pop(0)
        self._buffer.append(experience)
        
    def sample(self, batch_size: int) -> List[Experience]:
        """Sample experiences from memory"""
        import random
        return random.sample(self._buffer, min(batch_size, len(self._buffer)))
        
    def clear(self):
        """Clear all memories"""
        self._buffer.clear()

@dataclass
class Agent(Node):
    """AI agent implementation"""
    name: str = field(default="")
    kind: AIKind = field(default=AIKind.AGENT)
    config: AIConfig = field(default_factory=AIConfig)
    memory: Memory = field(default_factory=lambda: Memory(10000))
    _neural_net: Optional[NeuralNetwork] = None
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.AI, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.config = kwargs.get('config', AIConfig())
        self.memory = Memory(self.config.memory_size)
        
    def set_network(self, network: NeuralNetwork):
        """Set the agent's neural network"""
        self._neural_net = network
        
    def act(self, state: np.ndarray) -> np.ndarray:
        """Choose an action based on current state"""
        if self._neural_net is None or not self._neural_net._layers:
            raise ValueError("Neural network is not set or has no layers.")
        if np.random.random() < self.config.exploration_rate:
            return np.random.randn(self._neural_net._layers[-1].biases.shape[1])
        return self._neural_net.forward(state)
        
    def learn(self, experiences: List[Experience]):
        """Learn from experiences"""
        if not self._neural_net:
            return
            
        # Prepare training data
        states = np.array([exp.state for exp in experiences])
        actions = np.array([exp.action for exp in experiences])
        rewards = np.array([exp.reward for exp in experiences])
        next_states = np.array([exp.next_state for exp in experiences])
        dones = np.array([exp.done for exp in experiences])
        
        # Q-learning update
        current_q = self._neural_net.forward(states)
        next_q = self._neural_net.forward(next_states)
        target_q = current_q.copy()
        
        for i in range(len(experiences)):
            if dones[i]:
                target_q[i] = rewards[i]
            else:
                target_q[i] = rewards[i] + 0.99 * np.max(next_q[i])
                
        # Train the network
        self._neural_net.train(states, target_q)

@dataclass
class Sensor(Node):
    """Input processing for AI systems"""
    name: str = field(default="")
    kind: AIKind = field(default=AIKind.SENSOR)
    _preprocessors: List[Callable[[Any], Any]] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.AI, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_preprocessor(self, func: Callable[[Any], Any]):
        """Add a preprocessing function"""
        self._preprocessors.append(func)
        
    def process(self, data: Any) -> Any:
        """Process input data"""
        result = data
        for preprocessor in self._preprocessors:
            result = preprocessor(result)
        return result

@dataclass
class Actuator(Node):
    """Output actions for AI systems"""
    name: str = field(default="")
    kind: AIKind = field(default=AIKind.ACTUATOR)
    _actions: Dict[str, Callable[..., Any]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.AI, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def register_action(self, name: str, func: Callable[..., Any]):
        """Register an action function"""
        self._actions[name] = func
        
    def execute(self, action_name: str, *args, **kwargs) -> Any:
        """Execute an action"""
        if action_name in self._actions:
            return self._actions[action_name](*args, **kwargs)
        raise ValueError(f"Unknown action: {action_name}")