#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'WB sync services'
DESCRIPTION = 'WB synchronization services'
URL = 'https://github.com/aghatti/wb_rep'
EMAIL = ''
AUTHOR = 'Dan'
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '0.1.0'


    
setup(
    name='wb',
    version='1.0',
    include_package_data=True,
    description='WB synchronization services',
    author='Dan',
    author_email='',
    url='https://github.com/aghatti/wb_rep',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "idna==3.6",
        "mysql-connector-python==8.3.0",
        "requests==2.31.0",
        "python-dateutil==2.9.0.post0",
        "urllib3==2.2.1",
    ]
)
