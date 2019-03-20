# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""

# coding: utf8
from pycropml.transpiler.main import Main
from pycropml.transpiler.main import languages
from path import Path
import os.path
import sys


def main():
    

    usage = """
        cyml transpiler translate a cyml source code or a Crop2ML package with algo in cyml
        language to target language .
    Example
       cyml <source_code.pyx or pkg> <target_language>

    * target language must be:
        -py for python
        -cs for csharp
        -cpp for c++
        -f90 for fortran
        -java  for java
        -r for R

"""  

    if len(sys.argv)!=3:
        print(usage)
        return
 
    sourcef= sys.argv[1]
    language = sys.argv[2]
    
    if language not in languages:
        print(usage)
        return    
              
    if  len(sourcef.split("."))==2:  # translate from cyml code
        if sourcef.split(".")[1]!="pyx" :
            print(usage)
            return                  
        file = Path(sourcef)
        with open(file, 'r') as fi:
            source = fi.read()
        name = sourcef.split(".")[0]
        test=Main(file, language)
        test.parse()
        test.to_ast(source) 
        code=test.to_source()
        print(code)
        filename = "%s.%s"%(name, language)   
        with open(filename, "wb") as tg_file:
            tg_file.write(code.encode('utf-8'))
        
    else:                       # translate from crop2ml package
        from pycropml import render_cyml
        from pycropml.pparse import model_parser
        from pycropml.writeTest import WriteTest
        pkg= Path(sourcef)
        models = model_parser(pkg) # parse xml files and create python model object
        output = pkg/'src'
        dir_test= pkg/'test'
        m2p = render_cyml.Model2Package(models, dir=output)
        m2p.generate_package()        # generate cyml models in "pyx" directory          
        tg_rep = Path(output/"%s"%(language)) # target language models  directory in output
        dir_test_lang =  Path(dir_test/"%s"%(language))
 
        if not output.isdir() :  #Create src directory if it doesn't exist
            output.mkdir()              
            
        if not tg_rep.isdir() :  #Create if it doesn't exist
            tg_rep.mkdir()
			
        if not dir_test.isdir() :  #Create if it doesn't exist
			dir_test_lang.mkdir() 			
    
        if not dir_test_lang.isdir() :  #Create if it doesn't exist
            dir_test_lang.mkdir()             
            
        # generate 
        cyml_rep = Path(output/'pyx') # cyml model directory in output
        for k, file in enumerate(cyml_rep.files()):
            print(file)
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
    
        test = WriteTest(models,language)                  # writeTest
        code=test.write()
        filename = dir_test_lang/"test.%s"%language
        with open(filename, "wb") as tg_file:
            tg_file.write(code.encode('utf-8'))

if __name__ == '__main__':
    main()