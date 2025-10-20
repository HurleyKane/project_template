import os
import sys
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = 'Debug' if self.debug else 'Release'
        build_temp = self.build_temp

        os.makedirs(build_temp, exist_ok=True)
        subprocess.check_call([
            "cmake",
            os.path.abspath("."),
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}"
        ], cwd=build_temp)
        subprocess.check_call(["cmake", "--build", "."], cwd=build_temp)


setup(
    ext_modules= [Extension("function", [])],
    cmdclass={"build_ext": CMakeBuild},
)
