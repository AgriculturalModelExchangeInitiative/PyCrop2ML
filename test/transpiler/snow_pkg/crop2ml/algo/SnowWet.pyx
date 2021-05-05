if (Mrf  <= Swet_in) :
    tmp_swet=Swet_in+(precip-Snowaccu)+M-Mrf
    frac_sdry=0.1*Sdry
    if (tmp_swet  < frac_sdry):
        Swet=tmp_swet
    else:
        Swet=frac_sdry