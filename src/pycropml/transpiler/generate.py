# coding: utf8
from pycropml.transpiler.main import Main
from path import Path
from pycropml.pparse import model_parser
import os.path
from pycropml import render_cyml


def run(crop2ml_pkg,language):    
    models = model_parser(crop2ml_pkg) # parse xml files and create python model object
    output = Path(crop2ml_pkg/'src')
    m2p = render_cyml.Model2Package(models, dir=output)
    m2p.generate_package()        # generate cyml models in "pyx" directory
    
    tg_rep = Path(output/"%s"%(language)) # target language models  directory in output
        
    if not tg_rep.isdir() :  #Create if it doesn't exist
        tg_rep.mkdir()
    
    # generate 
    cyml_rep = Path(output/'pyx') # cyml model directory in output
    for k, file in enumerate(cyml_rep.files()):
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
                with open(filename, "w") as tg_file:
                    tg_file.write(str(code))


   
    
    



