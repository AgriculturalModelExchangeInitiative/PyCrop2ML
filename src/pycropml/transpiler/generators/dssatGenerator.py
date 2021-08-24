
from pycropml.transpiler.generators.fortranGenerator import FortranGenerator, FortranCompo
import os
from pycropml.transpiler import lib
from path import Path

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
        self.f_src=dir_lib/"f90"/"list_sub.f90"
        FortranGenerator.__init__(self, tree, model, name)
        self.f_dest = os.path.join(self.model.path,"src","dssat","list_sub.f90") 


class DssatCompo(FortranCompo):
    """ This class generates Dssat module
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        FortranCompo.__init__(self,tree, model, self.name)