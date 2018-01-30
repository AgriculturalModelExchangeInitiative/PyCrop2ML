""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""
from __future__ import print_function


class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['real'] = float
    DATATYPE['int'] = int
    DATATYPE['string'] = str

    def __init__(self, models, dir=None):
        self.models = models
        self.dir = dir

    def run(self):
        self.generate_package()

    def generate_package(self):
        """ Generate a Python package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        for model in self.models:
            self.generate_component(model)

        return self.code

    def generate_component(self, model_unit):
        """ Todo
        """
        desc = model_unit.description
        inputs = model_unit.inputs
        outputs = model_unit.outputs
        algo = model_unit.algorithm

        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        name = desc.Title
        name.strip()
        name = name.replace(' ', '_').lower()

        func_name = name

        print('Function Name', name)


        code = 'def %s('%(func_name,)

        code_size = len(code)

        # Signature

        _input_names = [inp.name.lower() for inp in inputs]

        def my_input(_input):
            name = _input.name
            _type = _input.datatype
            default = _input.default
            if _type in self.DATATYPE:
                default = self.DATATYPE[_type](default)

            return '%s=%s'%(name, str(default))


        ins = [ my_input(inp) for inp in inputs]
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        print (inputs)
        code+= '):'

        print ('Signature fun: ')
        print(code)

        # documentation
        _doc = '''
    """ %s \n \n Author: %s \n Reference: %s \n Instituton: %s \n Abstract: %s

    """
'''%(desc.Title, desc.Author, desc.Reference, desc.Institution, desc.Abstract)

        code += '\n'
        code += _doc

        # Algorithm
        tab = ' '*4
        lines = [l.strip() for l in algo.split('\n') if l.strip()]
        for line in lines:
            code += tab+line+'\n'
        print ('*'*79)

        # Parse the code to see the assignee


        # Outputs
        code += tab + 'return ' + ', '.join([o.name for o in outputs]) + '\n'

        print(code)

        self.code = code

    def generate_function_signature(model_unit):
        pass

    def generate_function_doc(model_unit):
        pass

    def generate_algorithm(model_unit):
        pass
