""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse

data = Path('test\data')
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
    name_input=['BaseTemp','MinTemp','GrowthRate', 'GrowthRateResponse', 'PlantAvailableWater', 'DrougtSensitivity', 'AvailableWater', 'BoltzmannConstant', 'AvailableWater', 'AtmosphericEmisivity']
    for k in name_input:
        assert k in [model.inputs[l].name for l in range(0,len(name_input))]
        
    assert len(model.outputs) == 1
    # TODO Check the output
    name_output=['PlantGrowth']     # we can add other outputs. we have just one with our example
    algo_name = [l.split()[0] for l in lines]    #extract algorithm functions names  
    for k in name_output:
        assert k in algo_name  # check output in algorithm functions names

    # check Description:
    # TODO
    assert model.description
    # Check ParameterSets
    assert len(model.parametersets) == 5
    v = ['soil', 'sorghum', 'wheat', 'wheat.cv1', 'crop']
    for k in v:
        assert k in model.parametersets.keys()  
    
    # Check each parameterset: TODO
    for k in v[:-1]:
        assert len(model.parametersets[k].params)==0
    assert len(model.parametersets["crop"].params)==2
        
    # Check tests: TODO
    assert len(model.tests) == 2
    v=['check wheat model', 'check wheat model2']
    for k in v:
        assert k in [ model.tests[j].name for j in range(0,2)]
    
    v1 = ['soil', 'wheat', 'wheat.cv1', 'crop']
    v2 = ['soil', 'sorghum', 'wheat.cv1', 'crop']
    
    for k in v1:
        assert k in model.tests[0].paramsets
    for k in v2:
        assert k in model.tests[1].paramsets   
        
                