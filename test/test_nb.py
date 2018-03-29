""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path
from urlparse import urlparse

from pycropml import pparse, render_notebook

from .test1 import example, cwd, xmls

REMOVE = True

##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)


    m2p = render_notebook.Model2Nb(models, dir='.');
    m2p.run()

    nb=Path('notebook')
    """if nb.exists() and nb.isdir():
        nb.rmtree()"""

    return models


if __name__ == '__main__':
    models = example()
    assert len(models)
    m2p = render_notebook.Model2Nb(models);
    m2p.run()
    code = m2p.code
    exec(code)
    codetest = m2p.codetest
    exec(codetest)
