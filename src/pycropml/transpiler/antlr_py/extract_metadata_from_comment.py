# inspired from http://csharphelper.com/blog/2015/10/extract-comments-from-a-c-file-in-c/

"""
    information extraction over structured documentation or comments

"""
from pycropml.composition import ModelComposition
from pycropml.modelunit import ModelUnit
from pycropml.description import Description
from pycropml.inout import Input, Output
import os
import re
# Return a file's comments.
def ExtractComments(filename, c_st_single, c_st_multi, c_end_multi):
    # If a language has no block comment style, be sure that the default c_st_multi and c_end_multi will never be met.
    if os.path.isfile(filename):
        with open(filename, 'r',  encoding='utf-8') as file:
            all_text = file.read()
    else: all_text = filename
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

pattern_attr_val = r"(\*\*?\s*(?P<attribute>\w+)\s*:\s*(?P<value>[\-\(\)\w+\s:,ï\[\]\\_\./\'\*]*))"


def extract(comment):
    keywords = ["name", "version", "timestep" ]
    patterns = [r'(\s*-?\s*Name:\s*(?P<name>\w+))',
                r'(\s*-?\s*Version:\s*(?P<version>\d+\.*\d+))',
                r'(\s*-?\s*Time step:\s*(?P<timestep>\d+\.*\d*))'] 
    
    # header of modelUnit name, version, timestep
    head = {}
    i = 0
    for p in patterns:
        if re.search(p, comment):
            head[keywords[i]] = re.search(p, comment).group(keywords[i])   
        i = i + 1
    m = ModelUnit(head)

    # description element of modelUnit (Title, Authors, Reference, Institution, Abstract)
    pat_description = r'-\s*Description:\s*(.*?)(?=\n\s*[#!/]*\s*-\s*inputs|\n\s*[#!/]*\s*-\s*outputs|$)'
    text_description = re.search(pat_description, comment, re.DOTALL).group(1)
    description = attval(text_description)
    d = Description()
    for k, v in description.items(): setattr(d, k, v) 
    m.add_description(d)

    # inputs
    pat_inputs = r'-\s*inputs:\s*(.*?)(?=\n\s*[#!/]*\s*-\s*outputs|\n\s*[#!/]*\n)'
    inputs_part = re.search(pat_inputs, comment, re.DOTALL).group(1)
    pat_input = r'\*\s*name:\s*(.*?)(?=\n\s*[#!/]*\s*\*\s*name:|\n\n)'
    input_parts = re.findall(pat_input, inputs_part+"\n\n", re.DOTALL)
    inpList = []
    if input_parts:
        for inp in input_parts:
            input={}
            name = inp.split("\n")[0].strip()
            inp = "\n".join(inp.split("\n")[1:])
            input["name"] = name
            input.update(attval(inp))
            inpList.append(Input(input))
    m.inputs = inpList

    # outputs
    pat_outputs = r'-\s*outputs:\s*(.*?)(?=\n\s*[#!/]*\s*-\s*inputs|\n\s*[#!/]*\s*\n)'
    outputs_part = re.search(pat_outputs, comment, re.DOTALL).group(1)
    pat_output = r'\*\s*name:\s*(.*?)(?=\n\s*[#!/]*\s*\*\s*name:|\n\n)'
    output_parts = re.findall(pat_output, outputs_part+'\n\n', re.DOTALL)
    outList = []
    if output_parts:
        for out in output_parts:
            output={}
            name = out.split("\n")[0].strip()
            out = "\n".join(out.split("\n")[1:])
            output["name"] = name
            output.update(attval(out))
            outList.append(Output(output))
    m.outputs = outList
    
    return m

def attval(text):  
    space = "    "
    lines = text.split('\n')
    dic = {}
    last_attr = None
    for line in lines:
        if not line: continue
        obj = re.search(pattern_attr_val, line)
        if not obj: attribute = last_attr
        else: attribute = obj.group("attribute")
        obj = re.search(pattern_attr_val, line, re.ASCII)
        if not obj:
            value =  '\n' + space*3 + line.strip()
        else: value = obj.group("value").replace('\r', "").strip()
        if attribute in dic : dic[attribute] += str(value)
        else: dic[attribute] = value
        last_attr = attribute
    return dic



def extract_compo(comment):
    keywords = ["name", "version", "timestep" ]
    patterns = [r'(\s*-?\s*Name:\s*(?P<name>\w+))',
                r'(\s*-?\s*Version:\s*(?P<version>\d+\.*\d+))',
                r'(\s*-?\s*Time step:\s*(?P<timestep>\d+\.*\d*))'] 
    
    # header of modelUnit name, version, timestep
    head = {}
    i = 0
    for p in patterns:
        if re.search(p, comment):
            head[keywords[i]] = re.search(p, comment).group(keywords[i])   
        i = i + 1
    m = ModelComposition(head)
    # description element of modelUnit (Title, Authors, Reference, Institution, Abstract)
    pat_description = r'-\s*Description:\s*(.*?)(?=\n\s*[#!/]*\s*-\s*inputs|\n\s*[#!/]*\s*-\s*outputs|$)'
    text_description = re.search(pat_description, comment, re.DOTALL).group(1)
    description = attval(text_description)    
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