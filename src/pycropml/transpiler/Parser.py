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
    options = opt(**options_defaults)
    context = Main.Context([os.path.dirname(filename)], {}, cpp=False, language_level=3, options=options)
    scope = context.find_submodule(filename)
    with open(filename.encode('utf-8'), 'r') as f:
        source = f.read()
    source_desc = Scanning.FileSourceDescriptor(filename, source)
    tree = context.parse(source_desc, scope, pxd=None, full_module_name=filename)
    return tree
