# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:25:51 2018

@author: midingoy
"""

class InputOutput(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in kwds.iteritems():
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)

