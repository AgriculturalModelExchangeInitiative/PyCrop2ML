"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
import os.path
from os.path import isdir
import six
from datetime import datetime
from path import Path
import numpy

try:
    from openalea.core import interface as inter
    from openalea.core import package
    from openalea.core import node
except:
    inter = None
    package = None
    node = None
    has_openalea = False

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['FLOAT'] = float
    DATATYPE['INT'] = int
    DATATYPE['STRING'] = str
    DATATYPE['DOUBLE'] = float
    DATATYPE['DOUBLELIST'] = list
    DATATYPE['INTLIST'] = list
    DATATYPE['STRINGLIST'] = list
    DATATYPE['CHARLIST'] = list
    DATATYPE['DATELIST'] = list
    DATATYPE['DOUBLEARRAY'] = numpy.array
    DATATYPE['BOOLEAN'] = bool
    DATATYPE['DATE'] = str



    num = 0

    def __init__(self, models, dir=None, pkg_name=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
        if pkg_name is None:
            self.pkg_name = "CropModel"
        else: self.pkg_name = pkg_name

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
        cwd = Path(self.dir)
        directory=cwd/'python_model'
        if isdir(directory):
            self.dir = directory
        else:
            self.dir = directory.mkdir()

        files = []
        count = 0

        for model in self.models:

            self.generate_component(model)

            #filename = self.dir/"model%s.py"%ext
            filename = self.dir/"%s.py"%signature(model)

            with open(filename, "wb") as python_file:
                python_file.write(self.code.encode('utf-8','ignore'))
                files.append(filename)

                model.module_name = str(Path(filename).namebase)

            count += 1

        return files


    def generate_wralea(self):
        """Generate wralea factories from the meta-information of the the model units."""

        '''if not has_openalea:
            return'''

        # TODO
        metainfo = {'version': '0.0.1',
                    'license': 'CECILL-C',
                    'authors': 'OpenAlea Consortium',
                    'institutes': 'INRA/CIRAD',
                    'description': 'CropML Model library.',
                    'url': 'http://pycropml.rtfd.org',
                    'icon': ''}

        _package = package.UserPackage(self.pkg_name, metainfo, self.dir)
        print(self.dir)
        for model in self.models:

            _factory = self.generate_factory(model)
            _package.add_factory(_factory)

        _package.write()


    def generate_factory(self, model):
        """Create a Node Factory from CropML model unit."""
        '''if not has_openalea:
            return'''

        inputs = []
        for input in model.inputs:
            name = input.name
            dtype = input.datatype
            interface = openalea_interface(input)
            if dtype not in ('STRING', 'BOOLEAN' ,'DATE') and 'default' in dir(input):
                value = eval(input.default)
                _in = dict(name=name, interface=interface, value=value)
            elif 'default' in dir(input):
                value=input.default.capitalize() if dtype=="BOOLEAN" else input.default
                _in = dict(name=name, interface=interface, value=value)
            elif 'default' not in dir(input):
                _in = dict(name=name, interface=interface)

            #value = eval(input.default) if dtype != 'string'else input.default

            inputs.append(_in)

        outputs = []
        for output in model.outputs:
            name = output.name
            dtype = output.datatype
            interface = openalea_interface(output)

            _out = dict(name=name, interface=interface)
            outputs.append(_out)

        _factory = node.Factory(name=model.name,
                                description=model.description.ExtendedDescription,
                                nodemodule=signature(model),
                                nodeclass=signature(model)+"_",
                                inputs=inputs,
                                outputs=outputs,
                                )
        return _factory

    def generate_component(self, model_unit):
        """ Todo
        """
        self.code= "import numpy as np \n" + "from copy import copy\n" + "from math import *\n\n"

        if model_unit.function:
            for function in model_unit.function:
                if function.language.lower() == "python":
                    module=os.path.split(function.filename)[1].split(".")[0]
                    self.code +="from %s import * \n"%module.lower()
                    break
        self.code += self.generate_function_signature(model_unit)

        self.code += self.generate_function_doc(model_unit)

        self.code += self.generate_algorithm(model_unit)

        return self.code



    def generate_algorithm(self, model_unit):

        outputs = model_unit.outputs
        tab = ' '*4
        code=""
        algo = None
        for algorithm in model_unit.algorithms:
            if ((algorithm.language == "python_ext") or
                (algorithm.language == " ") or
                (algorithm.language=="python")):
                algo = algorithm
                break

        if algo is None:
            return code

        development = algo.development
        if algo.filename==None:

            lines = [l.strip() for l in development.split('\n') if l.strip()]

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
            # Outputs
            code += tab + 'return  ' + ', '.join([o.name  for o in outputs]) + '\n'

        else:
            lines = [tab+l for l in development.split('\n') if l.split()]
            code = '\n'.join(lines)
            code += '\n'+tab + 'return  ' + ', '.join([o.name  for o in outputs]) + '\n'

        self.code = code

        return self.code

    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    """%s
    """
'''%generate_doc(model_unit)
        return doc



    def generate_function_signature(self, model_unit):

        inputs = model_unit.inputs

        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        #name = desc.Title
        func_name = signature(model_unit)

        code = 'def %s('%(func_name,)

        code_size = len(code)

        _input_names = [inp.name.lower() for inp in inputs]


        def my_input(_input):
            name = _input.name
            _type = _input.datatype
            if 'default' in dir(_input) and _input.default:
                default = _input.default

                if self.DATATYPE[_type]  == bool:
                    val = default.capitalize()
                    return "%s=%s"%(name, val)

                elif self.DATATYPE[_type] == list:
                    val = eval(default)
                    return '%s=%s'%(name, val)

                elif self.DATATYPE[_type] == str:
                    print("%s='%s'"%(name, default))
                    return "%s='%s'"%(name, default)

                elif _type in self.DATATYPE:# and _type!="Date":

                    default = self.DATATYPE[_type](default)
                ##if _type=="Date":
                    #default = datetime.strptime(default, '%d/%m/%Y')

                    return '%s=%s'%(name, default)
            else:
                return name


        ins = [ my_input(inp) for inp in inputs]
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        code+= '):'

        return code

    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit

        model_name =  signature(m)

        psets = m.parametersets
        self.codetest = ""
        for v_tests in m.testsets:

            #test_name = v_tests.name  # name of tests
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknown parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)

                for each_run in test_runs :
                    test_codes = []

                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')


                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']

                    code = '\n'
                    test_codes.append(code)

                    code = "def test_%s():"%(tname)
                    test_codes.append(code)
                    code = "    params= model_%s("%model_name
                    test_codes.append(code)

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        code = "    %s = %s,"%(k,v)
                        test_codes.append(code)
                    code = "     )"
                    test_codes.append(code)

                    for j, k in enumerate(m.outputs):
                        if  k.datatype.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY") :

                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)

                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])

                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)

                            test_codes.append(code)

                        if k.datatype.strip() in ("STRING", "BOOL", "INT", "DATE"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)

                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)

                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)


                        if k.datatype.strip() in ("DOUBLELIST", "DOUBLEARRAY"):
                            code = tab + "%s_estimated = np.around(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = np.around(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)

                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)


                        if k.datatype.strip() in ("INTLIST", "INTARRAY"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                        if k.datatype.strip() == "DOUBLE":
                            code = tab + "%s_estimated = round(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = round(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)

                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)

                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                    code = '\n'.join(test_codes)

                    self.codetest += code

        return self.codetest

    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = self.dir/"test_%s.py"%signature(model)

            codetest = "'Test generation'\n\n"+"from %s"%signature(model).capitalize() + " import *\n"+ "from math import *\n"+"import numpy as np\n\n" + codetest

            with open(filename, "wb") as python_file:
                python_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()

    return name




def generate_doc(model):
    desc = model.description

    _doc = """
    %s
    %s
    Authors: %s
    Reference: %s
    Institution: %s
    ExtendedDescription: %s
    ShortDescription: %s
""" %(desc.Title, "-Version: " + model.version +  "  -Time step: " + model.timestep, 
      desc.Authors, desc.Reference, desc.Institution, desc.ExtendedDescription, desc.ShortDescription)

    code = '\n'
    code += _doc

    return code

def openalea_interface(inout):
    if inter is None:
        return None

    dtype = inout.datatype.lower().strip()
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

    elif dtype == "boolean":
        interface = inter.IBool

    elif dtype == "date":
        interface = inter.IDateTime

    elif dtype in ("doublelist", "intlist", "stringlist","datelist", "doublearray", "intarray", "datearray"):
        interface=inter.ISequence

    return interface

