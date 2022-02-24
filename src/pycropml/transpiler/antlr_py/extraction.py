def lineNumber(s,l):
    c =  False
    n = 0
    for j in l:
        n = n + 1
        if s in j:
            c = True
            break
    if c: return n
    else: return -1

def replace(s,l):
    for k,v in enumerate(l):
        if s in v:
            l[k] = "  "*len(v)
            break
    return l

    
from collections import OrderedDict
def ExtractComments(all_text, c_st_single, c_st_multi, c_end_multi, pos=None):
    comments = OrderedDict()
    zz = all_text.split("\n")
    while (len(all_text) > 0):
        single_line_pos = all_text.find(c_st_single)
        if pos and single_line_pos!=0:
            txt = all_text
            while txt[single_line_pos-1]!="\n": 
                single_line_pos = txt.find(c_st_single, single_line_pos+1)
                if single_line_pos<0: break

        multi_line_pos = all_text.find(c_st_multi)
        if (single_line_pos < 0) and multi_line_pos <0 : break
        if (single_line_pos < 0) : single_line_pos = len(all_text)
        if (multi_line_pos < 0): multi_line_pos = len(all_text)
        if (single_line_pos < multi_line_pos):
            end_pos = all_text.find("\n", single_line_pos +1);
            if end_pos<0 :
                s = all_text[single_line_pos:]
                indice = lineNumber(s, zz) 
                zz = replace(s, zz)
                comments.update({indice : s})
                all_text = ""            
            else:
                s = all_text[single_line_pos: end_pos]
                indice = lineNumber(s, zz)
                zz = replace(s, zz)
                comments.update({indice :s})
                all_text = all_text[end_pos + 1:]          
        else:
            end_pos = all_text.find(c_end_multi, multi_line_pos + 1)
            if (end_pos < 0):
                s = all_text[multi_line_pos:]
                indice = multiLineNumber(s.split('\n'), zz)
                comments.update({indice : all_text[multi_line_pos:]})
                all_text = ""
            else:
                indice = multiLineNumber(all_text[multi_line_pos : end_pos+2].split('\n'), zz)
                comments.update({indice : all_text[multi_line_pos : end_pos+2]})
                all_text = all_text[end_pos + 1:]
    return comments

def multiLineNumber(vn, zz):
    f=False
    res = -1
    for k, j in enumerate(zz):
        if vn[0] in j:
            z = zip(vn, zz[k:k+len(vn)])
            check = [s in n for s,n in z]
            if all(check):
                f=True
                res = k
        else:
            continue
    if f: return res+1
    return -1