""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""
from __future__ import print_function
from __future__ import absolute_import
import os
from os.path import isdir
from path import Path

# The package used to generate Notebook
import nbformat as nbf

from . import render_csharp as rp
from sympy.codegen.fnodes import elemental
from six.moves import range




class Model2Nb(rp.Model2Package):
    """ Generate a Jupyter Notebook from a set of models in Csharp.
    """

    def __init__(self, models, dir=None):
        """TODO.

        """
        super(Model2Nb, self).__init__(models, dir=dir)
        self.with_import = False


    def run(self):
        """TODO.
        """
        self.generate_notebook()


    def generate_notebook(self):
        """Generate a csharp package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'csharp_notebook'
        if isdir(directory):
            _dir = directory
        else:
            _dir = directory.mkdir()
        
        count = 0
        files=[]
        for model in self.models:

            self.generate_component(model)

        # In the directory notebook_csharp/model.py
        # TODO: The code need to be generated locally in different methods.

            nb = nbf.v4.new_notebook()

            text = """\
# Automatic generation of Notebook using PyCropML (C# models)
This notebook implements a crop model."""
            _cells = nb['cells'] = [nbf.v4.new_markdown_cell(text),
                                nbf.v4.new_code_cell(self.code)]


            # Generate the tests
            text_test = """\
## Run the model with a set of parameters.
Each run will be defined in its own cell."""
            _cells.append(nbf.v4.new_markdown_cell(text_test))
        
        
            #for model in self.models:
            code_tests = self.generate_test(model)
            for code in code_tests:
                _cells.append(nbf.v4.new_code_cell(code))


            ext = '' if count == 0 else str(count)
            fname =_dir/"test_%s.ipynb"%signature(model)        
        
        #fname = _dir/'test.ipynb'
            with open(fname, "w") as f:
                nbf.write(nb, f)
                files.append(fname)
            count +=1
        return files


    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        sig = ""
        inputs = m.inputs
        outputs=m.outputs
        num=0
      
        psets = m.parametersets
        
        code_test= []
    
        
        for inp in inputs:            
            sig+= tab*3+self.DATATYPE[inp.datatype]+" "+inp.name+";\n" 
        
            
        for v_tests in m.testsets:
            
            
            test_name = v_tests.name  # name of tests
                        
            test_runs = v_tests.test  
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknow parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)
                
                for each_run in test_runs :
                                        
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    
                    des = ""                    

                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']
  
        
                    run_param = params.copy()
                    run_param.update(ins)
                    
                    for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default
                    
                    vartest = ""
                    for k, v in run_param.items():
                        type_v = [inp.datatype for inp in inputs if inp.name==k]
                        vartest+= "%s: %s,"%(k,transf(self.DATATYPE[type_v[0]], v))
                        #vartest += "%s:%s,"%(k,v)
                        
                    testcode =signature(m)+" res%s = "%num+"Estimation_%s.Calculate"%signature(m)+signature(m)+"("+vartest[:-1]+");\n"
                    
                    
                    testcode+="Console.WriteLine("
                    for l in range (0, len(outputs)):
                        des += "{"+str(l)+r"}\n"
                    des = '"'+des[:-2]+'"'+","
                    for out in outputs:
                        des+='"%s: "'%out.name+ "+"+"res%s."%num+out.name+","
                    
                    testcode+=des[:-1]+");\n\n"                    
                    
                    
                    for k, v in outs.items():
                        type_v=[out.datatype for out in outputs if out.name==k]
                        val = transfDouble(type_v,v[0]) if type_v[0]=="DOUBLE" else v[0]
                        if len(v)==2:
                            testcode+="Console.WriteLine("+'"%s Comparison: ("'%k+"+Math.Round("+val +","+v[1]+")+"+'";"' +"+Math.Round(res%s."%num+k+","+v[1]+")+"+'")  "' + "+Math.Equals(Math.Round("+val +","+v[1]+")," +"Math.Round(res%s."%num+k+","+v[1]+")));\n"
                        else: testcode+="Console.WriteLine("+'"%s Comparison: ("+'%k+ val+ '+";"' +"+res%s."%num+k+"+"+'")  "'+"+Math.Equals("+val+"," +"res%s."%num+k+"));\n"
                    
                    num = num+1                  
                    code_test.append(testcode)   
              
        return code_test

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