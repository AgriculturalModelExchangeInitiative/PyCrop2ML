# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:46:31 2019

@author: midingoy
"""
from pycropml import render_python
from pycropml import render_fortran

class WriteTest(object):
    def __init__(self, models, language, dir):
        self.models = models
        self.language= language
        self.dir=dir

    def write(self):
        """Populate and write the test files. """
        if self.language=="f90":
            render_fortran.Model2Package(self.models, self.dir).write_tests()

        if self.language=="py":
            render_python.Model2Package(self.models, self.dir).write_tests()
