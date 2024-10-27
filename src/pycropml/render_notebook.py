""" License, Header

Use pkglts

Problems:
- name of a model unit?
"""
from __future__ import print_function
from __future__ import absolute_import
import six
import os
from os.path import isdir
from path import Path

# The package used to generate Notebook
import nbformat as nbf

from . import render_python as rp



class Model2Nb(rp.Model2Package):
    """ Generate a Jupyter Notebook from a set of models.
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
        """Generate a Python package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'python_notebook'
        if isdir(directory):
            _dir = directory
        else:
            _dir = directory.mkdir()
        
        count = 0
        files=[]
        for model in self.models:

            self.generate_component(model)
        # In the directory notebook/model.py
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
            fname =_dir/"test%s.ipynb"%ext        
        
        #fname = _dir/'test.ipynb'
            with open(fname, "w") as f:
                nbf.write(nb, f)
                files.append(fname)
            count +=1
        return files


    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        #name = m.description.Title
        name = m.name
        name.strip()
        name = name.replace(' ', '_').lower()
        model_name = name
        psets = m.parametersets
        code_test=[]

        for v_tests in m.testsets:

            test_name = v_tests.name  # name of tests
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}
            
            if   test_paramsets not in list(psets.keys()):
                print('Unknow parameter %s'%test_paramsets)
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
                    
                    code = "params= %s("%model_name
                    test_codes.append(code)

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        code = "    %s = %s,"%(k,v)
                        test_codes.append(code)
                    code = "     )"
                    test_codes.append(code)

                    
                    
                    for j, k in enumerate(m.outputs):
                        if  k.datatype in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY") :
                            code = "print('%s_estimated =')"%k.name
                            test_codes.append(code) 
                            code = "print(params[%s])"%(j) if len(m.outputs)>1 else "print(params)"%k.name                           
                            test_codes.append(code)
                            code = "# %s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                                                   
                        if k.datatype in ("STRING", "BOOL", "INT", "DATE"):
                            code = "print('%s_estimated =')"%k.name
                            test_codes.append(code)
                            code = "print(params[%s])"%(j) if len(m.outputs)>1 else "print(params)"
                            test_codes.append(code)                       
                            code = "# %s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                       
                           
                        if k.datatype in ("DOUBLELIST", "DOUBLEARRAY"):
                            code = "print('%s_estimated =')"%k.name
                            test_codes.append(code) 
                            code = "print(np.around(params[%s], %s))"%(j,outs[k.name][1]) if len(m.outputs)>1 else  "print(np.around(params, %s))"%outs[k.name][1]
                            test_codes.append(code)
                            code = "# %s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
 
                           
                        if k.datatype in ("INTLIST", "INTARRAY"):
                            code = "print('%s_estimated =')"%k.name
                            test_codes.append(code)                             
                            code = "print(params[%s])"%(j) if len(m.outputs)>1 else "print(params)"
                            test_codes.append(code)
                            code = "# %s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)

                        if k.datatype == "DOUBLE":
                            code = "print('%s_estimated =')"%k.name
                            test_codes.append(code)                             
                            code = "print(round(params[%s], %s))"%(j,outs[k.name][1]) if len(m.outputs)>1 else "print(round(params, %s))"%outs[k.name][1]
                            test_codes.append(code)                         
                            code = "# %s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
 
                    code = '\n'.join(test_codes)
                    code_test.append(code)

        return code_test
