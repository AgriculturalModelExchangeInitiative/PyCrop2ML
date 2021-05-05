# ps calculation
if ( abs(Sdepth_in)  > 0. ):
    if ( abs( Sdry_in +  Swet_in )  > 0. ):
        ps = ( Sdry_in +  Swet_in )  / Sdepth_in
    else:
        ps=ps_in
