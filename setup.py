from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="pytorch-lamb",
    version="0.1.0",
    author="skyday123",
    author_email="",
    description="Implementation of LAMB optimizer in pytorch.",
    license="MIT",
    url="https://github.com/skyday123/pytorch-lamb",
    packages=find_packages(),
    install_requires=[
        'torch',
        ],
    )

