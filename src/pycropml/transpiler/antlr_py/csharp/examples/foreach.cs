
using System;
public class IterateSpanExample
{
    public Double psychrometricConstant
	{ 
		get {
			    VarInfo vi= _modellingOptionsManager.GetParameterByName("psychrometricConstant");
				if (vi != null && vi.CurrentValue!=null) return (Double)vi.CurrentValue ;
				else throw new Exception("Parameter 'psychrometricConstant' not found (or found null) in strategy 'CalculatePenman'");
		} set {
				VarInfo vi = _modellingOptionsManager.GetParameterByName("psychrometricConstant");
				if (vi != null)  vi.CurrentValue=value;
				else throw new Exception("Parameter 'psychrometricConstant' not found in strategy 'CalculatePenman'");
			}
	}
    private PublisherData _pd;
    public PublisherData PublisherData
	{
		get { return _pd; }
	}

    public IEnumerable<Type> GetStrategyDomainClassesTypes()
	{
		return new List<Type>() {  typeof(SiriusQualityEnergyBalance.EnergyBalanceState) };
	}

    public static void foreach_test()
    {
        List<int> fibNumbers = new List<int> { 0, 1, 1, 2, 3, 5, 8, 13 };
        int g, count = 0;
        string z = "jjj";
        double e = 70.5d, s;
        s = Math.Cos(e);
        s = Math.Sin(20.5d);
        s = Math.Exp(s) + Math.Sin(20.5d);
        List<int> primeNumbers = new List<int>();
        primeNumbers.Add(1); // adding elements using add() method
        primeNumbers.Add(3);
        g = primeNumbers.Count;
        //e = Math.Cos(20.5d);

        List<string> cities = new List<string>();
        cities.Add("New York");
        cities.Add("London");

        //adding elements using collection-initializer syntax
        /*var bigCities = new List<string>()
                    {
                        "New York",
                        "London",
                        "Mumbai",
                        "Chicago"                    
                    };*/
        /*foreach (int element in fibNumbers)
        {
            int ff = 2;
            //Console.WriteLine($"Element #{count}: {element}");
            //count++;
            count = count +1;
        }*/
        //Console.WriteLine($"Number of elements: {count}");
    }
}