""" Merge files into one file with unique functions.

Render a set of pyx files containing the same function several into one file containing one and only one function of each name.

"""
import re

def function_names(code):
    # Regular expression pattern to match function names
    # It assumes functions start with 'def' or 'cpdef'
    pattern = r'\b(?:def|cpdef)\s+([a-zA-Z_]\w*)\s*\('

    # Find all function names using regex
    function_names = re.findall(pattern, code)

    # Remove duplicates by converting to a set
    unique_function_names = list(function_names)

    return unique_function_names

# Define a function to retrieve the code of a specific function
def get_function_code(content, function_name):
    # Regex to capture function definition
    function_pattern = rf'(def|cpdef)\s+{function_name}\s*\((?:[^()]*(?:\([^()]*\))?)*\)\s*:[\s\S]*?'
    
    # Position of the function
    match = re.search(function_pattern, content, re.MULTILINE)
    
    if not match:
        return ''

    start = match.start()
    lines = content[start:].splitlines()
    function_lines = []
    
    # Iter on the next lines from the function
    # First line is the function definition
    count = 0
    for line in lines:
        if (line.startswith('def ') or line.startswith('cpdef ')) and count != 0:
            # Stop after the first line begining with def without indent
            break  
        function_lines.append(line)
        count +=1
    
    function_lines.append('')
    return '\n'.join(function_lines)

    

def unique_functions(files):
    unique_functions = []

    codes = []
    for fn in files:
        with open(fn.encode('utf-8'), 'r') as file:
            content = file.read()

        funs = function_names(content)
        for fun in funs:
            if fun in unique_functions:
                print(f'{fun} is duplicated')
            else:
                unique_functions.append(fun)
                function_code = get_function_code(content, fun)
                #print(function_code)
                codes.append(function_code)

    content = '\n'.join(codes)

    return content
                

