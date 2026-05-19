cmake_minimum_required(VERSION 3.16)
project(CPJ VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Platform-independent settings
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_SHARED_LIBS ON)

# Enable LTO (Link Time Optimization) for better cross-platform performance
include(CheckIPOSupported)
check_ipo_supported(RESULT supported OUTPUT error)
if(supported)
    set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()

# Platform-specific settings
if(WIN32)
    add_definitions(-DWIN32_LEAN_AND_MEAN)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
elseif(APPLE)
    set(CMAKE_MACOSX_RPATH ON)
endif()

# Ensure platform-independent paths
file(TO_CMAKE_PATH "${PROJECT_BINARY_DIR}" BINARY_DIR)
file(TO_CMAKE_PATH "${PROJECT_SOURCE_DIR}" SOURCE_DIR)

# CPJ compiler executable
add_executable(cpj_compiler
    cpj_compiler.cpp
)

if(WIN32)
    set_target_properties(cpj_compiler PROPERTIES OUTPUT_NAME cpj)
endif()

# Install rules
install(TARGETS cpj_compiler
    RUNTIME DESTINATION bin
)

# Package configuration
include(CPack)
set(CPACK_PACKAGE_NAME "CPJ")
set(CPACK_PACKAGE_VENDOR "CPJ Team")
set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})
