from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.env import Env
from pycropml.transpiler.antlr_py.fortran.fortran_preprocessing import Assignment, TransformLocal
from pycropml.transpiler.antlr_py.fortran.fortranExtraction import FortranExtraction
from pycropml.transpiler.ast_transform import transform_to_syntax_tree




class F90_Cyml_ast():
    """G
    """
    
    def __init__(self, tree, model=None, name=None, var= [], treeG=None):
        self.tree = tree
        self.model = model
        self.name = name
        self.recursive = False
        self.type_env = Env()
        self.var = var if var else []
        self.treeG = treeG if treeG else None
        

    def transform(self):
        self.type_env['functions'] = {}
        self.function_name = 'top level'
        self.decl = []
        #self.visit_top_level(self.tree.body)
        body = self.visit(self.tree.body) if "body" in dir(self.tree) else self.visit(self.tree)
        
        return  {'type': 'module', 'body': body if isinstance(body, list) else [body]}

    
    def visit(self, node):
        '''
        Parameters
        ----------
        node : Node
            DESCRIPTION.

        Returns
        -------
        dict
            Common Code Model Representation based on CyML constructs.

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
        
    def visit_top_level(self, nodes):
        for n in nodes:
            if n.type == "function_definition": #isinstance(n, SubroutineSubprogram)
                self.definitions.append(('function', n.name))
                self._definition_index['functions'][n.name] = n
                self.type_env.top['functions'][n.name] = [
                        'Function'] + ([None] * len(n.params)) + [None]
                self.type_env.top[n.params] = self.type_env.top['functions'][str(n.params)]

    def visit_import(self, node):
        return
    
    def visit_comments(self, node):
        return {"type":"comments", "comments":node.comments}

    def visit_tuple(self, node):
        return {'type':'tuple',
                'elements':self.visit(node.elements),
                "pseudo_type": node.pseudo_type}


    def visit_function_definition(self, node):
        varnotdeclared = node.notdeclared
        imports = node.imports
        extr2 = FortranExtraction()
        if varnotdeclared:
            res = extr2.getDecl(self.treeG, imports, varnotdeclared)
            otherparams = list(res.values())
        else: otherparams=[]
        pa = otherparams + self.visit(node.params)
        block = self.visit(node.block)       
        z = {
            'type':   "function_definition",
            'name':   node.name,
            'params': pa,
            'return_type':  node.return_type,
            'pseudo_type': node.pseudo_type,
            'block': block,
            'recursive':self.recursive,
           "comments": node.comments

        }
        return  z

    def visit_module(self, node):
        return self.visit(node.block)

    def visit_test(self, node):
        return {"type":"main", "body":self.visit(node.body)}

    def visit_declaration(self, node):
        res = []
        for de in node.decl:
            if de.name not in self.var:
                z = self.visit(de)
                self.type_env[z["name"]] = z["pseudo_type"]
                res.append(z) 
                self.var.append(z["name"])           
        if res:
            return {"type" : "declaration", "decl" : res, "comments":node.comments}
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

    def visit_bool(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'bool', 'name': str(node.name), 'value': val["value"].capitalize() if "value" in val else val.capitalize(), 'pseudo_type': 'bool'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'bool', 'value': val.capitalize(), 'pseudo_type': 'bool'}
        elif "name" in dir(node): 
            return {'type': 'bool', 'name':str(node.name), 'pseudo_type': 'bool'}

    def visit_str(self, node):
        if "value" in dir(node) and "name" in dir(node): 
            val = self.visit(node.value)
            return  {'type': 'str', 'name': node.name, 'value': val["value"], 'pseudo_type': 'str'}
        elif "value" in dir(node): 
            val = self.visit(node.value)
            return {'type': 'str', 'value': val, 'pseudo_type': 'str'}
        elif "name" in dir(node): return {'type': 'str', 'name':node.name, 'pseudo_type': 'str'}


    def visit_list(self, node):
        if "value" not in dir(node):
            z = []
            if "elements" in dir(node):
                z = self.visit(node.elements)
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
                    "args": self.visit(node.args[0])
                }
        if "elements" in dir(node):
            return res
    
    def visit_array(self, node):
        if "name" not in dir(node):
            return {'type': 'array',
                 'elements': self.visit(node.elements),
                 'pseudo_type': node.pseudo_type}            
        return {"type":"array",
                "name":str(node.name),
                "dim": node.dim,
                "elts":self.visit(node.elts),
                "pseudo_type":node.pseudo_type
        }
   
    def visit_assignment(self, node):
        target = self.visit(node.target)
        value = self.visit(node.value)
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
                        'pseudo_type': 'Void',
                        "comments":node.comments}
        return {'type': 'assignment',
           'target': target,
           'op': '=',
           'value': value,
           'pseudo_type': 'Void',
           "comments":node.comments}
    
    def visit_if_statement(self, node):
        return {'type': 'if_statement',
                 'test': self.visit(node.test),
                 'block': self.visit(node.block),
                 'pseudo_type': 'Void',
                 'otherwise': self.visit(node.otherwise),
                   "comments": node.comments}

    def visit_implicit_return(self, node):
        z = self.visit(node.value)
        
        return {'type': 'implicit_return',
         'value': z, 'pseudo_type': z['pseudo_type'],
           "comments": node.comments}


    def visit_else_statement(self, node):
        return {'type': 'else_statement',
             'block': self.visit(node.block),
             'pseudo_type': 'Void',
           "comments": node.comments}
    
    def visit_elseif_statement(self, node):
        return {'type': 'elseif_statement',
           'test': self.visit(node.test),
           'block': self.visit(node.block),
           'pseudo_type': 'Void',
           "comments": node.comments}
    
    
    def visit_for_range_statement(self, node):
        
        step = self.visit(node.step)
        if step["type"] == "unary_op" and step["operator"]=="-":
            end = {"type":"binary_op", "op":"-","left":self.visit(node.end), "right":{"type":"int", "value":"1"}}
        else:
            end ={"type":"binary_op", "op":"+","left":self.visit(node.end), "right":{"type":"int", "value":"1"}}
            
        z =  {'type': 'for_range_statement',
         'start': self.visit(node.start),
         'end': end,
         'step': step,
         'index': self.visit(node.index),
         'block': self.visit(node.block),
         "comments": node.comments}

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
    
    def visit_sliceindex(self, node):
        rec = self.visit(node.receiver)
        print(rec)
        return {'type': 'sliceindex',
                'receiver': self.visit(node.receiver),
                'message': 'sliceindex',
                'args': self.visit(node.args),
                'pseudo_type': rec["pseudo_type"]}
    
    def visit_index(self, node):
        z = self.visit(node.sequence)
        index = self.visit(node.index)
        if not isinstance(index, list): index = index
        elif isinstance(index, list) and len(index)==1: index = index[0]
        else: print("#########TODO") #TODO
        #print("bababa", index)
        return {'type': 'index',
            'sequence': z,
            'index': {"type":"binary_op", "op":"-", "left":index, "right":{"type":"int", "value":"1","pseudo_type":"int"}},
            'pseudo_type': z["pseudo_type"][-1]}

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
    
    def visit_whereconstruct(self, node):
        test = self.visit(node.test)
        body = self.visit(node.body)
        m = transform_to_syntax_tree(body)
        r = TransformLocal()
        arr = r.process(m)
        res = {'type': 'for_statement',
        'sequences': {'type': 'for_sequence_with_index',
            'sequence': test["left"]},
        'iterators': {'type': 'for_iterator_with_index',
            'index': {'type': 'local', 'pseudo_type': 'int', 'name': 'i_cyml'},
            'iterator': {'type': 'local', 'pseudo_type': test["left"]["pseudo_type"][-1], 'name': 'j_cyml'}},
        'block': {'type': 'if_statement',
            'test': {'type': 'comparison',
            'op': test["op"],
            'left': {'type': 'local',
            'name': 'j_cyml',
            'pseudo_type':  test["left"]["pseudo_type"][-1]},
            'right': test["right"],
            'pseudo_type': 'bool'},
            'block': arr,
            'pseudo_type': 'Void',
            'otherwise': []},
        'pseudo_type': 'Void'}
        return res