using System;

public class Test
{
    public static double test(double b)
    {
        int[] k = {2,2};
        //List<int[]> hh = new List<int[]>{k, k};
        //b = test2(10.5d);
        if(b>10.2) 
        {
               b=2.3;
        }
        while (b<10.3)
        {
            b = k[1];
        }

        return b;
    }

}
//Console.WriteLine(Test.test(10));