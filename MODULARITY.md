# CPJ Modular Architecture

CPJ is designed so each language component (C++, Python, Java) can be replaced or extended independently. Configuration is managed via `cpj_config.h` and documented interfaces.

## How to Replace/Extend Components
- **C++ Core:** Update or replace `main.cpp`, `code_analyzer.cpp`, or add new modules. Update `cppModulePath` in `cpj_config.h` if needed.
- **Java GUI:** Replace `GUIBridge.java` or add new GUI classes. Update `javaModulePath` in `cpj_config.h`.
- **Python AST:** Update `cpj_python.py` or add new analysis scripts. Update `pythonModulePath` in `cpj_config.h`.

## Extensibility
- Add new modules and update config paths.
- Use standardized IO (files, stdin/stdout) for communication.
- Document interfaces for each component.

---
For more details, see `cpj_config.h` and the main orchestrator code.
