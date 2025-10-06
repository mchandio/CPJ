# CPJ Quick Start Guide

## Installation

1. Install CPJ using pip:
```bash
pip install cpj-lang
```

2. Verify installation:
```bash
cpj --version
```

## Creating Your First CPJ Project

1. Create a new project:
```bash
cpj new my_project
cd my_project
```

2. Project structure:
```
my_project/
├── src/
│   └── main.cpj
├── tests/
├── cpj.toml
└── README.md
```

3. Edit `src/main.cpj`:
```python
// Your first CPJ program

def main():
    print("Hello from CPJ!")
    
    // C++ section
    int calculate() {
        return 42;
    }
    
    # Java section
    public class Greeter {
        public String getMessage() {
            return "Welcome!";
        }
    }
    
    // Use all languages
    value = calculate()  # Call C++
    greeter = Greeter()  # Create Java object
    message = greeter.getMessage()  # Call Java
    
    print(f"Value: {value}, Message: {message}")

if __name__ == "__main__":
    main()
```

4. Build and run:
```bash
cpj build
cpj run
```

## Key Concepts

### 1. Language Integration

CPJ allows seamless mixing of Python, C++, and Java:

```python
# Python code
def process_data(data: List[float]) -> float:
    return sum(data) / len(data)

// C++ code for performance
vector<double> optimize(vector<double>& data) {
    // Fast processing
    return result;
}

# Java code for GUI
public class Display {
    public void show(double[] data) {
        // Show results
    }
}
```

### 2. Type System

CPJ features a strong, unified type system:

```python
type Point {
    x: float
    y: float
}

type Rectangle {
    top_left: Point
    bottom_right: Point
    
    def area(self) -> float:
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y
        return width * height
}
```

### 3. AI Features

Built-in AI support:

```python
neural network Classifier {
    layers = [784, 256, 128, 10]
    activation = "relu"
    
    def train(self, data: Dataset):
        self.fit(data, epochs=10)
}
```

### 4. Memory Management

Automatic and manual memory management:

```python
// Automatic (Python-style)
def process():
    data = [1, 2, 3]  # Auto-managed

// Manual (C++-style)
void optimize() {
    auto* buffer = new char[1024];
    scope(exit) delete[] buffer;
}
```

## Common Tasks

### File I/O
```python
from cpj.io import File

def read_data(path: str) -> str:
    with File(path, "r") as f:
        return f.read()

def write_data(path: str, data: str):
    with File(path, "w") as f:
        f.write(data)
```

### Networking
```python
from cpj.net import HTTP

async def fetch_data(url: str) -> dict:
    response = await HTTP.get(url)
    return response.json()
```

### GUI
```python
from cpj.gui import Window, Button

class MainWindow(Window):
    def init(self):
        self.button = Button("Click me")
        self.button.on_click(self.handle_click)
    
    def handle_click(self):
        print("Button clicked!")
```

### Database
```python
from cpj.db import Database

async def save_user(user: dict):
    db = await Database.connect("postgresql://localhost/mydb")
    await db.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        user["name"], user["email"]
    )
```

## Testing

```python
from cpj.testing import TestCase

class MyTest(TestCase):
    def setup(self):
        self.data = [1, 2, 3]
    
    def test_processing(self):
        result = process_data(self.data)
        self.assertEqual(result, 2.0)
```

Run tests:
```bash
cpj test
```

## Debugging

1. Set breakpoints in code:
```python
def my_function():
    x = 42
    breakpoint()  # Debug here
    print(x)
```

2. Run with debugger:
```bash
cpj debug
```

## Package Management

1. Add dependency:
```bash
cpj add numpy
```

2. Update dependencies:
```bash
cpj update
```

## Building for Production

1. Create optimized build:
```bash
cpj build --release
```

2. Run tests:
```bash
cpj test --all
```

3. Package application:
```bash
cpj package
```

For more detailed information, see the full documentation at https://cpj-lang.org/docs