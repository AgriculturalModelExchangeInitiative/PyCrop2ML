from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.env import Env
class F90_Cyml_ast():
    
   
    def __init__(self, tree, model=None, name=None, var= []):
        self.tree = tree
        self.model = model
        self.name = name
        self.recursive = False
        self.type_env = Env()
        self.var =  var

    def transform(self):
        self.type_env['functions'] = {}
        self.function_name = 'top level'
        self.decl = []
        body = self.visit(self.tree.body) if "body" in dir(self.tree) else self.visit(self.tree)
        
        return  {'type': 'module', 'body': body if isinstance(body, list) else [body]}

    
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


    def visit_declaration(self, node):
        res = []
        for de in node.decl:
            if de.name not in self.var:
                z = self.visit(de)
                self.type_env[z["name"]] = z["pseudo_type"]
                res.append(z)            
        if res:
            return {"type" : "declaration", "decl" : res}
        else:
            pass

    def visit_float(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'float', 'name': str(node.name), 'value': val, 'pseudo_type': 'float'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        elif "name" in dir(node): return {'type': 'float', 'name':str(node.name), 'pseudo_type': 'float'}
        else: print ("todo doble")

    def visit_int(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'int', 'name': str(node.name), 'value': val["value"], 'pseudo_type': 'int'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'int', 'value': val, 'pseudo_type': 'int'}
        elif "name" in dir(node): 
            return {'type': 'int', 'name':str(node.name), 'pseudo_type': 'int'}


    def visit_list(self, node):
        if "value" not in dir(node):
            z = []
        elif "name" not in dir(node):
            z = self.visit(node.init.value)
        else:
            z = self.visit(node.value.init.value)
        res =   {'type': 'list',
          'elements': z,           
          'pseudo_type': node.pseudo_type}  
        if "name" in dir(node):
            res["name"] = str(node.name) 
            return res
        if "args" in dir(node):
            return {"type": "standard_call",
                    "function":"copy",
                    "namespace":"system",
                    "pseudo_type": node.pseudo_type,
                    "args": node.args[0]
                }
    
    def visit_array(self, node):
        return {"type":"array",
                "name":str(node.name),
                "dim": node.dim,
                "elements":node.elts,
                "pseudo_type":node.pseudo_type
        }
   
    def visit_assignment(self, node):
        target = self.visit(node.target)
        value = self.visit(node.value)
        if "name" in value and target["name"]== value["name"]:
            return
        else:
            if "name" in value and (isinstance(value["pseudo_type"], list) and value["pseudo_type"][0]=="list"):
                return {'type': 'assignment',
                        'target': target,
                        'op': '=',
                        'value': {"type": "standard_call",
                                    "function":"copy",
                                    "namespace":"system",
                                    "pseudo_type": value["pseudo_type"],
                                    "args": value
                                },
                        'pseudo_type': 'Void'}
            return {'type': 'assignment',
           'target': target,
           'op': '=',
           'value': value,
           'pseudo_type': 'Void'}
    
    def visit_if_statement(self, node):
        return node
    
    def visit_for_range_statement(self, node):
            
        z =  {'type': 'for_range_statement',
         'start': self.visit(node.start),
         'end': self.visit(node.end),
         'step': self.visit(node.step),
         'index': self.visit(node.index),
         'block': self.visit(node.block)}

        self.decl.append({'type': 'declaration',
                          'decl': [{'type': z["index"]["pseudo_type"],
                                    'name': z["index"]["name"],
                                    'pseudo_type': z["index"]["pseudo_type"]}]})
        return z

    def visit_binary_op(self, node):
        if node.op == "**":
            return {
            'type': 'standard_call',
                    'namespace': 'system',
                    'args': [self.visit(node.left), self.visit(node.right)],
                    'pseudo_type': node.pseudo_type,
                    'function': 'pow'
        }
        return {'type': 'binary_op',
          'op': str(node.op),
          'left': self.visit(node.left),
          'right': self.visit(node.right),
          'pseudo_type': node.pseudo_type}

    
    def visit_standard_method_call(self, node):
        return {'type': 'standard_method_call',
                  'receiver': self.visit(node.receiver),
                  'args': self.visit(node.args) if "args" in dir(node) else [],
                  'message': node.message,
                  'pseudo_type': node.pseudo_type}

    def visit_local(self, node):
        return {"type":"local", "name":str(node.name), "pseudo_type": node.pseudo_type}

    def visit_ExprStatNode(self, node):
        return {
            "type": "ExprStatNode",
            "expr": self.visit(node.expr)
        }
    
    def visit_index(self, node):
        z = self.visit(node.sequence)
        index = self.visit(node.index)
        return {'type': 'index',
            'sequence': z,
            'index': index,
            'pseudo_type': z["pseudo_type"]}

    def visit_while_statement(self, node):
        
        return {'type': 'while_statement',
            'test': self.visit(node.test),
            'block': self.visit(node.block),
            'pseudo_type': 'Void'
        }

    def visit_comparison(self, node):
        return {'type': 'comparison',
            'op': node.op,
            'left':self.visit(node.left),
            'right': self.visit(node.right),
            'pseudo_type': 'Void'}

    def visit_standard_call(self, node):
        return {'type': 'standard_call',
              'namespace': node.namespace,
              'function': node.function,
              'args': self.visit(node.args),
              'pseudo_type': node.pseudo_type}

    def visit_custom_call(self, node):
        return {"type": "custom_call",
                "args": self.visit(node.args),
                "function": node.function,
                "pseudo_type": node.pseudo_type}

    def visit_unary_op(self, node):
        return {
            'type': 'unary_op',
                    'operator': str(node.operator),
                    'value': self.visit(node.value),
                    'pseudo_type': node.pseudo_type
        } 