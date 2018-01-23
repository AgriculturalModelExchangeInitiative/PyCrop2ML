""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse

data = Path('data')
xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def test1():
    fn = data.glob('Example*.xml')[0]

    models = pparse.parse(fn)
    return models