
from pycropml.transpiler.generators.fortranGenerator import FortranGenerator, FortranCompo
import os
from pycropml.transpiler import lib
from path import Path

class SticsGenerator(FortranGenerator):
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
        pkg = self.model.path.split(os.path.sep)[-1]
        self.f_src=dir_lib/"stics"/"list_sub.f90" 
        self.f_dest = os.path.join(self.model.path,"src","stics",pkg,"list_sub.f90") 


class SticsCompo(FortranCompo):
    """ This class generates Dssat module
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        pkg = self.model.path.split(os.path.sep)[-1] 
        dir_lib = Path(os.path.dirname(lib.__file__))
        FortranCompo.__init__(self,tree, model, self.name)
        self.f_dest = os.path.join(self.model.path,"src","stics",pkg,"list_sub.f90") 
        self.f_src=dir_lib/"stics"/"list_sub.f90"
