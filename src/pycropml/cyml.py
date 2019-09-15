# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""
import os
from path import Path
import pycropml
from pycropml.transpiler.main import Main
from pycropml import render_cyml
from pycropml.pparse import model_parser
from pycropml.writeTest import WriteTest
from pycropml.transpiler.generators.csharpGenerator import to_struct_cs
from pycropml.transpiler.generators.javaGenerator import to_struct_java
from pycropml.topology import Topology
from pycropml.code2nbk import Model2Nb

NAMES = {'cs':'csharp', 'py':'python', 'f90':'fortran', 'java':'java'}

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
    print(code)
    filename = "%s.%s" % (name, language)
    with open(filename, "wb") as tg_file:
        tg_file.write(code.encode('utf-8'))
    return 0

def prefix(model):
    pref = model.modelid.split(".")[0]
    return pref
def transpile_package(package, language):
    # translate from crop2ml package
    sourcef = package
    namep = sourcef.split(".")[0]
    pkg = Path(sourcef)
    models = model_parser(pkg) # parse xml files and create python model object
    output = Path(os.path.join(pkg, 'src'))
    dir_test= Path(os.path.join(pkg, 'test'))
    dir_nb = Path(os.path.join(pkg, 'notebook'))

    # Generate packages if the directories does not exists.
    if not output.isdir():
        output.mkdir()
    if not dir_test.isdir():
        dir_test.mkdir()
    if not dir_nb.isdir():
        dir_nb.mkdir()

    m2p = render_cyml.Model2Package(models, dir=output)
    m2p.generate_package()        # generate cyml models in "pyx" directory
    tg_rep = Path(os.path.join(output, language)) # target language models  directory in output
    dir_test_lang = Path(os.path.join(dir_test, language))
    dir_nb_lang = Path(os.path.join(dir_nb, language))
    
    if not tg_rep.isdir():
        tg_rep.mkdir()    
    if not dir_test_lang.isdir() :  #Create if it doesn't exist
        dir_test_lang.mkdir()
    if not dir_nb_lang.isdir() :  #Create if it doesn't exist
        dir_nb_lang.mkdir()

    m2p.write_tests()


    # generate
    cyml_rep = Path(os.path.join(output, 'pyx')) # cyml model directory in output

    T = Topology(namep,package)
    T_pyx = T.algo2cyml()
    namep = T.model.name.lower()
    fileT = Path(os.path.join(cyml_rep, "%s.pyx"%namep))
    with open(fileT, "wb") as tg_file:
        tg_file.write(T_pyx.encode('utf-8'))  

    if language in ("cs", "java"):
        getattr(getattr(pycropml.transpiler.generators,
                    '%sGenerator' % NAMES[language]),
                'to_struct_%s' % language)([T.model],tg_rep, namep)

    filename = Path(os.path.join(tg_rep, "%s.%s"%(namep.capitalize(), language)))
    
    with open(filename, "wb") as tg_file:
        tg_file.write(T.compotranslate(language).encode('utf-8'))      
    
    for k, file in enumerate(cyml_rep.files()):
        #print(file)
        with open(file, 'r') as fi:
            source = fi.read()

        name = os.path.split(file)[1].split(".")[0]
        for model in models:                         # in the case we have'nt the same order
            if name.lower() == model.name.lower() and prefix(model)!="function":
                test=Main(file, language, model,T.model.name)
                test.parse()
                test.to_ast(source)
                code=test.to_source()
                filename = Path(os.path.join(tg_rep, "%s.%s"%(name.capitalize(), language)))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))
                Model2Nb(model,code,name,dir_test_lang).generate_nb(language,tg_rep,namep)
                #code2nbk.generate_notebook(code, name, dir_nb_lang)


    # writeTest
    '''TODO'''
    #test = WriteTest(models,language,dir_test_lang)
    #test.write()

    status = 0
    return status
