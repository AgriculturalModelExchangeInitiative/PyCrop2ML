""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse

data = Path('data')
xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def example():
    fn = data.glob('Example*.xml')[0]

    models = pparse.parse(fn)
    return models

def test1():
    models = example()
    assert len(models) == 1

    model = models[0]
    assert model.algorithm

    lines = [l for l in model.algorithm.split('\n') if l.strip()]
    assert len(lines) == 3

    assert len(model.inputs) == 10
    # TODO: check the different inputs (name at least)

    assert len(model.outputs) == 1
    # TODO Check the output

    # check Description:
    #TODO

    # Check ParameterSets
    assert len(model.parametersets) == 5
    v = ['soil', 'sorghum', 'wheat', 'crop', 'wheat.cv1']
    for k in v:
        assert k in model.parametersets

    # Check each parameterset: TODO

    # Check tests: TODO
