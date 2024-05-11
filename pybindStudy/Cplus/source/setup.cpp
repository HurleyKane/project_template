#include <pybind11/pybind11.h>
#include "add.h"
#include "struct_test.h"
#include "class_cat.h"

namespace py = pybind11;
PYBIND11_MODULE(function, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    /**************************普通函数********************/
    m.def("add", &add, "A function that adds two numbers",
          py::arg("i") = 1, py::arg("j") = 2
          );
    // shorthand
    using namespace pybind11::literals;
    m.def("add2", &add, "i"_a = 1, "j"_a = 2);
    /*************************struct结构体***********************/
    py::class_<Pet>(m, "Pet")
            .def(py::init<std::string &>())
            // 读写定义
            .def("setName", &Pet::setName)
            .def("getName", &Pet::getName)
            // 直接读写操作
            .def_readwrite("name", &Pet::name)
            .def_readwrite("age", &Pet::age)
            // lambda function [capture list](parameter list) -> return type { function body }
            .def("__repr__",
                 [](const Pet &a){
                            return "<example.Pet named '" + a.name + "'>";
                 }
                 )
            // 重载函数的定义
            .def("set", static_cast<void (Pet::*)(int)>(&Pet::set), py::arg("age"))
            .def("set", static_cast<void (Pet::*)(const std::string&)>(&Pet::set))
            .def("set1", py::overload_cast<int>(&Pet::set)) //重载更高级的写法，减少了返回类型 C++14以上支持
            ;

    /**************************class*****************************/
    py::class_<test11>(m, "test11")
            .def(py::init<std::string &>())
            .def_property("name", &test11::getName, &test11::setName);  //具有定义和返回两种形式的动态属性
            //返回结构体的属性设置
            // .def_property("data",
            //               py::cpp_function(&MyClass::getData, py::return_value_policy::copy),
            //               py::cpp_function(&MyClass::setData)
            // );
    //返回结构体引用
    m.def("get_class", &get_test11, py::return_value_policy::reference);
}
