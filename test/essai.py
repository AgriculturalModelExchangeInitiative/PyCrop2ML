# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:59:40 2018

@author: midingoy
"""

from path import Path
"""import parser as xx"""

import pparse as pp


data = Path('data')
xmls = data.glob('*.xml')

def essai():
    fn = data.glob('Example*.xml')[0]

    parser = pp.Parser()
    model = parser.parse(fn)
    return model
