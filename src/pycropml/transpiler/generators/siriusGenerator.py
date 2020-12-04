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
                

    def usingBioma(self):
        self.write("""
using System;
using System.Collections.Generic;
using System.Xml;
using System.Linq;
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

    
    def inOutputDesc(self, inout):
        """
        self.write("List<PropertyDescription> _%s0_0 = new List<PropertyDescription>();"%())
        self.write("PropertyDescription pd%s = new PropertyDescription();")
        self.write("pd%s.DomainClassType = typeof(%s.%s%s);"%())
        self.write('pd%s.PropertyName = "%s";'%())
        self.write('pd%s.PropertyType = (( %s.%s%sVarInfo.%s)).ValueType.TypeForCurrentValue;'%())
        self.write('pd%s.PropertyVarInfo =( %s.%s%sVarInfo.%s);'%())
        self.write('_%s0_0.Add(pd%s);'%())"""

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


    def estimate(self):
        self.write("public void Estimate(SiriusQualityEnergyBalanceDomainClass.EnergyBalanceState energybalancestate,SiriusQualityEnergyBalanceDomainClass.EnergyBalanceState energybalancestate1,SiriusQualityEnergyBalanceDomainClass.EnergyBalanceExogenous energybalanceexogenous,CRA.AgroManagement.ActEvents actevents)")
        self.write("{")
        self.write("try")
        self.write("{")
        self.write("CalculateModel(energybalancestate,energybalancestate1,energybalanceexogenous,actevents);")
        self.write("}")
        self.write("catch (Exception exception)")
        self.write("{")
        self.write('string msg = "Error in component SiriusQualityEnergyBalance, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;')				
        self.write('throw new Exception(msg, exception);')
        self.write('}')
        self.write('}')




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