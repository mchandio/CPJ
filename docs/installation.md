Installation

Install project dependencies and build the C++ compiler.

1. Create a virtual environment and install Python dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Optionally install system dependencies for Java/C++

- Java JDK (for GUI generation and execution)
- build-essential / gcc / g++

3. Build the C++ compiler

```bash
make clean && make
```

4. Run tests

```bash
python -m pytest -q
```

Notes

- `antlr4-python3-runtime` is required by tests that exercise the generated ANTLR parser.
- `pygls` is an optional dev dependency for language server development and local testing.
