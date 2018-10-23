#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import sys
import os

assert sys.version_info >= (2, 7), 'We only support Python 2.7+'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clubhouse'))

VERSION = '0.1.0'


setup(
    name='clubhouse',
    version=VERSION,
    description='A python client library for the clubhouse.io api',
    long_description=open('README.rst').read(),
    author=', '.join([
        'Mahmoud Abdelkader',
    ]),
    url='https://github.com/mahmoudimus/clubhouse',
    packages=find_packages(exclude=('tests', 'examples')),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'marshmallow>=3.0.0b18',
        'attrs>=17.4.0',
        'requests>=2.20.0',
    ],
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
