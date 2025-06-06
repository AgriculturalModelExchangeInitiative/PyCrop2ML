import json

from pycropml.modelunit import ModelUnit
from pycropml.inout import Input, Output

def test1():
    with open('data/simplace_ST.json', 'r') as f:
        sc = json.load(f)

    component = sc['function']



    return json2cml(component[0])


def json2cml(unit):
    """
    Convert a JSON object to a ModelUnit instance.
    """
    # TODO : Look at the constructor of a Model
    model_unit = ModelUnit(unit)
        
    description=unit.get('description', '')
    model_unit.add_description(description)

    inputs=[Input(input) for input in unit.get('inputs', [])]
    model_unit.inputs = inputs
    outputs=[Output(output) for output in unit.get('outputs', [])]
    model_unit.outputs = outputs


    return model_unit