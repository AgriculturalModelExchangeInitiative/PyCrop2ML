# coding: utf8
from pycropml.transpiler.main import Main
source =u"""def test(int a):
        cdef list g=[10,1,7]
        cdef int x=1
        cdef float s= 0.9
        cdef list e
        cdef str h
        return a"""
    
output_cs="""using System;
using System.Collections.Generic;
public class Program
{
    static int test(int a)
    {
        List<int> g= new List<int>{10, 1, 7};
        int x = 1;
        double s = 0.9d;
        var e = new List()
        string h;
        return a;
    }
}"""
  
def testDeclaration():
   
    test=Main(source, "py")
    test.parse() 
    
    test.to_ast(source)    
    code=test.to_source()
    print(code)
    assert(str(code)==output_cs)   

if __name__=='__main__':
    testDeclaration()
