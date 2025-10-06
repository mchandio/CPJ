add_library(cpj_core
    runtime/memory_manager.cpp
    frontend/java/SemanticAnalyzer.cpp
)

target_include_directories(cpj_core PUBLIC
    ${CMAKE_SOURCE_DIR}/include
)