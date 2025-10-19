cmake_minimum_required(VERSION 3.18)
project(geodesy LANGUAGES CXX)

# 查找 pybind11
find_package(pybind11 CONFIG REQUIRED)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/pybindStudy/Cplus/include)

file(GLOB SOURCES "./pybindStudy/Cplus/source/*.cpp")
pybind11_add_module(
        function MODULE ${SOURCES}
)

set(PYBIND_OUTPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}) # 路径可自行选择
set_target_properties(function PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PYBIND_OUTPUT_DIR} # 输出路径
)
