
# coding: utf-8
""" A simple Strategy class
 In the constructor (Parameters description, Input and Output name, category)
 In SetPublisherData method (author, institution)
 In Domain property (Composite name)
 In URL property (URL)
 In Description property (Description)

 """
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
from pycropml.function import Function
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract_compo

class DssatExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
    
    def getAlgo(self, tree):
        meth = self.getmethod(tree, "CalculateModel")
        return meth 

    def getSubroutine(self, tree):
        self.getTypeNode(tree, "function_definition") 
        return self.getTree 

    def modelunit(self, file, tree):
        self.model =  self.getFromComment(file, "!", "////", "////")
        funcs = self.externFunction(tree)
        self.model.function = funcs
        
    def externFunction(self, tree):
        algo = self.getSubroutine(tree)
        self.getTypeNode(algo[0], "custom_call")
        custom_call = self.getTree
        methNames = [c.function for c in custom_call] if custom_call else []
        return methNames
    
    def modelcomposition(self, file, models, tree):
        comments = ExtractComments(file, "!", "////", "////")
        self.mc = extract_compo(comments)
        inputlink = []
        outputlink = []
        inp = {}
        subroutines = self.getSubroutine(tree)
        algo = [f for f in subroutines if f.name.startswith("model")]
        self.getTypeNode(algo[0].block,"custom_call")
        call = self.getTree
        self.mc.model = [c.function.split("model_")[-1] for c in call]
        inps, outs = [], []
        md = [n for m in self.mc.model for n in models if m == n.name.split("model_")[-1]]
        inps = [n.name for m in md for n in m.inputs ]
        outs = [n.name for m in md for n in m.outputs ]
        m_in = set(inps) - set(outs)
        z = {}
        internallink= []
        for m in md:
            vi = list(set([n.name for n in m.inputs ]).intersection(m_in))
            vo = [n.name for n in m.outputs]
            for v in vi:
                inputlink.append({"target": m.name + "." + v, "source":v})
            for v in vo: z.update({v:m.name})

        for k, v in z.items():
            outputlink.append({"source": v + "." + k, "target":k})

        for i in range(0, len(md)-1):
            mi = md[i]
            for j in range(i+1, len(md)):
                mj = md[j]
                vi = list(set([n.name for n in mi.outputs ]).intersection(set([n.name for n in mj.inputs ])))
                if vi: 
                    for k in vi:
                        internallink.append({"source": mi.name + "." + k, "target":mj.name + "." + k})

        self.mc.inputlink = inputlink
        self.mc.outputlink = outputlink
        self.mc.internallink = internallink
   
        """
        call = self.getAttNode(self.getTree, **{"function":"Estimate"})
        self.mc.model = [c.namespace[1:] for c in call]
        inps, outs = [], []
        md = [n for m in self.mc.model for n in models if m == n.name]
        inps = [n.name for m in md for n in m.inputs ]
        outs = [n.name for m in md for n in m.outputs ]
        m_in = set(inps) - set(outs)
        z = {}
        internallink= []
        for m in md:
            vi = list(set([n.name for n in m.inputs ]).intersection(m_in))
            vo = [n.name for n in m.outputs]
            for v in vi:
                inputlink.append({"target": m.name + "." + v, "source":v})
            for v in vo: z.update({v:m.name})

        for k, v in z.items():
            outputlink.append({"source": v + "." + k, "target":k})

        for i in range(0, len(md)-1):
            mi = md[i]
            for j in range(i+1, len(md)):
                mj = md[j]
                vi = list(set([n.name for n in mi.outputs ]).intersection(set([n.name for n in mj.inputs ])))
                if vi: 
                    for k in vi:
                        internallink.append({"source": mi.name + "." + k, "target":mj.name + "." + k})

        self.mc.inputlink = inputlink
        self.mc.outputlink = outputlink
        self.mc.internallink = internallink"""
        
            
        
                    
















