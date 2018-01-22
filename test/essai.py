

from path import Path
import pparse as pp
data = Path('data')
xmls = data.glob('*.xml')

def essai():
    fn = data.glob('Example*.xml')[0]

    parser = pp.Parser()
    model = parser.parse(fn)
    return model
