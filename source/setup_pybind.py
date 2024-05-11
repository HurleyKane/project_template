import os
from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

# 定义输出路径
class CustomBuildExt(build_ext):
    def get_ext_fullpath(self, ext_name):
        # 定义拓展构建后的输出路径
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core"))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = self.get_ext_filename(ext_name)
        return os.path.join(output_dir, filename)

    def build_extension(self, ext):
        # 构建路径
        ext.build_lib = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "include"))
        super().build_extension(ext)

example_module = Pybind11Extension(
    name = "function",
    # sources = ["setup.cpp", "class_cat.cpp", "function_add.cpp", "struct_test.cpp"],
    sources = glob("*.cpp"),
    include_dirs=[r"../include"]
)

setup(
    name="example_package",
    version="core.0",
    author = "chenmingkai",
    description = "This is a test package",
    ext_modules=[example_module],
    cmdclass={"build_ext":CustomBuildExt}  # 确保所有与pybind11配套的优化和配置被实施和考虑
)
