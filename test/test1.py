""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse

# Fix pb in tlocal path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def example():
        
    fn = data.glob('Example*.xml')
    
    models = pparse.model_parser(fn)
    return models
"""
def test1():
    models = example()
    assert len(models) == 1

    model = models[0]
    assert model.algorithm.development

    lines = [l for l in model.algorithm.development.split('\n') if l.strip()]
    assert len(lines) == 40

    assert len(model.inputs) == 7

    name_input = ['cSoilLayerDepth', 'cFirstDayMeanTemp', 'cAVT',
                  'cABD', 'cDampingDepth', 'iSoilSurfaceTemperature',
                  'iSoilWaterContent']

    for l, k in enumerate(name_input):
        assert k == model.inputs[l].name

    assert len(model.outputs) == 1

    # TODO Check the output
    # we can add other outputs. we have just one with our example
    name_output=['SoilTempArray[i]']


    algo_name = [l.split()[0] for l in lines]    #extract algorithm functions names
    for k in name_output:
        assert k in algo_name  # check output in algorithm functions names

    # check Description:
    # TODO
    assert model.description
    # Check ParameterSets
    assert len(model.parametersets) == 3
    v = ['cold', 'hot', 'dry']
    for k in v:
        assert k in model.parametersets.keys()

    # Check each parameterset: TODO
    for k in v:
        assert len(model.parametersets[k].params) == 5
    

    # Check tests: TODO
    assert len(model.testsets) == 3
    v = ['check soil temp1', 'check soil temp2', 'check soil temp3']
    
    v1 = ['cold_and_colder1', 'cold_and_colder2']
    v2 = ['hot_and_hotter']
    v3 = ['dry_test']
    for j, k in enumerate(v):
        assert k == model.testsets[j].name
        
    for z,k in enumerate(v1):
        assert k in model.testsets[0].test[z]
        
    for z,k in enumerate(v2):
        assert k in model.testsets[1].test[z]
    
    for z,k in enumerate(v3):
        assert k in model.testsets[2].test[z]"""
