""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path
#from urlparse import urlparse

from pycropml import render_java

from .test1bis2 import example


##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)


    m2p = render_java.Model2Package(models, dir='.');
    m2p.run()
    mymodel = Path('java_model')
    mymodel.chdir()
    os.system('nosetests')

    Path('..').chdir()
    """if csharp_model.exists():
        csharp_model.rmtree()"""

    return models


if __name__ == '__main__':
    models = example()
    assert len(models)
    m2p = render_java.Model2Package(models);
    m2p.run()
    code = m2p.code
    #exec(code)
    codetest = m2p.codetest
    #exec(codetest)