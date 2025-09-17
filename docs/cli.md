CLI Reference (cpj_compiler)

Usage: `./cpj_compiler [options] <source>`

Options

- `--no-run` — do everything up to launching the generated Java program, then stop.
- `--no-compile` — emit source files but skip compiling/running generated artifacts.
- `-h`, `--help` — show help and exit.

Exit codes

- `0` — success
- non-zero — failure during parse/generation/compilation/runtime

Notes

- The compiler produces Java and Python sources for GUI constructs by default.
- Use `--no-run` in CI to avoid interactive GUI execution.
