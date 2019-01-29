double Phyllochron;
if choosePhyllUse =="Default"
{
	if (LeafNumber < Ldecr) Phyllochron = Fixphyll * Pdecr;
	else if (LeafNumber >= Ldecr && LeafNumber < Lincr) Phyllochron = Fixphyll;
	else Phyllochron = Fixphyll * Pincr;
}        
 
if choosePhyllUse =="PTQ"
{
    pastMaxAI1 = pastMaxAI;
    GAI = Math.Max(pastMaxAI1,GAI);
    pastMaxAI = GAI;
    if (GAI > 0.0) Phyllochron = PhylPTQ1 * ((GAI * Kl) / (1 - Math.Exp(-Kl * GAI))) / (PTQ + aPTQ);
    else Phyllochron = PhylPTQ1;
     
}        
if choosePhyllUse == "Test"
{
    if (LeafNumber < Ldecr) Phyllochron = P * Pdecr;
    elif (LeafNumber >= Ldecr and LeafNumber < Lincr)  Phyllochron = P;
    else Phyllochron = P * Pincr;
}       

    
 
