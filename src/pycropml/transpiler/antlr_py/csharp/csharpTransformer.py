from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import *
from pycropml.transpiler.antlr_py.csharp.builtin_typed_api import *
from pycropml.transpiler.antlr_py.csharp.api_transform import *
from pycropml.transpiler.env import Env
from pycropml.transpiler.helpers import *
from pycropml.transpiler.antlr_py import parse
import ast
from ast import AST, arg
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

class Constructor_initializer(AliasNode):
    _fields_spec = ["BASE", "THIS","argument_list" ]

class Property_declaration(AliasNode):
    _fields_spec = ["member_name","accessor_declarations","variable_initializer","right_arrow" ,"throwable_expression"]  

class Field_declaration(AliasNode):
    _fields_spec = [ "variable_declarators"]

class Enum_definition(AliasNode):
    _fields_spec = [ "identifier", "enum_base", "enum_body"]
    
class Namespace_member_declaration(AliasNode):
    _fields_spec = ["namespace_declaration", "type_declaration"]

class Namespace_declaration(AliasNode):
    _fields_spec = ["qualified_identifier", "namespace_body", "NAMESPACE"]

class Type_declaration(AliasNode):
     _fields_spec = ["attributes" ,"all_member_modifiers","class_definition"] 

class Class_body(AliasNode):
     _fields_spec = ["class_member_declarations"]  

class Attributes(AliasNode):
     _fields_spec = ["attribute_section"]  

class Namespace_body(AliasNode):
     _fields_spec = ["extern_alias_directives", "using_directives", "namespace_member_declarations"]     

class Namespace_or_type_name(AliasNode):
    _fields_spec = ["identifier", "type_argument_list", "qualified_alias_member", "DOT"]

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
    _fields_spec = ['simple_type','class_type', "VOID", "tuple_type"]

class ParenthesisExpressions(AliasNode):
    _fields_spec = ['expression']

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
    _fields_spec = ["primary_expression", "unary_expression", "TILDE","type_","PLUS","BANG", "MINUS","OP_INC","OP_DEC", "STAR"]

class Non_assignment_expression(AliasNode):
    _fields_spec = ["lambda_expression", "query_expression","conditional_expression"]

class Conditional_expression(AliasNode):
    _fields_spec = ["null_coalescing_expression", "throwable_expression"]

class Conditional_and_expression(AliasNode):
    _fields_spec = ["inclusive_or_expression", "OP_AND"]

class Conditional_or_expression(AliasNode):
    _fields_spec = ["conditional_and_expression", "OP_OR"]

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

class DefaultValueExpression(AliasNode):
    _fields_spec = ["type_" ]

class Object_creation_expression(AliasNode) :                                 
    _fields_spec = ["argument_list","object_or_collection_initializer"]

class Collection_initializer(AliasNode):
    _fields_spec = ["element_initializer"]

class Element_initializer(AliasNode):
    _fields_spec = ["non_assignment_expression","expression_list" ]

class Array_type(AliasNode):
    _fields_spec = ["base_type","rank_specifier"]

class TupleExpression(AliasNode):
    _fields_spec = ["argument"]

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

class Argument_list(AliasNode):
    _fields_spec = ["argument"]

class Argument(AliasNode):
    _fields_spec = ["identifier", "type_", "expression"]


class Bracket_expression(AliasNode):
    _fields_spec = ["indexer_argument"]
    
class Interface_definition(AliasNode):
    _fields_spec = ["INTERFACE", "identifier", "variant_type_parameter_list", "interface_base",
                    "type_parameter_constraints_clauses", "class_body"]

class SwitchStatement(AliasNode):
    _fields_spec = ["switch_section", "expression"]

class Switch_section(AliasNode):
    _fields_spec = ["switch_label", "statement_list"]

class Switch_label(AliasNode):
    _fields_spec = ["expression", "case_guard"]

class BreakStatement(AliasNode):
    _fields_spec = ["BREAK"]
    
class Class_base(AliasNode):
    _fields_spec = ["class_type","namespace_or_type_name"]

class ThrowStatement(AliasNode):
    _fields_spec = ["THROW", "expression"]
    
class Fixed_parameter(AliasNode):
    _fields_spec = [ "attributes", "parameter_modifier", "arg_declaration", "ARGLIST"]

class  Istype(AliasNode):
    _fields_spec = ["base_type", "rank_specifier", "isTypePatternArms", "identifier"]

class Array_initializer(AliasNode):
    _fields_spec = ["variable_initializer"]

class Enum_member_declaration(AliasNode):
    _fields_spec = ["attributes", "identifier", "expression"]
    
class BaseAccessExpression(AliasNode):
    _fields_spec = ["identifier", "type_argument_list", "expression_list"]


class Transformer(BaseNodeTransformer):
    def visit_Compilation_unit(self, node):
        return Compilation_unit.from_spec(node)
    
    def visit_Class_base(self, node):
        return Class_base.from_spec(node)
    
    def visit_ThrowStatement(self, node):
        return ThrowStatement.from_spec(node)
    
    def visit_SwitchStatement(self, node):
        return SwitchStatement.from_spec(node)
    
    def visit_BreakStatement(self, node):
        return BreakStatement.from_spec(node)
    
    def visit_Switch_section(self, node):
        return Switch_section.from_spec(node)
    
    def visit_Switch_label(self, node):
        return Switch_label.from_spec(node)
    
    def visit_Attributes(self, node) :
        return Attributes.from_spec(node)
    
    def visit_Interface_definition(self, node):
        return Interface_definition.from_spec(node)
    
    def visit_Namespace_member_declarations(self, node):
        return Namespace_member_declarations.from_spec(node)

    def visit_Constructor_declaration(self, node):
        return Constructor_declaration.from_spec(node)

    def visit_Constructor_initializer(self, node):
        return Constructor_initializer.from_spec(node)


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
    
    def visit_DefaultValueExpression(self, node):
        return DefaultValueExpression.from_spec(node)

    def visit_Namespace_body(self, node):
        return Namespace_body.from_spec(node)    

  
    def visit_Method_invocation(self, node):
        return Method_invocation.from_spec(node)
    
    def visit_Argument_list(self, node):
        return Argument_list.from_spec(node)

    def visit_Argument(self, node):
        return Argument.from_spec(node)

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

    def visit_ParenthesisExpressions(self, node):
        return ParenthesisExpressions.from_spec(node)

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

    def visit_Conditional_or_expression(self,node):
        return Conditional_or_expression.from_spec(node)
    
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

    def visit_TupleExpression(self, node):
        return TupleExpression.from_spec(node) 

    def visit_Switch_expression(self, node):
        return Switch_expression.from_spec(node) 

    def visit_Range_expression(self, node):
        return Range_expression.from_spec(node)

    def visit_ReturnStatement(self, node):
        return ReturnStatement.from_spec(node) 

    
    def visit_SimpleNameExpression(self, node):
        return SimpleNameExpression.from_spec(node)


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
     
    def visit_Enum_definition(self, node):
         return Enum_definition.from_spec(node)

    def visit_WhileStatement(self, node):
         return WhileStatement.from_spec(node)

    def visit_ForeachStatement(self, node):
         return ForeachStatement.from_spec(node)
        
    def visit_Bracket_expression(self, node):
        return Bracket_expression.from_spec(node)
    
    def visit_Fixed_parameter(self, node):
        return Fixed_parameter.from_spec(node)
    
    def visit_Istype(self, node):
        return Istype.from_spec(node)

    def visit_Array_initializer(self, node):
        return Array_initializer.from_spec(node)
    
    def visit_Enum_member_declaration(self, node):
        return Enum_member_declaration.from_spec(node)

    def visit_BaseAccessExpression(self, node):
        return BaseAccessExpression.from_spec(node)

    """def visit_Element_initializer(self, node):
        return Element_initializer.from_spec(node)"""

class AstTransformer():
    def __init__(self, tree, code: str=None, comments:str=None, env:str=None):
        self.tree = tree
        self.base = 0
        self.type_env = Env(dict(list(TYPED_API.items())), None)

    def transformer(self):
        self.type_env['functions'] = {}
        self.assign = False
        self.function_name = 'top level'
        self.definitions = []
        self._definition_index = {'functions': {}}
        self.non_identifier=[]
        self.decl = []
        self.clas = []
        self.namespace = []
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
                "body": z,
                "pseudo_type": "Void"}
    
    def visit_interface_definition(self, node, INTERFACE, identifier, variant_type_parameter_list, interface_base,
                    type_parameter_constraints_clauses, class_body, location):
        name = self.visit(identifier)
        self.clas.append(name)
        body = self.visit(class_body)
        res = {"type":"interface",
                "name": name,
                "block": body } 
        self.clas.pop()
        return res

    def visit_namespace_member_declarations(self,node, namespace_member_declaration, location):

        return self.visit(node.children)
    
    def visit_breakstatement(self, node, BREAK, location):
        return {
            "type": "breakstatnode"
        }

    def visit_switchstatement(self, node, switch_section, expression, location):
        self._if = 0
        selector = self.visit(expression)
        self.sel.append(selector)
        body = self.visit(switch_section)
        ifst = body[0]
        elsest = body[1:]
        ifst["otherwise"] = elsest
        return ifst

    def translate_list(self, inputs):
        res = []
        for arg in inputs:
            b = self.visit(arg)
            res.append(b)
        return res
    
    def visit_switch_section(self, node, switch_label, statement_list, location):
        casebody = self.visit(statement_list)
        res = self.translate_list(switch_label)
        r = []
        if len(res)>=1 and res[0]["type"]!="else_statement":
            for f in res:
                f["block"] = casebody
                r.append(f)
            return r
        elif res[0]["type"]=="else_statement": 
            res[0]["block"] = casebody
            return res[0]
        
        
    def visit_switch_label(self, node, expression, case_guard, location):
        if expression:
            res = self.visit(expression)
            test={"type":"comparison", "op": "==", "left":self.sel[-1], "right":res}
            if self._if ==0:
                r = {"type":"if_statement", "test":test, "block":[],"otherwise":[]}
            else:
                r = {"type":"elseif_statement", "test":test, "block":[]}
        else: 
            r = {"type":"else_statement", "block":[]}
        self._if = self._if + 1
        return r

    def visit_throwstatement(self, node, THROW, expression, location ):
        print(f"visit_throwstatement not yet implemented at {location}")
        return 
        
    
    def visit_Attributes(self, node) :
        return Attributes.from_spec(node)
    
    def visit_namespace_member_declaration(self,node, namespace_declaration, type_declaration, location):
        if type_declaration:
            return   self.visit(type_declaration)
        if namespace_declaration:
            return self.visit(namespace_declaration)
    
    def visit_namespace_declaration(self, node,NAMESPACE, qualified_identifier, namespace_body,SEMICOLON, location):
        namespace_id = self.visit(qualified_identifier)
        self.namespace.append(namespace_id)
        z = self.visit(namespace_body)
        res = {"type":"namespace", "name":namespace_id, "body":z}
        self.namespace.pop()
        return   res
    
    def visit_qualified_identifier(self, node, identifier, DOT, location):
        if len(identifier)==1: return self.visit(identifier[0].IDENTIFIER)
        res = self.translate_list(identifier)
        if len(res)==1: return res[0]
        else: return ".".join(res)
    

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
            name =  self.visit(class_definition.identifier)
            self.clas.append(name)
            block = self.visit(class_definition.class_body)
            res = {"type":"classDef",
                    "name": name,
                    "base": self.visit(class_definition.class_base) if class_definition.class_base else None ,  #TODO
                    "block": block } 
            self.clas.pop()
            return res
            
        if attributes:
            raise PseudoCythonTypeCheckError("Not implemented attributes , %s"%location)   
        
        
    def visit_class_base(self, node,class_type,namespace_or_type_name, location):
        res = []
        res.append(self.visit(class_type))
        if namespace_or_type_name:
            v = self.translate_list(namespace_or_type_name)
            res = res + v    
        return res
    
 
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
            if z:
                if x : z["modifiers"] = x
                if y : z["attributes"] = y
        return z
    
    def visit_attributes(self, node,attribute_section, location):
        print("Not implemented attributes , %s"%location[0]) 
        return 

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
        self.sel=[]
        
        if VOID:
            self.non_identifier = []
            self.function_name = self.visit(method_declaration.method_member_name)[0]
            param = self.visit(method_declaration.formal_parameter_list)
            ps = [p["pseudo_type"] for p in param] if param else [None]
            v = {"type":"methodDef",  
                    "name":self.function_name,
                    "params":param,
                    "return_type":"Void",
                    "block":self.visit(method_declaration.method_body),
                    "pseudo_type":["function"]+ps + ["Void"],
                    "non_identifier":self.non_identifier,
                    "namespace":self.namespace[-1],
                    "class_":self.clas[-1]}
            """domain = [a["pseudo_type"] if a is not None else None for a in v["params"] if v["params"] ]
            self.type_env.top["functions"][v["name"]] = domain + ["Void"]"""
            v["pseudo_type"] =  ["Void"]
            return v

        if constructor_declaration:
            return self.visit(constructor_declaration)
        
        elif typed_member_declaration:
            return self.visit(typed_member_declaration)
        
        elif enum_definition:
            return self.visit(enum_definition)
        elif constant_declaration:
            return self.visit(constant_declaration)
    
        elif event_declaration:
            pass
        
        elif class_definition: pass
        
        else: raise PseudoCythonTypeCheckError("Not implemented common member declaration , %s"%location[0])
    

    def visit_constructor_declaration(self, node, identifier, formal_parameter_list,constructor_initializer, body, location):
        z={}
        z["type"] = "constructorDef"
        z["name"]= self.visit(identifier)
        z["parameters"] = self.visit(formal_parameter_list) if formal_parameter_list else None
        if constructor_initializer : z["init"] = self.visit(constructor_initializer)
        z["block"] = self.visit(body)  if body else []     
        return z
    
    def visit_block(self, node, location, statement_list):
        if statement_list : return []
        return self.visit(statement_list)

    def visit_constructor_initializer(self, node, location, BASE, THIS, argument_list):
        p = "THIS" if THIS else BASE
        arg = self.visit(argument_list) if argument_list else []  
        
        return {"type":"constructor_init", "keyw":p, "args": arg, "pseudo_type":"Void"}

    def visit_property_declaration(self, node,member_name, accessor_declarations,variable_initializer,right_arrow ,throwable_expression, location):
        res = {}
        res["name"] = self.visit(member_name)
        accessors = self.visit(accessor_declarations)
        res["get"] = accessors["get"]
        res["set"] = accessors["set"]
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
    
    def visit_defaultvalueexpression(self, node,type_, location):
        return {"type":"custom_call", "name":"default", "args": self.visit("type")}
    
    def visit_variable_declarator(self, node, identifier,ASSIGNMENT, variable_initializer, location):
        if variable_initializer is None:
            return self.visit(identifier)
        
        else: return {"name":self.visit(identifier), "init":self.visit(variable_initializer)}

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
        self.sel= []
        typ = self.visit(type_)
        if namespace_or_type_name:
            res = {"type":"namespace", "block":self.visit(namespace_or_type_name)}
        if indexer_declaration:
            res = {"type":"indexer", "block":self.visit(indexer_declaration)}
        if method_declaration:
            self.non_identifier = []
            self.function_name = self.visit(method_declaration.method_member_name)[0]
            param = self.visit(method_declaration.formal_parameter_list)
            ps = [p["pseudo_type"] for p in param] if param else [None]
            res = {"type":"methodDef",  
                    "name":self.function_name,
                    "return_type" :typ["pseudo_type"],
                    "params":param,
                    "block":self.visit(method_declaration.method_body),
                    "pseudo_type":["function"] + ps + [typ["pseudo_type"]],
                    "non_identifier":self.non_identifier,
                    "namespace":self.namespace[-1],
                    "class_":self.clas[-1]}
            #domain = [a["pseudo_type"] for a in res["params"] if res["params"] ]
            self.type_env.top["functions"][res["name"]] = [res["return_type"]]

        if property_declaration:
            r = self.visit(property_declaration)
            pseudo = typ if isinstance(typ, str) else typ["pseudo_type"]
            self.type_env.top[r["name"]] = pseudo
            return {"type":"propertyDef", "name":r["name"], "get":r["get"], "set":r["set"], "pseudo_type":pseudo}
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

        re =  self.visit(res)
        if STAR : re["operator"] = "*"
        return re

    def visit_base_type(self, node,simple_type,class_type,VOID, tuple_type, location):
        if simple_type:
            res = simple_type
        if class_type:
            res = class_type
        if VOID:
            return "VOID"
        if tuple_type:
            res = self.visit(tuple_type)
        return self.visit(res)

    def visit_array_type(self,node,base_type,location):
        z = self.visit(base_type)
        res = {}
        res["type"] = "array"
        res["pseudo_type"] = ["array",z["type"]]
        return res

    def  visit_namespace_or_type_name(self, node, identifier,type_argument_list,qualified_alias_member,DOT, location) :
        #names=[]
        
        if qualified_alias_member is not None:
            raise PseudoCythonTypeCheckError("Not implemented quaified alias member , %s"%location[0])
        
        if len(identifier)==1: 
            #res = self.visit(identifier[0].IDENTIFIER)
            res = self.visit(identifier[0])
        else: res = self.translate_list(identifier)
        
        if not  type_argument_list :
            if isinstance(res, str): return res
            elif len(res)==1: 
                return res[0]
            else: 
                z = ".".join(res) 
                return  {"type":"objectcreation", "typename": z, "pseudo_type":z.split(".")[-1] } 
        
        else:
            targ = self.visit(type_argument_list)
            if len(targ)==1:
                if isinstance(targ[0], dict): targ = [targ[0]["pseudo_type"]]
                
            if isinstance(res, str): return [res] + targ
            elif len(res)==1: 
                return res[0] + targ
            else: 
                z = ".".join(res) 
                return  {"type":"objectcreation", "typename": z, "pseudo_type":[z.split(".")[-1]] + targ} 
             
        """
        if len(type_argument_list) == 0:
            if len(identifier)>1:
                for id in identifier:
                    names.append(str(id))
                z= ".".join(names)
                res2 = {"type":"objectcreation", "typename": z, "pseudo_type":z.split(".")[-1] }
                
            else:
                z= str(identifier[0])
                res2 = z
        else:
            if qualified_alias_member is not None:
                raise PseudoCythonTypeCheckError("Not implemented quaified alias member , %s"%location)
            else:
                r = self.visit(type_argument_list)
                res2=[str(identifier[0]),str(r[0]["type"])]
        return res2
        """


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
                else: return {"type":z["type"], "init": [], "args":[], "pseudo_type":z["pseudo_type"]}

        elif object_or_collection_initializer:
            z_oci = self.visit(object_or_collection_initializer)
            return {"type":z["type"], "init":z_oci["init"], "pseudo_type":z["pseudo_type"]} #
        elif expression_list:  
            dimLen = self.visit(expression_list)  # TODO
            dim = len(dimLen)
            size = dimLen
            z["init"] = {"type":"initArray", "value": self.visit(array_initializer) if array_initializer else None}
            #return {"type":"array"}
            if array_initializer: return {"type":"array", "dim": dim, "elts":size, "init":z["init"], "pseudo_type":["array",z["pseudo_type"]]}
            else: return {"type":"array", "dim": dim, "elts":size, "pseudo_type":["array",z["pseudo_type"]]}
        elif rank_specifier:
            dim = len(rank_specifier)
            if array_initializer :
                init = self.visit(array_initializer)
                init["dim"] = dim
            return init #{"type":"array", "dim":dim, "init": init, "pseudo_type": ["array", init[0]["pseudo_type"]]}
            #raise PseudoCythonTypeCheckError("Not implemented array initializer , %s"%location[0])
        else: 
            raise PseudoCythonTypeCheckError("Not implemented object creation , %s"%location[0])
            #return z["type"]


    def visit_object_initializer(self, node,member_initializer_list, location):
        z = {}
        if member_initializer_list:
            z["init"] = self.visit(member_initializer_list)
        else:
            z["init"] = []
        return z

    def visit_array_initializer(self, node,variable_initializer, location):
        r = self.visit(variable_initializer)
        res =  {"type":"array", "init":{"type":"initCollection", "value": r}, "pseudo_type": ["array", r[0]["pseudo_type"]], "size": str(len(r))}
        return res
        """if len (node.children)==1:
            res = self.visit(variable_initializer)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            args = [arg[0] for arg in args if isinstance(arg, list)]
            return args"""

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

    def visit_argument_list(self, node, argument,location):
        res = []
        for arg in argument:
            b = self.visit(arg)
            res.append(b)
        return res
    
    def visit_enum_definition(self, node, identifier, enum_base, enum_body, location):
        #TODO
        id = self.visit(identifier)
        if enum_base: 
            print("ENUM BASE TODO")
        body = self.visit(enum_body)
        return {"type":"enum", "name": id, "block":body, "namespace":self.namespace[-1], "class_":self.clas[-1] }


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
            return {"type":"object", "pseudo_type":"object"}
        if DYNAMIC: 
            return self.visit(DYNAMIC)
        if STRING: 
            return {"type":"string", "pseudo_type":"string"}

    def visit_type_argument_list(self, node,type_, location):
        return self.visit(type_)
    
    def visit_numeric_type(self, node,integral_type,floating_point_type, location):
        if integral_type:
            if integral_type=="int": return {"type":"int", "pseudo_type":"int"}
            elif integral_type=="long": return {"type":"int", "pseudo_type":"int"}
            elif integral_type=="char": return {"type":"char", "pseudo_type":"char"}
            else: raise PseudoCythonTypeCheckError("Not implemented integral type , %s"%location[0])
        if floating_point_type: 
            if floating_point_type=="float": return {"type":"float", "pseudo_type":"float"}
            elif floating_point_type=="double": return {"type":"double", "pseudo_type":"double"}
            else: raise PseudoCythonTypeCheckError("Not implemented floating , %s"%location)

    def visit_arg_declaration(self,
                                node,
                                type_,
                                identifier,
                                expression,
                                location):
        z= {"type":"local","name":self.visit(identifier), "pseudo_type":self.visit(type_)["pseudo_type"]}
        self.type_env[z["name"]]=z["pseudo_type"]
        return z

    def visit_declarationstatement(self,
                                     node,
                                     local_variable_declaration,
                                     local_constant_declaration,
                                     local_function_declaration,
                                     location):
        if local_variable_declaration:
            return self.visit(local_variable_declaration)
        if local_constant_declaration: 
            return self.visit(local_constant_declaration)
        if local_function_declaration :
            raise PseudoCythonTypeCheckError("Not implemented local constant declaration , %s"%location[0])
    
    def visit_local_constant_declaration(self, node, CONST, type_, constant_declarators, location):
        res = {}
        res["type"] = "declaration"
        res["decl"] = []
        typ = self.visit(type_)
        decls = self.visit(constant_declarators)
        for d in decls: 
            d["type"] = typ["pseudo_type"]       
            res["decl"].append(d)
        return res
    
    def visit_constant_declarator(self, node, identifier, expression, ASSIGNMENT, location):
        name = self.visit(identifier)
        value = self.visit(expression)
        pseudo_type = value["pseudo_type"]
        if "value" in value: value = value["value"]
        return {"value": value, "name": name, "pseudo_type":pseudo_type}
    
    def visit_constant_declaration(self, node, CONST ,type_, constant_declarators, SEMICOLON, location):
        return self.visit_local_constant_declaration(node, CONST, type_, constant_declarators, location)
            
    def visit_local_variable_type(self, node, VAR,  type_, location):
        if type_: return self.visit(type_)
        else: return "VAR"
        

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
                                     "pseudo_type":"Void", "op":"="},
                            "otherwise":{
                                "type":"assignment",
                                     "target": {"type":"local", "name": r["name"], "pseudo_type":t["pseudo_type"]},
                                     "value":r["value"]["otherwise"],"op":"=",
                                     "pseudo_type":"Void"                                
                            },
                            'pseudo_type': 'Void'
                            }
                    return [res1, res2]

                """if (t["pseudo_type"]!=r["value"]["pseudo_type"]) and (r["value"]["pseudo_type"]!="todooo") : 
                    raise type_check_error('bad declaration at line %s and column %s'%(location[0],location[1]))"""
            
            val = r["value"]
            if isinstance(t, dict):
                pseudo_type = t["pseudo_type"]
                type_ = t["type"]
            else:
                pseudo_type = val["pseudo_type"]
                type_ = val["pseudo_type"]
                
            res = {"type": type_, "name":r["name"], "value":val, "pseudo_type":pseudo_type}
            if res["value"] is None: del res["value"]
            z["decl"].append(res)
            self.type_env[str(res["name"])] = res["pseudo_type"]
            
        return z

    def visit_local_variable_declarator(self, node, identifier, local_variable_initializer, location):
        name = self.visit(identifier)
        return {"name":name, "value":self.visit(local_variable_initializer)}

    def visit_local_variable_initializer(self, node, expression,array_initializer,stackalloc_initializer,location):   
        if array_initializer: 
            z = self.visit(array_initializer)
            return z # {"type":"array", "value":z, "pseudo_type":["array","%s"%z[0]["pseudo_type"]]}
        if expression:
            return self.visit(expression)
        if stackalloc_initializer:
            print(f"stackalloc_initializer is not implemented at {location}")
    
    def visit_expression(self, node, assignment, non_assignment_expression, location):
        if non_assignment_expression:
            x = self.visit(non_assignment_expression)
            return  x[0] if isinstance(x, list) else x
        if assignment:
            return self.visit(assignment)
    
    def visit_assignment(self, node, unary_expression,assignment_operator,expression, location):
        if assignment_operator:
            self.assign= True
            z =  {
                    'type': 'assignment',
                    'target':self.visit(unary_expression),
                    'op':assignment_operator,
                    'value': self.visit(expression),
                    'pseudo_type': 'Void'
                }
            self.assign = False


            
            """r = z["value"]["pseudo_type"]
            if "Function" in z["value"]["pseudo_type"]:
                r = z["value"]["pseudo_type"][-1]

            if z["target"]["pseudo_type"]!="double" and z["target"]["pseudo_type"]!=r:
                jj = (z["target"]["pseudo_type"]!="double" and z["target"]["pseudo_type"]!=r)
                raise type_check_error(
                ' Cannot implicitly convert type %s from %s to %s at line %s. An explicit conversion exists (are you missing a cast11? %s)'%(z["target"]["name"],z["target"]["pseudo_type"], z["value"]["pseudo_type"], location[0], jj))"""
            return z
        
        else: 
            raise PseudoCythonTypeCheckError("Not yet implemented part of assignment , %s"%location)

    def visit_non_assignment_expression(self, 
                                        node, 
                                        lambda_expression,
                                        query_expression,
                                        conditional_expression,
                                        location):
        if  lambda_expression: raise PseudoCythonTypeCheckError("Not implemented lambda expression , %s"%location)  
        if  query_expression: raise PseudoCythonTypeCheckError("Not implemented query_expression , %s"%location)    
        return self.visit(conditional_expression)
    
    def visit_conditional_expression(self, node,null_coalescing_expression,throwable_expression, location):
        if null_coalescing_expression:
            res = self.visit(null_coalescing_expression)
        if throwable_expression:
            bodyif = self.visit(throwable_expression[0])
            bodyelse = self.visit(throwable_expression[1])
            res = {
                'type': 'cond_expr_node',
                'test': res,
                'true_val': bodyif,
                'pseudo_type': 'Void',
                'false_val': bodyelse
            }
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
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_conditional_or_expression(self,
                                        node, 
                                        conditional_and_expression,
                                        OP_OR,
                                        location):
        if len(node.children)==1:     
            return self.visit(conditional_and_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))


    def visit_tupleexpression(self, node, argument, location):
        res = []
        for arg in argument:
            z = self.visit(argument)
            res.append(z)
        return res


    def visit_inclusive_or_expression(self, node,
                                      exclusive_or_expression,
                                      BITWISE_OR,
                                      location):
        if len(node.children)==1:     
            return self.visit(exclusive_or_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(x, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_exclusive_or_expression(self, 
                                    node,
                                    and_expression,
                                    CARET,
                                    location):
        if len(node.children)==1:     
            return self.visit(and_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(x, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_and_expression(self, 
                            node,
                            equality_expression,
                            AMP,
                            location ):
        if len(node.children)==1:     
            return self.visit(equality_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(x, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_equality_expression(self, node, relational_expression, OP_EQ,OP_NE,location):
        if len(node.children)==1:     
            return self.visit(relational_expression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x[0], "right":y[0], "pseudo_type":"bool"}, list(args))

    def visit_relational_expression(self, node,shift_expression,LT, GT,OP_LE,OP_GE,IS,isType,AS,type_,location):
        if len(shift_expression)==1 and isType:
            left = self.visit(shift_expression)
            right = self.visit(isType)
            return {"type":"isExpression", "left": left, "right":right, "pseudo_type":"Void"}
        if len(shift_expression)==1 and AS:
            left = self.visit(shift_expression)
            right = self.visit(type_)
            return {"type":"isExpression", "left": left, "right":right, "pseudo_type":"Void"}
        if len(node.children)==1:
            return self.visit(shift_expression)
        else:
            args = map(lambda n:self.visit(n), node.children)   
            return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))
   
   
    def visit_istype(self, node, base_type, rank_specifier, isTypePatternArms, identifier, location):
        typ = self.visit(base_type)
        if identifier:
            return {"type":typ, "name":self.visit(identifier)}
        else:
            return {"type":typ, "pseudo_type":typ}
    
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

    def visit_unary_expression(self, node, primary_expression,PLUS,type_, BANG, MINUS,OP_INC,OP_DEC, unary_expression,STAR,TILDE, location):
        
        if primary_expression:
            z =  self.visit(primary_expression)
            return z
        if type_: 
            tp = self.visit(type_)
            receiver = self.visit(unary_expression)
            if receiver["pseudo_type"] != tp["type"]:
                return {"type":"standard_method_call", "message":tp["type"], "receiver":receiver, "pseudo_type":tp["pseudo_type"]}
            else: return receiver
        if unary_expression:
            if PLUS : op = PLUS
            elif MINUS : op = MINUS  
            elif OP_INC : op = OP_INC
            elif OP_DEC : op = OP_DEC
            elif BANG : op = "not"
            elif STAR: op = STAR
            elif TILDE: op = TILDE
            #else: raise PseudoCythonTypeCheckError("Not implemented unary operator , %s"%location)      
            z = self.visit(unary_expression)
            if op =="not": z["pseudo_type"] = "bool"
            res = {
                    'type': 'unary_op',
                            'operator': op,
                            'value': z,
                            'pseudo_type': z["pseudo_type"]
                }
            if op =="not" and z["type"]=="standard_method_call" and z["message"] == "contains?":
                z["message"] = "not contains?"
                return z
            return res

    def visit_returnstatement(self, node,expression,location):
        z = self.visit(expression)
        if z: return {'type': 'implicit_return', 
                'value':z , "pseudo_type":z["pseudo_type"]}
        else:
            return {'type': 'implicit_return', 
                'value':None , "pseudo_type":"Void"}
            
    
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
                raise PseudoCythonTypeCheckError("Not implemented OP_RANGE, %s"%location)

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

    def visit_primary_expression(self, node,primary_expression_start,OP_INC,BANG,OP_PTR,identifier, OP_DEC,member_access,method_invocation,bracket_expression, location ):
        res = self.visit(primary_expression_start)
        if BANG or OP_PTR or identifier:
            raise PseudoCythonTypeCheckError("Not implemented, %s"%location)
        if member_access:
            m = self.translate(member_access)
            if isinstance(res, str): res = {"type":"member_access", "name":res, "member":m, "pseudo_type":"unknown"}
            elif isinstance(res, dict) and "name" in res: res = {"type":"member_access", "name":res["name"], "member":m, "pseudo_type":res["pseudo_type"]}
            elif "class_type" in res: res = {"type":"member_access", "name":res["class_type"], "member":m, "pseudo_type":"unknown"}
            else: return None
            
            if res["name"] in CONSTANT_API and res["member"] in CONSTANT_API[res["name"]]:
                return CONSTANT_API.get(res["name"]).get(res["member"]) 
            
            receiver = res["pseudo_type"][0] if isinstance(res["pseudo_type"], list) else res["pseudo_type"]
            if isinstance(receiver, dict): receiver = receiver["pseudo_type"]
            if isinstance(receiver, list): 
                receiver = receiver[0] 
                m = res["member"]
            
            if receiver in PROPERTY_API and not method_invocation:
                rec = {"type":"local", "name": res["name"], "pseudo_type":res["pseudo_type"]}
                api = PROPERTY_API[receiver].get(m)      
                if not api:
                    raise translation_error('CyMLTx doesn\' t support property %s of %s' % (m, receiver),
                                                location, [location[0]],
                                                suggestions='CyMLTx supports those %s functions\n  %s' % (
                            receiver,
                            prepare_table(TYPED_API[receiver], ORIGINAL_METHODS.get(receiver)).strip()))

                elif not isinstance(api, dict):
                    z = api.expand([rec])
                    return z

        if method_invocation:
            args = self.visit(method_invocation)  
                   
            if member_access:
                member = self.visit(member_access)
                #print(member, "hhhhhh", location, m)
                if m.find(".") == -1:
                    method = m
                    receiver = res["name"]
                else:
                    method = m.split(".")[-1]
                    receiver = res["name"]+"."+".".join(m.split(".")[:-1])
                #print(receiver)
                receiver_type = self.type_env[receiver] 
                receiver_type = receiver_type[0] if isinstance(receiver_type, list) else receiver_type
                rec =  {"type":"local" , "name":receiver, "pseudo_type":self.type_env[receiver]}
                
                if isinstance(receiver_type, dict): receiver_type=receiver_type["typename"]
                #print(method, location, receiver, receiver_type)
                
                if receiver in FUNCTION_API:
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
                        if self.assign == False and res["message"] not in ("contains?", "index", "len"):
                            res = {"type": 'ExprStatNode', 'expr': res}
                    if not api:
                        raise translation_error('CyMLT doesn\' t support %s %s at line %s' % (receiver_type, method,location[0]),
                                                suggestions='CyMLT supports those %s functions\n  %s' % (
                          receiver, prepare_table(TYPED_API[receiver_type], ORIGINAL_METHODS.get(receiver_type)).strip()))
                

                else: 
                    res["member"] = receiver.split(".")[-1]
                    res = {'type': 'custom_call', 'namespace': res, "function":method, 'args': args, 'pseudo_type': "unknown", "class_": self.clas[-1]}      #TODO 
                    #if self.assign == False:
                            #res = {"type": 'ExprStatNode', 'expr': res}            
            else:
                if res in ("int", "float", "double", "ToInt32"):
                    if res == "ToInt32": res = "int"
                    if args[0]["pseudo_type"]!=res:
                        res = {'type': 'standard_method_call',
                                'receiver': args[0],
                                'args': [],
                                'message': res,
                                'pseudo_type': res}
                    else: res = args[0]
                   
                else:
                    fname = res["name"]
                    c = self.type_env.top['functions']
                    if fname in c:
                        pseudo_type = c[fname][-1]
                    else: pseudo_type="unknown"
                    res = {
                                "type": "custom_call",
                                "args": args,
                                "function": res["name"],
                                "pseudo_type":pseudo_type,
                            }   ####Todooooooo
                    
        
        if bracket_expression:
            t = self.visit(bracket_expression)
            res = {'type': 'index',
                    'sequence': res,
                    'index': t,
                    'pseudo_type': res["pseudo_type"][1] if isinstance(res["pseudo_type"], list) else res["pseudo_type"]
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


    
    def visit_baseaccessexpression(self, node,identifier, type_argument_list, expression_list , location):
        return {
                "type":"baseaccess",
                "class_type":"base",
                "name": self.visit(identifier),
                "args": self.visit(type_argument_list) if type_argument_list else []
            
        }
    
    
    
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
   
    def visit_bracket_expression(self, node,indexer_argument, location):
        if len(indexer_argument) ==1:
            k = self.visit(indexer_argument)
            return  k
        else: raise PseudoCythonTypeCheckError("Not implemented bracket expression , %s"%location[0])
        return
    

      
    def visit_simplenameexpression(self, node,identifier,type_argument_list, location):
        id_type = self.type_env.top[self.visit(identifier)]
        if id_type is None:
            self.non_identifier.append(self.visit(identifier))
            """ raise type_check_error(
                '%s is not defined at line %s and column %s' %(str(identifier), location[0], location[1]))""" # remove cote
        return {"type":"local", "name": self.visit(identifier), "pseudo_type":id_type}

    def visit_member_access(self, node,identifier, type_argument_list,DOT,INTERR, location):
        if type_argument_list: raise PseudoCythonTypeCheckError("Not implemented type_argument_list , %s"%location)
        res = self.visit(identifier)
        return res
    
    def visit_method_invocation(self, node,argument_list, location):
        return self.visit(argument_list)
    
    def visit_argument(self, node, location, type_, identifier, expression):

        r =  self.visit(expression)
        if type_:   
            r2 = self.visit(type_)
            op = str(r["operator"]) if "operator" in r else str(r2["operator"])
            right =  r["value"] if "value" in r else r
            left = {"type":"local", "name":r2["type"], "pseudo_type":self.type_env.top[r2["type"]]}
            return {"type":"binary_op",
                        "left":left,
                        "op": op,
                        "right":right,
                        "pseudo_type": TYPED_API['operators'][op](
                    left['pseudo_type'], r['pseudo_type'])[-1]}
        else:
            return r



    def visit_literalexpression(self, node,literal,location):
        return self.visit(literal)

    def visit_literal(self, node,boolean_literal,string_literal,INTEGER_LITERAL,REAL_LITERAL,CHARACTER_LITERAL,NULL,location):
        if boolean_literal: return {'type': 'bool', 'value': self.visit(boolean_literal), 'pseudo_type': 'bool'}
        if INTEGER_LITERAL: return {'type': 'int', 'value': self.visit(INTEGER_LITERAL), 'pseudo_type': 'int'}
        if REAL_LITERAL: 
            val = self.visit(REAL_LITERAL)
            if val.endswith("d"): return {'type': 'double', 'value': val[:-1], 'pseudo_type': 'double'}
            else: return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        if CHARACTER_LITERAL: 
            return {'type': 'char', 'value': str(self.visit(CHARACTER_LITERAL)), 'pseudo_type': 'char'}

        if string_literal: 
            val = str(string_literal)
            if '"' in val:
                val = val.replace('"', '')
                val = val.encode('utf-8')
            return {'type': 'string', 'value': val, 'pseudo_type': 'string'}
        if NULL:
            return {'type':"none", "value":"none", "pseudo_type":"none"}
  

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
        if expr["op"] in ["<", ">", '!=']:
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
            if r["op"]!="=": res["step"] = r["value"]
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

    def visit_parenthesisexpressions(self, node,expression, location):
        z = self.visit(expression)
        return z
    
    def visit_trystatement(self, node, TRY, block,catch_clauses, finally_clause, location):
        return

    """def visit_throwstatement(self, node, THROW, expression,SEMICOLON, location):
        return {"type":"throwstatement", 
                "exception": self.visit(expression) if expression else None,
                'pseudo_type': 'Void'}"""
    def visit_fixed_parameter(self, node, attributes, parameter_modifier, arg_declaration, ARGLIST, location):
        if arg_declaration: args = self.visit(arg_declaration)
        else: args = self.visit(ARGLIST)
        return args
    
    def visit_continuestatement(self, node, CONTINUE, SEMICOLON, location):
        return {
            "type": "continuestatnode"
        }
    
    def visit_enum_member_declaration(self, node, attributes, identifier, expression, location):
        value = None
        id = self.visit(identifier)
        if expression:
            value = self.visit(expression)
            pseudo_type =  value["pseudo_type"]
        else: pseudo_type = "string"
        
        res = {'type':"local", "name":id, "pseudo_type": pseudo_type}
        
        if value: res["value"] =  value
        return res

