# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""
import os
from path import Path
import pycropml
from pycropml.transpiler.main import Main
from pycropml.transpiler.antlr_py.dssat.run import process_dssat
from pycropml import render_cyml
from pycropml.pparse import model_parser
from pycropml.writeTest import WriteTest
from pycropml.transpiler.generators.csharpGenerator import to_struct_cs, to_wrapper_cs
from pycropml.transpiler.generators.javaGenerator import to_struct_java
from pycropml.topology import Topology
from pycropml.code2nbk import Model2Nb
from pycropml.transpiler.generators.pythonGenerator import PythonSimulation
from pycropml.transpiler.generators.siriusGenerator import to_struct_sirius,to_wrapper_sirius
from pycropml.transpiler.generators.recordGenerator import Crop2ML_Vpz
from pycropml.transpiler.generators.cppGenerator import to_struct_cpp
import pycropml.transpiler.antlr_py 


NAMES = {'r':'r','cs':'csharp','cpp':'cpp', 'py':'python', 'f90':'fortran', 'java':'java', 'simplace':'simplace', 'sirius':'sirius', "openalea":"openalea","check":"check","apsim":"apsim", "record":"record", "dssat":"dssat","bioma":"bioma", "stics":"stics"}
ext = {'r':'r','cs':'cs','cpp':'cpp', 'py':'py', 'f90':'f90', 'java':'java', 'simplace':'java', 'sirius':'cs','bioma':'cs', "openalea":"py","check":"check", "apsim":"cs", "record":"cpp", "dssat":"f90", "stics":"f90"}

domain_class = ["cs", "java", 'sirius','cpp', "bioma"]
wrapper=["cs", "sirius", "bioma"]
platform = ["simplace","sirius","openalea","apsim","bioma","record","dssat", "stics"]

def transpile_file(source, language):
    sourcef = source
    file = Path(sourcef)
    with open(file, 'r') as fi:
        source = fi.read()
    name = sourcef.split(".")[0]
    test = Main(file, language)
    test.parse()
    test.to_ast(source)
    code = test.to_source()
    filename = "%s.%s" % (name, language)
    with open(filename, "wb") as tg_file:
        tg_file.write(code.encode('utf-8'))
    return 0


def prefix(model):
    pref = model.modelid.split(".")[0]
    return pref


def transpile_package(package, language):
    """ translate from crop2ml package"""
    sourcef = package
    namep = sourcef.split(os.path.sep)[-1]
    pkg = Path(sourcef)
    models = model_parser(pkg) # parse xml files and create python model object
    output = Path(os.path.join(pkg, 'src'))
    dir_test= Path(os.path.join(pkg, 'test'))

    # Generate packages if the directories does not exists.
    if not output.isdir():
        output.mkdir()
    if not dir_test.isdir():
        dir_test.mkdir()

    m2p = render_cyml.Model2Package(models, dir=output)
    m2p.generate_package()        # generate cyml models in "pyx" directory
    tg_rep1 = Path(os.path.join(output, language)) # target language models  directory in output
    dir_test_lang = Path(os.path.join(dir_test, language))
    
    if not tg_rep1.isdir():
        tg_rep1.mkdir()
        
    tg_rep = Path(os.path.join(tg_rep1, namep))
    if not tg_rep.isdir():
        tg_rep.mkdir()

    if not dir_test_lang.isdir() :  #Create if it doesn't exist
        dir_test_lang.mkdir()

    m2p.write_tests()


    # generate cyml functions
    cyml_rep = Path(os.path.join(output, 'pyx')) # cyml model directory in output

    # cretae topology of composite model
    T = Topology(namep,package)
    mc_name = T.model.name

    # Record VPZ
    if language == "record":
        vpz = Crop2ML_Vpz(T)
        print(vpz.create())

    # domain class
    if language in domain_class:
        getattr(getattr(pycropml.transpiler.generators,
                    '%sGenerator' % NAMES[language]),
                'to_struct_%s' % language)([T.model],tg_rep, mc_name)
    # wrapper
    if language in wrapper:
        getattr(getattr(pycropml.transpiler.generators,
                    '%sGenerator' % NAMES[language]),
                'to_wrapper_%s' % language)(T.model,tg_rep, mc_name)    

    # Transform model unit to languages and platforms
    for k, file in enumerate(cyml_rep.files()):
        with open(file, 'r') as fi:
            source = fi.read()
        name = os.path.split(file)[1].split(".")[0]
        for model in models:                         # in the case we have'nt the same order
            if name.lower() == model.name.lower() and prefix(model) != "function":
                test = Main(file, language, model, T.model.name)
                test.parse()
                test.to_ast(source)
                code = test.to_source()
                filename = Path(os.path.join(tg_rep, "%s.%s"%(name.capitalize(), ext[language])))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))
                Model2Nb(model, code, name, dir_test_lang).generate_nb(language, tg_rep, namep)
                #code2nbk.generate_notebook(code, name, dir_nb_lang)

    # Create Cyml Composite model
    T_pyx = T.algo2cyml()
    fileT = Path(os.path.join(cyml_rep, "%sComponent.pyx"%mc_name))
    with open(fileT, "wb") as tg_file:
        tg_file.write(T_pyx.encode('utf-8'))  

    filename = Path(os.path.join(tg_rep, "%sComponent.%s"%(mc_name, ext[language])))
    
    with open(filename, "wb") as tg_file:
        tg_file.write(T.compotranslate(language).encode('utf-8'))   

    ## create computing algorithm
    if language == "py":
        simulation = PythonSimulation(T.model)
        simulation.generate()
        code = ''.join(simulation.result)
        filename = Path(os.path.join(tg_rep, "simulation.py"))
        initfile = Path(os.path.join(tg_rep, "__init__.py"))
        with open(filename, "wb") as tg_file:
            tg_file.write(code.encode("utf-8"))
        with open(initfile, "wb") as tg_file:
            tg_file.write("".encode("utf-8"))
        setup = PythonSimulation(T.model)
        setup.generate_setup()
        code = ''.join(setup.result)
        setupfile = Path(os.path.join(tg_rep1, "setup.py"))
        with open(setupfile, "wb") as tg_file:
            tg_file.write(code.encode("utf-8"))

    status = 0
    return status

def transpile_component(component, package, language):
    """Transform a framework model component to Crop2ML/CyML

    Args:
        component (path): a Crop2ML folder containing a repository of a framework model component
        language (str): a language or framework

    Returns:
        package: Crop2ML package containing xml files and 
    """

    if language == "dssat":
        process_dssat(component, package)

    return 0