#!/usr/bin/env python3

import os
from setuptools import setup
from sirbro_rest_saml2_example import __projname__, __projver__, __projdesc__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#
# list of classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    #use_scm_version=True,
    #setup_requires=['setuptools_scm'],
    install_requires=['flask>=0.11'],
    dependency_links=['https://github.com/pypa/setuptools_scm/archive/v1.11.1.zip'],
    name = __projname__,
    version = __projver__,
    author = "Benjamin Boortz",
    author_email = "benjamin.boortz@secure.mailbox.org",
    description = (__projdesc__),
    license = "GPLv3",
    keywords = "xaas broker service api lib",
    url = "http://packages.python.org/sirbro_rest_saml2_example",
    packages=['sirbro_rest_saml2_example', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
    test_suite = "sirbro_rest_saml2_example.tests.test_all",
)
