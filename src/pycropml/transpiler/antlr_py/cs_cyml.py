# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:05:11 2020

@author: midingoy
"""

from pycropml.transpiler.antlr_py.cs import csharpRules
from pycropml.transpiler.rules.csharpRules import CsharpRules
from pycropml.transpiler.env import Env


def cyml_ru(cs_op, ru):  
    for k, v in ru.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if v == cs_op:
            return k
    
lib = csharpRules.Cs_CymlRules()
                
from pycropml.transpiler.pseudo_tree import Node
class Cs_Cyml_ast():
    
    op = CsharpRules().binary_op
    math_ = CsharpRules().functions["math"]
    types_ = CsharpRules().types
    
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        self.recursive = False
        self.type_env = Env()


    def visit(self, node):
        '''
        Parameters
        ----------
        node : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if isinstance(node, list):
            results = []
            for n in node:
                x = self.visit(n)
                if isinstance(x, list):
                    results.extend(x)
                else:
                    results.append(x)
            return results
        elif isinstance(node, Node):
            return getattr(self, 'visit_%s'%(node.type))(node)
        else: 
            return node
            
    def transform(self):
        self.type_env['functions'] = {}
        self.function_name = 'top level'
        body = self.visit(self.tree.body)
        return  {'type': 'module', 'body': body if isinstance(body, list) else [body]}
    
    def visit_classDef(self, node):
        return self.visit(node.block)
    
    def visit_method(self, node):
        self.function_name = node.name
        pa = self.visit(node.params)
        print(pa)
        self.type_env.top['functions'][node.name] = [ 'Function'] + ([None] * len(node.params)) + [None]
        self.type_env.top[node.name] = self.type_env.top['functions'][node.name]
        env = {a["name"]: a["pseudo_type"] for a in pa}
        print(env)
        self.type_env, old_type_env = self.type_env.top.child_env( env), self.type_env
        domain_func = list(env.values())
        print("hh",domain_func)
        self.type_env.top["functions"][node.name][1:-1] = domain_func
        print("hh",domain_func)
        print("jj", self.type_env.top["functions"][node.name])
        block = self.visit(node.block)
        self.type_env = old_type_env
        
        z = {
            'type':   "function_definition",
            'name':   node.name,
            'params': pa,
            'return_type':  self.type_env.top["functions"][node.name][-1],
            'pseudo_type': self.type_env.top["functions"][node.name],
            'block': block,
            'recursive':self.recursive

        }
        return  z
    
    def translate_decl(self, type_):
        if not isinstance(type_, list):
            s = lib.types[type_]
        else: s = [self.translate_decl(i) for i in type_]
        return s
    
    def visit_local(self, node):
        #ps = self.translate_decl(node.pseudo_type)
        #if str(node.name) not in self.type_env: self.type_env[str(node.name)]= ps
        return {"type":"local", "name":str(node.name), "pseudo_type": self.translate_decl(node.pseudo_type)}
    
    def visit_declaration(self, node):
        z = self.visit(node.decl)
        self.type_env[z["name"]] = z["pseudo_type"]
        return {"type":"declaration", "decl": [z]}
    
    def visit_int(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'int', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'int'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'int', 'value': val, 'pseudo_type': 'int'}
        elif "name" in dir(node): 
            #if str(node.name) not in self.env:
            return {'type': 'int', 'name':str(node.name), 'pseudo_type': 'int'}

    def visit_double(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'float', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'float'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        elif "name" in dir(node): return {'type': 'float', 'name':str(node.name), 'pseudo_type': 'float'}
 
    def visit_float(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'float', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'float'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        elif "name" in dir(node): return {'type': 'float', 'name':str(node.name), 'pseudo_type': 'float'}

    def visit_array(self, node):
        if "value" not in dir(node):
            self.type_env[str(node.name)] = self.translate_decl(node.pseudo_type)
            return {'type': 'array', 'name': str(node.name), 'pseudo_type':  self.translate_decl(node.pseudo_type)}
        z = self.visit(node.value.value)
        self.type_env[str(node.name)] = z[0]["pseudo_type"]
        return   {'type': 'array',
          'name': str(node.name),
          'elements': z,           
          'pseudo_type': ['array', z[0]["type"]],
          'dim':1}   
    
    def visit_list(self, node):
        z = self.visit(node.init.value) if "name" not in dir(node) else self.visit(node.value.init.value)
        res =   {'type': 'list',
          'elements': z,           
          'pseudo_type': self.translate_decl(node.pseudo_type)}  
        if "name" in dir(node):
            res["name"] = str(node.name)
        
        self.type_env[res["name"]] = res["pseudo_type"]
        return res
        
    def visit_assignment(self, node):
        return {'type': 'assignment',
           'target': self.visit(node.target),
           'op': '=',
           'value': self.visit(node.value),
           'pseudo_type': 'Void'}
    
    def visit_implicit_return(self, node):
        z = self.visit(node.value)
        whiplash = self.type_env.top["functions"][self.function_name]
        whiplash[-1] = z['pseudo_type']
        
        return {'type': 'implicit_return',
         'value': z, 'pseudo_type': z['pseudo_type']}
    
    def visit_binary_op(self, node):
        return {'type': 'binary_op',
          'op': str(node.op),
          'left': self.visit(node.left),
          'right': self.visit(node.right),
          'pseudo_type': self.visit(node.pseudo_type)}
    
    def visit_if_statement(self, node):
        return {'type': 'if_statement',
         'test': self.visit(node.test),
         'block': self.visit(node.block),
         'pseudo_type': 'Void',
         'otherwise': self.visit(node.otherwise)}
 
    def visit_else_statement(self, node):
        return {'type': 'else_statement',
             'block': self.visit(node.block),
             'pseudo_type': 'Void'}
    
    def visit_elseif_statement(self, node):
        return {'type': 'elseif_statement',
           'test': self.visit(node.test),
           'block': self.visit(node.block),
           'pseudo_type': 'Void'}
    
    def visit_comparison(self, node):
        return {'type': 'comparison',
            'op': cyml_ru(node.op, self.op),
            'left':self.visit(node.left),
            'right': self.visit(node.right),
            'pseudo_type': 'Void'}
    
    def visit_standard_call(self, node):
        ns = node.namespace
        function = lib.functions[ns][node.function]
        if not callable(function): 
            return {'type': 'standard_call',
              'namespace': function.split(".")[0],
              'function': function.split(".")[1],
              'args': self.visit(node.args),
              'pseudo_type': node.pseudo_type}
        else:  
            args = self.visit(node.args)
            newNode = self.visit(function(node, args))
            return newNode
    
    def visit_standard_method_call(self, node):
        return {'type': 'standard_method_call',
                  'receiver': self.visit(node.receiver),
                  'args': [],
                  'message': self.visit(node.message),
                  'pseudo_type': self.translate_decl(node.pseudo_type)}
    
    def visit_custom_call(self, node):
        return {"type": "custom_call",
                "args": self.visit(node.args),
                "function": node.function,
                "pseudo_type": self.translate_decl(node.pseudo_type)}
    
    def visit_for_range_statement(self, node):
        
        return {'type': 'for_range_statement',
         'start': self.visit(node.start),
         'end': self.visit(node.end),
         'step': self.visit(node.step),
         'index': self.visit(node.index),
         'block': self.visit(node.block)}
        
