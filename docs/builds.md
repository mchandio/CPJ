Build helper notes

This document describes the minimal build scaffolding added to the repo:

Java (Gradle)
- Files: `java/build.gradle`, `java/settings.gradle`, `java/README.md`
- Usage: inside the repo root run `./gradlew -p java build` (if you add the Gradle wrapper), or `gradle -p java build` if Gradle is installed.
- The `Makefile` now includes a `java-build` target that will call Gradle if available.

C++ (CMake + FetchContent)
- Files: `cpp/CMakeLists.txt`, `cpp/conanfile.txt`
- Usage:
  - mkdir -p build && cd build
  - cmake -S .. -B .
  - cmake --build .
- The CMake file uses FetchContent to pull `nlohmann/json` as a header-only dependency. If you prefer `conan`, run `conan install ..` in the build dir and configure accordingly.

Makefile
- New targets:
  - `make java-build` — builds Java via Gradle (if wrapper or gradle available)
  - `make cpp-cmake` — prepares a CMake build directory

Notes
- These are minimal scaffolds intended to be non-invasive. If you'd like, I can add a Gradle wrapper, a Maven `pom.xml`, or full Conan/CI integration.
