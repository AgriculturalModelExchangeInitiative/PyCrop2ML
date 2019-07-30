# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:10:54 2019

@author: midingoy
"""

import os

path = os.path.dirname(os.path.realpath(__file__))
sbmlFilePath = os.path.join(path, 'MODEL1204190002.xml')

with open(sbmlFilePath,'r') as f:
    sbmlString = f.read()

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if module_exists('pycrop2ml'):
    import pycrop2ml


from pycropml import model
