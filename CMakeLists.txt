cmake_minimum_required(VERSION 3.18)
project(geodesy LANGUAGES CXX)

# 查找 pybind11
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# 自动获取 pybind11 的 cmake 路径
execute_process(
    COMMAND "${Python3_EXECUTABLE}" -m pybind11 --cmakedir
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 CONFIG REQUIRED HINTS ${pybind11_DIR})
message(STATUS "Found pybind11 in: ${pybind11_DIR}")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/pybindStudy/Cplus/include)

file(GLOB SOURCES "./pybindStudy/Cplus/source/*.cpp")
pybind11_add_module(
        function MODULE ${SOURCES}
)

set(PYBIND_OUTPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/python) # 路径可自行选择
set_target_properties(function PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PYBIND_OUTPUT_DIR} # 输出路径
)