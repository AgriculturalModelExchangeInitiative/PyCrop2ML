from __future__ import absolute_import
from __future__ import print_function
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.cmake.cmakeTransformer import retrievefiles
from collections import OrderedDict
from pycropml.transpiler.antlr_py.extraction import ExtractComments   
from pycropml.transpiler.antlr_py.codeExtraction import extraction
from pycropml.transpiler.antlr_py.fortran.fortran_preprocessing import Declarations, Attr, Assignment, Call_stmt, Implicit_return, Local
import tempfile

def translate(node, asgt, imports, inout=[]):
    """Transform specific nodes based on class of subnodes of node. It also allows to extract some usefull information. At finish
    the  modified node contains only the constructs of CyML and converted in CyML after applying translate_simple function.

    Args:
        node (Node): A subtree of asgt
        asgt (Node): A tree
        imports (str): Names of the import Modules used in the code from where the node is generated
        inout (list, optional): Names of the inputs and outputs of the ModelUnit. Defaults to [].

    Returns:
        files: init, algo and external functions files
    """
    attrib = Attr(asgt,imports=imports)
    node_w_attrib = attrib.process(node)
    
    ass = Assignment()
    node2=ass.process(node_w_attrib)
    
    l = Local()
    res = l.process(node2)
    pp = l.localvar.difference(set(inout))
    
    e = Declarations(localvar=list(pp))
    f = e.process(res)
    
    g = Call_stmt(trees=asgt)
    h = g.process(f)
    
    z = Implicit_return()
    r = z.process(h)
    

    return translate_simple(r)

def translate_simple(r):
    """ Transform the ASG of Fortran code in the Common Model Representation that is transformed into CyML

    Args:
        r (Node): The modified ASG of Fortran  

    Returns:
        str: The generated CyML code 
    """
    cd = f90_cyml.F90_Cyml_ast(r)
    hh = cd.transform()
    nd = transform_to_syntax_tree(hh)
    codes = writeCyml(nd)
    return codes

def fortrancomments(code):
    """
        Extract comments inside Fortran code
    """
    comments = ExtractComments(code, "C", '%%%%', '%%%%%', pos=1) 
    comments2 = ExtractComments(code, "!", '%%%%', '%%%%%') 
    comments.update(comments2)
    d_sorted = OrderedDict({key:value for key, value in sorted(comments.items(), key=lambda item: int(item[0]))})
    return d_sorted


""" Read DSSAT component and infer Initializations, Algorithms and External Functions

"""
def execute(package):

    # Read Cmake files
    modu=os.path.join(package, "CMakeLists.txt")
    with open(modu, "r") as f:
        cmakecode = f.read() 

    # Parse Cmake code to retrieve source files
    files = retrievefiles(cmakecode)
    fp = tempfile.TemporaryFile(mode="w+t",encoding="utf8")
 
    # Merge files in a temporary file
    for f in files:
        fil = open(os.path.join(package, f), "r")
        fp.write(fil.read())
        fp.write("\n")
        fil.close()
    fp.seek(0)
    #print(fp.read())
    
    # Create the Fortran ASG of the merged files
    code = fp.read()
    d_sorted = fortrancomments(code)
    asgt = to_CASG(code,'f90', comments=d_sorted)[0]
    fp.close() 
    
    extr = DssatExtraction()
    # Find the not required functions or subroutines
    notreq = extr.notRequiredFunc(asgt)

    for f in files:
        with open(os.path.join(package,f), 'r') as text:
            mod = text.read()
        res = extraction(mod, "!%%ModelUnit_Start%%","!%%ModelUnit_End%%","!%%Ignore_Start%%","!%%Ignore_End%%")
        if res:
            print(f)
            modunit_asg = to_CASG(res, "f90")
            decl=[]
            for m in modunit_asg[0][0].block:
                if m and m.type=="declaration":
                    decl.append(m)

            imports = modunit_asg[0][0].imports
            attrib = Attr(asgt,imports)
            node_w_attrib = attrib.process(modunit_asg[0])
            zz =attrib.decls
            attrname = []
            for d in zz:
                attrname.append(d.decl[0].name)

            initialization =  extraction(res, "!%%Initialization_Start%%","!%%Initialization_End%%")
            ratecalculation = extraction(res, "!%%Algorithm_RateCalculation_Start%%","!%%Algorithm_RateCalculation_End%%")
            statecalculation = extraction(res, "!%%Algorithm_StateCalculation_Start%%","!%%Algorithm_StateCalculation_End%%")
            algoPart = extraction(res, "!%%Algorithm_Part_Start%%","!%%Algorithm_Part_End%%")  
            initialization = initialization +"\n" + "end"
            if algoPart:
                algoPart = algoPart +"\n" + "end"

            ratecalculation = ratecalculation +"\n" + "end"
            statecalculation = statecalculation 
            comments_init = fortrancomments(initialization)
            comments_rate = fortrancomments(ratecalculation)
            initialization_asg = to_CASG(initialization, "f90",comments_init, env = modunit_asg[1])[0][0]
            ratecalculation_asg = to_CASG(ratecalculation, "f90",comments_rate, env = modunit_asg[1])[0][0]
            inout = modunit_asg[0][0].inputs + modunit_asg[0][0].outputs + attrname
            codes_init = translate(decl+initialization_asg,asgt,imports, inout=inout)
            codes_rates = translate(decl+ratecalculation_asg,asgt,imports,inout=inout)
            exterfunc = extr.externFunction(modunit_asg[0][0]) # external functions
            extfunc = exterfunc.difference(notreq)
            for ext in extfunc:
                func = extr.getSubroutine(asgt, ext)
                extcode = translate_simple(func)
            out_init = os.path.join(package, "temp", "init."+f.split(".")[0] + ".pyx")
            with open(out_init, "w") as fi:
                fi.write(codes_init)
            out_algo = os.path.join(package, "temp", f.split(".")[0] + ".pyx")
            with open(out_algo, "w") as fi:
                fi.write(codes_rates)
            exfunc = os.path.join(package, "temp", ext + ".pyx")
            with open(exfunc, "w") as fi:
                fi.write(extcode)
    
    


    
"""
def process_dssat(routines, output):
    compositeStrat= routines.glob('*Component.f90')[0]
    simpleStrat = [f for f in routines.glob('*.f90')  if (f not in compositeStrat and not f.endswith("list_sub.f90"))]
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not crop2ml_rep.isdir():
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not algo_rep.isdir():
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not cyml_rep.isdir():
        cyml_rep.mkdir()
    compo = to_CASG(compositeStrat, 'f90')
    models = []
    for strat in simpleStrat:
        with open(strat, 'r' ) as fil:
            code = fil.read()
        strAsg = to_CASG(code,'f90')
        z = DssatExtraction()  
        z.modelunit(strat,strAsg)  
        v = z.model.inputs + z.model.outputs 
        var = [vi.name for vi in v]   
        algo = z.getProcess(strAsg)
        for f in algo:
            if f.name.startswith("model"): 
                cd = f90_cyml.F90_Cyml_ast(f.block, var = var)
                h = cd.transform()
                nd = transform_to_syntax_tree(h)
                code = writeCyml(nd)
                filename = Path(os.path.join(cyml_rep, "%s.pyx"%(strat.basename().split(".")[0])))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))
                models.append(z.model)
                xml_ = Pl2Crop2ml(z.model, "Dssat.Pheno_Pkg").run_unit()
                filename = Path(os.path.join(crop2ml_rep, "unit.%s.xml"%(strat.basename().split(".")[0])))
                with open(filename, "wb") as xml_file:
                    xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
            
            else:
                nd = transform_to_syntax_tree(f)
                code = writeCyml(nd)
                filename = Path(os.path.join(cyml_rep, "%s.pyx"%(f.name)))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))
    z.modelcomposition(compositeStrat, models, compo)
    xml_ = Pl2Crop2ml(z.mc, "Dssat.Pheno_Pkg").run_compo()
    name = z.mc.name[:-9] if z.mc.name.endswith("Component") else z.mc.name
    filename = Path(os.path.join(crop2ml_rep, "composition.%s.xml"%(name)))
    with open(filename, "wb") as xml_file:
        xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
    
    return 0

"""