cmake_minimum_required(VERSION 3.18)
project(cpp_template)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory("src/")
add_subdirectory("tests/")
