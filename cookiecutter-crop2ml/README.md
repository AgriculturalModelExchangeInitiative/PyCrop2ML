# Cookiecutter Crop2ML

_A logical, reasonably standardized, but flexible project structure for sharing crop models components between crops modelling platform._


#### [Project homepage](https://github.com/AgriculturalModelExchangeInitiative/PyCrop2ML/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── tests             <- model tests
│
├── crop2ml          <- model units and composite.
│
|
│
├── src                <- Source code for use in this project.
│   ├── cython
│   │
│   ├── 
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://cropml.readthedocs.io/en/latest/).


