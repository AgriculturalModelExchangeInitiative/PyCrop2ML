from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.errors import *
from pycropml.transpiler.antlr_py.java.builtin_typed_api import *
from pycropml.transpiler.antlr_py.java.api_transform import *
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

class CompilationUnit(AliasNode):
    _fields_spec = ["packageDeclaration", "importDeclaration", "typeDeclaration"]

class ImportDeclaration(AliasNode):
    _fields_spec = ["singleTypeImportDeclaration","typeImportOnDemandDeclaration","singleStaticImportDeclaration", "staticImportOnDemandDeclaration"]

class  PackageDeclaration(AliasNode):
    _fields_spec = ["packageModifier", "package","packageName"]
    
class TypeDeclaration(AliasNode):
    _fields_spec = ["classDeclaration", "interfaceDeclaration" ]

class ClassDeclaration(AliasNode):
    _fields_spec = ["normalClassDeclaration", "enumDeclaration"]

class NormalClassDeclaration(AliasNode):
    _fields_spec = ["classModifier", "Identifier", "typeParameters", "superclass", "superinterfaces", "classBody"]

class ClassBody(AliasNode):
    _fields_spec =["classBodyDeclaration"]

class ClassBodyDeclaration(AliasNode):
    _fields_spec = ["classMemberDeclaration", "instanceInitializer","staticInitializer","constructorDeclaration"]

class ClassMemberDeclaration(AliasNode):
    _fields_spec = ["fieldDeclaration", "methodDeclaration", "classDeclaration", "interfaceDeclaration"]

class FieldDeclaration(AliasNode):
    _fields_spec = ["fieldModifier", "unannType", "variableDeclaratorList"]

class UnannType(AliasNode):
    _fields_spec = ["unannPrimitiveType","unannReferenceType"]

class UnannPrimitiveType(AliasNode):
    _fields_spec = ["numericType"]

class PrimitiveType(AliasNode):
    _fields_spec = ["numericType","annotation", "BOOLEAN"]

class UnannReferenceType(AliasNode):
    _fields_spec = ["unannClassOrInterfaceType", "unannTypeVariable", "unannArrayType"]

class UnannClassOrInterfaceType(AliasNode):
    _fields_spec = ["unannClassType_lfno_unannClassOrInterfaceType","unannInterfaceType_lfno_unannClassOrInterfaceType","unannClassType_lf_unannClassOrInterfaceType", "unannInterfaceType_lf_unannClassOrInterfaceType"]

class UnannClassType_lfno_unannClassOrInterfaceType(AliasNode):
    _fields_spec = ["Identifier", "typeArguments"]

class TypeArguments(AliasNode):
    _fields_spec = ["typeArgumentList"]

class TypeArgumentList(AliasNode):
    _fields_spec = ["typeArgument"]

class TypeArgument(AliasNode):
    _fields_spec = ["referenceType", "wildcard"]

class ReferenceType(AliasNode):
    _fields_spec = ["classOrInterfaceType", "typeVariable", "arrayType"]

class ArrayType(AliasNode):
    _fields_spec = ["primitiveType", "classOrInterfaceType","typeVariable"]

class ClassOrInterfaceType(AliasNode):
    _fields_spec = ["classType_lfno_classOrInterfaceType","interfaceType_lfno_classOrInterfaceType","classType_lf_classOrInterfaceType","interfaceType_lf_classOrInterfaceType"]

class ClassType_lfno_classOrInterfaceType(AliasNode):
    _fields_spec = ["annotation", "Identifier", "typeArguments"]  

class MethodDeclaration(AliasNode):
    _fields_spec = ["methodModifier", "methodHeader", "methodBody"]

class MethodHeader(AliasNode):
    _fields_spec = ["result", "methodDeclarator", "throws_","typeParameters", "annotation"]

class MethodDeclarator(AliasNode):
    _fields_spec = ["Identifier", "formalParameterList","dims"]

class FormalParameterList(AliasNode):
    _fields_spec = ["receiverParameter","formalParameters", "lastFormalParameter"]

class FormalParameters(AliasNode):
    _fields_spec = ["formalParameter", "receiverParameter"]

class FormalParameter(AliasNode):
    _fields_spec =  ["variableModifier", "unannType", "variableDeclaratorId"]

class LastFormalParameter(AliasNode):
    _fields_spec = ["variableModifier", "unannType", "annotation", "variableDeclaratorId","formalParameter"]

class MethodBody(AliasNode):
    _fields_spec =["block"]

class Block(AliasNode):
    _fields_spec = ["blockStatements"]

class BlockStatements(AliasNode):
    _fields_spec = ["blockStatement"]

class BlockStatement(AliasNode):
    _fields_spec = ["localVariableDeclarationStatement","classDeclaration","statement"]

class LocalVariableDeclarationStatement(AliasNode):
    _fields_spec = ["localVariableDeclaration"]

class LocalVariableDeclaration(AliasNode):
    _fields_spec = ["variableModifier", "unannType", "variableDeclaratorList"]

class VariableDeclaratorList(AliasNode):
    _fields_spec = ["variableDeclarator"]

class VariableDeclarator(AliasNode):
    _fields_spec = ["variableDeclaratorId", "variableInitializer"]
    
class VariableInitializer(AliasNode):
    _fields_spec = ["expression", "arrayInitializer"]

class Expression(AliasNode):
    _fields_spec = ["lambdaExpression","assignmentExpression"]

class AssignmentExpression(AliasNode):
    _fields_spec = ["conditionalExpression", "assignment"]

class ConditionalExpression(AliasNode):
    _fields_spec = ["conditionalOrExpression", "expression","conditionalExpression"]

class ConditionalOrExpression(AliasNode):
    _fields_spec = ["conditionalAndExpression","conditionalOrExpression", "OR"]

class ConditionalAndExpression(AliasNode):
    _fields_spec = ["inclusiveOrExpression","conditionalAndExpression", "AND"]

class InclusiveOrExpression(AliasNode):
    _fields_spec = ["exclusiveOrExpression","inclusiveOrExpression", "BITOR"]

class ExclusiveOrExpression(AliasNode):
    _fields_spec = ["andExpression","exclusiveOrExpression", "CARET"]

class AndExpression(AliasNode):
    _fields_spec = ["equalityExpression", "andExpression", "BITAND"]

class EqualityExpression(AliasNode):
    _fields_spec = ["relationalExpression","equalityExpression", "EQUAL", "NOTEQUAL"]

class RelationalExpression(AliasNode):
    _fields_spec = ["shiftExpression","relationalExpression", 'LT', 'GT', 'LE','GE', "INSTANCEOF", "referenceType"]

class ShiftExpression(AliasNode):
    _fields_spec = ["additiveExpression", "shiftExpression", "LT", "GT"]

class AdditiveExpression(AliasNode):
    _fields_spec = ["multiplicativeExpression", "additiveExpression", "ADD", "SUB"]

class MultiplicativeExpression(AliasNode):
    _fields_spec = ["unaryExpression", "multiplicativeExpression", "MUL", "DIV", "MOD"]

class UnaryExpression(AliasNode):
    _fields_spec = ["preIncrementExpression","preDecrementExpression","unaryExpression","unaryExpressionNotPlusMinus", "ADD", "SUB"]

class PreIncrementExpression(AliasNode):
    _fields_spec = ["unaryExpression" ]

class PreDecrementExpression(AliasNode):
    _fields_spec = ["unaryExpression" ]

class UnaryExpressionNotPlusMinus(AliasNode):
    _fields_spec = ["postfixExpression", "unaryExpression", "castExpression", "TILDE","BANG" ]

class PostfixExpression(AliasNode):
    _fields_spec = ["primary", "expressionName", "postIncrementExpression_lf_postfixExpression", "postDecrementExpression_lf_postfixExpression"]

class PostIncrementExpression(AliasNode):
    _fields_spec = ["postfixExpression"]

class PostDecrementExpression(AliasNode):
    _fields_spec = ["postfixExpression"]

class CastExpression(AliasNode):
    _fields_spec = ["primitiveType", "unaryExpression","referenceType", "additionalBound","unaryExpressionNotPlusMinus", "lambdaExpression", "LPAREN", "RPAREN"]

class PrimaryNoNewArray_lfno_primary(AliasNode):
    _fields_spec = ["literal","typeName","unannPrimitiveType","void","this","expression","classInstanceCreationExpression_lfno_primary","fieldAccess_lfno_primary","arrayAccess_lfno_primary","methodInvocation_lfno_primary","methodReference_lfno_primary", "THIS"]

class Literal(AliasNode):
    _fields_spec =["IntegerLiteral","FloatingPointLiteral","BooleanLiteral","CharacterLiteral","StringLiteral","NullLiteral"]

class MethodInvocation_lfno_primary(AliasNode):
    _fields_spec = ["methodName", "argumentList","typeName","typeArguments","Identifier","expressionName"]
        
class Statement(AliasNode):
    _fields_spec = ["statementWithoutTrailingSubstatement","labeledStatement","ifThenStatement","ifThenElseStatement","whileStatement","forStatement"]
    
class Assignment(AliasNode):
    _fields_spec= ["leftHandSide", "assignmentOperator", "expression"] 

class LeftHandSide (AliasNode):
    _fields_spec= ["expressionName","fieldAccess","arrayAccess"]

class ExpressionStatement(AliasNode):
    _fields_spec= ["statementExpression"]

class StatementExpression(AliasNode):
    _fields_spec= ["assignment","preIncrementExpression","preDecrementExpression","postIncrementExpression","postDecrementExpression","methodInvocation","classInstanceCreationExpression"]

class ExpressionName(AliasNode):
    _fields_spec= ["Identifier","ambiguousName", "DOT"]

class StatementWithoutTrailingSubstatement(AliasNode):
    _fields_spec= ["block","emptyStatement","expressionStatement","assertStatement","switchStatement","doStatement","breakStatement",	"continueStatement",	"returnStatement","synchronizedStatement",	"throwStatement",	"tryStatement"]
    
class MethodInvocation(AliasNode):
    _fields_spec= ["methodName", "argumentList","typeName","typeArguments","Identifier","expressionName"]  

class ArgumentList(AliasNode):
    _fields_spec= ["expression"]        
        
class ReturnStatement(AliasNode):
    _fields_spec = ["expression"]  

class ClassInstanceCreationExpression_lfno_primary(AliasNode):
    _fields_spec = ["typeArguments","annotation","Identifier","typeArgumentsOrDiamond","argumentList","classBody","expressionName"] 
    
class UnannArrayType(AliasNode):
    _fields_spec = ["unannPrimitiveType","unannClassOrInterfaceType","unannTypeVariable"]   
    
class ArrayAccess_lfno_primary(AliasNode):
    _fields_spec = ["expressionName","expression","primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary","primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary"]
   
class ArrayAccess(AliasNode):
    _fields_spec = ["expressionName","expression","primaryNoNewArray_lf_arrayAccess","primaryNoNewArray_lfno_arrayAccess"]

   
class ArrayCreationExpression(AliasNode):
    _fields_spec = ["primitiveType", "dimExprs","dims","classOrInterfaceType","arrayInitializer"]

class DimExprs(AliasNode):
    _fields_spec = ["dimExpr"]

class BasicForStatement(AliasNode):
    _fields_spec =["forInit","expression","forUpdate","statement"]

class WhileStatement(AliasNode):
    _fields_spec =["expression", "statement"]

class StatementNoShortIf(AliasNode):
    _fields_spec =[ "statementWithoutTrailingSubstatement", "labeledStatementNoShortIf", "ifThenElseStatementNoShortIf", "whileStatementNoShortIf","forStatementNoShortIf"]
 
 
class ArrayInitializer(AliasNode):
    _fields_spec =[ "variableInitializerList"]

class VariableInitializerList(AliasNode):
    _fields_spec =[ "variableInitializer"]

class MethodInvocation_lf_primary(AliasNode):
    _fields_spec =["typeArguments", "Identifier", "argumentList"]
                   
class Transformer(BaseNodeTransformer):
    def visit_CompilationUnit(self, node):
        return CompilationUnit.from_spec(node)
    
    def visit_PackageDeclaration(self, node):
        return PackageDeclaration.from_spec(node)

    def visit_ImportDeclaration(self, node):
        return ImportDeclaration.from_spec(node)
    
    def visit_TypeDeclaration(self, node):
        return TypeDeclaration.from_spec(node)
    
    def visit_ClassDeclaration(self, node):
        return ClassDeclaration.from_spec(node)
    
    def visit_NormalClassDeclaration(self, node):
        return NormalClassDeclaration.from_spec(node)
  
    def visit_ClassBody(self, node):
        return ClassBody.from_spec(node)
    
    def visit_ClassBodyDeclaration(self, node):
        return ClassBodyDeclaration.from_spec(node)
    
    def visit_ClassMemberDeclaration(self, node):
        return ClassMemberDeclaration.from_spec(node)
    
    def visit_FieldDeclaration(self, node):
        return FieldDeclaration.from_spec(node)
    
    def visit_UnannType(self, node):
        return UnannType.from_spec(node)

    def visit_UnannPrimitiveType(self, node):
        return UnannPrimitiveType.from_spec(node)

    def visit_PrimitiveType(self, node):
        return PrimitiveType.from_spec(node)
    
    def visit_UnannReferenceType(self, node):
        return UnannReferenceType.from_spec(node)
    
    def visit_UnannClassOrInterfaceType(self, node):
        return UnannClassOrInterfaceType.from_spec(node)
    
    def visit_UnannClassType_lfno_unannClassOrInterfaceType(self, node):
        return UnannClassType_lfno_unannClassOrInterfaceType.from_spec(node)

    def visit_TypeArguments(self, node):
        return TypeArguments.from_spec(node)    

    def visit_TypeArgumentList(self, node):
        return TypeArgumentList.from_spec(node)

    def visit_TypeArgument(self, node):
        return TypeArgument.from_spec(node)
    
    def visit_ReferenceType(self, node):
        return ReferenceType.from_spec(node)
    
    def visit_ClassOrInterfaceType(self, node):
        return ClassOrInterfaceType.from_spec(node)
    
    def visit_ClassType_lfno_classOrInterfaceType(self, node):
        return ClassType_lfno_classOrInterfaceType.from_spec(node)

    def visit_MethodDeclaration(self, node):
        return MethodDeclaration.from_spec(node)
    
    def visit_MethodHeader(self, node):
        return MethodHeader.from_spec(node)

    def visit_MethodDeclarator(self,node):
        return MethodDeclarator.from_spec(node)
    
    def visit_UnannArrayType(self, node):
        return UnannArrayType.from_spec(node)

    def visit_FormalParameterList(self,node):
        return FormalParameterList.from_spec(node)
    
    def visit_FormalParameters(self,node):
        return FormalParameters.from_spec(node)

    def visit_FormalParameter(self,node):
        return FormalParameter.from_spec(node)
    
    def visit_LastFormalParameter(self, node):
        return LastFormalParameter.from_spec(node)

    def visit_MethodBody(self, node):
        return MethodBody.from_spec(node)

    def visit_Block(self, node):
        return Block.from_spec(node)

    def visit_BlockStatements(self, node):
        return BlockStatements.from_spec(node)

    def visit_BlockStatement(self, node):
        return BlockStatement.from_spec(node)

    def visit_LocalVariableDeclarationStatement(self, node):
        return LocalVariableDeclarationStatement.from_spec(node)

    def visit_LocalVariableDeclaration(self, node):
        return LocalVariableDeclaration.from_spec(node)

    def visit_VariableDeclaratorList(self, node):
        return VariableDeclaratorList.from_spec(node)

    def visit_VariableDeclarator(self, node):
        return VariableDeclarator.from_spec(node)

    def visit_VariableInitializer(self, node):
        return VariableInitializer.from_spec(node)

    def visit_Expression(self, node):
        return Expression.from_spec(node)

    def visit_AssignmentExpression(self, node):
        return AssignmentExpression.from_spec(node)

    def visit_ConditionalExpression(self, node):
        return ConditionalExpression.from_spec(node)

    def visit_ConditionalOrExpression(self, node):
        return ConditionalOrExpression.from_spec(node)

    def visit_ConditionalAndExpression(self, node):
        return ConditionalAndExpression.from_spec(node)

    def visit_InclusiveOrExpression(self, node):
        return InclusiveOrExpression.from_spec(node)

    def visit_ExclusiveOrExpression(self, node):
        return ExclusiveOrExpression.from_spec(node)

    def visit_AndExpression(self, node):
        return AndExpression.from_spec(node)

    def visit_EqualityExpression(self, node):
        return EqualityExpression.from_spec(node)

    def visit_RelationalExpression(self, node):
        return RelationalExpression.from_spec(node)

    def visit_ShiftExpression(self, node):
        return ShiftExpression.from_spec(node)

    def visit_AdditiveExpression(self, node):
        return AdditiveExpression.from_spec(node)

    def visit_MultiplicativeExpression(self, node):
        return MultiplicativeExpression.from_spec(node)

    def visit_UnaryExpression(self, node):
        return UnaryExpression.from_spec(node)

    def visit_PreIncrementExpression(self, node):
        return PreIncrementExpression.from_spec(node)

    def visit_PreDecrementExpression(self, node):
        return PreDecrementExpression.from_spec(node)

    def visit_UnaryExpressionNotPlusMinus(self, node):
        return UnaryExpressionNotPlusMinus.from_spec(node)

    def visit_PostfixExpression(self, node):
        return PostfixExpression.from_spec(node)

    def visit_PostIncrementExpression(self, node):
        return PostIncrementExpression.from_spec(node)

    def visit_PostDecrementExpression(self, node):
        return PostDecrementExpression.from_spec(node)

    def visit_CastExpression(self, node):
        return CastExpression.from_spec(node)
    
    def visit_PrimaryNoNewArray_lfno_primary(self, node):
        return PrimaryNoNewArray_lfno_primary.from_spec(node)
    
    def visit_Literal(self, node):
        return Literal.from_spec(node)
    
    def visit_MethodInvocation_lfno_primary(self, node):
        return MethodInvocation_lfno_primary.from_spec(node)

    def visit_Statement(self, node):
        return Statement.from_spec(node)
        
    def visit_Assignment(self, node):
        return Assignment.from_spec(node)

    def visit_LeftHandSide(self, node):
        return LeftHandSide.from_spec(node)
    
    def visit_ExpressionStatement(self, node):
        return ExpressionStatement.from_spec(node)
    
    def visit_ExpressionName(self, node):
        return ExpressionName.from_spec(node)
    
    def visit_StatementWithoutTrailingSubstatement(self, node):
        return StatementWithoutTrailingSubstatement.from_spec(node)
    
    def visit_StatementExpression(self, node):
        return StatementExpression.from_spec(node)
    
    def visit_MethodInvocation(self, node):
        return MethodInvocation.from_spec(node)
    
    def visit_ReturnStatement(self, node):
        return ReturnStatement.from_spec(node)

    def visit_ClassInstanceCreationExpression_lfno_primary(self, node):
        return ClassInstanceCreationExpression_lfno_primary.from_spec(node)
    
    def visit_ArgumentList(self, node):
        return ArgumentList.from_spec(node)
    
    def visit_ArrayType(self, node):
        return ArrayType.from_spec(node)
    
    def visit_ArrayAccess_lfno_primary(self, node):
        return ArrayAccess_lfno_primary.from_spec(node)

    def visit_ArrayAccess(self, node):
        return ArrayAccess.from_spec(node)

    def visit_ArrayCreationExpression(self, node):
        return ArrayCreationExpression.from_spec(node)
    
    def visit_DimExprs(self, node):
        return DimExprs.from_spec(node)
    
    def visit_BasicForStatement(self, node):
        return BasicForStatement.from_spec(node)

    def visit_WhileStatement(self, node):
        return WhileStatement.from_spec(node)
    
    def visit_StatementNoShortIf(self, node):
        return StatementNoShortIf.from_spec(node)

    def visit_ArrayInitializer(self, node):
        return ArrayInitializer.from_spec(node)

    def visit_VariableInitializerList(self, node):
        return VariableInitializerList.from_spec(node)

    def visit_MethodInvocation_lf_primary(self, node):
        return MethodInvocation_lf_primary.from_spec(node)
    
class AstTransformer():
    def __init__(self, tree, code :str = None ,comments: str=None, env=None):
        self.tree = tree
        self.base = 0
        self.code=code
        self.type_env = Env(dict(list(TYPED_API.items())), None)
        self.comments = comments

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
            comment = []       
            if x:
                fields['location'] = x["line_start"],x["column_start"]
                while self.comments and x["line_start"] >= list(self.comments.keys())[0]:
                    comment.append(list(self.comments.values())[0].encode("utf-8"))
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
    
   
    def visit_compilationunit(self, node, packageDeclaration, importDeclaration, typeDeclaration, location, comments):
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
                "pseudo_type": "Void",
                "comments":comments}
    
    def visit_packagedeclaration(self, node, packageModifier, package,packageName ,location, comments):
        print(f"packagedeclaration not implemented {location}")
    
    def visit_importdeclaration(self, node, singleTypeImportDeclaration,typeImportOnDemandDeclaration,singleStaticImportDeclaration,staticImportOnDemandDeclaration,location, comments):
        pass
    
    def visit_typedeclaration(self, node,classDeclaration,interfaceDeclaration,location,comments):
        res = None
        if classDeclaration:
            res = self.visit(classDeclaration)
        if comments: res["comments"] = comments
        return res 
    
    def visit_classdeclaration(self, node,normalClassDeclaration, enumDeclaration, location,comments):
        if normalClassDeclaration:
            return self.visit(normalClassDeclaration)
    
    def visit_normalclassdeclaration(self, node,classModifier, Identifier, typeParameters, superclass, superinterfaces, classBody, location,comments):
        return  {"type":"classDef",
                 "base": None, # TODO
                "name": Identifier,
                "block": self.visit(classBody),
                "comments":comments}

    def visit_classbody(self, node, classBodyDeclaration, location,comments):
        res = self.visit(classBodyDeclaration)
        if comments: res["comments"] = comments
        return res
        
    
    def visit_classbodydeclaration(self, node,classMemberDeclaration,instanceInitializer,staticInitializer,constructorDeclaration,location,comments):
        if classMemberDeclaration:
            res = self.visit(classMemberDeclaration)
            if comments: res["comments"] = comments
            return res
        if instanceInitializer: print(f"instanceInitializer not implemented at {location}")
        if staticInitializer: print(f"staticInitializer not implemented at {location}")
    
    def visit_classmemberdeclaration(self, node,fieldDeclaration,methodDeclaration,classDeclaration,interfaceDeclaration, location,comments):
        if fieldDeclaration:
            res = self.visit(fieldDeclaration)
        if methodDeclaration:
            res = self.visit(methodDeclaration)
        if comments: res["comments"] = comments
        return res
    
    def visit_fielddeclaration(self, node,fieldModifier, unannType ,variableDeclaratorList, location,comments):
        typ = self.visit(unannType)
        pseudo_type = typ
        if isinstance(typ, list): 
            typ = typ[0]
        varlist = self.visit(variableDeclaratorList)
        z = {}
        z["type"] = "declaration"
        z["decl"] = []
        for d in varlist:
            s = {"type":typ, "name":d["id"], "pseudo_type":pseudo_type}
            if "value" in d: s["value"] = d["value"]
            self.type_env.top[d["id"]] = pseudo_type
            z["decl"].append(s) 
        z["comments"] = comments  
        return z
    
    def visit_methoddeclaration(self, node, methodModifier, methodHeader, methodBody, location,comments):
        self.decl = []
        self.for_range_index = []
        met_header = self.visit(methodHeader) # dict "typ" for return type, "id" for method name and "args" for arguments
        met_body = self.visit(methodBody)
        ps = [p["pseudo_type"] for p in met_header["args"]] if met_header["args"] else [None]
        res = {"type":"methodDef",  
                "name":met_header["name"],
                "return_type" :met_header["typ"],
                "params":met_header["args"],
                "block":met_body,
                "pseudo_type":["function"] + ps + [met_header["typ"]],
                "comments":comments}
        self.type_env.top["functions"][met_header["name"]] = [met_header["typ"]] 
        return res
        
        """
                    self.function_name = self.visit(method_declaration.method_member_name)[0]
            param = self.visit(method_declaration.formal_parameter_list)
            ps = [p["pseudo_type"] for p in param] if param else [None]
            res = {"type":"methodDef",  
                    "name":self.function_name,
                    "return_type" :typ["pseudo_type"],
                    "params":param,
                    "block":self.visit(methodBody),
                    "pseudo_type":["function"] + ps + [typ["pseudo_type"]]}
            #domain = [a["pseudo_type"] for a in res["params"] if res["params"] ]
            self.type_env.top["functions"][res["name"]] = [res["return_type"]]
        
        """

    def visit_methodheader(self, node, result, methodDeclarator, throws_,typeParameters, annotation, location,comments):
        return_type = self.visit(result)  # return type of method
        methdecl = self.visit(methodDeclarator)  # a dict "id" for method name and "args" for arguments
        methdecl["typ"] = return_type
        return methdecl
        """if typeParameters:
            tparams = self.visit(typeParameters)
            print(f"methodheader not yet implemented {location}")"""
    

    def visit_methoddeclarator(self, node,Identifier, formalParameterList,dims, location,comments):
        res = {}
        res["name"] = self.visit(Identifier) #method name
        if formalParameterList:            # method arguments
            res["args"] = self.visit(formalParameterList)
            if dims:
                print(f"dims Not Implemented {location}")
        else: res["args"] = []
        return res
    
    def visit_formalparameterlist(self, node,receiverParameter,formalParameters, lastFormalParameter, location,comments):
        if receiverParameter:
            print(f"receiverParameter Not Implemented {location}")
        elif formalParameters:
            res1 = self.visit(formalParameters)
            res2 = self.visit(lastFormalParameter)
            return res1+res2
        else:
            return self.visit(lastFormalParameter)

            
    
    def visit_formalparameters(self, node, formalParameter, receiverParameter, location,comments):
        if receiverParameter:
            print(f"receiverParameter Not Implemented {location}")
        else:
            res = []
            if isinstance(formalParameter, list):
                for arg in formalParameter:
                    res.append(self.visit(arg))
                return res
            else: return [self.visit(formalParameter)]
    
    def visit_formalparameter(self, node,variableModifier, unannType, variableDeclaratorId, location,comments):
        typ = self.visit(unannType)
        name = self.visit(variableDeclaratorId)
        z= {"type":typ[0] if isinstance(typ, list) else typ,"name":name, "pseudo_type":typ}
        self.type_env[name]=z["pseudo_type"]
        return z
    
    def visit_lastformalparameter(self, node, variableModifier,unannType, annotation,formalParameter,variableDeclaratorId,location,comments):
        if formalParameter:
            return [self.visit(formalParameter)]
        else:
            print(f"lastFormalParameter Not Implemented {location}")
    
    def visit_methodbody(self, node, block, location,comments):
        res = self.visit(block)
        if comments: res["comments"] = comments
        return res

    def visit_block(self, node,blockStatements, location,comments):
        res = self.visit(blockStatements)
        return res

    def visit_blockstatements(self, node,blockStatement, location,comments):
        res = []
        for j in blockStatement:
            res.append(self.visit(j))  
        if comments: res.insert(0,{"type":"comments", "comments": comments})
        return res

    def visit_blockstatement(self, node, localVariableDeclarationStatement,classDeclaration,statement, location,comments):
        if localVariableDeclarationStatement: res = self.visit(localVariableDeclarationStatement)
        if classDeclaration: res = self.visit(classDeclaration)
        if statement: 
            res = self.visit(statement)
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res

    def visit_localvariabledeclarationstatement(self, node, localVariableDeclaration, location,comments):
        return self.visit(localVariableDeclaration)

    def visit_localvariabledeclaration(self, node, variableModifier, unannType, variableDeclaratorList, location,comments):
        typ = self.visit(unannType)
        pseudo_type = typ
        if isinstance(typ, list): 
            typ = typ[0]
        varlist = self.visit(variableDeclaratorList)
        z = {}
        z["type"] = "declaration"
        z["decl"] = []
        for d in varlist:
            s = {"type":typ, "name":d["id"], "pseudo_type":pseudo_type}
            if "value" in d: 
                if d["value"]["type"] == "array": 
                    if "dim" in d["value"]: s["dim"] = d["value"]["dim"] 
                    if "elts" in d["value"]: s["elts"] = d["value"]["elts"]
                    if "init" in d["value"]: s["init"] = d["value"]["init"]
                else: 
                    s["value"] = d["value"]
            self.type_env.top[d["id"]] = pseudo_type
            z["decl"].append(s)   
        z["comments"] = comments
        return z

    def visit_variabledeclaratorlist(self, node, variableDeclarator, location,comments):
        res = self.visit(variableDeclarator)
        return res

    def visit_variabledeclarator(self, node, variableDeclaratorId, variableInitializer, location,comments):
        res =  {"id": self.visit(variableDeclaratorId)}
        if variableInitializer:
            res["value"] = self.visit(variableInitializer)
        return res

    def visit_variableinitializer(self, node,expression, arrayInitializer, location,comments):
        if expression:
            return self.visit(expression)
        else:
            return self.visit(arrayInitializer)

    def visit_expression(self, node, lambdaExpression,assignmentExpression, location,comments):
        if lambdaExpression:
            res = self.visit(lambdaExpression)
        else:
            res = self.visit(assignmentExpression)
        if comments: res["comments"] = comments
        return res

    def visit_assignmentexpression(self, node,conditionalExpression, assignment, location,comments):
        if conditionalExpression : res = self.visit(conditionalExpression)
        else: res = self.visit(assignment)
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res

    def visit_conditionalexpression(self, node, conditionalOrExpression, expression,conditionalExpression, location,comments):
        if conditionalOrExpression:
            return self.visit(conditionalOrExpression)
        else:
            print(f"conditionalexpression Not Implemented at %s"%location)

    def visit_conditionalorexpression(self, node,conditionalAndExpression,conditionalOrExpression,OR,location,comments):
        if len(node.children)==1: 
            return self.visit(conditionalAndExpression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_conditionalandexpression(self, node,inclusiveOrExpression,conditionalAndExpression,AND, location,comments):
        if len(node.children)==1:     
            return self.visit(inclusiveOrExpression)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_inclusiveorexpression(self, node,exclusiveOrExpression,inclusiveOrExpression,BITOR, location,comments):
        if len(node.children)==1:     
            return self.visit(exclusiveOrExpression)
        args = map(lambda n:self.visit(n), node.children)   
        args = [arg[0] if isinstance(arg, list) else arg for arg in args] 
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))

    def visit_exclusiveorexpression(self, node,andExpression,exclusiveOrExpression,CARET, location,comments):
        if len(node.children)==1:     
            return self.visit(andExpression)
        args = map(lambda n:self.visit(n), node.children)  
        args = [arg[0] if isinstance(arg, list) else arg for arg in args]  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))

    def visit_andexpression(self, node,equalityExpression, andExpression,BITAND, location,comments):
        if len(node.children)==1:     
            return self.visit(equalityExpression)
        args = map(lambda n:self.visit(n), node.children) 
        args = [arg[0] if isinstance(arg, list) else arg for arg in args]   
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))

    def visit_equalityexpression(self, node,relationalExpression,equalityExpression, EQUAL,NOTEQUAL,location,comments):
        if len(node.children)==1:     
            return self.visit(relationalExpression)
        args = map(lambda n:self.visit(n), node.children)  
        args = [arg[0] if isinstance(arg, list) else arg for arg in args]  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))

    def visit_relationalexpression(self, node,shiftExpression,relationalExpression,LT, GT, LE,GE,INSTANCEOF,referenceType, location,comments):
        if len(node.children)==1:
            return self.visit(shiftExpression)
        else:
            args = map(lambda n:self.visit(n), node.children)   
            args = [arg[0] if isinstance(arg, list) else arg for arg in args] 
            return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x, "right":y, "pseudo_type":"bool"}, list(args))
    
    def visit_shiftexpression(self, node,additiveExpression, shiftExpression, LT,GT,location,comments):
        if len(node.children)==1:
            return self.visit(additiveExpression)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            args = [arg[0] if isinstance(arg, list) else arg for arg in args]   
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x, "right":y}, list(args))
    
    def visit_additiveexpression(self, node,multiplicativeExpression, additiveExpression,ADD,SUB, location,comments):
        if len(node.children)==1:
            return self.visit(multiplicativeExpression)
        else:
            args = map(lambda n:self.visit(n), node.children) 
            args = [arg[0] if isinstance(arg, list) else arg for arg in args]                  
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op,"left":x, "right":y, "pseudo_type":TYPED_API['operators'][op](
            x['pseudo_type'], y['pseudo_type'])[-1]}, list(args))
            
    def visit_multiplicativeexpression(self, node,unaryExpression, multiplicativeExpression, MUL, DIV, MOD, location,comments):
        if len(node.children)==1:
            return self.visit(unaryExpression)
        else:
            args = map(lambda n:self.visit(n), node.children)   
            args = [arg[0] if isinstance(arg, list) else arg for arg in args]                     
            return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x, "right":y,"pseudo_type":TYPED_API['operators'][op](
            x['pseudo_type'], y['pseudo_type'])[-1]}, list(args))
    
    def visit_unaryexpression(self, node,preIncrementExpression,preDecrementExpression,unaryExpression,unaryExpressionNotPlusMinus,ADD,SUB, location,comments):
        if unaryExpressionNotPlusMinus:
            return self.visit(unaryExpressionNotPlusMinus)
        if preIncrementExpression:
            return self.visit(preIncrementExpression)
        if preDecrementExpression:
            return self.visit(preDecrementExpression)
        if unaryExpression:
            if ADD : op = "+"
            elif SUB : op = "-"  
            z = self.visit(unaryExpression)
            res = {
                    'type': 'unary_op',
                            'operator': op,
                            'value': z,
                            'pseudo_type': z["pseudo_type"]
                }
            return res

    
    def visit_preincrementexpression(self, node,unaryExpression, location,comments):
        print(f"preincrementexpression not implemented {location}")
        return self.visit(unaryExpression)
        
    def visit_predecrementexpression(self, node,unaryExpression, location,comments):
        print(f"predecrementexpression not implemented {location}")
        return self.visit(unaryExpression)

    def visit_unaryexpressionnotplusminus(self, node,postfixExpression, unaryExpression, castExpression,TILDE,BANG, location,comments):
        if postfixExpression:
            return self.visit(postfixExpression)
        if castExpression:
            return self.visit(castExpression)
        if unaryExpression:
            res = self.visit(unaryExpression)
            if BANG: op = "not"
            else: op = "~"
            return {
                'type': 'unary_op',
                        'operator': op,
                        'value': res,
                        'pseudo_type': "bool"
            } 


    def visit_postfixexpression(self, node,primary, expressionName, postIncrementExpression_lf_postfixExpression, postDecrementExpression_lf_postfixExpression, location,comments):
        if primary: 
            return self.visit(primary)
        if expressionName:
            res = self.visit(expressionName)
            return res
        if postIncrementExpression_lf_postfixExpression or postDecrementExpression_lf_postfixExpression:
            print(f"postfixexpression not implemented {location}")
    
    def visit_primary(self, node,primaryNoNewArray_lfno_primary,arrayCreationExpression,primaryNoNewArray_lf_primary,location,comments):
        if primaryNoNewArray_lfno_primary:
            res = self.visit(primaryNoNewArray_lfno_primary)
        else: res = self.visit(arrayCreationExpression)
        if primaryNoNewArray_lf_primary:
            r = self.visit(primaryNoNewArray_lf_primary) #TODO
            return {"type":"member_access", "name":res, "member":r, "pseudo_type":"void"}
        return res
    
    def visit_fieldaccess_lf_primary(self, node, DOT, Identifier,location,comments):
        return self.visit(Identifier)  
    
    def visit_arraycreationexpression(self, node,primitiveType, dimExprs,dims,classOrInterfaceType,arrayInitializer,location,comments):
        if dimExprs:
            dimexp = self.visit(dimExprs)
            if primitiveType:
                typ = self.visit(primitiveType)
            elif classOrInterfaceType:
                typ = self.visit(classOrInterfaceType)
            return {"type":"array", "dim":dimexp["length"], "elts":dimexp["expr"], "pseudo_type":["array", typ]}
        else:
            init = self.visit(arrayInitializer)
            return {"type":"array", "init":init, "pseudo_type":["array", init[0]["pseudo_type"]]}
    
    def visit_arrayinitializer(self, node,variableInitializerList, comments, location):
        return self.visit(variableInitializerList)
    
    def visit_variableinitializerlist(self, node,variableInitializer, comments, location):
        return self.visit(variableInitializer)
            
    def visit_dimexprs(self, node, dimExpr, location,comments):
        expr = []
        if isinstance(dimExpr, list):
            l = len(dimExpr)
            for r in dimExpr: expr.append(self.visit(r))
        else:
            l = 1
            expr = [self.visit(dimExpr)]
        return {"length":l, "expr":expr}
    
    def visit_dimexpr(self, node,annotation,LBRACK, RBRACK,expression,location,comments):
        if annotation:
            print(f"dimEXpr not yet implemented {location}")
        return self.visit(expression)
                
    
    
    def visit_arrayaccess_lfno_primary (self, node, expressionName,expression,primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary,primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary, location,comments):
        index = self.visit(expression)
        if expressionName:
            res = self.visit(expressionName)
           
        elif primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary:
            res = self.visit(primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary)

        result = {'type': 'index',
                'sequence': res,
                'index': index,'pseudo_type': res["pseudo_type"][1]}
        
        return result

    def visit_arrayaccess (self, node, expressionName,expression,primaryNoNewArray_lfno_arrayAccess,primaryNoNewArray_lf_arrayAccess, location,comments):
        index = self.visit(expression)
        if expressionName:
            res = self.visit(expressionName)
           
        elif primaryNoNewArray_lfno_arrayAccess:
            res = self.visit(primaryNoNewArray_lfno_arrayAccess)

        result = {'type': 'index',
                'sequence': res,
                'index': index,'pseudo_type': res["pseudo_type"][1]}
        
        return result
    
    def visit_primarynonewarray_lfno_primary(self, node, literal,typeName,unannPrimitiveType,void,this,expression,classInstanceCreationExpression_lfno_primary,fieldAccess_lfno_primary,arrayAccess_lfno_primary,methodInvocation_lfno_primary,methodReference_lfno_primary,THIS,location,comments):
        if literal:
            res = self.visit(literal)   
            return res
        if classInstanceCreationExpression_lfno_primary:
            return self.visit(classInstanceCreationExpression_lfno_primary)
        if fieldAccess_lfno_primary:
            return self.visit(fieldAccess_lfno_primary)
        if arrayAccess_lfno_primary:
            return self.visit(arrayAccess_lfno_primary)
        if methodInvocation_lfno_primary:
            return self.visit(methodInvocation_lfno_primary)
        if methodReference_lfno_primary:
            return self.visit(methodReference_lfno_primary)
        if expression:
            return self.visit(expression)
        if THIS:
            return "THIS"
        print(f"primarynonewarray_lfno_primary not implemented {location}")
            
    
    def visit_literal(self, node, IntegerLiteral, FloatingPointLiteral,BooleanLiteral,CharacterLiteral,StringLiteral,NullLiteral, location,comments):
        if BooleanLiteral: return {'type': 'bool', 'value': self.visit(BooleanLiteral), 'pseudo_type': 'bool'}
        if IntegerLiteral: return {'type': 'int', 'value': self.visit(IntegerLiteral), 'pseudo_type': 'int'}
        if FloatingPointLiteral: 
            val = self.visit(FloatingPointLiteral)
            if val.endswith("d"): return {'type': 'double', 'value': val[:-1]+".0" if "." not in val[:-1] else val[:-1], 'pseudo_type': 'double'}
            else: return {'type': 'float', 'value': val, 'pseudo_type': 'float'}
        if CharacterLiteral: 
            return {'type': 'char', 'value': str(self.visit(CharacterLiteral)), 'pseudo_type': 'char'}

        if StringLiteral: 
            val = str(StringLiteral)
            if '"' in val:
                val = val.replace('"', '')
                val = val.encode('utf-8')
            return {'type': 'string', 'value': val, 'pseudo_type': 'string'} 
        
        if NullLiteral  :
            return {"type":"Void", "value": self.visit(NullLiteral), "pseudo_type":"Void"}     
 
    def util_methodinvocation(self, api, receiver, method, args, location,comments):
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
           
    
    def visit_methodinvocation_lfno_primary(self, node,methodName, argumentList,typeName,typeArguments,Identifier,expressionName, location,comments):
        if methodName:
            args = self.visit(argumentList) 
            name = self.visit(methodName)
            if name in FUNCTION_API["Math"]:
                api = FUNCTION_API["Math"].get(name)
                return self.util_methodinvocation(api,"Math",name,args, location,comments)
            else:          
                return {"type":"custom_call", "function":name, "args": args, "pseudo_type":"Void"} #TODO
        if typeName:
            args = self.visit(argumentList) 
            receiver = self.visit(typeName) 
            method = self.visit(Identifier)
            receiver_type = self.type_env[receiver] 
            receiver_type = receiver_type[0] if isinstance(receiver_type, list) else receiver_type
            rec =  {"type":"local" , "name":receiver, "pseudo_type":self.type_env[receiver]} 
            if receiver in FUNCTION_API:
                api = FUNCTION_API[receiver].get(method) 
                return self.util_methodinvocation(api,receiver,method,args, location,comments)
                          
            elif receiver_type in METHOD_API:
                api = METHOD_API.get(receiver_type,{}).get(method)
                if api:
                    res = api.expand([rec]+ args)
                    if self.assign == False and res["message"] not in ("contains?", "index"):
                        res = {"type": 'ExprStatNode', 'expr': res}
                    return res
                if not api:
                    raise translation_error('CyMLT doesn\' t support %s %s at line %s' % (receiver_type, method,location[0]),
                                                suggestions='CyMLT supports those %s functions\n  %s' % (
                        receiver, prepare_table(TYPED_API[receiver_type], ORIGINAL_METHODS.get(receiver_type)).strip()))
            
            else: 
                res = {'type': 'custom_call', "instance": rec, "function":method, 'args': args, 'pseudo_type': "todooo"}       
            return res
        else:
            print(f"methodinvocation_lfno_primary not implemented {location}")
    
    def visit_argumentlist(self, node, expression, location,comments):
        res = []
        if isinstance(expression, list):
            for j in expression:
                res.append(self.visit(j))
        else: res = [self.visit(expression)]
        return res
    
    def visit_typename(self, node, Identifier, packageOrTypeName, DOT, comments, location):
        id = self.visit(Identifier)
        if not packageOrTypeName:
            return id
        else:
            return  self.visit(packageOrTypeName) + "%" + id
                
    
    def visit_methodinvocation(self,node,methodName, argumentList,typeName,typeArguments,Identifier,expressionName, location,comments):
        return self.visit_methodinvocation_lfno_primary(node,methodName, argumentList,typeName,typeArguments,Identifier,expressionName, location,comments)
            
        
    def visit_postincrementexpression(self, node,postfixExpression, location,comments):
        res = self.visit(postfixExpression)
        return {
                    'type': 'assignment',
                            "op":"=",
                            'target':res,
                            'value': {'type':'binary_op', 'op': "+","left":res, "right":{"type":"int", "value":"1", "pseudo_type":"int"}},
                            'pseudo_type': res["pseudo_type"]
                }
        
    def visit_postdecrementexpression(self, node,postfixExpression, location,comments):
        res = self.visit(postfixExpression)
        return {
                    'type': 'assignment',
                            "op":"=",
                            'target':res,
                            'value': {'type':'binary_op', 'op': "-","left":res, "right":{"type":"int", "value":"1", "pseudo_type":"int"}},
                            'pseudo_type': res["pseudo_type"]
                }
        
    def visit_castexpression(self, node,primitiveType, unaryExpression,referenceType, additionalBound,unaryExpressionNotPlusMinus, lambdaExpression,LPAREN, RPAREN, location,comments):
        if primitiveType:
            cas = self.visit(primitiveType)
            args = self.visit(unaryExpression)
            if cas in ("int", "double", "float", "char"):
                res = {'type': 'standard_method_call',
                            'receiver': args,
                            'args': [],
                            'message': cas,
                            'pseudo_type': cas}
                return res
            else:
                print(f"{cas} castexpression  not yet implemented {location}")
        if unaryExpressionNotPlusMinus:
            cas = self.visit(referenceType)
            args = self.visit(unaryExpressionNotPlusMinus)
            res = {'type': 'RefTypeCasting',
                        'receiver': args,
                        'args': [],
                        'message': cas,
                        'pseudo_type': cas}
            return res
        else:
            print(f"castexpression  not yet implemented {location}")
    
    def visit_unanntype(self, node, unannPrimitiveType, unannReferenceType,location,comments):
        if unannPrimitiveType:
            return self.visit(unannPrimitiveType)
        if unannReferenceType:
            z = self.visit(unannReferenceType)
            return z
    
    def visit_unannprimitivetype(self, node,numericType, location,comments):
        if numericType:
            return self.visit(numericType)
        else: return "bool"

    
    def visit_primitivetype(self, node,numericType, annotation,BOOLEAN,location,comments):
        if numericType:
            return self.visit(numericType)
        else: return "bool"
    
    def visit_numerictype(self, node, integralType, floatingPointType, location,comments):
        if integralType: return "int"
        if floatingPointType: return "float"
    
    def visit_unannarraytype(self, node, unannPrimitiveType,unannClassOrInterfaceType,unannTypeVariable, location,comments):
        if unannPrimitiveType:
            z = self.visit(unannPrimitiveType)
        if unannClassOrInterfaceType:
            z = self.visit(unannClassOrInterfaceType)
        if unannTypeVariable:
            z = self.visit(unannTypeVariable)            
        return ["array", z ]
    
    def visit_unannreferencetype(self, node, unannClassOrInterfaceType, unannTypeVariable, unannArrayType, location,comments):
        if unannClassOrInterfaceType:
            return  self.visit(unannClassOrInterfaceType)
        if unannTypeVariable:
            return self.visit(unannTypeVariable)
        if unannArrayType:
            return self.visit(unannArrayType)
    
    def visit_unannclassorinterfacetype(self, node,unannClassType_lfno_unannClassOrInterfaceType,unannInterfaceType_lfno_unannClassOrInterfaceType,unannClassType_lf_unannClassOrInterfaceType, unannInterfaceType_lf_unannClassOrInterfaceType, location,comments):
        if unannClassType_lfno_unannClassOrInterfaceType:
            res = self.visit(unannClassType_lfno_unannClassOrInterfaceType)
        if unannInterfaceType_lfno_unannClassOrInterfaceType:
            print("x2", location)
            res = self.visit(unannInterfaceType_lfno_unannClassOrInterfaceType)
        if unannClassType_lf_unannClassOrInterfaceType:
            print("x3", location)
            res = self.visit(unannClassType_lf_unannClassOrInterfaceType)
        if unannInterfaceType_lf_unannClassOrInterfaceType:
            print("x4", location)
            res = self.visit(unannInterfaceType_lf_unannClassOrInterfaceType)
        return res
    
    def visit_unannclasstype_lfno_unannclassorinterfacetype(self, node, Identifier, typeArguments, location,comments):
        res = []
        tparg = []
        res.append(self.visit(Identifier))
        if typeArguments:
            tparg = self.visit(typeArguments)
        if len(tparg)==1: 
            tparg = tparg[0]
        if len(tparg)>=1: res.append(tparg) 
        else: res = res[0]           
        return res

    def visit_typearguments(self, node, typeArgumentList, location,comments):
        return self.visit(typeArgumentList)
    
    def visit_typeargumentlist(self, node, typeArgument, location,comments):
        return self.visit(typeArgument)
    
    def visit_typeargument(self, node, referenceType, wildcard, location,comments):
        if referenceType:
            return self.visit(referenceType)
        if wildcard:
            print(f"wildcard Not Implemented {location}")
    
    def visit_referencetype(self, node, classOrInterfaceType, typeVariable, arrayType,location,comments):
        if classOrInterfaceType: 
            return self.visit(classOrInterfaceType)
        if typeVariable:
            return self.visit(typeVariable)
        if arrayType: 
            return self.visit(arrayType)
    
    def visit_arraytype(self, node,primitiveType, classOrInterfaceType,typeVariable, location,comments):
        if primitiveType:
            z = self.visit(primitiveType)
        if classOrInterfaceType:
            z = self.visit(classOrInterfaceType)
        if typeVariable:
            z = self.visit(typeVariable)
        res = {}
        return ["array",z]
        
    
    def visit_classorinterfacetype(self, node,classType_lfno_classOrInterfaceType,interfaceType_lfno_classOrInterfaceType,classType_lf_classOrInterfaceType,interfaceType_lf_classOrInterfaceType, location,comments):
        if classType_lfno_classOrInterfaceType:
            res = self.visit(classType_lfno_classOrInterfaceType)
        if interfaceType_lfno_classOrInterfaceType:
            print("x2a", location)
            res = self.visit(interfaceType_lfno_classOrInterfaceType)
        if classType_lf_classOrInterfaceType:
            print("x3a", location)
            res = self.visit(classType_lf_classOrInterfaceType)
        if interfaceType_lf_classOrInterfaceType:
            print("x4a", location)
            res = self.visit(interfaceType_lf_classOrInterfaceType)
        return res
    
    def visit_classtype_lfno_classorinterfacetype(self, node,annotation, Identifier, typeArguments, location,comments):
        id = self.visit(Identifier)
        typ = []
        if typeArguments:
            typ = self.visit(typeArguments)
        if typ and len(typ)==1: return [id, typ[0]]
        elif typ: return [id, typ]
        else: return id

    def visit_statement(self, node,statementWithoutTrailingSubstatement,labeledStatement,ifThenStatement,ifThenElseStatement,whileStatement,forStatement, location,comments):
        if statementWithoutTrailingSubstatement:
            res =  self.visit(statementWithoutTrailingSubstatement)
        if labeledStatement:
            res =  self.visit(labeledStatement)
        if ifThenStatement:
            res =  self.visit(ifThenStatement)
        if ifThenElseStatement:
            res =  self.visit(ifThenElseStatement)
        if whileStatement:
            res =  self.visit(whileStatement)
        if forStatement:
            res =  self.visit(forStatement)
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res
    
    def visit_forstatement(self, node, basicForStatement, enhancedForStatement, location,comments):
        if basicForStatement:
            return self.visit(basicForStatement)
        else:
            print(f"forstatement not implemented {location}")
            return self.visit(enhancedForStatement)
        
    
    def visit_basicforstatement(self, node,forInit,expression, forUpdate,statement,location,comments):
        res = {}
        init = self.visit(forInit)

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

        r = self.visit(forUpdate)[0]
        if (r["type"] == "unary_op" and r["operator"] == "++") or ("inc" in r):
            res["step"] = {"type":"int", "value":"1", "pseudo_type":"int"}
        elif (r["type"] == "unary_op" and r["operator"] == "--") or ("dec" in r): 
            res["step"] = {"type":"int", "value":"-1", "pseudo_type":"int"}
        elif (r["type"])=="assignment":
            if r["op"]!="=": res["step"] = r["value"]
            else: res["step"]=r["value"]["right"]
        res["index"] = init["decl"][0] if "decl" in init else init[0]["target"]
        res["index"]["type"] = "local"
        if "decl" in init: del res["index"]["value"]
        res["block"] = self.visit(statement)
        res["pseudo_type"] = "Void"
        if "decl" in init:
            decl = {"type":"declaration", "decl":[{"type":res["start"]['type'], "name":init["decl"][0]["name"], "pseudo_type":init["decl"][0]["pseudo_type"]}], "comments":[]}
            if decl not in self.for_range_index: 
                self.for_range_index.append(decl)
                return [decl, res]
        return res

        
    def visit_assignment(self, node, leftHandSide, assignmentOperator, expression, location,comments):

        z =  {
                    'type': 'assignment',
                    'target':self.visit(leftHandSide),
                    'op':assignmentOperator,
                    'value': self.visit(expression),
                    'pseudo_type': 'Void',
                    "comments":comments
                }

        return z
    
    def visit_expressionname(self, node, Identifier,ambiguousName,DOT,location,comments):
        id = self.visit(Identifier) 
        if not ambiguousName:
            pseudo_type = self.type_env[id]
            res = {"type":"local", "name":id, "pseudo_type":pseudo_type}
            return res
        else:
            res = self.visit(ambiguousName)
            pseudo_type = self.type_env[res]
            receiver =pseudo_type[0] if isinstance(pseudo_type, list) else pseudo_type
            if receiver in PROPERTY_API:
                rec = {"type":"local", "name": res, "pseudo_type":pseudo_type}
                api = PROPERTY_API[receiver].get(id)      
                if not api:
                    raise translation_error('pseudo-java doesn\' t support property %s of %s' % (id, receiver),
                                                location, [location[0]],
                                                suggestions='pseudo-java supports those %s functions\n  %s' % (
                            receiver,
                            prepare_table(TYPED_API[receiver], ORIGINAL_METHODS.get(receiver)).strip()))

                elif not isinstance(api, dict):
                    z = api.expand([rec])
                    return z
                else:
                    print(f"ExpressionName not implemented {location}")
            else:
                return {"type":"member_access", "name":res, "attribute":id, "pseudo_type":"Void"}
 
    
    def visit_ambiguousname(self, node,Identifier, ambiguousName, DOT, location,comments):
        return self.visit(Identifier)

    def visit_lefthandside(self, node, expressionName,fieldAccess,arrayAccess, location,comments):
        if expressionName: return self.visit(expressionName)
        if fieldAccess: return self.visit(fieldAccess)
        if arrayAccess: return self.visit(arrayAccess)
     
    def visit_expressionstatement(self, node, statementExpression, location,comments):
        res = self.visit(statementExpression)
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res
    
    def visit_statementwithouttrailingsubstatement(self, node, block,emptyStatement,expressionStatement,assertStatement,switchStatement,doStatement,breakStatement,	continueStatement,	returnStatement,synchronizedStatement,throwStatement,tryStatement, location,comments):
        if block: res = self.visit(block)
        if emptyStatement: res = self.visit(emptyStatement)
        if expressionStatement: res = self.visit(expressionStatement)
        if assertStatement: res = self.visit(assertStatement)
        if switchStatement: res = self.visit(switchStatement)
        if doStatement: res = self.visit(doStatement)
        if breakStatement: res = self.visit(breakStatement)
        if continueStatement: res = self.visit(continueStatement)
        if returnStatement: res = self.visit(returnStatement)
        if synchronizedStatement: res = self.visit(synchronizedStatement)
        if throwStatement: res = self.visit(throwStatement)
        if tryStatement: res = self.visit(tryStatement)
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res
    
    def visit_statementexpression(self, node,assignment,preIncrementExpression,preDecrementExpression,postIncrementExpression,postDecrementExpression,methodInvocation,classInstanceCreationExpression, location ,comments):
        if assignment:
            res = self.visit(assignment)
        if preIncrementExpression: res = self.visit(preIncrementExpression)
        if preDecrementExpression: res = self.visit(preDecrementExpression)
        if postIncrementExpression:res = self.visit(postIncrementExpression)
        if postDecrementExpression:res = self.visit(postDecrementExpression)
        if methodInvocation:res = self.visit(methodInvocation)
        if classInstanceCreationExpression: res = self.visit(classInstanceCreationExpression)
        if comments: res["comments"] = comments
        return res
    
    def visit_classinstancecreationexpression_lfno_primary(self, node,typeArguments,annotation,Identifier,typeArgumentsOrDiamond,argumentList,classBody,expressionName, location, comments):
        res = {}
        if expressionName:
            print(f"classinstancecreationexpression_lfno_primary expressionName not implemented {location}")
        else:
            if typeArguments:
                print(f"classinstancecreationexpression_lfno_primary typeArguments not implemented {location}")
            else:
                classname = self.visit(Identifier)
                res["type"] = "clsinstancecreationexpression"
                res["name"] = classname
                res["pseudo_type"] = res["type"]
                if argumentList:
                    args = self.visit(argumentList)
                    res["args"] = args
        return res
    
    """def visit_emptyStatement(self, node, location):
        pass
    
    def visit_assertStatement(self, node, location):
        pass
    
    def visit_switchStatement(self, node, location):
        pass
    
    def visit_doStatement(self, node, location):
        pass   """
        
    def visit_whilestatement(self,node,expression,statement, location ,comments):
        test_node = self.visit(expression)
        return {
            'type': 'while_statement',
            'test': test_node,
            'block': self.visit(statement),
            'pseudo_type': 'Void',
            "comments":comments
        } 
    
    def visit_returnstatement(self, node, expression, location,comments):
        z = self.visit(expression)
        return {'type': 'implicit_return', 
                'value':z , "pseudo_type":z["pseudo_type"]}
        
    def visit_terminal(self, node, value, location ,comments):
        return self.visit(value)
    
    def visit_ifthenstatement(self, node, expression, IF,LPAREN, RPAREN,statement, location,comments):
        R = {
            'type': 'if_statement',
            'test': self.visit(expression),
            'block': self.visit(statement),
            'pseudo_type': 'Void',
            'otherwise': [],
            "comments": comments
        }
        return R

    def visit_ifthenelsestatement(self, node, expression, IF,LPAREN, RPAREN,statementNoShortIf,ELSE,statement, location,comments):
        test = self.visit(expression)
        block = self.visit(statementNoShortIf)
        otherwise = self.visit(statement)
        R = {
            'type': 'if_statement',
            'test': test,
            'block': block,
            'pseudo_type': 'Void',
            'otherwise': [{
                'type': 'else_statement',
                'block': otherwise,
                'pseudo_type': 'Void'
            }],
            "comments": comments
        }
        return R
    
    def visit_statementnoshortif(self, node, statementWithoutTrailingSubstatement, labeledStatementNoShortIf, ifThenElseStatementNoShortIf, whileStatementNoShortIf,forStatementNoShortIf,location, comments):
        if statementWithoutTrailingSubstatement : res = self.visit(statementWithoutTrailingSubstatement)
        if labeledStatementNoShortIf: res = self.visit(labeledStatementNoShortIf)
        if ifThenElseStatementNoShortIf: res  = self.visit(ifThenElseStatementNoShortIf)
        if whileStatementNoShortIf: res = self.visit(whileStatementNoShortIf)
        if forStatementNoShortIf  : res = self.visit(forStatementNoShortIf)    
        if comments and isinstance(res, dict): res["comments"] = comments
        if comments and isinstance(res, list): res.insert(0,{"type":"comments", "comments": comments})
        return res    
    
    def visit_methodinvocation_lf_primary(self, node,typeArguments, Identifier, argumentList, comments, location) :
        args = self.visit(argumentList)  
        id = self.visit(Identifier)
        #TODO Continue
        return  {'type': 'methodcall',
                        'args': args,
                        'message': id,
                        'pseudo_type': "unknowwn"}
         
        