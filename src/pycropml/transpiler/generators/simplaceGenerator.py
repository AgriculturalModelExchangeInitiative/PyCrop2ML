from pycropml.transpiler.generators.javaGenerator import JavaGenerator
from copy import deepcopy

class SimplaceGenerator(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)
        self.parameters_ = deepcopy(self.model.parameters)
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
        self.write("import java.time.LocalDateTime;\n")
        self.write("import net.simplace.sim.model.FWSimComponent;\n")
        self.write("import net.simplace.sim.util.FWSimVarMap;\n")
        self.write("import net.simplace.sim.util.FWSimVariable;\n")
        self.write("import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;\n")
        self.write("import net.simplace.sim.util.FWSimVariable.DATA_TYPE;\n")
        self.write("import org.jdom.Element;\n")


    def simplaceVarDeclaration(self, node, elem):
        for va in elem:
            z =  "private " + cymlSimplaceType[va.datatype] + " " + va.name + ";"
            self.newline(node)
            self.write(z)

    def visit_module(self, node):
        self.importSimplace(node)
        self.newline(extra = 1)
        self.write("public class %s extends FWSimComponent"%self.model.name.capitalize())
        self.newline(node)
        self.write("{") 
        self.newline(node)
        self.indentation += 1
        self.simplaceVarDeclaration(node, self.model.parameters) 
        self.simplaceVarDeclaration(node, self.inputs_) 
        self.simplaceVarDeclaration(node, self.outputs_)
        self.simplaceVarDeclaration(node, self.model.states)
        self.simplaceVarDeclaration(node, self.model.rates)
        self.newline(node)
        self.constructorWithParam(node)
        self.newline(node)
        self.constructorWithoutParam(node)
        self.newline(node)
        self.visit(node.body)
        self.noInit(node)
        self.newline(node)
        self.clone(node)
        self.newline(node)
        self.hashMap(node)
        self.newline(node)
        self.indentation -= 1 
        self.write("}") 


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            if n.name not in self.var:
                self.newline(node)
                if 'value' not in dir(n) and n.type not in ("list", "tuple", "dict", "array"):
                    self.write(self.types[n.pseudo_type])
                    self.write(' %s;'%n.name) 
                if 'elements' not in dir(n) and n.type in ("list","array"):
                    if n.type=="list":
                        self.write("List<%s> %s = new ArrayList<>(Arrays.asList());"%(self.types2[n.pseudo_type[1]],n.name))
                    if n.type=="array":
                        self.write(self.types[n.type]%(self.types2[n.pseudo_type[1]], n.name, self.types2[n.pseudo_type[1]]))
                        self.write('[')
                        self.visit(n.elts)
                        self.write('];')
                if 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                    self.write("%s %s"%(self.types[n.type], n.name))
                    self.write(" = ")
                    if n.type=="local":
                        self.write(n.value)
                    else: self.visit(n)
                    self.write(";")
                elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                    if n.type=="list":
                        self.visit_decl(n.pseudo_type)
                        self.write(n.name)
                        self.write(" = new ArrayList <>(Arrays.asList") 
                    if n.type=='tuple':
                        pass
                    self.write(u'(')
                    self.comma_separated_list(n.elements)
                    self.write(u'));')           
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
                        if arg.type=="list": self.write("%s.setValue(t%s.toArray(new %s[0]), this);"%(arg.name,arg.name,self.types2[arg.pseudo_type[1]] ))
                        else: self.write("%s.setValue(t%s, this);"%(arg.name,arg.name ))
                        self.newline(node)

    def visit_local(self, node):
        if node.name in self.var:
            return self.write("t%s"%node.name)
        else: self.write(node.name)

    def visit_function_definition(self, node):
        self.newline(node)
        self.funcname = node.name
        self.newline(node)
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            if node.name=="main":
                self.write("public static void main(String[] args)") 
            else:
                self.write("public static ")
                self.visit_decl(node.return_type) if node.return_type else self.write("void")
                self.write(" %s("%node.name)
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
            self.write("@Override")
            self.newline(node)
            self.write("protected void process()") if node.name.startswith("model_") else self.write("protected void init()")
            self.newline(node)
            self.write('{')
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("IN"):
                        self.newline(1)
                        if self.model :
                            self.visit_decl(arg.pseudo_type)
                            self.write(" t")
                            self.write(arg.name)
                            if arg.type=="list": self.write(" = Arrays.asList(%s.getValue());" % arg.name)
                            else: self.write(" = %s.getValue();" % arg.name)
                    elif arg.feat!="INOUT":
                            self.newline(1)
                            self.visit_decl(arg.pseudo_type)
                            self.write(" t")
                            self.write(arg.name)
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
    
    def constructorWithParam(self, node):
        self.newline(extra = 1)
        self.write("public %s(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)"%self.model.name.capitalize())
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
        self.write("public %s()"%self.model.name.capitalize())
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
        self.write("return new %s(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);"%self.model.name.capitalize())
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
        self.addVar(node,"c",self.parameters_, "constant" )
        self.addVar(node,"i",self.inputs_, "input" )
        self.addVar(node,"",self.outputs_, "out" )
        self.addVar(node,"s",self.states_, "state" )
        self.addVar(node,"r", self.rates_, "rate" )
        self.newline(extra=1)               
        self.write("return iFieldMap;")
        self.newline(node)
        self.indentation-=1
        self.write("}")

    def addVar(self,node,prefix,elem, ztype ):
        for inp in elem:
            self.newline(node)
            if inp.min is not None: 
                if inp.min.strip() =="": zmin = "null" 
                else: zmin = transf(inp.datatype, inp.min)
            else: zmin = "null"
            if inp.max is not None: 
                if inp.max.strip() =="": zmax = "null" 
                else: zmax = transf(inp.datatype, inp.max)
            else: zmax = "null"
            if "default" in dir(inp): 
                if inp.default is not None and inp.default.strip() =="": zmin = "null" 
                elif inp.default: zdefault = transf(inp.datatype, inp.default)
            else: zdefault="null"
            if inp.datatype.startswith("DATE"): zmin, zmax,zdefault= "null", "null", "null"
            self.write('addVariable(FWSimVariable.createSimVariable("%s%s", "%s", DATA_TYPE.%s, CONTENT_TYPE.%s,"", %s, %s, %s, this));'%(prefix,inp.name, inp.description,DATA_TYPE[inp.datatype],ztype, zmin, zmax, zdefault))
            self.newline(node)     

class SimplaceCompo(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)

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

def transfDouble(type_v,elem):
    return str(elem)   
def transfString(type_v, elem): 
    return ('"%s"'%elem).replace('""', '"')
def transfList(type_v, elem):
    res = ",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),elem )))
    return "new %s[] {%s}"%(cymltype[type_v.split("LIST")[0]],res)
def transfArray(type_v, elem):
    res = ",".join(list(map(transf,[type_v.split("ARRAY")[0]]*len(elem),elem )))
    return "new %s[] {%s}"%(cymltype[type_v.split("LIST")[0]],res)
def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.lower()
    if type_v=="DOUBLE":
        return transfDouble(cymltype[type_v], elem)
    elif type_v in ("STRING", "DATE"):
        return transfString(cymltype[type_v], elem)
    elif type_v=="INT":
        return str(elem)
    elif type_v in ("STRINGLIST","DOUBLELIST","INTLIST", "DATELIST"):
        return transfList(type_v,eval(elem))
    elif type_v in ("STRINGARRAY","DOUBLEARRAY","INTARRAY", "DATEARRAY"):
        return transfArray(type_v,eval(elem))

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