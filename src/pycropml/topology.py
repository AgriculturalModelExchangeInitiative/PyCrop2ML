from pycropml import composition
from pycropml.pparse import model_parser
from path import Path
import networkx as nx
from collections import defaultdict
from IPython.display import Image, display
from networkx.drawing.nx_pydot import to_pydot
from pycropml.render_cyml import signature
import os
import sys
from pycropml.transpiler.main import Main


DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "str"
DATATYPE['DOUBLE'] = "float"
DATATYPE['DOUBLELIST'] = "list"
DATATYPE['INTLIST'] = "list"
DATATYPE['STRINGLIST'] = "list"
DATATYPE['CHARLIST'] = "list"
DATATYPE['DATELIST'] = "list"
DATATYPE['DOUBLEARRAY'] = "float"
DATATYPE['INTARRAY'] = "int"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "str"
def my_input(_input, defa=True):
    name = _input.name
    _type = _input.datatype      
    if 'default' in dir(_input) and defa:
        if _input.default :
            default = _input.default              
            if DATATYPE[_type]  == "bool":
                val = default.capitalize()
                return "bool %s=%s"%(name, val)                    
            elif DATATYPE[_type] == "list":
                val = eval(default)
                return 'list %s=%s'%(name, val)              
            elif DATATYPE[_type] == "str":                   
                return "str %s='%s'"%(name, default)                
            elif _type in DATATYPE:                   
                default = float(default) if DATATYPE[_type]=="float" else int(default)                                     
                return '%s %s=%s'%(DATATYPE[_type], name, default)
            else:
                if _type=="DOUBLEARRAY" or _type=="INTARRAY": 
                    length = _input.len
                    #print("%s %s[%s]"%(self.DATATYPE[_type], name,len))
                    return ("%s %s[%s]=%s"%(DATATYPE[_type], name, length, default))
                else:
                    return ("%s %s=%s"%(DATATYPE[_type], name, default))
    else:
        if _type=="DOUBLEARRAY" or _type=="INTARRAY": 
            length = _input.len
            #print("%s %s[%s]"%(self.DATATYPE[_type], name,len))
            return ("%s %s[%s]"%(DATATYPE[_type], name, length))
        else:
            return ("%s %s"%(DATATYPE[_type], name))            

       
class Package():
    def __init__(self, name, metainfo, path=None):
        self.name=name
        self.metainfo = metainfo
        
        if (not path):
            # package directory
            import inspect
            # get the path of the file which call this function
            call_path = os.path.abspath(inspect.stack()[1][1])
            self.path = os.path.dirname(call_path)
            self.wralea_path = call_path        

        # package directory

        if (not path):
            # package directory
            import inspect
            # get the path of the file which call this function
            call_path = os.path.abspath(inspect.stack()[1][1])
            self.path = os.path.dirname(call_path)
            self.wralea_path = call_path

        # wralea.py path is specified
        else:
            if (not os.path.exists(path)):
                os.mkdir(path)
            if (not os.path.isdir(path)):
                self.path = os.path.dirname(path)
                self.wralea_path = path

            else:
                self.path = path
                self.wralea_path = os.path.join(self.path, "model.py")
                self.crop2ml_path = os.path.join(self.path, "crop2ml")


 
class PackageManager():
    def __init__(self, proj):
        self.syspath = sys.path[:]
        self.pkg={}
        self.user_crop2ml_path = set()
        self.sys_crop2ml_path = set()  
        self.proj = proj
        

    def check_exist(self):
        pass
      
    def contain_pkg(self):
        pk={}
        for root, dirs, files in os.walk(self.proj):
            if "crop2ml" in dirs:
                pk[root.split('/')[-1]]=root              
        return pk
    
    def get_path(self,pkg):
        di = self.contain_pkg()
        wf_path={}
        for k, v in di.items():
            wf_name = k.split('\\')[-1]
            wf_path[wf_name]=v
        if pkg in wf_path.keys():
            return wf_path[pkg]
        else:
            print("pkge doesn't exist")

import importlib
class Topology():
    pkgs={}
    def __init__(self, name, pkg=None):
        self.name=name 
        if pkg is None:
            if self.isPackage(self.name):
                self.pkg = self.load_pkge(self.name).crop2mlpath
            else: 
                self.pkg=input("Give the path of package")
        else:
            self.pkg=pkg
        self.data = Path(self.pkg)/"crop2ml"
        
        composite_file = self.data.glob("composition*.xml")[0]
        self.mu =  model_parser(self.pkg)
        self.model, = composition.model_parser(composite_file)
        self.pkgs[self.name]=[self.pkg, self.model]
        self.model.inputs = self.meta_inp(self.name)
        self.model.outputs = self.meta_out(self.name)
        self.model.path = Path(self.pkg)
         
    def isPackage(self, name):
        pkg=importlib.util.find_spec(name)   #### Python>=3
        if pkg is None:
            return False
        else:
            if "crop2mlpath" in dir(self.load_pkge(name)):
                return True
            else: return False
                 
    def load_pkge(self, name):
        try:
            module = importlib.import_module(name)
        except Exception as e:
            print(e)
        return module

    def createGraph(self):
        d= defaultdict(list)        
        for mod in self.model.model:
            for inter in self.model.internallink:    
                source = inter["source"].split(".")[0]
                target = inter["target"].split(".")[0]
                if mod.name==source:
                    d[mod.name].append(target)
        return nx.DiGraph(d, name = self.model.name)
    
    def create_edgeInOut(self):
        edge_inout=defaultdict(list)
        for inter in self.model.internallink:
            out = inter["source"].split(".")[1]
            out_name = inter["source"].split(".")[0]
            inp = inter["target"].split(".")[1]
            if out!=inp:
                edge_inout[out_name].append([out,inp])
        return edge_inout
    
    def topologicalSort(self):
        ordV = list(nx.topological_sort(self.createGraph()))
        return ordV

    def info_minout(self):
        inout={}
        for m in self.model.model:
            if m.file.split(".")[0]=="unit":
                for mo in self.mu:
                    if mo.name==m.name:
                        inout[mo.name] = (mo.inputs, mo.outputs)
            else:
                pkgname = m.package_name
                inout[m.name] = (self.meta_inp(pkgname), self.meta_out(pkgname))
        return inout
 
    @property
    def minout(self):
        inout={}
        for m in self.model.model:
            if m.file.split(".")[0]=="unit":
                for mo in self.mu:
                    if mo.name==m.name:
                        inp = [m.name for m in mo.inputs]
                        out = [m.name for m in mo.outputs]
                        inout[mo.name] = (inp, out)
            else:
                pkgname = m.package_name
                inp = [p.name for p in self.meta_inp(pkgname)]
                out = [p.name for p in self.meta_out(pkgname)]
                inout[m.name] = (inp, out)
        return inout

    def algorithm(self):
        code=""
        W= self.topologicalSort()
        edge = self.create_edgeInOut()
        for v in W:
            if not self.check_compo(self.model,v):
                code += "%s = model_%s( %s)\n"%(', '.join(self.minout[v][1]),v.strip().replace(' ','_').lower(),','.join(self.minout[v][0]))
            else:
                code += "%s = model_%s( %s)\n"%(', '.join(self.minout[v][1]),v.strip().replace(' ','_').lower(),','.join(self.minout[v][0]))
                
            if len(edge)!=0:
                if v in list(edge.keys()):
                    for val in list(edge[v]):
                        code += "%s = %s\n"%(val[1],val[0])
        return code
              
    def write_xml(self):
        G = self.createGraph()
        filename = "%s.xml"%(self.model.name)
        nx.write_graphml_xml(G,filename)
    
    def write_png(self):
        a=to_pydot(self.createGraph())
        a.write_png("img.png")
        from networkx.drawing.nx_pydot import graphviz_layout
        print(graphviz_layout(self.createGraph()))
    
    def display_wf(self):
        a=to_pydot(self.createGraph())
        d=a.create_png()
        display(Image(d))
     
    def algo2cyml(self):
        code=''
        tab=' '*4
        for mod in self.model.model:
            code+= 'from %s import model_%s\n'%(signature(mod).capitalize(), signature(mod)) if mod.package_name is None else 'from %s import model_%s\n'%(signature(mod), signature(mod))
        name =self.model.name.strip().replace(' ','_').lower()
        signature_mod= "def model_" +  name + "(%s):"%(",\n      ".join(map(my_input,self.meta_inp(self.name))))
        code += signature_mod+"\n"
        code += self.decl(defa=False)
        lines = [tab+l for l in self.algorithm().split('\n') if l.split()]
        code += '\n'.join(lines)
        code += "\n" + tab + "return " + ", ".join([out.name for out in self.model.outputs]) 
        return code


    def retrive(self, pkgname):
        if pkgname in self.pkgs:
            pkg = self.pkgs[pkgname][0]
            mc = self.pkgs[pkgname][1]
        else:     
            model = Topology(name=pkgname)
            pkg = model.pkg
            mc = model.model
            self.pkgs[pkgname]=[pkg, mc]
        
        return pkg, mc

    def meta_inp(self, pkgname):
        pkg, mc = self.retrive(pkgname)        
        list_var=[]
        mod_inputs=[]
        for inter in mc.inputlink: 
            var = inter["source"]
            mod = inter["target"].split(".")[0]
            if var not in list_var:
                if self.check_compo(mc, mod)!=True:
                    inp = self.info_inputs_mu(pkg,mod,var)
                    list_var.append(var)
                    mod_inputs.append(inp)
                else:
                    name=self.pkg_m(mc, mod)
                    inp = self.get_mu_inp(name, var)
                    mod_inputs.append(inp)
                    list_var.append(var)                           
        return mod_inputs


    def meta_out(self, pkgname):
        pkg, mc = self.retrive(pkgname)
        list_var=[]
        mod_outputs=[]
        for inter in mc.outputlink:    
            var = inter["target"]
            mod = inter["source"].split(".")[0]
            
            if var not in list_var:
                if self.check_compo(mc, mod)!=True:
                    out = self.info_outputs_mu(pkg,mod,var)
                    list_var.append(var)
                    mod_outputs.append(out)
                else:
                    print("o", var)
                    #pa, mc = self.retrive(self.pkg_m(mc, mod))
                    name=self.pkg_m(mc, mod)
                    print(var, name)
                    #out = self.get_mu_out(pa, mod, var)
                    out = self.get_mu_out(name, var)
                    mod_outputs.append(out)
                    list_var.append(var)                           
        return mod_outputs


    # check if a model m is a composite model including in mc   
    def check_compo(self,mc, m):
        test=False
        for mod in mc.model:
            if mod.name == m:
                if mod.file.split(".")[0] == "composition":
                    test = True
                    break
        return test

    # get the name of composite model package    
    def pkg_m(self,mc, m):
        pkg_name=None
        for mod in mc.model:
            if mod.name == m:
                pkg_name = mod.package_name
        return pkg_name

    #get the path of the package    
    def path_pkg(self, mc,m):
        name = self.pkg_m(mc,m)
        ppkg = PackageManager(self.path).get_path(name)
        return ppkg
 
    # get the info of an input of a model unit from its name and the name of the input
    def info_inputs_mu(self,ppkg,mu,varname):
        mod =  model_parser(ppkg)
        for m in mod:
            if m.name==mu:
                for inp in m.inputs:
                    if inp.name == varname:
                        return inp
 
    # get the info of an output of a model unit from its name and the name of the output
    def info_outputs_mu(self,ppkg,mu,varname):
        mod =  model_parser(ppkg)
        for m in mod:
            if m.name==mu:
                for out in m.outputs:
                    if out.name == varname:
                        return out   
    
    # get the model unit from an input of a composite model                
    def get_mu_inp(self,pkgname,varname):
        listvar=[]
        ppkg,mc=self.retrive(pkgname)
        for inp in mc.inputlink:
            var = inp["source"]
            mod = inp["target"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_inp(ppkg, var)      
                inp = self.info_inputs_mu(ppkg,mod,var)
                listvar.append(var)
                return inp

    def get_mu_out(self,pkgname,varname):
        listvar=[]
        ppkg,mc=self.retrive(pkgname)
        for out in mc.outputlink:
            var = out["target"]
            mod = out["source"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_out(ppkg, var)      
                out = self.info_outputs_mu(ppkg,mod,var)
                listvar.append(var)
                return out

    """def get_mu_out(self,ppkg, mc, varname):
        listvar=[]
        data = Path(ppkg)/"crop2ml"
        composite_file = data.glob("composition.%s*.xml"%mc)[0]
        mc, = composition.model_parser(composite_file)
        for out in mc.outputlink:
            var = out["target"]
            mod = out["source"].split(".")[0]
            if var==varname and var not in listvar:
                if self.check_compo(mc,mod)==True:
                    ppkg, mc = self.retrive(self.pkg_m(mc, mod))
                    self.get_mu_out(ppkg, mod, var)      
                inp = self.info_outputs_mu(ppkg,mod,var)
                listvar.append(var)
                return inp   """  

    def decl(self, defa=True):
        info_var = self.info_minout()
        inp = [m.name for m in self.meta_inp(self.name)]
        declaration=""
        tab = ' '*4
        for k, v in info_var.items():
            for j in v[0]:
                if j.name not in inp:
                    declaration += tab+"cdef "+my_input(j, defa)+"\n"
                    inp.append(j.name)
            for w in v[1]:
                if w.name not in inp:
                    #print(w, w.name)
                    declaration += tab+"cdef "+my_input(w, defa)+"\n"
                    inp.append(w.name)
     
        return declaration
                     
    def compotranslate(self, language):
        d= self.algo2cyml()
        test=Main(d, language, models=self.model)
        test.parse()
        test.to_ast(d)
        code=test.translate()  
        return code
                
    def translate_all(self, model):
        for mod in model.model:
            if mod.package_name is not None:
                T= Topology(mod.package_name)
                #print(T.algo2cyml())
                model = self.retrive(mod.package_name)[1]
                self.translate_all(model)
                
    def translate(self):
        #print(self.algo2cyml())
        self.translate_all(self.model)
        
                


#from pycropml.topology import Topology
'''
from pycropml.topology import Topology
from pycropml.transpiler.generators.csharpGenerator import CsharpCompo
pkg1 = "C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/pheno_pkg"
T = Topology(name='pheno_pkg', pkg=pkg1) 
a =CsharpCompo(tree =None, model = T.model)

print(T.compotranslate('cs'))
T.translate()
algo = T.algo2cyml
aCsharpCompo(tree =None, model = T.model)


T.translate()

print(T.algo2cyml())
print(T.compotranslate('cs'))
T.translate_all()
T.write_png()
T.decl()


T.model.model[0].package_name
print(T.algo2cyml())

from pycropml.cyml import transpile_package
transpile_package(pkg, "py")
'''


