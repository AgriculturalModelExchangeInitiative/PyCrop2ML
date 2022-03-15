# inspired from http://csharphelper.com/blog/2015/10/extract-comments-from-a-c-file-in-c/

"""
    information extraction over structured documentation or comments

"""
from pycropml.composition import ModelComposition
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
# Return a file's comments.
def ExtractComments(filename, c_st_single, c_st_multi, c_end_multi):
    # If a language has no block comment style, be sure that the default c_st_multi and c_end_multi will never be met.
    with open(filename, 'r',  encoding='utf-8') as file:
        all_text = file.read()
    comments = "";
    while (len(all_text) > 0):
        single_line_pos = all_text.find(c_st_single)
        multi_line_pos = all_text.find(c_st_multi)
        if (single_line_pos < 0) and multi_line_pos <0 : break
        if (single_line_pos < 0) : single_line_pos = len(all_text)
        if (multi_line_pos < 0): multi_line_pos = len(all_text)
        if (single_line_pos < multi_line_pos):
            end_pos = all_text.find("\n", single_line_pos +1);
            if end_pos<0 :
                comments += all_text[single_line_pos:] + "\r\n"
                all_text = ""            
            else:
                comments += all_text[single_line_pos: end_pos] +"\r\n"
                all_text = all_text[end_pos + 1:]          
        else:
            end_pos = all_text.find(c_end_multi, multi_line_pos + 1)
            if (end_pos < 0):
                comments += all_text[multi_line_pos:] + "\r\n"
                all_text = ""
            else:
                comments += all_text[multi_line_pos : end_pos+2] + "\r\n";
                all_text = all_text[end_pos + 1:]
    return comments

pattern_attr_val = r"(\*?\*?\s*(?P<attribute>\w+)\s*:\s*(?P<value>[\w+\s:,ï\[\]\\_\./\'-]*))"

import re
def extract(comment):
    keywords = ["name", "version", "timestep" ]
    patterns = [r'(\b(?i)Name:\s*(?P<name>\w+))',
                r'(-Version:\s*(?P<version>\d+\.*\d+))',
                r'(-Time step:\s*(?P<timestep>\d+\.*\d*))'] 
    
    # header of modelUnit name, version, timestep
    head = {}
    i = 0
    for p in patterns:
        if re.search(p, comment):
            head[keywords[i]] = re.search(p, comment).group(keywords[i])   
        i = i + 1
    m = ModelUnit(head)

    # description element of modelUnit (Title, Authors, Reference, Institution, Abstract)
    pat_description = r'(Description:\s*\r*\n*(.*\*\s*\w+:.+\r*\n*/*)+)'
    description = attval(pat_description, comment)
    d = Description()
    for k, v in description.items(): setattr(d, k, v) 
    m.add_description(d)

    # inputs
    inputs = comment.split("inputs:")[1].split("outputs:")[0]
    pat_ = r'(name:\s*.+\s*)'
    z = re.findall(pat_, inputs, re.MULTILINE)
    inpList = []
    if z:
        for inp in z:
            input={}
            name = inp.replace("\r\n", "").replace("name:", "").lstrip().rstrip()
            pat_name = r'(%s\s*\r*\n*(.*\*\*\s*.+?:.+\r*\n*)+)'%(inp)
            input["name"] = name
            input.update(attval(pat_name, inputs))
            inpList.append(Input(input))
    m.inputs = inpList

    # outputs
    outputs = comment.split("outputs:")[1]
    z = re.findall(pat_, outputs, re.MULTILINE)
    outList = []
    if z:
        for out in z:
            output={}
            name = out.replace("\r\n", "").replace("name:", "").lstrip().rstrip()
            pat_name = r'(%s\s*\r*\n*(.*\*\*\s*.+?:.+\r*\n*)+)'%(out)
            output["name"] = name
            output.update(attval(pat_name, outputs))
            outList.append(Output(output))
    m.outputs = outList
    
    return m

def attval(pat_name, string):  
    att = re.findall(pat_name, string, re.MULTILINE)
    print("hhkkkk", att)
    lines = att[0][0].split('\n')[1:-1]
    dic = {}
    for line in lines:
        attribute = re.search(pattern_attr_val, line).group("attribute")
        value = re.search(pattern_attr_val, line, re.ASCII).group("value").replace('\r', "")
        dic[attribute] = str(value)
    return dic


def extract_compo(comment):
    keywords = ["name", "version", "timestep" ]
    patterns = [r'(\b(?i)Name:\s*(?P<name>\w+))',
                r'(-Version:\s*(?P<version>\d+\.*\d+))',
                r'(-Time step:\s*(?P<timestep>\d+\.*\d*))'] 
    
    # header of modelUnit name, version, timestep
    head = {}
    i = 0
    for p in patterns:
        if re.search(p, comment):
            head[keywords[i]] = re.search(p, comment).group(keywords[i])   
        i = i + 1
    m = ModelComposition(head)

    # description element of modelUnit (Title, Authors, Reference, Institution, Abstract)
    pat_description = r'(Description:\s*\r*\n*(.*\*\s*\w+:.+\r*\n*/*)+)'   # Todo
    description = attval(pat_description, comment)
    d = Description()
    for k, v in description.items(): 
        setattr(d, k, v) 
    m.add_description(d)
    return m


"""
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract
from path import Path
file = Path("C:/Users/midingoy/Documents/SQ_Wheat_Phenology/src/f90/vernalizationprogress.f90")
r = ExtractComments(file, "!", '"""', '"""') 
v = extract(r)


"""