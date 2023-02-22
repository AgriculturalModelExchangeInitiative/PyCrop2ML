"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import six
import os
from pycropml.composition import model_parser

class Model2Package(object):
    DATATYPE = {}
    DATATYPE['INT'] = "int"
    DATATYPE['STRING'] = "String"
    DATATYPE['DOUBLE'] = "double"
    DATATYPE['DOUBLELIST'] = "Arrays.asList"
    DATATYPE['STRINGLIST'] = "Arrays.asList"
    DATATYPE['INTLIST'] = "Arrays.asList"
    DATATYPE['BOOLEAN'] = "boolean"
    DATATYPE['DATE'] = "LocalDateTime"
    DATATYPE['DATELIST'] = "Arrays.asList"
    num = 0

    def __init__(self, models, dir=None):
        self.models = models
        self.dir = dir
        self.alg=""
        self.with_import = True
    def generate_test(self, model_unit):
        tab = ' '*4
        m = model_unit
        sig = ""
        inputs = m.inputs
        outputs=m.outputs
        num=0  
        dir_crop2ml = Path(os.path.join(m.path,"crop2ml"))
        dir_compo = dir_crop2ml.glob("composition*.xml")[0]
        name_mc = model_parser(dir_compo)[0].name            
        psets = m.parametersets
        self.codetest = ""
        self.runtest = "Test t = new Test();\n"
        code = "class Test\n{\n"     
        code += tab + "%sState s = new %sState();\n"%(name_mc, name_mc)
        code += tab + "%sState s1 = new %sState();\n"%(name_mc, name_mc)    
        code += tab + "%sRate r = new %sRate();\n"%(name_mc, name_mc)
        code += tab + "%sAuxiliary a = new %sAuxiliary();\n"%(name_mc, name_mc)
        code += tab + "%sExogenous ex = new %sExogenous();\n"%(name_mc, name_mc)
        code += tab + "%s mod = new %s();\n"%(m.name, m.name)
        def categ(k, inout):
            state = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory =="state"]
            rate = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory =="rate"]
            auxiliary = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory =="auxiliary"]
            exogenous = [m.name for m in inout if "variablecategory" in dir(m) and m.variablecategory =="exogenous"]
            parameter = [m.name for m in inout if "parametercategory" in dir(m)]
            if k in state and k.endswith("_t1"): return "s1"
            elif k in state : return "s"
            elif k in rate: return  "r"
            elif k in auxiliary: return  "a"
            elif k in exogenous: return  "ex"
            elif k in parameter: return "mod"
            else: raise Exception("error")    
        for inp in inputs:            
            sig+= inp.name+"," 
        for v_tests in m.testsets:
            test_name = v_tests.name  # name of tests
            code +=tab+"//%s"%test_name+");\n"    
            test_runs = v_tests.test  
            test_paramsets = v_tests.parameterset  # name of paramsets
        # map the paramsets
            params = {}            
            if   test_paramsets.strip()!="" and test_paramsets not in list(psets.keys()):
                print(' Unknow parameter %s'%test_paramsets)
            else:
                if   test_paramsets.strip()!="" :  
                    params.update(psets[test_paramsets].params)                    
                for each_run in test_runs :
                    des = ""                    
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')                   
                    self.runtest += "t.%s();\n"%tname                    
                    code +=tab+"//%s"%tname+"\n"                    
                    code +="\n"+tab+"public void %s()"%tname + "\n"+tab+ "{\n"
                    type_param = [ins.datatype for ins in inputs]
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']                          
                    run_param = params.copy()
                    run_param.update(ins)                   
                    """for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default if testinp.datatype not in ("DATE", "STRING") else str(testinp.default)"""
                    for k, v in six.iteritems(run_param):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        code_ = setval(type_v, categ(k, inputs), k, v, tab, inputs)   
                        if m.initialization:
                            if v and categ(k, inputs) != "s" :
                                code += code_ 
                        else:
                            code += code_ 

                    test_codes2 = ""            
                    for k, v in six.iteritems(ins):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        code_ = code_ = setval(type_v, categ(k, inputs), k, v, tab, inputs)
                        if v and categ(k, inputs) == "s" :
                            test_codes2 += code_                  
                    
                    if m.initialization: 
                        code_ = tab*2+"mod.Init(s,s1, r, a, ex);\n" 
                        code += code_
                        code += test_codes2 
                    
                    code+=tab*2+"mod.Calculate_%s(s,s1, r, a, ex);\n"%(m.name.lower())
                    for k, v in six.iteritems(outs):
                        type_o = [out.datatype for out in outputs if out.name==k][0]     
                        code += 2*tab + "//%s: %s;\n"%(k, v[0]) 
                        code += 2*tab + 'System.out.println("%s estimated :");\n'%(k)
                        if type_o.find("LIST")!=-1:
                            code += 2*tab +"for (int i=0; i<%s.get%s().size(); i++) System.out.println(%s.get%s().get(i));\n"%(categ(k, outputs),k, categ(k, outputs), k) 
                        elif type_o.find("ARRAY")!=-1:
                            code += 2*tab +"for (int i=0; i<%s.get%s().length; i++) System.out.println(%s.get%s()[i]);\n"%(categ(k, outputs),k, categ(k, outputs), k)                         
                        else:
                            code += 2*tab + "System.out.println(%s.get%s());\n"%(categ(k, outputs),k)                  
                    num = num+1                  
                    code+=tab+"}\n"                              
        code+="}\n"
        code += self.runtest
        self.codetest += code
        return self.codetest


    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            ext = '' if count == 0 else str(count)
            filename = self.dir/"test_%s.java"%signature(model)

            codetest = "//Test generation'\n\n" +"import java.math.BigDecimal;\n"+ codetest

            with open(filename, "w") as java_file:
                java_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files
    
        
def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')

    return name

DATATYPE = {}
DATATYPE['INT'] = "int"
DATATYPE['STRING'] = "String"
DATATYPE['DOUBLE'] = "double"
DATATYPE['DOUBLELIST'] = "Arrays.asList"
DATATYPE['STRINGLIST'] = "Arrays.asList"
DATATYPE['INTLIST'] = "Arrays.asList"
DATATYPE['BOOLEAN'] = "boolean"
DATATYPE['DATE'] = "LocalDateTime"
DATATYPE['DATELIST'] = "Arrays.asList"

cymltype={
"INT": "Integer",
"DOUBLE": "Double",
"STRING": "String",
"BOOLEAN":"Boolean",
"DATE":"LocalDateTime"}

def transfDouble(type_v,elem):
    return str(elem)   
def transfString(type_v, elem): 
    return ('"%s"'%elem).replace('""', '"')
def transfList(type_v, elem):
    res = ",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),elem )))
    return "new ArrayList<>(%s(%s))"%(DATATYPE[type_v],res)

def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.lower()
    elif type_v=="DOUBLE":
        return transfDouble(DATATYPE[type_v], elem)
    elif type_v in ("STRING", "DATE"):
        return transfString(DATATYPE[type_v], elem)
    elif type_v=="INT":
        return str(elem)
    elif type_v.endswith("LIST"):
        return transfList(type_v,eval(elem))
    elif type_v.endswith("ARRAY"):
        return transfArray(type_v, eval(elem))

def transfArray(type_v,elem):
    if isinstance(elem, list):
        res = ",".join(list(map(transf,[type_v.split("ARRAY")[0]]*len(elem),elem )))
        return "new %s[] {%s}"%(cymltype[type_v.split("ARRAY")[0]],res)
    else:
        return str(elem)

def transfDate(categ,name, elem):
    return "%s.set%s(LocalDateTime.of(%s));"%(categ,name, strtoList(elem))

def transfDateList(categ,name, elem):
    return "%s.set%s(new ArrayList<>(Arrays.asList(%s)));"%(categ, name, formatDateList(elem))

def formatDate(elem):
    return 'LocalDateTime.of(%s)'%strtoList(elem)
def formatDateList(elem):
    t=[]
    for el in eval(elem):
        t.append(formatDate(strtoList(el)))
    return ','.join(t)

def strtoList(elem):
    e = elem.split("/")
    elem = [str(el) for el in e]
    if len(elem)==3: elem.extend(["00","00","00"])
    return ", ".join(elem)

def setval(type_v, categ, k, v, tab, inputs):
    if type_v not in ("DATE", "DATELIST"):
        code_ = 2*tab + "%s.set%s(%s);\n"%(categ,k if not k.endswith("_t1") else k[:-3],transf(type_v, v)) 
    else:
        if type_v=="DATE":
            code_ = 2*tab + "%s\n"%(transfDate(categ(k, inputs),k if not k.endswith("_t1") else k[:-3], v))
        if type_v=="DATELIST":
            code_ = 2*tab + "%s\n"%(transfDateList(categ(k, inputs),k if not k.endswith("_t1") else k[:-3], v)) 
    return code_  
