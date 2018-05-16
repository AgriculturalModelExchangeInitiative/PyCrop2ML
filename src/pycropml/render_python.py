""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""
from __future__ import print_function
from path import Path
from numpy import double
from numpy import array

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['real'] = float
    DATATYPE['int'] = int
    DATATYPE['string'] = str
    DATATYPE['Double'] = float
    DATATYPE['DOUBLEARRAY'] = array
    
    num = 0

    def __init__(self, models, dir=None):
        """TODO.

        """
        self.models = models
        self.dir = dir

        self.with_import = True

    def run(self):
        """TODO.
        """
        self.generate_package()
        self.write_tests()

    def generate_package(self):
        """Generate a Python package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        # Create a directory (mymodel)
        cwd = Path.getcwd()
        directory=cwd/'mymodel'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()
        
        files = []
        count = 0
            
           
        for model in self.models:
            
            self.generate_component(model)
            ext = '' if count == 0 else str(count)
            filename = self.dir/"model%s.py"%ext
            
            with open(filename, "w") as python_file:
                python_file.write(self.code.encode('utf-8','ignore'))
                files.append(filename)
            count +=1
        return files



    def generate_component(self, model_unit):
        """ Todo
        """
        self.code= "import numpy as np \n" + "from copy import copy\n\n"

        self.code += self.generate_function_signature(model_unit)

        self.code += self.generate_function_doc(model_unit)

        self.code += self.generate_algorithm(model_unit)

        print (self.code)

        return self.code



    def generate_algorithm(self, model_unit):
        


        #code ="\n"
        outputs = model_unit.outputs
        algo = model_unit.algorithm.development

        #code = ''
        tab = ' '*4
        #code += tab+"try:" + "\n"
        lines = [l.strip() for l in algo.split('\n') if l.strip()]
        #lines = [l for l in algo.split('\n')]
        #for line in lines:
        #   code += tab+line+'\n'
        def indentation(lines):
            code=''
            z=' '*4
            tab=' '*4
            i=1        
            for line in lines:
                pline = line
                if line =="{":
                    pline = line.strip('{')
                    i = i+1
                    tab = z*i
                if line =="}":
                    pline = line.strip('}')    
                    i = i-1
                    tab = z*i
                code+=tab+pline+"\n"
            return code
        
        code = indentation(lines)            
        
        #code = algo +'\n'
        
        # Outputs
        code += tab + 'return ' + ', '.join([o.name for o in outputs]) + '\n'

        #code += tab + "except ValueError :" + '\n'

        #code += 2*tab + 'return' + "'  No Real Solution'"

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
        #name = desc.Title
        name = model_unit.name
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

            return '%s=%s'%(name, default)


        ins = [ my_input(inp) for inp in inputs]
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        #print (inputs)
        code+= '):'

        return code
    
    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        #name = m.description.Title
        name = m.name
        name.strip()
        name = name.replace(' ', '_').lower()
        model_name = name
        psets = m.parametersets
        self.codetest = ""
        """if self.with_import:
            self.codetest += "from model import *\n"+"import numpy as np\n\n"
        """

        for v_tests in m.testsets:

            test_name = v_tests.name  # name of tests
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}
            
            if   test_paramsets not in psets.keys():
                print('Unknow parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)
                     
                for each_run in test_runs :
                    test_codes = []

                    # make a function that transforms a title into a function name
                    tname = each_run.keys()[0].replace(' ', '_')
                    tname = tname.replace('-', '_')


                    (run, inouts) = each_run.items()[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']

                    code = '\n'
                    test_codes.append(code)

                    code = "def test_%s():"%(tname)
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

                    if len(outs) <= 1:
                        decimal = outs.values()[0][1]
                        code = tab + "params = np.around(params, {})".format(decimal)
                        test_codes.append(code)

                        code = tab + "out_computed = {}".format((outs.values()[0][0]))
                        test_codes.append(code)

                        code = tab + "assert np.all(params == out_computed)"
                        test_codes.append(code)
                    else:
                        precision = outs.values()[0][1]
                        code = tab + "params = [np.around(p, {}) for p in params]".format(precision)
                        test_codes.append(code)

                        code = tab + "out_computed = ["+ ', '.join([outs[o.name][0] for o in m.outputs]) + "]"
                        test_codes.append(code)

                        code = tab + "assert np.all(params== out_computed)"
                        test_codes.append(code)


                    code = '\n'.join(test_codes)

                    print (code)

                    self.codetest += code

        return self.codetest

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            ext = '' if count == 0 else str(count)
            filename = self.dir/"testrun%s.py"%ext
            
            codetest = "'Test generation'\n\n"+"from model%s"%ext + " import *\n"+"import numpy as np\n\n" + codetest

            with open(filename, "w") as python_file:
                python_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files


