"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import numpy
from six.moves import range


class Model2Package(object):
    """ TODO

    """

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

    num = 0

    def __init__(self, models, dir=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
    
    def run(self):
        """TODO."""
        self.generate_package()
        self.write_tests()
    
    
    def generate_package(self):
        """Generate a csharp package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """

        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'csharp_model'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()

        files = []
        count = 0

        for model in self.models:
            

            self.generate_component(model)
            
            ext = '' if count == 0 else str(count)
            filename = self.dir/"%s.cs"%signature(model)

            with open(filename, "w") as python_file:
                python_file.write(self.code.encode('utf-8','ignore'))
                files.append(filename)

                model.module_name = str(Path(filename).namebase)

            count += 1

        return files


    
    def generate_component(self, model_unit):
        """ Todo
        """
        self.code = self.generate_public_class(model_unit)+'\n\n'
        self.code += self.generate_estimation(model_unit)+'\n'
        self.code +=self.generate_function_doc(model_unit)+'\n'

        self.code += self.generate_algorithm(model_unit) + '\n'

        return self.code

    def generate_function_doc(self, model_unit):

        desc = model_unit.description
        
        _doc = """/*
     %s

    Author: %s
    Reference: %s
    Instituton: %s
    Abstract: %s
    
"""%(desc.Title, desc.Author, desc.Reference, desc.Institution, desc.Abstract)+"*/"

        code = '\n'
        code += _doc

        return code

    def generate_algorithm(self, model_unit):

        outputs = model_unit.outputs
        inputs = model_unit.inputs
        sig = ""
        output_declaration = ""
        tab = ' '*4
        list_inputs=[]
        
        
        """ we  declare all outputs which are not in inputs"""
        
        for inp in inputs:
            list_inputs.append(inp.name)
        for out in outputs:
            sig+=out.name+","
            if out.name not in list_inputs:
                output_declaration += tab*2+self.DATATYPE[out.datatype]+" "+out.name+";\n"
        
        """ we select the algorithm if the language is specified or not"""
        
        for algorithm in model_unit.algorithms: 
                                
            if (algorithm.language =="C#")or(algorithm.language==" "):
                algo = algorithm
                break
        development = algo.development 
          
        if algo.filename==None:
       

            code = output_declaration
                
            lines = [l.strip() for l in development.split('\n') if l.strip()]
            for line in lines:
                if (line[len(line)-1] !=";")and(algo.language==" "): line = line+";"
                code += tab*2+line+'\n'
                
            code += tab*2+ 'return ' + 'new '+model_unit.name+"("+sig[:-1]+");\n"
                
            code+=tab+'}\n'
            code+='}\n'
                
        else: 
            #print(Path.getcwd()/algo.filename) I will improve it to import code part
            code=output_declaration+"\n"
            lines = [tab*2+l for l in development.split('\n') if l.split()]
            code += '\n'.join(lines)            
            code += '\n'+tab*2 + 'return ' + 'new '+model_unit.name+"("+sig[:-1]+");\n"
                
            code+=tab+'}\n'  
            code+='}\n'        
                                                  
 
        self.code = code

        return self.code

    # documentation
    
    def generate_public_class(self, model_unit):
        
        outputs = model_unit.outputs
        
        tab=' '*4

        code ="public class " + signature(model_unit) +'\n{\n'

        for out in outputs:
            code+=tab+"public"+" "+self.DATATYPE[out.datatype.strip()]+" "+out.name + ';\n'
        
        code+=tab+"public" +" "+model_unit.name+"("
        sig = ""
        for out in outputs:
            sig+= self.DATATYPE[out.datatype.strip()]+" "+"_"+out.name+","
            
        code+=sig[:-1]+')\n'+tab+'{\n'

        for out in outputs:
            code+=tab*2+out.name+"="+ "_"+out.name+';\n'
        
        code+=tab+'}\n}'
        
        self.code = code
        return self.code
        
        
    def generate_estimation(self, model_unit):
        outputs=model_unit.outputs
        inputs = model_unit.inputs
        
        tab=' '*4

        code ="public static class Estimation_" + signature(model_unit) +'\n{\n'
      
        
        code+=tab+"public static "+ model_unit.name+ " Calculate"+signature(model_unit)+"("
        sig = ""
                
        for inp in inputs:
            
            sig+= self.DATATYPE[inp.datatype]+" "+inp.name+","
        """            
            if "default" not in inp.__dict__:
                sig+= self.DATATYPE[inp.datatype]+" "+inp.name+"," 
        for inp in inputs:
            if "default" in inp.__dict__:
                sig+= self.DATATYPE[inp.datatype]+" "+inp.name+ ","
        """      
                    
        code+=sig[:-1]+')\n'+tab+'{\n'
        self.code = code
        
        return self.code    
        


    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        sig = ""
        inputs = m.inputs
        outputs=m.outputs
        num=0
      
        psets = m.parametersets
        self.codetest = ""
 
        code = "public static class Test\n{\n"   
        
        for inp in inputs:            
            sig+= tab+self.DATATYPE[inp.datatype]+" "+inp.name+";\n" 
        
        #code+=sig+"\n"
        for v_tests in m.testsets:

            test_name = v_tests.name  # name of tests
            code +=tab+"//%s"%test_name+");\n"
            
            test_runs = v_tests.test  
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}
            
            if   test_paramsets not in list(psets.keys()):
                print('Unknow parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)
                               
                for each_run in test_runs :
                    

                    des = ""
                    
                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')
                    
                    code +=tab+"//%s"%tname+"\n"
                    
                    code +="\n"+tab+"public static void %s()"%tname + "\n"+tab+ "{\n"


                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']
                           
                    run_param = params.copy()
                    run_param.update(ins)
                    
                    for testinp in inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=[testinp.default] 
                            
                    
                    vartest = ""
                    for k, v in run_param.items():
                        type_v = [inp.datatype for inp in inputs if inp.name==k]
                        if type_v[0] in ("DATE","STRINGLIST","DOUBLELIST","INTLIST", "DATELIST"):
                            vartest+= "%s: new %s %s,"%(k,self.DATATYPE[type_v[0]], transfList(v)) 
                        else: "%s:%s,"%(k,v)
                        #vartest += "%s:%s,"%(k,v)
                        
                    code+=tab*2+signature(m)+" res%s = Estimation_%s.Calculate"%(num,signature(m))+signature(m)+"("+vartest[:-1]+");\n\n"
                    
                    
                    code+=tab*2+"Console.WriteLine("
                    for l in range (0, len(outputs)):
                        des += "{"+str(l)+r"}\n"
                    des = '"'+des[:-2]+'"'+","
                    for out in outputs:
                        des+='"%s: "'%out.name+ "+"+"res%s."%num+out.name+","
                    
                    code+=des[:-1]+");\n\n"                    
                    
                    
                    for k, v in outs.items():
                        type_v=[out.datatype for out in outputs if out.name==k]
                        val = transfDouble(v[0]) if type_v[0]=="DOUBLE" else v[0]
                        if len(v)==2:
                            code+=tab*2+"Console.WriteLine("+'"%s Comparison: (Math.Round(%s ,%s);Math.Round(res%s.%s, %s)) "'%(k, val,v[1], num, k, v[1]) + "+Equals(Math.Round("+val +","+v[1]+")," +"Math.Round(res%s."%num+k+","+v[1]+")));\n"
                        else: code+=tab*2+"Console.WriteLine("+'"%s Comparison: ("'%k+ val+ '";"' +"res%s."%num+k+")+"+'") "'+"+Equals("+val+"," +"res%s."%num+k+"));\n"
                    
                    code+=tab+"}\n"
                    num = num+1                  
   
        code+="}\n"
        
       
        self.codetest= code
        return self.codetest
    
    
    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            ext = '' if count == 0 else str(count)
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

def transfList(elem):
    return str(elem).replace("[", "{").replace("]", "}")
  
def transfDouble(elem):
    return str(elem)+'D'