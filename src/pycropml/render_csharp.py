"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""

from __future__ import print_function
from __future__ import absolute_import
import os
from path import Path
import six
from pycropml.composition import model_parser

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['INT'] = "int"
    DATATYPE['STRING'] = "string"
    DATATYPE['DOUBLE'] = "double"
    DATATYPE['BOOLEAN'] = "bool"
    DATATYPE['DATE'] = "string"
    DATATYPE['STRINGLIST'] = "List<string>"
    DATATYPE['DOUBLELIST'] = "List<double>"
    DATATYPE['INTLIST'] = "List<int>"
    DATATYPE['DATELIST']="List<string>"
    DATATYPE['DOUBLEARRAY']="double[]"
    DATATYPE['STRINGARRAY']="string[]"
    DATATYPE['INTARRAY']="int[]"

    num = 0

    def __init__(self, models, dir=None):
        """TODO."""
        self.models = models
        self.dir = dir
        #self.with_import = True

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
        self.codetest = ""
        self.runtest = "Test t = new Test();\n"
        code = "class Test\n{\n"     
        code += tab + "%sState s = new %sState();\n"%(name_mc, name_mc)
        code += tab + "%sState s1 = new %sState();\n"%(name_mc, name_mc)    
        code += tab + "%sRate r = new %sRate();\n"%(name_mc, name_mc)
        code += tab + "%sAuxiliary a = new %sAuxiliary();\n"%(name_mc, name_mc)
        code += tab + "%sExogenous ex = new %sExogenous();\n"%(name_mc, name_mc)
        code += tab + "%s mod = new %s();\n"%(m.name, m.name)
        for inp in inputs:            
            sig+= tab+self.DATATYPE[inp.datatype]+" "+inp.name+";\n"        
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
                if   test_paramsets.strip()!="" :  params.update(psets[test_paramsets].params)                     
                for each_run in test_runs :                  
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    self.runtest += "t.%s();\n"%tname                    
                    code +=tab+"//%s"%tname+"\n"                    
                    code +="\n"+tab+"public void %s()"%tname + "\n"+tab+ "{\n"
                    (run, inouts) = list(each_run.items())[0]
                    ins = inouts['inputs']
                    outs = inouts['outputs']                          
                    run_param = params.copy()
                    run_param.update(ins)                 
                    for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default if testinp.datatype not in ("DATE", "STRING") else str(testinp.default)
                    for k, v in six.iteritems(run_param):
                        if v: # the input could not be set in testset and no default value. In this case, it's supposed to set through initialization part
                            type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                            code_ = 2*tab + "%s.%s = %s;\n"%(categ(k, inputs),k if not k.endswith("_t1") else k[:-3],transf(type_v, v))
                            if m.initialization:
                                if v and categ(k, inputs) != "s" :
                                    code += code_ 
                            else:
                                code += code_ 
                    test_codes2 = ""            
                    for k, v in six.iteritems(ins):
                        type_v = [inp.datatype for inp in inputs if inp.name==k][0]
                        code_ = 2*tab + "%s.%s = %s;\n"%(categ(k, inputs),k if not k.endswith("_t1") else k[:-3],transf(type_v, v))
                        if v and categ(k, inputs) == "s" :
                            test_codes2 += code_                  
                    
                    if m.initialization: 
                        code_ = tab*2+"mod.Init(s,s1, r, a, ex);\n" 
                        code += code_
                        code += test_codes2 
                                        
                    code+=tab*2+"mod.CalculateModel(s,s1, r, a, ex);\n"
                    for k, v in six.iteritems(outs):
                        type_o = [out.datatype for out in outputs if out.name==k][0]     
                        code += 2*tab + "//%s: %s;\n"%(k, v[0]) 
                        code += 2*tab + 'Console.WriteLine("%s estimated :");\n'%(k)
                        if type_o.find("LIST")!=-1:
                            code += 2*tab +"for (int i=0; i<%s.%s.Count; i++) Console.WriteLine(%s.%s[i]);\n"%(categ(k, outputs),k, categ(k, outputs), k) 
                        elif type_o.find("ARRAY")!=-1:
                            code += 2*tab +"for (int i=0; i<%s.%s.Length; i++) Console.WriteLine(%s.%s[i]);\n"%(categ(k, outputs),k, categ(k, outputs), k)  
                        else:
                            code += 2*tab + "Console.WriteLine(%s.%s);\n"%(categ(k, outputs),k)                  
                    code+=tab+"}\n"
                    num = num+1                  
        code+="}\n"
        code += self.runtest
        self.codetest= code
        return self.codetest
    
    
    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = self.dir/"test_%s.cs"%signature(model)
            codetest = "//Test generation'\n\n" + codetest
            with open(filename, "w") as csharp_file:
                csharp_file.write(codetest.encode('utf-8'))
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
DATATYPE['STRING'] = "string"
DATATYPE['DOUBLE'] = "double"
DATATYPE['BOOLEAN'] = "bool"
DATATYPE['DATE'] = "DateTime"
DATATYPE['STRINGLIST'] = "List<string>"
DATATYPE['DOUBLELIST'] = "List<double>"
DATATYPE['INTLIST'] = "List<int>"
DATATYPE['DATELIST']="List<DateTime>"
DATATYPE['STRINGARRAY'] = "new string[]"
DATATYPE['DOUBLEARRAY'] = "new double[]"
DATATYPE['INTARRAY'] = "new int[]"
DATATYPE['DATEARRAY']="new DateTime[]"

def transfDouble(type_v,elem):
    return str(elem)+'D'

def transfDate(type, elem):
    ser = elem.split("/")
    if len(ser)==3:
        year, month, day = ser[0], ser[1], ser[2]
        return "new DateTime(%s, %s, %s) "%( year, month, day)
    if len(ser)==4:
        year, month, day, hour= ser[0], ser[1], ser[2], ser[3]
        return "new DateTime(%s, %s, %s,%s ) "%( year, month, day, hour)
    if len(ser)==5:
        year, month, day, hour, min = ser[0], ser[1], ser[2],ser[3], ser[4]
        return "new DateTime(%s, %s, %s, %s, %s) "%( year, month, day, hour, min) 
    if len(ser)==6:
        year, month, day, hour, min, sec = ser[0], ser[1], ser[2],ser[3], ser[4], ser[5]
        return "new DateTime(%s, %s, %s,%s,%s,%s) "%( year, month, day, hour, min, sec)   

def transfDateList(type, elem):
    res=""
    for dat in eval(elem):
        t = transfDate("DateTime",dat)
        res+=t+","
    return "new List<DateTime>{%s}"%(res)


def transfArray(type_v, elem):
    if isinstance(elem, list):
        res = ",".join(list(map(transf,[type_v.split("ARRAY")[0]]*len(elem),elem )))
        return "%s{%s}"%(DATATYPE[type_v],res)
    else:
        return str(elem)


def transfString(type_v, elem): 
    return ('"%s"'%elem).replace('""', '"')
def transfList(type_v, elem):
    res = ",".join(list(map(transf,[type_v.split("LIST")[0]]*len(elem),elem )))
    return "new %s() {%s}"%(DATATYPE[type_v],res)
def transf(type_v, elem):
    if type_v == "BOOLEAN":
        return elem.lower()
    elif type_v=="DOUBLE":
        return transfDouble(DATATYPE[type_v], elem)
    elif type_v in ("STRING"):
        return transfString(DATATYPE[type_v], elem)
    elif type_v =="DATE":
        return transfDate(DATATYPE[type_v], elem)        
    elif type_v=="INT":
        return str(elem)
    elif type_v in ("STRINGLIST","DOUBLELIST","INTLIST"):
        return transfList(type_v,eval(elem))
    elif type_v.endswith("ARRAY"):
        return transfArray(type_v,eval(elem))
    elif type_v == "DATELIST":
        return transfDateList(type_v,elem)
    else:
        print("uuuuuuuiiiiooooooo")


