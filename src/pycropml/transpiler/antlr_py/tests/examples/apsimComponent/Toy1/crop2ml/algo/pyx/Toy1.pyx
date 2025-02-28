cdef float SVPfrac = 0.66
cdef float VPDmint = svp(MinT) - VP
VPDmint=max(VPDmint, 0.0)
cdef float VPDmaxt = svp(MaxT) - VP
VPDmaxt=max(VPDmaxt, 0.0)
VPD=SVPfrac * VPDmaxt + ((1 - SVPfrac) * VPDmint)