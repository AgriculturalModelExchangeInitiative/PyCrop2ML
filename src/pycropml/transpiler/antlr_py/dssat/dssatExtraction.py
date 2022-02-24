
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
from pycropml.transpiler.antlr_py.extraction import ExtractComments

class DssatExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
    
    def getProcess(self, tree):
        self.getTypeNode(tree, "function_definition") 
        print([m.name for m in self.getTree])
        res = []
        for n in self.getTree:
            if n.comments:
                if n.comments[-1]=="!%%ModelUnit_Start%%":
                    res.append(n)
        return res
    
    def getSubroutine(self, tree, name):
        self.getTypeNode(tree, "function_definition")
        functionNode = self.getTree
        functions = self.getAttNode(functionNode,**{"name":name})
        return functions[0] if functions else []

    
    def getModule(self, tree, name):
        self.getTypeNode(tree, "module")
        moduleNode = self.getTree
        module = self.getAttNode(moduleNode,**{"name":name})
        return module[0] if module else []
    
    def getStruct(self, tree, name):
        self.getTypeNode(tree, "struct")
        structNode = self.getTree
        structs = self.getAttNode(structNode,**{"name":name})
        return structs[0] if structs else []
    
    def getDeclaration(self, tree, name):
        self.getTypeNode(tree, "declaration")
        declNodes = self.getTree
        declNode = []
        for d in declNodes:
            declNode.extend(d.decl)
        decls = self.getAttNode(declNode,**{"name":name})
        return decls[0] if decls else []

    def modelunit(self, file, tree):
        self.model =  self.getFromComment(file, "!", "////", "////")
        funcs = self.externFunction(tree)
        self.model.function = funcs
        
    def externFunction(self, algo): 
        self.getTypeNode(algo, "call_stmt")
        custom_call = self.getTree
        methNames = set({c.name for c in custom_call}) if custom_call else []
        return methNames

    def notRequiredFunc(self, tree):
        self.getTypeNode(tree, "function_definition") 
        res = []
        for n in self.getTree:
            if n.comments:
                if n.comments[-1]=='!%%NotRequired%%':
                    res.append(n)
        names = [n.name for n in res]
        return set(names)

    
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
        
            
        
                    
















