

from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
from pycropml.function import Function
from pycropml.composition import ModelComposition
from collections import defaultdict

class ApsimExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
        self.dclassdict = {}

    def getAllVar(self, tree):
        """get metadata from interfaces

        Args:
            tree (Node): list of interfaces transformed to Nodes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        
        Result:
            {'Q': {'Name': b'Q', 'category': 'AuxiliaryVarInfo', 'Description': b'Total moisture', 
                    'MaxValue': '100D', 'MinValue': '0D', 'DefaultValue': '50D', 
                    'Units': b'%', 'URL': b'http://', 'ValueType': 'DOUBLE'},
             'Q2': {...} ...
            }
        """

        
        listatt = ["DefaultValue","Description","MaxValue","Name", "MinValue", "Units", "URL", "ValueType"]            
        prop ={}
        var = {}
        for tr in tree:
            self.getTypeNode(tr, "propertyDef")
            prop.update({m.name :m.pseudo_type for m in self.getTree if "name" in dir(m)})
        return prop
 
    def getUtilities(self, tree):
        pass
    
    def getUtilitiesFunctions(self, tree):
        pass
    
    def getInputs(self, tree):
        pass
    
    def getOutputs(self, tree):
        pass
    
    def getInit(self, tree):
        """Get initialization method from the tree

        Args:
            tree (Node): ASG of the component

        Returns:
            Node: ASG of the initialization method
        """
        meth = self.getmethod(tree, "OnStartOfSimulation")
        return meth
    
    def getAlgo(self, tree):
        """Get algorithm method from the tree

        Args:
            tree (Node): ASG of the component

        Returns:
            Node: ASG of the algorithm method
        """
        meth = self.getmethod(tree, "OnProcess")
        if not meth: meth = self.getmethod(tree, "Estimate")
        return meth
    