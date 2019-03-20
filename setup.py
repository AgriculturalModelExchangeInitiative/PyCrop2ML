#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from os import walk
from os.path import abspath, normpath, splitext
from os.path import join as pj

from setuptools import setup, find_packages


short_descr = "A Python library to generate components from CropML declarative language"
readme = open('README.rst').read()
history = open('HISTORY.rst').read()


# find version number in src/pycropml/version.py
version = {}
with open("src/pycropml/version.py") as fp:
    exec(fp.read(), version)

# find packages
pkgs = find_packages('src')

pkg_data = {}

nb = len(normpath(abspath("src/pycropml"))) + 1
data_rel_pth = lambda pth: normpath(abspath(pth))[nb:]

data_files = []
for root, dnames, fnames in walk("src/pycropml"):
    for name in fnames:
        if splitext(name)[-1] in [u'.json', u'.ini']:
            data_files.append(data_rel_pth(pj(root, name)))


pkg_data['pycropml'] = data_files

setup_kwds = dict(
    name='pycropml',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="Cyrille Ahmed Midingoyi",
    author_email="cyrille.midingoyi@inra.fr",
    url='https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML',
    license='MIT',
    zip_safe=False,

    packages=pkgs,
    package_dir={'': 'src'},
    
    
    package_data=pkg_data,
    setup_requires=[
        ],
    install_requires=[
        ],
    tests_require=[
        "mock",
        "nose",
        "sphinx",
        ],
    entry_points={"console_scripts": ["cyml = pycropml.cyml:main"]},
    keywords='',
    
    test_suite='nose.collector',
    )
# #}
# change setup_kwds below before the next pkglts tag

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
