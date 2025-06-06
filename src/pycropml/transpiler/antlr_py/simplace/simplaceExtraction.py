
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
from pycropml.checking import Test, Testset
from pycropml.parameterset import Parameterset
from pycropml.function import Function
from pycropml.composition import ModelComposition
import xml.etree.ElementTree as xml
class SimplaceExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
    
    def getInouts(self, tree):
        createvarMethod = self.getmethod(tree, "createVariables")
        self.getTypeNode(createvarMethod, "custom_call")
        all_declarations = self.getAttNode(self.getTree, **{"function":"createSimVariable"})
        return all_declarations
    
    def getRealInOut(self, tree):
        initMethod = self.getmethod(tree, "init")
        self.getTypeNode(initMethod, "assignment")
        z = self.getTree
        res = {}
        for mm in z:
            if mm.value.type == "RefTypeCasting" and mm.value.receiver.type == "custom_call" and mm.value.receiver.function == "getVariable":
                val_name = mm.value.receiver.args[0].value.decode("utf-8")
                target_name = mm.target.name
                res[val_name] = target_name
        return res
    
    def var_access(self, tree):
        algo = self.getProcess(tree)
        self.getTypeNode(algo.block, "custom_call")
        node_algo = self.getAttNode(self.getTree, **{"function":"getValue"})
        init = self.getInit(tree)
        if init: 
            self.getTypeNode(init.block, "custom_call")
            node_init = self.getAttNode(self.getTree, **{"function":"getValue"})
        else: node_init = []
        var = [ n.instance.name for n in node_algo + node_init]
        return var
    
    def var_set(self, tree):
        self.getTypeNode(tree, "custom_call")
        nodes = self.getAttNode(self.getTree, **{"function":"setValue"})
        var = [ n.instance.name for n in nodes]
        return var
    
    def getProcess(self, tree):
        algo = self.getmethod(tree, "process")
        return algo
    
    def getTest(self, tree):
        test = self.getmethod(tree, "fillTestVariables")
        return test
    
    def getInOutValue(self, tree):
        test = self.getTest(tree)
        self.getTypeNode(test.block, "if_statement")
        if self.getTree and self.getTree[0].block:
            if len(self.getTree)==3:
                in_val1 = self.getAttNode(self.getTree[0].block, **{"function":"setValue"}) 
                in_val2 = self.getAttNode(self.getTree[1].block, **{"function":"setValue"}) 
                in_val = in_val1+in_val2
                out_val = self.getAttNode(self.getTree[2].block, **{"function":"setValue"}) 
            else:
                in_val = self.getAttNode(self.getTree[0].block, **{"function":"setValue"}) 
                out_val = self.getAttNode(self.getTree[1].block, **{"function":"setValue"})                 
            res_inputs = {}
            res_outputs = {}
            for in_ in in_val:
                args = in_.args
                name_ = args[1].args[0].value.decode("utf-8")
                name = name_.split(".")[-1] if "." in name_ else name_            
                value = args[0]
                if "init" in dir(value):
                    r=str([ trans_unary(m) if m.type not in ("float", "int") else eval(m.value) for m in value.init ])
                else:
                    r = trans_unary(value)
                res_inputs.update({name:r})
            for out_ in out_val:
                args = out_.args
                name_ = args[1].args[0].value.decode("utf-8")
                name = name_.split(".")[-1] if "." in name_ else name_
                value = args[0]
                if "init" in dir(value):
                    r=str([trans_unary(m) if m.type not in ("float", "int") else eval(m.value) for m in value.init ])
                else:
                    r = trans_unary(value)
                res_outputs.update({name:r})
    
            return res_inputs, res_outputs
        else: return None, None
        

    def getInit(self, tree):
        return self.getmethod(tree, "init")
    
    def getOutputs(self, tree):
        algo = self.getProcess(tree)
        self.getTypeNode(algo.block, "custom_call")
        setouts = self.getAttNode(self.getTree, **{"function":"setValue"}) + self.getAttNode(self.getTree, **{"function":"setArrayValue"})
        outs = list(map(lambda out: out.instance.name, setouts))
        return outs

    def modelunit(self, tree, auxiliary):
        desc = self.description(tree)
        self.model= ModelUnit({"name":desc["name"], "version":"001", "timestep":"1"})        
        description = self.model_desc(desc)
        self.model.add_description(description)
        all_declarations = self.getInouts(tree)
        realinout = self.getRealInOut(tree)
        outnames = self.getOutputs(tree)
        ins = self.var_access(tree)
        inputs = []
        outputs = []
        mu_ = {}
        for decl in all_declarations:
            d = decl.args 
            rname = d[0].value.decode("utf-8")
            name = realinout[rname] if (realinout and rname in realinout) else rname
            dd = d[1].value
            datatype = d[2].attribute  # Covert to Crop2ML data type
            att  = d[3].attribute
            v_inputtype = "parameter" if att == "constant" else "variable"
            v_categ = "variablecategory" if v_inputtype == "variable" else "parametercategory"
            
            #variable or parameter category
            if att == "input": 
                category = "exogenous"
            elif att == "out": category = "auxiliary"
            elif att == "privat": category = "state"
            elif att == "rate": category = "rate"
            elif att == "state": category = "state"
            else: category = att.lower()

            if auxiliary[self.model.name] and name in auxiliary[self.model.name]:
                category = "auxiliary"
            
            if name in ins and name in outnames: category = "state"
            
            unit = d[4].value
            min = trans_unary(d[5]) 
            max = trans_unary(d[6]) 
            default = trans_unary(d[7])
            if isinstance(default, Node) and d[7].type=="unary_op":
                default = str(d[7].operator)+default.value
                
            if default == "null": default = ""
            if max == "null": max = ""
            if min == "null": min = ""
    
            desc_dict = {"name":name, "description":dd.decode("utf-8"), 
                         v_categ : category,
                        "datatype": datatype,
                        "inputtype":v_inputtype,
                        "max":max,
                        "min":min,
                        "unit":unit.decode("utf-8")
                        }
            if datatype.endswith("ARRAY"): desc_dict['len']=""
            if name in ins:
                desc_dict["default"] = default # if isinstance(default, str) \
                            #else default.decode("utf-8"),
                inputs.append(Input(desc_dict))
            if name in outnames:
                mu_[name] = datatype
                outputs.append(Output(desc_dict))

        self.model.inputs = inputs
        self.model.outputs = outputs
        
        res_inputs, res_outputs = self.getInOutValue(tree)
        
        if res_inputs:
            pa = [m.name for m in self.model.parameters]
            params_val = {}
            var_val = {}
            for p, v in res_inputs.items():
                if p in pa:
                    params_val.update({p:v})
                else:
                    var_val.update({p:v})
                    
            pset = Parameterset("pset1", "first parametersets")
            pset.params = params_val
            self.model.parametersets[pset.name] = pset
            
            
            tsets = Testset("testset1", "pset1", "first testset")
            
           
            input_test = var_val
            output_test = res_outputs
            outs_ = {}
            for k, v in output_test.items():
                if mu_[k].startswith("DOUBLE") or mu_[k].startswith("INT") or mu_[k].startswith("FLOAT"):
                    outs_[k] = (v, "5")
                else: outs_[k] = v
                
            param_test = {"inputs":input_test, "outputs":outs_}

            tsets.test.append({"test1": param_test})
            
            self.model.testsets.append(tsets)
    
    def modelcomposition(self, xfile, models):
        doc = xml.parse(xfile)
        root = doc.getroot()
        compositeid = root.attrib["class"]
        id = compositeid
        compositeid = compositeid.split(".")[-1] if "." in compositeid else compositeid
        name = compositeid
        self.mc =  ModelComposition({"name":name, "version":"001", "timestep":"1"}) 
        desc = {}
        desc["name"] = name
        desc["authors"] = "Gunther Krauss"
        desc["institution"] = "INRES Pflanzenbau, Uni Bonn"
        desc["Reference"]  = "http://www.simplace.net/doc/simplace_modules/"
        desc["description"] = "as given in the documentation"
        desc["url"] = "http://www.simplace.net/doc/simplace_modules/"  
        description = self.model_desc(desc)
        self.mc.add_description(description)
        mods = []
        inputs = []
        outputs = []
        for el in list(root):
            for l in list(el):
                if l.tag=="simcomponent":
                    mu_name = l.attrib["id"]
                    mods.append(mu_name)
                    for j in list(l):
                        attr = j.attrib
                        if j.tag == "input" and "source" in attr:
                            id = attr["id"]
                            var = attr["source"].split(".")[-1]
                            mod = attr["source"].split(".")[0]
                            if mod == name or mod not in mods:
                                self.mc.inputlink.append({"target": mu_name + "." + id, "source":var})
                                inputs.append(var)
                            elif mod in mods:
                                self.mc.internallink.append({"source": mod + "." + var, "target":mu_name + "." + id})
                        elif j.tag == "output":
                            id = attr["id"]
                            var = attr["destination"].split(".")[-1]
                            mod = attr["destination"].split(".")[0]
                            self.mc.outputlink.append({"source": mu_name + "." + id, "target":var})
                            outputs.append(var)
        self.mc.model = mods
        for m in models:
            for n in m.inputs:
                if "variablecategory" in dir(n) and n.variablecategory == "state" and n.name not in inputs:
                    self.mc.inputlink.append({"target": m.name + "." + n.name, "source":n.name}) 
                    inputs.append(n.name)   
            for n in m.outputs:
                if "variablecategory" in dir(n) and n.variablecategory == "state" and n.name not in outputs:
                    self.mc.outputlink.append({"source": m.name + "." + n.name, "target":n.name})        
        return self.mc
                        
                        
    def getAuxiliary(self, xfile):
        doc = xml.parse(xfile)
        root = doc.getroot()
        compositeid = root.attrib["class"]
        name = compositeid.split(".")[-1]
        print("composite name", name)
        mods = []
        res = {}
        for el in list(root):
            for l in list(el):
                if l.tag=="simcomponent":
                    mu_name = l.attrib["id"]
                    mods.append(mu_name)
                    res[mu_name]=[]
                    for j in list(l):
                        attr = j.attrib
                        if j.tag == "input" and "source" in attr:
                            id = attr["id"]
                            mod = attr["source"].split(".")[0]
                            if mod != name:
                                res[mu_name].append(id) 
        return res         
        
        

    def model_desc(self, desc):
        name = desc["name"][:-9] if desc["name"].endswith("Component") else desc["name"]
        description = Description()
        description.Title = name+" model" 
        description.Authors = desc["authors"]
        description.Institution=desc["institution"]
        description.Reference = desc["Reference"], 
        description.ExtendedDescription = desc["description"]
        description.Url = desc["url"]
        return description

    def description(self, tree):
        
        d = ["name", "authors", "institution", "description", "url"]
        desc = {}
        constr = self.getTypeNode(tree, "classDef")
        desc["name"] = str(self.getTree[0].name) 
        desc["authors"] = "Gunther Krauss"
        desc["institution"] = "INRES Pflanzenbau, Uni Bonn"
        desc["Reference"]  = "http://www.simplace.net/doc/simplace_modules/"
        desc["description"] = "as given in the documentation"
        desc["url"] = "http://www.simplace.net/doc/simplace_modules/"     
        return desc   

               

def trans_unary(node):
    if "init" in dir(node):
        r = [trans_unary(m) for m in node.init]
        return r
    val = node.value
    if isinstance(val, Node) and node.type=="unary_op":
        val = str(node.operator)+val.value
    return val
              







