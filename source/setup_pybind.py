from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

example_module = Pybind11Extension(
    name = "function",
    sources = ["setup.cpp", "class_cat.cpp", "function_add.cpp", "struct_test.cpp"],
    include_dirs=[r"../include"]
)

setup(
    name="example_package",
    version="1.0",
    author = "chenmingkai",
    description = "This is a test package",
    ext_modules=[example_module],
    cmdclass={"build_ext": build_ext}  # 确保所有与pybind11配套的优化和配置被实施和考虑
)
