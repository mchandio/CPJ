CPJ Advisor

This document describes the `tools/cpj_advisor.py` utility. The advisor is a
local, deterministic helper that scans the repository for hints about desired
features (networking, GUI, parsing, LSP, JSON) and recommends candidate
libraries for C++, Python, and Java.

Why this exists

- The project owner asked for a local decision-maker that "thinks" like CPJ and
  recommends libraries to integrate. This tool provides a reproducible,
  transparent recommendation without external network calls.

How it works

- It scans the repository for keywords defined in `FEATURE_KEYWORDS`.
- It uses a small internal KB of candidate libraries per language.
- It ranks candidates with simple heuristics and emits a recommended choice
  plus a concise implementation prompt.

Usage

Run the advisor from the repo root:

python tools/cpj_advisor.py

Or emit JSON for programmatic consumption:

python tools/cpj_advisor.py --json

If you already know the feature you want to target, pass `--feature`:

python tools/cpj_advisor.py --feature gui --feature antlr

Notes and limitations

- This is intentionally offline and opinionated. It's a helper, not a
  replacement for architectural discussion.
- The KB is small. Feel free to extend `tools/cpj_advisor.py` with more
  candidates and richer scoring logic.
