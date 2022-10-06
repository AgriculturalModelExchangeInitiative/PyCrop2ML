"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import numpy 
import os.path
import six
from pycropml.nameconvention import signature1
import platform


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
        else: self.pkg_name = pkg_name

    def run(self):
        """TODO."""
        self.write_tests()

    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    %s  
'''%comment(generate_doc(model_unit))
        return doc

    def generate_test(self, model_unit, package=None):
        tab = ' '*4
        m = model_unit
        inputs = m.inputs
        outputs = m.outputs
        model_name  = signature(m)
        psets = m.parametersets
        pform = platform.system()
        list_var=[]
        init_var_in = []
        init_var_out = []
        for inp in m.inputs:
            list_var.append(inp.name)
            if hasattr(inp, "parametercategory"):
                init_var_in.append(inp.name)  
            elif inp.variablecategory=="exogenous":
                init_var_in.append(inp.name)
            elif inp.variablecategory=="state":
                init_var_out.append(inp.name)
        if pform == "linux":
            import_test = f'source("../../src/{"r"}/{package}/{signature1(m)}.r")\n'
        else:
            import_test = f'source("..\..\src\{"r"}\{package}\{signature1(m)}.r")\n'
        import_test += "library(assertthat)\n"
        codetest = [import_test]
        for v_tests in m.testsets:
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets
            # map the paramsets
            params = {}

            if test_paramsets.strip() != "" and test_paramsets not in list(psets.keys()):
                print(' Unknow parameter %s' % test_paramsets)
            else:
                if test_paramsets.strip() != "":
                    params.update(psets[test_paramsets].params)
                for each_run in test_runs :
                    test_codes = []
                    test_codes2 = []
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    code = '\n'
                    test_codes.append(code)
                    code = "test_%s<-function(){"%(tname)
                    test_codes.append(code)
                    name_categ = {}
                    

                    run_param = params.copy()
                    run_param.update(ins)
                    
                    for i, j in enumerate(m.inputs):
                        if j.name not in list(run_param.keys()):
                            run_param[j.name]=j.default 
                        name_categ[j.name] = j.variablecategory if hasattr(j, "variablecategory") else j.parametercategory        
                        
                    for k, v in six.iteritems(run_param):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        if v:
                            code = tab + "%s = %s"%(k,transf(type_v, v))
                            if m.initialization:
                                if v and name_categ[k] != "state" and m.initialization :
                                    test_codes.append(code) 
                            else:
                                test_codes.append(code)
            
                    for k, v in six.iteritems(ins):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        code = tab + "%s = %s" % (k, transf(type_v, v)) 
                        if v and name_categ[k] == "state" :
                            test_codes2.append(code) 

                    if m.initialization: 
                        code = tab + "param_init" + " = " + f"init_{signature1(m)}({','.join(init_var_in)})" 
                        test_codes.append(code)
                        for p in init_var_out:
                            code = tab + "%s = param_init$%s"%(p,p)
                            test_codes.append(code)
                        test_codes.extend(test_codes2) 

                    code = tab + "params= model_{0}({1})\n".format(model_name, ', '.join(list_var))
                    test_codes.append(code)
                        
                    for k, v in six.iteritems(outs):
                        type_v = [out.datatype for out in outputs if out.name==k][0]     
                        code = tab + "%s_estimated = params$%s"%(k,k) 
                        test_codes.append(code)
                        code = tab + "%s_computed = %s"%(k,transf(type_v,outs[k][0]))
                        test_codes.append(code)
                        if  type_v.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY", "BOOL","STRING", "DATE","INT", "INTLIST","INTARRAY") : # without precision
                            code = tab+ "assert_that(all.equal(%s_estimated, %s_computed)==TRUE)"%(k,k)   
                            test_codes.append(code)                                    
                        if type_v.strip() in ( "DOUBLE", "DOUBLELIST", "DOUBLEARRAY"): # with precision
                            code = tab+ "assert_that(all.equal(%s_estimated, %s_computed, scale=1, tol=0.%s)==TRUE)"%(k,k, outs[k][1])
                            test_codes.append(code)
                    code = '\n'.join(test_codes)
                    code += '\n}\n'
                    code += "test_%s()"%tname
                    codetest.append(code)
                    
        return codetest
    

    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
       pass

def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()
    return name


def generate_doc(model):
    desc = model.description      
    _doc = """
    %s
    Author: %s
    Reference: %s
    Institution: %s
    ExtendedDescription: %s
    ShortDescription: %s
""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.ExtendedDescription, desc.ShortDescription)
    code = '\n'
    code += _doc

    return code

def comment(line):
    list_com = ['#'+x for x in line.split('\n')]
    com = '\n'.join(list_com)
    return com

DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "string"
DATATYPE['DOUBLE'] = "double"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "string"
DATATYPE['STRINGLIST'] = "c(%s)"
DATATYPE['DOUBLELIST'] = "c(%s)"
DATATYPE['INTLIST'] = "c(%s)"
DATATYPE['DATELIST']="c(%s)"
DATATYPE['STRINGARRAY'] = "array(c(%s), dim=c(1,%s))"
DATATYPE['DOUBLEARRAY'] = "array(c(%s), dim=c(1,%s))"
DATATYPE['INTARRAY'] = "array(c(%s), dim=c(1,%s))"
DATATYPE['DATEARRAY']="array(c(%s), dim=c(1,%s))"

def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.upper()
    if type_v in ["STRING", "DATE"]:
        return ('"%s"'%elem).replace('""', '"')
    if type_v in ["DOUBLE", "INT"]:
        return str(elem)
    elif "LIST" in type_v:
        return DATATYPE[type_v.strip()]%",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),eval(elem))))
    elif "ARRAY" in type_v:
        return DATATYPE[type_v.strip()]%(",".join(list(map(transf,[type_v.split("ARRAY")[0]]*len(elem),eval(elem)))), len(eval(elem)))

        
