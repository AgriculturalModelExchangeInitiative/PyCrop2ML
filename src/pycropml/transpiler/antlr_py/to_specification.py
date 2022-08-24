from pycropml.transpiler.antlr_py.codeExtraction import extraction 
from pycropml.transpiler.antlr_py.listOfTags import *
import re
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
from pycropml.transpiler.antlr_py.extraction import ExtractComments 
from collections import OrderedDict
from pycropml.composition import ModelComposition


    
pattern = r'(?P<name>^[a-zA-Z][\w]+)'\
            r'\(?'\
            r'(?P<item>(\d+|[^  ,\(\)\[\]\s]*))?'\
            r'\)?'\
            r'\s+'\
            r'(?P<description>.*\S)'\
            r'\s+'\
            r'\((?P<unit>[a-zA-Z].*)?\)'\
            r'\s*'\
            r'\('\
            r'(?P<default>(\d+\.?\d*|[^  ,\(\)\[\]\s]*))?'\
            r'\s*'\
            r',?'\
            r'\s*'\
            r'\[?'\
            r'\s*'\
            r'(?P<mini>(\d+\.?\d*|[^  ,\(\)\[\]\s]*))?'\
            r'\s*'\
            r'-?'\
            r'\s*'\
            r'(?P<maxi>(\d+\.?\d*|[^  ,\(\)\[\]\s]*))?'\
            r'\s*'\
            r'\]?'\
            r'\s*'\
            r'\)'\
            r'\s*'\
            r'(?P<category>(state|rate|auxiliary|exogenous|soil|constant|genotypic))?'\
            r'\s*'\
            r'\s*'\
            r'(?P<type>(variable|parameter))?'




def extractMetaInfo(comments, symbol):
    """Extract inputs and outputs meta-information

    Args:
        comments (str): description of inputs and outputs. A continuous line of
                        an in/out description must begin after more than one space
        symbol (str): character at the biginning of each description 
                        (symbol of code comments depending on the language)
    """
    result = {}
    startcom = symbol + description_tags[0] # start of description extraction
    startend = symbol + description_tags[1] # end of description extraction
    # Transform comments to a list of comments. Each item represents 
    # an entire description of an input/output
    commentsPart = extraction(comments, startcom, startend)[0]  # suppose that there is one ModelUnit in a file or one place where metainfo is described
    commentsPart = commentsPart.replace(symbol, '').split('\n')
    commentList = []
    for line_ in commentsPart:
        if line_.startswith('  '):
            commentList[-1] = commentList[-1] + ' ' + line_.lstrip()
        else:
            commentList.append(line_.strip())
    
    for com in commentList:
        m = re.match(pattern, com)
        if m:
            name = m.group('name')
            result[name] = {}
            result[name].update({"description":m.group('description')})
            result[name].update({"len":m.group('item')})
            result[name].update({"unit":m.group('unit')})
            result[name].update({"default":m.group('default')})
            result[name].update({"max":m.group('maxi')})
            result[name].update({"min":m.group('mini')})
            result[name].update({"category":m.group('category')})
            result[name].update({"type":m.group('type')})
    
    return result


def createObjectModel(head: dict, description: dict, inputs:list, outputs: list, init:dict={}, funcs:list=[], parametersets:dict=[], testsets:dict=[]):
    """ generate Crop2ML ModelUnit Python object
    
    head (dict) : {Name:name, version: version, id:id, timestep:timestep }
    description (dict) : description element of modelUnit (Title, Authors, Reference, Institution, ExtendedDescription)
    inputs (list)
    outputs (list)
    parametersets (list)
    testsets (list)
    
    """
    m = ModelUnit(head)
    
    d = Description()
    for k, v in description.items(): setattr(d, k, v) 
    m.add_description(d)
    
    for n in inputs:
        m.inputs.append(Input(n))
    
    for n in outputs:
        m.outputs.append(Output(n))
    
    if init: 
        m.initialization.append(init)
    if funcs:
        for f in funcs:
            m.function.append(f)
    return m

def model_desc(desc):
    name = desc["name"][:-9] if desc["name"].endswith("Component") else desc["name"]
    description = Description()
    description.Title = name+" model" 
    description.Authors = desc["authors"]
    description.Institution=desc["institution"]
    description.Reference = desc["Reference"] if "Reference" in desc else None, 
    description.ExtendedDescription = desc["description"]
    description.Url = desc["url"]
    return description

def createObjectCompo(desc, models):
    inputlink = []
    outputlink = []
    mc = ModelComposition({"name":desc["name"], "version":"001", "timestep":"1"})
    description = model_desc(desc)
    mc.add_description(description)
    mc.model = [m.name for m in models]
    inps, outs = [], []
    md = models
    inps = [n.name for m in md for n in m.inputs ]
    outs = [n.name for m in md for n in m.outputs ]
    #m_in = set(inps) - set(outs)
    inits=[]
    inpsl = []
    for m in md:
        if "initialization" in dir(m) and m.initialization and  m.initialization[0]:
            mo = [r.name for r in m.inputs if "variablecategory" in dir(r) and r.variablecategory=="state"]
            inits.extend(mo)
    otherVar = [n.name for m in md for n in m.inputs if "parametercategory" in dir(n) or ("variablecategory" in dir(n) and n.variablecategory=="exogenous")]
    
    m_in = inits + otherVar  
        
            
    z = {}
    internallink= []
    for m in md:
        vi = list(set([n.name for n in m.inputs ]).intersection(m_in))
        vo = [n.name for n in m.outputs]
        for v in vi:
            inputlink.append({"target": m.name + "." + v, "source":v})
            for v in vo: z.update({v:m.name})

    for k, v in z.items():
        outputlink.append({"source": v + "." + k, "target":k})

    for i in range(0, len(md)-1):
        mi = md[i]
        for j in range(i+1, len(md)):
            mj = md[j]
            vi = list(set([n.name for n in mi.outputs ]).intersection(set([n.name for n in mj.inputs ])))
            if vi: 
                for k in vi:
                    internallink.append({"source": mi.name + "." + k, "target":mj.name + "." + k})

    mc.inputlink = inputlink
    mc.outputlink = outputlink
    mc.internallink = internallink
    
    return mc
    
    

def extractcomments(code, start_linecom=[],default_mltCom = ['%%%%', '%%%%%'] ):
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
    
    
    
    
    
    
    
    
    
            
    
