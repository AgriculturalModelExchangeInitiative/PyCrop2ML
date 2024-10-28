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

from . import render_java as rp



class Model2Nb(rp.Model2Package):
    """ Generate a Jupyter Notebook from a set of models in Java.
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
        """Generate a java package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'java_notebook'
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
# Automatic generation of Notebook using PyCropML
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
            sig+= inp.name+"," 
   
        for v_tests in m.testsets:

            test_name = v_tests.name  # name of tests
            #code =tab+"//%s"%test_name+");\n"
            
            test_runs = v_tests.test  
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknown parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)
               
                for each_run in test_runs :
       
                    des = ""
                
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    
                    code =tab+"//%s  %s"%(test_name,tname)+");\n"

                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']
                    
                    run_param = params.copy()
 

                    run_param.update(ins)
                    
                    declaration=""
                    for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default
                        declaration+= tab*2+self.DATATYPE[testinp.datatype]+" "+testinp.name + " = "+ run_param[testinp.name]+";\n"
                    """
                    vartest = ""
                    for k, v in run_param.iteritems():
                        vartest += "%s %s = %s,"%(k,v)
                    
                    """ 
                    code += declaration +"\n"    
                    code += tab*2+signature(m)+" res%s = Estimation_%s.Calculate"%(num,signature(m))+signature(m)+"("+sig[:-1]+");\n"
                    
                    
                    code+=tab*2+"System.out.println("

                    for out in outputs:
                        des+='" %s: "'%out.name+ "+"+"res%s."%num+out.name+"+"
                    
                    code+=des[:-1]+");\n\n"                    
                    
                    
                    for k, v in outs.items():
                        if len(v)==2:
                            code+=tab*2+ "System.out.println(((new BigDecimal(res%s.%s)).setScale(%s, BigDecimal.ROUND_HALF_DOWN)).equals((new BigDecimal(%s)).setScale(%s, BigDecimal.ROUND_HALF_DOWN)));\n"%(num,k,v[1],v[0],v[1])
                        else: code+=tab*2+"System.out.println((new BigDecimal(res%s.%s)).equals(new BigDecimal(%s)));\n"%(num,k,v[0])

                    num = num+1                  
                    code_test.append(code)  

        return code_test


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')

    return name
