

from pathlib import Path
from pycropml import pparse as pp
data = Path('test')/'data'
xmls = list(data.glob('*.xml'))

def example():
    fn = next(data.glob('Example*.xml'))

    parser = pp.Parser()
    model = parser.parse(fn)
    return model

