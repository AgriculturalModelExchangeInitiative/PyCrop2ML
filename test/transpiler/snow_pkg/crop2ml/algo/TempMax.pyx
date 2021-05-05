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