from pycropml import render_fortran
from pycropml import render_java
from pycropml import render_csharp
from pycropml import render_cpp
from pycropml import render_r
from pycropml.render_cyml import transf, signature
from pycropml.modelunit import ModelUnit
from pycropml.nameconvention import signature1
import six


def splitunit(unit):
    un=""
    for k,el in enumerate(unit):
        if el=="*" and unit[k+1]=="*" :un += "**"
        elif el=="*" and unit[k-1]=="*":un +=""
        elif el=="*": un += "*u."
        elif el=="/": un+="/u."
        else: un += el
    return un
        
    

def generate_test_py(model:ModelUnit,dir=None, package=None):
    from path import Path
    import os
    
    tab = ' '*4
    m = model
    #name = m.description.Title
    name = m.name
    name.strip()
    name = name.replace(' ', '_').lower()
    model_name = name
    psets = m.parametersets    
    list_var=[]
    init_var_in = []
    init_var_out = []
    for inp in m.inputs:
        list_var.append(inp.name)
        if hasattr(inp, "parametercategory"):
            init_var_in.append(inp.name)  
        elif inp.variablecategory=="exogenous":
            init_var_in.append(inp.name)
        elif inp.variablecategory=="state":
            init_var_out.append(inp.name)
    
    if package is not None:
        rel_dir_src = Path(os.path.join(m.path, "test", "py")).relpathto(Path(os.path.join(m.path, "src", "py", package.replace("-", "_"))))
    else:
        rel_dir_src = Path(os.path.join(m.path, "test", "py")).relpathto(Path(os.path.join(m.path, "src", "py")))
    
    import_test = f'import numpy\nfrom datetime import datetime\nfrom array import array\n'
    import_test += f'import sys\n'
    import_test += f'sys.path.append("{rel_dir_src}")\n'
    import_test += f'from {signature1(model)} import model_{name}\n'
    if m.initialization: import_test += f'from {name.lower()} import init_{name}\n'
    code_test = [import_test]
    for v_tests in m.testsets:

        #test_name = v_tests.name  # name of tests
        test_runs = v_tests.test  # different run in the thest
        test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
        params = {}

        if test_paramsets.strip() != "" and test_paramsets not in list(psets.keys()):
            print(' Unknow parameter %s' % test_paramsets)
        else:
            if test_paramsets.strip() != "":
                params.update(psets[test_paramsets].params)
            for each_run in test_runs:
                test_codes = []
                test_codes2 = []

                # make a function that transforms a title into a function name
                tname = list(each_run.keys())[0].replace(' ', '_')
                tname = tname.replace('-', '_')

                (run, inouts) = list(each_run.items())[0]
                ins = inouts['inputs']
                outs = inouts['outputs']
                name_categ = {}
                run_param = params.copy()
                run_param.update(ins)

                for i, j in enumerate(m.inputs):
                    if j.name not in list(run_param.keys()):
                        run_param[j.name]=j.default 
                    name_categ[j.name] = j.variablecategory if hasattr(j, "variablecategory") else j.parametercategory
                    
                
                for k, v in six.iteritems(run_param):
                    type_ = [(inp.datatype, inp.unit) for inp in m.inputs if inp.name==k][0]
                    code = "%s = %s" % (k, transf(type_[0], v)) 
                    if m.initialization:
                        if v and name_categ[k] != "state" and m.initialization :
                            test_codes.append(code) 
                    else:
                        test_codes.append(code)

                for k, v in six.iteritems(ins):
                    type_ = [(inp.datatype, inp.unit) for inp in m.inputs if inp.name==k][0]
                    code = "%s = %s" % (k, transf(type_[0], v)) 
                    if v and name_categ[k] == "state" :
                        test_codes2.append(code)                   

                
                if m.initialization: 
                    code = ', '.join(init_var_out) + " = " + f"init_{signature1(m)}({','.join(init_var_in)})" 
                    test_codes.append(code)
                    test_codes.extend(test_codes2) 
                code = "params= model_{0}({1})\n".format(model_name, ', '.join(list_var))
                test_codes.append(code)
                outnames = list(outs.keys())
                for j, k in enumerate(m.outputs):
                    if k.name in outnames:
                        if k.datatype in ("STRINGLIST","STRINGARRAY"):
                            code = "%s_estimated = " % k.name
                            code += "params[%s]" % (j) if len(m.outputs) > 1 else "params"
                            test_codes.append(code)
                            code = "%s_computed = %s" % (k.name, outs[k.name][0])
                            test_codes.append(code)
                            code = "assert numpy.all(%s_computed == %s_estimated)"%(k.name, k.name)
                            test_codes.append(code)

                        if k.datatype in ("DATELIST","DATEARRAY"):
                            code = "%s_estimated = " % k.name
                            code += "params[%s]" % (j) if len(m.outputs) > 1 else "params"
                            test_codes.append(code)
                            code = "%s_computed = %s" % (k.name, transf("DATELIST",outs[k.name][0]))
                            test_codes.append(code)
                            code = "assert numpy.all(%s_computed == %s_estimated)"%(k.name, k.name)
                            test_codes.append(code)
                        
                        if k.datatype == "DATE":
                            code = "%s_estimated =" % (k.datatype.lower().capitalize())
                            code += "params[%s]" % (j) if len(m.outputs) > 1 else "params"
                            test_codes.append(code)
                            code = "%s_computed = %s" % (k.name, transf("DATE",outs[k.name][0]))
                            test_codes.append(code)
                            code = "assert %s_computed == %s_estimated"%(k.name, k.name)
                            test_codes.append(code)                        

                        if k.datatype in ("STRING", "BOOL", "INT"):
                            code = "%s_estimated =" % (k.name if k.datatype !="BOOLEAN" else k.datatype.lower().capitalize())
                            code += "params[%s]" % (j) if len(m.outputs) > 1 else "params"
                            test_codes.append(code)
                            code = "%s_computed = %s" % (k.name, outs[k.name][0])
                            test_codes.append(code)
                            code = "assert %s_computed == %s_estimated"%(k.name, k.name)
                            test_codes.append(code)

                        if k.datatype in ("DOUBLELIST", "DOUBLEARRAY"):              
                            code = "%s_estimated = numpy.around(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else "%s_estimated = numpy.around(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)
                            code = "%s_computed = %s"%(k.name,outs[k.name][0]) if k.datatype=="DOUBLELIST" else "%s_computed = numpy.around(array('f', %s),%s)"%(k.name,outs[k.name][0], outs[k.name][1])
                            test_codes.append(code)

                            code = "assert numpy.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                        if k.datatype in ("INTLIST", "INTARRAY"):
                            code = "%s_estimated =" % k.name
                            code += "params[%s]" % (j) if len(m.outputs) > 1 else "params"
                            test_codes.append(code)
                            code = "%s_computed = %s" % (k.name, outs[k.name][0])
                            test_codes.append(code)
                            code = "assert numpy.all(%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)

                        if k.datatype == "DOUBLE":
                            code = "%s_estimated = round(params[%s], %s)"%(k.name,j,outs[k.name][1]) if len(m.outputs)>1 else "%s_estimated = round(params, %s)"%(k.name,outs[k.name][1])
                            test_codes.append(code)

                            code = "%s_computed = %s"%(k.name,outs[k.name][0])
                            test_codes.append(code)

                            code = "assert (%s_estimated == %s_computed)"%(k.name,k.name)
                            test_codes.append(code)
                code = '\n'.join(test_codes)
                code_test.append(code)
    return code_test

def generate_test_f90(model, dir, package=None):
    return [render_fortran.Model2Package(model, dir).generate_test(model)]


def generate_test_cs(model, dir, package=None):
    return [render_csharp.Model2Package(model, dir).generate_test(model)]

def generate_test_java(model,directory=None, package=None):
    return [render_java.Model2Package(model, directory).generate_test(model)]


def generate_test_cpp(model, directory=None, package=None):
    render = render_cpp.Model2Package(model, directory)
    return [render.generate_test_import(model, package),
            render.generate_test_function(model),
            render.generate_test_run(model)]

def generate_test_r(model,dir, package=None):
    return render_r.Model2Package(model, dir).generate_test(model, package)

def generate_test_simplace(model,dir=None, package=None):
    pass

def generate_test_sirius(model,dir=None, package=None):
    pass

def generate_test_stics(model,dir=None, package=None):
    pass

def generate_test_openalea(model,dir=None, package=None):
    pass

def generate_test_check(model,dir=None, package=None):
    pass
def generate_test_apsim(model,dir=None, package=None):
    pass
def generate_test_dssat(model,dir=None, package=None):
    pass
def generate_test_record(model,dir=None, package=None):
    pass
def generate_test_bioma(model,dir=None, package=None):
    pass