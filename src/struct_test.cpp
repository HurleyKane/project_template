#include "struct_test.h"
#include <string>

Pet::Pet(std::string &name) : name(name) {}

void Pet::setName(const std::string &name_) { name = name_;}

const std::string& Pet::getName() const {
    return name;
}

