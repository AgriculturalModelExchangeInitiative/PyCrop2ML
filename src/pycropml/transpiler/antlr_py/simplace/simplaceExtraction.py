
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
    
    def getProcess(self, tree):
        algo = self.getmethod(tree, "process")
        return algo

    def getInit(self, tree):
        return self.getmethod(tree, "init")
    
    def getOutputs(self, tree):
        algo = self.getProcess(tree)
        self.getTypeNode(algo.block, "custom_call")
        setouts = self.getAttNode(self.getTree, **{"function":"setValue"}) + self.getAttNode(self.getTree, **{"function":"setArrayValue"})
        outs = list(map(lambda out: out.instance.name, setouts))
        return outs

    def modelunit(self, tree):
        desc = self.description(tree)
        self.model= ModelUnit({"name":desc["name"], "version":"001", "timestep":"1"})        
        description = self.model_desc(desc)
        self.model.add_description(description)
        all_declarations = self.getInouts(tree)
        realinout = self.getRealInOut(tree)
        outnames = self.getOutputs(tree)
        inputs = []
        outputs = []
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
            elif att == "privat": category = "auxiliary"
            else: category = att.lower()
            
            unit = d[4].value
            min = d[5].value
            if isinstance(min, Node) and d[5].type=="unary_op":
                min = str(d[5].operator)+min.value
            max = d[6].value
            default = d[7].value
            if default == "null": default = ""
    
            desc_dict = {"name":name, "description":dd.decode("utf-8"), 
                         v_categ : category,
                        "datatype": datatype,
                        "inputtype":v_inputtype,
                        "max":max,
                        "min":min,
                        "unit":unit.decode("utf-8")
                        }
            if name not in outnames:
                desc_dict["default"] = default # if isinstance(default, str) \
                            #else default.decode("utf-8"),
                inputs.append(Input(desc_dict))
            else:
                outputs.append(Output(desc_dict))

        self.model.inputs = inputs
        self.model.outputs = outputs
        print(self.model.description.Title, 'ooooo')

    def model_desc(self, desc):
        name = desc["name"][:-9] if desc["name"].endswith("Component") else desc["name"]
        description = Description()
        description.Title = name+" model" 
        description.Authors = desc["authors"]
        description.Institution=desc["institution"]
        description.Reference = desc["Reference"], 
        description.Abstract = desc["description"]
        description.Url = desc["url"]
        return description

    def description(self, tree):
        
        d = ["name", "authors", "institution", "description", "url"]
        desc = {}
        constr = self.getTypeNode(tree, "classDef")
        desc["name"] = str(self.getTree[0].name) 
        desc["authors"] = "Gunther Krauss"
        desc["institution"] = "INRES Pflanzenbau, Uni Bonn"
        desc.update(Reference = "http://www.simplace.net/doc/simplace_modules/")
        desc["description"] = "as given in the documentation"
        desc["url"] = "http://www.simplace.net/doc/simplace_modules/"     
        return desc   

               
            







