""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path

from pycropml import pparse, render_python

from .test1 import example, cwd

from test import test1


##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)


    m2p = render_python.Model2Package(models, dir='.',pkg_name="Phenology")
    m2p.run()

    code = m2p.code
    exec(code)

    codetest = m2p.codetest


    mymodel = Path("python_model")
    mymodel.chdir()
    os.system('nosetests')

    Path("..").chdir()
    """if mymodel.exists():
        mymodel.rmtree()"""

    return models


if __name__ == '__main__':
    models = example()
    assert len(models)
    m2p = render_python.Model2Package(models)
    m2p.run()
    code = m2p.code
    exec(code)
    codetest = m2p.codetest
    exec(codetest)