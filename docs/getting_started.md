Getting started with CPJ

This quickstart gets you from checkout to running a simple CPJ sample.

Prerequisites

- Linux/macOS/Windows
- Python 3.10+
- Java JDK (for GUI code generation and execution)
- GNU Make

Quick steps

```bash
# create and activate virtualenv (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# install Python deps
pip install -r requirements.txt

# build the C++ compiler
make clean && make

# run the sample (headless wrapper recommended for CI)
./cpj_compiler_no_run samples/types_demo.cpj
```

If you want to run the generated GUI locally (interactive), omit the `_no_run` wrapper and run:

```bash
./cpj_compiler samples/types_demo.cpj
```

Where to go next

- See `docs/usage.md` for CLI reference and examples
- Explore `samples/` for example CPJ programs
- See `docs/developer_guide.md` for how to extend the compiler or backends
