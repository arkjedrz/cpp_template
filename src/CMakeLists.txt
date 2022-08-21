cmake_minimum_required(VERSION 3.18)
project(cpp_template)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-Wall -Wextra -pedantic)

set(SRC_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/hello.cpp
)

include_directories(${CMAKE_PROJECT_NAME}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable(${CMAKE_PROJECT_NAME} ${SRC_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME}
    # CONAN_PKGs here, eg:
    # CONAN_PKG::imgui
)