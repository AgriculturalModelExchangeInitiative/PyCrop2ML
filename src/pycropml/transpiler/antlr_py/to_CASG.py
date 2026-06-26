from pycropml.transpiler.antlr_py import parse, simplifyAntlrTree
from  pycropml.transpiler.antlr_py.csharp  import csharpTransformer
from pycropml.transpiler.antlr_py.fortran import fortranTransformer
from pycropml.transpiler.antlr_py.java import javaTransformer
from pycropml.transpiler.antlr_py.python import pythonTransformer
from pycropml.transpiler.antlr_py.xml import xmlTransformer

from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from path import Path
import pycropml.transpiler.antlr_py
import sys
import logging
import traceback

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

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
    # Step 1: Parse the code
    try:
        tree = parse.parsef(code, language, start="compilation_unit", strict=False)
    except Exception as e:
        logger.error(f"Failed to parse {language} code")
        logger.error(f"Error type: {type(e).__name__}")
        logger.error(f"Error message: {str(e)}")
        logger.error(f"Code snippet (first 200 chars): {code[:200] if code else '<empty>'}")
        logger.error(f"Traceback:\n{traceback.format_exc()}")
        sys.exit(1)
    
    # Step 2: Process the tree
    try:
        ast_proc = simplifyAntlrTree.process_tree(tree, transformer_cls=GENERATORS[language].Transformer)
    except Exception as e:
        logger.error(f"Failed to process tree for {language}")
        logger.error(f"Error type: {type(e).__name__}")
        logger.error(f"Error message: {str(e)}")
        logger.error(f"Tree text (first 200 chars): {tree.getText()[:200] if tree else '<empty>'}")
        logger.error(f"Traceback:\n{traceback.format_exc()}")
        sys.exit(1)
    
    # Step 3: Transform AST
    try:
        trans = GENERATORS[language].AstTransformer(ast_proc, code, comments, env).transformer()
    except Exception as e:
        logger.error(f"Failed to transform AST for {language}")
        logger.error(f"Error type: {type(e).__name__}")
        logger.error(f"Error message: {str(e)}")
        logger.error(f"Traceback:\n{traceback.format_exc()}")
        sys.exit(1)
    
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