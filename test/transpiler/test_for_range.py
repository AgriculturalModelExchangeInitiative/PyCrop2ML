# coding: utf8
from pycropml.transpiler.main import Main

source = """def test(int a):
        cdef int x=15, y=15
        cdef int i
        a=12
        for i in range(0,10,1):
            a=a+i 
        return a
        """
output_cs="""using System;
using System.Collections.Generic;
public class Program
{
    static int test(int a)
    {
        int x = 15;
        int y = 15;
        int i;
        a = 12;
        for (i=0 , i<10 , i+=1)
        {
            a = a + i;
        }
        return a;
    }
}"""
  
def test_for_range():
   
    test=Main(source, "cs")
    test.parse()    
    test.to_ast(source)    
    code=test.to_source()
    print(code)
    assert(code==output_cs)   

if __name__=='__main__':
    test_for_range()
