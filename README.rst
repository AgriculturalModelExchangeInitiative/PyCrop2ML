========================
Pycrop2ml
========================
..  image:: https://readthedocs.org/projects/pycrop2ml/badge/?version=latest
    :target: http://pycrop2ml.readthedocs.io/en/latest/
    :alt: Documentation Status
 
 .. image:: https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML/actions/workflows/codeql-analysis.yml/badge.svg
    :alt: CodeQL
    :target: https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML/actions/workflows/codeql-analysis.yml/

.. {# pkglts, doc

.. #}

A Python library to generate components from Crop2ML declarative language.

For more information, refer to `the documentation`__.

.. __: http://pycrop2ml.readthedocs.io/en/latest/


Dependencies
============
- openalea.core and openalea.deploy

   conda install -c conda-forge -c openalea3 openalea.core openalea.deploy

Installation
============


Using pip
~~~~~~~~~~~


   git clone https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML.git
   
   cd PyCropML
   
   pip install - r requirements.txt
   
   pip install .
   
   pip install antlr4-python3-runtime==4.8
