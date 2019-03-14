
cdef float  nextstartExpTT, nexttipTT, abl, tt_lim_lip, bbl, tt_bl
ntip=0.0   
if (phase == 1.0 and cumulTTPhenoMaizeAtEmergence == 0.0):
    cumulTTPhenoMaizeAtEmergence = cumulTT        
if (phase >= 1.0 and phase< 4.0):       
    if (hasFlagLeafLiguleAppeared==0): 
        if (switchMaize==0):            
            if (phyllochron == 0.0):
                phyllochron = 0.0000001
            leafNumber = leafNumber + min(deltaTT / phyllochron, 0.999)
            ntip=0.0
        else:
            if (leafNumber < leaf_tip_emerg):
                leafNumber = leaf_tip_emerg        
            else:
                nextstartExpTT = 0.0
                nexttipTT = ((leafNumber + 1) - leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence
                abl = k_bl * atip
                tt_lim_lip = ((nlim - leaf_tip_emerg) / atip) + cumulTTPhenoMaizeAtEmergence
                bbl = nlim - (abl * tt_lim_lip)
                tt_bl = ((leafNumber + 1) - bbl) / abl
                if (tt_bl > nexttipTT):
                    nextstartExpTT = nexttipTT
                else:     
                    nextstartExpTT = tt_bl    
                if (cumulTT >= nextstartExpTT):  
                    leafNumber = leafNumber + 1    
                
            ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + leaf_tip_emerg
