
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

class BiomaExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
      
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
                if att !="ValueType" : vi[att] = n[0].value.value
                else: vi[att] = n[0].value.args[0].value
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
    
    def getFromVarInfo(self, tree1, *tree):
        """get metadata from strategy classes and varinfo domain classes

        Args:
            tree1 (Node): A strategy class transformed to Node
            *tree (Node): varinfo domain classes transformed to Nodes

        Returns:
            Tuple: metadata (inputs, parameters, outputs)
        """
        tree2 = []
        for t in tree:
            tree2.append(t)
        self.getTypeNode(tree2, "methodDef")
        methNode = self.getTree
        descMeth = self.getAttNode(methNode,**{"name":"DescribeVariables"})
        block = descMeth[0].block
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










