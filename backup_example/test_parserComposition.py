# Fix pb in tlocal path
from __future__ import absolute_import
from __future__ import print_function
from path import Path
from pycropml import composition

cwd = Path.getcwd()
if (cwd/'data'/'usecase').isdir():
    data = cwd/'data'/'usecase'
elif (cwd/'test'/'data'/'usecase').isdir():
    data = cwd/'test'/'data'/'usecase'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')
    
# Test on Example

def example():

    composite_file = data.glob("composition*.xml")[0]
    
    models = composition.model_parser(composite_file)
    return models    


if __name__=='__main__':
    example()


    