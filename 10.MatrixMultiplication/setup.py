from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    name="cmatmul",
    sources=["cmatmul.pyx", "matmul.cpp"],
    language="c++",
    extra_compile_args=["-std=c++20"],
)

setup(ext_modules=cythonize(ext))
