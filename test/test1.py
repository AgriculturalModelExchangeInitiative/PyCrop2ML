""" Read xml representation of a component.

"""
from __future__ import absolute_import
from __future__ import print_function
from path import Path

from pycropml import pparse


# Fix pb in local path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')

##############################################################################
# Test on Example

def example():
        
    #fn = data.glob('Example*.xml')
    #print (fn)
    
    models = pparse.model_parser(data)
    return models

