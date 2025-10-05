Getting started with CPJ

This quickstart gets you from checkout to running a simple CPJ sample in a reproducible way.

Prerequisites (summary)

- A POSIX shell (Linux/macOS) or Git Bash on Windows
- Python 3.10+ (python3)
- Java JDK 11+ (for GUI code generation and optional runtime)
- GNU Make and a C++ toolchain (gcc/clang)

Recommended quickstart (one command)

Run the helper script which automates a minimal dev setup (creates a virtualenv, installs Python deps, builds the compiler, and runs a non-interactive sample):

```bash
./scripts/try_quickstart.sh
```

Manual quickstart (step-by-step)

```bash
# create and activate virtualenv (POSIX)
python3 -m venv .venv
source .venv/bin/activate

# install Python deps
pip install -r requirements.txt

# build the C++ compiler
make clean && make

# run the sample (headless wrapper recommended for CI)
./cpj_compiler_no_run samples/types_demo.cpj
```

To run the generated GUI interactively, omit the `_no_run` wrapper:

```bash
./cpj_compiler samples/types_demo.cpj
```

Where to go next

- See `docs/usage.md` for CLI reference and examples
- Explore `samples/` for example CPJ programs
- See `docs/developer_guide.md` for how to extend the compiler or backends
