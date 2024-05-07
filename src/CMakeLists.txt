# 加入cpp文件
pybind11_add_module(function SHARED binding.cpp add.cpp struct_test.cpp)
# 添加头文件目录
target_include_directories(function PRIVATE ${PROJECT_SOURCE_DIR}/include)
# 添加依赖项
link_to_python(function)