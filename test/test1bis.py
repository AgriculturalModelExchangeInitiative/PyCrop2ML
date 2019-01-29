""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse, render_csharp

# Fix pb in tlocal path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def example():
        
    #fn = data.glob('Example*.xml')
    #print (fn)
    
    models = pparse.model_parser(data)
    return models


