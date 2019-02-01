# coding: utf8
from pycropml.transpiler.main import Main
source = """def test(int a):
        cdef list g=[14,15,12,12]
        cdef int i
        a=12
        for i in g:
            a=a+i 
        return a
        """ 
output_cs="""using System;
using System.Collections.Generic;
public class Program
{
    static int test(int a)
    {
        List<int> g= new List<int>{14, 15, 12, 12};
        int i;
        a = 12;
        foreach(int i in g)
        {
            a = a + i;
        }
        return a;
    }
}"""
  
def test_for_statement():
   
    test=Main(source, "cs")
    test.parse()    
    test.to_ast(source)    
    code=test.to_source()
    print(code)
    assert(code==output_cs)   

if __name__=='__main__':
    test_for_statement()
