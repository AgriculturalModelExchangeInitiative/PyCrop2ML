"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""

from __future__ import print_function
from __future__ import absolute_import
import os
from path import Path
import numpy
import six
from pycropml.composition import model_parser


class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['INT'] = "int"
    DATATYPE['STRING'] = "string"
    DATATYPE['DOUBLE'] = "double"
    DATATYPE['BOOLEAN'] = "bool"
    DATATYPE['DATE'] = "string"
    DATATYPE['STRINGLIST'] = "vector<string>"
    DATATYPE['DOUBLELIST'] = "vector<double>"
    DATATYPE['INTLIST'] = "vector<int>"
    DATATYPE['DATELIST'] = "vector<string>"
    DATATYPE['STRINGARRAY'] = "vector<string>"
    DATATYPE['DOUBLEARRAY'] = "vector<double>"
    DATATYPE['INTARRAY'] = "vector<int>"
    DATATYPE['DATEARRAY'] = "vector<DateTime>"

    num = 0

    def __init__(self, models, dir=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.import_test = ""
        self.code_test = ""
        self.run_test = ""
        # self.with_import = True

    def generate_test_import(self, model_unit, package=None):
        m = model_unit
        dir_crop2ml = Path(os.path.join(m.path, "crop2ml"))
        if package is not None:
            rel_dir_src = Path(os.path.join(m.path, "test", "cpp")).relpathto(
                Path(os.path.join(m.path, "src", "cpp", package)))
        else:
            rel_dir_src = Path(os.path.join(m.path, "test", "cpp")).relpathto(Path(os.path.join(m.path, "src", "cpp")))

        dir_compo = dir_crop2ml.glob("composition*.xml")[0]
        name_mc = model_parser(dir_compo)[0].name

        self.import_test += f'#include "{os.path.join(rel_dir_src, name_mc)}State.cpp"\n'
        self.import_test += f'#include "{os.path.join(rel_dir_src, name_mc)}Rate.cpp"\n'
        self.import_test += f'#include "{os.path.join(rel_dir_src, name_mc)}Auxiliary.cpp"\n'
        self.import_test += f'#include "{os.path.join(rel_dir_src, name_mc)}Exogenous.cpp"\n'
        self.import_test += f'#include "{os.path.join(rel_dir_src, m.name)}.cpp"\n'

        return self.import_test

    def generate_test_function(self, model_unit):
        tab = ' ' * 4
        m = model_unit
        sig = ""
        inputs = m.inputs
        outputs = m.outputs
        num = 0
        dir_crop2ml = Path(os.path.join(m.path, "crop2ml"))
        dir_compo = dir_crop2ml.glob("composition*.xml")[0]
        name_mc = model_parser(dir_compo)[0].name
        psets = m.parametersets

        def categ(k, inout):
            state = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory == "state"]
            rate = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory == "rate"]
            auxiliary = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory == "auxiliary"]
            exogenous = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory == "exogenous"]
            parameter = [m.name for m in inout if "parametercategory" in dir(m)]
            if k in state and k.endswith("_t1"):
                return "s1"
            elif k in state:
                return "s"
            elif k in rate:
                return "r"
            elif k in auxiliary:
                return "a"
            elif k in exogenous:
                return "ex"
            elif k in parameter:
                return "mod"
            else:
                raise Exception("error")

        self.code_test = "class Test\n{\n"
        self.code_test += tab + "private:\n"
        self.code_test += 2 * tab + f"{name_mc.capitalize()}State s;\n"
        self.code_test += 2 * tab + f"{name_mc.capitalize()}State s1;\n"
        self.code_test += 2 * tab + f"{name_mc.capitalize()}Rate r;\n"
        self.code_test += 2 * tab + f"{name_mc.capitalize()}Auxiliary a;\n"
        self.code_test += 2 * tab + f"{name_mc.capitalize()}Exogenous ex;\n"
        self.code_test += 2 * tab + f"{m.name.capitalize()} mod;\n"

        for inp in inputs:
            sig += tab + self.DATATYPE[inp.datatype] + " " + inp.name + ";\n"

        self.code_test += tab + "public:\n"
        for v_tests in m.testsets:
            test_name = v_tests.name  # name of tests
            self.code_test += 2 * tab + "//%s" % test_name + "\n"
            test_runs = v_tests.test
            test_paramsets = v_tests.parameterset  # name of paramsets
            # map the paramsets
            params = {}
            if test_paramsets.strip() != "" and test_paramsets not in list(psets.keys()):
                print(' Unknown parameter %s' % test_paramsets)
            else:
                if test_paramsets.strip() != "":
                    params.update(psets[test_paramsets].params)

                for each_run in test_runs:
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    self.code_test += "\n" + 2 * tab + "// %s" % tname + "\n"
                    self.code_test += 2 * tab + "void %s()" % tname + "\n" + 2 * tab + "{\n"
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    run_param = params.copy()
                    run_param.update(ins)
                    for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name] = testinp.default if testinp.datatype not in ("DATE", "STRING") \
                                else str(testinp.default)
                    for k, v in six.iteritems(run_param):
                        type_v = [inp.datatype for inp in inputs if inp.name == k][0]
                        self.code_test += 3 * tab + "this->%s.set%s(%s);\n" % (
                        categ(k, inputs), k if not k.endswith("_t1") else k[:-3], transf(type_v, v))
                    self.code_test += 3 * tab + "this->mod.Calculate_Model(s,s1, r, a, ex);\n"
                    for k, v in six.iteritems(outs):
                        type_o = [out.datatype for out in outputs if out.name == k][0]
                        self.code_test += 3 * tab + "//%s: %s;\n" % (k, v[0])
                        self.code_test += 3 * tab + f'cout << "{k} estimated :\\n";\n'
                        if type_o.find("LIST") != -1:
                            self.code_test += 3 * tab + f'for (int i=0; i<this->{categ(k, outputs)}.get{k}().size(); i++) cout << "\\t" << this->{categ(k, outputs)}.get{k}()[i] << "\\n";\n'
                        else:
                            self.code_test += 3 * tab + f'cout << "\\t" << this->{categ(k, outputs)}.get{k}() << "\\n";\n'
                    self.code_test += 2 * tab + "};\n"
                    num = num + 1
        self.code_test += "}\n"
        return self.code_test

    def generate_test_run(self, model_unit):
        self.run_test += "Test t;\n"
        for v_tests in model_unit.testsets:
            test_runs = v_tests.test
            for each_run in test_runs:
                tname = list(each_run.keys())[0].replace(' ', '_')
                tname = tname.replace('-', '_')
                self.run_test += "t.%s();\n" % tname

        return self.run_test

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test_function(model)
            filename = self.dir / "test_%s.cpp" % signature(model)
            codetest = "//Test generation'\n\n" + codetest
            with open(filename, "w") as csharp_file:
                csharp_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count += 1
        return files


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')
    return name


DATATYPE = {
    'INT': "int",
    'STRING': "string",
    'DOUBLE': "double",
    'BOOLEAN': "bool",
    'DATE': "DateTime",
    'STRINGLIST': "vector<string>",
    'DOUBLELIST': "vector<double>",
    'INTLIST': "vector<int>",
    'DATELIST': "vector<DateTime>",
    'STRINGARRAY': "vector<string>",
    'DOUBLEARRAY': "vector<double>",
    'INTARRAY': "vector<int>",
    'DATEARRAY': "vector<DateTime>"
}


def transfDouble(type_v, elem):
    return str(elem)


def transfDate(type, elem):
    ser = elem.split("/")
    if len(ser) == 3:
        year, month, day = ser[0], ser[1], ser[2]
        return "new DateTime(%s, %s, %s) " % (year, month, day)
    if len(ser) == 4:
        year, month, day, hour = ser[0], ser[1], ser[2], ser[3]
        return "new DateTime(%s, %s, %s,%s ) " % (year, month, day, hour)
    if len(ser) == 5:
        year, month, day, hour, min = ser[0], ser[1], ser[2], ser[3], ser[4]
        return "new DateTime(%s, %s, %s, %s, %s) " % (year, month, day, hour, min)
    if len(ser) == 6:
        year, month, day, hour, min, sec = ser[0], ser[1], ser[2], ser[3], ser[4], ser[5]
        return "new DateTime(%s, %s, %s,%s,%s,%s) " % (year, month, day, hour, min, sec)


def transfDateList(type, elem):
    res = ""
    for dat in eval(elem):
        t = transfDate("DateTime", dat)
        res += t + ","
    return "{%s}" % (res)


def transfString(type_v, elem):
    return ('"%s"' % elem).replace('""', '"')


def transfList(type_v, elem):
    res = ",".join(list(map(transf, [type_v.split("LIST")[0]] * len(elem), elem)))
    return "{%s}" % res


def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.lower()
    if type_v == "DOUBLE":
        return transfDouble(DATATYPE[type_v], elem)
    elif type_v in ("STRING", "DATE"):
        return transfString(DATATYPE[type_v], elem)
    elif type_v == "INT":
        return str(elem)
    elif "LIST" in type_v:
        return transfList(type_v, eval(elem))
