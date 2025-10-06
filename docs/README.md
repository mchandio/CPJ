# CPJ (Cyber Programming Jet) Documentation

CPJ is a modern, multi-paradigm programming language that seamlessly integrates Python, C++, and Java, enabling developers to write hybrid applications that leverage the strengths of each language.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Language Fundamentals](#language-fundamentals)
3. [Type System](#type-system)
4. [AI Features](#ai-features)
5. [Cross-Language Integration](#cross-language-integration)
6. [Standard Library](#standard-library)
7. [Tools and Ecosystem](#tools-and-ecosystem)
8. [Best Practices](#best-practices)

## Getting Started

### Installation

```bash
# Install from package manager
pip install cpj-lang

# Or build from source
git clone https://github.com/mchandio/CPJ.git
cd CPJ
./build.sh
```

### Basic Example

```python
// This is a CPJ program combining Python, C++, and Java

# Python section - Data processing
def process_data(values: List[float]) -> float:
    return sum(values) / len(values)

// C++ section - Performance-critical computation
struct Matrix {
    vector<vector<double>> data;
    
    Matrix multiply(const Matrix& other) {
        // Matrix multiplication implementation
        return result;
    }
}

# Java section - GUI
public class DataVisualizer {
    public void display(double[] data) {
        // Create visualization using JavaFX
    }
}

// Main program
def main():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    avg = process_data(data)  # Python call
    
    matrix = Matrix()
    result = matrix.multiply(other_matrix)  # C++ call
    
    visualizer = DataVisualizer()
    visualizer.display(result)  # Java call
```

## Language Features

- Seamless integration of Python, C++, and Java
- Strong static typing with type inference
- Built-in AI and machine learning capabilities
- Automatic memory management
- Native parallel processing support
- Cross-language debugging
- Integrated build system

## Type System

CPJ features a unified type system that works across all three languages:

```python
# Type definitions
type Point {
    x: float
    y: float
    z: float
}

type Matrix<T> {
    rows: int
    cols: int
    data: List[List[T]]
}

# Usage in different languages
def python_func(p: Point) -> float:
    return sqrt(p.x * p.x + p.y * p.y + p.z * p.z)

void cpp_func(Point& p) {
    // C++ code with same Point type
}

public void javaFunc(Point p) {
    // Java code with same Point type
}
```

## AI Features

CPJ includes built-in AI capabilities:

```python
# Define a neural network
neural house MySmartHome {
    layers = [784, 256, 128, 10]
    activation = "relu"
    
    # Sensor definitions
    sensor temperature {
        input_size = 1
        preprocessors = [normalize, smooth]
    }
    
    # Action definitions
    actions {
        adjust_hvac(temp: float) -> None
        control_lighting(level: int) -> None
    }
}
```

## Cross-Language Integration

Example of cross-language feature usage:

```python
// CPJ file demonstrating cross-language integration

# Python data processing
def preprocess_image(image: numpy.ndarray) -> numpy.ndarray:
    # Image preprocessing in Python
    return processed_image

// C++ performance-critical operations
class ImageProcessor {
    public:
        vector<float> extract_features(const Mat& image) {
            // Feature extraction in C++
            return features;
        }
}

# Java UI and visualization
public class ResultDisplay {
    public void showResults(double[] features) {
        // Display results using Java Swing/JavaFX
    }
}

# Main integration
def main():
    # Seamless data flow between languages
    image = load_image("input.jpg")
    processed = preprocess_image(image)  # Python
    
    processor = ImageProcessor()
    features = processor.extract_features(processed)  # C++
    
    display = ResultDisplay()
    display.showResults(features)  # Java
```

For more detailed documentation, please refer to the specific sections above.