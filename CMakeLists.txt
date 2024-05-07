cmake_minimum_required(VERSION 3.28)
project(untitled11)

# 添加子目录 pybind11
add_subdirectory(extern/pybind11)

# 加入cpp文件
pybind11_add_module(example SHARED example.cpp)

# 设置输出文件后缀名为 .pyd
set_target_properties(example PROPERTIES SUFFIX ".pyd")

# 添加包含目录
include_directories(
        "E:\\DataBuffer\\hurleykane\\miniconda3\\include"
        "pybind11\\include"
)

# 添加库目录
set(PYTHON_LIB_DIR "E:\\DataBuffer\\hurleykane\\miniconda3\\libs")
find_library(PYTHON3_LIB python3 PATHS ${PYTHON_LIB_DIR})
find_library(PYTHON311_LIB python311 PATHS ${PYTHON_LIB_DIR})
link_directories(${PTTHON_LIB_DIR})

# 添加依赖项
target_link_libraries(example PUBLIC
        ${PYTHON3_LIB}
        ${PYTHON311_LIB}
)
