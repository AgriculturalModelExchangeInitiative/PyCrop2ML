# coding: utf8
from pycropml.transpiler.main import Main
source =u"""def test(int a):
        cdef int x=1, y=2
        if x==y:
            if x<2:
                return a+2
            elif x>10:
                return x+a
            else:
                return x
        else:
            return a
        """ 
output_cs=u"""using System;
using System.Collections.Generic;
public class Program
{
    static int test(int a)
    {
        int x = 1;
        int y = 2;
        if (x == y)
        {
            if (x < 2)
            {
                return a + 2;
            }
            elseif ( x > 10)
            {
                return x + a;
            }
            else
            {
                return x;
            }
        }
        else
        {
            return a;
        }
    }
}"""
  
def test_if_elif_else():
   
    test=Main(source, "cs")
    test.parse()    
    test.to_ast(source)    
    code=test.to_source()
    print(code)
    assert(code==output_cs)   

if __name__=='__main__':
    test_if_elif_else()



# coding: utf8
from pycropml.transpiler.main import Main
source =u"""def test(int a):
        cdef int x=1, y=2
        x=2
        return a"""
test=Main(source, "cs")
test.parse()    
test.to_ast(source) 