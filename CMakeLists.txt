cmake_minimum_required(VERSION 3.16)
project(CPJ VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Platform-specific settings
if(WIN32)
    add_definitions(-DWIN32_LEAN_AND_MEAN)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
elseif(APPLE)
    set(CMAKE_MACOSX_RPATH ON)
endif()

# Add subdirectories
add_subdirectory(src)
add_subdirectory(test)

# Main CPJ library
add_library(cpj SHARED
    src/runtime/memory_manager.cpp
    src/frontend/java/SemanticAnalyzer.cpp
    # Add other source files
)

# CPJ compiler executable
add_executable(cpj_compiler
    cpj_compiler.cpp
)

target_link_libraries(cpj_compiler PRIVATE cpj)

# Install rules
install(TARGETS cpj cpj_compiler
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Package configuration
include(CPack)
set(CPACK_PACKAGE_NAME "CPJ")
set(CPACK_PACKAGE_VENDOR "CPJ Team")
set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})