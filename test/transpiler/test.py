# coding: utf-8
from pycropml.transpiler.main import Main
from pycropml.pparse import model_parser

source = u"""import fibonacci
from math import *
def fib_(float n):
    n=ceil(10.5)
    return n"""

  
test=Main(source, "f90")
a=test.parse()    
g=test.to_ast(source)  
test.dictAst


  
code=test.to_source()
print(code)
  
source =u"""from math import exp
def phyllochron2(float fixPhyll=5.0,
                float leafNumber=0.0,
                float lincr=8.0,
                float ldecr=10.0,
                float pdecr=0.4,
                float pincr=1.5,
                float ptq=0.0,
                float gai=0.0,
                float pastMaxAI=0.0,
                float kl=0.45,
                float aPTQ=0.842934,
                float phylPTQ1=20.0,
                float p=120.0,
                str choosePhyllUse='Default'):

    cdef float phyllochron, pastMaxAI1
    if choosePhyllUse == "Default":
        if (leafNumber < ldecr): 
            phyllochron = fixPhyll * pdecr
        elif (leafNumber >= ldecr and leafNumber < lincr): 
            phyllochron = fixPhyll
        else: 
            phyllochron = fixPhyll * pincr
    if choosePhyllUse == "PTQ":
        pastMaxAI1 = pastMaxAI
        gai = max(pastMaxAI1,gai)
        pastMaxAI = gai
        if (gai > 0.0): 
            phyllochron = phylPTQ1 * ((gai * kl) / (1 - exp(kl * gai))) / (ptq + aPTQ)
        else: phyllochron = phylPTQ1      
    if choosePhyllUse == "Test":
        if (leafNumber < ldecr): 
            phyllochron = p * pdecr
        elif (leafNumber >= ldecr and leafNumber < lincr): 
            phyllochron = p
    else: phyllochron = p * pincr
    return  phyllochron, pastMaxAI"""
