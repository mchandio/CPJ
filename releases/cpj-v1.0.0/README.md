
x = add(5, 7)

# CPJ Language and Compiler Documentation

## Overview
CPJ (Cyber Programming Jet) is a tri-language compiler and development environment supporting C++, Python, and Java. It enables seamless integration and execution of code across all three languages, with features for auto-detecting and installing Python libraries, Java GUI support, and unified orchestration.

## Language Features
- Class and function definitions (C++/Java/Python style)
- Static and dynamic typing
- Print and input statements
- Exception handling
- GUI constructs (auto-generates Java Swing code)
- Integration with Python modules and Java GUI

## Example CPJ Program
```cpj
class HelloWorld {
    def main() {
        print("Hello, CPJ World!")
    }
}

def add(a: int, b: int) -> int {
    return a + b
}


print(x)
```

## Compiler Architecture
- **C++ Core:** Lexes, parses, and generates code for CPJ syntax. Handles code generation for print, function, class, and GUI constructs.
- **Python Integration:** Handles dynamic features, AST analysis, and auto-installs required libraries. Integration via connector module.
- **Java Integration:** Provides GUI and advanced OOP features. Auto-generates and compiles Java Swing code for GUI constructs. Integration via connector module.
- **Runtime Hooks:** C++ main calls Python and Java modules as needed, using connector scripts for seamless execution and data exchange.

## Integration Process
1. **Code Generation:** CPJ compiler parses CPJ source and generates code for C++, Python, and Java as needed.
2. **Connector Module:** `cpj_connector.py` enables communication and execution between C++, Python, and Java components. Supports data exchange via files.
3. **Orchestration:** `cpj_orchestrator.py` manages build and run workflow for all languages.
4. **GUI Automation:** GUI constructs in CPJ source trigger auto-generation of Java Swing code, compilation, and execution.
5. **Extensibility:** Modular architecture allows independent extension or replacement of C++, Python, or Java modules. Configuration via `cpj_config.h`.

## Build and Run
- Use the Makefile to build all components: `make clean && make`
- Run the compiler: `./cpj_compiler samples/demo.cpj`

## Extensibility
- Modular architecture: Replace or extend C++, Python, or Java components independently.
- Configuration via `cpj_config.h` and documented interfaces.

## Further Reading
- See `MODULARITY.md` for modular design.
- See `samples/demo.cpj` for example programs.

---
For questions or contributions, see the project README or contact the maintainer.
