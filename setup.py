#!/usr/bin/py

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='simple algorithms and data structures',
    long_description=readme,
    author='Fabio Lima',
    license=license
)
