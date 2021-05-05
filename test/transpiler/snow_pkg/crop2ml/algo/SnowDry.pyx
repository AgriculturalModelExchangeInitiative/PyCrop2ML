if (M  <= Sdry_in) :
    tmp_sdry=Snowaccu+Mrf-M+Sdry_in
    if (tmp_sdry  < 0.): 
        Sdry=0.001
    else:
        Sdry=tmp_sdr