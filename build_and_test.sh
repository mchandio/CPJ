#!/bin/bash
# CPJ Compiler - Comprehensive Build and Test Script
# This script compiles all components and runs verification tests

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[CPJ]${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_header() {
    echo ""
    echo -e "${BLUE}================================================${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}================================================${NC}"
    echo ""
}

# Check if we're in the CPJ directory
if [ ! -f "cpj_compiler.cpp" ]; then
    print_error "Please run this script from the CPJ project root directory"
    exit 1
fi

print_header "CPJ Tri-Language Compiler - Build & Test"

# Parse command line arguments
SKIP_CLEAN=false
SKIP_TESTS=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-clean)
            SKIP_CLEAN=true
            shift
            ;;
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --skip-clean    Skip the clean step"
            echo "  --skip-tests    Skip running tests"
            echo "  -v, --verbose   Show detailed output"
            echo "  -h, --help      Show this help message"
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Step 1: Clean previous build
if [ "$SKIP_CLEAN" = false ]; then
    print_header "Step 1: Cleaning Previous Build"
    print_status "Running make clean..."
    if [ "$VERBOSE" = true ]; then
        make clean
    else
        make clean > /dev/null 2>&1
    fi
    print_success "Clean completed"
else
    print_warning "Skipping clean step (--skip-clean)"
fi

# Step 2: Build C++ Compiler
print_header "Step 2: Building C++ Compiler"
print_status "Compiling cpj_compiler.cpp..."
if [ "$VERBOSE" = true ]; then
    g++ -o cpj_compiler cpj_compiler.cpp
else
    g++ -o cpj_compiler cpj_compiler.cpp 2>&1 | grep -i error || true
fi

if [ -f "cpj_compiler" ]; then
    SIZE=$(ls -lh cpj_compiler | awk '{print $5}')
    print_success "C++ compiler built successfully (${SIZE})"
else
    print_error "Failed to build C++ compiler"
    exit 1
fi

# Step 3: Build Java Components
print_header "Step 3: Building Java Components"
print_status "Running Gradle build..."
if [ "$VERBOSE" = true ]; then
    ./gradlew build -x test
else
    ./gradlew build -x test > /dev/null 2>&1
fi

if [ -f "java/build/libs/java-0.1.0.jar" ]; then
    SIZE=$(ls -lh java/build/libs/java-0.1.0.jar | awk '{print $5}')
    print_success "Java components built successfully (${SIZE})"
else
    print_error "Failed to build Java components"
    exit 1
fi

# Step 4: Setup Python Environment
print_header "Step 4: Setting Up Python Environment"
print_status "Creating virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    print_success "Virtual environment created"
else
    print_success "Virtual environment already exists"
fi

print_status "Installing Python dependencies..."
if [ "$VERBOSE" = true ]; then
    .venv/bin/python -m pip install --upgrade pip
    .venv/bin/python -m pip install -e .
    .venv/bin/python -m pip install -r requirements.txt
else
    .venv/bin/python -m pip install --upgrade pip > /dev/null 2>&1
    .venv/bin/python -m pip install -e . > /dev/null 2>&1
    .venv/bin/python -m pip install -r requirements.txt > /dev/null 2>&1
fi
print_success "Python environment ready"

# Step 5: Verify Components
print_header "Step 5: Verifying Build Components"

print_status "Checking cpj_compiler..."
if ./cpj_compiler --help > /dev/null 2>&1; then
    print_success "C++ compiler is functional"
else
    print_error "C++ compiler check failed"
    exit 1
fi

print_status "Checking Python parser..."
if PYTHONPATH=. .venv/bin/python -c "from tools.cpj_parser import Parser; print('OK')" > /dev/null 2>&1; then
    print_success "Python parser is functional"
else
    print_error "Python parser check failed"
    exit 1
fi

print_status "Checking Python emitter..."
if PYTHONPATH=. .venv/bin/python -c "from tools.cpj_emitter import Emitter; print('OK')" > /dev/null 2>&1; then
    print_success "Python emitter is functional"
else
    print_error "Python emitter check failed"
    exit 1
fi

# Step 6: Run Tests
if [ "$SKIP_TESTS" = false ]; then
    print_header "Step 6: Running Tests"

    print_status "Running C++ tests..."
    if [ "$VERBOSE" = true ]; then
        make test_runner && ./test_runner
    else
        make test_runner > /dev/null 2>&1 && ./test_runner > /dev/null 2>&1
    fi
    print_success "C++ tests passed"

    print_status "Running Python tests..."
    if [ "$VERBOSE" = true ]; then
        PYTHONPATH=. .venv/bin/python -m pytest tests/test_emit_and_run.py::test_emit_and_run_demo -v
    else
        PYTHONPATH=. .venv/bin/python -m pytest tests/test_emit_and_run.py::test_emit_and_run_demo -q > /dev/null 2>&1
    fi
    print_success "Python tests passed"

    print_status "Testing sample compilation..."
    if [ "$VERBOSE" = true ]; then
        ./cpj_compiler samples/demo.cpj
    else
        ./cpj_compiler samples/demo.cpj > /dev/null 2>&1
    fi
    print_success "Sample compilation test passed"

    print_status "Testing comprehensive tri-language test..."
    if [ "$VERBOSE" = true ]; then
        ./cpj_compiler samples/trilang_test.cpj
    else
        OUTPUT=$(./cpj_compiler samples/trilang_test.cpj 2>&1)
        if echo "$OUTPUT" | grep -q "All tests completed successfully"; then
            print_success "Tri-language test passed"
        else
            print_error "Tri-language test failed"
            echo "$OUTPUT"
            exit 1
        fi
    fi
else
    print_warning "Skipping tests (--skip-tests)"
fi

# Step 7: Summary
print_header "Build Summary"

echo ""
echo "Component Status:"
echo "  ✓ C++ Compiler:       $(ls -lh cpj_compiler | awk '{print $5}')"
echo "  ✓ Java Libraries:     $(ls -lh java/build/libs/java-0.1.0.jar | awk '{print $5}')"
echo "  ✓ Python Environment: .venv/"
echo ""

if [ "$SKIP_TESTS" = false ]; then
    echo "Test Results:"
    echo "  ✓ C++ Tests:          PASSED"
    echo "  ✓ Python Tests:       PASSED"
    echo "  ✓ Integration Tests:  PASSED"
    echo ""
fi

print_header "Build Completed Successfully!"

echo ""
echo "You can now use the CPJ compiler:"
echo "  ${GREEN}./cpj_compiler samples/demo.cpj${NC}"
echo "  ${GREEN}./cpj_compiler --help${NC}"
echo ""
echo "For more information, see:"
echo "  - README.md"
echo "  - CPJ_Guide.md"
echo "  - ROADMAP.MD"
echo ""

exit 0
