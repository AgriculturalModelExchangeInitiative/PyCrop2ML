
# Calculating average temperature
tavg = (tmax+tmin)/2.

############################################################################
#                     Snow variables calculation                           #
############################################################################

# Snow accumulation (unit cm)
if (tmax < P_tsmax): fs=1.
if ((tmax >= .P_tsmax) and (tmax  <= P_trmax)):
    fs=(P_trmax-tmax)/(P_trmax-P_tsmax)
Snowaccu=fs*precip  

# M calculation
K=(P_DKmax/2.)*(-sin((2.*pi*float(jul)/366.)+(9./16.)*pi)) +P_Kmin+(P_DKmax/2.)

if ( tavg  > P_Tmf ): 
    M = K * ( tavg - P_Tmf )

# Mrf calculation
if ( tavg  < P_Tmf ): 
    Mrf = P_SWrf * ( P_Tmf - tavg )

# Snow dry  calculation
if (M  <= Sdry_in) :
    tmp_sdry=Snowaccu+Mrf-M+Sdry_in
    if (tmp_sdry  < 0.): 
        Sdry=0.001
    else:
        Sdry=tmp_sdry

if (Mrf  <= Swet_in) :
    tmp_swet=Swet_in+(precip-Snowaccu)+M-Mrf
    frac_sdry=0.1*Sdry
    if (tmp_swet  < frac_sdry):
        Swet=tmp_swet
    else:
        Swet=frac_sdry

# ps calculation
if ( ABS(Sdepth_in)  > 0. ):
    if ( ABS( Sdry_in +  Swet_in )  > 0. ):
        ps = ( Sdry_in +  Swet_in )  / Sdepth_in
    else:
        ps=ps_in

# Snow melt calculation
if( ps  > 0. ):
    Snowmelt = M  / ps

# Snow depth calculation
if(Snowmelt  <= (Sdepth_in+Snowaccu/100)): 
    Sdepth=(Snowaccu/100+Sdepth_in-Snowmelt-(Sdepth_in*P_E))


############################################################################
#                Meteorological data calculation                           #
############################################################################

# Precipitations
if ((Sdry+Swet)  < (Sdry_in+Swet_in)):
    preciprec=preciprec+(Sdepth_in-Sdepth)*100-Mrf
preciprec=preciprec-Snowaccu

# Sdepth unit transformation m -> cm
Sdepth_cm=Sdepth*P_Pns

# Minimum temperature calculation
if (Sdepth_cm  > P_prof):
    if(tmin  < P_tminseuil):
        tminrec=P_tminseuil
    else:
        if (tmin  > P_tmaxseuil):
            tminrec=P_tmaxseuil
else
    if (Sdepth_cm  > 0.) :
        tminrec=P_tminseuil-(1-(Sdepth_cm/P_prof))*(ABS(tmin)+P_tminseuil)

# Maximum temperature  calculation
if (Sdepth_cm  > P_prof):
    if(tmax  < P_tminseuil):
        tmaxrec=P_tminseuil
    else
        if (tmax  > P_tmaxseuil):
            tmaxrec=P_tmaxseuil

else
    if (Sdepth_cm  > 0.):
        if (tmax  <= 0.) then
            tmaxrec=P_tmaxseuil-(1-(Sdepth_cm/P_prof))*(-tmax)
        else
            tmaxrec=0.
