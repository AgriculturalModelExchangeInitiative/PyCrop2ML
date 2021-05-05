# Snow depth calculation
if(Snowmelt  <= (Sdepth_in+Snowaccu/100)): 
    Sdepth=(Snowaccu/100+Sdepth_in-Snowmelt-(Sdepth_in*P_E)