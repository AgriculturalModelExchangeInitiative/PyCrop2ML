""" License, Header

Use pkglts

Generate notebook from code source
"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import pycropml.test_generator
from pycropml import render_fortran
import os
from . import render_python as rp
import sys

# The package used to generate Notebook
import nbformat as nbf
import six

class Model2Nb(object):
    """ Generate a Jupyter Notebook from a set of models.
    """
    """Generate a notebook for unit test.
        Args:
        - code :  from the model to code
        - dir: the directory where the code is generated.
        - name : name of the jupyter notebook
        Returns:
        - None or status
    """    
    nb = nbf.v4.new_notebook()
    def __init__(self, model, code, name, dir=None):
        self.model = model
        self.code = code
        self.name = name
        self.dir = dir

    def generate_nb(self, language, tg_rep, namep):
        
        text = u'''\
# Automatic generation of Notebook using PyCropML
    This notebook implements a crop model.'''

        _cells = self.nb['cells'] = [nbf.v4.new_markdown_cell(text)]

        var = ["Auxiliary", "Rate", "State"] 
        if language in ("cs", "java","cpp"):
            for v in var:
                fileVar = Path(os.path.join(tg_rep, "%s%s.%s"%(namep.capitalize(),v, language)))
                with open(fileVar, "r") as var_file:
                    fi = var_file.read()
                namev = "%s%s"%(namep.capitalize(),v)

                text = u"""\
### Domain Class %s"""%namev
                _cells.append(nbf.v4.new_markdown_cell(text))
                _cells.append(nbf.v4.new_code_cell(fi)) 

        text = u"""\
### Model %s"""%self.name
        _cells.append(nbf.v4.new_markdown_cell(text))
        code_tests = getattr(pycropml.test_generator,"generate_test_%s"%language)(self.model,self.dir)

        if language in ("cs", "java", "py","cpp","r"):
            _cells.append(nbf.v4.new_code_cell(self.code)) 
            for code in code_tests:
                _cells.append(nbf.v4.new_code_cell(code))

        elif language == "f90" :
            list_sub =  Path(os.path.join(tg_rep, "list_sub.f90"))
            if os.path.isfile(list_sub):
                with open(list_sub, "r") as fi:
                    sub = fi.read()                
                self.code = sub + self.code        
            for code in code_tests:
                code = self.code + code
                _cells.append(nbf.v4.new_code_cell(code)) 

        fname = Path(os.path.join(self.dir, "%s.ipynb" % self.name))
        if sys.version_info[0]>=3:
            with open(file = fname, mode ="w", encoding='utf-8') as f:
                nbf.write(self.nb, f) 
        else:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            with open(fname,  "w") as f:
                nbf.write(self.nb, f) 


