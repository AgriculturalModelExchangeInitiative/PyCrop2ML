# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:28:08 2018

@author: midingoy
"""

class Parameterset(object):
    """ Parameter set """
 
    def __init__(self, name, description, uri=None):
        self.name = name
        self.description = description
        self.uri = uri
        self.params = {}
        
    def _load_from_uri(self):
        pass

def parameterset(model, name, kwds):
    if not kwds:
        # look at the parameters in the parametersets and return it
        return model.parametersets.get(name)
    else:
        return Parameterset(name, **kwds)
    