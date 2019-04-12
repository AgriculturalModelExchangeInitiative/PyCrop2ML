""" Read xml representation of a component.

"""
from __future__ import absolute_import
from __future__ import print_function
from path import Path

from pycropml import pparse, render_python


cwd = Path(__file__).dirname()
data = cwd/'Tutorial'

packages = [p for p in data.listdir() if (p/'crop2ml').isdir()]
pkg_nrj, pkg_pheno = packages

##############################################################################
# Test on Example


def test_nrj():
    models = pparse.model_parser(pkg_nrj)
    assert len(models) == 13

def test_pheno():
    models = pparse.model_parser(pkg_pheno)
    assert len(models) == 12

def test_pkg2py_nrj():
    models = pparse.model_parser(pkg_nrj)

    m2p = render_python.Model2Package(models, dir='.', pkg_name="EnergyBalance")
    m2p.run()

def test_pkg2py_nrj():
    models = pparse.model_parser(pkg_pheno)

    m2p = render_python.Model2Package(models, dir='.', pkg_name="Phenology")
    m2p.run()
