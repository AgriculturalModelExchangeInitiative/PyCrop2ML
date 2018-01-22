# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:20:54 2018

@author: midingoy
"""

class ModelUnit(object):
    """ Formal description of a Model Unit. """

    def __init__(self):
        self.description = None
        self.inputs = []
        self.outputs = []
        self.parametersets = {}
        self.algorithm = None
        self.tests = []

    def add_description(self, description):
        """ TODO """
        self.description = description

    def __repr__(self):
        return 'ModelUnit'