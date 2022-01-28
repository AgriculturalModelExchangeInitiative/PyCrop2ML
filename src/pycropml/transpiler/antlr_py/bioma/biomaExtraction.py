
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
class BiomaExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
      
    def getStrategyVar(self, tree):
        """ This method returns a list of parameters and the value of their attributes
            and the name and category of model inputs and outputs

        Args:\n
            tree (Node): a tree where the parameters and inouts will be extracted

        Returns:\n
            list: list of parameters and the value of their attributes
            and the name of model inputs and outputs and their category
        """
        self.getTypeNode(tree, "constructorDef")
        constrNode = self.getTree
        self.getTypeNode(constrNode[0], "declaration")
        declNode = self.getTree
        vinfo, inou = [], []
        for g in declNode:
            decl = g.decl
            d = self.getAttNode(decl, **{"type":"VarInfo"})
            i = self.getAttNode(decl, **{"pseudo_type": ["List","PropertyDescription"]})
            if d: vinfo.append(d[0].name)
            if i: inou.append(i[0].name)
        pd = self.getAttNode(constrNode[0].block, **{"type":"ExprStatNode"})
        pde = [p.expr for p in pd]
        pdi = self.getAttNode(pde, **{"type":"standard_method_call", "receiver":Node(type ='local', name = inou[0], pseudo_type = ['List', 'PropertyDescription']), "message":"append"})
        pdo = self.getAttNode(pde, **{"type":"standard_method_call", "receiver":Node(type ='local', name = inou[1], pseudo_type = ['List', 'PropertyDescription']), "message":"append"})
        pdi_name = [x[0].name for x in [p.args for p in pdi if p]]
        pdo_name = [x[0].name for x in [p.args for p in pdo if p]]

        listatt = ["DefaultValue","Description","MaxValue", "MinValue", "Name", "Units", "URL", "ValueType"]
        pa =[]
        for v in vinfo:
            vi={}
            for att in listatt:
                n = self.getAttNode(constrNode[0].block,**{'type':'assignment', 'target': Node(type = 'member_access', name= v, member = att, pseudo_type = 'VarInfo')})      
                if len(n)>0:
                    if att !="ValueType" : 
                        vi[att] = n[0].value.value
                        if isinstance(vi[att] , Node): vi[att] = "%s%s"%(n[0].value.operator,vi[att].value)
                    else: 
                        vi[att] = mapType[n[0].value.args[0].value.decode("utf-8")]
            vi["category"] = "constant"     # "TODOOOOOOOO"   
            pa.append(vi) 
        def inout_att(pd_name):
            inps =[]
            for p in pd_name:
                pi={}
                n = self.getAttNode(constrNode[0].block,**{'type':'assignment', 'target': Node(type = 'member_access', name= p, member = "PropertyName", pseudo_type = 'PropertyDescription')})  
                pi["Name"] = n[0].value.value
                n = self.getAttNode(constrNode[0].block,**{'type':'assignment', 'target': Node(type = 'member_access', name= p, member = "DomainClassType", pseudo_type = 'PropertyDescription')})  
                pi["category"] = n[0].value.class_type
                inps.append (pi)
            return inps
        inp = inout_att(pdi_name)
        out = inout_att(pdo_name)
        return pa, inp, out
    
    def getFromVarInfo(self, tree1, tree):
        """get metadata from strategy classes and varinfo domain classes

        Args:
            tree1 (Node): A strategy class transformed to Node
            tree (Node): list of varinfo domain classes transformed to Nodes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        """
        self.getTypeNode(tree, "methodDef")
        methNode = self.getTree
        descMeth = self.getAttNode(methNode,**{"name":"DescribeVariables"})
        block = []
        for b in descMeth:
            if b.block:  block += b.block
        pa, inp, out = self.getStrategyVar(tree1)
        listatt = ["DefaultValue","Description","MaxValue","Name", "MinValue", "Units", "URL", "ValueType"]    
        def attV(inps):
            var_in = []
            for p in inps:
                vi = {}
                for b in block:
                    if b.target.name.endswith(p["Name"].decode("utf-8") ):
                        for att in listatt:
                            if att == b.target.member and att!="ValueType":
                                vi[att] = b.value.value
                                if b.value.type == "unary_op": vi[att] = "%s%s"%(b.value.operator, b.value.value.value)
                            if att == "ValueType" and b.target.member == "ValueType" :
                                vi[att] = mapType[b.value.args[0].value.decode('utf-8')]
                                break
                vi["category"] = p["category"]
                var_in.append(vi)
            return var_in
        var_in = attV(inp)
        var_out = attV(out)
        
        return var_in, pa, var_out
    
    def description(self, tree):
        
        d = ["name", "authors", "institution", "description", "url"]
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
        constr = self.getTypeNode(tree, "constructorDef")
        desc["name"] = self.getTree[0].name         
        return desc   
    
    def getAlgo(self, tree):
        meth = self.getmethod(tree, "CalculateModel")
        return meth
    
    def prec_cur_states(self, tree):
        algo = self.getAlgo(tree)
        p = self.getStrategyVar(tree)
        inputs = [st["Name"].decode("utf-8") for st in p[1]]
        outputs = [st["Name"].decode("utf-8") for st in p[2]]
        self.getTypeNode(algo.block,"member_access")
        v = self.getAttNode(self.getTree, name ="s1")
        precedent_v = list(set([vi.member for vi in v]))
        v1 = self.getAttNode(self.getTree, name ="s")
        current_v = list(set([vi.member for vi in v1]))
        cv=[v for v in current_v if v not in outputs ]
        for v in current_v:
            if v in inputs and v not in precedent_v:
                cv.append(v)
        inp_st = list(set(cv))+ [t+"_t1" for t in precedent_v]
        return inp_st
    
   
    def totalvar(self, tree):
        pc = self.prec_cur_states(tree)
        val = self.getStrategyVar(tree)
        p = val[1]
        p2 = val[2]
        var = []
        for inp in p:
            if not inp["category"].lower().endswith("state"):
                var.append(inp["Name"].decode("utf-8"))
        var = var + pc 
        for out in p2:
            var.append(out["Name"].decode("utf-8"))
        var = var + [v["Name"].decode("utf-8") for v in  self.getStrategyVar(tree)[0] ]
        return var


    def model_desc(self, desc):
        name = desc["name"][:-9] if desc["name"].endswith("Component") else desc["name"]
        description = Description()
        description.Title = name+" model" 
        description.Authors = desc["authors"].decode("utf-8")
        description.Institution=desc["institution"].decode("utf-8")
        description.Reference = desc["Reference"].decode("utf-8") if "Reference" in desc else "", 
        description.Abstract = desc["description"].decode("utf-8")
        description.Url = desc["url"].decode("utf-8")
        return description

    def modelunit(self, tree, tree2):
        desc = self.description(tree)
        self.model= ModelUnit({"name":desc["name"], "version":"001", "timestep":"1"})        
        description = self.model_desc(desc)
        self.model.add_description(description)
        var = self.getFromVarInfo(tree, tree2)
        inp = var[0]
        out = var[2]
        out_names = [p["Name"].decode("utf-8") for p in out]
        param = var[1]
        param_names = [p["Name"].decode("utf-8") for p in param]
        pc = self.prec_cur_states(tree)
        for k in inp:
            if not k["category"].lower().endswith("state"):
                pc.append(k["Name"].decode("utf-8"))
        inp = inp+param+out
        inputs = []
        outputs = []
        inp_par, outp=[], []
        for v in pc+param_names+out_names:
            vn = v[:-3] if (len(v)>3 and v not in param_names and v.endswith("_t1")) else v
            v_inputtype = "parameter" if v in param_names else "variable"
            v_categ = "parametercategory" if v in param_names else "variablecategory"
            description = [s["Description"].decode("utf-8") for s in inp if s["Name"].decode("utf-8") == vn][0]
            category = [categorize(s["category"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
            max = [modVal(s["MaxValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
            min = [modVal(s["MinValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
            default = [modVal(s["DefaultValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
            unit = [s["Units"].decode("utf-8") for s in inp if s["Name"].decode("utf-8") == vn][0]
            datatype = [s["ValueType"] for s in inp if s["Name"].decode("utf-8") == vn][0]
            desc_dict = {"name":v, "description":description, 
                                v_categ:category,
                                "datatype": datatype,
                                "inputtype":v_inputtype,
                                "max":max,
                                "min":min,
                                "unit":unit}
            
            if v in pc+param_names and v not in inp_par: 
                desc_dict["default"] = default
                inputs.append(Input(desc_dict))
                inp_par.append(v)
            if v in out_names and v not in outp:
                outputs.append(Output(desc_dict))
                outp.append(v)
            
        self.model.inputs = inputs
        self.model.outputs = outputs

        funcs = self.externFunction(tree)
        self.model.function = [func.name for func in funcs] if funcs else []
    
    def modelcomposition(self, models, tree):
        inputlink = []
        outputlink = []
        inp = {}
        algo = self.getmethod(tree, "EstimateOfAssociatedClasses")
        desc = self.description(tree)
        self.mc = ModelComposition({"name":desc["name"], "version":"001", "timestep":"1"})        
        description = self.model_desc(desc)
        self.mc.add_description(description)
        self.getTypeNode(algo.block,"custom_call")
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
        self.mc.internallink = internallink
            
        
        
        #n = self.getAttNode(self.getTree,**{'type':'declaration', 'target': Node(type = 'member_access', name= v, member = att, pseudo_type = 'VarInfo')})   
        
        

            

def modVal(val):
    if val=="-1D":
        return ""
    return val

def categorize(cat):
    if cat.lower().endswith("state"): return "state"
    if cat.lower().endswith("rate"): return "rate"
    if cat.lower().endswith("auxiliary"): return "auxiliary"
    if cat.lower().endswith("exogenous"): return "exogenous"
    else: return "constant" # TODOOOOOOOOOO



        
mapType = {"Integer":"INT",
           "Double":"DOUBLE",
           "String":"STRING",
           "Date":"DATE",
           "ListDouble":"DOUBLELIST",
           "ListInteger":"INTLIST",
           "ListString":"STRINGLIST",
           "ListDate":"DATELIST"}













