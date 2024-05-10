# 利用Python setuptools + pybind11对cpp文件进行打包

from setuptools import setup, Extension

example_module = Extension(name="function",
                           sources=["setup.cpp", "class_cat.cpp", "function_add.cpp", "struct_test.cpp"],
                           include_dirs=[r"../include",
                                         r"../extern/pybind11/include"
                                         ]
                           )

setup(ext_modules=[example_module])
