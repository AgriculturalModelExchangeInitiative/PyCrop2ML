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
        self.generate_testgeneration()

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
         
        self.code = self.generate_function_signature(model_unit) 

        self.code += self.generate_function_doc(model_unit)
                
        self.code += self.generate_algorithm(model_unit)
             
        print (self.code)
        
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
    
    def generate_test(self, model_unit):
        
        m = model_unit
        name = m.description.Title
        name.strip()
        name = name.replace(' ', '_').lower()
        model_name = name
        psets = m.parametersets
        self.codetest = "'Test generation'"
        
        for v_tests in m.tests.values():
    
            test_name = v_tests[0].name  # name of tests
            test_runs = v_tests[0].run  # different run in the thest
            test_paramsets = v_tests[0].paramsets  # name of paramsets
    
        # map the paramsets
            params = {}
            for pname in test_paramsets:
                if pname not in psets:
                    print('Unknow parameter %s'%pname)
                else:
                    params.update(psets[pname].params)
    
            for each_run in test_runs :
                test_codes = []
        
            # make a function that transforms a title into a function name
                tname = test_name.replace(' ', '_')
                tname = tname.replace('-', '_')
       
               
                (run, inouts) = each_run.items()[0]
    
                ins = inouts['inputs']
                outs = inouts['outputs']
        
                code = '\n'
                test_codes.append(code)

                code = "def test_%s_run%s():"%(tname, run)
                test_codes.append(code)
                code = "    params= %s("%model_name
                test_codes.append(code)

                run_param = params.copy()
                run_param.update(ins)
        
                for k, v in run_param.iteritems():
                    code = "    %s = %s,"%(k,v)
                    test_codes.append(code)
                code = "     )"
                test_codes.append(code)
                
                code = "    params = round(params, 2)"
                test_codes.append(code)
                
                code = "    out_computed = {}".format( float(outs.values()[0]))
                
                test_codes.append(code)
        
                code = "    return {'params': params, 'out_computed': out_computed} "
      
     
                test_codes.append(code)
                
                func = 'test_%s_run%s()'%(tname, run)
                
                code = "assert  "+ func+'["params"]=='+func+'["out_computed"]'
                
                test_codes.append(code)
                
                code = '\n'.join(test_codes)
        
                print (code)    
                          
                self.codetest += code
       
        return self.codetest
    
    def generate_testgeneration(self):
        
        for model in self.models:
            self.generate_test(model)
       
        with open(self.dir/"testrun.py", "w") as python_file:
            python_file.write(self.codetest)
        return self.codetest
        


