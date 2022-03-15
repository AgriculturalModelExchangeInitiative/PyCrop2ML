from pycropml.transpiler.antlr_py.codeExtraction import extraction 
from pycropml.transpiler.antlr_py.listOfTags import *
import re
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
from pycropml.transpiler.antlr_py.extraction import ExtractComments 
from collections import OrderedDict


    
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
    commentsPart = extraction(comments, startcom, startend)  
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


def createObjectModel(head: dict, description: dict, inputs:list, outputs: list, init:bool=False, funcs:list=[], parametersets:dict=[], testsets:dict=[]):
    """ generate Crop2ML Python ModelUnit
    
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
    
    if init: m.initialization[0].name = m.name
     
    return m

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
    
    
    
    
    
    
    
    
    
            
    
