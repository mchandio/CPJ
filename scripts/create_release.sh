#!/usr/bin/env bash
set -euo pipefail

# create_release.sh - Build and package CPJ into a release tarball
# Usage: ./scripts/create_release.sh <version>

VERSION=${1:-v1.0.0}
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
RELEASE_DIR="$ROOT_DIR/releases"
BUILD_DIR="$ROOT_DIR/build"
TARBALL="$RELEASE_DIR/cpj-${VERSION}.tar.gz"

mkdir -p "$RELEASE_DIR"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "[release] Building CPJ..."
cd "$ROOT_DIR"
make clean || true
make compile

echo "[release] Collecting artifacts..."
mkdir -p "$BUILD_DIR"
# Copy binaries, scripts, samples, and docs
cp -v cpj_compiler "$BUILD_DIR/" || true
cp -vr java "$BUILD_DIR/java" || true
cp -vr python "$BUILD_DIR/python" || true
cp -vr cpp "$BUILD_DIR/cpp" || true
cp -v README.md "$BUILD_DIR/" || true
cp -v CPJ_Guide.md "$BUILD_DIR/" || true
cp -v RELEASE.md "$BUILD_DIR/" || true
cp -vr samples "$BUILD_DIR/" || true

# Create tarball
cd "$BUILD_DIR"
tar -czf "$TARBALL" .

echo "[release] Created $TARBALL"
ls -lh "$TARBALL"
