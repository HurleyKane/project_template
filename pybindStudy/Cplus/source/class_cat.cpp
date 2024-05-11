//
// Created by HurleyKane on 2024/5/8.
//
#include <class_cat.h>
#include <string>

test11::test11(std::string &name) : name(name) {}

void test11::setName(const std::string &name_) { name = name_;}

const std::string &test11::getName() {return name;}

test11& get_test11(){
    std::string name = "fadfasdf";
    static test11 obj(name);
    return obj;
}