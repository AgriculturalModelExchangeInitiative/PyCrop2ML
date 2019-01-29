

double leafNumber1, nextstartExpTT, nexttipTT, abl, tt_lim_lip, bbl, tt_bl;
ntip = 0;
leafNumber1 =leafNumber;		
if (phase == 1 && cumulTTPhenoMaizeAtEmergence == 0)
{
	cumulTTPhenoMaizeAtEmergence = cumulTT;			
}		
if (phase >= 1 && phase< 4)
{
	if (hasFlagLeafLiguleAppeared==0)//sowingToAnthesis
	{
		if (switchMaize==0)
		{
			if (phyllochron == 0.0)
			{
				phyllochron = 0.0000001;		
			}
			leafNumber = leafNumber1 + Math.Min(deltaTT / phyllochron, 0.999);
		}
		else
		{		
			if (leafNumber1 < leaf_tip_emerg)
			{
				leafNumber = leaf_tip_emerg;
			}
			else
			{		
				nextstartExpTT = 0;
				nexttipTT = ((leafNumber1 + 1) - leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence;
				abl = k_bl * atip;
				tt_lim_lip = ((nlim - leaf_tip_emerg) / atip) + cumulTTPhenoMaizeAtEmergence;
				bbl = nlim - (abl * tt_lim_lip);
				tt_bl = ((leafNumber1 + 1) - bbl) / abl;
				if (tt_bl > nexttipTT)
				{
					nextstartExpTT = nexttipTT;
				}
				else
				{
					nextstartExpTT = tt_bl;
				}
				if (cumulTT>= nextstartExpTT)
				{
					leafNumber = leafNumber1 + 1;
				}
				else
				{
					leafNumber = leafNumber1;
				}
			}
			ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + leaf_tip_emerg;
		}
	}
}