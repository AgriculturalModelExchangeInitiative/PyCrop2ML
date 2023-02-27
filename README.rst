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

Using conda
~~~~~~~~~~~

    conda install -c amei -c openalea3 -c conda-forge pycropml
    
Usage
=====

From Platforms to Crop2ML
~~~~~~~~~~~~~~~~~~~~~~~~~

    cyml -c "name_of_the_component_repository" "absolute_path_of_the_output" "source_language_or_platform"

From Crop2ML to Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~

    cyml -p "name_of_the_Crop2ML_package" "target_language_or_platform_"
