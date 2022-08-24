
    public class CanopyTemperature : IStrategyEnergyBalance
    {
        public CanopyTemperature()
        {
            //Parameters
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 2.454;
            v1.Description = "latent heat of vaporization of water";
            v1.Id = 0;
            v1.MaxValue = 10;
            v1.MinValue = 0;
            v1.Name = "lambdaV";
            v1.Size = 1;
            v1.Units = "MJ/kg";

            //Inputs
            PropertyDescription pd1 = new PropertyDescription();
            pd1.PropertyName = "minTair";
            pd1.PropertyVarInfo =(EnergyBalance.DomainClass.EBAuxVarInfo.minTair);

            //Outputs
        } 
    }
