double Ntip;
Ntip = 0;
double LeafNumber1;
LeafNumber1 =LeafNumber;
		
if (phase == 1 && cumulTTPhenoMaizeAtEmergence == 0)
{
	cumulTTPhenoMaizeAtEmergence = cumulTT;
			
}
		
if (phase >= 1 && phase< 4)
{
	if (HasFlagLeafLiguleAppeared==0)//sowingToAnthesis
	{
		if (SwitchMaize==0)
		{
			if (Phyllochron == 0.0)
			{
				Phyllochron = 0.0000001;
					
			}
			LeafNumber = LeafNumber1 + Math.Min(DeltaTT / Phyllochron, 0.999);
		}
		else
		{
				
			if (LeafNumber1 < Leaf_tip_emerg)
			{
				LeafNumber = Leaf_tip_emerg;
			}
			else
			{
					
				double nextstartExpTT = 0;

				double nexttipTT = ((LeafNumber1 + 1) - Leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence;

				double abl = k_bl * atip;
				double tt_lim_lip = ((Nlim - Leaf_tip_emerg) / atip) + cumulTTPhenoMaizeAtEmergence;
				double bbl = Nlim - (abl * tt_lim_lip);

				double tt_bl = ((LeafNumber1 + 1) - bbl) / abl;
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
					LeafNumber = LeafNumber1 + 1;
				}
				else
				{
					LeafNumber = LeafNumber1;
				}
			}
			Ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + Leaf_tip_emerg;
		}
	}
}