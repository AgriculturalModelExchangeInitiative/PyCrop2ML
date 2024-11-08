import os
import re
from path import Path
import xmlformatter

from pycropml.transpiler.antlr_py import repowalk
from pycropml.transpiler.antlr_py.codeExtraction import extraction
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.listOfTags import *
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG, to_CASG
from pycropml.transpiler.antlr_py.python.pythonExtraction import PythonExtraction
from pycropml.transpiler.antlr_py.python.python_preprocessing import RemImplicit_return, Declarations
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import extract
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml, generate_compositefile, generate_unitfile, create_repo

class NotAuthorizedException(Exception):
    pass


def translate(inout, meth):
    # Remove declaration of model in/out
    d = Declarations(inout)
    dr = d.process(meth.block)

    # Remove return statement
    i = RemImplicit_return()
    ir = i.process(dr)

    # finally we got the algo
    algo = writeCyml(d.declarations + ir)
    
    return algo


modeltag_begin = "#"+model_tags[0]
modeltag_end = "#"+model_tags[1]

inittag_begin = "#"+init_tags[0]
inittag_end = "#"+init_tags[1]



def run_python(components, package):
    
    create_repo(package)    
    files = repowalk.walk(components, 'py')
    print('Process ', files)
    composite= None
    composites = Path(components).glob('*Component.py')
    if composites:
        composite = composites[0]
    else: 
        print('No model composite!')

    # Only for OpenAlea
    # wralea= Path(components).glob('__wralea__.py')[0]
    op_extr = PythonExtraction()
    #op_extr.pm.clear()
    #wf =  op_extr.retrievePackage(components)  
    # dtermine the package name to be used in models file
    m = os.path.basename(Path(package))
    m = m.split("_")
    package_name = m[0] +"." + "".join(m[1:])
    
    mu_names = []
    models = []
    for  k, v in files.items():
        if v not in composites:
            print(v)
            with open(v, "r") as f:
                code = f.read()
            #extract in py_units var all model units functions from each file! we suppose 
            # that more than one model unit function can be defined in a module
            # based on the cyml tags
            

            py_units = extraction(code,modeltag_begin,modeltag_end)
            py_inits = extraction(code,inittag_begin,inittag_end)
            
            file_dictasg = to_dictASG(code, 'py')
            file_asg = to_CASG(file_dictasg)
            
            z = PythonExtraction()
            
            
            if py_inits and len(py_inits)!=len(py_units):
                raise NotAuthorizedException("many init functions in the same module")
            
            # TODO we only handle one init function and one unit in the same module or no init function
            
            funcs = []
            if py_units:
                for py_unit in py_units:
                    
                    # match def ...() # retrieve the name
                    name = re.findall(r'(def\s+.+\()', py_unit)[0].replace("def", "").replace("(", "").strip()
                    # extract algorithm of each py_unit using file_asg, the name of the unit
                    meth = z.getmethod(file_asg, name, True)
                    
                    
                    
                    mdata = extract(meth.doc +"\n\n") # create a ModelUnit object (description, inputs and outputs). After we complete with other info
                    #print(mdata.description.ExtendedDescription, "babfsdvhsdbvjsbvbsjvjskdfbv")

                    inout = list({var.name for var in mdata.inputs + mdata.outputs}) # extract model in/out

                    # finally we got the algo
                    algo = translate(inout, meth)
                    
                    # save algo
                    if name.startswith("model_"): name = name.replace("model_", "")
                    mu_names.append(mdata.name)
                    
                    out_compute = os.path.join(package,  "crop2ml", "algo", "pyx", mdata.name + ".pyx")
                    with open(out_compute, "w") as fi:
                        fi.write(algo + '\n')
                    
                    #extract external function used in model unit
                    extfunc = z.externFunction(file_asg, meth, True)
                    # save external functions
                    for ext in extfunc:
                        name = ext.name
                        mdata.function.append(name)
                        r = [ext]
                        # find all external dependencies of external functions
                        while True:
                            ext = ext if  isinstance(ext, list) else [ext]
                            ex = [z.externFunction(file_asg, m, True, m.name) for m in ext ][0]
                            if ex:
                                r.append(ex)
                                ext = ex
                            else:
                                break
                        extcode = writeCyml(r)
                        exfunc = os.path.join(package, "crop2ml", "algo", "pyx", name + ".pyx")
                        with open(exfunc, "w") as fi:
                            fi.write(extcode + '\n')
                                
                    if py_inits:
                        dict_init = {} 
                        name_i = re.findall(r'(def\s+.+\()', py_inits[0])[0].replace("def", "").replace("(", "").strip()
                        dict_init["name"] = name_i
                        meth_ = z.getmethod(file_asg, name_i, True)
                        init_ = translate(inout, meth_)
                        # save init
                        if name_i.startswith("init_"): name_i = name_i.replace("init_", "")
                        name_i = "init."+ name_i
                        dict_init["filename"] = name_i + ".pyx"
                        out_compute = os.path.join(package,  "crop2ml", "algo", "pyx", name_i + ".pyx")
                        with open(out_compute, "w") as fi:
                            fi.write(init_ + '\n')
                        mdata.initialization = [dict_init]  

                        #extract external function used in model unit
                        extfunc = z.externFunction(file_asg, meth_, True)
                        # save external functions
                        for ext in extfunc:
                            name = ext.name
                            mdata.function.append(name)
                            r = [ext]
                            # find all external dependencies of external functions
                            while True:
                                ext = ext if  isinstance(ext, list) else [ext]
                                ex = [z.externFunction(file_asg, m, True, m.name) for m in ext ][0]
                                if ex:
                                    r.append(ex)
                                    ext = ex
                                else:
                                    break
                            extcode = writeCyml(r)
                            exfunc = os.path.join(package, "crop2ml", "algo", "pyx", name + ".pyx")
                            with open(exfunc, "w") as fi:
                                fi.write(extcode + '\n')
                        
                        models.append(mdata)
                        mdata = z.orderedvar(mdata,meth)
                        generate_unitfile(package, mdata, package_name)  
                                 
                        break
                    else:
                        mdata = z.orderedvar(mdata,meth)
                        models.append(mdata)
                        generate_unitfile(package, mdata, package_name)  

    for composite in composites:
        with open(composite, "r") as f:
            code = f.read()
        res_compo = extraction(code, modeltag_begin,modeltag_end)
        compo_dictasg = to_dictASG(res_compo[0] , "py")
        compo_asg = to_CASG(compo_dictasg)
        mc = op_extr.modelcomposition(res_compo[0], models, compo_asg) 
        generate_compositefile(package, mc, package_name)
    
