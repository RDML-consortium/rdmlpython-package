#! /usr/bin/env python

from setuptools import setup

setup(
    name='rdmlpython',
    version='0.8.3',
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
    ],
)
