# Contributing to CPJ

Thanks for contributing! This file explains the minimal steps to set up a developer environment, run tests, and make changes.

## Development setup (quick)

1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
```

2. Install editable package and test deps:

```bash
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip install -r requirements.txt
```

3. Run tests:

```bash
.venv/bin/python -m pytest -q
```

## Common tasks

- Build the project (C++ components):

```bash
make clean && make
```

- Run the compiler on a sample:

```bash
./cpj_compiler samples/demo.cpj
```

- Run the compiler in a non-interactive mode (CI/tests):

```bash
./cpj_compiler_no_run samples/types_demo.cpj
```

- Run the tokenizer preprocessor and tests using ANTLR files:

```bash
python3 grammar/indent_preprocessor.py samples/types_demo.cpj > samples/types_demo.pre.cpj
python3 -m pytest tests/test_tokenization.py
```

## Making changes

- Make small, focused commits with descriptive messages.
- Run the test suite before opening a PR.
- If you change the C++ compiler, update Makefile or build instructions and add regression tests.

## CI

- The repository includes a GitHub Actions workflow at `.github/workflows/python-tests.yml` that installs `requirements.txt` and runs `pytest` on pushes and PRs to `main`/`master`.

## Notes

- The project currently includes a small wrapper `cpj_compiler_no_run` used by tests and CI to avoid launching GUIs.
- If you add features that require runtime system dependencies (Java, GUI), document them in the README and add CI steps where needed.

Thanks for contributing — send PRs and issues and we'll review them promptly.
