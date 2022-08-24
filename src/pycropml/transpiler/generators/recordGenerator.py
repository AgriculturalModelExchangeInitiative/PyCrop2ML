#  -*- coding: utf-8 -*-
from pycropml.transpiler.generators.cppGenerator import CppGenerator, CppCompo
import os


class RecordGenerator(CppGenerator):
    """ This class contains the specific properties of
    Rceord and use the NodeVisitor to generate a vle
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        CppGenerator.__init__(self, tree, model, name)
        if model: 
            self.var = [m.name for m in self.model.states + self.model.rates + self.model.auxiliary]
            self.parameters = [m.name for m in self.model.parameters]
            o = [l.name for l in self.model.outputs]
            s = self.model.states + self.model.rates + self.model.auxiliary
            self.st_ext = []
            self.st_int = []
            for j in s:
                if j.name not in o:
                    self.st_ext.append(j)
                else: self.st_int.append(j) 

    def visit_module(self, node):
        if self.model:
            self.header()
            self.namespaceMod()
        else : self.write("using namespace std;\n")
        self.visit(node.body)
        self.newline(node) 
        self.indentation -= 1
        self.write("};")
        self.newline(node) 
        self.indentation -= 1
        self.write("}")
        self.newline(node) 
        self.indentation -= 1
        self.write("}")
        self.newline(1)
        self.write("DECLARE_DYNAMICS(record::%s::%s); // balise specifique VLE"%(self.name.capitalize(),self.model.name.capitalize()))




    def header(self):
        self.write("""// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends

#include <vle/DiscreteTime.hpp>
namespace vd = vle::devs;
namespace vv = vle::value;
// Definition du namespace de la classe du modele
namespace record {
""")

    def namespaceMod(self):
        self.write("namespace %s {"%self.name.capitalize())
        self.newline(1)
        self.write("using namespace vle::discrete_time;")
        self.newline(1)
        self.write("class %s: public DiscreteTimeDyn {"%self.model.name.capitalize())
        self.newline(1)
        self.write("public:")
        self.newline(1)
        self.indentation += 1
        self.constructorClass()
        self.destructorClass()

    
    def constructorClass(self):
        self.write("%s(const vd::DynamicsInit& atom, const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)"%self.model.name.capitalize())
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.transVarParam()
    
    def destructorClass(self):
        self.newline(1)
        self.write("""/**
    * @brief Destructeur de la classe du modèle.
    **/""")
        self.newline(1)
        self.write("virtual ~%s() {};"%self.model.name.capitalize())

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name
        self.add_features(node)
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.templateArr(node.params)
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            if self.model: self.write(" %s::"%self.model.name.capitalize())
            self.write(" %s("%node.name)
            for i, pa in enumerate(node.params):
                if pa.name in self.array_parameter(node.params)[0].values(): continue
                if pa.feat=="IN" and pa.type in ["list","array"]: self.write("const ")
                self.visit_decl(pa.pseudo_type, pa)
                if i!= (len(node.params)-1):
                    self.write(', ')
            self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
        else:
            self.write("""/**
    * @brief Methode de calcul effectuée à chaque pas de temps
    * @param time la date du pas de temps courant
    */""")
            self.newline(1)
            self.write("virtual void compute(const vd::Time& /*time*/)")
            self.newline(1)
            self.write ("{")
            self.newline(1)
        self.body(node.block)
        self.newline(node)
        self.write('}') 
        self.newline(node)
        if  node.name.startswith("model_"):
            self.indentation -= 1
            self.visit_decl_modelVarParam()
        



    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0]=="model":
            name  = node.value.function.split('model_')[1]
            self.write("_%s.Calculate_%s(s, s1, r, a);"%(name.capitalize(), name))
            self.newline(node)
        elif node.value.type =="standard_call" and node.value.function=="copy":
            self.newline(node)
            self.write("%s = %s;"%(node.target.name,node.value.args.name))
        elif node.value.type == "standard_call" and node.value.function=="integr":
            self.newline(node)
            self.write("%s = %s;"%(node.target.name,node.value.args[0].name))
            self.newline(node)
            if isinstance(node.value.args[1].pseudo_type, list):
                self.write("%s.reserve(%s.size() + distance(%s.begin(),%s.end()));"%(node.target.name, node.target.name, node.value.args[1].name, node.value.args[1].name))
                self.newline(node)
                self.write("%s.insert(%s.end(),%s.begin(),%s.end());"%(node.target.name, node.target.name, node.value.args[1].name, node.value.args[1].name))
            else: 
                self.write("%s.push_back("%node.target.name)
                self.visit( node.value.args[1])
                self.write(");")        
        elif node.value.type =="standard_method_call" and node.value.message in ["keys", "values"]:
                self.write("%s.reserve(%s.size());"%(node.target.name, node.value.receiver.name))
                self.newline(node)
                self.write("for(auto const&i : %s)"%node.value.receiver.name)
                self.newline(node)
                self.write("{")
                self.newline(node)
                self.write("    %s.push_back(i.first);"%node.target.name) if node.value.message=="keys" else self.write("    %s.push_back(i.second);"%node.target.name)
                self.newline(node)
                self.write("}")
                self.newline(node)
        else:
            self.newline(node)
            node.target.state = True
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)

    def visit_local(self, node):
        if self.model:
            if "state" not in dir(node) and node.name in self.var:
                if node.name.endswith("_t1"): self.write("%s(-1)"%node.name[:-3])
                else: self.write("%s()"%node.name)
            else: self.write(node.name)
        else: self.write(node.name)


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            self.newline(node)
            if n.name not in self.parameters + self.var:
                if 'value' not in dir(n) and not isinstance(n.pseudo_type, list) and n.pseudo_type!="datetime":
                    self.write(self.types[n.pseudo_type])
                    self.write(' %s;'%n.name) 
                if 'elements' not in dir(n) and n.type in ("list","array"):
                    if n.type=="list":
                        self.write("vector<%s> %s;"%(self.types[n.pseudo_type[1]],n.name))
                    if n.type=="array":
                        self.write(self.types["array"]%(self.types[n.pseudo_type[1]], n.elts.name if "name" in dir(n.elts) else n.elts.value))
                        self.write("%s;"%n.name)
                if 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                    self.write("%s %s"%(self.types[n.type], n.name))
                    self.write(" = ")
                    if n.type=="local":
                        self.write(n.value)
                    else: self.visit(n)
                    self.write(";")           
                elif  n.type=='datetime':
                    self.newline(node)
                    self.write("DateTime ")
                    self.write(n.name)
                    if "elts" in dir(n):
                        self.write(" = ")
                        self.visit(n.elts)
                    self.write(";")            
                elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                    if n.type=="list":
                        self.visit_decl(n.pseudo_type)
                        self.write(n.name)
                        self.write(" = ") 
                        self.write(u'{')
                        self.comma_separated_list(n.elements)
                        self.write(u'};')
                    if n.type=='tuple':
                        pass
                elif 'pairs' in dir(n) and n.type=="dict":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)             
                    self.write(u' = {')
                    self.comma_separated_list(n.pairs)
                    self.write(u'};')                   
        self.newline(node)
    

    def visit_decl_modelVarParam(self):
        tab = []
        self.write("private:")
        self.newline(1)
        self.indentation += 1
        self.write("//Variables d'etat")
        self.newline(1)
        for v in self.st_int:
            z = v.name[:-3] if v.name.endswith("_t1") else v.name
            if z not in tab:
                self.write("""/**
    * @brief %s (%s)
    */"""%(v.description, v.unit))
                self.newline(1)
                self.write("Vect %s"%z) if v.datatype.lower().endswith("list") else self.write("Var %s"%z)
                tab.append(z)

        self.newline(extra=1)
        self.write("//Entrées")
        self.newline(1)
        for v in self.st_ext:
            z = v.name[:-3] if v.name.endswith("_t1") else v.name
            if z not in tab:
                self.write("""/**
        * @brief %s (%s)
        */"""%(v.description, v.unit))
                self.newline(1)
                self.write("Vect %s"%z) if v.datatype.lower().endswith("list") else self.write("Var %s"%z)
                tab.append(z)

        self.newline(extra=1)
        self.write("//Paramètres du modele")
        for p in self.node_param:
            self.newline(1)
            self.write("""/**
    * @brief %s (%s)
    */"""%(p.desc, p.unit))
            self.newline()
            self.visit_decl(p.pseudo_type)
            self.write(" %s;"%p.name)

        




    def transVarParam(self):
        self.write("// Ces parametres ont une valeur par defaut utilise si la condition n'est pas definie")
        self.newline()
        tab = []
        for p in self.model.parameters:
            self.write('%s = (events.exist("%s")) ? vv::%s(events.get("%s")) : %s;'%(p.name, p.name,transType[p.datatype.lower()], p.name, p.default))
            self.newline(1) 
        self.write("//  Variables gérées par ce composant")
        for j in self.st_int:
            z = j.name[:-3] if j.name.endswith("_t1") else j.name
            if z not in tab:
                self.newline(1)
                self.write('%s.init(this,"%s", events);'%(z, z))
                tab.append(z)
        self.newline(1)
        self.write("//  Variables gérées par un autre composant")
        for j in self.st_ext:
            z = j.name[:-3] if j.name.endswith("_t1") else j.name
            if z not in tab:
                self.newline(1)
                self.write('%s.init(this,"%s", events);'%(z, z)) 
                tab.append(z)  
        self.newline(1)
        self.indentation -= 1
        self.write("}")
     

class RecordCompo(CppCompo):
    """ This class generates Record components
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        CppCompo.__init__(self,tree, model, self.name)
    
    def visit_module(self, node):
        return 


transType = {"double":"toDouble",
            "int":"toInteger", 
            "string":"toString",
            "intlist":"toMatrix",
            "date":"toDateTime",
            "boolean":"toBoolean"}


class Crop2ML_Vpz():
    def __init__(self, topology):
        self.topology = topology
        self.recModel = []
        self.recCon = []
        self.recDyn = []
        self.mc = self.topology.model
        self.mu = self.mc.model
        self.tab =" "

    def createAtomic(self):
        sr = "<submodels>\n"
        z = ""
        for m in self.mu:
            z += self.tab + '<model width=" " height=" " x=" " y=" " dynamics="%s" name="%s" type="atomic">\n'%("dyn"+ m.algorithms[0].filename.split("/")[-1].split(".")[0].capitalize(),m.name)
            modin = self.tab*2 + "<in>\n"
            for inp in m.inputs:
                if "variablecategory" in dir(inp):
                    modin += self.tab*3 + '<port name="%s"/>\n'%inp.name
            modin += self.tab*2 + "</in>\n"
            modout = self.tab*2 +"<out>\n"
            for out in m.outputs:
                modout += self.tab*3 + '<port name="%s"/>\n'%out.name
            modout += self.tab*2 +"</out>\n"
            modout += self.tab + "</model>\n"
            z = z + modin + modout
        sr += z + "</submodels>\n"
        return sr

    def createInOutMc(self):
        z_in = self.tab + "<in>\n"
        for inp in self.mc.inputs:
            if "variablecategory" in dir(inp):
                z_in += self.tab*2 +'<port name="%s"/>\n'%inp.name
        z_in += self.tab + "</in>\n"
        z_out = self.tab + "<out>\n"
        for out in self.mc.outputs:
            z_out += self.tab*2 +'<port name="%s"/>\n'%out.name
        z_out += self.tab + "</out>\n"
        return z_in + z_out
    
    def  param(self):
        z = []
        for inp in self.mc.inputs:
            if "parametercategory" in dir(inp): 
                z.append(inp.name )   
        return z  
    
    def createInpCon(self):
        para = self.param()
        z ="<connections>"
        for m in self.mc.inputlink:
            if m["target"].split(".")[1] not in para:
                z += '<connection type="input">\n <origin model="%s" port="%s"/>\n <destination model="%s" port="%s"/>\n</connection>\n'%(self.mc.name, m["source"], m["target"].split(".")[0], m["target"].split(".")[1])
        return z + "</connections>"
    
    def createIntCon(self):
        z =""
        for m in self.mc.internallink:
            z += '<connection type="internal">\n <origin model="%s" port="%s"/>\n <destination model="%s" port="%s"/>\n</connection>\n'%(m["source"].split(".")[0], m["source"].split(".")[1], m["target"].split(".")[0],m["target"].split(".")[1])
        return z
    
    def createDyn(self):
        z = "<dynamics>\n"
        for m in self.mu:
            z += '<dynamic library="%s" package="%s" name="dyn%s"/>\n'%(m.name.capitalize(), self.mc.name, m.name.capitalize())
        return z + "</dynamics>\n"

    def create(self):
        return self.createInOutMc() + \
                self.createAtomic() + \
                self.createInpCon() + self.createIntCon() +self.createDyn()


#mc = Crop2ML_Vpz()