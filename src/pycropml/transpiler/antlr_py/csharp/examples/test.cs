	public class CalculatePenman : IStrategySiriusQualityEnergyBalance
	{


			public CalculatePenman()
			{
				
				List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
				PropertyDescription pd1 = new PropertyDescription();
				pd1.DomainClassType = typeof(SiriusQualityEnergyBalance.EnergyBalanceState);
				pd1.PropertyName = "evapoTranspirationPriestlyTaylor";
				pd1.PropertyType = (( SiriusQualityEnergyBalance.EnergyBalanceStateVarInfo.evapoTranspirationPriestlyTaylor)).ValueType.TypeForCurrentValue;
				pd1.PropertyVarInfo =( SiriusQualityEnergyBalance.EnergyBalanceStateVarInfo.evapoTranspirationPriestlyTaylor);
				_inputs0_0.Add(pd1);
                
                
                ModellingOptions mo0_0 = new ModellingOptions();
				//Parameters
				List<VarInfo> _parameters0_0 = new List<VarInfo>();
				VarInfo v1 = new VarInfo();
				 v1.DefaultValue = 0.66;
				 v1.Description = "psychrometric constant";
				 v1.Id = 0;
				 v1.MaxValue = 1;
				 v1.MinValue = 0;
				 v1.Name = "psychrometricConstant";
				 v1.Size = 1;
				 v1.Units = "?";
				 v1.URL = "";
				 v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
				 v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
				 _parameters0_0.Add(v1);
				VarInfo v2 = new VarInfo();
				 v2.DefaultValue = 1.225;
				 v2.Description = "Density of air";
				 v2.Id = 0;
				 v2.MaxValue = 10;
				 v2.MinValue = 0;
				 v2.Name = "rhoDensityAir";
				 v2.Size = 1;
				 v2.Units = "?";
				 v2.URL = "";
				 v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
				 v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
					
			}
    }