//
// Created by HurleyKane on 2024/5/7.
//
#include <string>
#include <utility>
#include <pybind11/pybind11.h>

struct Pet{
    explicit Pet(std::string name) : name(std::move(name)) {}
    void setName(const std::string& name_){ name = name_; }
    const std::string& getName() const { return name;}
    std::string name;
};
