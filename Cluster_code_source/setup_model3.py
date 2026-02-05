#!/usr/bin/env python3

from setuptools import setup, Extension
from Cython.Build import build_ext


ext = [
    Extension(
        'fpe_model3',['fpe_model3.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall"]
        ),
    Extension(
        'utilities',['utilities.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall"]
        )
    ]

ext_parallel = [
    Extension(
        'fpe_model3', ['fpe_model3.pyx'],
        extra_compile_args=["-Ofast", "-march=native", "-Wall"],
        extra_link_args=['-lm']
        ),
    Extension(
        'utilities',['utilities.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall"]
        )
    ]

setup(
    name="FPE",
    version="1.0",
    ext_modules=ext_parallel,
    cmdclass={'build_ext': build_ext}
    )
