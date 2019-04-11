""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path
#from urlparse import urlparse

from pycropml import pparse, render_csharp

from .test1bis import example, cwd, xmls

from test import test1


##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)


    m2p = render_csharp.Model2Package(models, dir='.');
    m2p.run()

    code = m2p.code
    #exec(code)

    codetest = m2p.codetest

    mymodel = Path('csharp_model')
    mymodel.chdir()
    os.system('nosetests')

    Path('..').chdir()
    """if csharp_model.exists():
        csharp_model.rmtree()"""

    return models


if __name__ == '__main__':
    models = example()
    assert len(models)
    m2p = render_csharp.Model2Package(models);
    m2p.run()
    code = m2p.code
    #exec(code)
    codetest = m2p.codetest
    #exec(codetest)