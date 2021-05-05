if (Sdepth_cm  > P_prof):
    if(tmin  < P_tminseuil):
        tminrec=P_tminseuil
    else:
        if (tmin  > P_tmaxseuil):
            tminrec=P_tmaxseuil
else
    if (Sdepth_cm  > 0.) :
        tminrec=P_tminseuil-(1-(Sdepth_cm/P_prof))*(ABS(tmin)+P_tminseuil)
