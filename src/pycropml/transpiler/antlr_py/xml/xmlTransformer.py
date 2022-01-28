from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import *
from pycropml.transpiler.antlr_py.java.builtin_typed_api import *
from pycropml.transpiler.antlr_py.java.api_transform import *
from pycropml.transpiler.env import Env
from pycropml.transpiler.helpers import *
from pycropml.transpiler.antlr_py import parse
from pycropml.transpiler.antlr_py.java.api_declarations import Declarations
import ast
from ast import AST


class CompilationUnit(AliasNode):
    _fields_spec = ["packageDeclaration", "importDeclaration", "typeDeclaration"]

 
class Transformer(BaseNodeTransformer):
    def visit_CompilationUnit(self, node):
        return CompilationUnit.from_spec(node)

    
class AstTransformer():
    def __init__(self, tree):
        self.tree = tree
        self.base = 0
        self.type_env = Env(dict(list(TYPED_API.items())), None)

    def transformer(self):
        self.type_env['functions'] = {}
        self.assign = False
        self.function_name = 'top level'
        self.definitions = []
        self._definition_index = {'functions': {}}
        self.top_level(self.tree)
        body = self.visit(self.tree)
        return {'body': body if isinstance(body, list) else [body]}
    
    def top_level(self, tree):
        pass

    def getpath(self, node, child, tab=[]):
        if isinstance(node, list):
            for i in node:
                self.getpath(i,child)
        for i in node.children:
            result = getattr(i, child, None)
            if result:
                tab.append(result)
            elif result is None and "children" in dir(i):
                self.getpath(i, child, tab)
        return tab

    def visit(self, node):
        #if isinstance(node, ParserRuleContext):
        if isinstance(node, AST):
            x = node.get_position()
            fields = {field: getattr(node, field)
                    for field in node._fields  }# get_field_names(node)
            if "self" in fields:
                fields.pop("self")
            #l = getattr(node, 'position', None)
            fields["node"] = node       
            if x:
                fields['location'] = x["line_start"],x["column_start"]
            else:
                fields['location'] = None
            return getattr(self, 'visit_%s' % type(node).__name__.lower())(**fields)# [:-7]
        elif isinstance(node, list):
            results = []
            for n in node:
                x = self.visit(n)
                if isinstance(x, list):
                    results.extend(x)
                else:
                    results.append(x)
            return results
        elif isinstance(node, dict):
            return {k: self.visit(v) for k, v in node.items()}
        else:
            return node
    
    def visit_compilationunit(self, node, packageDeclaration, importDeclaration, typeDeclaration, location):
        impdecl,pkgdec,typdecl  = None,None,None
        if packageDeclaration:
            pkgdec = self.visit(packageDeclaration)
        if importDeclaration:
            impdecl = self.visit(importDeclaration)
        if typeDeclaration:
            typdecl = self.visit(typeDeclaration)
        return {"type": "module",
                "imports":impdecl,
                "body": [pkgdec,typdecl],
                "pseudo_type": "Void"}
    
