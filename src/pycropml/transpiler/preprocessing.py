# coding: utf8
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware


class check_range_function(Middleware):
    
    def __init__(self):
        self.res = False
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_standard_call(self, tree):
        if tree.function == "range":
            self.res = True
        return tree