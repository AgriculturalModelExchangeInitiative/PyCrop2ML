
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

class BiomaExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.inputs = []
        self.outputs = []
        self.model = None
        self.mc = None
        self.dclassdict = {}
      
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
    
    def getFromVarInfo(self, tree1, tree, dclass):
        """get metadata from strategy classes and varinfo domain classes

        Args:
            tree1 (Node): A strategy class transformed to Node
            tree (Node): list of varinfo domain classes transformed to Nodes
            dclass (Node): list of domain classes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        """
        self.getTypeNode(tree, "propertyDef")
        prop =  {m.name :m.get[0].value.name for m in self.getTree if "name" in dir(m.get[0].value)}
        
        self.getTypeNode(dclass, "propertyDef")
        prop2 =  {m.get[0].value.member:m.name for m in self.getTree if "name" in dir(m.get[0].value)}
        self.getTypeNode(dclass, "fielddecl")
        prop3 = {}
        for m in self.getTree:
            if m.name in prop2:
                if "init" in dir(m) and "elts" in dir(m.init):
                    if isinstance( m.init.elts[0], Node) and  m.init.elts[0].type == "custom_call" and m.init.elts[0].namespace.name=="Enum":
                        args = m.init.elts[0].args[0].class_type[0]
                        self.getTypeNode(dclass, "enum")
                        node = self.getAttNode(self.getTree, **{"name":args})
                        prop3[prop2[m.name]] = str(len(node[0].block))
                    else: prop3[prop2[m.name]] = [m.init.elts[0].value if "value" in dir(m.init.elts[0]) else m.init.elts[0].name , m.pseudo_type]
                else: 
                    prop3[prop2[m.name]] = None
       
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
                    if b.target.name.split(".")[0] == prop[p["Name"].decode("utf-8")]: #endswith(p["Name"].decode("utf-8") ):
                        for att in listatt:
                            if att == b.target.member and att!="ValueType":
                                if b.value.type == "binary_op":
                                    vi[att] = b.value.left.value + b.value.right.value
                                else: 
                                    vi[att] = b.value.value
                                if b.value.type == "unary_op": vi[att] = "%s%s"%(b.value.operator, b.value.value.value)
                            if att == "ValueType" and b.target.member == "ValueType" :
                                vi[att] = mapType[b.value.args[0].value.decode('utf-8')]
                                break
                vi["category"] = p["category"]
                if isinstance(prop3[p["Name"].decode("utf-8")], list): vi["len"] = prop3[p["Name"].decode("utf-8")][0]
                var_in.append(vi)
            return var_in
        var_in = attV(inp)
        var_out = attV(out)
        return var_in, pa, var_out
    

    def getAllVar(self, tree, dclass):
        """get metadata from strategy classes and varinfo domain classes

        Args:
            tree (Node): list of varinfo domain classes transformed to Nodes
            dclass (Node): list of domain classes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        
        Result:
            {'Q': {'Name': b'Q', 'category': 'AuxiliaryVarInfo', 'Description': b'Total moisture', 
                    'MaxValue': '100D', 'MinValue': '0D', 'DefaultValue': '50D', 
                    'Units': b'%', 'URL': b'http://', 'ValueType': 'DOUBLE'},
             'Q2': {...} ...
            }
        """

        self.getTypeNode(dclass, "propertyDef")
        prop2 =  {m.get[0].value.member:m.name for m in self.getTree if "name" in dir(m.get[0].value)}

        self.getTypeNode(dclass, "fielddecl")
        prop3 = {}
        for m in self.getTree:
            if m.name in prop2:
                if "init" in dir(m) and "elts" in dir(m.init):
                    if isinstance( m.init.elts[0], Node) and  m.init.elts[0].type == "custom_call" and m.init.elts[0].namespace.name=="Enum":
                        args = m.init.elts[0].args[0].class_type[0]
                        self.getTypeNode(dclass, "enum")
                        node = self.getAttNode(self.getTree, **{"name":args})
                        prop3[prop2[m.name]] = str(len(node[0].block))
                    else: prop3[prop2[m.name]] = [m.init.elts[0].value if "value" in dir(m.init.elts[0]) else m.init.elts[0].name , m.pseudo_type]
                else: 
                    prop3[prop2[m.name]] = None
        
        listatt = ["DefaultValue","Description","MaxValue","Name", "MinValue", "Units", "URL", "ValueType"]            
        prop ={}
        var = {}
        for tr in tree:
            self.getTypeNode(tr, "propertyDef")
            prop.update({m.name :m.get[0].value.name for m in self.getTree if "name" in dir(m.get[0].value)})
            self.getTypeNode(tr, "constructorDef")
            category = self.getTree[0].name  
            self.getTypeNode(tr, "methodDef")
            methNode = self.getTree
            descMeth = self.getAttNode(methNode,**{"name":"DescribeVariables"})
            block = []
            for b in descMeth:
                if b.block:  block += b.block
            for k,v in prop.items():
                vi = {}
                for b in block:
                    if b.target.name.split(".")[0] == v:
                        for att in listatt:
                            if att == b.target.member and att!="ValueType":
                                if b.value.type == "binary_op":
                                    vi[att] = b.value.left.value + b.value.right.value
                                else: 
                                    vi[att] = b.value.value
                                if b.value.type == "unary_op": vi[att] = "%s%s"%(b.value.operator, b.value.value.value)
                            if att == "ValueType" and b.target.member == "ValueType" :
                                vi[att] = mapType[b.value.args[0].value.decode('utf-8')]
                        vi["category"] = category
                        if isinstance(prop3[k], list): 
                            vi["len"] = prop3[k][0]
                        var[k] = vi
        return var
    
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
        else: r = None
        return r
    
    @staticmethod
    def retrieve_var_member(var):
        pass
    
    def prec_cur_states(self, tree, past_current=[]):
        inp_st = []
        if past_current:
            algo = self.getAlgo(tree)
            p = self.getStrategyVar(tree)
            inputs = [st["Name"].decode("utf-8") for st in p[1]]
            outputs = [st["Name"].decode("utf-8") for st in p[2]]
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
        val = self.getStrategyVar(tree)
        p = val[1]
        p2 = val[2]
        var = []
        for inp in p:
            #if not inp["category"].lower().endswith("state"):
            var.append(inp["Name"].decode("utf-8"))
        var = var + pc 
        for out in p2:                                 
            s = out["Name"].decode("utf-8")
            if not (s in var and s+"_t1" in var): # I suppose that we could not have a current and past state in input and current state in output
                var.append(s)
        var = var + [v["Name"].decode("utf-8") for v in  val[0] if v]
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

    def modelunit(self, desc, var, all_var_pa, tvar, inps, outs):
        #desc = self.description(tree)
        self.model= ModelUnit({"name":desc["name"], "version":"001", "timestep":"1"})        
        description = self.model_desc(desc)
        self.model.add_description(description)
        #var = self.getFromVarInfo(tree, tree2, dclass)
        #past_cur = self.instancePastCurrent(tree)
        inp = var[0]
        out = var[2]
        inp_names = [p["Name"].decode("utf-8") for p in inp]
        param = var[1]
        out_names = [p["Name"].decode("utf-8") for p in out]
        param_names = [p["Name"].decode("utf-8") for p in param]
        #pc = self.prec_cur_states(tree, past_cur)

        inp = inp+param+out
        inputs = []
        outputs = []
        inp_par, outp=[], []
        par_var = list(set(inps + outs))
        #varnames = inp_names  + out_names + param_names

        for v in par_var : #pc+param_names+out_names:
            vn = v[:-3] if (len(v)>3 and v not in param_names and v.endswith("_t1")) else v
            if vn in all_var_pa:
                mdata = all_var_pa[vn]
                #vn = v[:-3] if (len(v)>3 and v not in param_names and v.endswith("_t1")) else v
                v_inputtype = "parameter" if v in param_names else "variable"
                v_categ = "parametercategory" if v in param_names else "variablecategory"
                #description = [s["Description"].decode("utf-8") for s in inp if s["Name"].decode("utf-8") == vn][0]
                description = mdata["Description"].decode("utf-8")
                #category = [categorize(s["category"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
                category = categorize(mdata["category"])
                #datatype = [s["ValueType"] for s in inp if s["Name"].decode("utf-8") == vn][0]
                datatype = mdata["ValueType"]
                #max = [modVal(s["MaxValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
                max = modVal(mdata["MaxValue"])
                if max: 
                    #max = max.decode("utf-8")
                    if max.endswith("D"):  max = max.replace("D", "")
                
                #min = [modVal(s["MinValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
                min = modVal(mdata["MinValue"])
                if min:
                    #min = min.decode("utf-8")
                    if "D" in min: min = min.replace("D", "")
                    
                #default = [modVal(s["DefaultValue"]) for s in inp if s["Name"].decode("utf-8") == vn][0]
                default = modVal(mdata["DefaultValue"])
                if default:
                    #default = default.decode("utf-8")
                    if  datatype != "STRING" and default.endswith("D"): default = default.replace("D", "")
                    
                #unit = [s["Units"].decode("utf-8") for s in inp if s["Name"].decode("utf-8") == vn][0]
                unit = mdata["Units"].decode("utf-8")
                
                #len_ = [s["len"] for s in inp if s["Name"].decode("utf-8") == vn and "len" in s]
                len_ = [mdata["len"]] if "len" in mdata else None
                desc_dict = {"name":v, "description":description, 
                                    v_categ:category,
                                    "datatype": datatype,
                                    "inputtype":v_inputtype,
                                    "max":max,
                                    "min":min,
                                    "unit":unit,
                                    "len":len_[0] if len_ else ""}
                
                if v in inps: # I suppose that we could not have a current and past state in input and current state in output
                    desc_dict["default"] = default
                    inputs.append(Input(desc_dict))
                    inp_par.append(v)
                if v in outs:
                    outputs.append(Output(desc_dict))
                    outp.append(v)
            
        self.model.inputs = inputs
        self.model.outputs = outputs

        #algo = self.getAlgo(tree)
        #funcs = self.externFunction(tree, algo.block)
        #self.model.function = [func.name for func in funcs if func] if funcs else []
    
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
            
        
        
        #n = self.getAttNode(self.getTree,**{'type':'declaration', 'target': Node(type = 'member_access', name= v, member = att, pseudo_type = 'VarInfo')})   
        
        

            

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













