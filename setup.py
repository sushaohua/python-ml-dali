#!/usr/bin/env python
"""The setup script."""
import os
import re
import sys

from setuptools import find_packages, setup

def get_version():
    """Get current version from code."""
    regex = r"__version__\s=\s\"(?P<version>[\d\.]+?)\""
    path = ("python-ml-dali", "__version__.py")
    return re.search(regex, read(*path)).group("version")

def read(*parts):
    """Read file."""
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)
    sys.stdout.write(filename)
    with open(filename, encoding="utf-8", mode="rt") as fp:
        return fp.read()


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='python-ml-dali',
    version=get_version(),
    url='https://github.com/benoitdepaire/python-ml-dali',
    license='GNU GPLv3',
    author='Benoît Depaire',
    install_requires=[],
    author_email='benoit@depaire.net',
    description='A Python library to communicate with Dali controllers from Ministry of Light',
    long_description=readme,
    packages=find_packages(include=["mldali"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)d",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]

)