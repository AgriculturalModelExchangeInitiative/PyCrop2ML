phase1 = phase

if (phase1 >= 0 and phase1 < 1):
    if (SwitchMaize==0):
        if (cumulTT >= Dse):
            phase = 1#Emergence
        else:
            phase = phase1
    else:
        if (cumulTT >= Dse):
            phase= 1#Emergence
        else:
            phase = phase1
                
elif (phase1 >= 1 and phase1 < 2):#EmergenceToFloralInitiation
    if ((IsVernalizable==1 and Vernaprog >= 1) or (IsVernalizable==0)):
        if (SwitchMaize==0):
            if (DayLength > MaxDL):
                FinalLeafNumber = MinFinalNumber
                hasLastPrimordiumAppeared = 1
            else:
                appFLN = MinFinalNumber + SLDL * (MaxDL - DayLength)
                    
                    # calculation of final leaf number from daylength at inflexion plus 2 leaves
                if (appFLN / 2.0 <= LeafNumber):
                    FinalLeafNumber = appFLN
                    hasLastPrimordiumAppeared =1
                else:
                    phase = phase1

        else:
            hasLastPrimordiumAppeared = 1
                

            #CheckFloralInitiation
        if (hasLastPrimordiumAppeared==1):
                
                phase = 2#Floralinitiation
                
    else:
        phase = phase1
            
        
elif (phase1 >= 2 and phase1 < 4):#FloralInitiationToAnthesis
    if (isMomentRegistredZC_39==1):
            
                #calculate the heading date
        if (phase1 < 3):
            ttFromLastLeafToHeading = 0.0
            if(choosePhyllUse=="Default"): ttFromLastLeafToHeading =(PFLLAnth - PHEADANTH) * Fixphyll
            elif (choosePhyllUse == "PTQ"): ttFromLastLeafToHeading = (PFLLAnth - PHEADANTH) * Phyllochron
            elif (choosePhyllUse == "Test"): ttFromLastLeafToHeading = (PFLLAnth - PHEADANTH) * P

            if (cumulTTFromZC_39 >= ttFromLastLeafToHeading):
                    phase = 3
            else:
                phase = phase1
        else:
            phase = phase1
                                 
                    #CheckAnthesis;
        ttFromLastLeafToAnthesis =0.0
        if (choosePhyllUse == "Default"): ttFromLastLeafToAnthesis = PFLLAnth * Fixphyll
        elif (choosePhyllUse == "PTQ"): ttFromLastLeafToAnthesis = PFLLAnth * Phyllochron
        elif (choosePhyllUse == "Test"): ttFromLastLeafToAnthesis = PFLLAnth * P
        
            
        if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis):
            phase = 4#Anthesis
                
    else:
        phase = phase1
            
elif (phase1 == 4):#AnthesisToEndCellDivision
            
                #CheckEndCellDivision
    if (GrainCumulTT >= Dcd):
                
        phase = 4.5#EndCellDivision
                
    else:
                
        phase = phase1
                
            
elif (phase1 == 4.5):#EndCellDivisionToEndGrainFill
            
                # CheckEndGrainFilling
    if (GrainCumulTT >= Dgf or GAI <= 0):
                
        phase = 5#End of grain filling
                
    else:
                
        phase = phase1
                

            
elif (phase1 >= 5 and phase1 < 6):#EndGrainFillToMaturity
            
                #CheckMaturity
                #/<Comment>To enable ignoring grain maturation duration</Comment>
    LocalDegfm = Degfm
    if (IgnoreGrainMaturation==True): LocalDegfm = -1
                
    if (cumulTTFromZC_91 >= LocalDegfm ):
                
        phase = 6 #maturity
            
                
    else:
                
        phase= phase1
         

            
elif (phase1>= 6 and phase1 < 7):
            
    phase = phase1
    
    
    
    