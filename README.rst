=========
Pycrop2ml
=========
..  image:: https://readthedocs.org/projects/pycrop2ml/badge/?version=latest
    :target: http://pycrop2ml.readthedocs.io/en/latest/
    :alt: Documentation Status
 
..  image:: https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML/actions/workflows/codeql-analysis.yml/badge.svg
    :alt: CodeQL Status
    :target: https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML/actions/workflows/codeql-analysis.yml

.. image:: https://anaconda.org/amei/pycropml/badges/platforms.svg   
    :target: https://anaconda.org/amei/pycropml

.. image:: https://anaconda.org/amei/pycropml/badges/version.svg
    :target: https://anaconda.org/amei/pycropml

.. {# pkglts, doc

.. #}

A Python library to generate components from Crop2ML declarative language.

For more information, refer to `the documentation`__.

.. __: http://pycrop2ml.readthedocs.io/en/latest/



Installation
============

PyCropML relies on two Python packages to build the diagrams of a Crop2ML
composition: ``pydot``, a pure-Python library that describes the graph, and
``graphviz``, which only talks to the separate `Graphviz
<https://graphviz.org/download/>`_ ``dot`` **executable** that actually
renders it as an image. Both Python packages install automatically with
PyCropML below, but the ``dot`` executable itself is a system-level
dependency that pip cannot install for you. Without it, ``cyml -p ...``
fails as soon as a package links more than one ModelUnit, with::

    graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot')

Using conda
~~~~~~~~~~~

The ``conda-forge`` channel ships the Graphviz executables alongside the
Python packages, so this route needs nothing extra::

    conda install -c amei -c openalea3 -c conda-forge pycropml

Using pip
~~~~~~~~~

PyCropML is not yet published on PyPI, so install it from a source
checkout. Install the Graphviz executables first, since pip cannot::

    conda install -c conda-forge graphviz    # inside any conda environment
    # or, on Debian/Ubuntu:
    sudo apt install graphviz

Then install PyCropML itself::

    git clone https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML.git
    cd PyCrop2ML
    pip install .

Developer installation
~~~~~~~~~~~~~~~~~~~~~~~

To work on PyCropML itself — running its test suite, building its
documentation, or modifying its generators — install it in **editable**
mode from the same source checkout, after installing Graphviz as above::

    git clone https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML.git
    cd PyCrop2ML
    pip install -e ".[test,doc]"

``-e`` (editable) makes changes under ``src/pycropml`` take effect
immediately, with no reinstall step in between — the workflow used
throughout PyCropML's own test suite. ``[test,doc]`` pulls in ``pytest``
and the Sphinx toolchain declared as optional dependencies in
``pyproject.toml``; drop the extras (``pip install -e .``) for a plain
editable install.

Usage
=====

From Platforms to Crop2ML
~~~~~~~~~~~~~~~~~~~~~~~~~

    cyml -c name_of_the_component_repository absolute_path_of_the_output source_language_or_platform

From Crop2ML to Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~

    cyml -p name_of_the_Crop2ML_package target_language_or_platform

Testing
=======

Run the test suite using pytest or unittest:

Using pytest
~~~~~~~~~~~~
::

    # Run all tests
    python -m pytest test/cyml/test_cyml_operations.py -v
    
    # Run a specific test class
    python -m pytest test/cyml/test_cyml_operations.py::TestCyMLOperations -v
    
    # Run a single test
    python -m pytest test/cyml/test_cyml_operations.py::TestCyMLOperations::test_modulo_operation -v

Using unittest
~~~~~~~~~~~~~~
::

    cd test/cyml
    python -m unittest test_cyml_operations
