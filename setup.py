# 该库对C++进行
import os
import setuptools
from glob import glob
from setuptools import Extension
from setuptools.command.build_ext import build_ext

VERSION = '0.0.3'


# import subprocess
# cplus_projectPath = os.path.join(os.path.dirname(__file__), "pybindStudy", "Cplus")  # 子项目编译
# subprocess.run(["python", "setup.py", "build"], cwd=cplus_projectPath)

# 定义输出路径
class CustomBuildExt(build_ext):
    def get_ext_fullpath(self, ext_name):
        # 定义拓展构建后的输出路径
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "pybindStudy", "Cplus", "core"))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = self.get_ext_filename(ext_name)
        return os.path.join(output_dir, filename)


example_module = Extension(
    name="function",
    # sources = ["setup.cpp", "class_cat.cpp", "function_add.cpp", "struct_test.cpp"],
    sources=glob("pybindStudy/Cplus/source/*.cpp"),
    include_dirs=[r"pybindStudy/Cplus/include"]
)

setuptools.setup(
    name="pybindStudy",
    version=VERSION,  # 两个地方都可以
    description="pybind_study",
    author="<NAME>",
    author_email="<EMAIL>",
    url="https://github.com/hurleykane/pybind_study",
    packages=setuptools.find_packages("."),
    ext_modules=[example_module],
    package_data={
        # 引入任何包下的pyd文件，加入字典则对应包下的文件
        "": ["*.pyd"]
    },
    cmdclass={"build_ext": CustomBuildExt},
    install_requires=[
        "pybind11"
    ],
    setup_requires=[
    ]
)
