# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:28:43 2018

@author: midingoy
"""

class Test(object):
    """ Test """
    def __init__(self, name, description, uri=None):
        self.name = name
        self.description = description
        self.uri = uri
        self.paramsets = []