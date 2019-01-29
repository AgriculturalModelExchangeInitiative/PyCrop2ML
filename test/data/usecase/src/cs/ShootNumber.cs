
int OldCanopyShootNumber = CanopyShootNumber;
EmergedLeaves = (int)Math.Max(1, Math.Ceiling(LeafNumber - 1));
Shoots = fibonacci(EmergedLeaves);

CanopyShootNumber = Math.Min(Shoots * SowingDensity, TargetFertileShoot);
AverageShootNumberPerPlant = CanopyShootNumber / SowingDensity;

if (CanopyShootNumber != OldCanopyShootNumber)
{
	tilleringProfile.Add(CanopyShootNumber - OldCanopyShootNumber);
}
		
TillerNumber = tilleringProfile.Count;
		
for (int i = leafTillerNumberArray.Count; i < Math.Ceiling(LeafNumber); i++)
{
	leafTillerNumberArray.Add(TillerNumber);
}
