import numpy
from math import *

def ismomentregistredzc_39_(calendarMoments):
    #- Description:
    #            - Model Name: IsMomentRegistredZC39 Model
    #            - Author: Pierre Martre
    #            - Reference: Modeling development phase in the 
    #                Wheat Simulation Model SiriusQuality.
    #                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #            - Institution: INRA Montpellier
    #            - Abstract: if FlagLeafLiguleJustVisible is already Registred 
    #- inputs:
    #            - name: calendarMoments
    #                          - description : List containing appearance of each stage
    #                          - variablecategory : auxiliary
    #                          - datatype : STRINGLIST
    #                          - default : ['Sowing']
    #                          - unit : 
    #                          - inputtype : variable
    #- outputs:
    #            - name: isMomentRegistredZC_39
    #                          - description :  if Flag leaf ligule has already appeared 
    #                          - datatype : INT
    #                          - min : 0
    #                          - max : 1
    #                          - unit : 
    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments else 0
    return isMomentRegistredZC_39