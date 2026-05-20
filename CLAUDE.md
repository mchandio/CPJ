# CLAUDE.md

This file gives Claude Code the working context for the CPJ repository.

## Project Overview

CPJ, Cyber Programming Jet, is a multi-target compiler and development environment. The project includes:

- A C++ compiler core in `cpj_compiler.cpp`, `src/`, `cpp/`, and related root-level helpers.
- Python runtime helpers, emitters, parsers, and tooling in `python/`, `tools/`, root-level `cpj_*.py` files, and `tests/`.
- Java GUI/runtime support under `java/`, built with Gradle and Java 17.
- ANTLR grammar assets under `grammar/` and `java/src/main/antlr/`.
- LSP support under `lsp/`.
- CPJ examples under `samples/` and `test/`.

Prefer existing patterns in nearby files. This repository contains several generated and build-output directories, so be careful to distinguish source changes from artifacts.

## Common Commands

Set up Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Quick project setup from a POSIX shell or Git Bash:

```bash
./scripts/try_quickstart.sh
```

Build the C++ compiler with Make:

```bash
make clean && make
```

Build with CMake:

```bash
cmake -S . -B build
cmake --build build --parallel
```

Run a compiler sample without launching generated GUIs:

```bash
./cpj_compiler_no_run samples/types_demo.cpj
```

Run a compiler sample interactively:

```bash
./cpj_compiler samples/types_demo.cpj
```

Build Java components:

```bash
./gradlew :java:build
```

On Windows, the native build and install flow is:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\install_windows.ps1
cpj --help
```

## Testing

Run the main Python test suite:

```bash
python -m pytest -q
```

Run quick smoke tests:

```bash
make test
```

Run the full test target:

```bash
make test-all
```

Run coverage:

```bash
make coverage
```

Run Java tests in a headless Linux/CI-style environment:

```bash
xvfb-run -a ./gradlew :java:test --no-daemon
```

Run CMake tests after building:

```bash
ctest --test-dir build --output-on-failure
```

For focused changes, prefer targeted pytest commands such as:

```bash
python -m pytest tests/test_emit_and_run.py -q
python -m pytest tests/test_web_emitter.py -q
python -m pytest tests/test_lsp_smoke.py -q
```

## Development Notes

- Python requires 3.10 or newer.
- Java code targets Java 17 in Gradle.
- CI uses Python tests, CMake/CTest, Java/Gradle tests, and optional lint/security checks.
- The repository has both `test/` and `tests/`; check the surrounding code and pytest configuration before adding tests.
- Use `cpj_compiler_no_run` for tests or scripts that should not open generated Swing GUIs.
- If changing grammar behavior, update the relevant grammar files and regenerate parser outputs only when the workflow requires it. Then run focused parser/emitter tests.
- If changing web output, check `tools.cpj_web_emitter` behavior and tests in `tests/test_web_emitter.py`.
- If changing LSP behavior, update `lsp/server.py` and add or update tests under `tests/`.

## Repository Hygiene

- Do not commit local virtual environments, coverage output, Gradle caches, CMake build trees, class files, generated binaries, or other build artifacts unless the task explicitly requires it.
- Existing dirty files may be user work or generated output. Avoid reverting unrelated changes.
- Keep commits narrowly scoped. Stage only the files needed for the task.
- Prefer source files, docs, tests, and scripts over generated outputs when making feature or bug-fix changes.
