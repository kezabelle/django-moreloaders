#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-moreloaders",
    version="0.1.0",
    packages=find_packages(),
    tests_require=(
        'django-setuptest',
    ),
    test_suite='setuptest.setuptest.SetupTestSuite',
    author="Keryn Knight",
    author_email='python-package@kerynknight.com',
    description="more template loaders for Django",
    long_description=open(os.path.join(HERE, 'README.rst')).read(),
    keywords="django template loaders",
    license="BSD License",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: BSD License',
    ],
    platforms=['OS Independent'],
)
