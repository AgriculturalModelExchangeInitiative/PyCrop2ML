"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path
import numpy 
import os.path
import six

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['FLOAT'] = float
    DATATYPE['INT'] = int
    DATATYPE['STRING'] = str
    DATATYPE['DOUBLE'] = float
    DATATYPE['DOUBLELIST'] = list
    DATATYPE['INTLIST'] = list
    DATATYPE['STRINGLIST'] = list
    DATATYPE['CHARLIST'] = list
    DATATYPE['DATELIST'] = list
    DATATYPE['DOUBLEARRAY'] = numpy.array
    DATATYPE['BOOLEAN'] = bool
    DATATYPE['DATE'] = str
 
    

    num = 0

    def __init__(self, models, dir=None, pkg_name=None):
        """TODO."""
        self.models = models
        self.dir = dir

        self.with_import = True
        if pkg_name is None:
            self.pkg_name = "CropModel"
        else: self.pkg_name = pkg_name

    def run(self):
        """TODO."""
        self.generate_package()
        self.write_tests()


    def generate_package(self):
        """Generate a R package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'r_model'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()
        files = []
        count = 0
        for model in self.models:     
            self.generate_component(model)            
            filename = self.dir/"%s.R"%signature(model)
            with open(filename, "w") as R_file:
                R_file.write(self.code.encode('utf-8','ignore'))
                files.append(filename)
                model.module_name = str(Path(filename).namebase)
                count += 1
        return files


    def generate_component(self, model_unit):
        """ Todo
        """
        self.code=""
        if model_unit.function:
            for function in model_unit.function:
                if function.language in ("R", "r"):
                    module=os.path.splitext(function.filename)[0]
                    self.code +="source( %s/%s ) \n"%(self.dir,module.lower())
                    break
        self.code += self.generate_function_signature(model_unit)
        self.code += self.generate_function_doc(model_unit)
        self.code += self.generate_algorithm(model_unit)        
        return self.code

    def generate_algorithm(self, model_unit):

        outputs = model_unit.outputs
        tab = ' '*4
        code="\n"
        for algorithm in model_unit.algorithms:                                  
            if (algorithm.language=="R") or (algorithm.language==" ") or (algorithm.language=="r"):
                algo = algorithm
                break
        development = algo.development           
        if algo.filename==None:
        
        # Outputs
            code += tab + 'return  (list(%s))'%(', '.join(["%s=%s"%(o.name, o.name)  for o in outputs]))+ '\n}'
 
        else:
            lines = [tab+l for l in development.split('\n') if l.split()]
            code += '\n'.join(lines)
            code += '\n'+tab + 'return  (list(%s))'%(', '.join(["%s=%s"%(o.name, o.name)  for o in outputs]))+ '\n}'

        self.code = code

        return self.code

    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    %s  
'''%comment(generate_doc(model_unit))
        return doc



    def generate_function_signature(self, model_unit):
        inputs = model_unit.inputs
        func_name =  signature(model_unit)

        code = '%s <- function('%(func_name,)

        def my_input(_input):
            name = _input.name
            _type = _input.datatype
            if 'default' in dir(_input):
                default = _input.default
                
                if self.DATATYPE[_type]  == bool:
                    val = default.capitalize()
                    return "%s=%s"%(name, val)
                    
                elif self.DATATYPE[_type] == list:
                    val = eval(default)
                    return '%s=%s'%(name, val)
                
                elif self.DATATYPE[_type] == str: 
                    print("%s='%s'"%(name, default))                    
                    return "%s='%s'"%(name, default)
                
                elif _type in self.DATATYPE:# and _type!="Date":
                    
                    default = self.DATATYPE[_type](default)
                ##if _type=="Date":
                    #default = datetime.strptime(default, '%d/%m/%Y')
                    
                    return '%s=%s'%(name, default)
            else:
                return name


        ins = [ my_input(inp) for inp in inputs]
        separator = ','
        code += separator.join(ins)
        code = code[:-1]
        code+= ')\n{'

        return code

    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit

        model_name  = signature(m)

        psets = m.parametersets
        self.codetest = ""
        for v_tests in m.testsets:
            test_runs = v_tests.test  # different run in the thest
            test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
            params = {}

            if   test_paramsets not in list(psets.keys()):
                print('Unknown parameter %s'%test_paramsets)
            else:
                params.update(psets[test_paramsets].params)

                for each_run in test_runs :
                    test_codes = []

                    # make a function that transforms a title into a function name
                    tname = list(each_run.keys())[0].replace(' ', '_')
                    tname = tname.replace('-', '_')


                    (run, inouts) = list(each_run.items())[0]

                    ins = inouts['inputs']
                    outs = inouts['outputs']

                    code = '\n'
                    test_codes.append(code)

                    code = "test_%s<-function(){"%(tname)
                    test_codes.append(code)
                    code = "    params= %s("%model_name
                    test_codes.append(code)

                    run_param = params.copy()
                    run_param.update(ins)

                    for k, v in six.iteritems(run_param):
                        code = "    %s = %s,"%(k,v)
                        test_codes.append(code)
                    code = "     )"
                    test_codes.append(code)

                    for j, k in enumerate(m.outputs):
                        if  k.datatype.strip() in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY") :
                        
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                        
                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                        
                            test_codes.append(code)
                                                   
                        if k.datatype.strip() in ("STRING", "BOOL", "INT", "DATE"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)
                       
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                       
                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)
                       
                           
                        if k.datatype.strip() in ("DOUBLELIST", "DOUBLEARRAY"):
                            code = tab + "%s_estimated = np.around(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = np.around(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                       
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)
                           
                           
                        if k.datatype.strip() in ("INTLIST", "INTARRAY"):
                            code = tab + "%s_estimated = params[%s]"%(k.name,j) if len(m.outputs)>1 else tab + "%s_estimated = params"%(k.name)
                            test_codes.append(code)
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                            code = tab+ "assert np.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                        if k.datatype.strip() == "DOUBLE":
                            code = tab + "%s_estimated = round(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else tab + "%s_estimated = round(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                           
                            code = tab + "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)
                           
                            code = tab+ "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                    code = '\n'.join(test_codes)

                    self.codetest += code +'\n}'

        return self.codetest
    
    def generate_func_test(self, model_unit):
        pass

    def write_tests(self):
        """ TODO: Manage several models rather than just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            filename = self.dir/"test_%s.r"%signature(model)

            codetest = "#Test generation'\n\n"+'source("%s/%s.r")'%(self.dir.replace('\\','/'),signature(model)) + codetest

            with open(filename, "w") as r_file:
                r_file.write(codetest.encode('utf-8'))
                files.append(filename)
            count +=1
        return files


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()

    return name




def generate_doc(model):
    desc = model.description
        
    _doc = """
    %s
    Author: %s
    Reference: %s
    Institution: %s
    Abstract: %s
""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.Abstract)

    code = '\n'
    code += _doc

    return code


def comment(line):
    list_com = ['#'+x for x in line.split('\n')]
    com = '\n'.join(list_com)
    return com