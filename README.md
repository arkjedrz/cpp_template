# cpp_template

CMake/Conan-based template for C++ projects.

## Usage

Replace cpp_template with project name and remove redundant example files.

Quick start:

```bash
mkdir build && cd build
conan install ..
cmake ..
cmake --build .
./bin/cpp_template
```

## TODOs

- separate library and executable logic in src to simplify testing

## Tested configurations

- Ubuntu 22.04
