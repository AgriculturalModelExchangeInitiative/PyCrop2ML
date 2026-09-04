
from __future__ import absolute_import
from __future__ import print_function
from pathlib import Path
from pycropml.transpiler.antlr_py.dssat.run2 import process_dssat

""" Read BioMA component and extract metadata

"""

cwd = Path(__file__).parent
data = cwd/'examples'/'DssatComponent'/'phenology'

output = cwd/'examples'/'DssatComponent'/'phenology'

process_dssat(data, output)