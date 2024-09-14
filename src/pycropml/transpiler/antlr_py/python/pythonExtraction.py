
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.description import Description
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract_compo
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from openalea.core.pkgmanager import PackageManager
from pycropml.transpiler.antlr_py.codeExtraction import extraction
import re
import copy

def listdictvalues(dictlist:list) -> list:
    """Extract the values of a list of dictionnaries

    Args:
        dictlist (list): list of dictionnaries

    Returns:
        list: list of values
    """
    return [v for d in dictlist for v in d.values()]

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
    
    def orderedvar(self, mdata, tree):
        mu_inputs = [m.name for m in tree.params]
        mu_outputs = [m.name for m in tree.block[-1].value.elements]
        inps = []
        outs = []
        for n in mu_inputs:
            for inp in mdata.inputs:
                if inp.name == n:
                    inps.append(inp)
        for n in mu_outputs:
            for out in mdata.outputs:
                if out.name == n:
                    outs.append(out)
        mdata.inputs = inps
        mdata.outputs = outs
        return mdata

           
    def modelcomposition(self, file, models, tree):
        self.mc = extract_compo(file)
        self.getTypeNode(tree, "function_definition")
        mc_def_tree = self.getTree
        mc_inputs = [m.name for m in mc_def_tree[0].params]
        mc_outputs = [m.name for m in mc_def_tree[0].block[-1].value.elements]
        self.getTypeNode(mc_def_tree[0].block, "assignment")
        list_assign = self.getTree
        inputlink = []
        outputlink = []
        internallink = []
        inp = {}
        funcs = self.getMethod(tree)
        algo = [f for f in funcs if f.name.startswith("model")]
        self.getTypeNode(algo[0].block,"custom_call")
        call = self.getTree
        self.mc.model = [c.function.split("model_")[-1] for c in call]
        inps, outs = [], []
        md = [n for m in self.mc.model for n in models if m.lower() == n.name.split("model_")[-1].lower()]
        self.mc.model = [n.name for n in md]
        inps = {m.name:[n.name for n in m.inputs] for m in md}
        outs = {m.name:[n.name for n in m.outputs] for m in md}
        var_int = []
        var_out = [] # variables that are outputs of model units
        len_r = len(md) - 1 if len(md) > 1 else len(md)
        res_in = {}
        res_out = {}
        for i in range(0, len_r):
            mi = md[i]
            mi_inp = inps[mi.name]
            mi_out = outs[mi.name]
            mi_inp_p = set(mi_inp).intersection(set(mc_inputs)) # inputs of mi that are also inputs of the model composition
            mi_out_p = set(mi_out).intersection(set(mc_outputs)) # outputs of mi that are also outputs ...
            mi_inp_f = mi_inp_p - set(var_out) # inputs of mi that are not outputs of the previous model units
            if len(md) > 1:
                for j in range(i+1, len_r+1):
                    mj = md[j]
                    mj_inp = inps[mj.name]
                    zi = list(mi_out.intersection(set(mj_inp)))
                    var_int.extend(list(zi))
                    for k in zi:
                        internallink.append({"source": mi.name + "." + k, "target":mj.name + "." + k}) 
                var_out.extend(mi_out)
            mi_out_f = mi_out_p - set(var_int) # outputs of mi that are not used as intermediate variables are considered as outputs of the model composition
            res_in.update({mi.name:mi_inp_f})
            res_out.update({mi.name:mi_out_f})

        for k in mc_inputs:
            for m in md:
                if k in res_in[m.name]:
                    inputlink.append({"target": m.name + "." + k, "source":k})
        for k in mc_outputs:
            for m in md:
                if k in res_out[m.name]:
                    outputlink.append({"source": m.name + "." + k, "target":k})
   
        ilink = {}
        for a in list_assign:
            if "name" in dir(a.value) and a.value.name in mc_inputs:
                for m in md:
                    if a.target.name in inps[m.name]:
                        if a.value.name not in ilink: ilink[a.value.name] = []
                        ilink[a.value.name].append({m.name: a.target.name})

        self.mc.inputlink = inputlink
        self.mc.outputlink = outputlink
        self.mc.internallink = internallink
        return self.mc
        