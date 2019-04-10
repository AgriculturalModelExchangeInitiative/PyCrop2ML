# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""
import os.path
from path import Path

from pycropml.transpiler.main import Main

from pycropml import render_cyml
from pycropml.pparse import model_parser
from pycropml.writeTest import WriteTest

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

def transpile_package(package, language):
    # translate from crop2ml package
    sourcef = package
    pkg = Path(sourcef)
    models = model_parser(pkg) # parse xml files and create python model object
    output = pkg/'src'
    dir_test= pkg/'test'
    m=[model.name for model in models]

    # Generate packages if the directories does not exists.
    if not output.isdir():
        output.mkdir()

    if not dir_test.isdir():
        dir_test.mkdir()

    m2p = render_cyml.Model2Package(models, dir=output)
    m2p.generate_package()        # generate cyml models in "pyx" directory
    tg_rep = Path(output/"%s"%(language)) # target language models  directory in output
    dir_test_lang =  Path(dir_test/"%s"%(language))

    if not tg_rep.isdir():
        tg_rep.mkdir()

    if not dir_test_lang.isdir() :  #Create if it doesn't exist
        dir_test_lang.mkdir()

    # generate
    cyml_rep = Path(output/'pyx') # cyml model directory in output
    for k, file in enumerate(cyml_rep.files()):
        #print(file)
        with open(file, 'r') as fi:
            source = fi.read()
        name = os.path.split(file)[1].split(".")[0]
        for model in models:                         # in the case we have'nt the same order
            if name == model.name.lower():
                test=Main(file, language, model)
                test.parse()
                test.to_ast(source)
                code=test.to_source()
                filename = tg_rep/"%s.%s"%(name, language)
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))

    # writeTest
    test = WriteTest(models,language,dir_test_lang)
    test.write()

    status = 0
    return status
