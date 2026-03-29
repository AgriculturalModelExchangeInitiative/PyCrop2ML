
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.description import Description
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment_ori import ExtractComments, extract, extract_compo
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from pycropml.transpiler.antlr_py.codeExtraction import extraction
import re
import copy
from pycropml.transpiler.antlr_py.api_declarations import Middleware

description_tags = ["//%%CyML Description Begin%%", "//%%CyML Description End%%"]


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
from collections import defaultdict

class CsharpExtraction(MetaExtraction):
    def __init__(self, code=""):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
        self.dclassdict = {}
        self.code = code

    def getAlgo(self, tree):
        meth = self.getmethod(tree, "CalculateModel")
        if not meth: meth = self.getmethod(tree, "Estimate")
        return meth
    
    def getInit(self, tree):
        meth = self.getmethod(tree, "Init")
        return meth
    
      
    def getStrategyVar(self):
        commentsPart = extraction(self.code, description_tags[0], description_tags[1])
        mdata = extract(commentsPart[0]+"\n\n")
        inputs = mdata.inputs
        outputs = mdata.outputs
        parameters = [p for p in inputs if p.inputtype == "parameter"]
        return (parameters, inputs,  outputs)
    
    def getFromVarInfo(self, tree1, tree, dclass):
        """get metadata from strategy classes and varinfo domain classes

        Args:
            tree1 (Node): A strategy class transformed to Node
            tree (Node): list of varinfo domain classes transformed to Nodes
            dclass (Node): list of domain classes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        """ 
        self.getTypeNode(tree, "methodDef")
        methNode = self.getTree
        descMeth = self.getAttNode(methNode,**{"name":"CalculateModel"})
        pass
    

    def getAllVar(self, source_codes):
        """get metadata from source_codes of strategy classes

        Args:
            source_codes (list): list of source codes of strategy classes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        
        Result:
            {'Q': {'Name': b'Q', 'category': 'AuxiliaryVarInfo', 'Description': b'Total moisture', 
                    'MaxValue': '100D', 'MinValue': '0D', 'DefaultValue': '50D', 
                    'Units': b'%', 'URL': b'http://', 'ValueType': 'DOUBLE'},
             'Q2': {...} ...
            }
        """
        res = {}
        for mod in source_codes:
            commentsPart = extraction(mod, description_tags[0], description_tags[1])
            mdata = extract(commentsPart[0]+"\n\n")
            for m in mdata.inputs + mdata.outputs:
                res.update({ensure_text(m.name):m})
        return res
            
 
    def description(self, tree):
        
        d = ["name", "authors", "institution", "description", "url", "reference"]
        desc = {}
        # get an instance of PublisherData
        meth = self.getmethod(tree, "SetPublisherData")
        ass = self.getAttNode(meth.block,**{"type":"assignment"})
        target = ass[0].target.name
        addMeth = self.getAttNode(meth.block, **{"type":"custom_call"})
        for v in addMeth:
            if v.args[0].value==b"Creator": desc["authors"] = v.args[1].value
            if v.args[0].value==b"Publisher": desc["institution"] = v.args[1].value
        property = self.getTypeNode(tree, "propertyDef")
        pro = self.getAttNode(self.getTree,**{"name":"Description"} )
        desc["description"] = pro[0].get[0].value.value
        pro = self.getAttNode(self.getTree,**{"name":"URL"} )
        desc["url"] = pro[0].get[0].value.value  
        desc["reference"] = pro[0].get[0].value.value    
        constr = self.getTypeNode(tree, "constructorDef")
        desc["name"] = self.getTree[0].name   
            
        return desc   
    
    def getAlgo(self, tree):
        meth = self.getmethod(tree, "CalculateModel")
        if not meth: meth = self.getmethod(tree, "Estimate")
        return meth
    
    def getInit(self, tree):
        meth = self.getmethod(tree, "Init")
        return meth
    
    def instancePastCurrent(self, stra):
        algo = self.getAlgo(stra)
        params = algo.params
        res = {}
        y = None
        lst = []
        r  = []
        for p in params:
            if isinstance(p.pseudo_type, Node) and "typename" in dir(p.pseudo_type):
                pname = str(p.name)
                type_ = p.pseudo_type.typename
                lst.append((p.pseudo_type.pseudo_type, pname))
                if type_ in res.values(): y = type_
                res.update({pname:type_})
            elif isinstance(p.pseudo_type, str):
                lst.append((p.pseudo_type, str(p.name)))
                
        orDict = defaultdict(list)
        
        # iterating over list of tuples
        for key, val in lst:
            orDict[key].append(val)
        
        self.dclassdict = dict(orDict)
        if y: 
            r = [k for k,v in res.items() if v == y]  
        else: 
            for k,v in self.dclassdict.items():
                if len(v) > 1:
                    r = v
                    break
        return r
    
    @staticmethod
    def retrieve_var_member(var):
        pass
    
    def prec_cur_states(self, tree, past_current=[]):
        inp_st = []
        if past_current:
            algo = self.getAlgo(tree)
            p = self.getStrategyVar()
            inputs = [st.name for st in p[1]]
            outputs = [st.name for st in p[2]]
            self.getTypeNode(algo.block,"member_access")
            v = self.getAttNode(self.getTree, name =past_current[1])
            precedent_v = list(set([vi.member if "." not in vi.member else vi.member.split(".")[0]  for vi in v]))
            v1 = self.getAttNode(self.getTree, name =past_current[0])
            current_v = list(set([vi.member if "." not in vi.member else vi.member.split(".")[0] for vi in v1]))
            cv=[v for v in current_v if v not in outputs ]
            for v in current_v:
                if v in inputs and v not in precedent_v:
                    cv.append(v)
            inp_st = list(set(cv))+ [t+"_t1" for t in precedent_v]
        return inp_st
    
   
    def totalvar(self, tree):
        past_cur = self.instancePastCurrent(tree)
        pc = self.prec_cur_states(tree, past_cur)
        val = self.getStrategyVar()
        p = val[1]
        p2 = val[2]
        var = []
        for inp in p:
            var.append(inp.name)
        var = var + pc 
        for out in p2:                                 
            s = out.name
            if not (s in var and s+"_t1" in var): # I suppose that we could not have a current and past state in input and current state in output
                var.append(s)
        var = var + [v.name for v in  val[0] if v]
        return var


    def model_desc(self, desc):
        name = desc["name"][:-9] if desc["name"].endswith("Component") else desc["name"]
        description = Description()
        description.Title = name+" model" 
        description.Authors = desc["authors"].decode("utf-8")
        description.Institution=desc["institution"].decode("utf-8")
        description.Reference = desc["reference"].decode("utf-8"), 
        description.ExtendedDescription = desc["description"].decode("utf-8")
        description.Url = desc["url"].decode("utf-8")
        return description

    def modelunit(self, mdata, var, all_var_pa, tvar, inps, outs):
        description = mdata.description
        self.model= ModelUnit({"name":mdata.name, "version":mdata.version, "timestep":mdata.timestep})        
        self.model.add_description(mdata.description)
        inp = var[1]
        out = var[2]
        inpname = [p.name for p in inp]
        outname = [p.name for p in out]     
        param = var[0]
        param_names = [p.name for p in param]
        inp = inp+param+out
        inputs = []
        outputs = []
        par_var = list(set(inps + outs))
        
        for v in par_var : #pc+param_names+out_names:
            vn = v[:-3] if (len(v)>3 and v not in param_names and v.endswith("_t1")) else v
            if vn in inpname: # I suppose that we could not have a current and past state in input and current state in output
                input  = getInput(mdata, vn)
                inputs.append(input)
            if vn in outname:
                output = getOutput(mdata, vn)
                outputs.append(output)
        self.model.inputs = inputs
        self.model.outputs = outputs
    """        
    def modelcomposition(self, models, tree, mcdata):
        inputlink = []
        outputlink = []
        inp = {}
        algo = self.getmethod(tree, "CalculateModel")
        self.mc = ModelComposition({"name":mcdata.name, "version":mcdata.version, "timestep":mcdata.timestep})        
        self.mc.add_description(mcdata.description)
        self.getTypeNode(algo.block,"custom_call")
        call = self.getAttNode(self.getTree, **{"function":"CalculateModel"})
        self.mc.model = [c.namespace.name[1:] for c in call]
        print("mccccccccccccccccccc")
        print(self.mc.model[0])
        inps, outs = [], []
        md = []
        for m in self.mc.model:
            for n in models:
                if m.lower() == n.name.lower():
                    md.append(n)
                    break
        self.mc.model = [n.name for n in md]
        inps = [n.name for m in md for n in m.inputs ]
        outs = [n.name for m in md for n in m.outputs ]
        m_in = set(inps) - set(outs)
        z = {}
        internallink= []
        inp_=[]
        ins_ = []
        for m in md:
            vi = list(set([n.name for n in m.inputs ]).intersection(m_in))
            vo = [n.name for n in m.outputs]
            for v in vi:
                inputlink.append({"target": m.name + "." + v, "source":v})
                inp_.append(v+"_"+m.name)
            for v in vo: 
                z.update({v:m.name})
                #inp_.append(v+"_"+m.name)

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
                        ins_.append(k+"_"+mj.name)
        for m in md:
            states_in = [n.name for n in m.inputs if "variablecategory" in dir(n) and n.variablecategory == "state"]
            states_out = [n.name for n in m.outputs if n.variablecategory == "state"]
            for s_in in states_in:
                for s_out in states_out:
                    if s_in ==  s_out and s_in + '_' + m.name not in inp_ and s_in + '_' + m.name not in ins_:
                        inputlink.append({"target": m.name + "." + v, "source":v})
                        inp_.append(s_in+"_"+m.name)
                        
                        
        self.mc.inputlink = inputlink
        self.mc.outputlink = outputlink
        self.mc.internallink = internallink
    """            


    def modelcomposition(self, models, tree, mcdata):
        inputlink = []
        outputlink = []
        inp = {}
        algo = self.getmethod(tree, "CalculateModel")
        self.mc = ModelComposition({"name":mcdata.name, "version":mcdata.version, "timestep":mcdata.timestep})        
        self.mc.add_description(mcdata.description)
        self.getTypeNode(algo.block,"custom_call")
        call = self.getAttNode(self.getTree, **{"function":"CalculateModel"})
        self.mc.model = [c.namespace.name[1:] for c in call]
        inps, outs = [], []
        md = []
        for m in self.mc.model:
            for n in models:
                if m.lower() == n.name.lower():
                    md.append(n)
                    break
        self.mc.model = [n.name for n in md]
        inps = [n.name for m in md for n in m.inputs ]
        outs = [n.name for m in md for n in m.outputs ]
        m_in = set(inps) - set(outs)
        z = {}
        internallink= []
        inp_=[]
        
        inputlink = []
        internallink = []
        outputlink = []

        producer = {}           # var -> "ModelUnit.var" (dernier producteur)
        inferred_inputs = set()

        consumed = set()
        produced = set()
        state_outputs = set()

        composite_inputs = None

        # PASS 1: InputLink + InternalLink + producer
        for m in md:
            # inputs
            for inp in m.inputs:
                v = inp.name
                consumed.add(v)

                if v in producer:
                    internallink.append({
                        "source": producer[v],      # ModelA.x
                        "target": f"{m.name}.{v}"   # ModelB.x
                    })
                else:
                    inferred_inputs.add(v)
                    inputlink.append({
                            "source": v,            # composite input
                            "target": f"{m.name}.{v}"
                        })

            # outputs
            for out in m.outputs:
                v = out.name
                produced.add(v)

                # dernier producteur (pipeline semantics)
                producer[v] = f"{m.name}.{v}"

                if getattr(out, "variablecategory", None) == "state":
                    state_outputs.add(v)

        # PASS 2: composite outputs = sinks U state_outputs (TA règle)
        sinks = produced - consumed
        composite_outputs = sinks | state_outputs

        # IMPORTANT: on garde uniquement celles qui ont un producteur (donc un ModelUnit source)
        composite_outputs = {v for v in composite_outputs if v in producer}

        # PASS 3: OutputLink (toujours depuis un ModelUnit)
        for v in composite_outputs:
            outputlink.append({
                "source": producer[v],   # "ModelUnit.var"
                "target": v
            })
        self.mc.inputlink = inputlink
        self.mc.outputlink = outputlink
        self.mc.internallink = internallink        
        """
        for m in md:
            vi = list(set([n.name for n in m.inputs ]).intersection(m_in))
            vo = [n.name for n in m.outputs]
            for v in vi:
                inputlink.append({"target": m.name + "." + v, "source":v})
                inp_.append(v+"_"+m.name)
            for v in vo: 
                z.update({v:m.name})
                #inp_.append(v+"_"+m.name)
        for m in md:
            states_in = [n.name for n in m.inputs if "variablecategory" in dir(n) and n.variablecategory == "state"]
            states_out = [n.name for n in m.outputs if n.variablecategory == "state"]
            for s_in in states_in:
                for s_out in states_out:
                    if s_in ==  s_out and s_in + '_' + m.name not in inp_:
                        print("uiiiiiiiiii", m.name, states_in, states_out)
                        inputlink.append({"target": m.name + "." + v, "source":v})
                        inp_.append(s_in+"_"+m.name)

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
        #n = self.getAttNode(self.getTree,**{'type':'declaration', 'target': Node(type = 'member_access', name= v, member = att, pseudo_type = 'VarInfo')})   
                

def ensure_text(v):
    if isinstance(v, bytes):
        return v.decode("utf-8")
    return v   

def modVal(val):
    if val=="-1D":
        return ""
    return val

def categorize(cat):
    if "state" in cat.lower(): return "state"
    if "rate" in cat.lower(): return "rate"
    if "auxiliary" in cat.lower(): return "auxiliary"
    if "exogenous" in cat.lower(): return "exogenous"
    else: return "constant" # TODOOOOOOOOOO


def getInput(mdata, name):
    for inp in mdata.inputs:
        if inp.name == name:
            return inp
    return None

def getOutput(mdata, name):
    for out in mdata.outputs:
        if out.name == name:
            return out
    return None

        
mapType = {"Integer":"INT",
           "Double":"DOUBLE",
           "String":"STRING",
           "Date":"DATE",
           "ListDouble":"DOUBLELIST",
           "ListInteger":"INTLIST",
           "ListString":"STRINGLIST",
           "ListDate":"DATELIST",
           "Boolean": "BOOLEAN",
           "ArrayDouble":"DOUBLEARRAY",
           "ArrayInt":"INTARRAY"}













'''

def listdictvalues(dictlist:list) -> list:
    """Extract the values of a list of dictionnaries

    Args:
        dictlist (list): list of dictionnaries

    Returns:
        list: list of values
    """
    return [v for d in dictlist for v in d.values()]

class CsharpExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.model = None
        self.mc = None


    def getAlgo(self, tree):
        meth = self.getmethod(tree, "CalculateModel")
        if not meth: meth = self.getmethod(tree, "Estimate")
        return meth
    
    def getInit(self, tree):
        meth = self.getmethod(tree, "Init")
        return meth
        
    
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
'''