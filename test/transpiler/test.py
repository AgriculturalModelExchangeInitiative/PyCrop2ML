# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.main import Main


source="""
def fib(bool n):
    cdef bool f
    if not f:
        f = True
    return f

def gib(int n=5):
    cdef int res, res1, res2
    cdef list g=[15,20,13]
    g = g+fib(2)
    for res in g:
        res2 = res + 1
    if res2==10: return res2
    for res in g:
        res2 = res+gib(4)+len(g)
def gh(int n):
    if n==1: return n*0.2
    return gh(n)+2
"""

source="""
from datetime import datetime
def fibonacci(int n, datetime j)-> int:
    
    cdef int res
    cdef list jj=[15]
    cdef datetime h
    cdef int k[5];
    cdef float hh
    hh = 10 + 15
    if jj[0] ==2: res = 5 ; jj[2] = res
    if res==15: h = datetime(2000,1,2)
    res = sum(jj)
    jj[0]=13
    res = jj[0]
    
    res = 5**n
    return res
"""
source='''from units import u
def square(int a, int b):

    #a = b*u.m*u.kg/u.cm**3*m**3
    a = a/u.cm**3 * a/u.cm**3
    a = a+b/u.l*u.cm**3/u.mm**3
    a=a+6
    return a
'''

source = """
def test(int a):
    cdef str j
    cdef int b 
    cdef str currentZadokStage =''
    j=''
    
    return a
"""

source="""
def fib(bool f):
    cdef list h = [15,20]
    cdef int a
    if "2" not in h:
        a = 2    
    return f
"""
source = """from math import ceil
def testo(int b):
    cdef array k = array('i', [6])
    cdef list a =[k,k]
    cdef float hh
    cdef str t ="kkk"
    hh = float(ceil(10.5))
    a = testo2(2)
    return [k,k]  
def testo2(int gg):
    cdef array k = array('i', [5])
    cdef list a =[k,k]
    cdef list j = [15.2,20.2]
    cdef float hh
    hh = j[1]
    return [k,k]  
"""

test=Main(source, 'py')
a=test.parse()  
k=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)

from pycropml.transpiler.antlr_py import test








from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from path import Path
filePath = Path("c:/users/midingoy/documents/Restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/csharp/examples/CalculateGAImean.cs")
nodeAst = to_CASG(filePath,'cs')
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction

z = BiomaExtraction()
p = z.getStrategyVar(nodeAst)

filename = Path("c:/users/midingoy/documents/Restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/csharp/examples/PhenologyStateVarInfo.cs")
nodeAst2 = to_CASG(filename, 'cs')
p2 = z.getFromVarInfo(nodeAst,nodeAst2)
v = z.description(nodeAst)

filename = Path("c:/users/midingoy/documents/Restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/csharp/examples/EnergybalanceComponent.cs")
nodeAst3 = to_CASG(filename, 'cs')
p2 = z.getFromVarInfo(nodeAst,nodeAst2)
v = z.description(nodeAst3)
me = z.getAlgo(nodeAst3)


g = z.getAttNode(nodeAst,z.getTree[0],"decl","VarInfo")
y = z.getAttNode(z.getTree[0],"declaration","type","CalculateModel")
nodeAst = g
from pycropml.transpiler.ast_transform import transform_to_syntax_tree

def test(x, **kwargs):
    x = [j==k for j,k in kwargs.items()]
    if any(x):
        print 
       
    return x



from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.csharp.api_transform import *
from path import Path
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.generators.csharpGenerator import CsharpGenerator
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.antlr_py.createUnit import Pl2Crop2ml


dc =  Path("c:/users/midingoy/documents/Restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/examples/SiriusComponent/phenology/DomainClass")
varInfo = dc.glob('*VarInfo.cs')
vinfoAsg = []
for v in varInfo:
    asg = to_CASG(v, 'cs')
    vinfoAsg.append(asg)


filename = Path("c:/users/midingoy/documents/Restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/examples/SiriusComponent/phenology/Strategies/PhenologyComponent.cs")
nodeAst = to_CASG(filename, 'cs')
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction
z = BiomaExtraction()
a=z.modelcomposite([], nodeAst)
z.getFromVarInfo(nodeAst, vinfoAsg)

x = z.modelunit(nodeAst, vinfoAsg)
z.model.inputs
print(Pl2Crop2ml(z.model,"SQ.PhenoPkg").run())



algo = z.getAlgo(nodeAst)
#exter = z.externFunction(nodeAst)
var =  z.totalvar(nodeAst)


#cd = cs_cyml.Cs_Cyml_ast(exter)

cd = cs_cyml.Cs_Cyml_ast(algo.block, var = var)

cd = cs_cyml.Cs_Cyml_ast(nodeAst)
h = cd.transform()
nd = transform_to_syntax_tree(h)
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
p = CymlGenerator(nd)
p.visit(nd)
z= ''.join(p.result)
print(z)




from pycropml.transpiler.generators.pythonGenerator import PythonGenerator

p = PythonGenerator(nd)
p.visit(nd)
z= ''.join(p.result)
print(z)

from pycropml.transpiler.generators.fortranGenerator import FortranGenerator

p = FortranGenerator(nd)
p.visit(nd)
z= ''.join(p.result)
print(z)
        
from pycropml.transpiler.generators.javaGenerator import JavaGenerator

p = JavaGenerator(nd)
p.visit(nd)
z= ''.join(p.result)
print(z)

        
from pycropml.transpiler.generators.cppGenerator import CppGenerator

p = CppGenerator(nd)
p.visit(nd)
z= ''.join(p.result)
print(z)



from functools import *

h = ["10", "+","12", "-", "15", "+", "1225"]

def reduceT(function, iterable, initializer=None):
    iterable_new = [j for i, j in enumerate(iterable) if i%2!=1]
    op = [j for i, j in enumerate(iterable) if i%2==1]
    it = iter(iterable_new)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for k,element in enumerate(it):
        value = function(value, element, op[k])
    return value

reduceT(lambda x,y,op: {"type":"binary_op", "op":op, "left":x, "right":y}, h)


from sympy.parsing.sympy_parser import parse_expr

from pycropml.units import *
def square(n = [15],
         v:u.cm=2):
    res = 0
    jj = []
    a = Float(2 *v* 5 * u.cm / u.kg * pow(u.m, 3))
    #a=5*u.cm
    return a


A = type('A', (), {'x': 1})

B = type('B', ('A'), {'R': 1})


source = u"""import numpy 
from math import *
def cumulttfrom(int h):
    cdef:
        int j
        struct yy:
            int hf
        struct color:
            int x
            int y
            yy jj
        bool af = True
        color col
        int g[2]
    col.jj.hf = 6
    col.x = 2
    col.y = 6
    return  j"""
    
source = u"""from math import sum, pi
def mean(intlist x):
    cdef int y, i
    cdef list f=[15,20]
    y = sum(x)+int(pi)
    for i in f:
        y = y + i
    return y
"""
source = u"""from math import sum
def mean(intlist x):
    cdef int y, i=1
    cdef list f=[15,20]
    y = sum(x)
    cdef int h
    for i in f:
        y = y + i
    return y
"""



source = """from math import pi, exp, sqrt
def pdf(float x): 
    cdef float y
    y = exp(-x*x / 2) / sqrt(2 * pi)
    return y

#(x, mu, signma) = Gaussian pdf with mean mu and stddev sigma
def pdf2(float x, float mu, float sigma):
    cdef float y
    y = pdf((x - mu) / sigma) / sigma
    return y

#return cdf(z) = standard Gaussian cdf using Taylor approximation
def cdf(float z):
    cdef float sum, term, xx
    cdef int i
    if (z < -8.0):
        sum = 0.0
    if (z >  8.0):
        sum = 1.0
    sum = 0.0
    term = z;
    if term!=sum:
        xx = sum+0
    else: xx=sum+1
    for i in range(3, int(xx), 2):
        sum  = sum + term
        term = term * z * z / i
        if term!=sum:
            xx = sum+0
        else: xx=sum+1
    sum = 0.5 + sum * pdf(z)
    return sum

# return cdf(z, mu, sigma) = Gaussian cdf with mean mu and stddev sigma
def cdf2(float z, float mu, float sigma):
    cdef float y
    y = cdf((z - mu) / sigma)
    return y

def inverseCDF(float y, float delta, float lo, float hi):
    cdef float mid, res
    mid = lo + (hi - lo) / 2;
    if (hi - lo < delta):
        res = mid
    if (cdf(mid) > y):
        res = inverseCDF(y, delta, lo, mid)
    else:
        res =  inverseCDF(y, delta, mid, hi)
    return res

#Compute z such that cdf(z) = y via bisection search
def inverseCDF2(float y):
    cdef float res
    res = inverseCDF(y, 0.00000001, -8., 8.);
    return res
"""

source = """from datetime import datetime

def t(float y,int y) -> list[int]:
 '''hhhh
 '''
 # ttttt
 cdef int x, i
 cdef datetime tt
 cdef int yy[3]
 yy[0]=5
 cdef list List=["1","2","3"]
 x=10**6 + int(2./5)
 x = yy[4]
 for i in range(0,len(List),1):
     x=int(List[2])+x
 tt = datetime(2000,10,12)
 return x

"""

source="""
cdef struct bb:
    int ff
def test(int a):
    cdef int res
    cdef struct rr:
        int x
        int y
    cdef struct vv:
        int x
        float y
    cdef vv cal
    cal.x =10
    res = cal.x
    g.append(10.0)
    return res
    
"""
source ="""
def AFGEN1(int n, float xy[n], float t):
    cdef float x1, x2, y1, y2, res
    cdef int i
    res = float("nan")
    if(n>1):
        i = 0
        while (i < n-1 and t >= xy[i]): i = i + 2
        if(i==0): res = xy[1]
        elif (i>n-2): res = xy[i-1]
        else:
            x1 = xy[i-2]; x2 = xy[i];  y1 = xy[i-1]; y2 = xy[i+1]
            res = (y2 - y1)/(x2 - x1) * (t-x1) + y1
    return res
"""
 
source ="""
def sum_(int x[]):
    cdef datetime t
    cdef int i, y=0
    for i in x:
        y = y + i
    return y
"""
source ="""
def fib_(int n):
    cdef int i, y
    if n<=1: return n
    else: return fib_(n-1)+fib_(n-2) 
"""

source="""
def select(intlist x):
    cdef intlist y
    cdef int e
    cdef float j
    y = [e for e in x if e!=0]
    j = sum([(e-sum(x))**2/float(len(x)) for e in x if e!=0])
    return y
"""

source="""
def select(intlist x):
    cdef intlist y
    cdef str k
    cdef float ll
    cdef int e
    cdef int yy[5]
    cdef bool ee
    cdef datetime toto
    for e in x:
        if e!=0:
            y.append(e)
    return y
"""
source="""from datetime import datetime
def select(intlist x):
    cdef list y =[14,25]
    cdef floatlist y2
    cdef stringlist y3
    cdef booleanlist y4
    cdef str k = "taatta"
    cdef float ll
    cdef int e
    cdef int yy[5]
    cdef bool ee
    cdef datetime toto
    toto = datetime(2000,10,12)
    for e in x:
        if e!=0:
            y.append(e)
    print(y)
    return y
"""


source="""
def test(int n):
    cdef int x,y,z
    cdef list r=[(0,0,0)]
    r = [(x,y,z) for x in range(1,n+1) for y in range(x,n+1) for z in range(y,n+1) if x**2 + y**2 == z**2]
    return r
"""
source="""cdef int x=4, y=7
cdef int z
cdef list jj=[15,"a"], rr=[20],
cdef intlist h
h = jj+rr
z = (int(float(x)/y))*5


"""
source="""from math import *
from numpy import array
def toto(int x, int y):
    cdef list z = [1,2]
    cdef float zz
    zz = log(10,2)
    
    for x in range(0,20):
        for y in range(x,20):
            print(x)
    return x
"""
source ="""
def generator(str operation):
    if operation == 'add':
       def f(int a, int b):
           return a + b
    else:
       def f(int a, int b):
           return a - b
    return f
cdef int add, sub
add = generator('add')
sub = generator('sub')

"""

source = """

cdef enum CheeseState:
    hard 
    soft = 15
    runny 
cdef int h
    
h = CheeseState.runny

"""

from pycropml import pparse
from path import Path
cropdir = "c:/users/midingoy/documents/these/pycropml_pheno/test/tutorial/pheno_pkg"
model = pparse.model_parser(cropdir)

mod = [mod for mod in model if mod.name.lower() =="ismomentregistredzc_39" ][0]

source = '''from LeafNumber import model_leafnumber

def model_ismomentregistredzc_39(list calendarMoments=['Sowing']):
    cdef int isMomentRegistredZC_39
    cdef float deltaTT=23.5895677277199,
    cdef float phyllochron=0.0,
    cdef int hasFlagLeafLiguleAppeared=0,
    cdef float leafNumber=0.0,leaf
    cdef float phase=1.0
    cdef list cal = ["sowing"]
    """calcul"""
    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments else 0
    leaf = model_leafnumber(True,phyllochron,hasFlagLeafLiguleAppeared,leafNumber,phase)
    return  isMomentRegistredZC_39
'''

test=Main(source, 'cs', models = mod, name=mod.name)
a=test.parse()    
g=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)
import yaml
print(yaml.dump(source))

from hope import jit

@jit
def sum(x, y):
    return x + y


class yy:
    def __init__(self, hf):
        self.hf = hf
        
        
def argsToStr(args):
    t=[]
    for arg in args:
        t.append(str(arg))
    return "%s"%(''.join(t))

tt =[1222,12,2]
argsToStr(tt)

def test (a):
    """
    test
    params: int: a
    
    """
    return a

f = test
    


def testa(a=None, b=None):
    return a+b
def testb(c=None, d=None):
    return d/c

def test(j, a=None, b=None, c=None, d=None):
    if j==1:
        return testa(a, b)
    else: return testb(c, d)

                  


source="""

from math import *
def cumulttfrom(list calendarMoments=['Sowing'],
                      list calendarCumuls=[0.0],
                      float cumulTT=8.0):
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    # initialisation 
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0     
    if "Anthesis" in calendarMoments:
        cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.index("Anthesis")]    
    if "FlagLeafLiguleJustVisible" in calendarMoments:
        cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]  
    if "EndGrainFilling"in calendarMoments:
        cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.index("EndGrainFilling")]
    return  cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91
"""






source ="""
def test (int a):
    cdef dict b={1:2}
    cdef int n
    n = b.get(1)
    return n"""




source = u"""import numpy 
from math import *
def phylsowingdatecorrection(int sowingDay=1,
                                   float latitude=0.0,
                                   float sDsa_sh=1.0,
                                   float rp=0.0,
                                   int sDws=1,
                                   float sDsa_nh=1.0,
                                   float p=120.0):
    cdef float fixPhyll
    if (latitude < 0.0):
        if (sowingDay > int(sDsa_sh)):
            fixPhyll = p * (1 - rp * min(sowingDay - sDsa_sh, sDws, 10.5))
        else:
            fixPhyll = p
    else:
        if (sowingDay < int(sDsa_nh)):
            fixPhyll = p * (1 - rp * min(sowingDay, sDws))
        else:
            fixPhyll = p
    return  fixPhyll"""


from pycropml.transpiler.generators.csharpGenerator import  CsharpTrans
from path import Path
rep = Path("C:/Users/midingoy/Documents/THESE/dss_crop2ml")

from pycropml.pparse import model_parser
mod = model_parser(rep)
def to_struct(models, rep):
    generator = CsharpTrans(models)
    generator.model2Node(models)
    states = generator.node_states
    b=[a.name for a in states]
    print(b)
    generator.generate(states, "state")
    z= ''.join(generator.result)
    filename = rep/"states.cs"
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))
    rates = generator.node_rates
    b=[a.name for a in rates]
    print(b)   
    generator.result=[""]
    generator.generate(rates, "rate")
    z1= ''.join(generator.result)
    filename = rep/"rates.cs"
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))
    auxiliary = generator.node_auxiliary
    b=[a.name for a in auxiliary]
    print(b) 
    generator.result=[""]
    generator.generate(auxiliary, "auxiliary")
    z2= ''.join(generator.result)
    filename = rep/"auxiliary.cs"
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))
        
    return 0



    '''rates = generator.node_rates
    generator.generate(rates)
    z= ''.join(generator.result)
    filename = rep/"rates.cs"
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))  
    auxiliary = generator.node_auxiliary
    generator.generate(auxiliary)
    z= ''.join(generator.result)
    filename = rep/"auxiliary.cs"
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))  '''  

from path import Path
filename = Path("c:/users/midingoy/documents/these/pycropml_pheno/src/pycropml/transpiler/antlr_py/testcs.cs")
import sys
from antlr4 import *
from pycropml.transpiler.antlr_py import CSharpParserVisitor,CSharpParserListener, CSharpLexer, CSharpParser
with open(filename, "r") as tg_file:
    z = tg_file.read()  

input_stream = FileStream(filename)   

lexer = CSharpLexer.CSharpLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CSharpParser.CSharpParser(stream)
z=parser.compilation_unit()

from pycropml.transpiler.antlr_py import *
from pycropml.transpiler.antlr_py import parse

tree = parsef(filename, start="compilation_unit", strict=False)

ast_proc = process_tree(tree)

dump_node()
x = 15
def t(n):
    return x+n





from pycropml import render_python


from path import Path
direct = Path("C:/Users/midingoy/Documents/THESE/dss_crop2ml")
from pycropml.pparse import model_parser
models = model_parser(direct)

dir2 = direct/'src'/'py'
models = model_parser(direct)
nrj=render_python.Model2Package(models, dir2, "nrj")
nrj.generate_package()
nrj.generate_wralea()


def test1(a=6,b=5):
    return a+b

def test2(a=10, b=1):
    return a-1

switcher={
        1: test1,
        2: test2}



def test(a):
    print(a)

def test(a, b):
    print(a, b)

x = 20
def toto():
    x=15
    return x


n=20
def triplets(n):
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            for z in range(y, n + 1):
                yield x, y, z
[(x, y, z) for (x, y, z) in triplets(n) if x**2 + y**2 == z**2]

[(x,y,z) for x in range(1,n+1) for y in range(x,n+1) for z in range(y,n+1) if x**2 + y**2 == z**2]

from Cython.CodeWriter import CodeWriter
z = CodeWriter(a)



def fib():
    a,b = 1,0
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

def fib2(n):
    b = 1
    a=0
    res = 1
    for i in range(0,n):
        a = b
        b = res
        res = b + a
    return b

x = [fib2(i) for i in range(0,100)]

import numpy as np
z = [12,13]
z1 = np.append(z, [12,1])

z = [12,13]
z.extend([[12,1]])

class Toto:
    x= 6 
    def __init__(self,xf):
        self.xf = xf
    def je(self):
        return self.xf+ self.x


<ModelUnit modelid="SQ.PhenoPkg.ShootNumber" name="ShootNumber" timestep="1" version="001">
<Description>
    <Title>ShootNumber model</Title>
    <Authors>Pierre MARTRE</Authors>
    <Institution>INRA/LEPSE Montpellier</Institution>
    <Reference>(None,)</Reference>
    <Abstract>calculate the shoot number and update the related variables if needed</Abstract>
</Description></ModelUnit>