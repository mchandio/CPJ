CPJ ROADMAP
===========

Overview
--------
This document maps the high-level language-design and project checklist (goals, design, compiler, runtime, tooling, testing) to the current repository state, summarizes what we've implemented so far, and lists prioritized next milestones, estimates, and risks.

Scope of this roadmap
---------------------
CPJ is a tri-language project that targets interoperability and convenience across C++, Python, and Java. The repository contains a working CPJ toolchain for a domain-specific GUI-oriented language (parser, emitter, runtime helpers, tests, and small codegen backends). This roadmap focuses on the remaining work needed to evolve CPJ toward a broader, general-purpose programming language while documenting completed engineering milestones.

Completed (status: implemented in this repo)
--------------------------------------------
- Language goals and features (initial):
  - Clear goals and positioning: combine C++ performance ideas, Python ergonomics, and Java GUI tooling (documented in CPJ_Guide.md and LANGUAGE_SPEC.md).
  - Syntax choice for GUI DSL: lightweight, indentation-friendly, handler expressions support (parser and emitter).

- Design and front-end:
  - Lexer & Parser: custom recursive-descent parser implemented (see `tools/cpj_parser.py`).
  - Expression support: nested expressions, function calls, dotted identifiers, bitwise ops, chained comparisons.
  - AST: expression nodes and handlers suitable for code emission and tests.

- Runtime & backend (partial):
  - Emitter: Python emitter refactored to visitor/template style (`tools/cpj_emitter.py`).
  - Runtime helpers: `cpj_runtime.py` implements widget collection, coercion, and event invocation helpers.
  - Codegen targets: Python/Tkinter and Java Swing backends present in `java/` and `python/` directories.

- Type handling & safety improvements:
  - Per-widget type annotations (inline) and GUI-block `types` support with validation.
  - Replaced unsafe eval with `ast.literal_eval` for safer parsing of literal type maps.
  - Multiline and token-style `types` parsing with diagnostics and emitted runtime warnings for invalid entries.

- Tests & quality:
  - Comprehensive pytest suite covering parser, emitter, runtime coercion, GUI handler binding/invocation, and negative coercion tests (`tests/`).
  - Integration smoke test that runs `./cpj_compiler samples/types_demo.cpj` without crashing.

- Samples & docs (partial):
  - Several samples under `samples/` (farmflow.cpj, hello.cpj, types_demo pending).
  - Updated `README.md` and `CPJ_Guide.md` contain usage and architecture notes.

In-repo artifacts that show concrete progress
--------------------------------------------
- `tools/cpj_parser.py` — Parser implementation with support for dotted identifiers and extensive expression grammar.
- `tools/cpj_emitter.py` — Emitter refactored to visitor/template pattern, emits runtime warnings and wiring helpers.
- `cpj_runtime.py` — Runtime utilities for data collection and coercion.
- `tests/` — Unit and integration tests; all pass under pytest in the current workspace.
- `samples/` — Example CPJ programs; `types_demo.cpj` to be added if missing.

Remaining work (prioritized)
----------------------------
## CPJ Completion & Perfection TODO List (2025)

1. **Event Model & Connector Hardening (Essential)**
   - Robust, bi-directional event delivery (with error/reply semantics)
   - JSON schema validation for events
   - Async/event queue support for all runtimes
   - Cross-runtime handler invocation (Python, C++, Java)
   - Comprehensive integration tests

2. **Design IR and Backend Plan (Essential)**
   - Internal IR (Intermediate Representation) to decouple parsing from code generation
   - Modular backend support (C++, JVM, Python)
   - Enables future optimizations, static analysis, and new targets

3. **Expand LSP Features (Essential for Developer Experience)**
   - Completions, document symbols, go-to-definition, and improved diagnostics
   - LSP tests in CI for stability
   - Makes CPJ usable in modern editors

4. **CI: Enable pygls and LSP Tests (Essential for Quality)**
   - Ensure all LSP features are tested in CI
   - Prevents regressions and ensures cross-platform support

5. **Type System Expansion (Recommended for “Perfect”)**
   - Support for user-defined types, type inference, and generics (if feasible)
   - More expressive type annotations and error messages

6. **Vendor gradle-wrapper.jar (Recommended for Reproducibility)**
   - Ensures Java builds are always reproducible and offline

7. **Polish & Documentation**
   - Complete and polish all user/developer documentation
   - Add more real-world samples and advanced usage guides

---
*This list is the authoritative checklist for CPJ language completion and perfection. See the project board and issues for live progress.*
   - Choose and implement a memory model (GC, reference counting, or manual) suitable for mixed paradigms.
   - Design interop with native C++ memory and Java GC if targeting multiple runtimes.

8) Tooling ecosystem (ongoing)
   - IDE plugins, debugger integration, package manager, documentation generator. Each is a multi-week effort depending on scope.

9) CI, benchmarking, and quality gates (3-7d)
   - Add CI (tests, linting), benchmarks versus C++/Python/Java, and automated release tests.

10) Security, sandboxing, FFI safety (5-15d)
   - Harden execution (sandboxing untrusted code), validate FFI surface and memory safety when calling native code.

11) Long-term: standard library and ecosystem (months)
   - Build out standard libraries, community packages, and platform-specific bindings.

Risks and unknowns
------------------
- Scope creep: the tri-language ambition is large; recommend iterative scope and MVP choices.
- Memory/runtime mismatch: integrating manual memory management with multiple runtime models is complex.
- Ecosystem expectations: building a robust standard library and tooling takes most of the effort.

Short-term next steps (what I'll do now in this repo)
----------------------------------------------------
- Create `samples/types_demo.cpj` if missing and link it from `README.md`. (small, actionable)
- Add `ROADMAP.MD` (this file) to the repo root. (done)
- Mark the remaining `Add samples/types_demo.cpj and README link` todo item as `not-started` (done).

How this maps to the original high-level guide
----------------------------------------------
- "Define Language Goals and Features": done (initial goals + DSL focus). See `CPJ_Guide.md`.
- "Design the Language": partial (parser and expression grammar implemented; formal grammar and type system remain).
- "Build the Compiler/Interpreter": partial (lexer/parser + emitter + runtime helper implemented; IR and compiled backends remain).
- "Standard Library": largely unstarted beyond small runtime helpers and GUI-focused libs.
- "Tooling Ecosystem": minimal; tests exist but IDE, debugger, and package manager are future work.

Contact & contributing
----------------------
If you'd like, I can now:
- Create `samples/types_demo.cpj` and update `README.md` (0.5-1d).
- Start formalizing grammar into ANTLR (2-4d).
- Scaffold a minimal type-checker for GUI blocks (2-5d).

Pick one and I'll start it next.
