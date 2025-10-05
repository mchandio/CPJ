#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

GEN_DIR="$ROOT_DIR/generated/java"
OUT_DIR="${1:-/tmp/cpj-java-classes}"

if [ ! -d "$GEN_DIR" ]; then
  echo "No generated/java directory found at $GEN_DIR"
  exit 2
fi

mkdir -p "$OUT_DIR"

JAVAC=$(command -v javac || true)
if [ -z "$JAVAC" ]; then
  echo "javac not found in PATH"
  exit 3
fi

echo "Compiling Java files from $GEN_DIR to $OUT_DIR"
find "$GEN_DIR" -name '*.java' -print0 | xargs -0 "$JAVAC" -d "$OUT_DIR"
echo "Java compilation complete"
