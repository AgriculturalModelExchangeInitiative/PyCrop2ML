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

class SiriusGenerator(CsharpGenerator):
    """ This class contains the specific properties of
    Csharp language and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
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
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       
""")

    def usingComponentDomainClass(self):
        self.write("using SiriusQuality%sDomainClass"%self.name.capitalize())

    
    def inOutputDesc(self, node):
        self.newline(node)
        
        self.write("ModellingOptions mo0_0 = new ModellingOptions();")
        self.newline(node)
        self.write("//Parameters")
        self.newline(node)
        self.write("List<VarInfo> _parameters0_0 = new List<VarInfo>();")
        self.newline(node)
        n = 1
        for p in self.model.parameters:
            self.write("VarInfo v%s = new VarInfo();"%n)
            self.newline(node)
            self.write("v%s.DefaultValue = %s;"%(n, p.default))
            self.newline(node)
            self.write('v%s.Description = "%s";'%(n,p.description))
            self.newline(node)
            self.write("v%s.Id = 0;"%n)
            self.newline(node)
            self.write("v%s.MaxValue = %s;"%(n, p.max))
            self.newline(node)
            self.write("v%s.MinValue = %s;"%(n, p.min))
            self.newline(node)
            self.write('v%s.Name = "%s";'%(n, p.name))
            self.newline(node)
            self.write("v%s.Size = 1;"%n)
            self.newline(node)
            self.write('v%s.Units = "%s";'%(n, p.unit))
            self.newline(node)
            self.write('v%s.URL = "";'%n)
            self.newline(node)
            self.write("v%s.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;"%n)
            self.newline(node)
            self.write('v%s.ValueType = VarInfoValueTypes.GetInstanceForName("%s");'%(n, p.datatype))
            self.newline(node)
            self.write("_parameters0_0.Add(v%s);"%n)
            self.newline(node)
            n = n+1
        self.write("mo0_0.Parameters=_parameters0_0;")

        n = 1
        self.newline(extra=1)
        self.write("//Inputs")
        self.newline(node)
        self.write("List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();"%())
        self.newline(node)
        for inp in self.model.inputs:
            if inp.name not in self.modparam :
                self.write("PropertyDescription pd%s = new PropertyDescription();"%n)              
                self.newline(node)
                self.write("pd%s.DomainClassType = typeof(SiriusQuality%s.%s%s);"%(n, self.name.capitalize(),self.name.capitalize(),inp.variablecategory.capitalize()))
                self.newline(node)
                self.write('pd%s.PropertyName = "%s";'%(n,inp.name))
                self.newline(node)
                self.write('pd%s.PropertyType = ((SiriusQuality%s.%s%sVarInfo.%s)).ValueType.TypeForCurrentValue;'%(n, self.name.capitalize(),self.name.capitalize(), inp.variablecategory.capitalize(),inp.name))
                self.newline(node)
                self.write('pd%s.PropertyVarInfo =(SiriusQuality%s.%s%sVarInfo.%s);'%(n,self.name.capitalize(),self.name.capitalize(), inp.variablecategory.capitalize(),inp.name))
                self.newline(node)
                self.write('_inputs0_0.Add(pd%s);'%(n))
                self.write("")
                self.newline(node)
                n = n+1
        self.write("mo0_0.Inputs=_inputs0_0;")
    
        self.newline(extra=1)
        self.write("//Outputs")
        self.newline(node)
        self.write("List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();")
        self.newline(node)

        for out in self.model.outputs:
            if out.name not in self.modparam :
                self.write("PropertyDescription pd%s = new PropertyDescription();"%n)
                self.newline(node)
                self.write("pd%s.DomainClassType = typeof(SiriusQuality%s.%s%s);"%(n, self.name.capitalize(),self.name.capitalize(),out.variablecategory.capitalize()))
                self.newline(node)
                self.write('pd%s.PropertyName = "%s";'%(n,out.name))
                self.newline(node)
                self.write('pd%s.PropertyType = ((SiriusQuality%s.%s%sVarInfo.%s)).ValueType.TypeForCurrentValue;'%(n, self.name.capitalize(),self.name.capitalize(), out.variablecategory.capitalize(),out.name))
                self.newline(node)
                self.write('pd%s.PropertyVarInfo =(SiriusQuality%s.%s%sVarInfo.%s);'%(n,self.name.capitalize(),self.name.capitalize(), out.variablecategory.capitalize(),out.name))
                self.newline(node)
                self.write('_outputs0_0.Add(pd%s);'%(n))
                self.newline(node)
                n = n+1
            self.write("mo0_0.Outputs=_outputs0_0;")
    def otherDesc(self):
        self.write("//Associated strategies")
        self.write('List<string> lAssStrat0_0 = new List<string>();')
        self.write("mo0_0.AssociatedStrategies = lAssStrat0_0;")
        self.write("//Adding the modeling options to the modeling options manager")
        self.write("_modellingOptionsManager = new ModellingOptionsManager(mo0_0);")
        self.write("SetStaticParametersVarInfoDefinitions();")
        self.write("SetPublisherData();")
    
    def iAnnotable(self):
        pass

    def iStrategy(self):
        pass

    def instanceParam(self):
        pass

    def initParam(self):
        pass

    def varInfoParam(self):
        pass

    def preposCond(self):
        pass


    def estimate(self, node):
        self.write("public void Estimate(SiriusQuality%s.%sState s,SiriusQuality%s.%s s1,SiriusQuality%s.%sRAte r,SiriusQuality%s.%sAuxiliary a,SiriusQuality%s.%sExogenous ex,CRA.AgroManagement.ActEvents actevents)"%(self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize()))
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
        self.write("try")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1
        self.write("CalculateModel(s, s1, r, a, ex)")
        self.newline(node)
        self.indentation -= 1
        self.write("}")
        self.newline(node)
        self.write("catch (Exception exception)")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1
        self.write('string msg = "Error in component SiriusQuality%s, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;'%self.name.capitalize())				
        self.newline(node)
        self.write('throw new Exception(msg, exception);')
        self.newline(node)
        self.indentation -= 1
        self.write('}')
        self.newline(node)
        self.indentation -= 1
        self.write('}')
        self.newline(node)

    def get_set_param(self, node):
        self.write("// Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.\n")
        for arg in self.node_param : 
            self.newline(node)
            self.write("public ")
            self.visit_decl(arg.pseudo_type)
            self.write(' ' +arg.name)
            self.newline(node)
            self.write("{ ")
            self.newline(node)
            self.indentation += 1  
            self.write("get { ")
            self.newline(node)
            self.indentation += 1  
            self.write('VarInfo vi= _modellingOptionsManager.GetParameterByName("%s");'%arg.name)
            self.newline(node)
            self.write("if (vi != null && vi.CurrentValue!=null) return (")
            self.visit_decl(arg.pseudo_type)
            self.write(")vi.CurrentValue ;")
            self.newline(node)
            self.write('else throw new Exception("Parameter')
            self.write(" '%s' not found (or found null) in strategy '%s'"%(arg.name,self.model.name.capitalize()))
            self.write('");')
            self.newline(node)
            self.indentation -= 1 
            self.write('} set {')
            self.newline(node)
            self.indentation += 1
            self.write('VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");')
            self.newline(node)
            self.write('if (vi != null)  vi.CurrentValue=value;')
            self.newline(node)
            self.write('else throw new Exception("Parameter')
            self.write(" '%s' not found in strategy '%s'"%(arg.name,self.model.name.capitalize()))
            self.write('");')
            self.newline(node)
            self.indentation -= 1             
            self.write("}")
            self.newline(node)
            self.indentation -= 1    
            self.write("}")

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name     
        self.write("private void ")
        self.write(" CalculateModel(") if not node.name.startswith("init_") else self.write("Init(")
        self.write('SiriusQuality%s.%sState s, SiriusQuality%s.%sState s1, SiriusQuality%s.%sRate r, SiriusQuality%s.%sAuxiliary a, SiriusQuality%s.%sExogenous ex)'%(self.name.capitalize(), self.name.capitalize(),self.name.capitalize(),self.name.capitalize(),self.name.capitalize(), self.name.capitalize(),self.name.capitalize(),self.name.capitalize(), self.name.capitalize(),self.name.capitalize()))
        self.newline(node)
        self.write('{') 
        self.newline(node)
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
                            if arg.name in self.states and arg.name.endswith("_t1") :
                                self.write(" = s1.%s"%arg.name[:-3])
                            if arg.name in self.rates:
                                self.write(" = r.%s"%arg.name)
                            if arg.name in self.auxiliary:
                                self.write(" = a.%s"%arg.name) 
                        else:
                            if arg.pseudo_type[0] =="list":
                                self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
                            elif arg.pseudo_type[0] =="array":
                                self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                        self.write(";")                   
        self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1 
        self.write('}') 
        self.newline(node)



    def visit_module(self, node):
        self.write("namespace SiriusQuality%s.Strategies"%self.name.capitalize())
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
        self.write("public class %s : IStrategySiriusQuality%s"%(self.model.name.capitalize(), self.name.capitalize()))
        self.newline(node)
        self.write("{") 
        self.newline(node)
        self.write("#region Constructor")
        self.newline(node)
        self.indentation += 1 
        self.write("public %s()"%self.model.name.capitalize())  
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1        
        self.inOutputDesc(node)
        self.newline(node)
        self.indentation -= 1 
        self.write("}")

        self.newline(extra=1)        
        self.write("private ModellingOptionsManager _modellingOptionsManager;")
        self.newline(node)	
        self.write("public ModellingOptionsManager ModellingOptionsManager")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation += 1 
        self.write("get { return _modellingOptionsManager; } ")
        self.newline(node)
        self.indentation -= 1            
        self.write("}")

        self.newline(extra=1)
        self.get_set_param(node)

        self.newline(extra=1)
        self.estimate(node)

        self.visit(node.body)
        self.newline(node)
        self.indentation -= 1        # class
        self.newline(node)
        self.write("}")   
        self.indentation -= 1        # namespace
        self.newline(node)
        self.write("}")               


class SiriusTrans(CsharpTrans):
    """ This class used to generates states, rates and auxiliary classes
    for Sirius.
    """
    
    def __init__(self, models):
        self.models = models
        CsharpTrans.__init__(self, self.models)

def to_struct_sirius(models, rep, name):
    generator = CsharpTrans(models)
    generator.result=[u"using System;\nusing System.Collections.Generic;\n"]
    generator.model2Node()
    states = generator.node_states
    generator.generate(states, "%sState"%name.capitalize())
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sState.cs"%name.capitalize()))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))
    rates = generator.node_rates
    generator.result=[u"using System;\nusing System.Collections.Generic;\n"]
    generator.generate(rates, "%sRate"%name.capitalize())
    z1= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sRate.cs"%name.capitalize()))
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))       
    auxiliary = generator.node_auxiliary
    generator.result=[u"using System;\nusing System.Collections.Generic;\n"]
    generator.generate(auxiliary, "%sAuxiliary"%name.capitalize())
    z2= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sAuxiliary.cs"%name.capitalize()))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))
    return 0



''' Csharp composite'''


class SiriusCompo(CsharpCompo):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree=None, model=None, name=None):
        self.model=model
        self.tree = tree
        self.name = name
        CsharpCompo.__init__(self, tree, model, name)

    def visit_module(self, node): 
        self.write("namespace SiriusModel.Model.Strategies") 
        self.newline(node)
        self.write("{") 
        self.indentation += 1 
        self.newline(node)               
        self.write("public class %sComponent"%self.model.name.capitalize())
        self.newline(node)
        self.write("{") 
        self.newline(node)
        self.indentation += 1     
        self.visit(node.body)
        self.newline(node)
        if "function" in dir(self.model) and self.model.function:
            func_name = os.path.split(self.model.function[0].filename)[1]
            func_path = os.path.join(self.model.path,"src","pyx", func_name)
            func_tree=parser(Path(func_path))  
            newtree = AstTransformer(func_tree, func_path)
            dictAst = newtree.transformer()
            nodeAst= transform_to_syntax_tree(dictAst)
            self.model=None
            self.visit(nodeAst.body)
        self.indentation -= 1        
        self.newline(node)
        self.write("}") 
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}") 

    def wrapper(self):
        self.write("using SQCrop2ML_%s.DomainClass;"%self.model.name.capitalize())
        self.newline(1)
        self.write("using SQCrop2ML_%s.Strategies;"%self.model.name.capitalize())
        self.newline(extra=1)
        self.write("namespace SiriusModel.Model.%s"%self.model.name.capitalize())
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1         
        self.write("class %sWrapper :  UniverseLink"%self.model.name.capitalize())
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
        self.write("public %sWrapper(Universe universe) : base(universe)"%(name.capitalize()))
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write("s = new %sState();"%(name.capitalize()))
        self.newline(1)
        self.write("r = new %sRate();"%(name.capitalize()))
        self.newline(1)
        self.write("a = new %sAuxiliary();"%(name.capitalize()))
        self.newline(1)
        self.write("%sComponent = new %s();"%(name.lower(), name.capitalize()))
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")


    def copyconstrWrap(self):
        self.write("public %sWrapper(Universe universe, %sWrapper toCopy, bool copyAll) : base(universe)"%(self.model.name.capitalize(),self.model.name.capitalize()))
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("s = (toCopy.s != null) ? new %sState(toCopy.s, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.newline(1)
        self.write("r = (toCopy.r != null) ? new %sRate(toCopy.r, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.write("a = (toCopy.a != null) ? new %sAuxiliary(toCopy.a, copyAll) : null;"%(self.model.name.capitalize()))
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write("%sComponent = (toCopy.%sComponent != null) ? new %s(toCopy.%sComponent) : null;"%(self.model.name.lower(),self.model.name.lower(),self.model.name.capitalize(),self.model.name.lower()))
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

def to_wrapper_sirius(models, rep, name):
    generator = SiriusCompo(model = models)
    generator.result=[u"using System;\nusing System.Collections.Generic;\nusing System.Linq;\n"]
    generator.model2Node()
    generator.wrapper()
    z= ''.join(generator.result)
    filename = Path(os.path.join(rep, "%sWrapper.cs"%name.capitalize()))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    return 0