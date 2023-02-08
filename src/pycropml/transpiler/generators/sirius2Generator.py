# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.csharpRules import CsharpRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
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
                "DOUBLEARRAY":"DOUBLEARRAY",
                "INTARRAY":"INTARRAY"}

def getdefault(x, typ):
    df = "-1D"
    if typ in dir(x):
        if  x.datatype=="DOUBLE" or x.datatype == "INT":
            p = getattr(x, typ) 
            if p and p is not None:
                df = p
    return df
    

def noValue(pa):
    if "DOUBLE" in pa.datatype or "DATE" in pa.datatype: df = "-1D"
    if "INT" in pa.datatype: df = '-1'
    if "BOOLEAN" in pa.datatype: df = 'false'
    if "STRING" in pa.datatype: df = "null"
    return df


class Sirius2Generator(CsharpGenerator):
    """ This class contains the specific properties of
    SQ components and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree based on BioMa structure.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        CsharpGenerator.__init__(self, tree, model, name)  
        self.usingBioma()  
                

    def usingBioma(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;    
""")

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name  
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.write("public static ")
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            self.write(" Main(") if node.name=="main" else self.write(" %s("%node.name)
            for i, pa in enumerate(node.params):
                self.visit_decl(pa.pseudo_type)
                self.write(" %s"%pa.name)
                if i!= (len(node.params)-1):
                    self.write(', ')
            self.write(')')
            self.open(node)
        else: 
            if self.node_param and not node.name.startswith("init_") :
                for arg in self.node_param: 
                    self.newline(node) 
                    self.write ('private ') 
                    self.visit_decl(arg.pseudo_type)
                    self.write(" _")
                    self.write(arg.name) 
                    self.write(";")                     
                    #self.generator.private(self.node_param)        
                    self.newline(node)
                    self.write("public ")
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' +arg.name)
                    self.write(self.public_properties%(arg.name,arg.name))
            self.write(self.constructor%self.model.name) if not node.name.startswith("init_") else ""
            self.newline(node)      
            self.write("private void CalculateModel(") if not node.name.startswith("init_") else self.write("public void Init(")
            self.write('SiriusQuality%s.DomainClass.%sState s, SiriusQuality%s.DomainClass.%sState s1, SiriusQuality%s.DomainClass.%sRate r, SiriusQuality%s.DomainClass.%sAuxiliary a, SiriusQuality%s.DomainClass.%sExogenous ex)'%(self.name, self.name,self.name,self.name,self.name, self.name,self.name,self.name, self.name,self.name))
            self.newline(node)
            self.write("{")
            self.newline(node)
            self.indentation += 1 
            if not node.name.startswith("init_"):
                self.write(self.doc.header)
                self.newline(node)
                self.write(self.doc.desc)
                self.newline(node)
                self.write(self.doc.inputs_doc)
                self.newline(node)
                self.write(self.doc.outputs_doc)
                self.newline(node)
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
                                if arg.name in self.states and arg.name.endswith("_t1") :
                                    self.write(" = s1.%s"%arg.name[:-3])
                                if arg.name in self.rates:
                                    self.write(" = r.%s"%arg.name)
                                if arg.name in self.auxiliary:
                                    self.write(" = a.%s"%arg.name) 
                                if arg.name in self.exogenous:
                                    self.write(" = ex.%s"%arg.name) 
                            else:
                                if arg.pseudo_type[0] =="list":
                                    self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
                                elif arg.pseudo_type[0] =="array":
                                    if arg.elts:
                                        length =  arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name
                                        if length:
                                            self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], length))
                            self.write(";")                   
        self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.close(node)
        self.newline(extra=1)

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
        self.write("using SiriusQuality%s.DomainClass;"%self.name)
        self.newline(node)
        self.write("namespace SiriusQuality%s.Strategies"%self.name)
        self.open(node)
        if self.model is not None:
            self.write("public class %s"%self.model.name)
        else:
            self.write("public class Test")
        self.open(node) 
        self.estimate(node)  ###
        self.visit(node.body)
        self.close(node)  #namespace  
        self.close(node)  

    def estimate(self, node):
        self.write("public void Estimate(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("CalculateModel(s, s1, r, a, ex);")
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)")
        self.open(node)
        self.write('string msg = "Error in component SiriusQuality%s, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;'%self.name)				
        self.newline(node)
        self.write('throw new Exception(msg, exception);')
        self.close(node)
        self.close(node)
        self.newline(extra=1)        


class Sirius2Trans(CsharpTrans):
    """ This class used to generates states, rates, auxiliary and exogenous classes
    for Sirius.
    """
    
    def __init__(self, models):
        self.models = models
        CsharpTrans.__init__(self, self.models)


    def using(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Reflection;

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
        self.write('public %s(%s toCopy, bool copyAll) // copy constructor '%(typ, typ))
        self.open(nodes)
        self.write('if (copyAll)')
        self.open(nodes)
        self.copyconstructor(nodes)
        self.close(nodes)
        self.close(nodes)
        self.newline(extra = 1)


    def clearValue(self, node):
        self.write("public virtual Boolean ClearValues()")
        self.open(node)
        for arg in node:
            self.newline(node) 
            self.write(" _")
            self.write(arg.name)
            if arg.pseudo_type[0] =="list":
                self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
            elif arg.pseudo_type=="DateTime":
                self.write(" = new DateTime()")
            elif arg.pseudo_type[0] =="array":
                self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
            elif arg.pseudo_type == "str":
                self.write(" = null")
            else: self.write(" = default(%s)"%(self.types[arg.pseudo_type]))
            self.write(";") 
        self.newline(node);
        self.write("return true;")
        self.close(node)
        self.newline(extra=1)

    def generate(self, nodes, typ, name): 
        self.using()
        self.write("namespace SiriusQuality%s.DomainClass"%name)
        self.open(nodes)
        self.write("public class %s"%typ)
        self.newline()
        self.write("{")
        self.indentation += 1        
        self.newline()
        self.private(nodes)
        self.newline()
        self.copyConstr(nodes, typ)###### copy constructor     
        self.getset(nodes)
        self.newline(extra=1)
        self.clearValue(nodes)
        self.indentation -= 1
        self.newline()
        self.write('}')
        self.close(nodes)
    

def to_struct_sirius2(models, rep, name):
    generator = Sirius2Trans(models)
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


class Sirius2Compo(CsharpCompo):
    """ This class used to generates states, rates, auxiliary and exogenous classes
        for C# languages.
    """
    def __init__(self, tree=None, model=None, name=None):
        self.model=model
        self.tree = tree
        self.name = name
        CsharpCompo.__init__(self, tree, model, name)

    def usingBioma(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;     
""")
        



    def estimate(self, node):
        self.write("public void Estimate(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("try")
        self.open(node)
        self.write("CalculateModel(s, s1, r, a, ex);")
        self.close(node)
        self.newline(node)
        self.write("catch (Exception exception)")
        self.open(node)
        self.write('string msg = "Error in component SiriusQuality%s, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;'%self.name)				
        self.newline(node)
        self.write('throw new Exception(msg, exception);')
        self.close(node)
        self.close(node)
        self.newline(extra=1)
        

    def constructor(self, node):
        self.write("public %sComponent()"%self.model.name)  
        self.open(node)   
        self.newline(node)    
        self.close(node)
        self.newline(extra=1)

    def calculateModel(self, node):
        self.write("private void CalculateModel(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        self.open(node)
        self.write("EstimateOfAssociatedClasses(s, s1, r, a, ex);")
        self.close(node)
        self.newline(extra=1)
    
    def copy_Constructor(self, node):
        self.write('public %sComponent(%sComponent toCopy): this() // copy constructor '%(self.model.name, self.model.name))
        self.open(node)
        self.copyconstructor(self.node_param)
        self.close(node)
        

    def visit_module(self, node): 
        self.usingBioma()
        self.newline(node)
        self.write("using SiriusQuality%s.DomainClass;"%self.model.name)
        self.newline(node)
        self.write("namespace SiriusQuality%s.Strategies"%self.model.name)
        self.open(node)
        self.write("public class %sComponent "%(self.model.name))
        self.open(node)   
        self.constructor(node)   
        self.getsetParam(node,self.node_param)
        self.estimate(node)
        self.calculateModel(node)
        self.createModelInstances()
        self.newline(extra=1)
        self.visit(node.body)
        self.newline(extra=1)
        self.copy_Constructor(self.node_param)
        self.newline(node)
        self.close(node)
        self.close(node)
    
    def visit_function_definition(self, node):
        if node.name.startswith("model"):
            self.write("private void EstimateOfAssociatedClasses(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
        else:
            self.write("public void Init(SiriusQuality%s.DomainClass.%sState s,SiriusQuality%s.DomainClass.%sState s1,SiriusQuality%s.DomainClass.%sRate r,SiriusQuality%s.DomainClass.%sAuxiliary a,SiriusQuality%s.DomainClass.%sExogenous ex)"%(self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name,self.name))
            self.init=True
        self.open(node)
        self.visit(node.block)
        self.close(node)
        self.newline(extra=1)

    def visit_implicit_return(self, node):
        self.newline(node)

    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            nm = [m.name for m in self.model.model if m.name.lower() == name][0]
            self.write("_%s.Estimate(s,s1, r, a, ex);"%(nm))
            self.newline(node)
        else:
            self.newline(node)
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)


    def wrapper(self):
        self.write("using SiriusQuality%s.DomainClass;"%self.model.name)
        self.newline(1)
        self.write("using SiriusQuality%s.DomainClass;"%self.model.name)
        self.newline(extra=1)
        self.write("namespace SiriusModel.Model.%s"%self.model.name)
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1         
        self.write("class %sWrapper :  UniverseLink"%self.model.name)
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.privateWrap()
        self.constrWrap()
        self.newline(extra=1)
        self.outputWrap()
        self.newline(extra=1)
        self.copyconstrWrap()
        self.newline(extra=1)
        self.initWrap()
        self.newline(extra=1)
        self.loadParamWrap()
        self.newline(extra=1)
        self.estimateWrap()
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}")
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}")
    
    def constrWrap(self):
        name = self.model.name
        self.write("public %sWrapper(Universe universe) : base(universe)"%(name))
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
        self.write("%sComponent = new %s();"%(name.lower(), name))
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")


    def copyconstrWrap(self):
        self.write("public %sWrapper(Universe universe, %sWrapper toCopy, bool copyAll) : base(universe)"%(self.model.name,self.model.name))
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("s = (toCopy.s != null) ? new %sState(toCopy.s, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("s1 = (toCopy.s != null) ? new %sState(toCopy.s1, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("r = (toCopy.r != null) ? new %sRate(toCopy.r, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("a = (toCopy.a != null) ? new %sAuxiliary(toCopy.a, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("ex = (toCopy.ex != null) ? new %sExogenous(toCopy.ex, copyAll) : null;"%(self.model.name))
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("%sComponent = (toCopy.%sComponent != null) ? new %s(toCopy.%sComponent) : null;"%(self.model.name.lower(),self.model.name.lower(),self.model.name,self.model.name.lower()))
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

def to_wrapper_sirius2(models, rep, name):
    generator = Sirius2Compo(model = models)
    generator.result=[u"using System;\nusing System.Collections.Generic;\nusing System.Linq;\n"]
    generator.model2Node()
    generator.wrapper()
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sWrapper.cs"%name))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    return 0