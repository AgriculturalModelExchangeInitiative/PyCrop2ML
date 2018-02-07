""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""
from __future__ import print_function
from path import Path

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['real'] = float
    DATATYPE['int'] = int
    DATATYPE['string'] = str

    def __init__(self, models, dir=None):
        """TODO.

        """
        self.models = models
        self.dir = dir

    def run(self):
        """TODO.
        """
        self.generate_package()

    def generate_package(self):
        """Generate a Python package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        for model in self.models:
            self.generate_component(model)

        # Create a directory (mymodel)
        cwd = Path.getcwd()
        directory=cwd/'mymodel'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()
        # In the directory mymodel/model.py
        # Generate a mymodel/test.py
        with open(self.dir/"model.py", "w") as python_file:
            python_file.write(self.code)
        return self.code



    def generate_component(self, model_unit):
        """ Todo
        """
                
        code1 = self.generate_function_signature(model_unit) 

        code2 = self.generate_function_doc(model_unit)
                
        code3 = self.generate_algorithm(model_unit)

     
        code = code1+code2+code3
        
        print (code)

        self.code = code
        return self.code



    def generate_algorithm(self, model_unit):
                
        code ="\n"
        outputs = model_unit.outputs
        algo = model_unit.algorithm        
        
        tab = ' '*4
        code += tab+"try:" + "\n"
        lines = [l.strip() for l in algo.split('\n') if l.strip()]
        for line in lines:
            code += 2*tab+line+'\n'

        # Outputs
        code += 2*tab + 'return ' + ', '.join([o.name for o in outputs]) + '\n'
        
        code += tab + "except ValueError :" + '\n'
        
        code += 2*tab + 'return' + "'  No Real Solution'"

        self.code = code
        
        return self.code

    # documentation
    def generate_function_doc(self, model_unit):
        
        desc = model_unit.description
        _doc = '''
    """ %s

    Author: %s
    Reference: %s
    Instituton: %s
    Abstract: %s
    """
'''%(desc.Title, desc.Author, desc.Reference, desc.Institution, desc.Abstract)

        code = '\n'
        code += _doc
        
        return code



    def generate_function_signature(self, model_unit):
        
        desc = model_unit.description
        inputs = model_unit.inputs
        
        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        name = desc.Title
        name.strip()
        name = name.replace(' ', '_').lower()

        func_name = name
 
        code = 'def %s('%(func_name,)

        code_size = len(code)

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
        #print (inputs)
        code+= '):'
        
        return code


