#!/usr/bin/env python
from io import open  # Defaults to text mode with universal newlines.
from os import path

from setuptools import setup  # Prefer setuptools to distutils, always.


# Load the README text.
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sphinxcontrib-fontawesome',
    version='0.0.1',
    description='Support for `Font Awesome`_ icons and logos in Sphinx documentation.',
    long_description=long_description,
    # url='https://hedron-sphinx-theme.hedronvision.com',
    author='Sam Redmond',
    author_email='sredmond@stanford.edu',
    # Contents of the package.
    packages=['sphinxcontrib'],
    namespace_packages = ['sphinxcontrib'],
    include_package_data=True,
    # Supported Python versions. Unlike the classifiers, `pip install` actually
    # checks these constraints and refuses to install projects with mismatches.
    python_requires='>=3.5, <4'
)
