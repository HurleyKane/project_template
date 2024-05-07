# 加入cpp文件
pybind11_add_module(add SHARED add.cpp)

# 设置输出文件后缀名为 .pyd
set_target_properties(
        add PROPERTIES SUFFIX ".pyd"
)

# 添加依赖项
link_to_python(add)