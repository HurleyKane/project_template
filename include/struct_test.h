#ifndef PYBIND_TEST_STRUCT_TEST_H
#define PYBIND_TEST_STRUCT_TEST_H

#include <string>

struct Pet {
    // 构造函数，使用 std::move 来优化字符串的移动
    explicit Pet(std::string& name);

    // 设置宠物的名字
    void setName(const std::string& name_);

    void set(int age_);

    void set(const std::string& name_);

    // 获取宠物的名字
    const std::string& getName() const;

    std::string name;

    int age;
};

#endif // PYBIND_TEST_STRUCT_TEST_H
