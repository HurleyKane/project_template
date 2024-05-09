#ifndef PYBIND_TEST_STRUCT_TEST_H
#define PYBIND_TEST_STRUCT_TEST_H

#include <string>

struct Pet {
    std::string name;

    // 构造函数，使用 std::move 来优化字符串的移动
    explicit Pet(std::string& name);

    // 设置宠物的名字
    void setName(const std::string& name_);

    // 获取宠物的名字
    const std::string& getName() const;
};

#endif // PYBIND_TEST_STRUCT_TEST_H
