""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse, render_csharp

# Fix pb in tlocal path
cwd = Path.getcwd()
if (cwd/'data'/'exo').isdir():
    data = cwd/'data'/'exo'
elif (cwd/'test'/'data'/'exo').isdir():
    data = cwd/'test'/'data'/'exo'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def example():
        
    fn = data.glob('Example*.xml')
    print (fn)
    
    models = pparse.model_parser(fn)
    return models


