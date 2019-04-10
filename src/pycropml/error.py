# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:01:34 2019

@author: midingoy
"""

from __future__ import absolute_import
class Error(Exception):
    def __init__(self, message):
        self.message = message


