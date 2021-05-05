""" Generate a Python/OpenAlea package from an xml component.

"""
from __future__ import absolute_import
import os
from path import Path
#from urlparse import urlparse

from pycropml import render_R

from .test1 import example,cwd


##############################################################################
# Test on Example


def test1():
    models = example()
    assert len(models)


    m2p = render_R.Model2Package(models, dir=cwd,pkg_name="EnergyBalance")
    m2p.run()
    mymodel = Path('r_model')
    mymodel.chdir()
    os.system('nosetests')

    Path('..').chdir()
    """if mymodel.exists():
        mymodel.rmtree()"""

    return models


if __name__ == '__main__':
    models = example()
    assert len(models)
    m2p = render_R.Model2Package(models);
    m2p.run()
