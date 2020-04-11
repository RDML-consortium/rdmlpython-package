#! /usr/bin/env python

import rdmlpython as rdml
from setuptools import setup

vers = rdml.get_rdml_lib_version()

print("Current version: " + vers)

setup(
    name='rdmlpython',
    version=vers,
    author='Andreas Untergasser',
    author_email='andreas@untergasser.de',
    packages=['rdmlpython'],
    url='https://github.com/RDML-consortium/rdmlpython',
    license='MIT',
    description='A package to read and edit RDML files.',
    long_description=open('README.txt').read(),
    install_requires=[
        "lxml >= 4.2.1",
        "numpy >= 1.17.2",
        "scipy >= 1.3.1", 
    ],
)
