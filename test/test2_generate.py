""" Generate a Python/OpenAlea package from an xml component.

"""
from path import Path
from pycropml import pparse, render_python

from .test1 import example, cwd, xmls






##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)
    return models
