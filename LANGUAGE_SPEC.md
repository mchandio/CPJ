# CPJ Language Specification v0.1

This document describes the goals and minimal design of CPJ (Cyber Programming Jet) — a multi-language-aware programming
language that blends C++ performance, Python ergonomics, and Java's GUI/tooling ecosystem.

## High-level goals

- Familiar syntax mixing C++/Python/Java styles; quick to write like Python but able to target C++ for performance-critical code.
- First-class GUI constructs that compile to Java Swing (or an alternative UI backend).
- Seamless interop: call into Python and Java from CPJ code with well-defined marshalling rules.
- Incremental adoption: programs can include annotations or pragmas to pick which backend (C++/Python/Java) a module should target.

## v0.1 design decisions (opinionated)

- Syntax: Python-like for function bodies (indentation-friendly), C++/Java-like signatures optional. A small sample grammar will be provided.
- Typing: Optional static typing. By default variables are dynamically typed; type annotations enable static checks and C++ codegen.
- Memory: Hybrid model. CPJ runtime provides simple reference-counted objects for dynamic features and allows compiling modules to native C++ with manual resource management.
- Concurrency: Map to underlying platform facilities — threads in C++/Java, asyncio-style in Python backend.

## Language subsets and modes

- Script mode: interpreted-style semantics mapped to Python execution.
- Native mode: statically-typed functions and classes compiled to C++ for performance.
- GUI mode: `GUI { ... }` blocks compile to Java Swing code; connectors pass events back to CPJ runtime.

## Interoperability rules (v0.1)

- Primitive types (int, float, bool, string) map directly between languages.
- Lists/arrays, maps/dicts require marshaling; shallow copies are used for safety across boundaries.
- Functions can be marked `export` to allow calls from other languages.
- Event handlers in GUI will be generated as small Java callbacks that write JSON to a temporary file; connectors will read that file and dispatch into CPJ runtime.

## Minimal grammar sketch (informal)

- Top-level items: imports, function/class definitions, `GUI { ... }` blocks, and free statements.
- Function: `def name(arg: Type = default) -> ReturnType: \n    indented-body` (Python-like)
- Class: `class Name(Base1, Base2): \n    def method(...)` (Python-like)
- GUI: `GUI { addLabel("Hello") \n addTextField("name") \n addButton("Greet") \n show() }`

## Tooling and build model

- `cpj_compiler` (C++) parses CPJ source into an AST/IR and produces language-specific artifacts (C++ files, Python modules, Java classes).
- `cpj_connector.py` and `cpj_orchestrator.py` manage execution of generated artifacts and marshal data.
- `Makefile` provides simple build and run targets; a more advanced build system (CMake/meson) is planned.

## Example: Hello World (mixed)

```
# hello.cpj
import time

class Greeter:
    def __init__(self, name: string):
        self.name = name

    def greet(self):
        print("Hello, " + self.name)

# Native fast add
def add_fast(a: int, b: int) -> int @native:
    return a + b

GUI {
    addLabel("Hello CPJ")
    addTextField("name")
    addButton("Greet")
    show()
}
```

## Next steps for spec v0.2

- Formal grammar (ANTLR .g4 file)
- Precise type mapping table and ABI definition for interop
- Event model for GUI and async callbacks
- Runtime architecture and GC/memory plan

---

This v0.1 spec is intentionally small to let us iterate quickly. If you're happy with these goals I will:
- produce a formal grammar and a small recursive-descent parser next,
- or implement a richer GUI generator (event wiring between Java and CPJ runtime).

Which do you want me to do next?