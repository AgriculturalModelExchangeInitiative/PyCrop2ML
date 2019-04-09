# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:39:28 2019

@author: midingoy
"""
"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
from six.moves import range


class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['INT'] = "INTEGER::"
    DATATYPE['STRING'] = "CHARACTER(65)::"
    DATATYPE['DOUBLE'] = "REAL::"
    DATATYPE['BOOLEAN'] = "LOGICAL::"
    DATATYPE['DATE'] = "CHARACTER(65)"
    DATATYPE['STRINGLIST'] = "CHARACTER(65), DIMENSION(:), ALLOCATABLE ::"
    DATATYPE['DOUBLELIST'] = "REAL, DIMENSION(:), ALLOCATABLE ::"
    DATATYPE['INTLIST'] = "INTEGER, DIMENSION(:), ALLOCATABLE ::"
    DATATYPE['DATELIST']="CHARACTER(65), DIMENSION(:), ALLOCATABLE ::"

    num = 0

    def __init__(self, models, dir=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
    
    def run(self):
        """TODO."""
        self.generate_package()
        self.write_tests()
    
    
    def generate_package(self):
        """Generate a csharp package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """

        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'csharp_model'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()

        files = []
        count = 0

        for model in self.models:
            

            self.generate_component(model)
            
            ext = '' if count == 0 else str(count)
            filename = self.dir/"%s.cs"%signature(model)

            with open(filename, "w") as python_file:
                python_file.write(self.code.encode('utf-8','ignore'))
                files.append(filename)

                model.module_name = str(Path(filename).namebase)

            count += 1

        return files


    
    def generate_component(self, model_unit):
        """ Todo
        """
        self.code = self.generate_public_class(model_unit)+'\n\n'
        self.code += self.generate_estimation(model_unit)+'\n'
        self.code +=self.generate_function_doc(model_unit)+'\n'

        self.code += self.generate_algorithm(model_unit) + '\n'

        return self.code

    def generate_function_doc(self, model_unit):

        desc = model_unit.description
        
        _doc = """/*
     %s

    Author: %s
    Reference: %s
    Instituton: %s
    Abstract: %s
    
"""%(desc.Title, desc.Author, desc.Reference, desc.Institution, desc.Abstract)+"*/"

        code = '\n'
        code += _doc

        return code

    def generate_algorithm(self, model_unit):

        outputs = model_unit.outputs
        inputs = model_unit.inputs
        sig = ""
        output_declaration = ""
        tab = ' '*4
        list_inputs=[]
        
        
        """ we  declare all outputs which are not in inputs"""
        
        for inp in inputs:
            list_inputs.append(inp.name)
        for out in outputs:
            sig+=out.name+","
            if out.name not in list_inputs:
                output_declaration += tab*2+self.DATATYPE[out.datatype]+" "+out.name+";\n"
        
        """ we select the algorithm if the language is specified or not"""
        
        for algorithm in model_unit.algorithms: 
                                
            if (algorithm.language =="C#")or(algorithm.language==" "):
                algo = algorithm
                break
        development = algo.development 
          
        if algo.filename==None:
       

            code = output_declaration
                
            lines = [l.strip() for l in development.split('\n') if l.strip()]
            for line in lines:
                if (line[len(line)-1] !=";")and(algo.language==" "): line = line+";"
                code += tab*2+line+'\n'
                
            code += tab*2+ 'return ' + 'new '+model_unit.name+"("+sig[:-1]+");\n"
                
            code+=tab+'}\n'
            code+='}\n'
                
        else: 
            #print(Path.getcwd()/algo.filename) I will improve it to import code part
            code=output_declaration+"\n"
            lines = [tab*2+l for l in development.split('\n') if l.split()]
            code += '\n'.join(lines)            
            code += '\n'+tab*2 + 'return ' + 'new '+model_unit.name+"("+sig[:-1]+");\n"
                
            code+=tab+'}\n'  
            code+='}\n'        
                                                  
 
        self.code = code

        return self.code

    # documentation
    
    def generate_public_class(self, model_unit):
        
        outputs = model_unit.outputs
        
        tab=' '*4

        code ="public class " + signature(model_unit) +'\n{\n'

        for out in outputs:
            code+=tab+"public"+" "+self.DATATYPE[out.datatype.strip()]+" "+out.name + ';\n'
        
        code+=tab+"public" +" "+model_unit.name+"("
        sig = ""
        for out in outputs:
            sig+= self.DATATYPE[out.datatype.strip()]+" "+"_"+out.name+","
            
        code+=sig[:-1]+')\n'+tab+'{\n'

        for out in outputs:
            code+=tab*2+out.name+"="+ "_"+out.name+';\n'
        
        code+=tab+'}\n}'
        
        self.code = code
        return self.code
        
        
    def generate_estimation(self, model_unit):
        outputs=model_unit.outputs
        inputs = model_unit.inputs
        
        tab=' '*4

        code ="public static class Estimation_" + signature(model_unit) +'\n{\n'
      
        
        code+=tab+"public static "+ model_unit.name+ " Calculate"+signature(model_unit)+"("
        sig = ""
                
        for inp in inputs:
            
            sig+= self.DATATYPE[inp.datatype]+" "+inp.name+","
        """            
            if "default" not in inp.__dict__:
                sig+= self.DATATYPE[inp.datatype]+" "+inp.name+"," 
        for inp in inputs:
            if "default" in inp.__dict__:
                sig+= self.DATATYPE[inp.datatype]+" "+inp.name+ ","
        """      
                    
        code+=sig[:-1]+')\n'+tab+'{\n'
        self.code = code
        
        return self.code    
        




    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit

        model_name  = signature(m)

        psets = m.parametersets
        self.codetest = ""
        for v_tests in m.testsets:
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

                    code = "test_%s<-function(){"%(tname)
                    test_codes.append(code)
                    code = "    params= %s("%model_name
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

                    self.codetest += code +'\n}'

        return self.codetest


    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            ext = '' if count == 0 else str(count)
            filename = self.dir/"test_%s.cs"%signature(model)

            codetest = "//Test generation'\n\n" + codetest

            with open(filename, "w") as csharp_file:
                csharp_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files
    
def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')

    return name   
    
def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')

    return name
def transfSDIList(type,elem): #String, Double, Int List
    return "new %s %s"%(type,str(elem).replace("[", "{").replace("]", "}"))

def transfDouble(type,elem):
    return str(elem)+'D'

def transfDate(type, elem):
    ser = elem.split("/")
    year, month, day = ser[2], ser[1], ser[0]
    return "new %s (%s, %s, %s) "%(type, year, month, day)
    
def transfString(type, elem): 
    return '"%s"'%elem

def transfDateList(type, elem):
    res=""
    for date in elem:
        print(date)
        t = transfDate("DateTime",date)
        res+=t+","
    return "new %s {%s}"%(type,res[:-1])

def transf(type, elem):
    if type=="double":
        return transfDouble(type, elem)
    elif type =="string":
        return transfString(type, elem)
    elif type=="int":
        return elem
    elif type=="List<DateTime>": 
        print(elem)
        return transfDateList(type, eval(elem))
    elif type in ("List<string>","List<double>","List<int>"):
        return transfSDIList(type,elem)
    elif type =="DateTime":
        return transfDate(type, elem)