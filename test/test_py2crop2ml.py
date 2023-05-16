""" Read xml representation of a component
    and translate Crop2ML models to python codes

"""
from __future__ import absolute_import
from __future__ import print_function
from path import Path

from pycropml.cyml import transpile_component

cwd = Path(__file__).dirname()
package = cwd/'Models'/'SQ_Energy_Balance_py'


##############################################################################
# Test on Example


def test_py2crop2ml():
    transpile_component(package,package,"py")



test_py2crop2ml()

