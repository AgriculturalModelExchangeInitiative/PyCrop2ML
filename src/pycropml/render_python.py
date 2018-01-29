""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""

def generate_package(models, dir=None):
    """ Generate a Python package equivalent to the xml definition.

    Args:
    - models : a list of model
    - dir: the directory where the code is generated.

    Returns:
    - None or status
    """
    for model in models:
        generate_component(model)



def generate_component(model_unit):
    """ Todo
    """
    desc = model_unit.desccription
    inputs = model_unit.inputs
    outputs = model_unit.outputs
    algo = model_unit.algorithm



def generate_function_signature(model_unit):
    pass

def generate_function_doc(model_unit):
    pass

def generate_algorithm(model_unit):
    pass
