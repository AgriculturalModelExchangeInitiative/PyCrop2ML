from pycropml.transpiler.antlr_py import parse, simplifyAntlrTree
from  pycropml.transpiler.antlr_py.csharp  import csharpTransformer
from pycropml.transpiler.antlr_py.fortran import fortranTransformer
from pycropml.transpiler.antlr_py.java import javaTransformer
from pycropml.transpiler.antlr_py.python import pythonTransformer
from pycropml.transpiler.antlr_py.xml import xmlTransformer

from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from path import Path
import pycropml.transpiler.antlr_py

languages = ['cs',"bioma", "dssat", "f90", "java", "simplace", "xml", "py"]
NAMES = {'cs':'csharp','sirius':'csharp',"bioma":"csharp", "dssat":"fortran", "f90":"fortran", "java":"java", "simplace":"java", "xml":"xml", "py":"python", "openalea":"python", "stics":"f90"}

GENERATORS = {
    format: getattr(getattr(
                    pycropml.transpiler.antlr_py,
                    '%s' % NAMES[format]), '%sTransformer'% NAMES[format])
    for format in languages
}

def to_dictASG(code, language,comments=None, env=None):

    """Transform CST provided from ANTLR parsers into a common language ASG

    Args:
        filePath (Path): path of the class

    Returns:
        dict: A common Abstract Semantic Graph CASG of a specific language in dict format
    """
    tree = parse.parsef(code,language, start="compilation_unit", strict=False)
    ast_proc = simplifyAntlrTree.process_tree(tree,transformer_cls =GENERATORS[language].Transformer )
    trans = GENERATORS[language].AstTransformer(ast_proc,code, comments, env).transformer()
    return trans

def to_CASG(dictree):
    """Transform CST provided from ANTLR parsers into a common language ASG

    Args:
        filePath (Path): path of the class

    Returns:
        Node: A common Abstract Semantic Graph CASG of a specific language
    """
    csag= transform_to_syntax_tree(dictree["body"])
    return csag