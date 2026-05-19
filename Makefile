CC=g++
PYTHON=python3
GRADLE=./gradlew


all: cpj_compiler java_compile python-install

cpj_compiler:
	$(CC) -o cpj_compiler cpj_compiler.cpp

# Use Gradle to build Java components (includes ANTLR dependencies)
java_compile:
	@echo "Building Java components with Gradle..."
	$(GRADLE) build -x test
	@echo "Java build complete."

run:
	# Run the compiler against the sample CPJ program. Adjust the path as needed.
	./cpj_compiler samples/demo.cpj || true

# Build and run the DOS system
.PHONY: dos
dos: cpj_compiler python-install
	@echo "Building DOS system..."
	./cpj_compiler dos_shell.cpj
	./cpj_compiler dos_filesystem.cpj
	./cpj_compiler dos_memory.cpj
	@echo "Starting CPJ-DOS..."
	.venv/bin/python -c "from dos_shell import DOSShell; DOSShell().run()"


# Build the compiler and run a CPJ sample end-to-end (emit + run).
.PHONY: run-sample
run-sample: cpj_compiler
	@echo "Building cpj_compiler and running samples/types_demo.cpj (verbose)..."
	./cpj_compiler -v -o generated samples/types_demo.cpj || true

python-install:
	@echo "Creating venv and installing Python requirements..."
	python3 -m venv .venv || true
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -e .
	.venv/bin/python -m pip install -r requirements.txt || true

python-test:
	@echo "Running Python tests in venv..."
	.venv/bin/python -m pytest -q

# Quick test target: runs the small emit-and-run smoke test (fast)
test:
	@echo "Running quick CPJ smoke test..."
	# Run both quick smoke tests and generate a junit xml report for CI
	mkdir -p reports
	pytest -q \
		tests/test_emit_and_run.py::test_emit_and_run_demo \
		tests/test_types_demo_emit.py::test_types_demo_emits_and_runs \
		--junitxml=reports/junit.xml


.PHONY: ci-quick
ci-quick:
	@echo "Running CI quick tests (PYTHONPATH=. -> reports/junit.xml)"
	PYTHONPATH=. pytest -q \
		tests/test_emit_and_run.py::test_emit_and_run_demo \
		tests/test_types_demo_emit.py::test_types_demo_emits_and_runs \
		--junitxml=reports/junit.xml

# Full test suite
test-all:
	@echo "Running full pytest suite..."
	pytest -q

coverage:
	@echo "Running tests with coverage..."
	mkdir -p reports
	pytest -q --cov=tools --cov=python --cov-report=xml:reports/coverage.xml


clean:
	rm -f cpj_compiler
	rm -rf build
	rm -f java/*.class
	rm -rf bin

release: all
	./scripts/create_release.sh v1.0.0


# Vendor Java libs
LIB_DIR=lib
lib/%.jar:
	mkdir -p lib
	@echo "Place $* in lib/ or use a build tool to fetch it"


# C++ deps guidance
# Add include paths and link flags for chosen libraries (e.g. -I/path/to/include -L/path/to/lib)

# Gradle helper: build Java artifacts if Gradle wrapper or gradle available
.PHONY: java-build
java-build:
	@if [ -x ./gradlew ]; then \
		./gradlew -p java build; \
	else \
		if command -v gradle > /dev/null 2>&1; then \
			gradle -p java build || true; \
		else \
			echo "Gradle not found. To build Java artifacts, install Gradle or run ./gradlew in the java/ directory."; \
		fi; \
	fi

# CMake helper for C++: optional fetch nlohmann/json via FetchContent
.PHONY: cpp-cmake
cpp-cmake:
	@mkdir -p build && cd build && \
		cmake -S .. -B . -DCPJ_BUILD_EXAMPLES=OFF || true

src/runtime/memory_manager.cpp: src/runtime/memory_manager.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Add to build objects
OBJS += src/runtime/memory_manager.o

# Test framework
test/framework/test_framework.o: test/framework/test_framework.cpp test/framework/test_framework.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

test/framework/test_examples.o: test/framework/test_examples.cpp test/framework/test_framework.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

test_runner: test/framework/test_framework.o test/framework/test_examples.o
	$(CXX) $(CXXFLAGS) $^ -o $@

test: test_runner
	./test_runner

.PHONY: test
