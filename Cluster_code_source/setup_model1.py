#!/usr/bin/env python3

from distutils.core import setup, Extension
from Cython.Build import build_ext


ext = [
    Extension(
        'fpe_model1',['fpe_model1.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall"]
        ),
    Extension(
        'utilities',['utilities.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall"]
        )
    ]

ext_parallel = [
    Extension(
        'fpe', ['fpe.pyx'],
        extra_compile_args=["-Ofast", "-march=native", "-Wall","-fopenmp"],
        extra_link_args=['-fopenmp','-lm']
        ),
    Extension(
        'utilities',['utilities.pyx'],
        extra_compile_args=["-Ofast", "-v", "-march=native", "-Wall","-fopenmp"]
        )
    ]

setup(
    name="FPE1",
    version="1.0",
    ext_modules=ext_parallel,
    cmdclass={'build_ext': build_ext}
    )
