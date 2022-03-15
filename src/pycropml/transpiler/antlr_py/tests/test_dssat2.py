
from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.dssat.run2 import process_dssat

""" Read BioMA component and extract metadata

"""

cwd = Path(__file__).dirname()
data = cwd/'examples'/'DssatComponent'/'phenology'

output = cwd/'examples'/'DssatComponent'/'phenology'

process_dssat(data, output)