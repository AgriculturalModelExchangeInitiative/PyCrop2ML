""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path
from urlparse import urlparse

from pycropml import pparse, render_python

from .test1 import example, cwd, xmls

from test import totalparse


##############################################################################
# Test on Example


def test1():
    models = totalparse.totalexample()
    assert len(models)


    m2p = render_python.Model2Package(models, dir='.');
    m2p.run()

    code = m2p.code
    exec(code)

    codetest = m2p.codetest

    mymodel = Path('mymodel')
    mymodel.chdir()
    os.system('nosetests')

    Path('..').chdir()
    if mymodel.exists():
        mymodel.rmtree()

    return models


if __name__ == '__main__':
    models = totalparse.totalexample()
    assert len(models)
    m2p = render_python.Model2Package(models);
    m2p.run()
    code = m2p.code
    exec(code)
    codetest = m2p.codetest
    exec(codetest)
