
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.description import Description
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract_compo
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from openalea.core.pkgmanager import PackageManager
from pycropml.transpiler.antlr_py.codeExtraction import extraction
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
    
    def getMethod(self, tree):
        self.getTypeNode(tree, "function_definition") 
        return self.getTree 
           
    def modelcomposition(self, file, models, tree):
        self.mc = extract_compo(file)
        inputlink = []
        outputlink = []
        inp = {}
        #name = re.findall(r'(def\s+.+\()', py_unit)[0].replace("def", "").replace("(", "").strip()
        funcs = self.getMethod(tree)
        algo = [f for f in funcs if f.name.startswith("model")]
        self.getTypeNode(algo[0].block,"custom_call")
        call = self.getTree
        self.mc.model = [c.function.split("model_")[-1] for c in call]
        inps, outs = [], []
        md = [n for m in self.mc.model for n in models if m.lower() == n.name.split("model_")[-1].lower()]
        self.mc.model = [n.name for n in md]
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
        return self.mc
        