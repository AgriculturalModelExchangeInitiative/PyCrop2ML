
from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.antlr_py import simplifyAntlrTree

from ast import AST


class File_c(AliasNode):
    _fields_spec = ["command_invocation"]


class Transformer(BaseNodeTransformer):

    def visit_File_c(self, node):
        return File_c.from_spec(node)

class AstTransformer():
    def __init__(self, tree, code :str = None ,comments: str=None):
        self.tree = tree
        self.base = 0
        self.comments = comments
        self.definitions = None
        self.code : str = code
        if self.code:
            self.codelines = self.code.split("\n")

    def transformer(self):
        self.definitions = []
        self.visit_top_level(self.tree.command_invocation)
        return self.definitions

    def visit_top_level(self, nodes):
        for n in nodes:
            if n.Identifier == "set": 
                z = n.single_argument[0]
                if z =="source_list":
                    res = n.single_argument
                    res.remove(n.single_argument[0])
                    for r in res:
                        if '"' in str(r):
                            self.definitions.append(str(r).replace('"', ""))
                
 
        
def retrievefiles(code):
    tree = parsef(code,"cmake", start="file_c", strict=False)
    ast_proc = simplifyAntlrTree.process_tree(tree,transformer_cls =Transformer )
    trans = AstTransformer(ast_proc,code, None).transformer()
    return trans
       



       


    