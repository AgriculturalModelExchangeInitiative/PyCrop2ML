import numpy
from math import *

def leafnumber_(deltaTT,phyllochron,hasFlagLeafLiguleAppeared,leafNumber,phase):
    #- Description:
    #            - Model Name: CalculateLeafNumber Model
    #            - Author: Pierre MARTRE
    #            - Reference: Modeling development phase in the 
    #                Wheat Simulation Model SiriusQuality.
    #                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #            - Institution: INRA Montpellier
    #            - Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
    #- inputs:
    #            - name: deltaTT
    #                          - description : daily delta TT 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : -20
    #                          - max : 100
    #                          - default : 23.5895677277199
    #                          - unit : °C d
    #                          - inputtype : variable
    #            - name: phyllochron
    #                          - description : phyllochron
    #                          - variablecategory : state
    #                          - inputtype : variable
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 1000
    #                          - default : 0
    #                          - unit : °C d leaf-1
    #            - name: hasFlagLeafLiguleAppeared
    #                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    #                          - variablecategory : state
    #                          - datatype : INT
    #                          - min : 0
    #                          - max : 1
    #                          - default : 0
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: leafNumber
    #                          - description :  Actual number of phytomers
    #                          - variablecategory : state
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 25
    #                          - default : 0
    #                          - unit : leaf
    #                          - inputtype : variable
    #            - name: phase
    #                          - description :  the name of the phase
    #                          - variablecategory : state
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 7
    #                          - default : 1
    #                          - unit :  
    #                          - uri : some url
    #                          - inputtype : variable
    #- outputs:
    #            - name: leafNumber
    #                          - description : Actual number of phytomers
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 10000
    #                          - unit : leaf
    #                          - uri : some url
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron == 0.0:
                phyllochron_ = 0.0000001
            else:
                phyllochron_ = phyllochron
            leafNumber = leafNumber + min(deltaTT / phyllochron_, 0.999)
    return leafNumber