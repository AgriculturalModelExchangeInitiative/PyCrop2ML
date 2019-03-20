# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:46:31 2019

@author: midingoy
"""
from pycropml.render_cyml import Model2Package 
class WriteTest(object):
    def __init__(self, models, language):
        self.models = models
        self.language= language
    
    def write(self):
        """TODO"""
        code="from math import *\n"
        for model in self.models:
            if self.language=="f90":
                #code+=WriteTest_f90(models, language, dir).write()
                pass
            if self.language=="py":
                code+= "\nfrom %s import *"%model.name
                code+= Model2Package(self.models).generate_test(model)+"\n"
        return code
            
            