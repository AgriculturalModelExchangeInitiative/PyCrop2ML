LeafNumber1 =LeafNumber
Ntip=0
    
if (phase == 1 and cumulTTPhenoMaizeAtEmergence == 0):
    cumulTTPhenoMaizeAtEmergence = cumulTT
        
if (phase >= 1 and phase< 4):
        
    if (HasFlagLeafLiguleAppeared==0): 
        if (SwitchMaize==0):
            
            if (Phyllochron == 0.0):
                Phyllochron = 0.0000001
            LeafNumber = LeafNumber1 + min(DeltaTT / Phyllochron, 0.999)
            Ntip=0
        else:
            if (LeafNumber1 < Leaf_tip_emerg):
                LeafNumber = Leaf_tip_emerg
                
            else:
                nextstartExpTT = 0

                nexttipTT = ((LeafNumber1 + 1) - Leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence

                abl = k_bl * atip
                tt_lim_lip = ((Nlim - Leaf_tip_emerg) / atip) + cumulTTPhenoMaizeAtEmergence
                bbl = Nlim - (abl * tt_lim_lip)

                tt_bl = ((LeafNumber1 + 1) - bbl) / abl
                if (tt_bl > nexttipTT):
                    nextstartExpTT = nexttipTT
                else:
                    
                    nextstartExpTT = tt_bl
                    
                if (cumulTT >= nextstartExpTT):
                    
                    LeafNumber = LeafNumber1 + 1
                    
                else:
                    
                    LeafNumber = LeafNumber1
                    
                
            Ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + Leaf_tip_emerg
