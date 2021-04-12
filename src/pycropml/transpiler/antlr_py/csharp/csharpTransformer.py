from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import PseudoCythonTypeCheckError, PseudoCythonNotTranslatableError, translation_error, type_check_error
from pycropml.transpiler.antlr_py.csharp.builtin_typed_api import *
from pycropml.transpiler.antlr_py.csharp.api_transform import *
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

class Constructor_declaration(AliasNode):
    _fields_spec = ["identifier", "formal_parameter_list","constructor_initializer", "body"]


class Property_declaration(AliasNode):
    _fields_spec = ["member_name","accessor_declarations","variable_initializer","right_arrow" ,"throwable_expression"]  

class Field_declaration(AliasNode):
    _fields_spec = [ "variable_declarators"]


class Namespace_member_declaration(AliasNode):
    _fields_spec = ["namespace_declaration", "type_declaration"]

class Namespace_declaration(AliasNode):
    _fields_spec = ["qualified_identifier", "namespace_body", "NAMESPACE"]

class Type_declaration(AliasNode):
     _fields_spec = ["attributes" ,"all_member_modifiers","class_definition"] 

class Class_body(AliasNode):
     _fields_spec = ["class_member_declarations"]  

class Namespace_body(AliasNode):
     _fields_spec = ["extern_alias_directives", "using_directives", "namespace_member_declarations"]     

class Namespace_or_type_name(AliasNode):
    _fields_spec = ["identifier", "type_argument_list", "qualified_alias_member"]

class Class_member_declarations(AliasNode):
    _fields_spec = ["class_member_declaration"]

class Common_member_declaration(AliasNode):
    _fields_spec =  ["constant_declaration","typed_member_declaration","event_declaration","conversion_operator_declarator"," body" , "right_arrow" ,"throwable_expression",
                         "constructor_declaration","VOID", "method_declaration","class_definition",
                        "struct_definition","interface_definition","enum_definition","delegate_definition"]

class Type_(AliasNode):
    _fields_spec = ["base_type", "INTERR", "rank_specifier", "STAR"]

class TypeofExpression(AliasNode):
    _fields_spec = ["unbound_type_name" , "type_" , "VOID"]
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
    _fields_spec = ["null_coalescing_expression", "throwable_expression"]

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

class ForeachStatement(AliasNode):
    _fields_spec = ["local_variable_type", "identifier", "expression", "embedded_statement"]

class Method_invocation(AliasNode):
    _fields_spec = ["argument_list"]

class Bracket_expression(AliasNode):
    _fields_spec = ["indexer_argument"]


class Transformer(BaseNodeTransformer):
    def visit_Compilation_unit(self, node):
        return Compilation_unit.from_spec(node)
    
    def visit_Namespace_member_declarations(self, node):
        return Namespace_member_declarations.from_spec(node)

    def visit_Constructor_declaration(self, node):
        return Constructor_declaration.from_spec(node)

    def visit_Property_declaration(self, node):
        return Property_declaration.from_spec(node)

    def visit_Field_declaration(self, node):
        return Field_declaration.from_spec(node)
    
    def visit_TypeofExpression(self, node):
        return TypeofExpression.from_spec(node)
    
    def visit_Common_member_declaration(self, node):
        return Common_member_declaration.from_spec(node)

    def visit_Namespace_member_declaration(self, node):
        return Namespace_member_declaration.from_spec(node)

    def visit_Class_member_declarations(self, node):
        return Class_member_declarations.from_spec(node)
    
    def visit_Class_body(self, node):
        return Class_body.from_spec(node)

    def visit_Namespace_body(self, node):
        return Namespace_body.from_spec(node)    

  
    def visit_Method_invocation(self, node):
        return Method_invocation.from_spec(node)

    def visit_Namespace_or_type_name(self, node):
        return Namespace_or_type_name.from_spec(node)

    def visit_Namespace_declaration(self, node):
        return Namespace_declaration.from_spec(node)

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

    def visit_ForeachStatement(self, node):
         return ForeachStatement.from_spec(node)
        
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
        self.assign = False
        self.function_name = 'top level'
        self.definitions = []
        self.decl = []
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
    
    def visit_namespace_declaration(self, node,NAMESPACE, qualified_identifier, namespace_body,SEMICOLON, location):
        z = self.visit(namespace_body) 
        namespace_id = qualified_identifier

        res = {"type":"namespace", "name":namespace_id, "body":z}

        return   res

    def visit_namespace_body(self, node,extern_alias_directives, using_directives, namespace_member_declarations, location):
        r = []
        res, res2 = [], []
        if using_directives:
            us = using_directives.children
            for n in us:
                z = n.namespace_or_type_name.identifier
                res.append(z)
            for n in res:
                usin = [str(rs) for rs in n ]
                us = usin[0] if len(usin)==1 else ".".join(usin)
                res2.append(us)
            u = res2 
            r.append(u)
        if namespace_member_declarations:
            z = self.visit(namespace_member_declarations.children)
            r.append(z)
        return r
            



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
                    "base": class_definition.class_base,  #TODO
                    "block": block } 
        if attributes:
            print("attribute1")    
 
    def visit_class_body(self, node, class_member_declarations, location):

        return self.visit(class_member_declarations)
    
    def visit_class_member_declarations(self, node, class_member_declaration, location):
 
        return self.visit(node.children)
            
        """
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

        
        return self.visit(class_member_declarations.children)"""

    def visit_class_member_declaration(self,
                                        node,
                                        common_member_declaration,
                                        destructor_definition,
                                        attributes,
                                        all_member_modifiers,
                                        location):
        
        z = {}
        x = None
        y=None
        if all_member_modifiers is not None:            
            x = self.visit(all_member_modifiers)
        if attributes is not None: 
            y = self.visit(attributes)
        if common_member_declaration:
            z = self.visit(common_member_declaration)
            if x : z["modifiers"] = x
            if y : z["attributes"] = y
        return z

    def visit_common_member_declaration(self, node,constant_declaration,
                                            typed_member_declaration,
                                            event_declaration,
                                            conversion_operator_declarator, body , right_arrow ,throwable_expression,
                                            constructor_declaration,
                                            VOID, method_declaration,
                                            class_definition,
                                            struct_definition,
                                            interface_definition,
                                            enum_definition,
                                            delegate_definition,location):
        
        if VOID:
            self.function_name = self.visit(method_declaration.method_member_name)[0]
            return {"type":"methodDef",  
                    "name":self.function_name,
                    "params":self.visit(method_declaration.formal_parameter_list),
                    "return_type":"VOID",
                    "block":self.visit(method_declaration.method_body)}

        if constructor_declaration:
            return self.visit(constructor_declaration)
        
        if typed_member_declaration:
            return self.visit(typed_member_declaration)
        
        else: print("TODO_common")
    

    def visit_constructor_declaration(self, node, identifier, formal_parameter_list,constructor_initializer, body, location):
        z={}
        z["type"] = "constructorDef"
        z["name"]= str(identifier)
        z["parameters"] = self.visit(formal_parameter_list) if formal_parameter_list else None
        if constructor_initializer : raise PseudoCythonTypeCheckError("Not Implemented")
        z["block"] = self.visit(body)
        return z

    def visit_property_declaration(self, node,member_name, accessor_declarations,variable_initializer,right_arrow ,throwable_expression, location):
        res = {}
        res["name"] = self.visit(member_name)
        res["accessors"] = self.visit(accessor_declarations)
        return res

    def visit_accessor_declarations(self, node, attributes, accessor_modifier, GET, accessor_body, set_accessor_declaration, SET, get_accessor_declaration, location):
        setbody, getbody = None, None
        if GET:
            getbody = self.visit(accessor_body)
            if set_accessor_declaration:
                setbody = self.visit(accessor_body)

        if SET:
            setbody = self.visit(accessor_body)
            if get_accessor_declaration:
                getbody = self.visit(accessor_body)
        return {"get":getbody, "set":setbody}
    
    def visit_member_name(self, node,namespace_or_type_name, location):
        return self.visit(namespace_or_type_name)

    def visit_field_declaration(self, node,  variable_declarators, location):
        res = {}
        s =  self.visit(variable_declarators)
        if isinstance(s, list): s = s[0]
        if "init" in s:
            res["name"] =s["name"]
            res["init"] = s["init"]
        else:
            res["name"] = s
        return res
    
    def visit_variable_declarators(self, node,variable_declarator, location):
        r=[]
        if isinstance(variable_declarator, list):
            r.append(self.visit(variable_declarator))
        else:
            return self.visit(variable_declarator)
        return r
    
    def visit_variable_declarator(self, node, identifier,ASSIGNMENT, variable_initializer, location):
        if variable_initializer is None:
            return str(identifier)
        
        else: return {"name":identifier, "init":self.visit(variable_initializer)}

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
        z = {}
        typ = self.visit(type_)
        if namespace_or_type_name:
            res = {"type":"namespace", "block":self.visit(namespace_or_type_name)}
        if indexer_declaration:
            res = {"type":"indexer", "block":self.visit(indexer_declaration)}
        if method_declaration:
            self.function_name = self.visit(method_declaration.method_member_name)[0]
            res = {"type":"methodDef",  
                    "name":self.function_name,
                    "return_type" :typ["pseudo_type"],
                    "params":self.visit(method_declaration.formal_parameter_list),
                    "block":self.visit(method_declaration.method_body)}
        if property_declaration:
            r = self.visit(property_declaration)
            pseudo = typ if isinstance(typ, str) else typ["pseudo_type"]
            return {"type":"propertyDef", "name":r["name"], "accessors":r["accessors"], "pseudo_type":pseudo}
        if operator_declaration:
            res = {"type":"operator", "block":self.visit(operator_declaration)}
        if field_declaration:
            r = self.visit(field_declaration)
            z = r["name"][0] if isinstance(r["name"], list) else r["name"]
            self.type_env.top[str(z)] = typ["pseudo_type"]
            res =  {"type":"fielddecl", "name":str(z), "pseudo_type":typ["pseudo_type"]}
            if "init" in r: res["init"] = r["init"]
            
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
        names=[]
        if len(type_argument_list) == 0:
            if len(identifier)>1:
                for id in identifier:
                    names.append(str(id))
                z= ".".join(names)
                res2 = {"type":"objectcreation", "class": z, "pseudo_type":z.split(".")[-1] }
                
            else:
                z= str(identifier[0])
                res2 = z
        else:
            if qualified_alias_member is not None:
                print("TODO qualified_alias_member")
                res2 = "tttttt"
            else:
                r = self.visit(type_argument_list)
                res2=[str(identifier[0]),str(r[0]["type"])]
        return res2


    def visit_objectcreationexpression(self, node,NEW,OPEN_BRACKET,expression_list,CLOSE_BRACKET,
                                    type_,
                                    anonymous_object_initializer,
                                    rank_specifier,
                                    array_initializer,
                                    object_creation_expression,
                                    object_or_collection_initializer,
                                    location):
        z = self.visit(type_)
        if isinstance(z, list): z = z[0]
        if object_creation_expression:
            z_oce = self.visit(object_creation_expression)
            if len(z_oce["args"]) > 0: 
                return {"type":z["type"], "args": z_oce["args"], "init":z_oce["init"], "pseudo_type":z["pseudo_type"]}
            else: 
                if z_oce["init"]:
                    return {"type":z["type"], "args": [], "init":z_oce["init"], "pseudo_type":z["pseudo_type"]}
                else: return None

        elif object_or_collection_initializer:
            z_oci = self.visit(object_or_collection_initializer)
            return {"type":z["type"], "init":z_oci["init"], "pseudo_type":z["pseudo_type"]} #
        elif expression_list:
            dimLen = self.visit(expression_list)
            dim = len(dimLen)
            size = dimLen
            z["init"] = {"type":"initArray", "value": self.visit(array_initializer) if array_initializer else None}
            return {"type":z["type"], "dim": dim, "size":size, "init":z["init"], "pseudo_type":z["pseudo_type"]}
        elif rank_specifier:
            print("TODO_rank_specifier")
        elif array_initializer : print("TODO_array_initializer")
        else: 
            print("hhhhhh")
            return z["type"]

    def visit_array_initializer(self, node,variable_initializer, location):
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
            if "init" in x:
                z["init"] = x["init"]
            else:
                z["init"] = x
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
            x = self.visit(namespace_or_type_name)
            typ = x[0] if isinstance(x, list) else x
            return {"type":typ, "pseudo_type":x}
        if OBJECT: 
            return self.visit(OBJECT)
        if DYNAMIC: 
            return self.visit(DYNAMIC)
        if STRING: 
            return {"type":"string", "pseudo_type":"string"}

    def visit_type_argument_list(self, node,type_, location):
        return self.visit(type_)
    
    def visit_numeric_type(self, node,integral_type,floating_point_type, location):
        if integral_type:
            if integral_type=="int": return {"type":"int", "pseudo_type":"int"}
            elif integral_type=="char": return {"type":"char", "pseudo_type":"char"}
            else: print("TODO22")
        if floating_point_type: 
            if floating_point_type=="float": return {"type":"float", "pseudo_type":"float"}
            elif floating_point_type=="double": return {"type":"double", "pseudo_type":"double"}
            else: print("TODO23")

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
        if local_constant_declaration: print("TODO26")

    def visit_local_variable_declaration(self, 
                                        node,
                                        local_variable_type,
                                        local_variable_declarator,
                                        location):
        var = local_variable_declarator
        if not isinstance(var, list):
            var = [var]
        z = {}
        z["type"] = "declaration"
        z["decl"] = []
        t = self.visit(local_variable_type)
        for d in var:
            r = self.visit(d)
            if r["value"] is not None:
                if r["value"]["type"] == "if_statement":
                    res1 = {"type":"declaration", "decl":{"type": t["type"], "name":r["name"],  "pseudo_type":t["pseudo_type"]}}
                    self.type_env[str(r["name"])] = t["pseudo_type"]
                    res2 = {"type":"if_statement",
                            "test":r["value"]["test"],
                            "block":{"type":"assignment",
                                     "target": {"type":"local", "name": r["name"], "pseudo_type":t["pseudo_type"]},
                                     "value":r["value"]["block"],
                                     "pseudo_type":"Void"},
                            "otherwise":{
                                "type":"assignment",
                                     "target": {"type":"local", "name": r["name"], "pseudo_type":t["pseudo_type"]},
                                     "value":r["value"]["otherwise"],
                                     "pseudo_type":"Void"                                
                            },
                            'pseudo_type': 'Void'
                            }
                    return [res1, res2]

                """if (t["pseudo_type"]!=r["value"]["pseudo_type"]) and (r["value"]["pseudo_type"]!="todooo") : 
                    raise type_check_error('bad declaration at line %s and column %s'%(location[0],location[1]))"""
            res = {"type": t["type"], "name":r["name"], "value":r["value"], "pseudo_type":t["pseudo_type"]}
            if res["value"] is None: del res["value"]
            z["decl"].append(res)
            self.type_env[str(res["name"])] = res["pseudo_type"]
        return z

    def visit_local_variable_declarator(self, node, identifier, local_variable_initializer, location):
        name = str(identifier)
        return {"name":name, "value":self.visit(local_variable_initializer)}

    def visit_local_variable_initializer(self, node, expression,array_initializer,stackalloc_initializer,location):   
        if array_initializer: 
            z = self.visit(array_initializer)
            return {"type":"array", "value":z, "pseudo_type":["array","%s"%z[0]["pseudo_type"]]}
        if expression:
            return self.visit(expression)
    
    def visit_expression(self, node, assignment, non_assignment_expression, location):
        if non_assignment_expression:
            x = self.visit(non_assignment_expression)
            return  x[0] if isinstance(x, list) else x
        if assignment:
            return self.visit(assignment)
    
    def visit_assignment(self, node, unary_expression,assignment_operator,expression, location):
        self.assign = False
        if assignment_operator:
            self.assignment = True
            z =  {
                    'type': 'assignment',
                    'target':self.visit(unary_expression),
                    'op':assignment_operator,
                    'value': self.visit(expression),
                    'pseudo_type': 'Void'
                }
            """r = z["value"]["pseudo_type"]
            if "Function" in z["value"]["pseudo_type"]:
                r = z["value"]["pseudo_type"][-1]

            if z["target"]["pseudo_type"]!="double" and z["target"]["pseudo_type"]!=r:
                jj = (z["target"]["pseudo_type"]!="double" and z["target"]["pseudo_type"]!=r)
                raise type_check_error(
                ' Cannot implicitly convert type %s from %s to %s at line %s. An explicit conversion exists (are you missing a cast11? %s)'%(z["target"]["name"],z["target"]["pseudo_type"], z["value"]["pseudo_type"], location[0], jj))"""
            return z
        
        else: 
            print("TODO_assignment")
            return "TODO"

    def visit_non_assignment_expression(self, 
                                        node, 
                                        lambda_expression,
                                        query_expression,
                                        conditional_expression,
                                        location):
        if  lambda_expression: print("TODO lambda")  
        if  query_expression: print("TODO query")     
        return self.visit(conditional_expression)
    
    def visit_conditional_expression(self, node,null_coalescing_expression,throwable_expression, location):
        if null_coalescing_expression:
            res = self.visit(null_coalescing_expression)
        if throwable_expression:
            bodyif = self.visit(throwable_expression[0])
            bodyelse = self.visit(throwable_expression[1])
            res = {
                'type': 'if_statement',
                'test': res,
                'block': bodyif,
                'pseudo_type': 'Void',
                'otherwise': bodyelse
            }
            print(res, "jkjlkmkm")
        return res
        

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
            return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))
    
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
            args = [arg[0] if isinstance(arg, list) else arg for arg in args]                  
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
        
        if primary_expression:
            z =  self.visit(primary_expression)
            return z
        if type_: 
            tp = self.visit(type_)
            return {"type":"standard_method_call", "message":tp["type"], "receiver":self.visit(unary_expression), "pseudo_type":tp["pseudo_type"]}
        else:
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
            if OP_RANGE:
                print("TODO_OP_RANGE")

    def visit_terminal(self, node, value, location):
        return self.visit(value)

    def translate(self, member_access):
        if len(member_access)==1:
            r = self.visit(member_access)
            return r[0]
        else:
            z = []
            for m in member_access:
                z.append(self.visit(m))
            return '.'.join(z)

    def visit_primary_expression(self, node,primary_expression_start,OP_INC, OP_DEC,member_access,method_invocation,bracket_expression, location ):
        args = None
        res = self.visit(primary_expression_start)
        if member_access:
            m = self.translate(member_access)
            res = {"type":"member_access", "name":res["name"], "member":m, "pseudo_type":res["pseudo_type"]}

        if method_invocation:
            args = self.visit(method_invocation)
            if member_access:
                if m.find(".") == -1:
                    method = m
                    receiver = res["name"]
                else:
                    method = m.split(".")[-1]
                    receiver = res["name"]+"."+".".join(m.split(".")[:-1])
            
                receiver_type = self.type_env[receiver] 
                receiver_type = receiver_type[0] if isinstance(receiver_type, list) else receiver_type
                rec =  {"type":"local" , "name":receiver, "pseudo_type":self.type_env[receiver]}
                
                
                if receiver in FUNCTION_API:
                    print(location, "hhkhjkkjkhjk", receiver, method)
                    api = FUNCTION_API[receiver].get(method) 
                    if not api:
                        raise translation_error('pseudo-cython doesn\' t support %s %s' % (receiver, method),
                                                location, [location[0]],
                                                suggestions='pseudo-cython supports those %s functions\n  %s' % (
                            receiver,
                            prepare_table(TYPED_API[receiver], ORIGINAL_METHODS.get(receiver)).strip()))

                    elif not isinstance(api, dict):
                        z = api.expand(args )
                        return z
                    else:
                    
                        for count, (a, b) in enumerate(list(api.items())):
                            if len(args) == a:
                                return b.expand(args)
                        raise translation_error(
                            'pseudo-cython doesn\'t support %s%s with %d args' % (
                                receiver, method, len(args)),
                            location, self.lines[location[0]])
                          
                elif receiver_type in METHOD_API:
                    api = METHOD_API.get(receiver_type,{}).get(method)
                    if api:
                        res = api.expand([rec]+ args)
                        if self.assign == False:
                            res = {"type": 'ExprStatNode', 'expr': res}
                    if not api:
                        raise translation_error('CyMLT doesn\' t support %s %s at line %s' % (receiver_type, method,location[0]),
                                                suggestions='CyMLT supports those %s functions\n  %s' % (
                          receiver, prepare_table(TYPED_API[receiver], ORIGINAL_METHODS.get(receiver_type)).strip()))
                

                else: res = {'type': 'custom_call', 'namespace': receiver, "function":method, 'args': args, 'pseudo_type': "todooo"}       
              
            else:
                res = {
                        "type": "custom_call",
                        "args": args,
                        "function": res["name"],
                        "pseudo_type": res["pseudo_type"][-1] if res["pseudo_type"] is not None else "unknown" } ####Todooooooo
        
        if bracket_expression:
            print(location, "eedddddddd", res["pseudo_type"]) 
            t = self.visit(bracket_expression)
            res = {'type': 'index',
                    'sequence': res,
                    'index': t,
                    'pseudo_type': res["pseudo_type"]
                    }
        if OP_DEC: 
            res = {'type': 'unary_op',
                            'operator': OP_DEC[0],
                            'value': res
                }
        if OP_INC: 
            res = {'type': 'unary_op',
                            'operator': OP_INC[0],
                            'value': res
                }
        return res


    def visit_typeofexpression(self, node, unbound_type_name , type_ , VOID,location):
        if unbound_type_name is not None:
            r = self.visit(unbound_type_name)
        elif type_:
            r = self.visit(type_)
        elif VOID:
            r = "VOID"
        res = {"type":"typeofexpression", "class_type":r}
        return res
    
    def visit_unbound_type_name(self, node, identifier, DOUBLE_COLON,DOT,generic_dimension_specifier, location):
        if not generic_dimension_specifier:
            if isinstance(identifier, list):
                return ".".join(self.visit(identifier))
            else:
                return self.visit(identifier)
        else:
            raise PseudoCythonTypeCheckError("Not implemented")

    def visit_primary_expression_start(self, node, location):
        print("TODOprimary_expression_start")
        pass
    
    def visit_bracket_expression(self, node,indexer_argument, location):
        if len(indexer_argument) ==1:
            k = self.visit(indexer_argument)
            return  k
        else: print("TODO_bracket")
        return
    

      
    def visit_simplenameexpression(self, node,identifier,type_argument_list, location):
        id_type = self.type_env.top[str(identifier)]
        if id_type is None:
            """ raise type_check_error(
                '%s is not defined at line %s and column %s' %(str(identifier), location[0], location[1]))""" # remove cote
        return {"type":"local", "name": str(identifier), "pseudo_type":id_type}

    def visit_member_access(self, node,identifier, type_argument_list,DOT,INTERR, location):
        if type_argument_list: print("TODO_type_argument_list")
        res = str(identifier)
        return res
    
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

        if string_literal: 
            val = str(string_literal)
            if '"' in val:
                val = val.replace('"', '')
                val = val.encode('utf-8')
            return {'type': 'string', 'value': val, 'pseudo_type': 'string'}
  

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
        res["start"] = init["decl"][0]["value"] if "decl" in init else init[0]["value"]
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
        ii = self.visit(for_iterator)
        if (r["type"] == "unary_op" and r["operator"] == "++") or ("inc" in r):
            res["step"] = {"type":"int", "value":"1", "pseudo_type":"int"}
        elif (r["type"] == "unary_op" and r["operator"] == "--") or ("dec" in r): 
            res["step"] = {"type":"int", "value":"-1", "pseudo_type":"int"}
        elif (r["type"])=="assignment":
            res["step"] = {"type":"int", "value":r["value"]["right"]["value"], "pseudo_type":"int"}
        res["index"] = init["decl"][0] if "decl" in init else init[0]["target"]
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
    
    def visit_foreachstatement(self, node, local_variable_type, identifier,expression, embedded_statement, location):
        z = self.visit(local_variable_type)
        return {'type': 'for_statement',
                'sequences': {'type': 'for_sequence',
                    'sequence': self.visit(expression)},
                'iterators': {'type': 'for_iterator',
                    'iterator': {'type':'local', 'name':self.visit(identifier), 'pseudo_type':z["pseudo_type"]}},
                'block': self.visit(embedded_statement)}  

    def visit_parenthesisexpressions(self, node,expression, OPEN_PARENS,CLOSE_PARENS,location):
        return self.visit(expression)
    
    def visit_trystatement(self, node, TRY, block,catch_clauses, finally_clause, location):
        print("tryyyyy", location)
        return

    def visit_throwstatement(self, node, THROW, expression,SEMICOLON, location):
        return {"type":"throwstatement", 
                "exception": self.visit(expression) if expression else None,
                'pseudo_type': 'Void'}

