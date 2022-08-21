cmake_minimum_required(VERSION 3.18)
project(cpp_templateTests)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-Wall -Wextra -pedantic)

set(SRC_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/test_hello.cpp
    ${CMAKE_SOURCE_DIR}/src/hello.cpp
)

include_directories(${CMAKE_SOURCE_DIR}/src)

add_executable(cpp_templateTests ${SRC_FILES})
target_link_libraries(cpp_templateTests
    CONAN_PKG::gtest
)
