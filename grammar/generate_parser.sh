#!/usr/bin/env bash
# Helper to generate an ANTLR4 Python3 parser from grammar/CPJ.g4
# Place the ANTLR jar (e.g. antlr-4.12.0-complete.jar) in the tools/ or grammar/ directory,
# then run this script. It requires Java.

set -euo pipefail
DEFAULT_JAR_OLD=antlr-4.12.0-complete.jar
DEFAULT_JAR_NEW=antlr-4.13.2-complete.jar
if [ -n "${1:-}" ]; then
  ANTLR_JAR=$1
elif [ -f "$DEFAULT_JAR_NEW" ]; then
  ANTLR_JAR=$DEFAULT_JAR_NEW
else
  ANTLR_JAR=$DEFAULT_JAR_OLD
fi
OUT_DIR=${2:-generated}

if [ ! -f "$ANTLR_JAR" ]; then
  echo "ANTLR jar not found at $ANTLR_JAR"
  echo "Download it from https://www.antlr.org/download.html and save as $ANTLR_JAR"
  exit 2
fi

mkdir -p "$OUT_DIR"
java -jar "$ANTLR_JAR" -Dlanguage=Python3 -o "$OUT_DIR" CPJ.g4

echo "Generated parser files in $OUT_DIR"

echo "Next: add the generated directory to PYTHONPATH or move the generated files into your toolchain."