# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='mcp23017',
    version='0.1.0',
    description='MCP23017 Library',
    long_description=readme,
    author='Mirko Haeberlin',
    author_email='mirko.haeberlin@sensorberg.com',
    url='https://github.com/sensorberg-dev/MCP23017-python',
    packages=find_packages(exclude=('tests', 'docs'))
)