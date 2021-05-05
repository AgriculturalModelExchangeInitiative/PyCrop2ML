# Snow accumulation (unit cm)
if (tmax < P_tsmax): fs=1.
if ((tmax >= .P_tsmax) and (tmax  <= P_trmax)):
    fs=(P_trmax-tmax)/(P_trmax-P_tsmax)
Snowaccu=fs*precip 