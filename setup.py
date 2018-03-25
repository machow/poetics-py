#!/usr/bin/env python

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('poetics.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
	name = 'poetics',
	version = version,
	py_modules= ['poetics'],
	install_requires = [],
        description = 'computational poetry',
        author = 'Michael Chow',
        author_email = 'mc_al_github@fastmail.com',
        url = 'https://github.com/machow/poetics')

