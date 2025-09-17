cmake_minimum_required(VERSION 3.15)
project(cpj CXX)

# Optionally use FetchContent to get header-only nlohmann/json
include(FetchContent)

option(CPJ_BUILD_EXAMPLES "Build example targets" OFF)

FetchContent_Declare(
  nlohmann_json
  GIT_REPOSITORY https://github.com/nlohmann/json.git
  GIT_TAG v3.11.2
)
FetchContent_MakeAvailable(nlohmann_json)

add_executable(cpj_compiler
    ../cpj_compiler.cpp
)

target_include_directories(cpj_compiler PRIVATE ${nlohmann_json_SOURCE_DIR}/include)

# You can add other dependencies via target_link_libraries

if(CPJ_BUILD_EXAMPLES)
  # add example targets here
endif()
