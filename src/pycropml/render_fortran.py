"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path 
from pycropml.formater_f90 import formater  
import six
import os
from pycropml.composition import model_parser

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['FLOAT'] = 'REAL'
    DATATYPE['INT'] = 'INTEGER'
    DATATYPE['STRING'] = 'CHARACTER(65)'
    DATATYPE['DATE'] = 'CHARACTER(65)'
    DATATYPE['DOUBLE'] = 'REAL'
    DATATYPE['DOUBLELIST'] = 'REAL, ALLOCATABLE, DIMENSION(:)'
    DATATYPE['INTLIST'] = 'INTEGER, ALLOCATABLE, DIMENSION(:)'
    DATATYPE['STRINGLIST'] = 'CHARACTER(65), ALLOCATABLE, DIMENSION(:)'
    DATATYPE['INTARRAY'] = 'INTEGER, ALLOCATABLE, DIMENSION'
    DATATYPE['DOUBLEARRAY'] = 'REAL, ALLOCATABLE, DIMENSION'
    DATATYPE['STRINGARRAY'] = 'CHARACTER(65), ALLOCATABLE, DIMENSION'
    DATATYPE['BOOLEAN'] = 'LOGICAL'
    DATATYPE['DATELIST'] = 'CHARACTER(65), ALLOCATABLE, DIMENSION(:)'
 
    

    num = 0

    def __init__(self, models, directory=None, pkg_name=None):
        """TODO."""
        self.models = models
        self.directory = directory

        self.with_import = True
        if pkg_name is None:
            self.pkg_name = "CropModel"
        else: self.pkg_name = pkg_name

    def my_input(self,_input):
        name = _input.name
        _type = _input.datatype
        if _type=="DOUBLEARRAY" or _type=="INTARRAY" or _type =="STRINGARRAY": 
            size = _input.len
            return ("%s(%s) :: %s \n"%(self.DATATYPE[_type],size, name)) 
        else:
            return ("%s:: %s\n"%(self.DATATYPE[_type], name))            

    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        model_name = signature(m) 
        psets = m.parametersets
        list_var=[]
        list_inouts=[]
        for inp in m.inputs:
            list_var.append(inp.name)
            list_inouts.append(inp)
        for out in m.outputs:
            if out.name not in list_var:
                list_var.append(out.name)
                list_inouts.append(out)
        self.codetest = "PROGRAM test\n"
        self.codetest += tab+ "USE" + " %smod\n"%model_unit.name.capitalize()
        test_codes = []
        decl_ins= [ tab + self.my_input(var) for var in list_inouts]
        test_codes.append(''.join(decl_ins))
        code='' 
        for v_tests in m.testsets:
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets
        # map the paramsets
            params = {}            
            if   test_paramsets.strip()!="" and test_paramsets not in list(psets.keys()):
                print(' Unknow parameter %s'%test_paramsets)
            else:
                if   test_paramsets.strip()!="" :  params.update(psets[test_paramsets].params)                     
                for each_run in test_runs :
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    #code = "PROGRAM test_%s_%s \n"%(tname,m.name)
                    #code += tab+ "USE" + " %smod"%model_unit.name.capitalize()                    
                    #test_codes.append(code)
                    #test_codes.append('\n'.join(decl_ins))
                    code = tab +'print *, "--------test_%s_%s-------" \n'%(tname,m.name)                                         
                    run_param = params.copy()
                    run_param.update(ins)
                    for testinp in m.inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default                                      
                    for k, v in six.iteritems(run_param):
                        typ = [inp.datatype for inp in list_inouts if inp.name == k][0]
                        if typ == "STRING" or typ == "DATE": code += '    %s = "%s"\n'%(k,v.replace('"', ''))
                        elif typ != "BOOLEAN" and typ != "STRINGLIST" and typ!= "DATELIST": code += "    %s = %s\n"%(k,v)
                        elif typ == "BOOLEAN": code +="    %s = .%s.\n"%(k, v.capitalize())
                        else:
                            value = ""
                            for val in eval(v):
                                value += '    CALL Add(%s, "%s")\n'%(k,val)
                            code += value
                    test_codes.append(code)                        
                    code="    call model_{0}({1})\n".format(model_name, ', '.join(list_var))
                    for k, v in six.iteritems(outs):
                        type_o = [out.datatype for out in m.outputs if out.name==k][0]     
                        code += tab + "!%s: %s\n"%(k, v[0]) 
                        code += tab + 'print *, "%s estimated :" \n'%(k)
                        if type_o.find("LIST")!=-1:
                            code += tab +"Do i_cyml = 1, size(%s)\n"%k
                            code += 2*tab + "print *, %s(i_cyml);\n"%(k)
                            code += tab + "END DO\n" 
                        else:
                            code += tab + "print *, %s\n"%(k) 
                    test_codes.append(code)                 
                    code = ''.join(test_codes)
        self.codetest += code+'\nEND PROGRAM\n\n'
        return formater(self.codetest)
    
    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = Path(self.directory/"test_%s.f90"%signature(model))
            codetest = "!Test generation\n\n"+codetest
            with open(filename, "wb") as f90_file:
                f90_file.write(codetest.encode('utf-8'))
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
    Author: %s
    Reference: %s
    Institution: %s
    Abstract: %s
""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.Abstract)
    code = '\n'
    code += _doc
    return code


