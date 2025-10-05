#!/usr/bin/env bash
# Quick helper to create a virtualenv, install python deps, build the compiler, and run a non-interactive sample
# Usage: ./scripts/try_quickstart.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Starting CPJ quickstart..."

# 1) Create venv if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtualenv .venv"
  python3 -m venv .venv
fi

echo "Activating virtualenv"
# shellcheck disable=SC1091
source .venv/bin/activate

echo "Installing Python requirements (may take a minute)"
pip install --upgrade pip >/dev/null
pip install -r requirements.txt

echo "Building the C++ compiler"
make clean && make

echo "Running cpj_compiler in non-interactive (no GUI) mode"
if [ -x ./cpj_compiler_no_run ]; then
  ./cpj_compiler_no_run samples/types_demo.cpj
else
  # fallback to invoking the compiler directly with --no-run if available
  if [ -x ./cpj_compiler ]; then
    ./cpj_compiler --no-run samples/types_demo.cpj
  else
    echo "No compiler binary found. Build failed or binaries missing."
    exit 2
  fi
fi

echo "Quickstart complete. Check the output in the generated/ and reports/ directories."
