from pycropml.transpiler.env import Env
from pycropml.transpiler.helpers import *
from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.antlr_py.fortran.builtin_typed_api import *
from pycropml.transpiler.antlr_py.fortran.api_transform import *
from pycropml.transpiler.errors import PseudoCythonTypeCheckError, PseudoCythonNotTranslatableError, translation_error, type_check_error

from ast import AST

f90_op = {".AND":"and", ".OR":"or"}
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

class Program(AliasNode):
    _fields_spec = ["COMMENTORNEWLINE", "executableProgram"]

class ExecutableProgram(AliasNode):
    _fields_spec = ["programUnit"]

class ProgramUnit(AliasNode):
    _fields_spec = ["mainProgram", "functionSubprogram", "subroutineSubprogram", "blockDataSubprogram", "module" ]

class Module(AliasNode):
    _fields_spec = ["moduleStmt","moduleBody" ]

class ModuleSubprogramPartConstruct(AliasNode):
    _fields_spec = ["containsStmt", "moduleSubprogram" ]

class ModuleSubprogram(AliasNode):
    _fields_spec = ["functionSubprogram", "subroutineSubprogram" ]

class UseStatement(AliasNode):
    _fields_spec = ["useStmt"]

class UseStmt(AliasNode):
    _fields_spec = ["NAME", "EOS","ONLY","renameList","onlyList"]

class TypeDeclarationStmt(AliasNode):
    _fields_spec =["typeSpec", "entityDeclList", "EOS", "DOUBLECOLON", "attrSpecSeq"]

class EntityDeclList(AliasNode):
    _fields_spec =["entityDecl"]

class EntityDecl(AliasNode):
    _fields_spec =["objectName","arraySpec", "charLength","STAR","expression"]

class ImplicitStatement(AliasNode):
    _fields_spec = ["implicitSpecList", "EOS"]

class SpecPartStmt(AliasNode):
    _fields_spec = ["specificationPartConstruct" ]

class SubmoduleStmt(AliasNode):
    _fields_spec = ["moduleSubprogramPartConstruct"]

class ComplexSubmodule(AliasNode):
    _fields_spec = ["moduleBody" , "moduleSubprogramPartConstruct"]

class SubroutineSubprogram(AliasNode):
    _fields_spec = ["subroutineName","subroutineRange", "RECURSIVE"]

class SubroutineRange(AliasNode):
    _fields_spec = ["subroutineParList", "EOS", "body","bodyPlusInternals"]

class TypeSpec(AliasNode):
    _fields_spec =["INTEGER","REAL","DOUBLEPRECISION","COMPLEX","DOUBLE","LOGICAL","CHARACTER","lengthSelector","kindSelector","PRECISION","charSelector","typeName"]

class AttrSpecSeq(AliasNode):
    _fields_spec = ["attrSpecSeq","attrSpec"]

class AssignmentStmt(AliasNode):
    _fields_spec = ["label", "NAME", "sFExprListRef", "substringRange", "expression", "EOS", "nameDataRef",	"sFDummyArgNameList", "PCT"]

class Expression(AliasNode):
    _fields_spec =["level5Expr", "expression", "definedBinaryOp"]

class Level5Expr(AliasNode):
    _fields_spec = ["equivOperand" ,"NEQV" ,"EQV"]

class EquivOperand(AliasNode):
    _fields_spec = ["orOperand" ,"LOR"]

class OrOperand(AliasNode):
    _fields_spec = ["andOperand" ,"LAND"]

class AndOperand(AliasNode):
    _fields_spec = ["level4Expr" ,"LNOT"]

class Level4Expr(AliasNode):
    _fields_spec = ["level3Expr" ,"relOp"]

class Level3Expr(AliasNode):
    _fields_spec = ["level2Expr" ,"DIV", "SPOFF","SPON"]

class Level2Expr(AliasNode):
    _fields_spec = ["addOperand" ,"sign", "PLUS","MINUS"]

class AddOperand(AliasNode):
    _fields_spec = ["multOperand" ,"STAR", "DIV"]

class MultOperand(AliasNode):
    _fields_spec = ["level1Expr" ,"POWER"]

class Level1Expr(AliasNode):
    _fields_spec = ["primary" ,"definedUnaryOp"]

class Primary(AliasNode):
    _fields_spec = ["unsignedArithmeticConstant", "nameDataRef","functionReference","expression", "SCON","logicalConstant","arrayConstructor", "LPAREN", "RPAREN"]

class UnsignedArithmeticConstant(AliasNode):
    _fields_spec = []

class IfConstruct(AliasNode):
    _fields_spec = ["ifThenStmt", "conditionalBody", "elseIfConstruct", "elseConstruct"]

class ElseIfStmt(AliasNode):
    _fields_spec = ["expression"]

class ElseConstruct(AliasNode):
    _fields_spec = ["conditionalBody"]

class FunctionReference(AliasNode):
    _fields_spec = ['NAME', 'functionArgList']

class NameDataRef(AliasNode):
    _fields_spec = ['NAME', 'complexDataRefTail', 'REAL', 'SIZE']

class FunctionArgList(AliasNode):
    _fields_spec = ['functionArg', 'functionArgList', 'sectionSubscriptList']

class FunctionArg(AliasNode):
    _fields_spec = ['NAME', 'expression']

class ComplexDataRefTail(AliasNode):
    _fields_spec = ["sectionSubscriptRef", "NAME"]

class SectionSubscriptRef(AliasNode):
    _fields_spec = ["sectionSubscriptList"]

class SectionSubscriptList(AliasNode):
    _fields_spec = ["sectionSubscript"]

class SectionSubscript(AliasNode):
    _fields_spec = ["expression","subscriptTripletTail"]

class BlockDoConstruct(AliasNode):
    _fields_spec = ["commaLoopControl","executionPartConstruct"]

class LoopControl(AliasNode):
    _fields_spec = ["variableName","expression","commaExpr","WHILE"]

class CallStmt(AliasNode):
    _fields_spec = ["subroutineNameUse","subroutineArgList"]

class CommaLoopControl(AliasNode):
    _fields_spec = ["loopControl"]

class FunctionSubprogram(AliasNode):
    _fields_spec = ["functionPrefix", "functionName", "functionRange"]

class FunctionRange(AliasNode):
    _fields_spec = ["functionParList", "NAME", "RESULT", "EOS", "body","bodyPlusInternals"]

class FunctionParList(AliasNode):
    _fields_spec = ["functionPars"]

class FunctionPars(AliasNode):
    _fields_spec = ["functionPar"]

class FunctionPrefixRec(AliasNode):
    _fields_spec = ["recursive", "typeSpec"]

class FunctionPrefixTyp(AliasNode):
    _fields_spec = ["typeSpec", "RECURSIVE"]

class DeallocateStmt(AliasNode):
    _fields_spec = ["allocateObjectList", "STAT", "variable", "EOS"]

class Transformer(BaseNodeTransformer):
    def visit_Program(self, node):
        return Program.from_spec(node)
    def visit_ExecutableProgram(self, node):
        return ExecutableProgram.from_spec(node)
    def visit_ProgramUnit(self, node):
        return ProgramUnit.from_spec(node)
    def visit_Module(self, node):
        return Module.from_spec(node)
    def visit_ModuleSubprogramPartConstruct(self, node):
        return ModuleSubprogramPartConstruct.from_spec(node)
    def visit_ModuleSubprogram(self, node):
        return ModuleSubprogram.from_spec(node)
    def visit_SpecPartStmt(self, node):
        return SpecPartStmt.from_spec(node)
    def visit_SubmoduleStmt(self, node):
         return SubmoduleStmt.from_spec(node)  
    def visit_ComplexSubmodule(self, node):
        return ComplexSubmodule.from_spec(node)
    def visit_UseStatement(self, node):
        return UseStatement.from_spec(node)
    def visit_UseStmt(self, node):
        return UseStmt.from_spec(node)
    def visit_ImplicitStatement(self, node):
        return ImplicitStatement.from_spec(node)
    def visit_SubroutineSubprogram(self, node):
        return SubroutineSubprogram.from_spec(node)
    def visit_SubroutineRange(self, node):
        return SubroutineRange.from_spec(node)
    def visit_TypeDeclarationStmt(self,node):
        return TypeDeclarationStmt.from_spec(node)
    def visit_EntityDeclList(self,node):
        return EntityDeclList.from_spec(node)
    def visit_EntityDecl(self,node):
        return EntityDecl.from_spec(node)
    def visit_TypeSpec(self, node):
        return TypeSpec.from_spec(node)
    def visit_AttrSpecSeq(self, node):
        return AttrSpecSeq.from_spec(node)
    def visit_AssignmentStmt(self,node):
        return AssignmentStmt.from_spec(node)
    def visit_Expression(self,node):
        return Expression.from_spec(node)
    def visit_Level5Expr(self,node):
        return Level5Expr.from_spec(node)
    def visit_EquivOperand(self,node):
        return EquivOperand.from_spec(node)
    def visit_OrOperand(self,node):
        return OrOperand.from_spec(node)
    def visit_AndOperand(self,node):
        return AndOperand.from_spec(node)
    def visit_Level4Expr(self,node):
        return Level4Expr.from_spec(node)
    def visit_Level3Expr(self,node):
        return Level3Expr.from_spec(node)
    def visit_Level2Expr(self,node):
        return Level2Expr.from_spec(node)
    def visit_AddOperand(self,node):
        return AddOperand.from_spec(node)
    def visit_MultOperand(self,node):
        return MultOperand.from_spec(node)
    def visit_Level1Expr(self,node):
        return Level1Expr.from_spec(node)
    def visit_Primary(self,node):
        return Primary.from_spec(node)
    def visit_IfConstruct(self,node):
        return IfConstruct.from_spec(node)
    def visit_ElseIfStmt(self,node):
        return ElseIfStmt.from_spec(node)
    def visit_ElseConstruct(self,node):
        return ElseConstruct.from_spec(node)
    def visit_FunctionReference(self,node):
        return FunctionReference.from_spec(node)
    def visit_NameDataRef(self,node):
        return NameDataRef.from_spec(node)
    def visit_FunctionArgList(self,node):
        return FunctionArgList.from_spec(node)
    def visit_FunctionArg(self,node):
        return FunctionArg.from_spec(node)
    def visit_ComplexDataRefTail(self,node):
        return ComplexDataRefTail.from_spec(node)
    def visit_SectionSubscriptRef(self,node):
        return SectionSubscriptRef.from_spec(node)
    def visit_SectionSubscriptList(self,node):
        return SectionSubscriptList.from_spec(node)
    def visit_SectionSubscript(self,node):
        return SectionSubscript.from_spec(node)
    def visit_BlockDoConstruct(self,node):
        return BlockDoConstruct.from_spec(node)
    def visit_LoopControl(self, node):
        return LoopControl.from_spec(node)
    def visit_CallStmt(self, node):
        return CallStmt.from_spec(node)
    def visit_CommaLoopControl(self, node):
        return CommaLoopControl.from_spec(node)
    def visit_FunctionSubprogram(self, node):
        return FunctionSubprogram.from_spec(node)
    def visit_FunctionRange(self, node):
        return FunctionRange.from_spec(node)
    def visit_DeallocateStmt(self, node):
        return DeallocateStmt.from_spec(node)
    def visit_FunctionParList(self, node):
        return FunctionParList.from_spec(node)
    def visit_FunctionPars(self, node):
        return FunctionPars.from_spec(node)
    def visit_FunctionPrefixRec(self, node):
        return FunctionPrefixRec.from_spec(node)
    def visit_FunctionPrefixTyp(self, node):
        return FunctionPrefixTyp.from_spec(node)

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
        self.recursive = False
        self.out = None
        self._imports=[]
        self._fromimport = {}
        self._definition_index = {'functions': {}}
        self.decl = []
        self.attr = {}
        self.top_level(self.tree)
        body = self.visit(self.tree)
        return {'body': body if isinstance(body, list) else [body]}
    
    def top_level(self, tree):
        """
        elif isinstance(nodes, Nodes.DefNode):
            self.definitions.append(('function', nodes.name))
            self._definition_index['functions'][nodes.name] = nodes
            self.type_env.top['functions'][nodes.name] = [
                'Function'] + ([None] * len(nodes.args)) + [None]
            self.type_env.top[nodes.name] = self.type_env.top['functions'][nodes.name]
        elif isinstance(nodes, Nodes.StatListNode):
            for node in nodes.stats:
                if isinstance(node, Nodes.DefNode):
                    self.visit_top_level(node)"""


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
    
    def visit_program(self, node, COMMENTORNEWLINE, executableProgram, location):
        z = self.visit(executableProgram)
        return z

    def visit_executableprogram(self, node, programUnit, location):
        res = self.translate_list(programUnit)
        return res if len(res)>1 else res[0]
    
    def visit_programunit(self, node,mainProgram,functionSubprogram,subroutineSubprogram,blockDataSubprogram, module, location):
        if mainProgram : return self.visit(mainProgram)
        if functionSubprogram : return self.visit(functionSubprogram)
        if subroutineSubprogram : return self.visit(subroutineSubprogram)
        if blockDataSubprogram : return self.visit(blockDataSubprogram)
        if module : return self.visit(module)

    def visit_mainprogram(self, node,programStmt, mainRange, location):
        res= self.visit(mainRange)
        return {"type":"main", "block": res}

    
    def visit_module(self, node, moduleStmt, moduleBody, location):
        body =[]
        if moduleBody : 
            body = self.visit(moduleBody)
        name = self.visit(moduleStmt.moduleName)
        return {"type":"module", "name":name, "body":body}
    
    def visit_submodulestmt(self, node, moduleSubprogramPartConstruct, location):
        return self.visit(moduleSubprogramPartConstruct)
    
    def visit_specpartstmt(self, node, specificationPartConstruct, location):
        return self.visit(specificationPartConstruct)
    
    def visit_modulesubprogrampartconstruct(self, node,moduleSubprogram,containsStmt, location):
        if moduleSubprogram : return self.visit(moduleSubprogram)
        return 
    
    def visit_modulesubprogram(self, node,functionSubprogram , subroutineSubprogram, location):
        if functionSubprogram : return self.visit(functionSubprogram)
        if subroutineSubprogram : return self.visit(subroutineSubprogram)

    def visit_complexsubmodule(self, node, moduleBody, moduleSubprogramPartConstruct,location):
        res1 = self.visit(moduleBody)
        res = res1 if isinstance(res1, list) else [res1] 
        z = self.visit(moduleSubprogramPartConstruct)
        res.append(z) 
        return res

    def visit_complexspecpart(self, node,moduleBody, specificationPartConstruct, location):
        res1 = self.visit(moduleBody)
        res = res1 if isinstance(res1, list) else [res1] 
        z = self.visit(specificationPartConstruct)
        res.append(z) 
        return res

        

    def visit_usestatement(self, node, useStmt ,location):
        return self.visit(useStmt)

    def visit_usestmt(self, node, NAME, EOS,ONLY,renameList,onlyList,location):
        if renameList:
            #res = {"type":"import", "module": self.visit(renameList) }
            pass
        elif onlyList:
            #res = {"type":"import", "module": self.visit(onlyList) }
            pass
        elif ONLY:
            pass
        else:
            res = {"type":"import", "name": str(node.NAME) }
            if str(node.NAME) in SYSTEM_API: self._fromimport[str(node.NAME)] = list(SYSTEM_API.values())
        #return res
    
    def translate_list(self, inputs):
        res = []
        for arg in inputs:
            b = self.visit(arg)
            res.append(b)
        return res

    def visit_containsstmt(self, node, CONTAINS, EOS , location ):
        pass

    def visit_implicitstatement(self, node, implicitSpecList, EOS,location):
        pass

    def visit_subroutinesubprogram(self, node, subroutineName,subroutineRange, RECURSIVE, location):
        name = self.visit(subroutineName)
        z = self.visit(subroutineRange) 
        params = z["_params"]
        decl = [m["decl"] for m in z["_body"] if (isinstance(m, dict) and m["type"]=="declaration")]
        d = [item for sublist in decl for item in sublist]
        arguments = [m for m in d if 'attr' in m and  ((m['attr']=="IN" or m['attr']=="in") or  (m['attr']=="INOUT" or m['attr']=="inout")) ] 
        out_pseudo_t = [m["pseudo_type"] for m in d if 'attr' in m and  ((m['attr']=="OUT" or m['attr']=="out") or  (m['attr']=="INOUT" or m['attr']=="inout")) ] 
        in_pseudo_t = [m["pseudo_type"] for m in arguments]
        return_type = out_pseudo_t if len(out_pseudo_t)==1 else [["tuple"]+out_pseudo_t]
        body = []
        for n in z["_body"] :
            if isinstance(n, dict) and n["type"]=="declaration":
                print(n)
                v = {}
                v["type"] = "declaration"
                v["decl"] = []
                for m in  n["decl"]:
                    if m not in arguments:
                        v["decl"].append(m)
                if v["decl"]: body.append(v)
            else: body.append(n)
        res = {"type":"function_definition", 
                "name": str(name), 
                "params":arguments, 
                "pseudo_type":['Function']+in_pseudo_t+return_type,
                "return_type": return_type[0],
                "block":body}
        self.type_env.top["functions"][res["name"]] = [res["return_type"]]
        return res

    def visit_subroutinerange(self, node, subroutineParList, EOS, body,bodyPlusInternals,location):
        if body :
            bod = self.visit(body)
        else : bod = self.visit(bodyPlusInternals)
        params = self.translate_list(subroutineParList.subroutinePars)
        return {"_params":params, "_body": bod}
    
    def visit_entitydecllist(self, node,entityDecl, location):
        if not isinstance(entityDecl, list):
            return self.visit(entityDecl)
        res = self.translate_list(entityDecl)
        return res

    def visit_entitydecl(self, node, objectName, arraySpec, charLength,STAR,expression, location) :
        if charLength and arraySpec :
            if expression:
                print("houm1")
            else:
                print("houm2")
        elif charLength:
            if expression:
                print("houm3")
            else:
                print("houm4")
        elif arraySpec:
            if expression:
                print("houm5")
            else:
                spec = self.visit(arraySpec)
                z = {"name":objectName, "dim": len(spec), "elts":spec}
                return z
        elif expression:
            return {"name":objectName, "value":self.visit(expression)}
        else:
            return {"name":objectName}

    

    
    def visit_typedeclarationstmt(self, node, typeSpec, entityDeclList, EOS, DOUBLECOLON, attrSpecSeq,location):
        z = []
        attr = {}
        names = self.visit(entityDeclList)
        elemtype_ = self.visit(typeSpec)
        attr = None
        if attrSpecSeq:
            self.attr = {}
            attr = self.visit(attrSpecSeq)
        if attr and "DIMENSION" in attr and "ALLOCATABLE" in attr and attr["DIMENSION"] == [":"]:
            typ = "list"
            pseudo_type = ["list", elemtype_]
        else : 
            typ = elemtype_
            pseudo_type = elemtype_
        for j in names:
            zj = {"type":typ, "name": str(j["name"]), "pseudo_type":pseudo_type}
            if "dim" in j:
                zj["type"] = "array"
                zj["dim"] = j["dim"]
                zj["elts"] = j["elts"]
                zj["pseudo_type"] = ["array", elemtype_]            
            self.type_env[str(j["name"])] = zj["pseudo_type"]
            if "value" in j: zj["value"] = j["value"]
            if attr and 'INTENT' in attr : zj["attr"] = attr['INTENT']
            z.append(zj)     
        res = {"type":"declaration", "decl":z}
        return res
    
    def visit_attrspecseq(self, node, attrSpecSeq,attrSpec, location):
        if "DIMENSION" in dir(attrSpec) : self.attr.update({"DIMENSION": self.visit(attrSpec.arraySpec)})
        elif "INTENT" in dir(attrSpec):  self.attr.update({"INTENT": self.visit(attrSpec.intentSpec)})
        else : self.attr.update({self.visit(attrSpec):None})

        if attrSpecSeq: 
            node = attrSpecSeq
            attrSpecSeq = node.attrSpecSeq
            attrSpec = node.attrSpec
            self.visit_attrspecseq(node, attrSpecSeq,attrSpec, location)
        
        return self.attr 
    
    def visit_typespec(self, node, INTEGER,REAL,DOUBLEPRECISION,DOUBLE,COMPLEX,LOGICAL,CHARACTER,lengthSelector,kindSelector,PRECISION,charSelector,typeName,location):
        if INTEGER:
            type_ = "int"
        if REAL:
            type_ = "float"
        if DOUBLEPRECISION or DOUBLE:
            type_ = "double"
        if LOGICAL:
            type_ = "boolean"
        if CHARACTER :
            type_ = "string" 
        return type_
    
    def visit_terminal(self, node, value, location):
        return str(self.visit(value))

    
    def visit_assignmentstmt(self, node, label, NAME, sFExprListRef, substringRange, expression, EOS, 
                            nameDataRef, sFDummyArgNameList, PCT,location):
        if sFDummyArgNameList:
            pass
        elif PCT:
            pass
        else :
            if not sFExprListRef and not substringRange :
                res = {"type":"assignment",
                        "target": {"type":"local", "name":str(NAME), "pseudo_type": self.type_env[str(NAME)]} ,
                        "value" : self.visit(expression),
                        "pseudo_type":"VOID"}
                if self.recursive and str(NAME)==self.out:
                        return {"type":"implicit_return",
                                "value": res["value"],
                                "pseudo_type": res["target"]["pseudo_type"]}
                return res

    def visit_expression(self, node, level5Expr, expression, definedBinaryOp, location):
        if definedBinaryOp:
            return
        else: 
            res = self.visit(level5Expr)
            return res[0]

    
    def visit_level5expr(self,node,equivOperand,NEQV, EQV,location):
        if len(node.children)==1:   
            return self.visit(equivOperand)
        args = map(lambda n:self.visit(n), node.children)  
        op = "!=" if  NEQV else "=="
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_equivoperand(self,node,orOperand,LOR,location):
        op = "or"
        if len(node.children)==1:    
            return self.visit(orOperand)
        args = map(lambda n:self.visit(n) if (n!=".OR." and n!='.or.') else "or", node.children)  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_oroperand(self,node,andOperand,LAND,location):
        op = "and"
        if len(node.children)==1:     
            return self.visit(andOperand)
        args = map(lambda n:self.visit(n) if (n!=".AND." and n!='.and.') else "and", node.children)  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))


    def visit_andoperand(self,node,level4Expr,LNOT,location):
        op = "not"
        if len(node.children)==1:     
            return self.visit(level4Expr)
        args = map(lambda n:self.visit(n) if n!=".NOT." else "not", node.children)  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_level4expr(self,node,level3Expr,relOp,location):
        if len(node.children)==1:     
            return self.visit(level3Expr)
        args = map(lambda n:self.visit(n), node.children)  
        op = relOp
        res = reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))
        if isinstance(res["left"]["pseudo_type"], list): res["pseudo_type"]=["list", "bool"]
        return res 

    def visit_relop(self, node,  LT,LE ,EQ , NE , GT , GE, OP, location):
        if LT : op="<"
        if LE : op = "<="
        if EQ : op = "=="
        if NE : op = "!="
        if GT : op = ">"
        if GE : op = ">="
        if OP :
            if OP == "/=" : op = "!="
            else : op = OP
        return op

        return


    def visit_level3expr(self,node,level2Expr,DIV, SPOFF, SPON,location):
        if len(node.children)==1:     
            return self.visit(level2Expr)
        args = map(lambda n:self.visit(n), node.children)  
        op = "//"
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_level2expr(self,node,addOperand,PLUS, MINUS,sign,location):
        op = "+" if PLUS else "-"
        if sign:
            if len(addOperand)==1:     
                res = self.visit(addOperand)
                return {"type":"unary_op", "operator":str(sign), "value": res[0], "pseudo_type":res[0]["pseudo_type"]}
            else:
                res = self.visit(node.children[1])
                r = {"type":"unary_op", "operator":str(sign), "value": res[0], "pseudo_type":res[0]["pseudo_type"]}
                args = map(lambda n:self.visit(n), node.children[3:]) 
                res = reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, [r] + [node.children[2]]+list(args))
                return  res
        else:
            if len(addOperand)==1:     
                return self.visit(addOperand)
            args = map(lambda n:self.visit(n), node.children)  
            res = reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, list(args))
            return res
    
    def visit_sign(self, node, PLUS , MINUS, location):
        return "+" if PLUS else "-"


    def visit_addoperand(self,node,multOperand,STAR , DIV,location):   
        op = "*" if STAR else "/"
        if len(node.children)==1:     
            return self.visit(multOperand)
        args = map(lambda n:self.visit(n), node.children)
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, list(args))

    def visit_multoperand(self,node,level1Expr,POWER,location):
        op = "**"
        if len(node.children)==1:     
            return self.visit(level1Expr)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, list(args))
  
    def visit_level1expr(self,node,primary,definedUnaryOp,location):
        if definedUnaryOp:  
            res = self.visit(primary)   
            return  {"type":"unary_op", "operator":self.visit(definedUnaryOp), "value": res, "pseudo_type":res["pseudo_type"]}
        res = self.visit(primary)
        return res
    
    def visit_primary(self, node, unsignedArithmeticConstant, \
                        nameDataRef,functionReference,expression, \
                        SCON,logicalConstant,arrayConstructor,LPAREN, RPAREN, location\
                    ):
        if unsignedArithmeticConstant : 
            res = self.visit(unsignedArithmeticConstant)
            res2 = eval(res)
            typ = str(type(res2)).split(" ")[1][1:-2]
            return {"type":typ, "value":res, "pseudo_type": typ}
        if nameDataRef : 
            return self.visit(nameDataRef)
        if functionReference : return self.visit(functionReference)
        if expression: return self.visit(expression)
        if SCON: 
            val = str(self.visit(SCON))
            if "'" in val:
                val = val.replace("'", '' )
                val = val.encode('utf-8')
            return {'type':'string', 'value': val, "pseudo_type":"string"}
        if logicalConstant : return {"type":"bool", "value": self.visit(logicalConstant), "pseudo_type":"bool"}
        if arrayConstructor : return self.visit(arrayConstructor)
        else:
            pass

    def visit_unsignedarithmeticconstant(self, node,  ICON, RDCON, complexConst, UNDERSCORE, kindParam, location):
        if ICON: return self.visit(ICON)
        elif RDCON: return self.visit(RDCON)
        else:
            print(location, "unsign")

        return 
    
    def visit_caseconstruct(self, node, NAME, COLON, SELECTCASE, CASE,LPAREN, expression, RPAREN, EOS, SELECT, selectCaseRange, location):
        
        
        return 

    def visit_ifconstruct(self, node,ifThenStmt, conditionalBody, elseIfConstruct, elseConstruct, location):
        otherwise = []
        
        test = self.visit(ifThenStmt.expression)
        block = self.visit(conditionalBody)

        if elseIfConstruct :
            r = self.translate_list(elseIfConstruct)
            otherwise = otherwise + r
        
        if elseConstruct:
            r = self.visit(elseConstruct)
            otherwise.append(r)
        
        R = {
            'type': 'if_statement',
            'test': test,
            'block': block,
            'pseudo_type': 'Void',
            'otherwise': otherwise
        }
        return R

    def visit_elseifconstruct(self, node, elseIfStmt,conditionalBody, location):
        test = self.visit(elseIfStmt)
        body = self.visit(conditionalBody)[0]
        return {'type': 'elseif_statement',
           'test': test,
           'block': body,
           'pseudo_type': 'Void'}
    
    def visit_elseifstmt(self, node, expression, location):
        return self.visit(expression)
        

    def visit_elseconstruct(self, node, conditionalBody,location):
        res = self.visit(conditionalBody)[0]
        return {'type': 'else_statement',
            'block': res,
            'pseudo_type': 'Void'}
    
    def visit_conditionalbody(self, node,  executionPartConstruct, location):
        return self.translate_list(executionPartConstruct)
    
    def visit_printstmt(self, node, PRINT, formatIdentifier, outputItemList, EOS, location):
        if outputItemList : 
            r = self.visit(outputItemList)
            print(r, "ghhgh")
            return {"type":"standard_call", "namespace":"io", "function":"print", "args": r if isinstance(r, list) else [r]}
        else: print("todo print")
    
    def visit_exitstmt(self, node, EXIT, endName, EOS, location):
        print("todo exitstmt")
        return
    
    def visit_functionreference(self, node,NAME,functionArgList, location):
        args =self.visit(functionArgList)
        name = str(NAME).lower()
        pass
        if name in BUILTIN_FUNCTIONS:
            if name in ['any', 'all', 'sum', 'mean', 'count']:
                if len(args) != 1:
                    raise translation_error('%s expected 1 arg, not %d' % (name, len(args)),
                                            location, self.lines[location[0]])            
                else:
                    if name not in ['sum',"mean","count"]:
                        if args[0]['pseudo_type'] != ['list', 'bool']:
                            raise type_check_error('%s expected list[bool]' % name,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=args['pseudo_type'])
                        message = name
                        return {
                            'type': 'standard_method_call',
                            'receiver': args,
                            'message': message,
                            'args': [],
                            'pseudo_type': "bool"
                        }
                    else:
                        if args['pseudo_type'] not in[ ['list', 'int'] , ['list', 'float'],['array', 'int'] , ['array', 'float'],"unknown"]:
                            raise type_check_error('%s expected list[int] / list[float]' % name,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=args['pseudo_type'])
                        message = name
                        _type = args['pseudo_type'][1] if message !="count" else "int"
                        return {
                            'type': 'standard_method_call',
                            'receiver': args,
                            'message': message,
                            'args': [],
                            'pseudo_type': _type
                        }
            else:
                return self._translate_builtin_call('global', name, args, location, attrib=0)
        else:
            c = self.type_env.top['functions']
            message = str(NAME)
            param_types = [param['pseudo_type'] for param in args]
            if message in c:
                if len(c[message]) == 2 or len(c[message]) > 2 and c[message][1]:
                    g = self.type_env.top.values.get("functions", {}).get(message)[1:]
                    q = self._type_check(g,message, param_types)[-1]
                    x = [f for f in self.signature if f.name == message]
                    if q is None: 
                        self.accessReturn(x[0])
                        q = self.q["pseudo_type"]
                else:
                    v = self.function_name
                    x = [f for f in self.signature if f.name == message]
                    argx = [a["pseudo_type"] for a in self.visit_node(x[0].args)]
                    self._definition_index["functions"][message] = self.visit_node(x[0])
                    q = c[message][-1]
                    if argx != param_types:
                        raise PseudoCythonTypeCheckError("Types incompatibility at line %s"%location[0])
                    #q = self._type_check(argx+returnx,message, param_types)[-1]
                    self.function_name = v 
                if message == self.function_name: self.recursive = True 
                                                  
                return {
                    "type": "custom_call",
                    "args": args[0],
                    "function": message,
                    "pseudo_type": q}
            else:
                meth = [d for m in list(self._fromimport.values()) for d in m]
                if name not in meth:
                    pass
                else:
                    if self.retrieve_library(name) not in self._imports:
                        self._imports.append(
                            self.retrieve_library(name))
                    return self._translate_builtin_call(self.retrieve_library(name), name, args, location, attrib=0)

   
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
    def visit_namedataref(self, node, NAME, SIZE, REAL, complexDataRefTail, location):        
        if not complexDataRefTail:
            id_type = self.type_env.top[str(NAME)]
            if id_type is None:
                """ raise type_check_error(
                    '%s is not defined at line %s and column %s' %(str(identifier), location[0], location[1]))""" # remove cote

            return {"type":"local", "name": str(NAME), "pseudo_type":id_type}
        
        else :
            if NAME :  func = str(NAME) 
            if SIZE : func = str(SIZE)
            if REAL : func = str(REAL)
            args = self.translate_list(complexDataRefTail)
            if "attr" not in args[0]:
                res = self.translate_func(func, args, location)
                return res
        
        return
    
    def visit_complexdatareftail(self, node, sectionSubscriptRef, NAME, location):
        if sectionSubscriptRef :
            return self.visit(sectionSubscriptRef)
        return {'attr':str(NAME)}

    def visit_sectionsubscriptref(self, node, sectionSubscriptList, location):
        return self.visit(sectionSubscriptList)
    
    def visit_sectionsubscriptlist(self, node,sectionSubscript, location ):
        return self.translate_list(sectionSubscript)
    
    def visit_sectionsubscript(self, node, expression,subscriptTripletTail,location):
        if expression:
            if subscriptTripletTail:
                pass
            else:
                return self.visit(expression)
        else:
            return self.visit(subscriptTripletTail)
        
    
    def visit_functionarglist(self, node, functionArg, functionArgList,sectionSubscriptList, location):
        r = self.visit(functionArg)
        res = []
        if functionArgList:
            if functionArgList.sectionSubscriptList:
                res.append(self.visit(functionArgList.sectionSubscriptList))
                res.append(r)
            else:
                res.append(self.visit(functionArgList.functionArg))
                res.append(r)
        elif sectionSubscriptList:
            res.append(self.visit(sectionSubscriptList))
            res.append(r)
        else:
            res.append(r)
        return res
    
    def visit_functionarg(self, node,NAME, expression, location):

        return {"type":"assignment", "target":{"type":"local", "name":str(NAME), "pseudo_type":self.type_env.top[str(NAME)]},
                                            "value":self.visit(expression),
                                            "pseudo_type":"VOID" }
 
    def _general_type(self, t):
        if isinstance(t, list):
            return t[0]
        else:
            return t
    
    def translate_func(self, name, args, location):
        if name.lower() in FUNCTION_API:
            api = FUNCTION_API[name.lower()]
            if not isinstance(api, dict):
                z = api.expand(args)
                return z
        meth = [d for m in list(self._fromimport.values()) for d in m]
        n = {}
        for a in meth:
            n.update(a)
        if name.lower() in n:
            api = n[name.lower()]
            if not isinstance(api, dict):
                z = api.expand(args)
                return z
        id_type = self.type_env.top[name]
        if id_type and isinstance(id_type, list):
            return {'type': 'index',
                    'sequence': {'type': 'local',
                    'name': name,
                    'pseudo_type': id_type},
                    'index': args[0][0],
                    'pseudo_type': id_type[-1] }
        
        else:
            fname = name
            c = self.type_env.top['functions']
            if fname in c:
                pseudo_type = c[fname][-1]
            else: pseudo_type="unknown"
            return {"type": "custom_call",
                        "args": args[0],
                        "function":name,
                        "pseudo_type":pseudo_type
                    }   ####Todooooooo


        
        

    
    def visit_blockdoconstruct(self, node,commaLoopControl,executionPartConstruct,location):
        lpc = self.visit(commaLoopControl)
        block = {"block":self.visit(executionPartConstruct)}
        lpc.update(block)
        return lpc         
    
    def visit_commaloopcontrol(self, node, loopControl, location):
        return self.visit(loopControl)
    
    def visit_loopcontrol(self, node,variableName,expression,commaExpr,WHILE, location):
        if not WHILE : 
            nm = self.visit(variableName)
            index = {'type': 'local', 'pseudo_type': self.type_env.top[nm], 'name': nm}
            start = self.visit(expression[0])
            end = self.visit(expression[1])
            if commaExpr:
                step = self.visit(commaExpr)
            else : step = {"type":"int", "value":"1", "pseudo_type":"int"}
            return {"type":"for_range_statement","index":index, "start":start, "end":end, "step": step, 'pseudo_type': 'Void'}
        else :
            return {
            'type': 'while_statement',
            'test': self.visit(expression),
            'pseudo_type': 'Void'
        }
    
    def visit_callstmt(self, node, subroutineNameUse, subroutineArgList, location):
        name = self.visit(subroutineNameUse)
        meth = [d for m in list(self._fromimport.values()) for d in m]
        n = {}
        for a in meth:
            n.update(a)
        if subroutineArgList:
            args = self.visit(subroutineArgList)
            if name.lower() in n:
                api = n[name.lower()]
                if not isinstance(api, dict):
                    z = api.expand(args)
                    return z
            else:
                return {"type": "custom_call",
                "args": args,
                "function": name,
                "pseudo_type": "None"}         
        else:
            args = None
        return args
    
    def visit_functionsubprogram(self, node, functionPrefix, functionName, functionRange, location):
        if functionPrefix:
            d = self.visit(functionPrefix)
        name = self.visit(functionName)
        z = self.visit(functionRange) 
        params = z["_params"]
        decl = [m["decl"] for m in z["_body"] if (isinstance(m, dict) and m["type"]=="declaration")]
        d = [item for sublist in decl for item in sublist]
        arguments = [m for m in d if 'attr' in m and  (m['attr']=="IN" or  m['attr']=="INOUT") ] 
        out_pseudo_t = [m["pseudo_type"] for m in d if 'attr' in m and  (m['attr']=="OUT" or  m['attr']=="INOUT") ] 
        in_pseudo_t = [m["pseudo_type"] for m in arguments]
        if self.out:
            return_type = [m["pseudo_type"] for m in d if self.out==m["name"] ]
        else: return_type = out_pseudo_t if len(out_pseudo_t)==1 else [["tuple"]+out_pseudo_t]
        body = []
        for n in z["_body"] :
            if isinstance(n, dict) and n["type"]=="declaration":
                z = {}
                z["type"] = "declaration"
                z["decl"] = []
                for m in  n["decl"]:
                    if m not in arguments and (self.out and self.out!=m["name"] and self.recursive==False) :
                        z["decl"].append(m)
                        body.append(z)
            else: body.append(n)
        res = {"type":"function_definition", 
                "name": str(name), 
                "params":arguments, 
                "pseudo_type":['Function']+in_pseudo_t+return_type,
                "return_type": return_type[0],
                "block":body}
        self.type_env.top["functions"][res["name"]] = [res["return_type"]]
        return res


    def visit_functionrange(self,node,functionParList, NAME, RESULT, EOS, body,bodyPlusInternals, location):
        if RESULT:
            self.out = self.visit(NAME)
        if body :
            bod = self.visit(body)
        else : bod = self.visit(bodyPlusInternals)
        params = self.visit(functionParList)
        return {"_params":params, "_body": bod}
    
    def visit_deallocatestmt(self,node, allocateObjectList, STAT, variable, EOS, location):
        pass
    
    def visit_functionparlist(self, node, functionPars, location):
        if functionPars: return self.visit(functionPars)
        else: return []
    
    def visit_functionpars(self, node, functionPar, location):
        res = self.translate_list(functionPar)
        return res

    def visit_functionprefixrec(self, node,recursive, typeSpec, location):
        if recursive : self.recursive = True
        if typeSpec: self.out["type"] = self.visit(typeSpec)

    def visit_returnstmt(self, node,RETURN, expression, EOS, location):
        if expression: return {"type": "implicit_return", "value":self.visit(expression)}
        else: return {"type": "implicit_return", "value":" "}

        
        

       



       


    