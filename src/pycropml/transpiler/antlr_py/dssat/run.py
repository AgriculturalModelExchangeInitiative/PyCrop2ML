from __future__ import absolute_import
from __future__ import print_function
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
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

model_tags = ["!%%CyML Model Begin%%", "!%%CyML Model End%%"]
init_tags=["!%%CyML Init Begin%%", "!%%CyML Init End%%"]
rates_tags = ["!%%CyML Rate Begin%%", "!%%CyML Rate End%%"]
states_tags = ["!%%CyML State Begin%%", "!%%CyML State End%%"]
compute_tags = ["!%%CyML Compute Begin%%", "!%%CyML Compute End%%"]
ignore_tags = ["!%%CyML Ignore Begin%%", "!%%CyML Ignore End%%"]

start_linecom = ["!", ["C", 1]] # if item is a list: first is the tag and scond is the porition of the tag
default_mltCom = ['%%%%', '%%%%%'] # use '%%%%' if the language didn't provide multi lines comments

language = 'f90'

endconstruct = "end"

endline = "\n"

cyml_ext = ".pyx"

output_folder = "temp"

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
    

    return translate_simple(r, total_tree=asgt)

def translate_simple(r, total_tree=None):
    """ Transform the ASG of Fortran code in the Common Model Representation that is transformed into CyML

    Args:
        r (Node): The modified ASG of Fortran  

    Returns:
        str: The generated CyML code 
    """
    cd = f90_cyml.F90_Cyml_ast(r, treeG=total_tree)
    hh = cd.transform()
    nd = transform_to_syntax_tree(hh)
    codes = writeCyml(nd)
    return codes

def fortrancomments(code, start_linecom=[],default_mltCom = ['%%%%', '%%%%%'] ):
    """
        Extract comments inside Fortran code
    """
    comments = {}
    if start_linecom:
        for tag in start_linecom:
            if isinstance(tag, list):
                r = ExtractComments(code, tag[0], default_mltCom[0], default_mltCom[1], pos=tag[1]) 
            else:
                r = ExtractComments(code, tag, default_mltCom[0], default_mltCom[1]) 
            comments.update(r)
    d_sorted = OrderedDict({key:value for key, value in sorted(comments.items(), key=lambda item: int(item[0]))})
    return d_sorted


""" Read DSSAT component and infer Initializations, Algorithms and External Functions

"""
def execute(package):

    # Read Cmake files !!!!!!!!
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
    #!!!!
    
    # Create the Fortran ASG of the merged files
    code = fp.read()
    d_sorted = fortrancomments(code)
    dictasgt = to_dictASG(code,language, comments=d_sorted)
    asgt = to_CASG(dictasgt)
    fp.close() 
    
    extr = DssatExtraction()
    # Find the not required functions or subroutines
    notreq = extr.notRequiredFunc(asgt)

    for f in files:
        with open(os.path.join(package,f), 'r') as text:
            mod = text.read()
        #comments = fortrancomments(mod)
        res = extraction(mod, model_tags[0],model_tags[1],ignore_tags[0],ignore_tags[1])
        if res:
            modunit_dictasg = to_dictASG(res, language)
            modunit_asg = to_CASG(modunit_dictasg)
            decl=[]
            for m in modunit_asg[0].block:
                if m and m.type=="declaration":
                    decl.append(m)

            imports = modunit_asg[0].imports
            attrib = Attr(asgt,imports)
            node_w_attrib = attrib.process(modunit_asg[0])
            zz =attrib.decls
            attrname = []
            for d in zz:
                attrname.append(d.decl[0].name)

            initialization =  extraction(res, init_tags[0],init_tags[1])
            ratecalculation = extraction(res, rates_tags[0],rates_tags[1])
            statecalculation = extraction(res, states_tags[0],states_tags[1])
            algoPart = extraction(res, compute_tags[0],compute_tags[1])  
            initialization = initialization +endline + endconstruct
            algoPart = algoPart + endline + endconstruct
   
            ratecalculation = ratecalculation + endline + endconstruct
            statecalculation = statecalculation + endline + endconstruct
            comments_init = fortrancomments(initialization)
            comments_rate = fortrancomments(ratecalculation)
            comments_compute = fortrancomments(algoPart)
            initialization_dictasg = to_dictASG(initialization, language,comments_init, env = modunit_asg[0].env)
            ratecalculation_dictasg = to_dictASG(ratecalculation, language,comments_rate, env = modunit_asg[0].env)
            algoPart_dictasg = to_dictASG(algoPart, language,comments_compute, env = modunit_asg[0].env)
            initialization_asg = to_CASG(initialization_dictasg)
            ratecalculation_asg = to_CASG(ratecalculation_dictasg)
            algoPart_asg = to_CASG(algoPart_dictasg)
            inout = modunit_asg[0].inputs + modunit_asg[0].outputs + attrname
            codes_init = translate(decl+initialization_asg,asgt,imports, inout=inout)
            codes_rates = translate(decl+ratecalculation_asg,asgt,imports,inout=inout)
            codes_compute = translate(decl+algoPart_asg,asgt,imports,inout=inout)
            exterfunc = extr.externFunction(modunit_asg[0]) # external functions
            extfunc = exterfunc.difference(notreq)
            
            
            for ext in extfunc:
                func = extr.getSubroutine(asgt, ext)
                extcode = translate_simple(func, total_tree=asgt)
                exfunc = os.path.join(package, output_folder, ext + ".pyx")
                with open(exfunc, "w") as fi:
                    fi.write(extcode)
            
            if codes_init:
                out_init = os.path.join(package, output_folder, "init."+f.split(".")[0] + ".pyx")
                with open(out_init, "w") as fi:
                    fi.write(codes_init)
            if codes_rates:
                out_rates = os.path.join(package, output_folder, f.split(".")[0] + ".pyx")
                with open(out_rates, "w") as fi:
                    fi.write(codes_rates)
            else:
                out_compute = os.path.join(package, output_folder, f.split(".")[0] + ".pyx")
                with open(out_compute, "w") as fi:
                    fi.write(codes_compute)

    
    


    
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