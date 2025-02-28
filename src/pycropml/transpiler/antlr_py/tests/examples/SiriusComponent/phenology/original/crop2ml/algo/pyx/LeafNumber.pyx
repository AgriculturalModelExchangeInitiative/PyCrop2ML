cdef float phyllochron_ 
leafNumber=leafNumber_t1
if phase >= 1.0 and phase < 4.0:
    if hasFlagLeafLiguleAppeared == 0:
        if phyllochron_t1 == 0.0:
            phyllochron_=0.0000001
        else:
            phyllochron_=phyllochron_t1
        leafNumber=leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)