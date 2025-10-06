enable_testing()

add_executable(cpj_tests
    test_compiler.cpp
    test_runtime.cpp
)

target_link_libraries(cpj_tests PRIVATE cpj_core)

add_test(NAME CPJTests COMMAND cpj_tests)