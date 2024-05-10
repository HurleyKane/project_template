//
// Created by HurleyKane on 2024/5/8.
//

#ifndef PYBIND_TEST_CLASS_CAT_H
#define PYBIND_TEST_CLASS_CAT_H
#include <iostream>
class test11 {
public:
    explicit test11(std::string& name);
    void setName(const std::string& name_);
    const std::string& getName();
private:
    std::string name;
};

test11& get_test11();
#endif //PYBIND_TEST_CLASS_CAT_H
