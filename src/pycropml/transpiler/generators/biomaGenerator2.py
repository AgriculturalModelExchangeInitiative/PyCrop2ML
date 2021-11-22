
from pycropml.transpiler.generators.csharpGenerator import CsharpGenerator, CsharpCompo
import os


class BiomaGenerator(CsharpGenerator):
    """ This class contains the specific properties of
    Bioma and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        CsharpGenerator.__init__(self, tree, model, name)


class BiomaCompo(CsharpCompo):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        CsharpCompo.__init__(self,tree, model, self.name)