if choosePhyllUse =="Default":
    if (LeafNumber < Ldecr): Phyllochron = FixPhyll * Pdecr
    elif (LeafNumber >= Ldecr and LeafNumber < Lincr): Phyllochron = Fixphyll
    else: Phyllochron = FixPhyll * Pincr
        
 
if choosePhyllUse =="PTQ":
    pastMaxAI1 = pastMaxAI
    GAI = max(pastMaxAI1,GAI)
    pastMaxAI = GAI
    if (GAI > 0.0): Phyllochron = PhylPTQ1 * ((GAI * Kl) / (1 - exp(-Kl * GAI))) / (PTQ + aPTQ)
    else: Phyllochron = PhylPTQ1
     
        
if choosePhyllUse == "Test":
    if (LeafNumber < Ldecr): Phyllochron = P * Pdecr
    elif (LeafNumber >= Ldecr and LeafNumber < Lincr): Phyllochron = P
    else: Phyllochron = P * Pincr
        

    
 
