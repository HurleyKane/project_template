# 测试文件
add_executable(main main.cpp class_cat.cpp)
target_include_directories(main PRIVATE ${PROJECT_SOURCE_DIR}/include)

# 加入cpp文件
file(GLOB SOURCE_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp") # 找出改文件下所有cpp文件
pybind11_add_module(function SHARED ${SOURCE_FILES})
target_include_directories(function PRIVATE ${PROJECT_SOURCE_DIR}/include)

# 输出
set(LIBRARY_OUTPUT_PATH  ${CMAKE_CURRENT_SOURCE_DIR}/../core)  # 库文件输出目录
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../) # 设置可执行文件输出目录

# 添加依赖项
link_to_python(function)
