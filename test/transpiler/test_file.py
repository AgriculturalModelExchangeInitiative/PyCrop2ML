# coding: utf-8
from pycropml.transpiler.generate import run
from path import Path

if __name__ == '__main__':

    data = Path.getcwd()/"test"/"transpiler"/"pheno_pkg" #crop2ml (xml with algo) files
    run(data,"f90")  # change the language by "cs", "py"

    data = Path.getcwd()/"test"/"transpiler"/"energybalance_pkg" #crop2ml (xml with algo) files
    run(data,"f90")  # change the language by "cs", "py"   
      


