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

    m2p = render_python.Model2Package(models);
    m2p.run()

    code = m2p.code
    exec(code)

    return models
