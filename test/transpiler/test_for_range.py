# coding: utf8
from pycropml.transpiler.main import Main

source =u"""def test(int a):
        cdef int x=15, y=15
        cdef int i
        a=12
        for i in range(0,10,1):
            a=a+i 
        return a
        """
output_cs=u"""using System;
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

output_py=u"""def test(a):
    x = 15
    y = 15
    a = 12
    for i in range(0 , 10 , 1):
        a = a + i
    return a"""

languages=["py","cs"]
output={"py":output_py, "cs":output_cs}        
  
def test_for_range():
    for lang in languages:   
        test=Main(source, lang)
        test.parse()    
        test.to_ast(source)    
        code=test.to_source()
        print(code)
        assert(code==output[lang])

if __name__=='__main__':
    test_for_range()
