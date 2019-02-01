import os
from Cython.Compiler import Scanning
from Cython.Compiler import Main

options_defaults = dict(
    show_version = 0,
    use_listing_file = 0,
    errors_to_stderr = 1,
    cplus = 0,
    output_file = None,
    annotate = None,
    annotate_coverage_xml = None,
    generate_pxi = 0,
    capi_reexport_cincludes = 0,
    working_path = "",
    timestamps = None,
    verbose = 0,
    quiet = 0,
    compiler_directives = {},
    embedded_metadata = {},
    evaluate_tree_assertions = True,
    emit_linenums = False,
    relative_path_in_code_position_comments = True,
    c_line_in_traceback = True,
    language_level = 3,  # warn but default to 2
    formal_grammar = False,
    gdb_debug = False,
    compile_time_env = None,
    common_utility_include_dir = None,
    output_dir=None,
    build_dir=None,
    cache=None,
    create_extension=None,
    np_pythran=False
)
class opt:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


    
def parser(filename):
    
    """ Read, parse a Cython code and generate an abstract syntaxique tree.
    
    Context: Compilation context: contains every pxd ever loaded, path information and the data related to the compilation.
    Class where it is implemented Cython parse method.
    
    options: To set Compilation Options as 
                language_level:     The source language level to use,
                formal_grammar:     to define if it will be used to Parse the file
                evaluate_tree_assertions:   evaluate parse tree
                show_version :  Display version number
                use_listing_file:  Generate a .lis file
                errors_to_stderr:   Echo errors to stderr when using .lis
                include_path:    Directories to search for include files
                output_file:     Name of generated .c file
                generate_pxi:   generate .pxi file for public declarations
                capi_reexport_cincludes:   Add cincluded headers to any auto-generated  header files.
                timestamps:   Only compile changed source files  
                verbose : Always print source names being compiled
                compiler_directives:    Overrides for pragma options (see Options.py)
                embedded_metadata:      Metadata to embed in the C file as json.
                evaluate_tree_assertions:  Test support: evaluate parse tree assertions
                cplus :     Compile as c++ code                
    
    Here default options were used except language level
    
    Scanning.FileSourceDescriptor: Represents a code source. Only file sources for Cython code supported
    """
    options = opt(**options_defaults)
    context = Main.Context([os.path.dirname(filename)], {}, cpp=False, language_level=3, options=options)
    scope = context.find_submodule(filename)
    with open(filename.encode('utf-8'), 'r') as f:
        source = f.read()
    source_desc = Scanning.FileSourceDescriptor(filename, source)
    tree = context.parse(source_desc, scope, pxd=None, full_module_name=filename)
    return tree