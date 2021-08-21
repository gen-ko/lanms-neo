from glob import glob
from os import path
from setuptools import setup, find_packages

from pybind11.setup_helpers import Pybind11Extension, build_ext

this_dir = path.dirname(path.abspath(__file__))
extensions_dir = path.join(this_dir, "lanms", "csrc")

ext_modules = [
    Pybind11Extension(
        'lanms._C',
        sorted(glob('lanms/csrc/*.cpp')) + sorted(glob('lanms/csrc/clipper/*.cpp')),
        include_dirs=[extensions_dir],
    )
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lanms_neo',
    version='1.0.2',
    author="gen-ko",
    author_email="yuanl5@alumni.cmu.edu",
    description="Standalone Locality-Aware NMS module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gen-ko/lanms-neo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=ext_modules,
    cmdclass= {'build_ext': build_ext},
    packages=find_packages(exclude=['tests']),
)

