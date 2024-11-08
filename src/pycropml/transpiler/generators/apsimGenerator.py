# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.csharpRules import CsharpRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
from pycropml.nameconvention import signature2, signature2_from_name
import os
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml import code2nbk
from pycropml.transpiler.generators.csharpGenerator import CsharpGenerator, CsharpTrans,CsharpCompo



category = {"state":"s", "rate":"r", "auxiliary":"a", "exogenous":"ex"}
param_datatype ={"STRING":"String", 
                "INT":"Integer", 
                "DOUBLE":"Double", 
                "BOOLEAN":"Boolean",
                "DATE":"Date",
                "DATELIST":"ListDate",
                "STRINGLIST": "ListString",
                "DOUBLELIST": "ListDouble",
                "INTLIST": "ListInteger",
                "BOOLEANLIST": "ListBoolean",
                "DOUBLEARRAY":"ArrayDouble",
                "INTARRAY":"ArrayInteger"}

def getdefault(x, typ):
    df = "-1D"
    if typ in dir(x):
        if  x.datatype=="DOUBLE" or x.datatype == "INT":
            p = getattr(x, typ) 
            if p and p is not None:
                df = p
    return df
    

class ApsimGenerator(CsharpGenerator):
    """ This class contains the specific properties of
    APSIM components and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree based on BioMa structure.
    """
    
    def __init__(self, tree=None, model=None, name=None, customer=''):
        CsharpGenerator.__init__(self, tree, model, name) 
        self.tree = tree
        self.model=model
        self.name = name
        self.customer = customer
        self.indent_with=' '*4
        self.doc= DocGenerator(model, '///','')
        print(self.doc.header) 
        self.usingApsim()  
                

    def usingApsim(self):
        self.write("""using System;
using System.Collections.Generic;
using System.Linq;    
using Models.Core;   
""")


    def visit_function_definition(self, node):      
        self.newline(node)
        #self.add_features(node)
        self.funcname = node.name
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.write("/// <summary>")
            self.newline(1)
            self.write(f"/// ")
            self.newline(1)
            self.write("/// </summary>")  
            self.newline(1) 
            if isinstance(node.block, list)  and "elements" in dir(node.block[-1].value):           
                self.write("public static void ")
                tg = [elt.name for elt in node.block[-1].value.elements]
                self.tg = tg
                tb = []
                #self.visit_decl(node.return_type) if node.return_type else self.write("void")
                self.write(" Main(") if node.name=="main" else self.write(" %s("%node.name)
                for i, pa in enumerate(node.params):
                    if pa.name in tg:
                        self.write("ref ")
                        tb.append(pa.name)
                    self.visit_decl(pa.pseudo_type)
                    self.write(" %s"%pa.name)
                    if i!= (len(node.params)-1):
                        self.write(', ')
                for elt in node.block[-1].value.elements:
                    if elt.name not in tb:
                        self.write(", out ")
                        self.visit_decl(elt.pseudo_type)
                        self.write(f' {elt.name}') 
            else:
                self.write("public static ")
                self.visit_decl(node.return_type) if node.return_type else self.write("void")
                self.write(" Main(") if node.name=="main" else self.write(" %s("%node.name)
                for i, pa in enumerate(node.params):
                    self.visit_decl(pa.pseudo_type)
                    self.write(" %s"%pa.name)
                    if i!= (len(node.params)-1):
                        self.write(', ')  
            self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
        else:
            name = signature2_from_name(self.model.name)
            cpnent = signature2_from_name(self.name)
            if self.node_param and not node.name.startswith("init_") :
                for arg in self.node_param: 
                    self.newline(extra=1) 
                    self.write ('private ') 
                    self.visit_decl(arg.pseudo_type)
                    self.write(" _")
                    self.write(arg.name) 
                    self.write(";")                     
                    #self.generator.private(self.node_param)        
                    self.newline(node)
                    self.write("/// <summary>")
                    self.newline(1)
                    self.write(f"/// Gets and sets the {arg.description}")
                    self.newline(1)
                    self.write("/// </summary>")  
                    self.newline(1) 
                    self.write(f'[Description("{arg.description}")] ')
                    self.newline(1)
                    self.write(f'[Units("{arg.unit}")] ')
                    self.newline(1)
                    self.write(f'//[Crop2ML(datatype="{arg.datatype}", min={arg.mini}, max={arg.maxi}, default={arg.default}, parametercategory={arg.category}, inputtype="parameter")] ')
                    self.newline(1)
                    self.write("public ")
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' +arg.name)
                    self.write(self.public_properties%(arg.name,arg.name))
            self.newline(extra=1)
            self.write(self.constructor%(name,name)) if not node.name.startswith("init_") else ""
            self.newline(node)  
            if node.name.startswith("init_"):
                self.write("/// <summary>")
                self.newline(1)
                self.write(f"/// initialization of the {name} component")
                self.newline(1)
                self.write("/// </summary>")  
                self.newline(1)
            else:
                self.write("/// <summary>")
                self.newline(1)
                self.write(f"/// Algorithm of the {name} component")
                self.newline(1)
                self.write("/// </summary>")  
                self.newline(1)              
            self.write("public void ")
            self.write(" CalculateModel(") if not node.name.startswith("init_") else self.write("Init(")
            self.write('%sState s, %sState s1, %sRate r, %sAuxiliary a, %sExogenous ex)'%(cpnent, cpnent,cpnent, cpnent, cpnent))
            self.newline(node)
            self.write('{') 
            self.newline(node)
            if not node.name.startswith("init_"):
                pass
            self.indentation += 1 
            for arg in self.add_features(node) :
                if "feat" in dir(arg):
                    if arg.feat in ["IN","INOUT"] :
                        self.newline(node) 
                        if self.model and arg.name not in self.modparam:
                            self.visit_decl(arg.pseudo_type)
                            self.write(" ")
                            self.write(arg.name)
                            if not node.name.startswith("init_"):
                                if arg.name in self.states and not arg.name.endswith("_t1") :
                                    self.write(" = s.%s"%arg.name)
                                elif arg.name.endswith("_t1") and arg.name in self.states:
                                    self.write(" = s1.%s"%arg.name[:-3])
                                elif arg.name in self.rates:
                                    self.write(" = r.%s"%arg.name)
                                elif arg.name in self.auxiliary:
                                    self.write(" = a.%s"%arg.name) 
                                elif arg.name in self.exogenous:
                                    self.write(" = ex.%s"%arg.name)
                            else:
                                if arg.name in self.exogenous:
                                    self.write(" = ex.%s"%arg.name)                                
                                elif arg.pseudo_type[0] =="list":
                                    self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
                                elif arg.pseudo_type[0] =="array":
                                    if not arg.elts:
                                        pass
                                    else: self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                            self.write(";")                   
            self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1 
        self.write('}') 
        self.newline(node)

    def open(self, node):
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
    
    def close(self, node):
        self.newline(node)
        self.indentation -= 1 
        self.write("}")


    def visit_module(self, node):
        self.write("namespace Models.Crop2ML;")
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(node)
        self.write(self.doc.header)
        self.newline(node)
        self.write(self.doc.desc)
        self.newline(node)
        self.write(self.doc.inputs_doc)
        self.newline(node)
        self.write(self.doc.outputs_doc)
        self.newline(node)
        self.write("/// </summary>")
        self.newline(node)
        self.write("public class %s"%(signature2_from_name(self.model.name)))
        self.open(node)
        self.visit(node.body)
        self.close(node)  #class          


class ApsimTrans(CsharpTrans):
    """ This class used to generates states, rates, auxiliary and exogenous classes
    for Bioma.
    """
    
    def __init__(self, models, customer=''):
        self.models = models
        self.customer=customer
        CsharpTrans.__init__(self, self.models)


    def using(self):
        self.write("""using System;
using System.Collections.Generic;
using Models.Core;
""")

    def open(self, node):
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
    
    def close(self, node):
        self.newline(node)
        self.indentation -= 1 
        self.write("}")

    def copyConstr(self, nodes, typ):
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"/// Copy constructor")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1)
        self.write(f'/// <param name="toCopy"></param>')
        self.newline(1)
        self.write(f'/// <param name="copyAll"></param>') 
        self.newline(1)  
        self.write('public %s(%s toCopy, bool copyAll) // copy constructor '%(signature2_from_name(typ), signature2_from_name(typ)))
        self.open(nodes)
        self.write('if (copyAll)')
        self.open(nodes)
        self.indentation -= 2
        self.copyconstructor(nodes)
        self.close(nodes)
        self.close(nodes)
        self.newline(extra = 1)


    def constr(self, node, typ):
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"/// Constructor {signature2_from_name(typ)} domain class")
        self.newline(1)
        self.write("/// </summary>")  
        self.newline(1)  
        self.write('public %s() { }'%signature2_from_name(typ))
        self.newline(1)
        
    def generate(self, nodes, typ, name): 
        self.using()
        self.write("namespace Models.Crop2ML;")
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"/// {nodes[0].category} variables class of the {name} component") if len(nodes)>0 else ""
        self.newline(1)
        self.write("/// </summary>")  
        self.newline(1)
        self.write("public class %s"%signature2_from_name(typ))
        self.newline()
        self.write("{")
        self.indentation += 1        
        self.newline()
        self.private(nodes)
        self.newline()
        self.constr(nodes, typ)    ########### constructor
        self.newline(extra = 1)
        self.copyConstr(nodes, typ)###### copy constructor     
        self.getset(nodes)
        self.newline(extra=1)
        self.indentation -= 1
        self.newline()
        self.write("}")


    def getset(self,node, wrap=False):
        for arg in node:   
            self.newline(node)
            self.write("/// <summary>")
            self.newline(1)
            self.write(f"/// Gets and sets the {arg.description}")
            self.newline(1)
            self.write("/// </summary>")    
            self.newline(node)
            self.write(f'[Description("{arg.description}")] ')
            self.newline(1)
            self.write(f'[Units("{arg.unit}")] ')
            self.newline(1)
            self.write("public ")
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] in ("list", "array"):
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' + arg.name)                                                            
            else:
                self.visit_decl(arg.pseudo_type)
                self.write(' ' +arg.name)
            self.write(self.public_properties%(arg.name,arg.name)) if wrap==False else self.write(self.public_properties_wrap%(arg.cat,arg.name))
            self.newline(extra=1)

def to_struct_apsim(models, rep, name):
    generator = ApsimTrans(models)
    generator.model2Node()

    def createdc(states, catvar):
        generator.result = []
        generator.generate(states, "%s%s"%(name,catvar), name)
        z= ''.join(generator.result)
        filename = Path(os.path.join(rep, "%s%s.cs"%(name, catvar)))
        with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))

    states = generator.node_states
    createdc(states,"State")
    rates = generator.node_rates
    createdc(rates,"Rate")      
    auxiliary = generator.node_auxiliary
    createdc(auxiliary,"Auxiliary") 
    exogenous = generator.node_exogenous
    createdc(exogenous,"Exogenous") 




''' Csharp composite'''


class ApsimCompo(CsharpCompo):
    """ This class used to generates states, rates, auxiliary and exogenous classes
        for C# languages.
    """
    def __init__(self, tree=None, model=None, name=None, customer=""):
        CsharpCompo.__init__(self, tree, model, name)
        self.model=model
        self.tree = tree
        self.name = name
        self.customer=customer
        

    def usingApsim(self):
        self.write("""using Models.Core;
using Models.Utilities;
using System; 
namespace Models.Crop2ML;
     
""")

    def constructor(self, node):
        self.write("public %sComponent() {}"%signature2_from_name(self.model.name))  

    
    def copy_Constructor(self, node):
        self.write('public %sComponent(%sComponent toCopy): this() // copy constructor '%(signature2_from_name(self.model.name), signature2_from_name(self.model.name)))
        self.open(node)
        self.indentation -= 1
        self.copyconstructor(self.node_param)
        self.indentation -= 1
        self.close(node)
        

    def visit_module(self, node): 
        self.usingApsim()
        self.newline(node)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  {self.model.name} component")
        self.newline(1)
        self.write("/// </summary>")
        self.newline(1)
        self.write(f"public class {signature2_from_name(self.model.name)}Component ")
        self.open(node)
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  constructor of {signature2_from_name(self.model.name)} component")
        self.newline(1)
        self.write("/// </summary>")
        self.newline(1)
        self.constructor(node)
        self.newline(extra=1)     
        self.createModelInstances()   
        self.newline(extra=1)      
        self.getsetParam(node,self.node_param)
        self.newline(extra=1)
        self.visit(node.body)
        self.newline(extra=1)
        self.newline(node)
        if not self.model.initialization:
            self.write("/// <summary>")
            self.newline(1)
            self.write(f"/// Initialization of {signature2_from_name(self.model.name)} component")
            self.newline(1)
            self.write("/// </summary>")
            self.newline(1)
            self.initcomposition(node)
            self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"/// constructor copy of {signature2_from_name(self.model.name)} component")
        self.newline(1)
        self.write("/// </summary>")
        self.newline(1)
        self.write('/// <param name="toCopy"></param>')
        self.newline(1)
        self.copy_Constructor(self.node_param)
        self.newline(node)
        self.close(node)
        
    def initcomposition(self, node):
        name = signature2_from_name(self.model.name)
        self.write(f"public void Init({name}State s, {name}State s1, {name}Rate r, {name}Auxiliary a, {name}Exogenous ex)")
        self.open(node)
        self.newline(1)
        for m in self.model.ord:
            for mod in self.model.model:
                if m == mod.name and "initialization" in dir(mod) and mod.initialization:
                    self.write(f"_{signature2_from_name(m)}.Init(s, s1, r, a, ex);")
                    self.newline(1)
        self.close(node)
        

    def getsetParam(self,node, pa)   :
        for arg in pa :  
            if arg.name in self.parameters:                        
                self.newline(extra=1)
                self.write("/// <summary>") 
                self.newline(1)
                self.write(f"/// Gets and sets the {arg.description}")
                self.newline(1)
                self.write("/// </summary>")  
                self.newline(1) 
                self.write(f'[Description("{arg.description}")] ')
                self.newline(1)
                self.write(f'[Units("{arg.unit}")] ')
                self.newline(1)
                self.write("public ")
                self.visit_decl(arg.pseudo_type)
                self.write(' ' +arg.name)
                self.open(node)
                self.write("get")
                self.open(node)
                self.write(" return _%s.%s; "%(signature2_from_name(self.get_mo(arg.name)[0]["modu"]),self.get_mo(arg.name)[0]["var"]))
                self.close(node)
                self.newline(1)
                self.write("set")
                self.open(node)
                self.setCompo(arg.name)
                self.close(node)
                self.close(node)
        self.newline(extra=1)
    
    def visit_function_definition(self, node):
        name = signature2_from_name(self.model.name)
        cpnt = signature2_from_name(self.name)
        if node.name.startswith("model"):
            self.newline(1)
            self.write("/// <summary>")
            self.newline(1)
            self.write(f"/// Algorithm of {signature2_from_name(self.model.name)} component")
            self.newline(1)
            self.write("/// </summary>")
            self.newline(1)
            self.write(f"public void CalculateModel({cpnt}State s,{cpnt}State s1,{cpnt}Rate r,{cpnt}Auxiliary a,{cpnt}Exogenous ex)")
        else:
            self.write("/// <summary>")
            self.newline(1)
            self.write(f"/// initialization of the {name} component")
            self.newline(1)
            self.write("/// </summary>")
            self.newline(1)
            self.write(f"public void Init({self.name}State s,{self.name}State s1,{self.name}Rate r,{self.name}Auxiliary a,{self.name}Exogenous ex)")
            self.init=True
        self.open(node)
        self.visit(node.block)
        self.close(node)
        self.newline(extra=1)

    def visit_implicit_return(self, node):
        self.newline(node)



    def wrapper(self):
        name = signature2_from_name(self.model.name)
        self.write("""using APSIM.Shared.Utilities;
using Models.Climate;
using Models.Core;
using Models.Interfaces;
using Models.PMF;
using Models.Soils;
using Models.Surface;
using System;
using System.Collections.Generic;
using System.Linq;
namespace Models.Crop2ML;""")

        self.newline(extra=1)  
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  This class encapsulates the {name}Component")
        self.newline(1)
        self.write("/// </summary>")  
        self.write("""
[Serializable]
[PresenterName("UserInterface.Presenters.PropertyPresenter")]
[ViewName("UserInterface.Views.PropertyView")]
[ValidParent(ParentType = typeof(Zone))]
""")    
        self.write("class %sWrapper :  Model"%name)
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write("[Link] Clock clock = null;")
        self.newline(1)
        self.write("//[Link] Weather weather = null; // other links")
        self.newline(extra=1)
        self.privateWrap()
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  The constructor of the Wrapper of the {name}Component")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1) 
        self.constrWrap()
        self.newline(extra=1)
        self.outputWrap()
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  The Constructor copy of the wrapper of the {name}Component")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1)
        self.write(f'/// <param name="toCopy"></param>')
        self.newline(1)
        self.write(f'/// <param name="copyAll"></param>') 
        self.newline(1)  
        self.copyconstrWrap()
        self.newline(extra=1)
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  The Initialization method of the wrapper of the {signature2_from_name(self.model.name)}Component")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1)
        self.initWrap()
        self.newline(extra=1)
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  Load parameters of the wrapper of the {signature2_from_name(self.model.name)}Component")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1)
        self.loadParamWrap()
        self.newline(extra=1)
        self.write("/// <summary>")
        self.newline(1)
        self.write(f"///  Set exogenous variables of the wrapper of the {signature2_from_name(self.model.name)}Component")
        self.newline(1)
        self.write("/// </summary>") 
        self.newline(1)
        self.setexogenousWrap()
        self.newline(extra=1)
        self.estimateWrap()
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}")

    def estimateWrap(self):
        self.write('[EventSubscribe("Crop2MLProcess")]')
        self.newline(1)
        self.write("public void CalculateModel(object sender, EventArgs e)")       
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        self.write("if (clock.Today == clock.StartDate)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        self.write("Init();")
        self.newline(1)
        self.indentation -= 1 
        self.newline(1)
        self.write("}")
        self.newline(1)
        self.write("setExogenous();")
        self.newline(1)
        self.write("%sComponent.CalculateModel(s,s1, r, a, ex);"%(self.model.name.lower()))
        self.newline(1)
        self.indentation -= 1 
        self.write("}")
        
        
    def outputWrap(self):
        out = [out.name for out in self.model.outputs]
        tabout=[]
        nodes =self.node_states+self.node_rates+self.node_auxiliary + self.node_exogenous
        for node in nodes :
            if node.name in out and node.name not in tabout:
                self.newline(extra=1)
                self.write("/// <summary>")
                self.newline(1)
                self.write(f"///  The get method of the {node.description} output variable")
                self.newline(1)
                self.write("/// </summary>") 
                self.newline(1)
                self.write(f'[Description("{node.description}")]')
                self.newline(1)
                self.write(f'[Units("{node.unit}")]')
                self.getset([node], True)
                tabout.append(node.name)
    
    def constrWrap(self):
        name = signature2_from_name(self.model.name)
        self.write("public %sWrapper()"%(name))
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write("s = new %sState();"%(name))
        self.newline(1)
        self.write("s1 = new %sState();"%(name))
        self.newline(1)
        self.write("r = new %sRate();"%(name))
        self.newline(1)
        self.write("a = new %sAuxiliary();"%(name))
        self.newline(1)
        self.write("ex = new %sExogenous();"%(name))
        self.newline(1)
        self.write("%sComponent = new %sComponent();"%(name.lower(), name))
        self.newline(1)
        self.indentation -= 1
        self.write("}")


    def copyconstrWrap(self):
        name = signature2_from_name(self.model.name)
        self.write("public %sWrapper(%sWrapper toCopy, bool copyAll) "%(name,name))
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("s = (toCopy.s != null) ? new %sState(toCopy.s, copyAll) : null;"%(name))
        self.newline(1)
        self.newline(1)
        self.write("r = (toCopy.r != null) ? new %sRate(toCopy.r, copyAll) : null;"%(name))
        self.newline(1)
        self.write("a = (toCopy.a != null) ? new %sAuxiliary(toCopy.a, copyAll) : null;"%(name))
        self.newline(1)
        self.write("ex = (toCopy.ex != null) ? new %sExogenous(toCopy.ex, copyAll) : null;"%(name))
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("%sComponent = (toCopy.%sComponent != null) ? new %sComponent(toCopy.%sComponent) : null;"%(name.lower(),name.lower(),name,name.lower()))
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

def to_wrapper_apsim(models, rep, name, customer = ''):
    generator = ApsimCompo(model = models, customer=customer)
    generator.model2Node()
    generator.wrapper()
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sWrapper.cs"%name))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    return 0