"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from path import Path
import numpy

from openalea.core import package
from openalea.core import node
from openalea.core import interface as inter


class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['float'] = float
    DATATYPE['int'] = int
    DATATYPE['string'] = str
    DATATYPE['Double'] = float
    DATATYPE['DOUBLEARRAY'] = numpy.array
    DATATYPE['BOOLEAN'] = bool
    DATATYPE['DATE'] = str

    num = 0

    def __init__(self, models, dir=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True

    def run(self):
        """TODO."""
        self.generate_package()
        self.generate_wralea()
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

                model.module_name = str(Path(filename).namebase)

            count += 1

        return files


    def generate_wralea(self):
        """Generate wralea factories from the meta-information of the the model units."""

        # TODO
        metainfo = {'version': '0.0.1',
                    'license': 'CECILL-C',
                    'authors': 'OpenAlea Consortium',
                    'institutes': 'INRA/CIRAD',
                    'description': 'CropML Model library.',
                    'url': 'http://pycropml.rtfd.org',
                    'icon': ''}

        _package = package.UserPackage("CropModel", metainfo, self.dir)

        for model in self.models:
            _factory = self.generate_factory(model)
            _package.add_factory(_factory)

        _package.write()


    def generate_factory(self, model):
        """Create a Node Factory from CropML model unit."""

        inputs = []
        for input in model.inputs:
            name = input.name
            dtype = input.datatype
            interface = openalea_interface(input)
            value = eval(input.default) if dtype != 'string' else input.default

            _in = dict(name=name, interface=interface, value=value)
            inputs.append(_in)

        outputs = []
        for output in model.outputs:
            name = output.name
            dtype = output.datatype
            interface = openalea_interface(output)

            _out = dict(name=name, interface=interface)
            outputs.append(_out)

        _factory = node.Factory(name=model.name,
                                description=model.description.Abstract,
                                nodemodule=model.module_name,
                                nodeclass=signature(model),
                                inputs=inputs,
                                outputs=outputs,
                                )
        return _factory

    def generate_component(self, model_unit):
        """ Todo
        """
        self.code= "import numpy as np \n" + "from copy import copy\n\n"

        self.code += self.generate_function_signature(model_unit)

        self.code += self.generate_function_doc(model_unit)

        self.code += self.generate_algorithm(model_unit)

        # print (self.code)

        return self.code



    def generate_algorithm(self, model_unit):



        #code ="\n"
        outputs = model_unit.outputs
        
        for num_algo in range(0, len(model_unit.algorithms)):
            
            if (model_unit.algorithms[num_algo].language=="python_ext"):
               
                algo = model_unit.algorithms[num_algo].development

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
        func_name = name = signature(model_unit)

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

        model_name = name = signature(m)

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


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()

    return name

def openalea_interface(inout):
    dtype = inout.datatype.lower()
    interface = None

    kwds = {}
    if inout.min:
        kwds['min'] = inout.min
    if inout.max:
        kwds['max'] = inout.max

    if dtype in ('int', 'float', 'double') :
        interface =inter.IInt if dtype == 'int' else inter.IFloat
        if ('min' in kwds) and ('max' in kwds):
            interface = interface(min=eval(inout.min), max=eval(inout.max))
        elif 'min' in kwds:
            interface = interface (min=eval(inout.min))
        elif 'max' in kwds:
            interface = interface(max=eval(inout.max))

    elif dtype == 'string':
        interface = inter.IStr

    elif 'array' in dtype:
        interface = inter.ISequence
    
    elif 'bool' in dtype:
        interface = inter.IBool


    return interface

