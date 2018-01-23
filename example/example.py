

from path import Path
from pycropml import pparse as pp
data = Path('test/data')
xmls = data.glob('*.xml')

def example():
    fn = data.glob('Example*.xml')[0]

    parser = pp.Parser()
    model = parser.parse(fn)
    return model

