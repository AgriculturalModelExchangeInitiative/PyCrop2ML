# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:10:54 2019

@author: midingoy
"""

import os

path = os.path.dirname(os.path.realpath(__file__))

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if module_exists('pycropml'):
    import pycropml


