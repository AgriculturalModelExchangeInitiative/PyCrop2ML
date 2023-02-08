from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG ,to_CASG
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml, create_repo
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.fortran.fortranExtraction import FortranExtraction
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import extract
from pycropml.transpiler.antlr_py.fortran.fortran_preprocessing import Declarations, Local, Call_stmt, Implicit_return
import tempfile
from pycropml.transpiler.antlr_py import repowalk
from pycropml.transpiler.antlr_py.to_specification import extractMetaInfo, createObjectModel, extractcomments, createObjectCompo
from pycropml.transpiler.antlr_py.codeExtraction import extraction
import re

""" Read non-specific fortran component and infer Crop2ML model

"""

types = ["float", "str", "list", "array", "int", "boolean"]

model_tags = ["!%%CyML Model Begin%%", "!%%CyML Model End%%"]
init_tags=["!%%CyML Init Begin%%", "!%%CyML Init End%%"]
rates_tags = ["!%%CyML Rate Begin%%", "!%%CyML Rate End%%"]
states_tags = ["!%%CyML State Begin%%", "!%%CyML State End%%"]
compute_tags = ["!%%CyML Compute Begin%%", "!%%CyML Compute End%%"]
ignore_tags = ["!%%CyML Ignore Begin%%", "!%%CyML Ignore End%%"]
description_tags = ["!%%CyML Description Begin%%", "!%%CyML Description End%%"]

start_linecom = ["!", ["C", 1]] # if item is a list: first is the tag and scond is the porition of the tag
default_mltCom = ['%%%%', '%%%%%'] # use '%%%%' if the language didn't provide multi lines comments

language = 'f90'

endconstruct = "end"

endline = "\n"

cyml_ext = ".pyx"

output_folder = "temp"

def translate(node, asgt, inout=[], index=[]):
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
     
    l = Local()
    res = l.process(node)
    pp = l.localvar.difference(set(inout)) # remove input output declarations
    #zz = pp.intersection(ass.targets) ### to remove local variables that are not used as targets  in an assignment 
    if index: 
        zz = pp.union(set(index))
    else: zz = pp
    e = Declarations(localvar=list(zz)) ## pp by zz
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


def fortrancomments(code ):
    """
        Extract comments inside Fortran code
    """
    return extractcomments(code, ["!", ["C", 1]])


def run_fortran(routines, output):
    
    compositeStrat= Path(routines).glob('*Component.f90')
    if compositeStrat: compositeStrat = compositeStrat[0]
    simpleStrat = [f for f in Path(routines).glob('*.f90')  if (f not in compositeStrat and not f.endswith("list_sub.f90"))]
    create_repo(output)
    files = repowalk.walk(routines, 'f90')
    
    mu_names = []
    
    for  k, v in files.items():
        print(v)
        with open(v, "r") as f:
            code = f.read()
        f90_units = extraction(code,model_tags[0],model_tags[1])
        
        file_dictasg = to_dictASG(code, 'f90')
        file_asg = to_CASG(file_dictasg)
        
        z =  FortranExtraction()
        for f90_unit in f90_units:
            name = re.findall(r'(subroutine\s+.+\()', f90_unit)[0].replace("subroutine", "").replace("(", "").strip()    
            # extract algorithm of each py_unit using file_asg, the name of the unit
            meth = z.getSubroutine(file_asg, name) 
            startcom = description_tags[0] # start of description extraction
            startend = description_tags[1] # end of description extraction
            # Transform comments to a list of comments. Each item represents 
            # an entire description of an input/output
            commentsPart = extraction(f90_unit, startcom, startend)
            mdata = extract(commentsPart[0])

            inout = list({var.name for var in mdata.inputs + mdata.outputs}) # extract model in/out
            print(name)
            # finally we got the algo
            algo = translate(meth.block, file_asg, inout=inout)

            # save algo
            if name.startswith("model_"): name = name.replace("model_", "")
            mu_names.append(mdata.name)
                    
            out_compute = os.path.join(output,  "crop2ml", "algo", "pyx", mdata.name + ".pyx")
            with open(out_compute, "w") as fi:
                fi.write(algo + '\n')
            """
            z.modelunit(f90_unit,meth)  
            print(name, z.inputs)
            varnotdeclared = meth.notdeclared"""
            
    

    """

    fp = tempfile.TemporaryFile(mode="w+t",encoding="utf8", dir = routines)
    
 
    # Merge files in a temporary file
    for f in files:
        fil = open(os.path.join(routines, f), "r")
        fp.write(fil.read())
        fp.write("\n")
        fil.close()
    fp.seek(0)

    for f in files:
        pass
    """
    # Create the Fortran ASG of the merged files
    """code = fp.read()
    d_sorted = fortrancomments(code)
    dictasgt = to_dictASG(code,language, comments=d_sorted)
    asgt = to_CASG(dictasgt)
    fp.close() """
    
    """
    
    if compositeStrat:
        with open(compositeStrat, 'r' ) as fil:
            codecompo = fil.read()
            compodict = to_dictASG(codecompo, 'f90')
            compo = to_CASG(compodict)
    models = []
    
    for strat in simpleStrat:
        with open(strat, 'r' ) as fil:
            code = fil.read()
        print(strat)
        dictstr =to_dictASG(code,'f90')
        strAsg = to_CASG(dictstr)
        z = DssatExtraction()  
        z.modelunit(strat,strAsg)  
        v = z.model.inputs + z.model.outputs 
        var = [vi.name for vi in v]   
        algo = z.getSubroutine(strAsg)
        if algo :
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

