using System;
using System.Collections.Generic;
public class Fibonacci_
{
    public static int fibonacci_(int n)
    {
        //- Description:
    //            - Model Name: fibonacci function
    //            - Author: Pierre Martre
    //            - Reference:  to write in package
    //            - Institution: INRA Montpellier
    //            - Abstract: see documentation
        //- inputs:
    //            - name: n
    //                          - description : argument
    //                          - datatype : INT
    //                          - inputtype : variable
        //- outputs:
    //            - name: result
    //                          - description :  fibonacci number 
    //                          - datatype : INT
        int result;
        int b;
        int temp;
        int i;
        result = 0;
        b = 1;
        for (i=0 ; i<n ; i+=1)
        {
            temp = result;
            result = b;
            b = temp + b;
        }
        return result;
    }
}