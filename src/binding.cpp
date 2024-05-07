//
// Created by HurleyKane on 2024/5/8.
//
#include <pybind11/pybind11.h>
#include "add.h"
#include "struct_test.cpp"

namespace py = pybind11;
PYBIND11_MODULE(function, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function that adds two numbers");
    py::class_<Pet>(m, "Pet")
            .def(py::init<const std::string &> ())
            .def("setName", &Pet::setName)
            .def("getName", &Pet::getName);
}
