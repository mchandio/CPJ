# CPJ Intermediate Representation (IR) and Backend Plan

## Goals
- Decouple parsing/front-end from code generation/backends
- Enable modular, pluggable backends (C++, JVM, Python, etc.)
- Support static analysis, optimizations, and future language features
- Make it easy to add new targets or improve existing ones

## IR Design
- **AST (Abstract Syntax Tree):**
  - Already implemented in `tools/cpj_parser.py` (Module, FuncDef, GUIBlock, Expr, etc.)
  - Should be extended with type annotations, source locations, and metadata
- **HIR (High-level IR):**
  - Normalized, language-agnostic representation
  - All control flow, types, and expressions explicit
  - Example: `HIRFunction`, `HIRBlock`, `HIRExpr`, `HIRType`
- **LIR (Low-level IR, optional):**
  - Closer to target code (C++/JVM bytecode/Python AST)
  - Used for advanced optimizations or backend-specific lowering

## Backend Architecture
- **Backend Interface:**
  - Each backend implements a `generate(ir: Module/HIR) -> str` method
  - Backends: `CPlusPlusBackend`, `PythonBackend`, `JavaBackend`, etc.
- **Pipeline:**
  1. Parse source to AST
  2. Lower AST to HIR (normalize, type-check, annotate)
  3. Pass HIR to selected backend for code generation
  4. Backend emits code, compiles/runs as needed

## Example Pipeline
```python
from tools.cpj_parser import Parser
from tools.ir import lower_to_hir
from backends.cpp import CPlusPlusBackend

ast = Parser(src).parse()
hir = lower_to_hir(ast)
cpp_code = CPlusPlusBackend().generate(hir)
```

## Next Steps
- Define HIR node classes in `tools/ir.py`
- Implement `lower_to_hir(ast)` transformation
- Refactor backends to consume HIR
- Add tests for IR lowering and backend output

---
*This plan enables CPJ to scale to new targets and advanced features. See ROADMAP.MD for progress.*
