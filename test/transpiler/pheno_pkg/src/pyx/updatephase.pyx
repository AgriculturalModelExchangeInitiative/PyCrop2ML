import numpy as np 
from math import *

def updatephase_(float cumulTT=354.582294512,
                 float leafNumber=4.62051162186,
                 float cumulTTFromZC_39=0.0,
                 int isMomentRegistredZC_39=0,
                 float gai=0.325519628514,
                 float grainCumulTT=0.0,
                 float dayLength=12.7433275303,
                 float vernaprog=1.05325268296,
                 float minFinalNumber=6.87941041399,
                 float fixPhyll=91.2,
                 int isVernalizable=1,
                 float dse=105.0,
                 float pFLLAnth=2.22,
                 float dcd=100.0,
                 float dgf=450.0,
                 float degfm=0.0,
                 float maxDL=15.0,
                 float sLDL=0.85,
                 bool ignoreGrainMaturation=False,
                 float pHEADANTH=1.0,
                 int switchMaize=0,
                 str choosePhyllUse='Default',
                 float p=120.0,
                 float phase=1.0,
                 float cumulTTFromZC_91=0.0,
                 float phyllochron=91.2,
                 int hasLastPrimordiumAppeared=0):
    """


    UpdatePhase Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: This strategy advances the phase and calculate the final leaf number
    	

    """
    cdef float finalLeafNumber
    cdef float phase1, ttFromLastLeafToHeading, appFLN, localDegfm, ttFromLastLeafToAnthesis
    phase1 = phase
    if (phase1 >= 0.0 and phase1 < 1.0):
        if (switchMaize==0):
            if (cumulTT >= dse):
                phase = 1.0  #Emergence
            else:
                phase = phase1
        else:
            if (cumulTT >= dse):
                phase= 1.0   #Emergence
            else:
                phase = phase1               
    elif (phase1 >= 1.0 and phase1 < 2.0):  #EmergenceToFloralInitiation
        if ((isVernalizable==1 and vernaprog >= 1.0) or (isVernalizable==0)):
            if (switchMaize==0):
                if (dayLength > maxDL):
                    finalLeafNumber = minFinalNumber
                    hasLastPrimordiumAppeared = 1
                else:
                    appFLN = minFinalNumber + sLDL * (maxDL - dayLength)                    
                        # calculation of final leaf number from daylength at inflexion plus 2 leaves
                    if (appFLN / 2.0 <= leafNumber):
                        finalLeafNumber = appFLN
                        hasLastPrimordiumAppeared =1
                    else:
                        phase = phase1
            else:
                hasLastPrimordiumAppeared = 1
                #CheckFloralInitiation
            if (hasLastPrimordiumAppeared==1):              
                    phase = 2.0#Floralinitiation             
        else:
            phase = phase1   
    elif (phase1 >= 2.0 and phase1 < 4.0):#FloralInitiationToAnthesis
        if (isMomentRegistredZC_39==1):
                      #calculate the heading date
            if (phase1 < 3.0):
                ttFromLastLeafToHeading = 0.0
                if(choosePhyllUse=="Default"): ttFromLastLeafToHeading =(pFLLAnth - pHEADANTH) * fixPhyll
                elif (choosePhyllUse == "PTQ"): ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
                elif (choosePhyllUse == "Test"): ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                if (cumulTTFromZC_39 >= ttFromLastLeafToHeading):
                        phase = 3.0
                else:
                    phase = phase1
            else:
                phase = phase1                          
                        #CheckAnthesis;
            ttFromLastLeafToAnthesis =0.0
            if (choosePhyllUse == "Default"): ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
            elif (choosePhyllUse == "PTQ"): ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
            elif (choosePhyllUse == "Test"): ttFromLastLeafToAnthesis = pFLLAnth * p      
            if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis):
                phase = 4.0#Anthesis           
        else:
            phase = phase1            
    elif (phase1 == 4.0):#AnthesisToEndCellDivision          
                    #CheckEndCellDivision
        if (grainCumulTT >= dcd):             
            phase = 4.5#EndCellDivision           
        else:           
            phase = phase1                  
    elif (phase1 == 4.5):#EndCellDivisionToEndGrainFill    
                    # CheckEndGrainFilling
        if (grainCumulTT >= dgf or gai <= 0.0):          
            phase = 5.0#End of grain filling        
        else:         
            phase = phase1      
    elif (phase1 >= 5.0 and phase1 < 6.0):#EndGrainFillToMaturity
                    #CheckMaturity
                    #/<Comment>To enable ignoring grain maturation duration</Comment>
        localDegfm = degfm
        if ignoreGrainMaturation: localDegfm = -1.0       
        if (cumulTTFromZC_91 >= localDegfm ):        
            phase = 6.0 #maturity               
        else:        
            phase= phase1     
    elif (phase1>= 6.0 and phase1 < 7.0):     
        phase = phase1
    return  finalLeafNumber, phase, hasLastPrimordiumAppeared
