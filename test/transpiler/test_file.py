# coding: utf8
from pycropml.transpiler.generate import run
from path import Path

if __name__ == '__main__':

    data = Path.getcwd()/"test"/"transpiler"/"crop2ml_package" #crop2ml (xml with algo) files
    run(data,"cs")  # change the language by "cs", "py"

   
    
    



