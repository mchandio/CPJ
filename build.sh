#!/bin/bash

# Detect OS
case "$(uname -s)" in
    Linux*)     OS=linux ;;
    Darwin*)    OS=macos ;;
    CYGWIN*)    OS=windows ;;
    MINGW*)     OS=windows ;;
    *)          OS=unknown ;;
esac

# Set platform-specific variables
case "$OS" in
    linux)
        export CC=gcc
        export CXX=g++
        ;;
    macos)
        export CC=clang
        export CXX=clang++
        ;;
    windows)
        export CC=cl
        export CXX=cl
        ;;
esac

# Build CPJ
echo "Building CPJ for $OS..."
make clean
make all

# Run tests
echo "Running tests..."
make test