#!/usr/bin/env python

from setuptools import setup

setup(name='zenoss',

version='0.6.4',
    description='Module to work with the Zenoss JSON API.',
    author="jim regovich",
    author_email='jregovic@rego.org'
    url='https://github.com/jregovic/python-zenoss',
    py_modules=['zenoss',],
    keywords = ['zenoss', 'api', 'json', 'rest'],
    test_suite='tests',
    data_files = [('', ['LICENSE.txt']),('', ['README.md']),]
)
