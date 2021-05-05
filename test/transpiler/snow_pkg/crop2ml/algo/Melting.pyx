# M calculation
K=(P_DKmax/2.)*(-sin((2.*pi*float(jul)/366.)+(9./16.)*pi)) +P_Kmin+(P_DKmax/2.)

if ( tavg  > P_Tmf ): 
    M = K * ( tavg - P_Tmf )