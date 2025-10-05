# CPJ Language: Complete Guide

## Introduction
CPJ (Cyber Programming Jet) is a tri-language programming environment and compiler that unifies C++, Python, and Java. It enables seamless integration, code generation, and execution across all three languages, supporting both console and GUI applications.

---

## 1. Language Syntax

### Classes
```cpj
class MyClass {
    def main() {
        print("Hello from CPJ!")
    }
}
```

### Functions
```cpj
def add(a: int, b: int) -> int {
    return a + b
}
```

### Variables and Types
```cpj
x: int = 42
y: float = 3.14
name: string = "CPJ"
```

### Print Statement
```cpj
print("Hello, CPJ World!")
```

### Exception Handling
```cpj
try {
    risky_operation()
} catch (Exception e) {
    print(e)
}
```

---

## 2. GUI Constructs (Java Swing)

CPJ supports GUI creation via special constructs that auto-generate Java Swing code.

### Example
```cpj
GUI {
    addLabel("Calculator")
    addTextField("display")
    addButton("1")
    addButton("2")
    addButton("+")
    onClick("+") {
        // handle addition
    }
    show()
}
```

---

## 3. Multi-Language Integration

- **C++ Core:** Handles parsing, code generation, and orchestration.
- **Python Integration:** Supports dynamic features, auto-installs libraries, and executes Python code.
- **Java Integration:** Generates, compiles, and runs Java GUI code.
- **Connector Module:** `cpj_connector.py` enables communication and data exchange between languages.

---

## 4. Build and Run Workflow

1. **Build All Components:**
   ```bash
   make clean && make
   ```
2. **Run CPJ Compiler:**
   ```bash
   ./cpj_compiler samples/demo.cpj
   ```
3. **Auto-Generated GUI:**
   - If GUI constructs are present, Java Swing code is generated, compiled, and launched automatically.

---

## 5. Extensibility

- Modular architecture: Replace or extend C++, Python, or Java modules independently.
- Configuration via `cpj_config.h`.
- Add new language features by updating parser and code generation modules.

---

## 6. Example Program

```cpj
class Calculator {
    def main() {
        print("Welcome to CPJ Calculator!")
    }
}

def add(a: int, b: int) -> int {
    return a + b
}

x = add(10, 20)
print(x)

GUI {
    addLabel("CPJ Calculator")
    addTextField("display")
    addButton("1")
    addButton("2")
    addButton("+")
    onClick("+") {
        // handle addition
    }
    show()
}
```

---

## 7. Advanced Topics

- **Custom Modules:** Add new modules in C++, Python, or Java and update config paths.
- **Data Exchange:** Use connector module to share data between languages via files.
- **Orchestration:** Use `cpj_orchestrator.py` for unified build/run management.

---

## 8. Troubleshooting

- Check Makefile for build errors.
- Ensure all dependencies are installed (see `requirements.txt`).
- For integration issues, review connector and orchestrator modules.

---

## 9. Further Reading

- `README.md`: Quick start and architecture overview.
- `MODULARITY.md`: Details on modular design and extensibility.
- `samples/demo.cpj`: Example CPJ programs.

---

## 10. Contact & Contribution

For questions, contributions, or bug reports, see the project README or contact the maintainer.
