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
#pattern_attr_val = r"(\*\*?\s*(?P<attribute>\w+)\s*:\s*(?P<value>.*))"

def ensure_text(v):
    if isinstance(v, bytes):
        return v.decode("utf-8")
    return v
'''
def _search_group(pattern, text, group=1, flags=0, default=None):
    """Return match.group(group) or default if no match."""
    m = re.search(pattern, text, flags)
    return m.group(group) if m else default

import json
def parse_default(val):
    if isinstance(val, str):
        s = val.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                return json.loads(s)
            except json.JSONDecodeError:
                return val
    return val

def _find_section(text, section_name):
    """
    Return the raw body of a section like '- inputs:' up to next top-level '- <something>:'
    Works even if the section is last.
    """
    # top-level section markers: start of line then '-' then name then ':'
    # allow optional comment prefixes like //, #, !, * and spaces
    pat = rf"(?im)^[ \t*/#!-]*-\s*{re.escape(section_name)}\s*:\s*(.*?)(?=^[ \t*/#!-]*-\s*\w+\s*:|\Z)"
    m = re.search(pat, text, flags=re.DOTALL)
    return m.group(1) if m else None

def _split_named_items(section_body):
    """
    Split a section body into chunks per '* name: ...'
    Returns list of (name, body_after_name).
    """
    if not section_body:
        return []

    # Normalize line endings
    section_body = section_body.replace("\r\n", "\n").replace("\r", "\n")

    # Find all occurrences of '* name: X' with their spans
    item_pat = re.compile(r"(?im)^[ \t*/#!-]*\*\s*name\s*:\s*(?P<name>[^\n]+)\n?", re.MULTILINE)
    matches = list(item_pat.finditer(section_body))
    if not matches:
        return []

    items = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section_body)
        name = ensure_text(m.group("name").strip())
        body = section_body[start:end].strip("\n")
        items.append((name, body))
    return items

def attval(text):
    """
    Parse lines like:
       * Title: ...
       ** description : ...
    Supports multiline continuation: lines without attribute are appended to last attribute.
    """
    if not text:
        return {}

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln for ln in text.split("\n") if ln.strip()]

    dic = {}
    last_attr = None

    for line in lines:
        # Try strict match first
        m = re.search(pattern_attr_val, line)
        if m:
            attr = m.group("attribute").strip()
            val = m.group("value").strip()
            val = ensure_text(val)
            last_attr = attr
        else:
            # continuation line
            if last_attr is None:
                # If we don't know what to attach to, skip or store under a generic key
                continue
            attr = last_attr
            val = ensure_text(line.strip())

        # Clean common comment junk at line start
        val = re.sub(r"^[ \t*/#!-]+", "", val).strip()

        if attr in dic:
            dic[attr] += "\n" + val
        else:
            dic[attr] = val

    return dic

def extract(comment):
    # -------- header (safe) --------
    header_patterns = {
        "name": r"(?im)\bName\s*:\s*(?P<name>[^\s,]+)",
        "version": r"(?im)\bVersion\s*:\s*(?P<version>[^\s,]+)",
        "timestep": r"(?im)\bTime\s*step\s*:\s*(?P<timestep>[^\s,]+)",
    }

    head = {}
    for k, pat in header_patterns.items():
        m = re.search(pat, comment)
        if m:
            head[k] = ensure_text(m.group(k))

    munit = ModelUnit(head)

    # -------- description (optional) --------
    desc_body = _find_section(comment, "Description")
    if desc_body:
        desc_dict = attval(desc_body)
        d = Description()
        for k, v in desc_dict.items():
            setattr(d, k, v)
        munit.add_description(d)

    # -------- inputs (optional) --------
    inputs_body = _find_section(comment, "inputs")
    inpList = []
    for name, body in _split_named_items(inputs_body):
        data = {"name": name}
        data.update(attval(body))
        inpList.append(Input(data))
    munit.inputs = inpList  # empty if missing

    # -------- outputs (optional) --------
    outputs_body = _find_section(comment, "outputs")
    outList = []
    for name, body in _split_named_items(outputs_body):
        data = {"name": name}
        data.update(attval(body))
        outList.append(Output(data))
    munit.outputs = outList  # empty if missing

    return munit

'''
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
            input["name"] = ensure_text(name)
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
            output["name"] = ensure_text(name)
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