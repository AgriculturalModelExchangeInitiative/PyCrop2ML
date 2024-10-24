from pycropml.transpiler.generators.javaGenerator import JavaGenerator, Custom_call
from copy import deepcopy
import os
import six
from pycropml.transpiler.antlr_py.toxml import Namespace
import os
from path import Path
from pycropml.nameconvention import signature2
from pycropml.transpiler.pseudo_tree import Node

class SimplaceGenerator(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)
        self.parameters_ = deepcopy(self.model.parameters)
        self.par_ = [p.name for p in self.parameters_ ]
        self.inputs_ = [inp for inp in self.model.inputs if ("variablecategory" in dir(inp) and inp.variablecategory=="auxiliary" )]
        self.outputs_ = [out for out in self.model.outputs if ("variablecategory" in dir(out) and out.variablecategory=="auxiliary" )]
        self.inputs = [inp.name for inp in self.model.inputs]
        self.outputs = [out.name for out in self.model.outputs]
        self.var = self.inputs+self.outputs
        self.states_, self.statesName_=[], []
        self.states = deepcopy(self.model.states)
        for s in self.states:
            if s.name.endswith("_t1") and s.name[:-3] not in self.statesName_: 
                s.name = s.name[:-3]
                self.states_.append(s)
                self.statesName_.append(s.name)
            elif s.name not in self.statesName_: 
                self.states_.append(s)
                self.statesName_.append(s.name)
        self.rates_ = self.model.rates


    def importSimplace(self, node):
        self.write(u"import  java.io.*;\nimport  java.util.*;\nimport java.text.ParseException;\nimport java.text.SimpleDateFormat;\nimport java.time.LocalDateTime;\n")
        self.write("import net.simplace.sim.model.FWSimComponent;\n")
        self.write("import net.simplace.sim.util.FWSimVarMap;\n")
        self.write("import net.simplace.sim.util.FWSimVariable;\n")
        self.write("import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;\n")
        self.write("import net.simplace.sim.util.FWSimVariable.DATA_TYPE;\n")
        self.write("import org.jdom2.Element;\n")


    def simplaceVarDeclaration(self, node, elem):
        listvar = []
        for va in elem:
            if va.name not in listvar:
                z =  "private " + cymlSimplaceType[va.datatype] + " " + va.name + ";"
                self.newline(node)
                self.write(z)
                listvar.append(va.name)

    def visit_module(self, node):
        package = self.model.path.split(os.sep)[-1]
        self.module = node
        self.extfuncs = []
        self.write(f"package net.simplace.sim.components.{package};")
        self.newline()
        self.importSimplace(node)
        self.newline(extra = 1)
        self.write("public class %s extends FWSimComponent"%signature2(self.model))
        self.newline(node)
        self.write("{") 
        self.newline(node)
        self.indentation += 1
        #self.simplaceVarDeclaration(node, self.model.parameters) 
        #self.simplaceVarDeclaration(node, self.inputs_) 
        #self.simplaceVarDeclaration(node, self.outputs_)
        #self.simplaceVarDeclaration(node, self.model.states)
        #self.simplaceVarDeclaration(node, self.model.rates)
        self.simplaceVarDeclaration(node, self.model.inputs + self.model.outputs)
        self.newline(node)
        self.constructorWithParam(node)
        self.newline(node)
        self.constructorWithoutParam(node)
        self.newline(node)
        self.hashMap(node)
        self.newline(node)
        self.visit(node.body)
        self.noInit(node)
        self.newline(node)
        self.unittest(node)
        self.clone(node)
        self.newline(node)
        self.indentation -= 1 
        self.write("}") 
        self.newline(node)
        for ext in self.extfuncs:
            self.translate_final_class(ext)   


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            if n.name not in self.var or not self.ismodel:
                self.newline(node)
                if 'value' not in dir(n) and n.type not in ("list", "tuple", "dict", "array"):
                    self.write(self.types[n.pseudo_type])
                    self.write(' %s%s;'%("t_" if n.name in self.var else "", n.name) )
                elif 'elements' not in dir(n) and n.type in ("list","array"):
                    if n.type=="list":
                        self.write("List<%s> %s%s = new ArrayList<>(Arrays.asList());"%("t_" if n.name in self.var else "",self.types2[n.pseudo_type[1]],n.name))
                    if n.type=="array":
                        self.write(self.types[n.type]%(self.types2[n.pseudo_type[1]], n.name))
                        if n.elts:
                            self.write(f" = new {self.types2[n.pseudo_type[1]]}")
                            for n in n.elts: 
                                self.write('[')
                                self.visit(n)
                                self.write(']')
                        self.write(";")
                elif 'value' in dir(n) and n.value is not None and n.type in ("int", "float", "str", "bool"):
                    self.write("%s %s"%(self.types[n.type], n.name))
                    self.write(" = ")
                    if n.type=="local":
                        self.write(n.value)
                    else: self.visit(n.value) if isinstance(n.value, Node) else self.write(n.value)
                    self.write(";")
                elif 'elements' in dir(n) and n.type in ("list", "tuple", "array"):
                    if n.type=="list":
                        self.visit_decl(n.pseudo_type)
                        self.write(n.name)
                        self.write(" = new ArrayList <>(Arrays.asList") 
                        self.write(u'(')
                        self.comma_separated_list(n.elements)
                        self.write(u'));') 
                    elif n.type=='tuple':
                        pass
                    elif n.type=="array":
                        self.visit_decl(n.pseudo_type)
                        self.write(n.name)
                        self.write(" = ")  
                        self.write(u'{')
                        self.comma_separated_list(n.elements)
                        self.write(u'};')           
                elif  n.type=='datetime':
                    self.newline(node)
                    self.write("Date")
                    self.write(n.name)                 
                elif 'pairs' in dir(n) and n.type=="dict":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)
                    self.write(" = new ") 
                    self.visit_decl(n.pseudo_type)               
                    self.write(u'{')
                    self.comma_separated_list(n.pairs)
                    self.write(u'};')
                    
            self.newline(node)
   
    def visit_return(self, node):
        if self.model:
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("OUT", "INOUT"):
                        if arg.type=="list": self.write("%s.setValue(t_%s.toArray(new %s[0]), this);"%(arg.name,arg.name,self.types2[arg.pseudo_type[1]] ))
                        else: self.write("%s.setValue(t_%s, this);"%(arg.name,arg.name ))
                        self.newline(node)

    def visit_local(self, node):
        if node.name in self.var:
            return self.write("t_%s"%node.name)
        else: self.write(node.name)


    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            self.write("_%s.Calculate_%s(s, s1, r, a, ex);"%(name.capitalize(), name))
            self.newline(node)
        else:
            self.newline(node)
            if "index" in dir(node.target) and node.target.sequence.pseudo_type[0]=="list": 
                self.write(node.target.sequence.name)
                self.write(".set(")
                self.visit(node.target.index)
                self.write(',')
                self.visit(node.value)
                self.write(");")
                self.newline(node)
            elif node.value.type == "standard_call" and node.value.function=="integr":
                self.write("%s = new ArrayList<>(%s);"%(node.target.name,node.value.args[0].name))
                self.newline(node)
                if isinstance(node.value.args[1].pseudo_type, list):
                    self.write("%s.addAll("%node.target.name)
                else: self.write("%s.add("%node.target.name)
                self.visit( node.value.args[1])
                self.write(");")
            elif node.value.type == "standard_call" and node.value.function=="datetime":
                self.newline(node)
                if len(node.value.args)==3:node.value.args.extend([00,00,00])
                self.write(" %s = LocalDateTime.of(%s);"%(node.target.name,",".join(node.value.args)))
                self.newline(node)
            elif node.value.type =="standard_method_call" and node.value.message in ["keys", "values"]:
                self.write(node.target.name)
                self.write(".addAll(")
                self.visit(node.value)
                self.write(");")
                self.newline(node)     
            elif node.value.type=="array" and "elements" in dir(node.value):
                if isinstance(node.value.elements, Node):
                    self.write("Arrays.fill(")
                    self.visit(node.target)
                    self.write(", ")
                    self.visit(node.value.elements.left.elements[0])  
                    self.write(");")  
                else:
                    self.visit(node.target)
                    self.write(' = ')
                    self.write("new %s[] "%self.types2[node.value.pseudo_type[1]])
                    self.write(u'{')
                    self.comma_separated_list(node.value.elements)
                    self.write(u'};') 
            elif node.value.type=="custom_call" and isinstance(node.value.pseudo_type, list) and node.value.pseudo_type[0]=="tuple":

                self.write(f'zz_{node.value.function} = Calculate_{node.value.function}(')
                self.comma_separated_list(node.value.args)
                self.write(");")
                self.meta = Custom_call(self.module)
                r = self.meta.process(node)
                if node.value.function in self.meta.extern:
                    func = self.meta.extern[node.value.function]
                    outs = [n.name for n in func.block[-1].value.elements]
                    for k,out in enumerate(outs):
                        self.newline(node)
                        if node.target.elements[k].name in self.var: self.write("t_")
                        self.write(f'{node.target.elements[k].name} = zz_{node.value.function}.get{out}();')
                        
            elif node.value.type=="none":
                pass
                              
            else:
                self.visit(node.target)
                self.write(' = ')
                self.visit(node.value) 
                self.write(";")
                self.newline(node)
                
                

    def visit_function_definition(self, node):
        self.newline(node)
        self.funcname = node.name
        self.meta = Custom_call(self.module)
        r = self.meta.process(node)
        self.newline(node)
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.ismodel=False
            if node.name=="main":
                self.write("public static void main(String[] args)") 
            else:
                if node.return_type[0]=="tuple":
                    self.extfuncs.append(node)
                    self.extfunc = node
                    self.write(f"public {node.name} Calculate_{node.name} (")   
                else:  
                    self.write("public static ")
                    self.visit_decl(node.return_type) if node.return_type else self.write("void")
                    self.write(" %s("%node.name)
                for i, pa in enumerate(node.params):
                    self.visit_decl(pa.pseudo_type)
                    if pa.name in self.var: self.write(f" t_{pa.name}")
                    else:self.write(" %s"%pa.name)
                    if i!= (len(node.params)-1):
                        self.write(', ')
                self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
            self.indentation+=1
        else:
            self.ismodel=True
            self.meta = Custom_call(self.module)
            r = self.meta.process(node)
            self.write("@Override")
            self.newline(node)
            self.write("protected void process()") if node.name.startswith("model_") else self.write("protected void init()")
            self.newline(node)
            self.write('{')
            self.newline(node)
            self.indentation += 1
            if self.meta.extern:
                for j,k in self.meta.extern.items():
                    self.write(f"{j} zz_{j};")
                    self.newline(node)
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("IN") or (node.name.startswith("model_") and arg.feat=="INOUT"):
                        self.newline(1)
                        if self.model :
                            self.visit_decl(arg.pseudo_type)
                            self.write(" t_")
                            self.write(arg.name)
                            if arg.type=="list": self.write(" = Arrays.asList(%s.getValue());" % arg.name)
                            else:
                                #if arg.type == "array" and "elts" in dir(arg) and len(arg.elts)>0 and arg.name not in self.par_ :
                                '''self.write(" = new ")
                                    self.visit_decl(arg.pseudo_type[1])
                                    self.write("[")
                                    self.visit(arg.elts[0])
                                    self.write("];")'''
                                #else:
                                self.write(" = %s.getValue();" % arg.name)
                    elif arg.feat!="INOUT":
                            self.newline(1)
                            self.visit_decl(arg.pseudo_type)
                            self.write(" t_")
                            self.write(arg.name)
                            if node.name.startswith("init"):
                                if arg.type == "array" and "elts" in dir(arg):
                                    if len(arg.elts)>0:
                                        self.write(" = new ")
                                        self.visit_decl(arg.pseudo_type[1])
                                        self.write("[")
                                        self.visit(arg.elts[0])  
                                        self.write("]")
                                    else: self.write(" = %s.getValue();" % arg.name)
                                else: self.write(f" = {arg.name}.getDefault()")
                            self.write(";")
        self.indentation -= 1
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1
        self.write('}')
        self.newline(node)


    def visit_import(self, node):
        return
    
    def unittest(self, node):
        m = self.model
        type_in = {inp.name: inp.datatype for inp in m.inputs}
        type_out = {out.name: out.datatype for out in m.outputs}
        self.write(f"public HashMap<String, FWSimVariable<?>> fillTestVariables(int aParamIndex, TEST_STATE aDefineOrCheck)")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation+=1
        psets = m.parametersets
        for v_tests in m.testsets:

            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

            # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknown parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)
                num = 0
                for each_run in test_runs :
                    self.write(f"if(aParamIndex == {num} && aDefineOrCheck == TEST_STATE.DEFINE) //before process")
                    self.newline(1)
                    self.write("{")
                    self.newline(1)
                    self.indentation+=1
                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        self.write(f'FWSimVariable.setValue({transf(type_in[k],v)}, iFieldMap.get("{self.model.name}.{k}"), this);')
                        self.newline()
                    
                    self.indentation-=1
                    self.write("}")
                    self.newline(node)
                    
                    
                    self.write(f"else if(aParamIndex ==  {num} && aDefineOrCheck == TEST_STATE.CHECK) //after process")
                    self.newline(1)
                    self.write("{")	
                    self.newline(1)	
                    self.indentation+=1	

                    for k, v in six.iteritems(outs):
                        self.write(f'FWSimVariable.setValue({transf(type_out[k],v[0])}, iFieldMap.get("{self.model.name}.{k}"), this);')
                        self.newline()
                    
                    self.indentation-=1
                    self.write("}")
                    self.newline(node)
                    self.write("else return null;")
                    self.newline(node)
                    num = num+1
                    self.newline(1)
                    
        self.write("return iFieldMap;")
        self.newline(1)
        self.indentation-=1
        self.write("}")
    
    def constructorWithParam(self, node):
        self.newline(extra = 1)
        self.write("public %s(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)"%signature2(self.model))
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation+=1
        self.write("super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);")
        self.newline(node)
        self.indentation-=1
        self.write("}")

    def constructorWithoutParam(self, node):
        self.newline(extra = 1)
        self.write("public %s()"%signature2(self.model))
        self.write("{")
        self.newline(node)
        self.indentation+=1
        self.write("super();")
        self.newline(node)
        self.indentation-=1
        self.write("}")
    
    def noInit(self, node):
        self.newline(extra = 1)
        if not self.model.initialization:
            self.write("@Override")
            self.newline(node)
            self.write("protected void init()")
            self.newline(node)
            self.write("{")
            self.newline(node)
            self.write("}") 
        else:
            pass  

    def clone(self, node):
        self.newline(extra = 1)
        self.write("@Override")
        self.newline(node)
        self.write("protected FWSimComponent clone(FWSimVarMap aVarMap)")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation+=1
        self.write("return new %s(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);"%signature2(self.model))
        self.newline(node)
        self.indentation-=1
        self.write("}")

    def hashMap(self, node):
        self.newline(extra = 1)
        self.write("@Override")
        self.newline(node)
        self.write("public HashMap<String, FWSimVariable<?>> createVariables()")
        self.newline(node)
        self.write("{")
        self.newline(node)
        self.indentation+=1
        self.addVar(node,self.model.inputs + self.model.outputs )
        self.newline(extra=1)               
        self.write("return iFieldMap;")
        self.newline(node)
        self.indentation-=1
        self.write("}")

    def addVar(self,node,elem):
        vars = []
        for inp in elem:
            if inp.name not in vars:
                if hasattr(inp, "parametercategory"):
                    ztype = "constant"
                elif hasattr(inp, "variablecategory") and hasattr(inp, "inputtype") and inp.variablecategory in ["auxiliary", "exogenous"]:
                    ztype = "input"
                elif hasattr(inp, "variablecategory") and inp.variablecategory == "state":
                    ztype = "state"
                elif hasattr(inp, "variablecategory") and inp.variablecategory == "rate":
                    ztype = "rate"
                elif hasattr(inp, "variablecategory") and not hasattr(inp, "inputtype") and inp.variablecategory == "auxiliary":
                    ztype = "out"

                vars.append(inp.name)
                
                self.newline(node)
                zmin = transf(inp.datatype, inp.min) if (hasattr(inp, "min") and inp.min) else "null"
                zmax = transf(inp.datatype, inp.max) if (hasattr(inp, "max") and inp.max) else "null"
                zdefault = transf(inp.datatype, inp.default) if hasattr(inp, "default") else  transf(inp.datatype, "") 
                unit = inp.unit

                if inp.datatype.startswith("DATE"): zmin, zmax,zdefault= "null", "null", "null"
                self.write('addVariable(FWSimVariable.createSimVariable("%s", "%s", DATA_TYPE.%s, CONTENT_TYPE.%s,"%s", %s, %s, %s, this));'%(inp.name, inp.description,DATA_TYPE[inp.datatype],ztype,unit, zmin, zmax, zdefault))
                self.newline(node) 
    




class SimplaceCompo(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)
    
    def visit_module(self, node):
        xml_ = Pl2Crop2ml(self.model, "Simplace.SoilTemp").run_simplace()             
        filename = os.path.join(self.model.model[0].path,  "src", "simplace",  self.model.path, "%s.xml"%(self.model.name)) # "unit.%s.xml"%(strat.basename().split(".")[0])
        with open(filename, "wb") as xml_file:
            r = '<?xml version="1.0" encoding="UTF-8"?>\n'
            r += '<!DOCTYPE configuration PUBLIC "-//SIMPLACE/DTD GRP 1.0//EN" "http://simplace.net/dtd/GroupComponent.dtd">\n'
            r += xml_.unicode(indent=4)#.encode('utf-8')
            xml_file.write(r.replace("Class", "class").encode())
        
    


class ns(Namespace):
    "Custom xml namespace"

class Pl2Crop2ml(object):
    """ Export a platform component into a Crop2ML ModelUnit.

    """
    def __init__(self, md, pkgname):
        """ Export a workflow into Crop.

        :Parameters:
          - md : A platform component metainformation

        """
        self.md = md
        self.pkgname = pkgname 
    
    def run_simplace(self):
        md = self.md
        package = md.path.split(os.sep)[-1]
        
        xml = ns.configuration(Class=f"net.simplace.sim.components.{package}.{md.name}")
        
        simg = ns.simgroup()
        print(md.ord)     
        for num, m in enumerate(md.ord):
            mod = []
            m_inps = [k  for k in md.inputlink if k["target"].split(".")[0]==m ]
            m_outs = [k  for k in md.outputlink if k["source"].split(".")[0]==m ]
            m_inters = [k  for k in md.internallink if k["target"].split(".")[0]==m ]
            
            for in_ in m_inps:
                in_n = in_["source"]
                id = in_["target"].split(".")[-1]
                if in_n.endswith("_t1"): in_n = in_n[:-3]
                
                r = check_model_output(in_n, md.ord[num+1:], md.model)
                if in_n not in r:
                    mod.append(ns.input(id = id, source=f"{md.name}.{in_n}"))
                else:
                    mod.append(ns.input(id = id, source=f"{r[in_n]}.{in_n}"))
            
            for inter_ in m_inters:
                source_m, source_o = inter_["source"].split(".")
                id = inter_["target"].split(".")[-1]
                mod.append(ns.input(id = id, source=f"{source_m}.{source_o}"))
                    
            for out_ in m_outs:
                id =  out_["source"].split(".")[-1]
                out_n = out_["target"]
                mod.append(ns.output(id = id, destination=f"{md.name}.{out_n}"))     
                 
            simg.append(ns.simcomponent(mod, id=m, Class=f"net.simplace.sim.components.{package}.{m}"))
        xml.append(simg)
        return xml

    
    
def check_model_output(outname, ord, models):
    r = {}
    for o in ord:
        for m in models:
            if o == m.name :
                outnames = [i.name for i in m.outputs]
                if outname in outnames:
                    r = {outname:m.name} 
    return r
        
    
    
    
    
    

cymltype={
"INT": "Integer",
"DOUBLE": "Double",
"STRING": "String",
"BOOLEAN":"Boolean",
"DATE":"LocalDateTime"}

cymlSimplaceType = {
"INT": "FWSimVariable<Integer>",
"DOUBLE": "FWSimVariable<Double>",
"STRING": "FWSimVariable<String>",
"BOOLEAN":"FWSimVariable<Boolean>",
"DATE":"FWSimVariable<LocalDateTime>",
"STRINGARRAY":"FWSimVariable<String[]>",
"INTARRAY":"FWSimVariable<Integer[]>",
"DOUBLEARRAY":"FWSimVariable<Double[]>",
"BOOLEANARRAY":"FWSimVariable<Boolean[]>",
"DATEARRAY":"FWSimVariable<LocalDateTime[]>",
"INTLIST":"FWSimVariable<Integer[]>",
"DATELIST":"FWSimVariable<LocalDateTime[]>",
"DOUBLELIST":"FWSimVariable<Double[]>",
"STRINGLIST":"FWSimVariable<String[]>",
"BOOLEANLIST":"FWSimVariable<Boolean[]>",
}
DATA_TYPE = {
"INT": "INT",
"DOUBLE": "DOUBLE",
"STRING": "CHAR",
"BOOLEAN":"BOOLEAN",
"DATE":"DATE",
"STRINGARRAY":"CHARARRAY",
"INTARRAY":"INTARRAY",
"DOUBLEARRAY":"DOUBLEARRAY",
"BOOLEANARRAY":"BOOLEANARRAY",
"DATEARRAY":"CHARARRAY",
"INTLIST":"INTARRAY",
"DATELIST":"CHARARRAY",
"DOUBLELIST":"DOUBLEARRAY",
"STRINGLIST":"CHARARRAY",
"BOOLEANLIST":"BOOLEANARRAY",
}


def transfInt(type_v,elem):
    if isinstance(elem, str) and elem.strip() =="": return "null"
    return str(elem)

def transfDouble(type_v,elem):
    if isinstance(elem, str) and elem.strip() =="": return "null"
    return str(elem)   

def transfString(type_v, elem): 
    if isinstance(elem, str) and elem.strip() =="": return 'null'
    return ('"%s"'%elem).replace('""', '"')

def transfList(type_v, elem):
    if isinstance(elem, str) and elem.strip() =="": return 'null'
    elem = eval(elem)
    if isinstance(elem, int) or isinstance(elem, float): return "null"
    res = ",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),elem )))
    return "new %s[] {%s}"%(cymltype[type_v.split("LIST")[0]],res)

def transfArray(type_v, elem):
    if isinstance(elem, str) and elem.strip() =="": return 'null'
    elif isinstance(eval(elem), list):
        elem =eval(elem)
        res = ",".join(list(map(transf,[type_v.split("ARRAY")[0]]*len(elem),elem )))
        return "new %s[] {%s}"%(cymltype[type_v.split("ARRAY")[0]],res)
    else:
        return str(elem)


def transf(type_v, elem):
   
    if type_v == "BOOLEAN":
        return elem.lower()
    if type_v=="DOUBLE":
        return transfDouble(cymltype[type_v], elem)
    elif type_v in ("STRING", "DATE"):
        return transfString(cymltype[type_v], elem)
    elif type_v=="INT":
        return transfInt(cymltype[type_v], elem)
    elif type_v.endswith("LIST"):
        return transfList(type_v,elem)
    elif type_v.endswith("ARRAY"):
        return transfArray(type_v,elem)

def transfDate(categ,name, elem):
    return """
        try{
            %s.set%s(format.parse("%s"));
        }
        catch (ParseException e){
        }
"""%(categ,name, elem)

def transfDateList(categ,name, elem):
    return """
        try{
            %s.set%s(new ArrayList<>(Arrays.asList(%s)));
        }
        catch (ParseException e){
        }
"""%(categ, name, formatDateList(elem))

def formatDate(elem):
    return 'format.parse("%s")'%elem
def formatDateList(elem):
    t=[]
    for el in eval(elem):
        t.append(formatDate(str(el)))
    return ','.join(t)