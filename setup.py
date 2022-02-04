"""Create a python package."""
from distutils.core import setup

from setuptools import find_packages

setup(name="Calculator",
      version="1.0",
      description="Simple python calculator",
      author="Piotr Kolebski",
      packages=find_packages(exclude="tests"),
      )
