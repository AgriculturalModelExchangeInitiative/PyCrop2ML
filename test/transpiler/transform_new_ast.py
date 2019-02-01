from pycropml.transpiler.main import Main
from path import Path

file = Path.getcwd()/"test"/"transpiler"/"data"/"example2.pyx"
with open(file, 'r') as fi:
    source = fi.read()

test=Main(file, "cs")

tree=test.parse()

nodeAst = test.to_ast(source) 

code=test.to_source()

print(code)

result = """using System;
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
assert(str(code)==result)   

