# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:24:30 2018

@author: midingoy
"""

class Description(object):
    """ Model Unit Description.

    A description is defined by:
      - Title
      - Author
      - Institution
      - Reference
      - Abstract
    """

    def __init__(self):
        self.Title = ''
        self.Author= ''
        self.Institution = ''
        self.Reference = ''
        self.Abstract = ''
