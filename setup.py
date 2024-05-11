import setuptools

VERSION = '0.0.2'

setuptools.setup(
    name = "pybind_study",
    version = VERSION,   #   两个地方都可以
    description = "pybind_study",
    author = "<NAME>",
    author_email = "<EMAIL>",
    url="https://github.com/hurleykane/pybind_study",
    packages=setuptools.find_packages("."),
    package_data = {
        # 引入任何包下的pyd文件，加入字典则对应包下的文件
        "core": ["*.pyd"]
    },
    install_requires=[
        "numpy",
    ]
)