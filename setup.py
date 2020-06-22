#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys

from setuptools import find_packages, setup
import subprocess

subprocess.call(
    [sys.executable, "-m", "pip", "install", "requirements-parser"])
import requirements  # noqa: F401

# Package meta-data.
NAME = 'Testing-Dependencies-'
DESCRIPTION = 'Testing repository for dependency checking'
URL = 'https://github.com/TuckerMullens/Testing-Dependencies-.git'
EMAIL = 'mullte17@wfu.edu'
AUTHOR = ['Tucker Mullens']
REQUIRES_PYTHON = '>=3.6.0'
VERSION = 1.1
REQUIRED = []
DEPENDENCY_LINKS = []

# What packages are required for this module to be executed?
with open('requirements.txt', 'r') as _file:
    for req in requirements.parse(_file):
        if req.specifier:
            REQUIRED.append(req.line)
        elif req.uri:
            # need to append the whole path with #egg=, not just the uri
            path = req.line.replace(
                '-e ',
                '')  # remove the optional -e prefix of the editable line
            DEPENDENCY_LINKS.append(path)
            REQUIRED.append(
                req.name)  # Seems like ralib-0.1 works, as well as ralib
        else:
            raise NotImplementedError

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests', )),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    dependency_links=DEPENDENCY_LINKS)
