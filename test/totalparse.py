from pycropml import pparse
from test1 import example, cwd


if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')


def totalexample():   
    models = example()
    m, = models

    pparse.parse_parameter_uri(data, m)
    pparse.parse_tests_uri(data, m)
    
    return models


