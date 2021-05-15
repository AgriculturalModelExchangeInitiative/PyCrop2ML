# inspired from http://csharphelper.com/blog/2015/10/extract-comments-from-a-c-file-in-c/

"""
    information extraction over structured documentation or comments



"""

 


# Return a file's comments.
def ExtractComments(filename, c_st_single="//", c_st_multi="/*", c_end_multi="*/", remove=[]):
    # If a language has no block comment style, be sure that the default c_st_multi and c_end_multi will never be met.
    with open(filename, 'r') as file:
        all_text = file.read()
    comments = "";
    if remove:
        for r in remove:
            all_text = all_text.replace(r, "")
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

"""
from pycropml.transpiler.antlr_py.readComment import ExtractComments
from path import Path
file = Path("C:/Users/midingoy/Documents/SQ_Wheat_Phenology/src/cs/Gaimean.cs")
file = Path("C:/Users/midingoy/Documents/SQ_Wheat_Phenology/src/py/Gaimean.py")
file = Path("C:/Users/midingoy/Documents/SQ_Wheat_Phenology/src/f90/Gaimean.f90")
r = ExtractComments(file) # C# java C++
r = ExtractComments(file, "#", '"""', '"""') # python
r = ExtractComments(file, "!") f90

"""