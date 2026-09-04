
import os
from pathlib import Path

from pycropml.transpiler.generators.fortranGenerator import FortranGenerator, FortranCompo
from pycropml.transpiler import lib

class DssatGenerator(FortranGenerator):
    """ This class contains the specific properties of
    Apsim and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        dir_lib = Path(os.path.dirname(lib.__file__))
        FortranGenerator.__init__(self, tree, model, name)
        pkg = Path(self.model.path).name
        self.f_dest = Path(self.model.path) / "src" / "dssat" / pkg / "list_sub.f90"
        self.f_src=dir_lib / "dssat" / "list_sub.f90"

class DssatCompo(FortranCompo):
    """ This class generates Dssat module
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        FortranCompo.__init__(self,tree, model, self.name)
        dir_lib = Path(os.path.dirname(lib.__file__))
        pkg = Path(self.model.path).name
        self.f_dest = Path(self.model.path) / "src" / "dssat" / pkg / "list_sub.f90"
        self.f_src=dir_lib/"dssat"/"list_sub.f90"