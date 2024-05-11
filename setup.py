# 该库对C++进行
import os
import subprocess
import setuptools

VERSION = '0.0.2'

cplus_projectPath = os.path.join(os.path.dirname(__file__), "pybindStudy", "Cplus")  # 子项目编译
subprocess.run(["python", "setup.py", "build"], cwd=cplus_projectPath)

setuptools.setup(
    name="pybindStudy",
    version=VERSION,  # 两个地方都可以
    description="pybind_study",
    author="<NAME>",
    author_email="<EMAIL>",
    url="https://github.com/hurleykane/pybind_study",
    packages=setuptools.find_packages("."),
    package_data={
        # 引入任何包下的pyd文件，加入字典则对应包下的文件
        "": ["*.pyd"]
    },
    install_requires=[
    ],
    setup_requires=[
        "examplepackage"
    ]
)
