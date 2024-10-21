from __future__ import absolute_import
from __future__ import print_function
import os
#import copy
from os.path import isdir
import tempfile
from path import Path
from collections import OrderedDict

from pycropml.composition import Description
from pycropml.transpiler.antlr_py import repowalk
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pycropml.transpiler.antlr_py.fortran.fortranExtraction import FortranExtraction
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.cmake.cmakeTransformer import retrievefiles
#from pycropml.transpiler.antlr_py.extraction import ExtractComments  
from pycropml.transpiler.antlr_py.codeExtraction import extraction
from pycropml.transpiler.antlr_py.fortran.fortran_preprocessing import Declarations, Attr, Assignment, Call_stmt, Implicit_return, Local
from pycropml.transpiler.antlr_py.to_specification import extractMetaInfo, createObjectModel, extractcomments, createObjectCompo
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml, generate_compositefile, generate_unitfile, create_repo
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract

types = ["float", "str", "list", "array", "int", "boolean"]

model_tags = ["!%%CyML Model Begin%%", "!%%CyML Model End%%"]
init_tags=["!%%CyML Init Begin%%", "!%%CyML Init End%%"]
rates_tags = ["!%%CyML Rate Begin%%", "!%%CyML Rate End%%"]
states_tags = ["!%%CyML State Begin%%", "!%%CyML State End%%"]
compute_tags = ["!%%CyML Compute Begin%%", "!%%CyML Compute End%%"]
ignore_tags = ["!%%CyML Ignore Begin%%", "!%%CyML Ignore End%%"]
composition_tags = ["!%%CyML Composition Begin%%", "!%%CyML Composition End%%"]
description_tags = ["!%%CyML Description Begin%%", "!%%CyML Description End%%"]

start_linecom = ["!", ["C", 1]] # if item is a list: first is the tag and scond is the porition of the tag
default_mltCom = ['%%%%', '%%%%%'] # use '%%%%' if the language didn't provide multi lines comments

language = 'f90'

endconstruct = "end"

endline = "\n"

cyml_ext = ".pyx"

output_folder = "temp"

def translate(node, asgt, imports, inout=[], index=[]):
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
    pp = l.localvar.difference(set(inout)) # remove input output declarations
    #zz = pp.intersection(ass.targets) ### to remove local variables that are not used as targets  in an assignment 
    if index: 
        zz = pp.union(set(index))
    else:
        zz = pp
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


""" Read DSSAT component and infer Initializations, Algorithms and External Functions

"""
def run_stics(component, package):


    # Temporary file
    fp = tempfile.TemporaryFile(mode="w+t",encoding="utf8")

    create_repo(package)    
    files = repowalk.walk(component, 'f90')

    # Merge files in a temporary file
    for name, f in files.items():
        fil = open(f, "r")
        fp.write(fil.read())
        fp.write("\n")
        fil.close()
    fp.seek(0)
    #print(fp.read())
    #!!!!

    # Create the Fortran ASG of the merged files
    code = fp.read()
    d_sorted = fortrancomments(code)
    print("dsorted donce")
    dictasgt = to_dictASG(code,language, comments=d_sorted)
    asgt = to_CASG(dictasgt)
    fp.close() 
    
    
    # dtermine the package name to be used in models file
    m = os.path.basename(Path(package))
    m = m.split("_")
    package_name = m[0] +"." + "".join(m[1:])
    models = []
    extr = FortranExtraction()
    # Find the not required functions or subroutines
    notreq = extr.notRequiredFunc(asgt)
    for f in files:
        print(f)
        with open(os.path.join(component,f), 'r') as text:
            mod = text.read()
        #comments = fortrancomments(mod)
        res = extraction(mod, model_tags[0],model_tags[1],ignore_tags[0],ignore_tags[1])
        if res:
            totalcomments = fortrancomments(mod)
            modunit_dictasg = to_dictASG(res[0] , language)
            modunit_asg = to_CASG(modunit_dictasg)
            exterfunc = extr.externFunction(modunit_asg[0]) # external functions
            imports = modunit_asg[0].imports
           
            
            attrib = Attr(asgt,imports)
            node_w_attrib = attrib.process(modunit_asg[0])
            zz =attrib.decls

            attrname = []
            newinputs = []
            for d in zz:
                attrname.append(d.decl[0].name)
                newinputs.append(d.decl[0])
            
            inout = modunit_asg[0].inputs_name + modunit_asg[0].outputs_name + attrname
            
            gg = Call_stmt(trees=asgt)
            hh = gg.process(node_w_attrib)
                
            ass = Assignment()
            node2=ass.process(hh)     
            l = Local()
            res1 = l.process(node2)
            pp = l.localvar.difference(set(inout)) # remove input output declarations
            input1 = pp.difference(ass.targets) ### to get local variables that are used as model inputs 
            decl=[]
            inputs1=[]
            for m in modunit_asg[0].block:
                if m and m.type=="declaration":
                    decl.append(m)
                    for inp in m.decl:
                        if inp.name in input1 and inp.name not in modunit_asg[0].indexnames and "value" not in dir(inp) :
                            inputs1.append(inp)


            initialization =  extraction(res[0] , init_tags[0],init_tags[1])
            algoPart = extraction(res[0], compute_tags[0],compute_tags[1])

            varnotdeclared = modunit_asg[0].notdeclared
            extr2 = FortranExtraction()
            if varnotdeclared:
                res = extr2.getDecl(asgt, imports, varnotdeclared)
                otherparams = list(res.values())
            else: otherparams=[]
            model_inputs = [m for m in otherparams + newinputs + modunit_asg[0].inputs+ inputs1 if m.type in types]

            model_outputs = modunit_asg[0].outputs
            
            inout = list(set([m.name for m in model_inputs + model_outputs  ])) 
            
            metainfo_init = {}
            initv = False
            algop = False
            
            if initialization:
                initv = True
                metainfo_init = {"name": f"init.{modunit_asg[0].name}", "language":"Cyml", "filename":f"algo/pyx/init.{modunit_asg[0].name}.pyx"}
                initialization = initialization[0]  +endline + endconstruct
                comments_init = fortrancomments(initialization)
                initialization_dictasg = to_dictASG(initialization, language,comments_init, env = modunit_asg[0].env)
                initialization_asg = to_CASG(initialization_dictasg)
                codes_init = translate(initialization_asg,asgt,imports, inout=inout, index = modunit_asg[0].indexnames)
            

            if algoPart:
                algop = True
                algoPart = algoPart[0]  + endline + endconstruct 
                comments_compute = fortrancomments(algoPart)
                algoPart_dictasg = to_dictASG(algoPart, language,comments_compute, env = modunit_asg[0].env)
                algoPart_asg = to_CASG(algoPart_dictasg)
                codes_compute = translate(decl+algoPart_asg,asgt,imports,inout=inout, index = modunit_asg[0].indexnames)                               
            
            #r = ExtractComments(mod, "!", '"""', '"""') 
            
            startcom = description_tags[0] # start of description extraction
            startend = description_tags[1] # end of description extraction
            # Transform comments to a list of comments. Each item represents 
            # an entire description of an input/output
            commentsPart = extraction(mod, startcom, startend)
            mdata = extract(commentsPart[0]+"\n\n")
            #mdata = extract(r)
            #metainfo = extractMetaInfo(mod, "!")
                               
            out_compute = os.path.join(package,  "crop2ml", "algo", "pyx", mdata.name + ".pyx")
            with open(out_compute, "w") as fi:
                fi.write(codes_compute + '\n')
            
            extfunc = exterfunc.difference(notreq) 
         
            for ext in extfunc:
                mdata.function.append(ext)
                func = extr.getSubroutine(asgt, ext)
                extcode = translate_simple(func, total_tree=asgt)
                exfunc = os.path.join(package, "crop2ml", "algo", "pyx", ext + ".pyx")
                with open(exfunc, "w") as fi:
                    fi.write(extcode + '\n')
            
            models.append(mdata)

            if initv:
                dict_init = {} 
                name_i = f.split(".")[0]
                dict_init["name"] = "init."+mdata.name
                
                dict_init["filename"] = f"algo/pyx/init.{f.split('.')[0]}.pyx"
                mdata.initialization = [dict_init]
                out_init = os.path.join(package, "crop2ml", dict_init["filename"])
                with open(out_init, "w") as fi:
                    fi.write(codes_init+'\n')  
            generate_unitfile(package, mdata, package_name) 


    res_compo = extraction(code, composition_tags[0],composition_tags[1],ignore_tags[0],ignore_tags[1])
    #print("ooo", res_compo[0])
    if res_compo:
        compo_dictasg = to_dictASG(res_compo[0] , language)
        compo_asg = to_CASG(compo_dictasg)
        mc = extr.modelcomposition(res_compo[0], models, compo_asg) 
        generate_compositefile(package, mc, package_name)   
    
    else:
        description={}
        description["name"]=mdata.name+"_"
        description["version"]=mdata.version
        description["timestep"]=mdata.timestep
        description["url"] = ""
        description["Authors"] = mdata.description.Authors
        description["Institution"] = mdata.description.Institution
        description["ShortDescription"] = mdata.description.ShortDescription
        description["ExtendedDescription"] = mdata.description.ExtendedDescription
        mc = createObjectCompo(description, models)   
        generate_compositefile(package, mc, package_name)       
                    


                    
            


dicttype = {"str":"STRING", "int":"INT", "float":"DOUBLE"}
    
def transform_type(pseudo_type):
    if isinstance(pseudo_type, list):
        newtype = dicttype[pseudo_type[-1]] + pseudo_type[0].upper()
    else:
        newtype = dicttype[pseudo_type]
    return newtype


    """
 from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG ,to_CASG
from pycropml.transpiler.antlr_py.dssat.dssatExtraction2 import DssatExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py.fortran import f90_cyml


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


