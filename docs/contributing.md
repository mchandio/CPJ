Contributing to CPJ

Thanks for your interest in contributing! Please follow these steps to get started:

1. Fork the repository and create a feature branch.
2. Run tests locally and ensure they pass: `python -m pytest -q`.
3. Follow the coding style and add tests for new behavior.
4. Open a PR and link to the ROADMAP.MD item you're addressing.

Developer environment

- Use the provided `Makefile` and `requirements.txt` to set up your environment.
- If working on grammar changes, regenerate the ANTLR parser and include generated artifacts if they are necessary for tests.

CI notes

- The CI workflow installs `requirements.txt` and runs pytest. If your change adds new dev dependencies (e.g., `pygls`), update `requirements.txt` or the CI workflow accordingly.
