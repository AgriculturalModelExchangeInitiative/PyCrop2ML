"""Add License, Header.
Use pkglts
Problems:
- name of a model unit?
"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
from datetime import datetime
import os.path
from pycropml.modelunit import ModelUnit
import six
import shutil
from . import error
import sys

DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "str"
DATATYPE['DOUBLE'] = "float"
DATATYPE['DOUBLELIST'] = "list"
DATATYPE['INTLIST'] = "list"
DATATYPE['STRINGLIST'] = "list"
DATATYPE['CHARLIST'] = "list"
DATATYPE['DATELIST'] = "datelist"
DATATYPE['DOUBLEARRAY'] = "float"
DATATYPE['INTARRAY'] = "int"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "datetime"
class Model2Package(object):
    """ TODO
    """

    num = 0

    def __init__(self, models, dir=None, pkg_name=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
        if pkg_name is None:
            self.pkg_name = "CropModel"
        else:
            self.pkg_name = pkg_name
        self.cwd = Path(self.dir)
        self.rep = os.path.abspath(os.path.dirname(self.cwd))

    def run(self):
        """TODO."""
        self.generate_package()
        #self.write_tests()

    def generate_package(self):
        """Generate a Cyml package equivalent to the xml definition.
        Args:
        - models : a list of model
        - dir: the directory where the code is generated.
        Returns:
        - None or status
        """

        # Create a directory (mymodel)
        
        directory = Path(os.path.join(self.cwd, 'pyx'))
        if directory.isdir():
            self.dir = directory
        else:
            self.dir = directory.mkdir()

        files = []
        count = 0
        for model in self.models:          
            self.generate_component(model) 
            filename = Path(os.path.join(self.dir, f"{signature(model).capitalize()}.pyx"))
            with open(filename, "wb") as cyml_file:
                # cyml_file.write(self.code.encode('utf-8','ignore'))
                cyml_file.write(self.code.encode('utf-8'))
                files.append(filename)          
                model.module_name = str(Path(filename).name)
            count += 1
        return files
        
    def generate_component(self, model_unit):
        """Todo"""
        if model_unit.modelid.split(".")[0] != "function":
            func_name = f"model_{signature(model_unit)}"
        else:
            func_name = signature(model_unit)
        types = [inp.datatype for inp in model_unit.inputs] + [out.datatype for out in model_unit.outputs]
        self.code = "import numpy\n"
        self.code += "from math import *\n"
        if "DATE" in types or "DATELIST" in types:
            self.code += "from datetime import datetime\n"
        self.code += "\n"
        if model_unit.initialization is not None and len(model_unit.initialization) != 0:
            self.code += self.initialization(model_unit) + "\n"
            
        self.code += self.generate_function_signature(func_name, model_unit.inputs) + "\n"
        self.code += self.generate_function_doc(model_unit) + "\n"
        if sys.version_info[0] >= 3:
            self.code += self.generate_algorithm(model_unit) + "\n"
        else:
            self.code += self.generate_algorithm(model_unit).decode("utf-8") + "\n"

        if model_unit.function:
            for function in model_unit.function:
                if function.language in ("Cyml", "cyml"):
                    filefunc = Path(os.path.join(model_unit.path, "crop2ml", function.filename))
                    with open(filefunc.encode('utf-8'), 'r') as f:
                        source = f.read()
                        self.code += source 
                        self.code += "\n\n\n"
     
        return self.code

    def generate_algorithm(self, model_unit):
        outputs = model_unit.outputs
        inputs = model_unit.inputs
        tab = ' '*4
        list_inputs = []
        algo = ""
        
        """ we  declare all outputs which are not in inputs"""
        output_declaration = ""
        for inp in inputs:
            list_inputs.append(inp.name)
        for out in outputs:
            if out.name not in list_inputs:
                output_declaration += tab+"cdef "+my_input(out, True)+"\n"

        for algorithm in model_unit.algorithms:                                  
            if (algorithm.language == "Cyml") or (algorithm.language == "cyml"):
                algo = algorithm
                break
        
        if algo:
            development = algo.development           
            lines = [tab+l for l in development.split('\n') if l.split()]
            code = output_declaration
            code += '\n'.join(lines)
            code += '\n'+tab + 'return  ' + ', '.join([o.name for o in outputs]) + '\n\n\n'
            self.code = code
        else:
            raise error.Error("algorithm is not defined in model unit")
        return self.code

    def initialization(self, model_unit):
        outputs = model_unit.outputs
        inputs = model_unit.inputs
        tab = ' '*4
        list_inputs = []
        outs = []     
        
        """ we  declare all outputs which are not in inputs"""
        output_declaration = ""
        other = ""
        z = []
        for inp in inputs:
            if "variablecategory" in dir(inp) and inp.variablecategory == "state":
                list_inputs.append(inp.name)
                """if inp.datatype in ("DOUBLE", "FLOAT"):
                    inp.default = "0.0"
                if inp.datatype == "INT":
                    inp.default = "0" """
                output_declaration += tab+"cdef "+my_input(inp, defa=True)+"\n"
                outs.append(inp)
                if not inp.default:
                    other += tab + inp.name + " = " + default_value(inp)+"\n"
        
        code = ""
        if model_unit.initialization:
            file_init = model_unit.initialization[0].filename
            path_init = Path(os.path.join(model_unit.path, "crop2ml", file_init))
            par = []
            for inp in inputs:
                if "parametercategory" in dir(inp):
                    par.append(inp)  
                elif inp.variablecategory == "exogenous":
                    par.append(inp)
                        
            with open(path_init, 'r') as f:
                code_init = f.read() 
            if code_init is not None:
                lines = [tab+l for l in code_init.split('\n') if l.split()]
                code += self.generate_function_signature(f"init_{signature(model_unit)}", par) + '\n'
                code += output_declaration
                code += other
                code += '\n'.join(lines)
                code += '\n'+tab + 'return  ' + ', '.join([o.name for o in outs]) + '\n'
        return code

    # documentation
    def generate_function_doc(self, model_unit):
        return f'''\
    """
{generate_doc(model_unit)}
    """
'''

    def generate_function_signature(self, func_name,inputs):
        #inputs = model_unit.inputs
        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        #name = desc.Title
        code = f'def {func_name}('
        code_size = len(code)
        #_input_names = [inp.name.lower() for inp in inputs]
        ins = [my_input(inp, False) for inp in inputs]
        separator = ',\n' + code_size*' '
        code += separator.join(ins)
        code += '):'
        return code


    def generate_test(self, model_unit):
        tab = ' '*4
        m = model_unit

        model_name = signature(m)

        psets = m.parametersets
        self.codetest = ""
        for v_tests in m.testsets:

            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if test_paramsets not in list(psets.keys()):
                print(f'Unknown parameter {test_paramsets}')
            else:
                params.update(psets[test_paramsets].params)

                for each_run in test_runs:
                    test_codes = []

                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')

                    run, inouts = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    #print(outs.keys())

                    code = '\n'
                    test_codes.append(code)

                    code = f"def test_{tname}():"
                    test_codes.append(code)
                    code = f"    params = {model_name}("
                    test_codes.append(code)

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        code = f"    {k} = {v},"
                        test_codes.append(code)
                    code = "     )"
                    test_codes.append(code)
                    outnames = list(outs.keys())
                    for j, k in enumerate(m.outputs):
                        if k.name in outnames:
                            if k.datatype.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY"):
                            
                                code = tab + f"{k.name}_estimated = params[{j}]" if len(m.outputs) > 1 \
                                    else tab + f"{k.name}_estimated = params"
                                
                                test_codes.append(code)
                                code = tab + f"{k.name}_computed = {outs[k.name][0]}"
                            
                                test_codes.append(code)
                                code = tab + f"assert np.all({k.name}_estimated == {k.name}_computed)"
                            
                                test_codes.append(code)
                                                    
                            if k.datatype.strip() in ("STRING", "BOOL", "INT", "DATE"):
                                code = tab + f"{k.name}_estimated = params[{j}]" if len(m.outputs) > 1 \
                                    else tab + f"%{k.name}estimated = params"
                                test_codes.append(code)
                        
                                code = tab + f"{k.name}_computed = {outs[k.name][0]}"
                                test_codes.append(code)
                        
                                code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                                test_codes.append(code)

                            if k.datatype.strip() in ("DOUBLELIST", "DOUBLEARRAY"):
                                code = tab + f"{k.name}_estimated = np.around(params[{j}], {outs[k.name][1]})"\
                                    if len(m.outputs) > 1 \
                                    else tab + f"{k.name}_estimated = np.around(params, {outs[k.name][1]})"
                                test_codes.append(code)
                                code = tab + f"{k.name}_computed = {outs[k.name][0]}"
                                test_codes.append(code)
                        
                                code = tab + f"assert np.all({k.name}_estimated == {k.name}_computed)"
                                test_codes.append(code)

                            if k.datatype.strip() in ("INTLIST", "INTARRAY"):
                                code = tab + f"{k.name}_estimated = params[{j}]" if len(m.outputs) > 1 \
                                    else tab + f"{k.name}_estimated = params"
                                test_codes.append(code)
                                code = tab + f"{k.name}_computed = {outs[k.name][0]}"
                                test_codes.append(code)
                                code = tab + f"assert np.all({k.name}_estimated == {k.name}_computed)"
                                test_codes.append(code)

                            if k.datatype.strip() == "DOUBLE":
                                code = tab + f"{k.name}_estimated = round(params[{j}], {outs[k.name][1]})"\
                                    if len(m.outputs) > 1 \
                                    else tab + f"{k.name}_estimated = round(params, {outs[k.name][1]})"
                                test_codes.append(code)
                            
                                code = tab + f"{k.name}_computed = {outs[k.name][0]}"
                                test_codes.append(code)
                            
                                code = tab + f"assert ({k.name}_estimated == {k.name}_computed)"
                                test_codes.append(code)

                    code = '\n'.join(test_codes)
                    self.codetest += code

        return self.codetest
    
    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
        """
        TODO: Manage several models rather than just one.
        """
        self.rep = Path(os.path.join(self.rep, 'test', 'pyx'))
        if not self.rep.isdir():
            self.rep.mkdir()
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = Path(os.path.join(self.rep, f"test_{signature(model).capitalize()}.pyx"))
            codetest = f"""\
#'Test generation'

from {signature(model)} import *
from math import *
import numpy
 
 {codetest}"""
            with open(filename, "wb") as cyml_file:
                cyml_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count += 1
        return files


def signature(model: ModelUnit):
    """_summary_

    Args:
        model (ModelUnit): A Python object of a Crop2ML model Unit

    Returns:
        str: name
    """
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()

    return name


def generate_doc(model: ModelUnit):
    desc = model.description
    return f"""\
    {desc.Title}
    Author: {desc.Authors}
    Reference: {desc.Reference}
    Institution: {desc.Institution}
    ExtendedDescription: {desc.ExtendedDescription}
    ShortDescription: {desc.ShortDescription}"""

def transfDate(type, elem):
    ser = elem.split("/")
    if len(ser) == 3:
        year, month, day = ser[0], ser[1], ser[2]
        return f"datetime({year}, {month}, {day}) "
    if len(ser) == 4:
        year, month, day, hour= ser[0], ser[1], ser[2], ser[3]
        return f"datetime({year}, {month}, {day}, {hour}) "
    if len(ser) == 5:
        year, month, day, hour, min = ser[0], ser[1], ser[2],ser[3], ser[4]
        return f"datetime({year}, {month}, {day}, {hour}, {min}) "
    if len(ser) == 6:
        year, month, day, hour, min, sec = ser[0], ser[1], ser[2], ser[3], ser[4], ser[5]
        return f"datetime({year}, {month}, {day}, {hour}, {min}, {sec}) "


def transfDateList(type, elem):
    res = ""
    for dat in eval(elem):
        t = transfDate("DateTime", dat)
        res += t + ","
    return f"[{res}]"


def transBool(type, elem):
    return elem.lower().capitalize()


def transf(type_, elem):
    if type_ == "DATE":
        return transfDate(type_, elem)
    elif type_ == "DATELIST":
        return transfDateList(type_, elem)
    elif type_ == "BOOLEAN":
        return transBool(type_, elem)
    else:
        return elem


def my_input(_input, defa=False):
    name = _input.name
    _type = _input.datatype
        
    if 'default' in dir(_input) and defa:
        if _input.default:
            default = _input.default              
            if DATATYPE[_type] == "bool":
                val = default.capitalize()
                return f"bool {name} = {val.lower().capitalize()}"
            elif DATATYPE[_type] == "list":
                val = eval(default)
                return f'list {name} = {val}'
            elif DATATYPE[_type] == "datelist":
                return f'list {name} = {transfDateList(type, default)}'
            elif DATATYPE[_type] == "str":                
                return f"str {name}='{default}'"
            elif DATATYPE[_type] == "datetime":                   
                return f"datetime {name} = {transfDate(_type,default)}"
            elif _type in DATATYPE: 
                if "ARRAY" in _type : return  f'{DATATYPE[_type]}array {name}'
                default = float(default) if DATATYPE[_type] == "float" else int(default)
                return f'{DATATYPE[_type]} {name} = {default}'
        else:
            if _type == "DOUBLEARRAY" or _type == "INTARRAY":
                length = _input.len
                    #print("%s %s[%s]"%(DATATYPE[_type], name,len))
                return (f"{DATATYPE[_type]} {name}[{length}]")
            else:
                return (f"{DATATYPE2[_type]} {name}")
    else:
            if _type == "DOUBLEARRAY" or _type == "INTARRAY":
                length = _input.len
                    #print("%s %s[%s]"%(DATATYPE[_type], name,len))
                return (f"{DATATYPE[_type]} {name}[{length}]")
            else:
                return (f"{DATATYPE2[_type]} {name}")

def default_value(inp):
    type_ = inp.datatype
    if type_.endswith("LIST"): return "[]"
    elif type_ == "INT": return "0"
    elif type_ =="DOUBLE": return "0.0"
    elif type_ == "DATE": return "None"
    elif type_.endswith("ARRAY") and not inp.len: return "None"
    elif type_.endswith("ARRAY") and inp.len:
        if type_=="INTARRAY": return f"array('i', [0]*{inp.len})"
        if type_=="DOUBLEARRAY": return f"array('f', [0.0]*{inp.len})"

DATATYPE2 = {}
DATATYPE2['INT'] = "int"
DATATYPE2['STRING'] = "str"
DATATYPE2['DOUBLE'] = "float"
DATATYPE2['DOUBLELIST'] = "floatlist"
DATATYPE2['INTLIST'] = "intlist"
DATATYPE2['STRINGLIST'] = "stringlist"
DATATYPE2['CHARLIST'] = "stringlist"
DATATYPE2['DATELIST'] = "datelist"
DATATYPE2['DOUBLEARRAY'] = "floatarray"
DATATYPE2['INTARRAY'] = "intarray"
DATATYPE2['BOOLEAN'] = "bool"
DATATYPE2['DATE'] = "datetime"