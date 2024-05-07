//
// Created by HurleyKane on 2024/5/8.
//

#ifndef PYBIND_TEST_STRUCT_TEST_H
#define PYBIND_TEST_STRUCT_TEST_H

#include <string>
struct Pet{
    Pet(const std::string& name);
    void setName(const std::string& name_);
    const std::string& getName();
    std::string name;
};
#endif //PYBIND_TEST_STRUCT_TEST_H
