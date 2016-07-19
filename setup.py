#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/flamework.api.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read(),

setup(
    name='flamework.api',
    namespace_packages=['flamework', 'flamework.api'],
    version=version,
    description='Base class for flamework-api derived API classes',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-flamework-api',
    dependency_links=[
    ],
    install_requires=[
        'requests'
    ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-flamework-api/releases/tag/' + version,
    license='BSD')
