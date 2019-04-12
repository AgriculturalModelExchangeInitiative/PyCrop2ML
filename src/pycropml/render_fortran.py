"""Add License, Header.

Use pkglts

Problems:
- name of a model unit?

"""
from __future__ import print_function
from __future__ import absolute_import
from path import Path 
import six

class Model2Package(object):
    """ TODO

    """

    DATATYPE = {}
    DATATYPE['FLOAT'] = 'REAL'
    DATATYPE['INT'] = 'INTEGER'
    DATATYPE['STRING'] = 'CHARACTER'
    DATATYPE['DATE'] = 'CHARACTER'
    DATATYPE['DOUBLE'] = 'REAL'
    DATATYPE['DOUBLELIST'] = 'REAL, ALLOCATABLE, DIMENSION(:)'
    DATATYPE['INTLIST'] = 'INTEGER, ALLOCATABLE, DIMENSION(:)'
    DATATYPE['STRINGLIST'] = 'CHARACTER, ALLOCATABLE, DIMENSION(:)'
    DATATYPE['INTARRAY'] = 'INTEGER, ALLOCATABLE, DIMENSION'
    DATATYPE['DOUBLEARRAY'] = 'REAL, ALLOCATABLE, DIMENSION'
    DATATYPE['BOOLEAN'] = 'LOGICAL'
    DATATYPE['DATELIST'] = 'CHARACTER, ALLOCATABLE, DIMENSION(:)'
 
    

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
        """Generate a Cyml package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """

        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'pyx'
        if (directory).isdir() :
            self.dir = directory
        else:
            self.dir = directory.mkdir()
        files = []
        count = 0
        for model in self.models:          
            self.generate_component(model)
            filename = self.dir/"%s.f90"%signature(model)                     
            with open(filename, "wb") as f90_file:
#                cyml_file.write(self.code.encode('utf-8','ignore'))
                f90_file.write(self.code.encode('utf-8'))
                files.append(filename)           
                model.module_name = str(Path(filename).namebase)
            count += 1
        return files
        
    def generate_component(self, model_unit):
        """ Todo
        """
        self.code= "\n\n"  
        if model_unit.function:
            for function in model_unit.function:
                if function.language in ("Cyml", "cyml"):
                    #module=os.path.splitext(function.filename)[0]
                    self.code +="USE %s_mod \n"%(function.name.lower()) 
                    break
        self.code += self.generate_function_signature(model_unit)
        self.code += self.generate_function_doc(model_unit)
        self.code += self.generate_algorithm(model_unit)        
        return self.code

    def generate_algorithm(self, model_unit):
        outputs = model_unit.outputs
        inputs = model_unit.inputs
        tab = ' '*4
        list_inputs=[] 
        algo=""
        code=""
        
        """ we  declare all outputs which are not in inputs"""
        output_declaration=""
        for inp in inputs:
            list_inputs.append(inp.name)
        for out in outputs:
            if out.name not in list_inputs:
                output_declaration += tab+self.my_input(out)+"\n"

        for algorithm in model_unit.algorithms:                                  
            if (algorithm.language=="f90") or (algorithm.language=="F90"):
                algo = algorithm
                break
        if algo:
            development = algo.development           
            lines = [tab+l for l in development.split('\n') if l.split()]
            code = output_declaration
            code += '\n'.join(lines)
            code += '\n'+tab + 'return  ' + ', '.join([o.name  for o in outputs]) + '\n'
        self.code = code
        return self.code

    # documentation
    def generate_function_doc(self, model_unit):
        doc='''
    """%s
    """
'''%generate_doc(model_unit)
        return doc

    def generate_function_signature(self, model_unit):
        desc = model_unit.description
        inputs = model_unit.inputs
        # Compute name from title.
        # We need an explicit name rather than infering it from Title
        #name = desc.Title
        func_name = "%s_"%signature(model_unit)
        code = 'def %s('%(func_name,)
        code_size = len(code)
        #_input_names = [inp.name.lower() for inp in inputs]
        ins = [ self.my_input(inp) for inp in inputs]
        separator = ',\n'+ code_size*' '
        code += separator.join(ins)
        code+= '):'
        return code

    def my_input(self,_input):
        name = _input.name
        _type = _input.datatype  
        if _type=="DOUBLEARRAY" or _type=="INTARRAY": 
            size = _input.len
            return ("%s(%s) :: %s \n"%(self.DATATYPE[_type],size, name))
        else:
            return ("%s:: %s\n"%(self.DATATYPE[_type], name))            

    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        model_name = signature(m)
        psets = m.parametersets
        list_var=[]
        list_inouts=[]
        for inp in m.inputs:
            list_var.append(inp.name)
            list_inouts.append(inp)
        for out in m.outputs:
            if out.name not in list_var:
                list_var.append(out.name)
                list_inouts.append(out)
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
                    decl_ins= [ tab + self.my_input(var) for var in list_inouts]
                    code = "PROGRAM test_%s_%s "%(tname,m.name)
                    test_codes.append(code)
                    test_codes.append('\n'.join(decl_ins))                                          
                    run_param = params.copy()
                    run_param.update(ins)
                    for testinp in m.inputs:
                        if testinp.name not in list(run_param.keys()):
                            run_param[testinp.name]=testinp.default                                       
                    for k, v in six.iteritems(run_param):
                        code = "    %s = %s\n"%(k,v)
                        test_codes.append(code)
                        
                    code="    call %s_(%s)"%(model_name, ','.join(list_var))
                    test_codes.append(code)
                    code = "    print *,%s"%','.join([out.name for out in m.outputs])
                    test_codes.append(code)
                    
                    '''for j, k in enumerate(m.outputs):
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
                            test_codes.append(code)'''

                    code = '\n'.join(test_codes)
                    

                    self.codetest += code+'\n END PROGRAM\n\n'

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
            filename = Path(self.dir/"test_%s.f90"%signature(model))
            codetest = "!Test generation'\n\n"+codetest
            with open(filename, "wb") as f90_file:
                f90_file.write(codetest.encode('utf-8'))
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
