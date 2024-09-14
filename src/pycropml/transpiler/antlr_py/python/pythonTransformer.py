from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import *
from pycropml.transpiler.antlr_py.python.builtin_typed_api import *
from pycropml.transpiler.antlr_py.python.api_transform import *
from pycropml.transpiler.env import Env
from pycropml.transpiler.helpers import *
from pycropml.transpiler.antlr_py import parse
import ast
from ast import AST, expr
def reduceT(function, iterable, initializer=None):
    iterable_new = [j for i, j in enumerate(iterable) if i%2!=1]
    op = [j for i, j in enumerate(iterable) if i%2==1]
    it = iter(iterable_new)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for k,element in enumerate(it):
        value = function(value, element, op[k])
    return value

def treeWalker(node, child):
    tab =[]
    for j in node.children:
        if j==child:
            tab.append(j)
    if len(tab)!=0: return tab
    else:
        ext_node = treeWalker(node.children, child)
        if len(ext_node)!=0:
            return ext_node
    return None      


class Root(AliasNode):
    _fields_spec = ["single_input", "file_input","eval_input"]

class File_input(AliasNode):
    _fields_spec = ["stmt"]

class Funcdef(AliasNode):
    _fields_spec = ["name", "typedargslist", "test", "suite"]

class Typedargslist(AliasNode):
    _fields_spec = ["def_parameters","args", "kwargs"]

class Def_parameters(AliasNode):
    _fields_spec = ["def_parameter"]

class Def_parameter(AliasNode):
    _fields_spec = ["named_parameter", "test", "STAR"]

class Named_parameter(AliasNode):
    _fields_spec = ["name", "test"]
    
class Simple_stmt(AliasNode):
    _fields_spec = ["small_stmt"]

class Import_stmt(AliasNode):
    _fields_spec = ["dotted_as_names"]

class Suite(AliasNode):
    _fields_spec = [ "simple_stmt", "stmt"]

class Stmt(AliasNode):
    _fields_spec = ["simple_stmt",  "compound_stmt"]

class Return_stmt(AliasNode):
    _fields_spec =["testlist"]

class Testlist(AliasNode):
    _fields_spec =["test"]

class Test(AliasNode):
    _fields_spec =["logical_test", "IF",  "test", "varargslist"]

class Logical_test(AliasNode):
    _fields_spec =["comparison", "NOT", "logical_test","AND","OR"]

class Comparison(AliasNode):
    _fields_spec =["comparison", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ",  "NOT_EQ_1",  "NOT_EQ_2", "NOT", "IN" , "IS", "expr"]
    
class Expr(AliasNode):
    _fields_spec = ["AWAIT","expr", "atom", "trailer","POWER","ADD","MINUS","NOT_OP","STAR","DIV","MOD","IDIV", "AT","LEFT_SHIFT","RIGHT_SHIFT","AND_OP","XOR","OR_OP"]

class Trailer(AliasNode):
    _fields_spec =["name", "arguments"]

class Arguments(AliasNode):
    _fields_spec =["arglist", "subscriptlist"]

class Arglist(AliasNode):
    _fields_spec =["argument"]

class Subscriptlist(AliasNode):
    _fields_spec =["subscript", "COMMA"]

class Argument(AliasNode):
    _fields_spec =["test","comp_for", "ASSIGN" ,"POWER", "STAR"]

class Subscript(AliasNode):
    _fields_spec =["ELLIPSIS", "test", "COLON", "sliceop"]

class Atom(AliasNode):
    _fields_spec =["OPEN_PAREN", "yield_expr", "testlist_comp", "OPEN_BRACKET", "OPEN_BRACE", "dictorsetmaker", "REVERSE_QUOTE", "testlist", "ELLIPSIS", "name",  "PRINT", "EXEC", "MINUS", "number", "NONE", "STRING"]

class Testlist_comp(AliasNode):
    _fields_spec = ["test", "comp_for", "star_expr", "COMMA"]
    
class Expr_stmt(AliasNode):
    _fields_spec = ["testlist_star_expr", "assign_part"]

class Assign_part(AliasNode):
    _fields_spec = [ "ASSIGN", "testlist_star_expr", "yield_exp", "COLON", "test" ,"testlist", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN",
         "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN",  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN"]   

class Testlist_star_expr(AliasNode):
    _fields_spec = ["test", "star_expr", "testlist"]

class If_stmt(AliasNode):
    _fields_spec = ["test", "suite", "elif_clause",  "else_clause"]

class From_stmt(AliasNode):
    _fields_spec = ["DOT", "ELLIPSIS", "dotted_name", "STAR","import_as_names" ]

class Import_as_names(AliasNode):
    _fields_spec = ["import_as_name"]

class Import_as_name(AliasNode):
    _fields_spec = ["name", "AS"]

class For_stmt(AliasNode):
    _fields_spec = [ "ASYNC", "exprlist", "testlist", "suite", "else_clause"]  

class While_stmt(AliasNode):
    _fields_spec = ["test", "suite", "else_clause"]

class Class_or_func_def_stmt(AliasNode):
    _fields_spec = ["decorator", "classdef",  "funcdef"]

    
    
class Transformer(BaseNodeTransformer):
    def visit_Root(self, node):
        return Root.from_spec(node)
    def visit_File_input(self, node):
        return File_input.from_spec(node)
    def visit_Funcdef(self, node):
        return Funcdef.from_spec(node)
    def visit_Typedargslist(self, node):
        return Typedargslist.from_spec(node)
    def visit_Def_parameters(self, node):
        return Def_parameters.from_spec(node)   
    def visit_Def_parameter(self, node):
        return Def_parameter.from_spec(node) 
    def visit_Named_parameter(self, node):
        return Named_parameter.from_spec(node)  
    def visit_Simple_stmt(self, node):
        return Simple_stmt.from_spec(node)    
    def visit_Import_stmt(self, node):
        return Import_stmt.from_spec(node)    
    def visit_Stmt(self, node):
        return Stmt.from_spec(node)  
    def visit_Suite(self, node):
        return Suite.from_spec(node)   
    def visit_Return_stmt(self, node):
        return Return_stmt.from_spec(node)  
    def visit_Test(self, node):
        return Test.from_spec(node)  
    def visit_Testlist(self, node):
        return Testlist.from_spec(node)  
    def visit_Logical_test(self, node):
        return Logical_test.from_spec(node)  
    def visit_Comparison(self, node):
        return Comparison.from_spec(node)  
    def visit_Expr(self, node):
        return Expr.from_spec(node)
    def visit_Trailer(self, node):
        return Trailer.from_spec(node)
    def visit_Arguments(self, node):
        return Arguments.from_spec(node)
    def visit_Arglist(self, node):
        return Arglist.from_spec(node)
    def visit_Subscriptlist(self, node):
        return Subscriptlist.from_spec(node)
    def visit_Argument(self, node):
        return Argument.from_spec(node)
    def visit_Subscript(self, node):
        return Subscript.from_spec(node)
    def visit_Atom(self, node):
        return Atom.from_spec(node)
    def visit_Expr_stmt(self, node):
        return Expr_stmt.from_spec(node)
    def visit_Assign_part(self, node):
        return Assign_part.from_spec(node)
    def visit_Testlist_star_expr(self, node):
        return Testlist_star_expr.from_spec(node)
    def visit_If_stmt(self, node):
        return If_stmt.from_spec(node)
    def visit_From_stmt(self, node):
        return From_stmt.from_spec(node)
    def visit_Import_as_names(self, node):
        return Import_as_names.from_spec(node)
    def visit_Import_as_name(self, node):
        return Import_as_name.from_spec(node)
    def visit_For_stmt(self, node):
        return For_stmt.from_spec(node)
    def visit_While_stmt(self, node):
        return While_stmt.from_spec(node)
    def visit_Class_or_func_def_stmt(self, node):
        return Class_or_func_def_stmt.from_spec(node)
    def visit_Testlist_comp(self, node):
        return Testlist_comp.from_spec(node)
                

class AstTransformer():
    def __init__(self, tree, code :str = None ,comments: str=None, env=None):
        self.tree = tree
        self.lines = [''] + code.split('\n')
        self.base = 0
        self.code=code
        self.type_env = Env(dict(list(TYPED_API.items())), None)
        self.comments = comments
        self.q=None
        
        
    def transformer(self):
        self.base = 0
        self.body = []
        self._attr_index = {}
        self.arguments = []
        self.returnValue = []
        self.declarations = []
        self.definitions = []
        self._definition_index = {'functions': {}}
        self._hierarchy = {}
        self._imports = []
        self._fromimport = {}
        self._tuple_used = []
        self._tuple_assigned = []
        self.function_name = 'top level'
        self.iterators = []
        self.type_env['functions'] = {}
        self.visit_top_level(self.tree)
        self.main = []
        self.forSequence = False
        self.struct={}
        self.units={}
        self.isattr = False
        self.signature = self.visit_definitions()
        body = self.visit(self.tree)
        self.type_env.top['__name__'] = "str"
        self.q=None
        #'definition':self.signature,
        #print(self.type_env.values)
        return {'type': 'module', 'iterators':self.iterators, 'body': body if isinstance(body, list) else [body]}
    
    def visit_definitions(self):
        definitions = []
        for definition in self.definitions:
            if definition[0] == 'function':
                definitions.append(
                    self._definition_index['functions'][definition[1]])
            else:
                print("error")  # do Assert
        return definitions

    def visit_top_level(self, nodes):
        for node_r in nodes.children:
            if node_r.__class__.__name__ == "File_input":
                for node_s in node_r.children:
                    if node_s.__class__.__name__ == "Stmt":
                        for node_c in node_s.children:
                            if node_c.__class__.__name__=='Class_or_func_def_stmt':
                                for node_f in node_c.children:
                                    if node_f.__class__.__name__ == "Funcdef":
                                        self.definitions.append(('function', str(node_f.name.NAME)))
                                        self._definition_index['functions'][str(node_f.name.NAME)] = node_f
                                        self.type_env.top['functions'][str(node_f.name.NAME)] = [
                                            'Function'] + ([None] * len(node_f.typedargslist.def_parameters)) + [None]
                                        self.type_env.top[str(node_f.name.NAME)] = self.type_env.top['functions'][str(node_f.name.NAME)]
    

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
        if isinstance(node, AST):
            x = node.get_position()
            fields = {field: getattr(node, field)
                    for field in node._fields  }# get_field_names(node)
            if "self" in fields:
                fields.pop("self")
            #l = getattr(node, 'position', None)
            fields["node"] = node       
            comment = []       
            if x:
                fields['location'] = x["line_start"],x["column_start"]
                while self.comments and x["line_start"] >= list(self.comments.keys())[0]:
                    comment.append(list(self.comments.values())[0])
                    self.comments.popitem(0)
                fields['comments'] = comment
            else:
                fields['location'] = None
                fields["comments"] = None
                
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
    
    def visit_root(self, node,single_input, file_input, eval_input,comments, location):
        if single_input: return self.visit(single_input)
        if file_input: return self.visit(file_input)
        if eval_input: return self.visit(eval_input)
    
    def visit_file_input(self, node, stmt,comments, location):
        self.doc = ""
        r = self.visit(stmt)
        return {"type":"module", "body":r}
    
    def visit_class_or_func_def_stmt(self, node, decorator, classdef, funcdef,comments, location):
        r = self.visit(classdef) if classdef else self.visit(funcdef)
        if not decorator: return r
    
    def visit_funcdef(self, node,name, typedargslist, test, suite,comments, location):
        self.doc = ""
        self.recursive = False
        self.function_name = self.visit(name)
        arg_nodes = self.visit(typedargslist)
        env = {a["name"]: a["pseudo_type"] for a in arg_nodes}
        self.type_env, old_type_env = self.type_env.top.child_env(
            env), self.type_env
        
        domain_func = list(env.values())
        self.type_env.top["functions"][self.function_name][1:-1] = domain_func
        children = self.visit(suite)
        self.type_env = old_type_env
        r_type = self.type_env.top["functions"][self.function_name][-1]
        if test: return_type = self.visit(test)
        q = {
            'type':   "function_definition",
            'name':   self.function_name,
            'params': arg_nodes,
            'pseudo_type': self.type_env.top["functions"][self.function_name],
            'return_type': r_type,
            'block': children,
            'recursive':self.recursive,
            'doc':self.doc
        }
        self.recursive = False
        return q

    def visit_typedargslist(self, node, def_parameters,args, kwargs,comments, location):
        
        params = self.visit(def_parameters)
        
        return params
    
    def visit_def_parameters(self, node,def_parameter, comments, location ):
        res = []
        if isinstance(def_parameter, list):
            for arg in def_parameter:
                res.append(self.visit(arg))
            return res
        else: return self.visit(def_parameter)
        
    

    def visit_def_parameter(self, node,named_parameter, test, STAR, comments, location ):
        default_value = None
        res = self.visit(named_parameter)
        if test: 
            default_value = self.visit(test)
            res["value"] = default_value
        return res
    
    def visit_named_parameter(self, node, name, test, comments, location):
        name = self.visit(name)
        type_ = self.visit(test)
        if isinstance(type_, dict):
            type_ = self._translate_type(type_)
        r = {"type":"local", "name":name, "pseudo_type":type_}
        self.type_env.top[name] = type_
        return r

    def _translate_type(self, type_):
        r = []
        if "sequence" in type_: r.append(maptype_[type_["sequence"]])
        if "value" in type_: 
            if '[' in type_["value"].decode('utf-8'):
                ty1 = type_["value"].decode('utf-8').split("[")[0].replace("'", "").lower()
                ty2 = type_["value"].decode('utf-8').split("[")[1].split("]")[0].replace("'", "").lower()
                r.append(ty1)
                r.append(ty2)
            else: return type_["value"].decode('utf-8')
        if "index" in type_:
            if isinstance(type_["index"], dict):
                tt = self._translate_type(type_["index"] )
                r.append(tt)
            else:
                if isinstance(type_["index"], str):
                    r.append(type_["index"])
                else:           
                    for t in type_["index"]:
                        if isinstance(t, dict) and t["type"] == "index":
                            tt = self._translate_type(t )
                            r.append(tt)
                        else:
                            r.append(t)
        return r

    def visit_terminal(self, node, value, comments, location):
        return self.visit(value)
    
    def visit_simple_stmt(self, node, small_stmt, comments, location):
        return self.visit(small_stmt)
    
    def visit_import_stmt(self, node, dotted_as_names,comments, location):
        r = self.visit(dotted_as_names)
        module_name = r
        self._imports.extend(module_name)
        for a in module_name:
            self.type_env.top['_%s' %
                                a], self.type_env.top[a] = self.type_env.top[a], 'library'
        return {"type": "import",
                    "module": module_name,
                    }
    
    def visit_suite(self, node, simple_stmt, stmt,comments, location):
        if simple_stmt: return self.visit(simple_stmt)
        else: return self.visit(stmt)
    
    def visit_stmt(self, node, simple_stmt, compound_stmt, comments, location):
        if  simple_stmt: return self.visit(simple_stmt)
        else: return self.visit(compound_stmt)
    
    def visit_return_stmt(self, node, testlist, comments, location):
        value_node = self.visit(testlist) if testlist else None
        if isinstance(value_node, list) and len(value_node)>1:
            value_node = {"type":"tuple", "elements":value_node, "pseudo_type":['tuple']+[t["pseudo_type"] for t in value_node]}
        whiplash = self.type_env.top["functions"][self.function_name]
        if value_node is None:
            raise type_check_error("expected a non-void return type for %s" %
                                   self.function_name, location, self.lines[location[0]], wrong_type='Void')
        elif whiplash[-1] and whiplash[-1] != value_node['pseudo_type']:
            raise type_check_error(
                "expected %s return type for %s" % (serialize_type(whiplash[-1]), self.function_name), location, self.lines[location[0]], wrong_type=value_node['pseudo_type'])
        elif whiplash[-1] is None:
            whiplash[-1] = value_node['pseudo_type']
        s = {
            'type': 'implicit_return',
            'value': value_node,
            'pseudo_type': value_node['pseudo_type']
        }
        self.returnValue.append(s)
        return s

    def visit_testlist(self, node, test, comments, location):
        r = self.visit(test)
        res = r if len(r)>1 else r[0]
        return res

    
    def visit_test(self, node, logical_test, IF,  test, varargslist, comments, location):
        lt = self.visit(logical_test)
        if IF: 
            false_val = self.visit(test)
            a = self._compatible_types(
                lt[0]["pseudo_type"], false_val["pseudo_type"], "can't change the type of variable")
            return {
                'type': 'cond_expr_node',
                'test': lt[1],
                'true_val': lt[0],
                'pseudo_type': a,
                'false_val': false_val
            }
        r =  lt[0] if len(lt)==1 else lt
        return r
        
    
    def visit_logical_test(self, node, comparison, NOT, logical_test,AND,OR, comments, location):
        if comparison: 
            r =  self.visit(comparison)
            return r
        elif AND or OR:
            if AND: op = AND
            elif OR: op = OR
            op = self.visit(op)
            r = self.visit(logical_test)
            right_node = r[1]
            left_node = r[0]
            result = {
                'type': 'comparison',
                'op':   op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': "bool"
            }
            return result
        elif NOT:
            r = self.visit(logical_test)
            node = r[0]
            return {
                'type': 'unary_op',
                        'operator': 'not',
                        'value': node,
                        'pseudo_type': node['pseudo_type']
            }
            
    
    def visit_comparison(self, node, comparison, LESS_THAN, GREATER_THAN, EQUALS, GT_EQ, LT_EQ,  NOT_EQ_1,  NOT_EQ_2, NOT, IN , IS, expr, comments, location):
        if expr:
            result = self.visit(expr)
        else:
            r = self.visit(comparison)
            if LESS_THAN or GREATER_THAN or EQUALS or GT_EQ or LT_EQ or NOT_EQ_1 or NOT_EQ_2:
                if LESS_THAN: op = LESS_THAN
                elif GREATER_THAN: op = GREATER_THAN
                elif EQUALS: op = EQUALS
                elif GT_EQ: op = GT_EQ
                elif LT_EQ: op = LT_EQ
                elif NOT_EQ_1: op = NOT_EQ_1  
                elif NOT_EQ_2: op = NOT_EQ_2
                op = self.visit(op)

                right_node = r[1]
                left_node = r[0]

                self._confirm_comparable(op, left_node['pseudo_type'], right_node['pseudo_type'], location)
                result = {
                'type': 'comparison',
                'op':   op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': 'bool'
                }
            else:
                if IN and not NOT:
                    sequence_node = r[1]
                    element_node = r[0]
                    result = {
                        'type': 'standard_method_call',
                        'receiver': sequence_node,
                        'message': 'contains?',
                        'args': [element_node],
                        'pseudo_type': 'Boolean'
                    }
                elif IN and NOT:
                    sequence_node = r[1]
                    element_node = r[0]
                    result = {
                        'type': 'standard_method_call',
                        'receiver': sequence_node,
                        'message': 'not contains?',
                        'args': [element_node],
                        'pseudo_type': 'Boolean'
                    } 
        return result

    def _confirm_comparable(self, o, l, r, location):
        if o == '==' and l != r or o != '==' and (isinstance(l, list) or isinstance(r, list) or
                                                  l != r or l not in COMPARABLE_TYPES):
            raise type_check_error(
                '%s not comparable with %s' % (
                    serialize_type(l), serialize_type(r)),
                location, self.lines[location[0]],
                suggestions='comparable types in pseudo-cython: %s' % ' '.join(COMPARABLE_TYPES))
            
    
    def visit_expr(self, node, AWAIT,expr,  atom, trailer,POWER,ADD,MINUS,NOT_OP,STAR,DIV,MOD,IDIV, AT,LEFT_SHIFT,RIGHT_SHIFT,AND_OP,XOR,OR_OP, comments, location):
        if atom:
            r = self.visit(atom)
            if not trailer:
                return r
            t = self.visit(trailer)
            fname = r["name"] if isinstance(r, dict) else r
            m = t[0]
            if "type" in m and m["type"] == "sliceindex":
                m["receiver"]= r
                m["pseudo_type"] = r["pseudo_type"] 
                return m
            if "args" in t[0]:
                args = t[0]["args"]
                if fname in BUILTIN_FUNCTIONS:
                    if fname in ['any', 'all', 'sum', 'mean', 'count']:
                        if len(args) != 1:
                            raise translation_error('%s expected 1 arg, not %d' % (fname, len(args)),
                                            location, self.lines[location[0]])
                        else:
                            arg_node = args[0]
                            if fname not in ['sum',"mean","count"]:
                                if arg_node['pseudo_type'] != ['list', 'bool']:
                                    raise type_check_error('%s expected list[bool]' % fname,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=arg_node['pseudo_type'])
                                message = fname
                                return {
                                    'type': 'standard_method_call',
                                    'receiver': arg_node,
                                    'message': message,
                                    'args': [],
                                    'pseudo_type': "bool"
                                }
                            else:
                                if arg_node['pseudo_type'] not in[ ['list', 'int'] , ['list', 'float'],['array', 'int'] , ['array', 'float'],"unknown"]:
                                    raise type_check_error('%s expected list[int] / list[float]' % fname,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=arg_node['pseudo_type'])
                                message = r
                                _type = arg_node['pseudo_type'][1] if message !="count" else "int"
                                return {
                                    'type': 'standard_method_call',
                                    'receiver': arg_node,
                                    'message': message,
                                    'args': [],
                                    'pseudo_type': _type
                                }
                    else:
                        return self._translate_builtin_call('global', fname, args, location, attrib=0)
                
                elif isinstance(fname, str) and not("type" in t[0] and t[0]["type"]=="attribute"):
                    if not self._fromimport and fname not in list(self.type_env.top['functions'].keys()):
                        print("errr")
                    c = self.type_env.top['functions']
                    message = fname
                    param_types = [param['pseudo_type'] for param in args]
                    if message in c:
                        if len(c[message]) == 2 or len(c[message]) > 2 and c[message][1]:
                            g = self.type_env.top.values.get("functions", {}).get(message)[1:]
                            q = self._type_check(g,message, param_types)[-1]
                            x = [f for f in self.signature if f.name.NAME == message]
                            if q is None: 
                                self.accessReturn(x[0])
                                q = self.q["pseudo_type"]
                        else:
                            x = [f for f in self.signature if f.name.NAME == message]
                            argx = [a["pseudo_type"] for a in self.visit(x[0].typedargslist)]
                            #self._definition_index["functions"][message] = self.visit(x[0])
                            q = c[message][-1]
                            if argx != param_types:
                                raise PseudoCythonTypeCheckError("Types incompatibility at line %s"%location[0])
                            #q = self._type_check(argx+returnx,message, param_types)[-1]
                        if message == self.function_name: self.recursive = True                                
                        return {
                            "type": "custom_call",
                            "args": args,
                            "function": message,
                            "pseudo_type": q,
                            "recursive": True}
                    else:
                        arg_nodes = args
                        meth = [d for m in list(self._fromimport.values()) if m for d in m] 
                        if r in ["range", "enumerate"]:
                            return {
                                "type": "custom_call",
                                "args": args,
                                "function": message,
                                "pseudo_type": "unknown"}     
                        if r not in meth:
                            print("err", fname)
                        else:
                            if self.retrieve_library(fname) not in self._imports:
                                self._imports.append(
                                    self.retrieve_library(fname))
                            return self._translate_builtin_call(self.retrieve_library(fname), fname, arg_nodes, location, attrib=0)
                        
                elif "type" in t[0] and t[0]["type"]=="attribute": # [2].append
                    value_node = r
                    function = t[0]["name"]
                    if value_node['pseudo_type'] == 'library':  # math.log
                        return self._translate_builtin_call(value_node['name'], function, args, location, attrib=1)  
                    elif self._general_type(value_node['pseudo_type']) in PSEUDON_BUILTIN_TYPES:
                        r =  self._translate_builtin_method_call(self._general_type(value_node['pseudo_type']), value_node, function, args, location)
                        return r
                    else:
                        print('TODO method_call')
 
            else:
                return {"type":"index", 
                        "sequence":r, 
                        "index":t[0], 
                        "pseudo_type":r["pseudo_type"][-1]}
        else:
            r = self.visit(expr)
            if len(r)>1:                
                if STAR or DIV or MINUS or ADD:
                    if STAR: op = self.visit(STAR)
                    elif DIV: op =  self.visit(DIV)
                    elif MOD: op =  self.visit(MOD)
                    elif MINUS: op = self.visit(MINUS)
                    elif ADD: op = self.visit(ADD)
                    left_node = r[0]
                    right_node = r[1]
                    binop_type = TYPED_API['operators'][op](
                        left_node['pseudo_type'], right_node['pseudo_type'])[-1]
                    return {'type': 'binary_op',
                            'op': op,
                            'left': left_node,
                            'right': right_node,
                            'pseudo_type': binop_type
                            }
                elif POWER:
                    r = self.visit(expr)
                    op = self.visit(POWER)
                    left_node = r[0]
                    right_node = r[1]
                    binop_type = TYPED_API['operators'][op](
                    left_node['pseudo_type'], right_node['pseudo_type'])[-1]
                    return {
                    'type': 'standard_call',
                            'namespace': 'system',
                            'args': [left_node, right_node],
                            'pseudo_type': binop_type,
                            'function': 'pow'
                }
                elif NOT_OP:
                    value =  self.visit(expr)
                    pseudo_type_  = value['pseudo_type']
                    return {
                    'type': 'unary_op',
                            'operator': 'not',
                            'value': value,
                            'pseudo_type': pseudo_type_
                }
                elif MOD:
                    r = self.visit(expr)
                    op = self.visit(MOD)
                    left_node = r[0]
                    right_node = r[1]
                    binop_type = TYPED_API['operators'][op](
                    left_node['pseudo_type'], right_node['pseudo_type'])[-1]

                    return {
                        'type': 'standard_call',
                                'namespace': 'system',
                                'args': [left_node, right_node],
                                'pseudo_type': binop_type,
                                'function': 'modulo'
                    }
            else:
                if ADD or MINUS or NOT_OP:
                        if ADD: op = ADD
                        elif MINUS: op = MINUS
                        elif NOT_OP: op = NOT_OP

                        res = {
                            'type': 'unary_op',
                                    'operator': self.visit(op),
                                    'value': r[0],
                                    'pseudo_type': r[0]['pseudo_type']
                        }
                        return res

    def _type_check(self, g,message, types):
        if not g:
            raise PseudoCythonTypeCheckError("%s is not defined" % message)

        return self._real_type_check(g, types, '%s#%s' % ("function", message))

    def _real_type_check(self, g, types, name):
        if len(g) - 1 != len(types):
            raise PseudoCythonTypeCheckError("%s expected %d args" % (name, len(g) - 1))

        for j, (a, b) in enumerate(zip(g[0:-1], types)):
            general = self._compatible_types(b, a, "can't convert %s %dth arg" % (name, j))

        return g

    def _compatible_types(self, from_, to, err, silent=False):
        '''if from_[0] == "array":
            from_[0] = "list"'''
        if from_ == "unknown" or to == "unknown":
            return to
        if isinstance(from_, str):
            if not isinstance(to, str):
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))

            elif from_ == to:
                return to

            elif from_ in self._hierarchy:
                if to in self._hierarchy:
                    if to in self._hierarchy[from_][1]:
                        return from_

                    base = to
                    while base:
                        if from_ in self._hierarchy[base][1]:
                            return base
                        base = self._hierarchy[base][0]
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            elif from_ == 'int' and to == 'float':
                raise PseudoCythonTypeCheckError(
                    err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            elif silent:
                return False
            else:
                raise PseudoCythonTypeCheckError(
                    err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
        else:
            if not isinstance(to, list) or len(from_) != len(to) or from_[0] != to[0] or from_[1] != to[1] :
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            for f, t in zip(from_[1:-1], to[1:-1]):
                self._compatible_types(f, t, err)
            return to



    def _translate_attribute(self, obj, node, location):
        value_node = obj

        if self.struct and value_node["pseudo_type"] in self.struct.keys():
            attr_name = node["name"]
            return  {'type': 'attr',
                    'object': value_node,
                    'name': node["name"],
                    'pseudo_type': self.type_env[attr_name]}

        if isinstance(value_node["pseudo_type"], list) and value_node["pseudo_type"][0]=="enum":         
            return  {'type': 'attr',
                    'object': value_node,
                    'name': node["name"],
                    'pseudo_type': value_node["pseudo_type"][1]}
   
        if not isinstance(value_node['pseudo_type'], str):
            raise type_check_error(
                "you can't access attr of %s, only of normal objects or modules" % serialize_type(value_node['pseudo_type']),
                (location[0], location[1]), self.lines[location[0]],
                suggestions='[2].s is invalid',
                right='h = H()\nh.y',
                wrong='h = (2, H())\nh.hm')

        if value_node['pseudo_type'] == 'library':
            if value_node['name'] == 'sys' and node["name"] == 'argv':
                return {
                    'type': 'standard_call',
                    'namespace': 'system',
                    'function': 'args',
                    'args': [],
                    'pseudo_type': ['List', 'String'],
                    'special': None
                }
            else:
                return {
                    'type': 'library_function',
                    'library': value_node['name'],
                    'function': node["name"],
                    'pseudo_type': 'library'
                }
        else:
            value_general_type = self._general_type(value_node['pseudo_type'])
            attr_type = self._attr_index.get(value_general_type, {}).get(node["name"])
            if attr_type is None:
                m = METHOD_API.get(value_general_type, {}).get(node.attribute)
                if m:
                    attr_type = m.expand()["pseudo_type"] #'builtin_method[%s]' % serialize_type(m)
                else:
                    m = self.type_env.top.values.get(value_general_type, {}).get(node.attribute)
                    if m:
                        attr_type = m #'user_method[%s]' % serialize_type(m)

                if not m:
                    value_type = value_node['pseudo_type']
                    value_general_type = self._general_type(value_type)
                    show_type = serialize_type(TYPED_API.get('_generic_%s' % value_general_type, value_type))
                    raise translation_error(
                        "CyML can\'t infer the type of %s#%s"  % (serialize_type(value_type), node.attribute),
                        location, self.lines[location[0]],
                        suggestions='CyML knows about those %s methods:\n%s' % (
                            show_type,
                            prepare_table(self.type_env.top[value_general_type], ORIGINAL_METHODS.get(value_general_type))))

            else:
                attr_type = attr_type[0]['pseudo_type']

            if value_node['type'] == 'this':
                result = {
                    'type': 'instance_variable',
                    'name': node.attribute,
                    'pseudo_type': attr_type
                }
                if result in self._tuple_assigned:
                    if not any(a[0] == '_old_self_%s' % node.attribute for a in self._tuple_used):
                        self._tuple_used.append(('_old_self_%s' % node.attribute, result))


                    result = {'type': 'local', 'name': '_old_self_%s' % node.attribute, 'pseudo_type': attr_type}
                return result
            else:
                result = {
                    'type': 'attr',
                    'object': value_node,
                    'attr': node.attribute,
                    'pseudo_type': attr_type
                }
                if result in self._tuple_assigned:
                    if not any(a[0] == '_old_%s' % node.attribute for a in self._tuple_used):
                        self._tuple_used.append(('_old_%s' % node.attribute, result))
                    result = {'type': 'local', 'name': '_old_%s' % node.attribute, 'pseudo_type': attr_type}
                return result





    def accessReturn(self, node):
        if isinstance(node, list) and node:
            for n in node:
                if n.__class__.__name__== "Return_stmt":
                    self.q = self.visit_return_stmt(n, n.testlist,None,  n.position)
                    break
                self.accessReturn(n)
        else:
            if "_fields" in dir(node):
                fields = [getattr(node, field) for field in node._fields]
                fields_=[i for i in fields if i]
                node = fields_
                self.accessReturn(node)          
        
                
                
    
    def retrieve_library(self, func):
        for lib, meth in self._fromimport.items():
            if meth:
                for m in meth:
                    if m == func:
                        return lib
                        break
        return
        

    def _translate_builtin_method_call(self, class_type, base, message, args, location):
        if class_type not in METHOD_API:
            raise translation_error(
                "pseudo-cython doesn't support %s" % class_type,
                location, self.lines[location[0]],
                suggestions='pseudo-cython support those builtin classes:\n%s' % ' '.join(
                    PSEUDON_BUILTIN_TYPES[k] for k in METHOD_API.keys()))
        api = METHOD_API.get(class_type, {}).get(message)
        if not api:
            raise translation_error(
                "pseudo-cython doesn\'t support %s#%s" % (
                    serialize_type(class_type), message),
                location, self.lines[location[0]],
                suggestions='pseudo-cython supports those %s methods:\n%s' % (
                    PSEUDON_BUILTIN_TYPES[class_type],
                    prepare_table(TYPED_API[class_type], ORIGINAL_METHODS.get(class_type)).strip()))
        if isinstance(api, Standard):
            if base["pseudo_type"] =="list":
                self.type_env.top[base["name"]] = [
                    "list", args[0]["pseudo_type"]]
            return api.expand([base] + args)
        else:
            for count, b in api.items():
                if len(args) == count:
                    return b.expand([base] + args)
            raise translation_error(
                'pseudo-cython doesn\'t support %s%s with %d args' % (
                    serialize_type(class_type), message, len(args)),
                location, self.lines[location[0]])

    def _translate_builtin_call(self, namespace, function, args, location, attrib):
        if namespace != 'global' and namespace not in self._imports:
            raise type_check_error(
                'module %s not imported: impossible to use %s' % (
                    namespace, function),
                location, self.lines[location[0]],
                suggestions='a tip: pseudo-cython currently supports only import, no import as or from..import')
        if namespace not in FUNCTION_API and namespace not in self._imports:
            raise translation_error(
                "pseudo-cython doesn't support %s" % namespace,
                location, self.lines[location[0]],
                suggestions='pseudo-cython supports methods from\n  %s' % ' '.join(
                    k for k in FUNCTION_API if k != 'global'))
        if namespace in FUNCTION_API:
            api = FUNCTION_API[namespace].get(function)
            if not api:
                raise translation_error('pseudo-cython doesn\' t support %s %s' % (namespace, function),
                                        location, self.lines[location[0]],
                                        suggestions='pseudo-cython supports those %s functions\n  %s' % (
                    namespace,
                    prepare_table(TYPED_API[namespace], ORIGINAL_METHODS.get(namespace)).strip()))

            elif not isinstance(api, dict):
                z = api.expand(args)
                if attrib == 1:
                    z["attrib"] = 1
                return z
            else:
                for count, (a, b) in enumerate(list(api.items())):
                    if len(args) == a:
                        return b.expand(args)
                raise translation_error(
                    'pseudo-cython doesn\'t support %s%s with %d args' % (
                        namespace, function, len(args)),
                    location, self.lines[location[0]])
        if namespace in self._imports:
            return {
                'type': 'custom_call',
                'namespace': namespace,
                'args': self.visit_node(args),
                'pseudo_type': "unknown",
                'function': function
            }


    def _translate_builtin_call(self, namespace, function, args, location, attrib):
        if namespace != 'global' and namespace not in self._imports:
            raise type_check_error(
                'module %s not imported: impossible to use %s' % (
                    namespace, function),
                location, self.lines[location[0]],
                suggestions='a tip: pseudo-cython currently supports only import, no import as or from..import')
        if namespace not in FUNCTION_API and namespace not in self._imports:
            raise translation_error(
                "pseudo-cython doesn't support %s" % namespace,
                location, self.lines[location[0]],
                suggestions='pseudo-cython supports methods from\n  %s' % ' '.join(
                    k for k in FUNCTION_API if k != 'global'))
        if namespace in FUNCTION_API:
            api = FUNCTION_API[namespace].get(function)
            if not api:
                raise translation_error('pseudo-cython doesn\' t support %s %s' % (namespace, function),
                                        location, self.lines[location[0]],
                                        suggestions='pseudo-cython supports those %s functions\n  %s' % (
                    namespace,
                    prepare_table(TYPED_API[namespace], ORIGINAL_METHODS.get(namespace)).strip()))

            elif not isinstance(api, dict):
                z = api.expand(args)
                if attrib == 1:
                    z["attrib"] = 1
                return z
            else:
                for count, (a, b) in enumerate(list(api.items())):
                    if len(args) == a:
                        return b.expand(args)
                raise translation_error(
                    'pseudo-cython doesn\'t support %s%s with %d args' % (
                        namespace, function, len(args)),
                    location, self.lines[location[0]])
        if namespace in self._imports:
            return {
                'type': 'custom_call',
                'namespace': namespace,
                'args': self.visit(args),
                'pseudo_type': "unknown",
                'function': function
            }

            
    
    def visit_trailer(self, node, arguments, name, comments, location):
        args = self.visit(arguments)
        if name: 
            r = {"type":"attribute", "name": self.visit(name)}
            if arguments: 
                args.update(r)
                return args
            return r
        return args
    
    def visit_arguments(self, node, arglist, subscriptlist, comments, location):
        if arglist:
            return self.visit(arglist)
        elif subscriptlist:
            return self.visit(subscriptlist)
        else:
            print("tofo not arglist")

    
    def visit_arglist(self, node,argument, comments, location):   
        res = self.visit(argument)
        r = {}
        r["args"] = res
        return r


    def  visit_subscriptlist(self, node, subscript,comments,COMMA, location):
        r1 = self.visit(subscript)
        if not COMMA:
            return r1
        res = r1 if len(r1)>1 else r1[0]
        r = {}
        r['type'] = "index"
        r["index"] = res
        return r
        
        
        

    def visit_argument(self, node, test,comp_for, ASSIGN ,POWER, STAR,comments, location):
        arg = self.visit(test)
        if comp_for:
            pass
        elif ASSIGN:
            pass
        elif POWER:
            pass
        elif STAR:
            pass
        else:
            return arg

    def visit_subscript(self, node, ELLIPSIS, test, COLON, sliceop,comments, location):
        rt = []
        if ELLIPSIS:
            pass
        elif test:
            rt = self.visit(test)
            if len(node.children) == 1:
                return rt
            elif node.children[0]==COLON:
                if len(test)==1:
                    return  {'type': "sliceindex",
                            'message': "sliceindex_to",
                            'args': rt}
                elif sliceop:
                    print("todo sliceop [:c:c]")
                else: print("todo [:c]")
            else:
                if len(test)==1:
                    return  {'type': "sliceindex",
                            'message': "sliceindex_from",
                            'args': rt}
                elif len(test)==2:
                    if sliceop:
                        print("todo [c:c:c]")
                    else:
                        return  {'type': "sliceindex",
                                'message': "sliceindex",
                                'args': rt}
        else:
            print("yessss6")
            if sliceop:
                print("todo [::c]")
            else:
                rt = {'type': 'sliceindex', 'message': 'slice_', 'args': []}   
        return rt
    
    def visit_atom(self, node, OPEN_PAREN, yield_expr, testlist_comp, OPEN_BRACKET, OPEN_BRACE,dictorsetmaker, REVERSE_QUOTE, testlist, ELLIPSIS, name,  PRINT, EXEC, MINUS, number, NONE, STRING, comments, location):
        if OPEN_PAREN:
            if not yield_expr and not testlist_comp:
                print("ExprNodes.TupleNode(pos, args = [])")
            elif yield_expr:
                print("p_yield_expression(s)")
            elif testlist_comp:
                r = self.visit(testlist_comp)
                return r
        elif OPEN_BRACKET:
            if not testlist_comp:
                return {'type': 'list', 'elements': [], 'pseudo_type': ['list', None]}
            else:
                res = self.visit(testlist_comp)
                return {'type': 'list', 'elements': res, 'pseudo_type': ['list', res[0]["pseudo_type"]]}
        elif OPEN_BRACE:
            if not dictorsetmaker:
                return {'type': 'dict', 'pairs': [], 'pseudo_type': ['dict', None, None]}
            else:
                return self.visit(dictorsetmaker)
        elif testlist:
            return self.visit(testlist)
        elif ELLIPSIS:
            return self.visit(ELLIPSIS)
        elif name:
            rr = self.visit(name)
            if rr =="float": return "float"
            if rr == "int": return "int"
            if rr == "str": return "str"
            if rr == "datetime": return "datetime"
            if rr == "bool": return "bool"
            if rr == "True" or rr == "False": return {"type":"bool", "value":"%s"%rr, "pseudo_type":"bool"}
            id_type = self.type_env[rr]
            if id_type is not None:
                return {"type":"local", "name":rr, "pseudo_type":self.type_env[rr]}
            else: return rr
        elif PRINT:
            return "print"
        elif EXEC:
            return "exec"
        elif number: 
            r = self.visit(number)
            rtype = "int" if isinstance(eval(r), int) else "float"
            if not MINUS:
                return {"type":rtype,  "value":r, "pseudo_type":rtype}
            else:
                return {
                'type': 'unary_op',
                        'operator': '-',
                        'value':{'type':rtype,
                                'value':r,
                                "pseudo_type":rtype                        
                                },
                        'pseudo_type': rtype
                        }
        elif NONE:
            return "none"
        elif STRING:
            r = self.visit(STRING)
            return {"type":"str", "value":r[0].replace('"', "").encode('utf-8)'), "pseudo_type":"str" }
        else:
            print("I dont know", location)
        
    def visit_expr_stmt(self, node, testlist_star_expr,  assign_part, comments, location):
        target = self.visit(testlist_star_expr)
        if assign_part:
            value = self.visit(assign_part)
            if isinstance(value, dict) and "type" in value and value["type"] == 'declaration': 
                target = target["name"] if isinstance(target, dict) else target
                self.type_env.top[target] = value["decl"][0]["pseudo_type"]
                value["decl"][0]["name"] = target
                return value
            elif isinstance(value, list):
                r = {"type":"list", "elements":value["value"], "pseudo_type":value[0]["pseudo_type"]}
            else:
                r = value["value"]
                    
            #elif isinstance(value, dict) and value["type"] == 'attribute': 
                #value = 
                
            return {
                    'type': 'assignment',
                    'target': target,
                    'value': r,
                    'op':value["op"],
                    'pseudo_type': 'Void'
                } 
        else:
            r = self.visit(testlist_star_expr)
            if r["type"] == "str":
                self.doc += r["value"].decode("utf-8") + "\n"
            else:
                return {
                        "type": "ExprStatNode",
                        "expr": self.visit(testlist_star_expr)
            }
                
    
    def visit_assign_part(self, node, ASSIGN, testlist_star_expr, yield_exp, COLON, test ,testlist, ADD_ASSIGN, SUB_ASSIGN, MULT_ASSIGN, AT_ASSIGN, DIV_ASSIGN, MOD_ASSIGN,
         AND_ASSIGN, OR_ASSIGN, XOR_ASSIGN, LEFT_SHIFT_ASSIGN,  RIGHT_SHIFT_ASSIGN, POWER_ASSIGN, IDIV_ASSIGN,  comments, location):
        if ASSIGN and not COLON:
            r =  self.visit(testlist_star_expr)
            r = r if len(r)>1 else r[0]
            return {"op":"=", "value":r}
        elif COLON:
            decl = self.visit(test)
            if isinstance(decl, dict):
                pseudo_type = self._translate_type(decl)
                type_ = pseudo_type[0]
            else:
                pseudo_type = decl
                type_ = decl
            de = {"type":type_, "pseudo_type":pseudo_type}
            if ASSIGN:
                r = self.visit(testlist)
                de["value"] = r
            return {"type":"declaration", "decl":[de]}
        else:
            r = self.visit(testlist)
            if ADD_ASSIGN: return {"op":"+=", "value":r}
            if SUB_ASSIGN: return {"op":"-=", "value":r}
            if MULT_ASSIGN: return {"op":"*=", "value":r}
            if DIV_ASSIGN: return {"op":"/=", "value":r}
            if MOD_ASSIGN: return {"op":"%=", "value":r}

    
    def visit_testlist_star_expr(self, node, test, star_expr, testlist, comments, location):
        if star_expr:
            print("todo starred expression")
        elif test:
            r = self.visit(test)
        elif testlist:
            r = self.visit(testlist)
        if isinstance(r, list):
            res = {}
            res["type"] = "tuple"
            res["pseudo_type"] = ["tuple"]+[arg["pseudo_type"] for arg in r]
            res["elements"] = r
            return res
        return r
    
    def visit_if_stmt(self, node,test,suite, elif_clause, else_clause, comments, location):
        otherwise = []
        test_ = self.visit(test)
        elifclause = self.visit(elif_clause) if elif_clause else []
        elseclause = self.visit(else_clause) if else_clause else []
        if elifclause: otherwise.extend(elifclause)
        
        if elseclause:
            otherwise.append(elseclause)
        block = self.visit(suite)
        R = {
            'type': 'if_statement',
            'test': test_,
            'block': block,
            'pseudo_type': 'Void',
            'otherwise': otherwise
        }
        return R
    
    def visit_elif_clause(self, node, ELIF, test, COLON, suite, comments, location):
        block = self.visit(suite)
        return {
            'type': 'elseif_statement',
            'test': self.visit(test),
            'block': [block] if isinstance(block, dict) else block,
            'pseudo_type': 'Void'
        }
    
    def visit_else_clause(self, node,ELSE, COLON ,suite, comments, location):
        r = self.visit(suite)
        res = {
                    'type': 'else_statement',
                    'block': [r] if isinstance(r, dict) else r,
                    'pseudo_type': 'Void'
            }
        return res

    def visit_from_stmt(self, node, DOT, ELLIPSIS, dotted_name, STAR,import_as_names, comments, location):
        module = self.visit(dotted_name)
        imp = self.visit(import_as_names)
        if module == "math" and STAR:
            name_list = list(FUNCTION_API["math"].keys()) +list(CONSTANT_API["math"].keys())
        else:
            name_list = imp
        self._fromimport[module] = name_list
        return {"type": "importfrom",
                    "namespace": module,
                    "name": name_list
                }
    
    def visit_import_as_names(self, node, import_as_name, comments, location):
        return self.visit(import_as_name)
    
    def visit_import_as_name(self, node,name, AS, comments, location):
        if not AS:
            return self.visit(name)
    
    def visit_dotted_name(self, node, dotted_name,DOT, name, comments, location):
        name = self.visit(name)
        if not DOT:
            return name
        else:
            m = self.visit(dotted_name)
            return m + "." + name
    
    def visit_for_stmt(self, node,  ASYNC, exprlist, testlist, suite, else_clause, comments, location):
        expr_l = self.visit(exprlist)
        test_l = self.visit(testlist)
        block = self.visit(suite)
        if isinstance(test_l, dict) and test_l["type"]=="custom_call" and test_l["function"]=="range":
            range = test_l["args"]
            if len(range) == 1:
                start, end, step = {'type': 'int', 'value': "0", 'pseudo_type': 'int'},  range[0], {'type': 'int', 'value': "1", 'pseudo_type': 'int'}
            elif len(range) == 2:
                start, end, step = range[0], range[1], {'type': 'int', 'value': "1", 'pseudo_type': 'int'}
            else:
                start, end, step = range[0], range[1], range[2]
            for label, r in [('start', start), ('end', end), ('step', step)]:
                if r['pseudo_type'] != 'int':
                    raise PseudoCythonTypeCheckError(
                        'expected int for range %s index' % label)
            return {
                'type': 'for_range_statement',
                'start': start,
                'end': end,
                'step': step,
                'index': {
                    'type': 'local',
                    'pseudo_type': 'int',
                    'name': expr_l[0]["name"]
                },
                'block':block
            }  
        elif isinstance(test_l, dict) and test_l["type"]=="local" and test_l["pseudo_type"][0] in ["array", "list"]:
            return {
                'type': 'for_statement',
                'sequences': {'type': 'for_sequence', 'sequence': test_l},
                'iterators': {
                    'type': 'for_iterator',
                    'iterator': expr_l
                },
                "block": block
            }   
        
    def visit_while_stmt(self, node,test,  suite ,else_clause, comments, location):
        test_node = self.visit(test)
        return {
                'type': 'while_statement',
                'test': test_node,
                'block': self.visit(suite),
                'pseudo_type': 'Void'
            }   
    
    def visit_testlist_comp(self, node, test, comp_for, COMMA,star_expr, comments, location):
        if comp_for:
            print("comp_for not yet implemented")
        else:
            r =  self.visit(test) 
            return r
    
    



    def _general_type(self, t):
        if isinstance(t, list):
            return t[0]
        else:
            return t
        
                
            

maptype_ = {"Dict":"dict", "List":"list", "Array":"array"}