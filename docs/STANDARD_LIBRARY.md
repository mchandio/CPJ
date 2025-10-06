# CPJ Standard Library Reference

## Core Modules

### 1. Data Structures
```python
from cpj.collections import List, Dict, Set, Queue, Stack

# Dynamic arrays
list = List[int]()
list.append(1)
list.extend([2, 3, 4])

# Hash tables
dict = Dict[str, Any]()
dict["key"] = "value"

# Priority queues
queue = PriorityQueue[Task]()
queue.push(task, priority=1)
```

### 2. Algorithms
```python
from cpj.algorithms import sort, search, graph

# Sorting
sorted_list = sort.quick_sort(items)
heap_sorted = sort.heap_sort(items)

# Searching
index = search.binary_search(items, target)
path = graph.shortest_path(graph, start, end)
```

### 3. I/O Operations
```python
from cpj.io import File, Directory, Path

# File operations
with File("data.txt", "r") as f:
    content = f.read()

# Directory operations
dir = Directory("path/to/dir")
for file in dir.glob("**/*.cpj"):
    process(file)
```

### 4. Networking
```python
from cpj.net import HTTP, TCP, UDP, WebSocket

# HTTP client
response = await HTTP.get("https://api.example.com")
data = response.json()

# WebSocket
socket = WebSocket("ws://server")
socket.on_message(handle_message)
```

### 5. GUI Components
```python
from cpj.gui import Window, Button, TextField

class MyWindow(Window):
    def init(self):
        self.button = Button("Click me")
        self.input = TextField()
        
    def layout(self):
        return Grid([
            [self.input],
            [self.button]
        ])
```

### 6. Machine Learning
```python
from cpj.ml import Model, Layer, Optimizer

# Neural network
model = Sequential([
    Layer.Dense(128, activation="relu"),
    Layer.Dense(64, activation="relu"),
    Layer.Dense(10, activation="softmax")
])

# Training
model.compile(optimizer="adam", loss="categorical_crossentropy")
model.fit(x_train, y_train, epochs=10)
```

### 7. Database
```python
from cpj.db import Database, Query

# Database connection
db = Database.connect("postgresql://localhost/mydb")

# Queries
users = db.query("SELECT * FROM users WHERE age > ?", 18)
```

### 8. Testing
```python
from cpj.testing import TestCase, assert_equals

class MyTest(TestCase):
    def setup(self):
        self.data = [1, 2, 3]
    
    def test_processing(self):
        result = process(self.data)
        assert_equals(result, 6)
```

## Language Integration

### 9. Cross-Language Tools
```python
from cpj.interop import CPP, Java, Python

# C++ integration
cpp_array = CPP.Array[int](size=100)
cpp_array.fill(0)

# Java integration
java_list = Java.ArrayList[String]()
java_list.add("Hello")

# Python integration
numpy_array = Python.numpy.array([1, 2, 3])
```

### 10. Memory Management
```python
from cpj.memory import SharedMemory, MemoryPool

# Shared memory
shared = SharedMemory("name", size=1024)
shared.write(data)

# Memory pools
pool = MemoryPool(block_size=64)
block = pool.allocate()
```

### 11. Concurrency
```python
from cpj.concurrent import Thread, ThreadPool, Lock

# Threading
thread = Thread(target=my_function)
thread.start()

# Thread pools
with ThreadPool(4) as pool:
    results = pool.map(process, items)
```

### 12. AI Components
```python
from cpj.ai import NeuralNetwork, Agent, Sensor

# Neural network
nn = NeuralNetwork()
nn.add_layer(784, 128, "relu")
nn.add_layer(128, 10, "softmax")

# Reinforcement learning
agent = Agent(state_size=10, action_size=4)
agent.train(environment, episodes=1000)
```

### 13. Error Handling
```python
from cpj.errors import Error, try_except

# Error handling
try:
    risky_operation()
except Error.FileNotFound as e:
    handle_error(e)
finally:
    cleanup()
```

### 14. Configuration
```python
from cpj.config import Config

# Load configuration
config = Config.load("config.toml")
debug = config.get("debug", False)
```

### 15. Logging
```python
from cpj.logging import Logger

# Create logger
logger = Logger(__name__)
logger.info("Operation started")
logger.error("An error occurred", exc_info=True)
```

For more detailed information about each module and its components, see the individual module documentation.