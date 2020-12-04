from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import PseudoCythonTypeCheckError, PseudoCythonNotTranslatableError, translation_error, type_check_error
from pycropml.transpiler.antlr_py.cs.builtin_typed_api import *
from pycropml.transpiler.antlr_py.cs.api_transform import *
from pycropml.transpiler.env import Env
from pycropml.transpiler.helpers import *
import ast
from ast import AST
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



class Compilation_unit(AliasNode):
    _fields_spec = ["using_directives", "namespace_member_declarations"]

class Namespace_member_declarations(AliasNode):
    _fields_spec = ["namespace_member_declaration"]

class Namespace_member_declaration(AliasNode):
    _fields_spec = ["namespace_declaration", "type_declaration"]

class Type_declaration(AliasNode):
     _fields_spec = ["attributes" ,"all_member_modifiers","class_definition"] 

class Class_body(AliasNode):
     _fields_spec = ["class_member_declarations"]     

class Namespace_or_type_name(AliasNode):
    _fields_spec = ["identifier", "type_argument_list", "qualified_alias_member"]

class Class_member_declarations(AliasNode):
    _fields_spec = ["class_member_declaration"]

class Type_(AliasNode):
    _fields_spec = ["base_type", "INTERR", "rank_specifier", "STAR"]

class Base_type(AliasNode):
    _fields_spec = ['simple_type','class_type']

class Simple_type(AliasNode):
    _fields_spec = ['numeric_type', "BOOL"]

class Class_type(AliasNode):
    _fields_spec = ['namespace_or_type_name', "OBJECT", "DYNAMIC", "STRING"]

class Numeric_type(AliasNode):
    _fields_spec = ['integral_type',"floating_point_type"]

class Typed_member_declaration(AliasNode):
    _fields_spec = ["type_","namespace_or_type_name","indexer_declaration","method_declaration","property_declaration", "operator_declaration","field_declaration","REF","READONLY"]                          

class Arg_declaration(AliasNode):
    _fields_spec = ["type_ ", "identifier", "expression"]

class DeclarationStatement(AliasNode):
    _fields_spec = ["local_variable_declaration","local_constant_declaration","local_function_declaration"]

class Local_variable_declaration(AliasNode):
    _fields_spec = ["local_variable_type", "local_variable_declarator"]

class Local_variable_declarator(AliasNode):
    _fields_spec = ["identifier","local_variable_initializer"]

class Local_variable_initializer(AliasNode):
    _fields_spec = ["expression","array_initializer","stackalloc_initializer"]

class Expression(AliasNode):
    _fields_spec = ["assignment","non_assignment_expression"]

class Relational_expression(AliasNode):
    _fields_spec = ["shift_expression", 'LT', 'GT', 'OP_LE','OP_GE','IS','isType',"AS","type_"]

class Shift_expression(AliasNode):
    _fields_spec = ["additive_expression","right_shift",'OP_LEFT_SHIFT']

class Additive_expression(AliasNode):
     _fields_spec = ["multiplicative_expression", "PLUS", "MINUS", ]

class Multiplicative_expression(AliasNode):
     _fields_spec = ["switch_expression", 'STAR', 'DIV','PERCENT']

class ExpressionStatement(AliasNode):
    _fields_spec = ["expression"]

class Assignment(AliasNode):
    _fields_spec = ["unary_expression", "assignment_operator","expression"]

class Unary_expression(AliasNode):
    _fields_spec = ["primary_expression", "unary_expression", "type_","PLUS", "MINUS","OP_INC","OP_DEC"]

class Non_assignment_expression(AliasNode):
    _fields_spec = ["lambda_expression", "query_expression","conditional_expression"]

class Conditional_expression(AliasNode):
    _fields_spec = ["null_coalescing_expression"]

class Conditional_and_expression(AliasNode):
    _fields_spec = ["inclusive_or_expression", "OP_AND"]

class Inclusive_or_expression(AliasNode):
      _fields_spec = ["exclusive_or_expression", "BITWISE_OR"]
  
class Exclusive_or_expression(AliasNode):
      _fields_spec = ["and_expression", "CARET"]

class And_expression(AliasNode):
      _fields_spec = ["equality_expression","AMP"]

class Equality_expression(AliasNode):
      _fields_spec = ["relational_expression", "OP_EQ","OP_NE"]

class Switch_expression(AliasNode):
      _fields_spec = ["range_expression", "switch_expression_arms", "SWITCH"]

class Range_expression(AliasNode):
      _fields_spec = ["unary_expression","OP_RANGE"]

class ReturnStatement(AliasNode):
      _fields_spec = ["expression"]

class Primary_expression(AliasNode):
    _fields_spec = ["primary_expression_start","OP_INC", "OP_DEC","member_access","method_invocation", "bracket_expression"]

class SimpleNameExpression(AliasNode):
    _fields_spec = ["identifier", "type_argument_list"]

class LiteralExpression(AliasNode):
    _fields_spec = ["literal"]

class Literal(AliasNode):
    _fields_spec = ["boolean_literal","string_literal","INTEGER_LITERAL","REAL_LITERAL","CHARACTER_LITERAL","NULL"]

class Type_argument_list(AliasNode):
    _fields_spec = ["type_"]

class ObjectCreationExpression(AliasNode):
    _fields_spec = [ "type_","expression_list","anonymous_object_initializer","rank_specifier","array_initializer","object_creation_expression","object_or_collection_initializer"]

class Object_creation_expression(AliasNode) :                                 
    _fields_spec = ["argument_list","object_or_collection_initializer"]

class Collection_initializer(AliasNode):
    _fields_spec = ["element_initializer"]

class Element_initializer(AliasNode):
    _fields_spec = ["non_assignment_expression","expression_list" ]

class Array_type(AliasNode):
    _fields_spec = ["base_type","rank_specifier"]

class IfStatement(AliasNode):
    _fields_spec = ["expression","if_body","ELSE","IF"]

class ForStatement(AliasNode):
    _fields_spec = ["for_initializer","expression","for_iterator","embedded_statement"]

class WhileStatement(AliasNode):
    _fields_spec = ["expression","embedded_statement"]

class Method_invocation(AliasNode):
    _fields_spec = ["argument_list"]

class Bracket_expression(AliasNode):
    _fields_spec = ["indexer_argument"]


class Transformer(BaseNodeTransformer):
    def visit_Compilation_unit(self, node):
        return Compilation_unit.from_spec(node)
    
    def visit_Namespace_member_declarations(self, node):
        return Namespace_member_declarations.from_spec(node)

    def visit_Namespace_member_declaration(self, node):
        return Namespace_member_declaration.from_spec(node)

    def visit_Class_member_declarations(self, node):
        return Class_member_declarations.from_spec(node)
    
    def visit_Class_body(self, node):
        return Class_body.from_spec(node)
    
    def visit_Method_invocation(self, node):
        return Method_invocation.from_spec(node)

    def visit_Namespace_or_type_name(self, node):
        return Namespace_or_type_name.from_spec(node)

    def visit_Type_(self, node):
        return Type_.from_spec(node)

    def visit_Base_type(self, node):
        return Base_type.from_spec(node)

    def visit_Class_type(self, node):
        return Class_type.from_spec(node)

    def visit_Simple_type(self, node):
        return Simple_type.from_spec(node)

    def visit_Numeric_type(self, node):
        return Numeric_type.from_spec(node)

    def visit_Array_type(self, node):
        return Array_type.from_spec(node)

    def visit_Typed_member_declaration(self, node):
        return Typed_member_declaration.from_spec(node)
    
    def visit_Arg_declaration(self, node):
        return Arg_declaration.from_spec(node)

    def visit_DeclarationStatement(self, node):
        return DeclarationStatement.from_spec(node)
    
    def visit_Local_variable_declaration(self, node):
        return Local_variable_declaration.from_spec(node)
    
    def visit_Local_variable_declarator(self, node):
        return Local_variable_declarator.from_spec(node)
    
    def visit_Local_variable_initializer(self,node):
        return Local_variable_initializer.from_spec(node)

    def visit_Expression(self,node):
        return Expression.from_spec(node)
    
    def visit_Relational_expression(self, node):
        return Relational_expression.from_spec(node)
    
    def visit_Shift_expression(self, node):
        return Shift_expression.from_spec(node)
    
    def visit_Additive_expression(self, node):
        return Additive_expression.from_spec(node)

    def visit_Multiplicative_expression(self, node):
        return Multiplicative_expression.from_spec(node)

    def visit_ExpressionStatement(self, node):
        return ExpressionStatement.from_spec(node)

    def visit_Assignment(self, node):
        return Assignment.from_spec(node)
    
    def visit_Non_assignment_expression(self, node):
        return Non_assignment_expression.from_spec(node)
    
    def visit_Conditional_expression(self, node):
        return Conditional_expression.from_spec(node)
    
    def visit_Conditional_and_expression(self,node):
        return Conditional_and_expression.from_spec(node)
    
    def visit_Inclusive_or_expression(self, node):
        return Inclusive_or_expression.from_spec(node)      

    def visit_Exclusive_or_expression(self, node):
        return Exclusive_or_expression.from_spec(node)          

    def visit_And_expression(self, node):
        return And_expression.from_spec(node)   

    def visit_Equality_expression(self, node):
        return Equality_expression.from_spec(node)   

    def visit_Unary_expression(self, node):
        return Unary_expression.from_spec(node) 

    def visit_Switch_expression(self, node):
        return Switch_expression.from_spec(node) 

    def visit_Range_expression(self, node):
        return Range_expression.from_spec(node)

    def visit_ReturnStatement(self, node):
        return ReturnStatement.from_spec(node) 

    def visit_Primary_expression(self, node):
        return Primary_expression.from_spec(node) 
    
    def visit_SimpleNameExpression(self, node):
        return SimpleNameExpression.from_spec(node)

    """def visit_Primary_expression_start(self, node):
        return Primary_expression_start.from_spec(node) """

    def visit_Literal(self, node):
        return Literal.from_spec(node) 
    
    def visit_Type_argument_list(self, node):
        return Type_argument_list.from_spec(node) 

    def visit_Object_creation_expression(self, node):
        return Object_creation_expression.from_spec(node)

    def visit_Collection_initializer(self, node):
         return Collection_initializer.from_spec(node)

    def visit_IfStatement(self, node):
         return IfStatement.from_spec(node)

    def visit_ForStatement(self, node):
         return ForStatement.from_spec(node)

    def visit_WhileStatement(self, node):
         return WhileStatement.from_spec(node)
        
    def visit_Bracket_expression(self, node):
        return Bracket_expression.from_spec(node)


    """def visit_Element_initializer(self, node):
        return Element_initializer.from_spec(node)"""

class AstTransformer():
    def __init__(self, tree):
        self.tree = tree
        self.base = 0
        self.type_env = Env(dict(list(TYPED_API.items())), None)

    def transformer(self):
        self.type_env['functions'] = {}
        self.function_name = 'top level'
        self.definitions = []
        body = self.visit(self.tree)
        return {'body': body if isinstance(body, list) else [body]}

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
        
    def visit_compilation_unit(self,node, using_directives, namespace_member_declarations, location):
        res, res2 = [], []
        if using_directives is None:
            u = []
        else:
            for n in using_directives:
                z = n.namespace_or_type_name.identifier
                res.append(z)
            for n in res:
                usin = [str(rs) for rs in n ]
                us = usin[0] if len(usin)==1 else ".".join(usin)
                res2.append(us)
            u = res2
        print("kk",len(namespace_member_declarations.children))
        z = self.visit(namespace_member_declarations)
        return {"type": "module",
                "using": u,
                "body": z}

    def visit_namespace_member_declarations(self,node, namespace_member_declaration, location):

        return self.visit(node.children)
    
    def visit_namespace_member_declaration(self,node, namespace_declaration, type_declaration, location):
        if type_declaration:
            return   self.visit(type_declaration)
        if namespace_declaration:
            return self.visit(namespace_declaration)
    
    

    def visit_type_declaration(self,node,class_definition,
                                struct_definition,
                                interface_definition,
                                enum_definition,
                                delegate_definition,
                                attributes,
                                all_member_modifiers,
                                location):
        if interface_definition:
            return self.visit(interface_definition)
        if enum_definition:
            return self.visit(enum_definition)    
        if struct_definition:
            return self.visit(struct_definition)    
        if delegate_definition:
            return self.visit(delegate_definition)  
        if class_definition:
            block = self.visit(class_definition.class_body)
            return{"type":"classDef",
                    "name": class_definition.identifier,
                    "base": class_definition.class_base,
                    "block": block }     
 
    def visit_class_body(self, node, class_member_declarations, location):

        z = self.getpath(node, "typed_member_declaration")

        for child in z:
            if child.method_declaration:
                name = self.visit(child.method_declaration.method_member_name)
                name  = name[0]
                rt = self.visit(child.type_)
                params = self.visit(child.method_declaration.formal_parameter_list)
                self.definitions.append(('function', name))
                if params:
                    self.type_env.top['functions'][name] = ['Function'] +[p["pseudo_type"] for p in params] + [rt["pseudo_type"]] 
                    self.type_env.top[name] = self.type_env.top['functions'][name]   
                else:
                    self.type_env.top['functions'][name] = ['Function'] +[None] + [rt["pseudo_type"]] 
                    self.type_env.top[name] = self.type_env.top['functions'][name]   

        
        return self.visit(class_member_declarations.children)

    def visit_class_member_declaration(self,
                                        node,
                                        common_member_declaration,
                                        destructor_definition,
                                        attributes,
                                        all_member_modifiers,
                                        location):
        z = self.visit(common_member_declaration)
        return z

    def visit_typed_member_declaration(self,
                                        node,
                                        type_,
                                        namespace_or_type_name,
                                        indexer_declaration,
                                        method_declaration,
                                        property_declaration,
                                        operator_declaration,
                                        field_declaration,
                                        REF,
                                        READONLY,
                                        location):
        if type_:
            typ = self.visit(type_)
        if namespace_or_type_name:
            res = {"type":"namespace", "block":self.visit(namespace_or_type_name)}
        if indexer_declaration:
            res = {"type":"indexer", "block":self.visit(indexer_declaration)}
        if method_declaration:
            self.function_name = self.visit(method_declaration.method_member_name)[0]
            res = {"type":"method",  
                    "name":self.function_name,
                    "return_type" :typ["pseudo_type"],
                    "params":self.visit(method_declaration.formal_parameter_list),
                    "block":self.visit(method_declaration.method_body)}
        if property_declaration:
            res = {"type":"property", "block":self.visit(property_declaration)}
        if operator_declaration:
            res = {"type":"operator", "block":self.visit(operator_declaration)}
        if field_declaration:
            res = {"type":"field", "block":self.visit(field_declaration)}   
        return res

    def visit_type_(self, 
                    node,INTERR,rank_specifier,STAR,
                    base_type,
                    location):
        if rank_specifier: 
            return self.visit_array_type(node,base_type,location)
        if base_type.simple_type:
            res = base_type.simple_type

        if base_type.class_type:
            res = base_type.class_type
            
        return self.visit(res)

    def visit_base_type(self, node,simple_type,class_type, location):
        if simple_type:
            res = simple_type
        if class_type:
            res = class_type
        return self.visit(res)

    def visit_array_type(self,node,base_type,location):
        z = self.visit(base_type)
        res = {}
        res["type"] = "array"
        res["pseudo_type"] = ["array",z["type"]]
        return res

    def  visit_namespace_or_type_name(self, node, identifier,type_argument_list,qualified_alias_member,location) :
        z ={}
        if identifier[0]=="List":
            z["type"]="list"
            z["pseudo_type"]=["list",self.visit(type_argument_list)[0]["pseudo_type"]]
        else:
            z["type"]= identifier[0]
            z["pseudo_type"] = identifier[0]
        return z

    def visit_objectcreationexpression(self, node,NEW,OPEN_BRACKET,expression_list,CLOSE_BRACKET,
                                    type_,
                                    anonymous_object_initializer,
                                    rank_specifier,
                                    array_initializer,
                                    object_creation_expression,
                                    object_or_collection_initializer,
                                    location):
        z = self.visit(type_)
        if object_creation_expression:
            z_oce = self.visit(object_creation_expression)
            return {"type":z["type"], "args": z_oce["args"], "init":z_oce["init"], "pseudo_type":z["pseudo_type"]}
        elif object_or_collection_initializer:
            z_oci = self.visit(object_or_collection_initializer)
            return {"type":z["type"], "init":z_oci["init"], "pseudo_type":z["pseudo_type"]}
        elif expression_list:
            dimLen = self.visit(expression_list)
            dim = len(dimLen)
            size = dimLen
            z["init"] = {"type":"initArray", "value": self.visit(array_initializer) if array_initializer else None}
            return {"type":z["type"], "dim": dim, "size":size, "init":z["init"], "pseudo_type":z["pseudo_type"]}
        elif rank_specifier:
            print("ok4")
        elif array_initializer : print("kkkkk")
        else: print("nn")

    def visit_array_initializer(self, node,variable_initializer, location):
        print('iiiiii')
        if len (node.children)==1:
            res = self.visit(variable_initializer)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            args = [arg[0] for arg in args if isinstance(arg, list)]
            return args

    def visit_object_creation_expression(self, node, argument_list,object_or_collection_initializer, location):
        z = {}
        if argument_list:  z["args"] = self.visit(argument_list)
        else:  z["args"]=[]
        if object_or_collection_initializer:
            x = self.visit(object_or_collection_initializer)
            z["init"] = x["init"]
        else: z["init"] = []
        return z

    def visit_argument_list(self, node, arguments,location):
        print("argument_list_TODO")

    def visit_collection_initializer(self, node,element_initializer, location):
        res={}
        if len (node.children)==1:
            ini = self.visit(element_initializer)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            ini = [arg[0] for arg in args if arg[0] not in ['{','}',","]]
        res["init"] = {"type":"initCollection", "value":ini}
        return res

    def visit_element_initializer(self, node, non_assignment_expression, expression_list, location):
        if non_assignment_expression: 
            return self.visit(non_assignment_expression)
        if expression_list:
            return self.visit(expression_list)

    def visit_simple_type(self, node,numeric_type,BOOL, location):
        if numeric_type:  return self.visit(numeric_type)
        if BOOL: return {"type":"bool", "pseudo_type":"bool"}

    def visit_class_type(self, node,namespace_or_type_name, OBJECT, DYNAMIC, STRING, location):
        if namespace_or_type_name:  
            return self.visit(namespace_or_type_name)
        if OBJECT: 
            return self.visit(OBJECT)
        if DYNAMIC: 
            return self.visit(DYNAMIC)
        if STRING: 
            return {"type":"str", "pseudo_type":"str"}

    def visit_type_argument_list(self, node,type_, location):
        return self.visit(type_)
    
    def visit_numeric_type(self, node,integral_type,floating_point_type, location):
        if integral_type:
            if integral_type=="int": return {"type":"int", "pseudo_type":"int"}
            elif integral_type=="char": return {"type":"char", "pseudo_type":"char"}
            else: print("TODO")
        if floating_point_type: 
            if floating_point_type=="float": return {"type":"float", "pseudo_type":"float"}
            elif floating_point_type=="double": return {"type":"double", "pseudo_type":"double"}
            else: print("TODO")

    def visit_arg_declaration(self,
                                node,
                                type_,
                                identifier,
                                expression,
                                location):
        z= {"type":"local","name":identifier, "pseudo_type":self.visit(type_)["pseudo_type"]}
        self.type_env[str(identifier)]=z["pseudo_type"]
        return z

    def visit_declarationstatement(self,
                                     node,
                                     local_variable_declaration,
                                     local_constant_declaration,
                                     local_function_declaration,
                                     location):
        if local_variable_declaration:
            return self.visit(local_variable_declaration)
        if local_constant_declaration: print("TODO")

    def visit_local_variable_declaration(self, 
                                        node,
                                        local_variable_type,
                                        local_variable_declarator,
                                        location):
        v = self.visit(local_variable_declarator)
        t = self.visit(local_variable_type)
        if (v[0]["value"] is not None):
            if (t["pseudo_type"]!=v[0]["value"]["pseudo_type"]) : 
                raise type_check_error('bad declaration at line %s and column %s'%(location[0],location[1]))
        z = {"type":"declaration", "decl": {"type": t["type"], "name":v[0]["name"], "value":v[0]["value"], "pseudo_type":t["pseudo_type"]}}
        if z["decl"]["value"] is None: del z["decl"]["value"]
        self.type_env[str(z["decl"]["name"])] = z["decl"]["pseudo_type"]
        return z

    def visit_local_variable_declarator(self, 
                                        node,
                                        identifier, 
                                        local_variable_initializer,
                                        location):
        name = identifier
        return {"name":name, "value":self.visit(local_variable_initializer)}

    def visit_local_variable_initializer(self,
                                        node,
                                        expression,
                                        array_initializer,
                                        stackalloc_initializer,
                                        location):
        
        if array_initializer: 
            z = self.visit(array_initializer)
            return {"type":"array", "value":z, "pseudo_type":["array","%s"%z[0]["pseudo_type"]]}
        if expression:
            return self.visit(expression)
    
    def visit_expression(self, node, assignment, non_assignment_expression, location):
        if non_assignment_expression:
            x = self.visit(non_assignment_expression)
            return  x[0]
        if assignment:
            return self.visit(assignment)
    
    def visit_assignment(self, node, unary_expression,assignment_operator,expression, location):

        if assignment_operator:
            z =  {
                    'type': 'assignment',
                    'target':self.visit(unary_expression),
                    'op':assignment_operator,
                    'value': self.visit(expression),
                    'pseudo_type': 'Void'
                }
            
            r = z["value"]["pseudo_type"]
            if "Function" in z["value"]["pseudo_type"]:
                r = z["value"]["pseudo_type"][-1]

            if z["target"]["pseudo_type"]!=r:
                raise type_check_error(
                ' Cannot implicitly convert type %s from %s to %s at line %s. An explicit conversion exists (are you missing a cast?)'%(z["target"]["name"],z["target"]["pseudo_type"], z["value"]["pseudo_type"], location[0]))
            return z
        
        else: return "TODO"

    def visit_non_assignment_expression(self, 
                                        node, 
                                        lambda_expression,
                                        query_expression,
                                        conditional_expression,
                                        location):
        if  lambda_expression: print("TODO lambda")  
        if  query_expression: print("TODO query")     
        return self.visit(conditional_expression)
    
    def visit_conditional_expression(self, node,null_coalescing_expression, location):
        if null_coalescing_expression:
            return self.visit(null_coalescing_expression)

    def visit_expressionstatement(self, node, expression, location):
        return self.visit(expression)
   
    def visit_conditional_and_expression(self,
                                        node, 
                                        inclusive_or_expression,
                                        OP_AND,
                                        location):
        if len(node.children)==1:     
            return self.visit(inclusive_or_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_inclusive_or_expression(self, node,
                                      exclusive_or_expression,
                                      BITWISE_OR,
                                      location):
        if len(node.children)==1:     
            return self.visit(exclusive_or_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_exclusive_or_expression(self, 
                                    node,
                                    and_expression,
                                    CARET,
                                    location):
        if len(node.children)==1:     
            return self.visit(and_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_and_expression(self, 
                            node,
                            equality_expression,
                            AMP,
                            location ):
        if len(node.children)==1:     
            return self.visit(equality_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_equality_expression(self, node, relational_expression, OP_EQ,OP_NE,location):
        if len(node.children)==1:     
            return self.visit(relational_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_relational_expression(self, node,shift_expression,LT, GT,OP_LE,OP_GE,IS,isType,AS,type_,location):
        if len(node.children)==1:
            return self.visit(shift_expression)
        else:
            args = map(lambda n:self.visit(n), node.children)   
            return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y}, list(args))
    
    def visit_shift_expression(self, 
                                node,
                                additive_expression,OP_LEFT_SHIFT,
                                right_shift,
                                location):

        if len(node.children)==1:
            return self.visit(additive_expression)[0]
        else:
            #op = OP_LEFT_SHIFT if OP_LEFT_SHIFT else right_shift
            args = map(lambda n:self.visit(n), node.children)   
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x, "right":y}, list(args))
    
    def visit_additive_expression(self, node,multiplicative_expression, PLUS,MINUS,location):
        if len(node.children)==1:
            return self.visit(multiplicative_expression)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            args = [arg[0] for arg in args]                  
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op,"left":x, "right":y, "pseudo_type":TYPED_API['operators'][op](
            x['pseudo_type'], y['pseudo_type'])[-1]}, list(args))

    def visit_multiplicative_expression(self, node,switch_expression, STAR,DIV,PERCENT, location):

        if len(node.children)==1:
            return self.visit(switch_expression)
        else:
            args = map(lambda n:self.visit(n), node.children)                       
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x, "right":y,"pseudo_type":TYPED_API['operators'][op](
            x['pseudo_type'], y['pseudo_type'])[-1]}, list(args))

    def visit_unary_expression(self, node, primary_expression,PLUS,type_, MINUS,OP_INC,OP_DEC, unary_expression, location):
        if len(node.children)==1:
            res = self.visit(primary_expression)
            return res
        else:
            if type_: 
                tp = self.visit(type_)
                return {"type":"standard_method_call", "message":tp["type"], "receiver":self.visit(unary_expression), "pseudo_type":tp["pseudo_type"]}
            if PLUS : op = PLUS
            if MINUS : op = MINUS  
            if OP_INC : op = OP_INC
            if OP_DEC : op = OP_DEC
            return {
                'type': 'unary_op',
                        'operator': op,
                        'value': self.visit(unary_expression)
            }

    def visit_returnstatement(self, node,expression,location):
        z = self.visit(expression)
        return {'type': 'implicit_return', 
                'value':z , "pseudo_type":z["pseudo_type"]}
    
    def visit_switch_expression(self, node,range_expression,SWITCH,switch_expression_arms, location):
        if len(node.children)==1:
            return self.visit(range_expression)
        else:
            lhs = self.visit(range_expression)
            rhs = self.visit(switch_expression_arms)
            return {"type":"switch", "op":"switch", "left":lhs, "right": rhs}

    def visit_range_expression(self, node,unary_expression,OP_RANGE, location):
        if len(node.children)==1:
            res = self.visit(unary_expression)
            return res[0]
        else:
            pass

    def visit_terminal(self, node, value, location):
        return value

    def visit_primary_expression(self, node,primary_expression_start,OP_INC, OP_DEC,member_access,method_invocation,bracket_expression, location ):
        ns, met = None, None
        if member_access:
            function = self.visit(member_access)
            function = str(function[0])
        if method_invocation:
            met = self.visit(method_invocation)
            ns = self.visit(primary_expression_start)
            if member_access:
                namespace = ns["name"]
                if namespace in FUNCTION_API:
                    api = FUNCTION_API[namespace].get(function)
                    if not api:
                        raise translation_error('CyMLT doesn\' t support %s %s at line %s' % (namespace, function,location[0]),
                                            suggestions='CyMLT supports those %s functions\n  %s' % (
                        namespace, prepare_table(TYPED_API[namespace], ORIGINAL_METHODS.get(namespace)).strip()))
                    elif not isinstance(api, dict):
                        z = api.expand(met)
                        return z            
                    #return {'type': 'standard_call', 'namespace': namespace, 'function': function, 'args': met, 'pseudo_type': "double"}
        
            else:
                return {
                        "type": "custom_call",
                        "args": met,
                        "function": ns["name"],
                        "pseudo_type": ns["pseudo_type"][-1]}
        
        pr = self.visit(primary_expression_start)
        print(pr)
        if bracket_expression: 
            t = self.visit(bracket_expression)
            print("jjj", t)
            return {'type': 'index',
                    'sequence': pr,
                    'index': t,
                    'pseudo_type': pr["pseudo_type"][1]
                    }
        return pr
    
    def visit_bracket_expression(self, node,indexer_argument, location):
        if len(indexer_argument) ==1:
            k = self.visit(indexer_argument)
            return  k
        return
    

      
    def visit_simplenameexpression(self, node,identifier,type_argument_list, location):
        id_type = self.type_env[str(identifier)]
        if id_type is None:
            raise type_check_error(
                '%s is not defined at line %s and column %s' %(str(identifier), location[0], location[1]))
        return {"type":"local", "name": str(identifier), "pseudo_type":id_type}

    def visit_member_access(self, node,identifier, type_argument_list,DOT,INTERR, location):
        if type_argument_list: print("jjjj")
        return identifier
    
    def visit_method_invocation(self, node,argument_list, location):
        return self.visit(argument_list)

    def visit_literalexpression(self, node,literal,location):
        return self.visit(literal)

    def visit_literal(self, node,boolean_literal,string_literal,INTEGER_LITERAL,REAL_LITERAL,CHARACTER_LITERAL,NULL,location):
        if boolean_literal: return {'type': 'bool', 'value': self.visit(boolean_literal), 'pseudo_type': 'bool'}
        if INTEGER_LITERAL: return {'type': 'int', 'value': self.visit(INTEGER_LITERAL), 'pseudo_type': 'int'}
        if REAL_LITERAL: 
            val = self.visit(REAL_LITERAL)
            if val.endswith("d"): return {'type': 'double', 'value': val[:-1], 'pseudo_type': 'double'}
            else: return {'type': 'float', 'value': val[:-1], 'pseudo_type': 'float'}
        if CHARACTER_LITERAL: 
            return {'type': 'char', 'value': str(self.visit(CHARACTER_LITERAL)), 'pseudo_type': 'char'}

        if string_literal: return {'type': 'str', 'value': str(self.visit(string_literal)), 'pseudo_type': 'str'}
  

    def visit_ifstatement(self, node,expression,if_body, location,ELSE,IF):
        otherwise = []
        if len(if_body)==1:
            test = self.visit(expression)
            block = self.visit(if_body)
        else:
            test = self.visit(expression)
            block = self.visit(if_body[0])
            while(node.ELSE and "IF" in dir(node.if_body[1])):
                z = node.if_body[1]
                elseif = z.if_body[0]
                r = self.visit_ifclausenode(z, z.expression, elseif)
                otherwise.append(r)
                node = z
                if "IF" not in dir(node) or "ELSE" not in dir(node):
                    break
            
            if "ELSE" in dir(node) and node.ELSE:
                r = self.visit_elseStatement(node.if_body[1])
                otherwise.append(r)
        R = {
            'type': 'if_statement',
            'test': test,
            'block': block,
            'pseudo_type': 'Void',
            'otherwise': otherwise
        }
        return R

    def visit_ifclausenode(self, node, condition, body):
        return {
                    'type': 'elseif_statement',
                    'test': self.visit(condition),
                    'block': self.visit(body),
                    'pseudo_type': 'Void'
        }

    def visit_elseStatement(self, node):
        block = self.visit(node)
        r = {
                'type': 'else_statement',
                'block': [block] if isinstance(block, dict) else block,
                'pseudo_type': 'Void'
            }
        return r

    def visit_forstatement(self,node,for_initializer,expression,for_iterator, embedded_statement, location):
        res = {}
        init = self.visit(for_initializer)
        res["type"] = "for_range_statement"
        res["start"] = init["decl"]["value"] if "decl" in init else init[0]["value"]
        expr = self.visit(expression)
        if expr["op"] in ["<", ">"]:
            res["end"] = expr["right"]
        elif expr["op"] in ["<=", ">="]: 
            res["end"]={'type': 'binary_op',
                'op': '+',
                'left': expr["right"],
                'right': {'type': 'int', 'value': '1', 'pseudo_type': 'int'},
                'pseudo_type': 'int'}


        r = self.visit(for_iterator)[0]
        if (r["type"] == "unary_op" and r["operator"] == "++") or ("inc" in r):
            res["step"] = {"type":"int", "value":"1", "pseudo_type":"int"}
        elif (r["type"] == "unary_op" and r["operator"] == "--") or ("dec" in r): 
            res["step"] = {"type":"int", "value":"-1", "pseudo_type":"int"}
        elif (r["type"])=="assignment":
            res["step"] = {"type":"int", "value":r["value"]["right"]["value"], "pseudo_type":"int"}
        res["index"] = init["decl"] if "decl" in init else init[0]["target"]
        res["index"]["type"] = "local"
        if "decl" in init: del res["index"]["value"]
        res["block"] = self.visit(embedded_statement)
        res["pseudo_type"] = "Void"
        return res

    
    def visit_whilestatement(self,node,expression,embedded_statement, location):
        test_node = self.visit(expression)
        return {
            'type': 'while_statement',
            'test': test_node,
            'block': self.visit(embedded_statement),
            'pseudo_type': 'Void'
        } 
    
    def visit_parenthesisexpressions(self, node,expression, OPEN_PARENS,CLOSE_PARENS,location):
        return self.visit(expression)
        



def process_tree(
    antlr_tree: ParseTree,
    base_visitor_cls: Type["BaseAstVisitor"] = None,
    transformer_cls = Transformer,
    simplify=True,
) -> "BaseNode":
    cls_registry = BaseNodeRegistry()

    if not base_visitor_cls:
        base_visitor_cls = BaseAstVisitor
    elif not issubclass(base_visitor_cls, BaseAstVisitor):
        raise ValueError("base_visitor_cls must be a BaseAstVisitor subclass")
    tree = base_visitor_cls(cls_registry).visit(antlr_tree)

    if transformer_cls is not None:
        if not issubclass(transformer_cls, BaseNodeTransformer):
            raise ValueError("transformer_cls must be a BaseNodeTransformer subclass")
        tree = transformer_cls(cls_registry).visit(tree)

    if simplify:
        tree = simplify_tree(tree, unpack_lists=False)

    return tree


"""from path import Path
filename = Path("c:/users/midingoy/documents/restore/users/midingoy/documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/testcs.cs")
tree = parsef(filename, start="compilation_unit", strict=False)
ast_proc = process_tree(tree)
trans = AstTransformer(ast_proc).transformer()
print(trans)
trans"""
