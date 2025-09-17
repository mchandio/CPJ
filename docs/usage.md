Usage & CLI

The `cpj_compiler` is the main CLI entrypoint for compiling and running CPJ programs.

Basic usage

```bash
./cpj_compiler [options] <source.cpj>
```

Common options

- `--no-run` — compile only, do not run the generated Java GUI (useful for CI/headless)
- `--no-compile` — emit sources but skip compilation step
- `-o, --out <dir>` — output directory for generated sources and artifacts

Headless testing

CI and headless test runners should avoid launching GUIs. Use the included wrapper to stub Java:

```bash
./cpj_compiler_no_run samples/types_demo.cpj
```

Build and debug

- Use `make` to build the compiler and binaries.
- The runtime helpers are in `cpj_runtime.py` and `python/` and `java/` directories contain codegen targets.
