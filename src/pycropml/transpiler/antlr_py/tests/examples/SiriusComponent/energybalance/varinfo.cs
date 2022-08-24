  

    public class EBAuxVarInfo : IVarInfoClass
    {
        static VarInfo _minTair = new VarInfo();
        public static  VarInfo minTair
        {
            get { return _minTair;}
        }
        static void DescribeVariables()
        {
            _minTair.Name = "minTair";
            _minTair.Description = "min air temperature";
            _minTair.MaxValue = 45;
            _minTair.MinValue = -30;
            _minTair.DefaultValue = 0.7;
            _minTair.Units = "degC";
        }
    }


