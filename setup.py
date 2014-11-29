#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='flamework.api',
    namespace_packages=['flamework', 'flamework.api'],
    version='0.2',
    description='Base class for flamework-api derived API classes',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-flamework-api',
    dependency_links=[
      ],
    install_requires=[
    ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-flamework-api/releases/tag/v0.2',
    license='BSD')
