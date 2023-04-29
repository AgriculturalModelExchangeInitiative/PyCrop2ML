
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.description import Description
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract_compo
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from openalea.core.pkgmanager import PackageManager
import re


class PythonExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.model = None
        self.mc = None
    
    def retrievePackage(self, wralea_dir):
         self.pm.init(wralea_dir)
         pkg = self.pm.get_composite_nodes()[0]  
         return pkg

    def modelunit(self, file, tree):
        pass
           
    def modelcomposition(self, wf, mu_names):
        pass
        