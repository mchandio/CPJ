# CPJ — Cyber Programming Jet

[![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)
[![Python tests](https://github.com/<OWNER>/<REPO>/actions/workflows/python-tests.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/python-tests.yml)
[![Release](https://github.com/<OWNER>/<REPO>/actions/workflows/release.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/release.yml)
[![Coverage](https://codecov.io/gh/<OWNER>/<REPO>/branch/main/graph/badge.svg)](https://codecov.io/gh/<OWNER>/<REPO>)

CPJ is a tri-language compiler and development environment that targets C++, Python, and Java. It includes a C++ core compiler, Python runtime helpers, and Java GUI generation support.

Canonical Quickstart

The easiest way to get started is the quickstart script that automates a minimal local setup (creates a virtualenv, installs Python deps, builds the C++ compiler, and runs a non-interactive sample):

```bash
./scripts/try_quickstart.sh
```

If you prefer to run the steps manually, see `docs/getting_started.md` for platform notes and step-by-step commands.

Badges

The badge URLs in this README use the placeholder `<OWNER>/<REPO>`. To update them for your repository, replace the placeholder (example from repo root):

```bash
sed -i 's|<OWNER>/<REPO>|myuser/cpj|g' README.md
```

Alternatively the repo includes `scripts/update_badges.sh` which replaces the placeholders for you.

# CPJ Language and Compiler Documentation

## Documentation

Full project documentation is in the `docs/` folder. Start at `docs/index.md` for a guided table of contents and walk-throughs:

- `docs/index.md` — top-level documentation index and links
- `docs/getting_started.md` — quickstart and samples
- `docs/developer_guide.md` — how to extend and develop CPJ


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

## Testing

- Quick smoke test (fast):

```bash
make test
```

- Full test suite:

```bash
make test-all
```

The CI runs `make test` in the fast matrix jobs and `make test-all` on pushes to `main`.

### Coverage

Run coverage locally and generate an XML report:

```bash
make coverage
# report is written to reports/coverage.xml
```

You can upload the `reports/coverage.xml` artifact to a coverage service or inspect it locally with tools that read Cobertura/coverage XML.

## Extensibility
- Modular architecture: Replace or extend C++, Python, or Java components independently.
- Configuration via `cpj_config.h` and documented interfaces.

## Further Reading
`samples/types_demo.cpj` demonstrates token-style `types` (e.g. `types count:int flag:bool`),
a multi-line dict-style `types` block, and per-field overrides passed to widget constructors like
`addTextField` and `addButton`. To generate the preprocessed file used by tests run:

```bash
python3 grammar/indent_preprocessor.py samples/types_demo.cpj > samples/types_demo.pre.cpj
```

Try the sample:

```bash
./cpj_compiler samples/types_demo.cpj
```

Preprocess and test with the ANTLR grammar

```bash
python3 grammar/indent_preprocessor.py samples/types_demo.cpj > samples/types_demo.pre.cpj
python3 -m pytest tests/test_tokenization.py
```

## Widget Type Annotations and Coercion

CPJ's GUI block supports optional widget type annotations to help the emitted Python runtime coerce
widget values into appropriate Python types before calling handlers.

Per-field annotations
- addTextField("name", "int") — declares the `name` text field should be coerced to int.
- addCheckbox("agree", "bool") — declares a checkbox that will be coerced to bool.
- addSlider("speed", "int") — declares a slider whose value will be coerced to an integer.

Block-level types map
- You can also provide a block-level `types` map as the first line of a GUI block. Example:

```cpj
GUI {
        types {"count":"int", "flag":"bool"}
        addTextField("count")
        addTextField("other")
        addButton("Go", handler(count, other))
        show()
}
```

Coercion rules
- If a widget has a declared type, `cpj_runtime.gather_widget_data` will attempt to coerce the
    raw widget value to that type. Supported types: `int`, `float`/`double`, `bool`/`boolean`,
    `str`/`string`.
- `bool` accepts `true/false`, `1/0`, `yes/no` (case-insensitive) and falls back to `bool(str)`
    when ambiguous.
- On failed numeric coercion (e.g. trying to coerce `'abc'` to `int`), the runtime will fall back
    to the original string value and will add a `_coercion_errors` entry in the returned data mapping
    the widget name to an error message, so handlers can detect and handle malformed input.

Notes
- Per-field annotations override block-level `types` entries for the same widget name.
- The emitter also supports `addCheckbox` and `addSlider` in addition to `addTextField`.

## CI & headless testing

The CPJ compiler can generate and run Java Swing GUIs for samples. To keep CI and automated
tests fast and deterministic, the repository includes a small wrapper that runs the compiler
in a non-interactive, compile-only mode without launching the generated GUI:

- `cpj_compiler_no_run` — wrapper script that stubs `javac`/`java` on a temporary PATH and
  invokes the real `cpj_compiler` binary. Use this in CI or tests to avoid launching GUIs.

CI uses the `python-tests.yml` workflow which installs `requirements.txt` and runs `pytest`.
If you run tests locally and the GUI would otherwise be launched, prefer the wrapper:

```bash
./cpj_compiler_no_run samples/types_demo.cpj
python3 -m pytest -q
```

If you prefer an alternative approach, you can also run tests inside a proper CI runner or
set up a headless Java environment; the wrapper is a small convenience to keep on-disk
artifacts and runtime behavior unchanged.

## Quickstart

1. Install CPJ (see `docs/installation.md`)
2. Write your first program in `.cpj` file
3. Use the orchestrator to compile and run code in C++, Python, or Java

## Learning Resources
- [Language Reference](docs/language_reference.md)
- [Getting Started Guide](docs/getting_started.md)
- [Migration Guide](docs/migration_guide.md)
- [Interactive Tutorials](docs/tutorials/)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/community.md](docs/community.md)

---
For questions or contributions, see the project README or contact the maintainer.
