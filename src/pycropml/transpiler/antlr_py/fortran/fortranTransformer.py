
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
    _fields_spec = ["commentOrNewLine", "executableProgram"]

class ExecutableProgram(AliasNode):
    _fields_spec = ["programUnit"]

class ProgramUnit(AliasNode):
    _fields_spec = ["eos", "mainProgram", "functionSubprogram", "subroutineSubprogram", "blockDataSubprogram", "module" ]

class MainProgram(AliasNode):
    _fields_spec = [ "programStmt", "mainRange"]

class SaveStmt(AliasNode):
    _fields_spec = [ "eos", "savedEntityList"]
    
class MainRange(AliasNode):
    _fields_spec = ["body", "endProgramStmt", "bodyPlusInternals", "endProgramStmt"]
    
class ProgramStmt(AliasNode):
    _fields_spec = ["PROGRAM", "NAME"]
    
class Module(AliasNode):
    _fields_spec = ["moduleStmt","moduleBody" ]

class ModuleSubprogramPartConstruct(AliasNode):
    _fields_spec = ["containsStmt", "moduleSubprogram" ]

class ModuleSubprogram(AliasNode):
    _fields_spec = ["functionSubprogram", "subroutineSubprogram" ]

class UseStmt(AliasNode):
    _fields_spec = ["NAME", "eos","ONLY","renameList","onlyList"]

class TypeDeclarationStmt(AliasNode):
    _fields_spec =["typeSpec", "entityDeclList", "DOUBLECOLON", "attrSpecSeq"]

class EntityDeclList(AliasNode):
    _fields_spec =["entityDecl"]

class Body(AliasNode):
    _fields_spec = ["bodyConstruct"]

class EntityDecl(AliasNode):
    _fields_spec =["objectName","arraySpec", "charLength","STAR","expression"]

class ImplicitStmt(AliasNode):
    _fields_spec = ["implicitSpecList"]

class SpecPartStmt(AliasNode):
    _fields_spec = ["specificationPartConstruct" ]

class SubmoduleStmt(AliasNode):
    _fields_spec = ["moduleSubprogramPartConstruct"]

class ComplexSubmodule(AliasNode):
    _fields_spec = ["moduleBody" , "moduleSubprogramPartConstruct"]

class SubroutineSubprogram(AliasNode):
    _fields_spec = ["subroutineName","subroutineRange", "RECURSIVE"]

class SubroutineRange(AliasNode):
    _fields_spec = ["subroutineParList", "endSubroutineStmt", "body","bodyPlusInternals"]

class EndSubroutineStmt(AliasNode):
    _fields_spec = ['END', "SUBROUTINE", "NAME"]

class TypeSpec(AliasNode):
    _fields_spec =["INTEGER","REAL","DOUBLEPRECISION","COMPLEX","DOUBLE","LOGICAL","CHARACTER","lengthSelector","kindSelector","PRECISION","charSelector","typeName"]

class AttrSpecSeq(AliasNode):
    _fields_spec = ["attrSpecSeq","attrSpec"]

class AssignmentStmt(AliasNode):
    _fields_spec = ["label", "NAME", "sFExprListRef", "substringRange", "expression", "eos", "nameDataRef",	"sFDummyArgNameList", "PCT"]

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

class DoConstruct(AliasNode):
    _fields_spec = ["labelDoStmt", "blockDoConstruct" ]

class BlockDoConstruct(AliasNode):
    _fields_spec = ["commaLoopControl","executionPartConstruct", "nameColon"]

class LoopControl(AliasNode):
    _fields_spec = ["variableName","expression","commaExpr","WHILE"]

class ExecutionPartConstruct(AliasNode):
    _fields_spec = ["executableConstruct", "formatStmt", "dataStmt", "entryStmt","doubleDoStmt" ]

class ExecutableConstruct(AliasNode):
    _fields_spec = ["actionStmt", "doConstruct", "ifConstruct", "caseConstruct", "whereConstruct"]

class CallStmt(AliasNode):
    _fields_spec = ["subroutineNameUse","subroutineArgList"]

class CommaLoopControl(AliasNode):
    _fields_spec = ["loopControl"]

class FunctionSubprogram(AliasNode):
    _fields_spec = ["functionPrefix", "functionName", "functionRange"]

class FunctionRange(AliasNode):
    _fields_spec = ["functionParList", "NAME", "RESULT", "eos", "body","bodyPlusInternals"]

class FunctionParList(AliasNode):
    _fields_spec = ["functionPars"]

class FunctionPars(AliasNode):
    _fields_spec = ["functionPar"]

class FunctionPrefixRec(AliasNode):
    _fields_spec = ["recursive", "typeSpec"]

class FunctionPrefixTyp(AliasNode):
    _fields_spec = ["typeSpec", "RECURSIVE"]

class DeallocateStmt(AliasNode):
    _fields_spec = ["allocateObjectList", "STAT", "variable", "eos"]

class DataStmt(AliasNode):
    _fields_spec = ["dataStmtSet"]

class Dse1(AliasNode):
    _fields_spec = ["dataStmtObject"]

class Dse2(AliasNode):
    _fields_spec = ["dataStmtValue"]

class DataStmtValue(AliasNode):
    _fields_spec = [ "namedConstantUse", "STAR", "constant"]

class DataStmtObject(AliasNode):
    _fields_spec = ["variable", "dataImpliedDo"]
    
class DerivedTypeDef(AliasNode):
    _fields_spec =["derivedTypeStmt", "derivedTypeBody"]

class DerivedTypeStmt(AliasNode):
    _fields_spec =[ "ACCESSSPEC", "NAME"]
    
class DerivedTypeBody(AliasNode):
    _fields_spec =[ "derivedTypeBody", "derivedTypeBodyConstruct"]
    
class DerivedTypeBodyConstruct(AliasNode):
    _fields_spec =["privateSequenceStmt", "componentDefStmt"]

class PrivateSequenceStmt(AliasNode):
    _fields_spec =["PRIVATE", "SEQUENCE"]

class ComponentDefStmt(AliasNode):
    _fields_spec =["componentAttrSpecList", "typeSpec","componentDeclList"]

class ComponentDeclList(AliasNode):
    _fields_spec =["componentDecl"]

class ComponentDecl(AliasNode):
    _fields_spec =["componentName", "charLength","componentArraySpec", "expression"]
    
class ComponentAttrSpecList(AliasNode):
    _fields_spec = ["componentAttrSpec"]

class ComponentAttrSpec(AliasNode):
    _fields_spec = ["componentArraySpec", "POINTER"]

class ComponentArraySpec(AliasNode):
    _fields_spec = ["explicitShapeSpecList" , "deferredShapeSpecList" ]

class ExplicitShapeSpecList(AliasNode):
    _fields_spec = ["explicitShapeSpec"]

class ExplicitShapeSpec(AliasNode):
    _fields_spec = ["lowerBound", "upperBound"]

class OpenStmt(AliasNode):
    _fields_spec = ["connectSpecList"]

class WriteStmt(AliasNode):
    _fields_spec = ["ioControlSpecList", "outputItemList"]

class FormatStmt(AliasNode):
    _fields_spec = ["fmtSpec"]

class CloseStmt(AliasNode):
    _fields_spec = ["closeSpecList"]

class SFExprListRef(AliasNode):
    _fields_spec = ["sFExprList","commaSectionSubscript"]

class ParameterStmt(AliasNode):
    _fields_spec = ["namedConstantDefList"]
    
class NamedConstantDefList(AliasNode):
    _fields_spec = ["namedConstantDef"]

class NamedConstantDef(AliasNode):
    _fields_spec = ["NAME", "expression"]

class BodyConstruct(AliasNode):
    _fields_spec = ["specificationPartConstruct", "executableConstruct"]

class ReturnStmt(AliasNode):
    _fields_spec = ["expression"]

class SpecificationPartConstruct(AliasNode):
    _fields_spec = ["implicitStmt", "parameterStmt", "formatStmt",  "entryStmt", "declarationConstruct", "includeStmt", "useStmt"]

class DeclarationConstruct(AliasNode):
    _fields_spec = ["derivedTypeDef", "interfaceBlock", "typeDeclarationStmt", "specificationStmt"]
    
class InterfaceBlock(AliasNode):
    _fields_spec = ["interfaceStmt", "interfaceBlockBody"]

class InterfaceBlockBody(AliasNode):
    _fields_spec = ["interfaceBlockBody", "interfaceBodyPartConstruct"]

class InterfaceBodyPartConstruct(AliasNode):
    _fields_spec = ["interfaceBody", "moduleProcedureStmt"]

class InterfaceBody(AliasNode):
    _fields_spec = ["functionPrefix", "NAME", "functionInterfaceRange", "SUBROUTINE", "subroutineInterfaceRange"]

class FunctionInterfaceRange(AliasNode):
    _fields_spec =  ["functionParList" ,"subprogramInterfaceBody"]

class SubroutineInterfaceRange(AliasNode):
    _fields_spec = ["subroutineParList", "subprogramInterfaceBody"]

class SubprogramInterfaceBody(AliasNode):
    _fields_spec = ["specificationPartConstruct", "subprogramInterfaceBody"]

class CaseConstruct(AliasNode):
    _fields_spec = ["NAME", "expression", "selectCaseRange"]


class AllocateStmt(AliasNode):
    _fields_spec = ["allocationList", "variable"]
    
class AllocationList(AliasNode):
    _fields_spec = ["allocation"]
    
class Allocation(AliasNode):
    _fields_spec = ["allocateObject",  "allocatedShape"]
    
class AllocateObject(AliasNode):
    _fields_spec = ["variableName", "allocateObject", "fieldSelector"]
    
class AllocatedShape(AliasNode):
    _fields_spec = ["sectionSubscriptList"]
    
class FieldSelector(AliasNode):
    _fields_spec = ["sectionSubscriptList", "PCT", "NAME"]


class SelectCaseRange(AliasNode):
    _fields_spec = ["selectCaseBody", "endSelectStmt"]

    
class SelectCaseBody(AliasNode):
    _fields_spec = ["caseStmt", "selectCaseBody", "caseBodyConstruct"]
    
class CaseBodyConstruct(AliasNode):
    _fields_spec = ["caseStmt", "executionPartConstruct"]
    
class CaseStmt(AliasNode):
    _fields_spec = ["caseSelector"]
    
class CaseSelector(AliasNode):
    _fields_spec = ["caseValueRangeList"]
    

class CaseValueRangeList(AliasNode):
    _fields_spec = ["caseValueRange"]

class CaseValueRange(AliasNode):
    _fields_spec = ["expression", "COLON"]

class SubroutineArgList(AliasNode):
    _fields_spec = ["subroutineArg"]

class AccessStmt(AliasNode):
    _fields_spec = ["ACCESSSPEC", "accessIdList" ]

class OutputItemList1(AliasNode):
    _fields_spec = ["expression", "outputImpliedDo", "outputItemList1"]
 
class ActionStmt(AliasNode):
     _fields_spec =  ["arithmeticIfStmt", "assignmentStmt", "assignStmt", "backspaceStmt", "callStmt", "closeStmt",
	                    "continueStmt", "endfileStmt", "gotoStmt", "computedGotoStmt", "assignedGotoStmt", "ifStmt"  , "inquireStmt", 
                     "openStmt", "pauseStmt", "printStmt", "readStmt", "returnStmt", "rewindStmt", "stmtFunctionStmt", "stopStmt", 
                     "writeStmt" , "allocateStmt" , "cycleStmt" , "deallocateStmt" , "exitStmt", "nullifyStmt" , "pointerAssignmentStmt" , "whereStmt"]

class AcImpliedDo(AliasNode):
    _fields_spec = ["acImpliedDo","impliedDoVariable" ,"expression"]
    
class SFExprList(AliasNode):
    _fields_spec = ["expression", "DOUBLECOLON",  "COLON"]

class SubscriptTripletTail(AliasNode):
    _fields_spec = ["expression", "DOUBLECOLON",  "COLON"]



class Transformer(BaseNodeTransformer):
    
    def visit_SubroutineArgList(self, node):
        return SubroutineArgList.from_spec(node)

    def visit_AllocateStmt(self, node):
        return AllocateStmt.from_spec(node)
    
    def visit_AllocationList(self, node):
        return AllocationList.from_spec(node)
    
    def visit_Allocation(self, node):
        return Allocation.from_spec(node)
    
    def visit_AllocateObject(self, node):
        return AllocateObject.from_spec(node)
    
    def visit_AllocatedShape(self, node):
        return AllocatedShape.from_spec(node)
    
    def visit_FieldSelector(self, node):
        return FieldSelector.from_spec(node)
    
    def visit_EndSubroutineStmt(self, node):
        return EndSubroutineStmt.from_spec(node)
    def visit_CaseConstruct(self, node):
        return CaseConstruct.from_spec(node)
    def visit_SelectCaseRange(self, node):
        return SelectCaseRange.from_spec(node)
    def visit_SelectCaseBody(self, node):
        return SelectCaseBody.from_spec(node)
    def visit_CaseBodyConstruct(self, node):
        return CaseBodyConstruct.from_spec(node)
    def visit_CaseStmt(self, node):
        return CaseStmt.from_spec(node)
    def visit_CaseSelector(self, node):
        return CaseSelector.from_spec(node)
    def visit_CaseValueRangeList(self, node):
        return CaseValueRangeList.from_spec(node)
    def visit_CaseValueRange(self, node):
        return CaseValueRange.from_spec(node)   
    def visit_SubprogramInterfaceBody(self, node):
        return SubprogramInterfaceBody.from_spec(node)
    def visit_SubroutineInterfaceRange(self, node):
        return SubroutineInterfaceRange.from_spec(node)   
    def visit_FunctionInterfaceRange(self, node):
        return FunctionInterfaceRange.from_spec(node)   
    def visit_InterfaceBody(self, node):
        return InterfaceBody.from_spec(node)   
    def visit_InterfaceBodyPartConstruct(self, node):
        return InterfaceBodyPartConstruct.from_spec(node)
    def visit_InterfaceBlockBody(self, node):
        return InterfaceBlockBody.from_spec(node)    
    def visit_InterfaceBlock(self, node):
        return InterfaceBlock.from_spec(node)
    def visit_DeclarationConstruct(self, node):
        return DeclarationConstruct.from_spec(node)
    def visit_SFExprListRef(self, node):
        return SFExprListRef.from_spec(node)    
    def visit_SpecificationPartConstruct(self, node):
        return SpecificationPartConstruct.from_spec(node)
    def visit_BodyConstruct(self, node):
        return BodyConstruct.from_spec(node)
    def visit_ReturnStmt(self, node):
        return ReturnStmt.from_spec(node)
    def visit_ParameterStmt(self, node): 
        return ParameterStmt.from_spec(node)  
    def visit_NamedConstantDefList(self, node):
         return NamedConstantDefList.from_spec(node)
    def visit_NamedConstantDef(self, node):
         return NamedConstantDef.from_spec(node)
    def visit_ExecutionPartConstruct(self, node):
        return ExecutionPartConstruct.from_spec(node)   
    def visit_Body(self, node):
        return Body.from_spec(node)
    def visit_DoConstruct(self, node):
        return DoConstruct.from_spec(node)
    def visit_ComponentArraySpec(self, node):
        return ComponentArraySpec.from_spec(node)
    def visit_FormatStmt(self, node):
        return FormatStmt.from_spec(node)
    def visit_CloseStmt(self, node):
        return CloseStmt.from_spec(node)
    def visit_OpenStmt(self, node):
        return OpenStmt.from_spec(node)
    def visit_WriteStmt(self, node):
        return WriteStmt.from_spec(node)
    def visit_ExplicitShapeSpecList(self, node):
        return ExplicitShapeSpecList.from_spec(node)
    def visit_ExplicitShapeSpec(self, node):
        return ExplicitShapeSpec.from_spec(node)
    def visit_ComponentAttrSpecList(self, node):
        return ComponentAttrSpecList.from_spec(node)
    def visit_ComponentAttrSpec(self, node):
        return ComponentAttrSpec.from_spec(node)
    def visit_ComponentDefStmt(self, node):
        return ComponentDefStmt.from_spec(node)
    def visit_ComponentDeclList(self, node):
        return ComponentDeclList.from_spec(node)
    def visit_ComponentDecl(self, node):
        return ComponentDecl.from_spec(node) 
    def visit_DerivedTypeDef(self, node):
        return DerivedTypeDef.from_spec(node)
    def visit_DerivedTypeStmt(self, node):
        return DerivedTypeStmt.from_spec(node)
    def visit_DerivedTypeBody(self, node):
        return DerivedTypeBody.from_spec(node)
    def visit_DerivedTypeBodyConstruct(self, node):
        return DerivedTypeBodyConstruct.from_spec(node)
    def visit_PrivateSequenceStmt(self, node):
        return PrivateSequenceStmt.from_spec(node)
    def visit_Dse1(self, node):
        return Dse1.from_spec(node)
    def visit_Dse2(self, node):
        return Dse2.from_spec(node)
    def visit_DataStmtValue(self, node):
        return DataStmtValue.from_spec(node)
    def visit_DataStmtObject(self, node):
        return DataStmtObject.from_spec(node)
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
    def visit_UseStmt(self, node):
        return UseStmt.from_spec(node)
    def visit_ImplicitStmt(self, node):
        return ImplicitStmt.from_spec(node)
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
    def visit_MainProgram(self, node):
        return MainProgram.from_spec(node)
    def visit_MainRange(self, node):
        return MainRange.from_spec(node)
    def visit_ProgramStmt(self, node):
        return ProgramStmt.from_spec(node)
    def visit_SaveStmt(self, node):
        return SaveStmt.from_spec(node)
    def visit_DataStmt(self, node):
        return DataStmt.from_spec(node)
    def visit_AccessStmt(self, node):
        return AccessStmt.from_spec(node)
    def visit_OutputItemList1(self, node):
        return OutputItemList1.from_spec(node)
    def visit_ExecutableConstruct(self, node):
        return ExecutableConstruct.from_spec(node)
    def visit_ActionStmt(self, node):
        return ActionStmt.from_spec(node)
    def visit_AcImpliedDo(self, node):
        return AcImpliedDo.from_spec(node)
    def visit_SFExprList(self, node):
        return SFExprList.from_spec(node)
    def visit_SubscriptTripletTail(self, node):
        return SubscriptTripletTail.from_spec(node)

class AstTransformer():
    def __init__(self, tree, code :str = None ,comments: str=None, env=None):
        self.tree = tree
        self.base = 0
        self.comments = comments
        if env: self.type_env = env 
        else: 
            self.type_env = Env(dict(list(TYPED_API.items())), None)
            self.type_env['arrays']={}
        self.code : str = code
        if self.code:
            self.codelines = self.code.split("\n")

    def transformer(self):
        self.type_env['functions'] = {}
        self.assign = False
        self.index = []
        self.indexnames = []
        self.function_name = 'top level'
        self.definitions = []
        self.dependencies=[]
        self.recursive = False
        self.struct={}
        self.notdeclared = set()
        self.out = None
        self.selector = []
        self._imports=[]
        self._fromimport = {}
        self._definition_index = {'functions': {}}
        self.decl = []
        self.attr = {}
        self._attr_index = {}
        self.bodycomp = []
        self._hierarchy = {}
        self.visit_top_level(self.tree.executableProgram.programUnit)
        #self.signature = self.visit_definitions()
        body = self.visit(self.tree)
        return {'dependencies':self.dependencies, 'env':self.type_env, 'struct': self.struct, "index":self.index, 'body': body if isinstance(body, list) else [body]}
    

    def visit_top_level(self, nodes):
        for node in nodes:
            for n in node.children:
                if n.__class__.__name__ == "SubroutineSubprogram": #or n.__class__.__name__ == "FunctionSubprogram": #isinstance(n, SubroutineSubprogram)
                    self.definitions.append(('function', str(n.subroutineName.NAME)))
                    self._definition_index['functions'][str(n.subroutineName.NAME)] = n
                    if n.subroutineRange.subroutineParList.subroutinePars:
                        self.type_env.top['functions'][str(n.subroutineName.NAME)] = [
                        'Function'] + ([None] * len(n.subroutineRange.subroutineParList.subroutinePars)) + [None]
                    else:
                        self.type_env.top['functions'][str(n.subroutineName.NAME)] = [
                        'Function'] + [None]
                        
                    self.type_env.top[str(n.subroutineName.NAME)] = self.type_env.top['functions'][str(n.subroutineName.NAME)]
                elif  n.__class__.__name__ == "FunctionSubprogram": #isinstance(n, SubroutineSubprogram)
                    self.definitions.append(('function', str(n.functionName.NAME)))
                    self._definition_index['functions'][str(n.functionName.NAME)] = n
                    if n.functionRange.functionParList.functionPars:
                        self.type_env.top['functions'][str(n.functionName.NAME)] = [
                        'Function'] + ([None] * len(n.functionRange.functionParList.functionPars.functionPar)) + [None]
                    else:
                        self.type_env.top['functions'][str(n.functionName.NAME)] = [
                        'Function'] + [None]
                        
                    self.type_env.top[str(n.functionName.NAME)] = self.type_env.top['functions'][str(n.functionName.NAME)]
                if n.__class__.__name__ == "Module" : #isinstance(n, SubroutineSubprogram)
                    name = str(n.moduleStmt.moduleName)
                    self._attr_index[name] = {}
                    self.type_env.top[name] = {}
                    self.definitions.append(('module',name))

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

    def visit_definitions(self):
        definitions = []
        for definition in self.definitions:
            if definition[0] == 'function':
                definitions.append(
                    self._definition_index['functions'][definition[1]])
            else:
                print("error")  # do Assert
        return definitions
    
    def visit_program(self, node, commentOrNewLine, executableProgram, comments, location):
        res = self.visit(executableProgram)
        if isinstance(res, dict) : res['comments']= comments
        elif isinstance(res, list): res.append({"type":"comments", "comments":comments})
        return res


    def visit_executableprogram(self, node,programUnit, comments, location):
        res = self.translate_list(programUnit)
        return res 
    
    def visit_programunit(self, node,eos, mainProgram,functionSubprogram,subroutineSubprogram,blockDataSubprogram, module,comments, location):
        if mainProgram : res =  self.visit(mainProgram)
        if functionSubprogram : res =  self.visit(functionSubprogram)
        if subroutineSubprogram : res =  self.visit(subroutineSubprogram)
        if blockDataSubprogram : res =  self.visit(blockDataSubprogram)
        if module : res =  self.visit(module)
        if isinstance(res, dict) : res['comments']= comments
        return res
            

    def visit_mainprogram(self, node,programStmt, mainRange, comments,location):
        self.sel=[]
        res = self.visit(mainRange)
        if programStmt:
            return {"type":"test", "name":str(programStmt.NAME), "body":res, "comments":comments}
        if isinstance(res, dict) : res['comments']= comments
        elif isinstance(res, list): res.append({"type":"comments", "comments":comments})
        return res
    
    def visit_mainrange(self, node, body, endProgramStmt, bodyPlusInternals,comments,location):
        if body:
            body = self.visit(body.bodyConstruct)
        if bodyPlusInternals:
            body = self.visit(bodyPlusInternals)
        return body
    
    def visit_bodyplusinternals(self, node, body, internalSubprogram, containsStmt, bodyPlusInternals, comments, location):
        res = []
        internal = self.visit(internalSubprogram)
        if bodyPlusInternals:
            body = self.visit(bodyPlusInternals)
            res.append(body)
            res.append(internal)
            return res
        elif body:
            body = self.visit(body)
            res.append(body)
            res.append(internal)
        else: return internal

        

    def visit_parameterstmt(self, node, namedConstantDefList, comments,location):
        res = self.visit(namedConstantDefList)
        return res
    
    def visit_namedconstantdeflist(self, node, namedConstantDef,comments, location):
        res = self.translate_list(namedConstantDef)
        return res

    def visit_namedconstantdef(self, node, NAME, expression,comments, location):
        pseudo_type = self.type_env[str(NAME)]
        if not pseudo_type: self.notdeclared.add(str(NAME))
        res = self.visit(expression)
        return {"type":"assignment", "op":"=", "target":{"type":"local", "name":str(NAME), "pseudo_type":pseudo_type}, "value":res, "comments":comments}

    
    def visit_module(self, node, moduleStmt, moduleBody, comments, location):
        body =[]
        self.type_env['arrays'] = {}
        name = self.visit(moduleStmt.moduleName)
        self.type_env, old_type_env = self.type_env.top.child_env({}), self.type_env
        if moduleBody : 
            body = self.visit(moduleBody)
        res = {"type":"module", "name":name, "block":body, "comments":comments}
        self.notdeclared = set()
        self.type_env = Env(dict(list(TYPED_API.items())), None)
        self.type_env['arrays'] = {}
        return res
    
    def visit_submodulestmt(self, node, moduleSubprogramPartConstruct, location):
        return self.visit(moduleSubprogramPartConstruct)
    
    def visit_specpartstmt(self, node, specificationPartConstruct, comments,location):
        res = self.visit(specificationPartConstruct)
        if res: res["comments"] = comments
        return res

    def visit_internalsubprogram(self, node, specificationPartConstruct, comments, location ):
        res = self.visit(specificationPartConstruct)
        if res: res["comments"] = comments
        return res
    
    def visit_bodyconstruct(self, node, specificationPartConstruct, executableConstruct, comments, location):
        if specificationPartConstruct: res =self.visit(specificationPartConstruct)
        if executableConstruct: res = self.visit(executableConstruct)
        if isinstance(res, dict): res["comments"] = comments
        if isinstance(res, list): res.append({"type":"comments", "comments":comments})
        return res
    
    def visit_executableconstruct(self, node, actionStmt, doConstruct, ifConstruct, caseConstruct,  whereConstruct, comments, location):
        if actionStmt: return self.visit(actionStmt)
        if doConstruct: return self.visit(doConstruct)
        if ifConstruct: return self.visit(ifConstruct)
        if caseConstruct: return self.visit(caseConstruct)
        if whereConstruct: return self.visit(whereConstruct)
        

    def visit_specificationpartconstruct(self, node, implicitStmt, parameterStmt, formatStmt,  entryStmt, declarationConstruct, includeStmt, useStmt,comments, location):
        if implicitStmt: res = self.visit(implicitStmt)
        if parameterStmt: res = self.visit(parameterStmt)
        if formatStmt: res = self.visit(formatStmt)
        if entryStmt: res = self.visit(entryStmt)
        if declarationConstruct: res = self.visit(declarationConstruct)
        if includeStmt: res = self.visit(includeStmt)
        if useStmt: res = self.visit(useStmt)
        if res and isinstance(res, dict):
            res["comments"] =  comments
        elif comments and isinstance(res, list): 
            res.append({"type":"comments", "comments":comments})
        return res

    def visit_declarationconstruct(self, node, derivedTypeDef, interfaceBlock, typeDeclarationStmt, specificationStmt,comments, location):
        if derivedTypeDef: res = self.visit(derivedTypeDef)
        if interfaceBlock: res = self.visit(interfaceBlock)
        if typeDeclarationStmt: res = self.visit(typeDeclarationStmt)
        if specificationStmt:   
            res = self.visit(specificationStmt) 
        if res and isinstance(res, dict): res["comments"] =  comments
        elif res and comments and isinstance(res, list): res.append({"type":"comments", "comments":comments})
        return res
    
  
    
    def visit_modulesubprogrampartconstruct(self, node,moduleSubprogram,containsStmt,comments, location):
        if moduleSubprogram : 
            res = self.visit(moduleSubprogram)
            res["comments"] = comments
            return res
         
    
    def visit_modulesubprogram(self, node,functionSubprogram , subroutineSubprogram,comments, location):
        if functionSubprogram : return self.visit(functionSubprogram)
        if subroutineSubprogram : return self.visit(subroutineSubprogram)

    def visit_complexsubmodule(self, node, moduleBody, moduleSubprogramPartConstruct,comments,location):
        res1 = self.visit(moduleBody)
        res = res1 if isinstance(res1, list) else [res1] 
        z = self.visit(moduleSubprogramPartConstruct)
        res.append(z) 
        return res

    def visit_complexspecpart(self, node,moduleBody, specificationPartConstruct,comments, location):
        res1 = self.visit(moduleBody)
        res = res1 if isinstance(res1, list) else [res1] 
        z = self.visit(specificationPartConstruct)
        res.append(z) 
        return res


    def visit_usestmt(self, node, NAME, eos,ONLY,renameList,onlyList,comments,location):
        res = {}
        if renameList:
            #res = {"type":"import", "module": self.visit(renameList) }
            pass
        elif onlyList:
            #res = {"type":"import", "module": self.visit(onlyList) }
            pass
        elif ONLY:
            pass
        else:
            res = {"type":"import", "name": str(node.NAME),
                        "comments":comments }
            if str(node.NAME) in SYSTEM_API: self._fromimport[str(node.NAME)] = list(SYSTEM_API.values())
            else :                 
                self._imports.append(str(NAME))
                self.type_env['_%s' % str(NAME)], self.type_env[str(NAME)] = self.type_env[str(NAME)], 'library'
        return res
    
    def translate_list(self, inputs):
        res = []
        for arg in inputs:
            b = self.visit(arg)
            res.append(b)
        return res

    def visit_containsstmt(self, node, CONTAINS, eos ,comments, location ):
        return None

    def visit_implicitstmt(self, node, implicitSpecList,comments,location):
        return None
    
    def _attrFromCode(self, location, endline):
        inp, out = [], []
        codes = self.codelines[location-1:endline]
        num = None
        for k,v in enumerate(codes):
            if "!input" in v.lower() or "!output" in v.lower() or '!inout' in v.lower() :
                num = k
                break
        if not num: return [], []
        location = num
        line_ = codes[location]
        k = 0
        while line_.lower().endswith("!input") or line_.lower().endswith("!output") or line_.lower().endswith("!inout") :
            line=line_.replace(" ", "")\
                    .replace("&", "")\
                    .split(",")
            if line[-1].lower().endswith("!input"):
                for i,j in enumerate(line):
                    if i==0 and "(" in j:
                        inp.append(j[j.index("(")+1:])
                    elif i!=len(line)-1:
                        inp.append(j)
            elif line[-1].lower().endswith("!output"):
                for i,j in enumerate(line):
                    if i==len(line)-1 and ")" in j:
                        out.append(j[:j.index(")")])
                    else:
                        out.append(j)
            elif line[-1].lower().endswith("!inout") :
                for i,j in enumerate(line):
                    if i==0 and "(" in j:
                        inp.append(j[j.index("(")+1:])
                        out.append(j[j.index("(")+1:])
                    elif i!=len(line)-1:
                        inp.append(j)
                        out.append(j)
                    elif i==len(line)-1 and ")" in j:
                        out.append(j[:j.index(")")])
                        inp.append(j[:j.index(")")])
                    else:
                        out.append(j)
                        inp.append(j)
            k = k+1
            line_ = codes[location + k]
        return inp, out
                        
                

    def visit_subroutinesubprogram(self, node, subroutineName,subroutineRange, RECURSIVE,comments, location):
        self._imports=[]
        self.index = []
        self.indexnames = []
        self.sel = []
        self.notdeclared=set()
        name = self.visit(subroutineName)
        self.type_env, old_type_env = self.type_env.top.child_env({}), self.type_env
        self.type_env['arrays']={}
        z = self.visit(subroutineRange) 
        endline = z["endline"]
        params = z["_params"]
        inp, out = self._attrFromCode(location[0], endline)
        decl = [m["decl"] for m in z["_body"] if (isinstance(m, dict) and m["type"]=="declaration")]
        d = [item for sublist in decl for item in sublist]
        arguments, inputs_name =[], []
        outputs, outputs_name = [], []
        for j in params:
            for m in d:
                n = 0
                if m["name"]==j and (('attr' in m and  ((m['attr']=="IN" or m['attr']=="in" ) or  (m['attr']=="INOUT" or m['attr']=="inout"))) or m["name"] in inp):
                    arguments.append(m)
                    inputs_name.append(m["name"])
                    n = 1
                if m["name"]==j  and (('attr' in m and  ((m['attr']=="OUT" or m['attr']=="out") or  (m['attr']=="INOUT" or m['attr']=="inout"))) or m["name"]in out):
                    outputs.append(m)
                    outputs_name.append(m["name"])
                    n = 1
                if n ==1: break
        
        out_pseudo_t = [m["pseudo_type"] for m in outputs] 
        in_pseudo_t = [m["pseudo_type"] for m in arguments]
        return_type = out_pseudo_t if len(out_pseudo_t)==1 else [["tuple"]+out_pseudo_t]
        body = []
        for n in z["_body"] :
            if isinstance(n, dict) and n["type"]=="declaration":
                v = {}
                v["type"] = "declaration"
                v["comments"]= n["comments"]
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
                "block":body,
                "imports":self._imports,
                "comments":comments,
                'inputs_name':inputs_name,
                'inputs_pos':[k for k,v in enumerate(params) if v in inputs_name],
                'outputs_pos':[k for k,v in enumerate(params) if v in outputs_name],
                "outputs_name":outputs_name,
                'notdeclared':self.notdeclared,
                'inputs':arguments,
                'outputs':outputs,
                'index': self.index,
                'indexnames':self.indexnames,
                'env':self.type_env}
        from copy import deepcopy
        outs = deepcopy(outputs)
        outs_ = []
        for o in outs:
            o['type'] = "local"
            outs_.append(o)
        #self.type_env.top["functions"][res["name"]] = [res["return_type"]]
        
        if len(outs_)>1 :
            type_ = "tuple"
            res["block"].append({'type': 'implicit_return',
                                'value': {'type': type_,
                                'pseudo_type': return_type[0],
                                'elements': outs_},
                                'pseudo_type':return_type[0]
                                })
        elif len(outs_)==1: 
            type_ = "local"
            res["block"].append({'type': 'implicit_return',
                            'value': {'type': type_,
                            'pseudo_type': return_type[0],
                            'name': outs_[0]["name"]},
                            'pseudo_type':return_type[0]
                            })

        self.type_env = old_type_env
        self._imports=[]
        self.notdeclared = set()
        self._imports=[]
        self.index = []
        self.indexnames = []
        return res

    def visit_subroutinerange(self, node, subroutineParList, body,bodyPlusInternals,endSubroutineStmt,comments,location):
        if body :
            bod = self.visit(body.bodyConstruct)
        else : bod = self.visit(bodyPlusInternals)
        if subroutineParList.subroutinePars:
            params = self.translate_list(subroutineParList.subroutinePars)
        else: params = []
        endline = self.visit(endSubroutineStmt)
        return {"_params":params, "_body": bod, "endline":endline}
    
    def visit_endsubroutinestmt(self, node, END, SUBROUTINE, NAME, comments,location ):
        return location[0]
    
    def visit_body(self, node,bodyConstruct, comments, location):
        return self.visit(bodyConstruct)
    
    def visit_entitydecllist(self, node,entityDecl, comments,location):
        if not isinstance(entityDecl, list):
            return self.visit(entityDecl)
        res = self.translate_list(entityDecl)
        return res

    def visit_entitydecl(self, node, objectName, arraySpec, charLength,STAR,expression, comments,location) :
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
                z = {"name":str(objectName), "dim": len(spec), "elts":spec}
                self.type_env['arrays'].update({str(objectName): spec})
                return z
        elif expression:
            return {"name":objectName, "value":self.visit(expression)}
        else:
            return {"name":objectName}

    

    
    def visit_typedeclarationstmt(self, node, typeSpec, entityDeclList, DOUBLECOLON, attrSpecSeq,comments,location):
        z = []
        attr = {}
        names = self.visit(entityDeclList)
        elemtype_ = self.visit(typeSpec)
        attr = None
        if attrSpecSeq:
            self.attr = {}
            attr = self.visit(attrSpecSeq)
            
        #if attr and "DIMENSION" in attr and "ALLOCATABLE" in attr and attr["DIMENSION"] == [":"]:
        if attr and ("allocatable" in attr or "ALLOCATABLE" in attr):
            typ = "list"
            pseudo_type = ["list", elemtype_]
        else : 
            typ = elemtype_
            pseudo_type = elemtype_
        for j in names:
            zj = {"type":typ, "name": str(j["name"]), "pseudo_type":pseudo_type}
            if "dim" in j and typ!="list":
                zj["type"] = "array"
                zj["dim"] = j["dim"]
                zj["elts"] = j["elts"]
                zj["pseudo_type"] = ["array", elemtype_]  
                self.type_env['arrays'].update({zj["name"]: zj["elts"] }) 
            elif attr and  "DIMENSION" in attr and ("ALLOCATABLE" not in attr and "allocatable" not in attr):
                zj["type"] = "array"
                zj["dim"] = len(attr["DIMENSION"])
                zj["elts"] = attr["DIMENSION"]
                zj["pseudo_type"] = ["array", elemtype_]  
                self.type_env['arrays'].update({zj["name"]: zj["elts"] })                     
            self.type_env.top[str(j["name"])] = zj["pseudo_type"]
            if "value" in j: zj["value"] = j["value"]
            if attr and 'INTENT' in attr : zj["attr"] = attr['INTENT']
            z.append(zj)     
        res = {"type":"declaration", "decl":z, "comments":comments}
        return res
    
    def visit_attrspecseq(self, node, attrSpecSeq,attrSpec,comments, location):
        if ("DIMENSION" in dir(attrSpec) or "dimmension" in dir(attrSpec) ) : self.attr.update({"DIMENSION": self.visit(attrSpec.arraySpec)})
        elif ("INTENT" in dir(attrSpec) or "intent" in dir(attrSpec)):  self.attr.update({"INTENT": self.visit(attrSpec.intentSpec)})
        else : self.attr.update({self.visit(attrSpec):None})

        if attrSpecSeq: 
            node = attrSpecSeq
            attrSpecSeq = node.attrSpecSeq
            attrSpec = node.attrSpec
            self.visit_attrspecseq(node, attrSpecSeq,attrSpec,comments, location)
        
        return self.attr 
    
    def visit_typespec(self, node, INTEGER,REAL,DOUBLEPRECISION,DOUBLE,COMPLEX,LOGICAL,CHARACTER,lengthSelector,kindSelector,PRECISION,charSelector,typeName,comments,location):
        if INTEGER:
            type_ = "int"
        if REAL:
            type_ = "float"
        if DOUBLEPRECISION or DOUBLE:
            type_ = "double"
        if LOGICAL:
            type_ = "bool"
        if CHARACTER :
            type_ = "str" 
        if DOUBLE:
            type_ = "float"
        if typeName:
            type_ = self.visit(typeName)
            
        return type_
    
    def visit_terminal(self, node, value, comments, location):
        return str(self.visit(value))
    
    def visit_savestmt(self, node, eos, savedEntityList, comments,location):
        com = {}
        """if eos:
            com =self.visit(eos)
        if savedEntityList:
            print(f"visit_savestmt not impl {location}")
        return com"""
        print(f"visit_savestmt not impl {location}")
        return None
    
    def visit_assignmentstmt(self, node, label, NAME, sFExprListRef, substringRange, expression,comments, eos, 
                            nameDataRef, sFDummyArgNameList, PCT,location):

        id_type = self.type_env.top[str(NAME)]
        if id_type is None:
            self.notdeclared.add(str(NAME))
            
        if sFDummyArgNameList:
            pass
        elif PCT:
            nam = self.visit(nameDataRef)
            if not sFExprListRef:
                return {"type":"assignment", 
                        "target":{"type":"attr", 
                                  "object":{"type":self.type_env.top[str(NAME)], "name": str(NAME), "pseudo_type":self.type_env.top[str(NAME)]},
                                  "name":nam
                                  },
                        "value":self.visit(expression),"op":"=",
                        "comments":comments}
        else :
            if not sFExprListRef and not substringRange :
                res = {"type":"assignment",
                        "target": {"type":"local", "name":str(NAME), "pseudo_type": self.type_env.top[str(NAME)]} ,
                        "value" : self.visit(expression),
                        "pseudo_type":"VOID","op":"=",
                        "comments":comments}
                if isinstance(res["target"]["pseudo_type"], list) and (res["target"]["pseudo_type"][0]=="array" or res["target"]["pseudo_type"][0]=="list") and res["value"]["pseudo_type"] in ["int", "float", "str", "bool"]:
                    type_ = res["value"]["pseudo_type"]
                    res["value"] = {'type': res["target"]["pseudo_type"][0],
                                    'elements': {'type': 'binary_op',
                                    'op': '*',
                                    'left': {'type': 'list',
                                    'pseudo_type': ['list', type_],
                                    'elements': [res["value"]]},
                                    'right': self.type_env['arrays'][res["target"]["name"]],
                                    'pseudo_type': ['list', type_]},
                                    'pseudo_type': ["array",type_]}
                if self.recursive and str(NAME)==self.out:
                        return {"type":"implicit_return",
                                "value": res["value"],
                                "pseudo_type": res["target"]["pseudo_type"],
                        "comments":comments}
                return res
            elif sFExprListRef and not nameDataRef:
                if not label:
                    if not substringRange:
                        value = self.visit(expression)
                        return {'type': 'assignment',
                            'target': {'type': 'index',
                                'sequence': {'type': 'local',
                                'name': self.visit(NAME),
                                'pseudo_type': id_type},
                                'index': self.visit(sFExprListRef),
                                'pseudo_type':  value["pseudo_type"]},
                            'value': value,
                            'pseudo_type': 'Void',
                        "comments":comments}
        
    def visit_sfexprlistref(self, node,sFExprList, commaSectionSubscript,comments, location):
        
        if len(commaSectionSubscript)==0:
            return  self.visit(sFExprList)       
        else:
            return self.translate_list(commaSectionSubscript)
        

    def visit_expression(self, node, level5Expr, expression, definedBinaryOp, comments,location):
        if definedBinaryOp:
            print(f"definedBinaryOp not yet implemented at {location}")
        else: 
            res = self.visit(level5Expr)
            return res[0]
    
    def visit_datastmt(self, node, dataStmtSet, comments,location):
        res = self.visit(dataStmtSet)
        return res

    def visit_datastmtset(self, node,dse1 , dse2, comments,location):
        res1 = self.visit(dse1)
        res2 = self.visit(dse2)
        if len(res1)==1:
            if len(res2)>1:
                return    {'type': 'assignment',
                            'target': res1[0],
                            'value': {'type': 'array',
                                'elements': [{'type': res1[0]["pseudo_type"][-1], 'value': r[0], 'pseudo_type': res1[0]["pseudo_type"][-1]}  for r in res2 ],
                                'dim': 1,
                                'pseudo_type': res1[0]["pseudo_type"]},
                            'pseudo_type': 'Void',
                        "comments":comments}
            else:
                return {'type': 'assignment',
                            'target': res1[0],
                            'value': {'type': res1[0]["pseudo_type"], "value": res2[0][0], 'pseudo_type': res1[0]["pseudo_type"]},
                            'pseudo_type':"void",
                        "comments":comments}
        else:
            return [{"type":"assignment", "op":"=", "target":j, "value":{"type":j["pseudo_type"],"value":k[0],"type":j["pseudo_type"] }, 'pseudo_type':"void",
                        "comments":comments} for j,k in zip(res1, res2)]
                
    
    def visit_dse1(self, node, dataStmtObject,comments, location):
        if isinstance(dataStmtObject, list):
            res = self.translate_list(dataStmtObject)
        else: res = self.visit(dataStmtObject)
        return res

    def visit_dse2(self, node, dataStmtValue, comments,location):
        if isinstance(dataStmtValue, list):
            res = self.translate_list(dataStmtValue)
        else: res = self.visit(dataStmtValue)
        return res

    def visit_datastmtvalue(self, node,constant, STAR, namedConstantUse,comments, location):
        if constant and namedConstantUse:
            print(f'datastmt not implemented at {location}')
        elif  isinstance(constant, list):
            return self.translate_list(constant)
        else:
            res = self.visit(constant)
            return res

    def visit_datastmtobject(self, node, variable, dataImpliedDo , comments,location):
        if variable: 
            res = self.visit(variable)
            return {"type":"local", "name":res, "pseudo_type":self.type_env.top[res],
                        "comments":comments}
        elif dataImpliedDo:
            print(f'datastmtobject not implemented at {location}')
        return

    def visit_derivedtypedef(self,node, derivedTypeStmt, derivedTypeBody,comments, location):
        self.bodycomp = []
        name = self.visit(derivedTypeStmt)
        elements = self.visit(derivedTypeBody)
        res = {"type":"declaration", "decl":[{"type":"struct", "name":name, "elements": self.bodycomp}],
                        "comments":comments}
        self.type_env.top[name] = self.bodycomp
        self.struct.update({name:self.bodycomp})
        return res

    def visit_derivedtypestmt(self, node, ACCESSSPEC, NAME, comments,location):
        return self.visit(NAME)

    def visit_derivedtypebody(self, node, derivedTypeBody, derivedTypeBodyConstruct, comments,location):
        z = self.visit(derivedTypeBodyConstruct)
        self.bodycomp.append(z)
        if derivedTypeBody is not None:
            r = self.visit(derivedTypeBody)
        return self.bodycomp
 
    
    def visit_derivedtypebodyconstruct(self, node,privateSequenceStmt, componentDefStmt,comments, location):
        res =  self.visit(componentDefStmt)
        if res: res["comments"] = comments
        return res

    def visit_privatesequencestmt(self, node,PRIVATE, SEQUENCE, location):
        return

    def visit_componentdefstmt(self, node, componentAttrSpecList, typeSpec, componentDeclList, comments,location):
        type_ = {"type":self.visit(typeSpec)}
        other_type_= self.visit(componentAttrSpecList)
        if other_type_:
            if "dim" in other_type_:
                type_["pseudo_type"] = ["array", type_["type"] ]
                type_["type"]="array"
                other_type_["elts"] = other_type_["dim"]
                other_type_["dim"] = len(other_type_["elts"])
            type_.update(other_type_)
        else:
            type_["pseudo_type"] = type_["type"]
        r = self.visit(componentDeclList)
        res = []
        for p in r:
            p.update(type_)
            res.append(p)
        res2 = {"type":"declaration", "decl":res, "comments":comments}
        return res2

    def visit_componentattrspeclist(self, node, componentAttrSpec, comments,location):
        res = {}
        for f in componentAttrSpec:
            r = self.visit(f)
            if r is not None:
                if isinstance(r, list):
                    res.update(r[0])
                else: res.update(r)
        return res

    def visit_componentattrspec(self, node, componentArraySpec, POINTER,comments, location):
        if POINTER:
            print(f"ComponentAttrSpec not well implemented at {location}")
            return {"pointer":"yes"}
        else:
            res = self.visit(componentArraySpec)
            return {"dim":res}

    def visit_componentdecllist(self, node,componentDecl, comments, location):
        return self.visit(componentDecl)
    
    def visit_componentarrayspec(self, node, explicitShapeSpecList, deferredShapeSpecList,comments, location):
        if explicitShapeSpecList:
            return self.visit(explicitShapeSpecList)
        elif deferredShapeSpecList:
            return self.visit(deferredShapeSpecList)

    def visit_explicitshapespeclist(self, node, explicitShapeSpec,comments, location) :
        res = self.translate_list(explicitShapeSpec)
        return res
        
    def visit_explicitshapespec(self, node,lowerBound,  upperBound, comments,location):
        if lowerBound:
            low = self.visit(lowerBound)
            upp =  self.visit(upperBound)
            return {"low":low, "upp":upp}     
        else:
            res = self.visit(upperBound)
            return res
    

    def visit_componentdecl(self, node, componentName, componentArraySpec, charLength,expression,comments, location) :
        if charLength and componentArraySpec :
            if expression:
                print("houm1")
            else:
                print("houm2")
        elif charLength:
            if expression:
                print("houm3")
            else:
                print("houm4")
        elif componentArraySpec:
            if expression:
                print("houm5")
            else:
                spec = self.visit(componentArraySpec)
                z = {"name":str(componentName), "dim": len(spec), "elts":spec}
                return z
        elif expression:
            return {"name":str(componentName), "value":self.visit(expression)}
        else:
            return {"name":str(componentName)}
    
    
    def visit_level5expr(self,node,equivOperand,NEQV, EQV,comments, location):
        if len(node.children)==1:   
            return self.visit(equivOperand)
        args = map(lambda n:self.visit(n), node.children)  
        op = "!=" if  NEQV else "=="
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_equivoperand(self,node,orOperand,LOR,comments,location):
        op = "or"
        if len(node.children)==1:    
            return self.visit(orOperand)
        args = map(lambda n:self.visit(n) if (n!=".OR." and n!='.or.') else "or", node.children)  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_oroperand(self,node,andOperand,LAND,comments,location):
        op = "and"
        if len(node.children)==1:     
            return self.visit(andOperand)
        args = map(lambda n:self.visit(n) if (n!=".AND." and n!='.and.') else "and", node.children)  
        return reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))


    def visit_andoperand(self,node,level4Expr,LNOT,comments,location):
        r = self.visit(level4Expr)
        if not LNOT: return r
        return {"type":"unary_op", "op":"not", "value":r, "pseudo_type":"bool"}

    def visit_level4expr(self,node,level3Expr,relOp,comments,location):
        if len(node.children)==1:     
            return self.visit(level3Expr)
        args = map(lambda n:self.visit(n), node.children)  
        op = relOp
        res = reduceT(lambda x,y, op: {"type":"comparison", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))
        if isinstance(res["left"]["pseudo_type"], list): res["pseudo_type"]=["list", "bool"]
        return res 

    def visit_relop(self, node,  LT,LE ,EQ , NE , GT , GE, OP,comments, location):
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


    def visit_level3expr(self,node,level2Expr,DIV, SPOFF, SPON,comments,location):
        if len(node.children)==1:     
            return self.visit(level2Expr)
        args = map(lambda n:self.visit(n), node.children)  
        op = "//"
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":"bool"}, list(args))

    def visit_level2expr(self,node,addOperand,PLUS, MINUS,sign,comments,location):
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
    
    def visit_sign(self, node, PLUS , MINUS,comments, location):
        return "+" if PLUS else "-"


    def visit_addoperand(self,node,multOperand,STAR , DIV,comments,location):   
        op = "*" if STAR else "/"
        if len(node.children)==1:     
            return self.visit(multOperand)
        args = map(lambda n:self.visit(n), node.children)
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, list(args))

    def visit_multoperand(self,node,level1Expr,POWER,comments,location):
        op = "**"
        if len(node.children)==1:     
            return self.visit(level1Expr)
        args = map(lambda n:self.visit(n), node.children)   
        return reduceT(lambda x,y, op: {"type":"binary_op", "op":op, "left":x if not isinstance(x, list) else x[0], "right":y if not isinstance(y, list) else y[0], "pseudo_type":TYPED_API['operators'][str(op)](
            x['pseudo_type'] if not isinstance(x, list) else x[0]['pseudo_type'], y['pseudo_type'] if not isinstance(y, list) else y[0]['pseudo_type'])[-1]}, list(args))
  
    def visit_level1expr(self,node,primary,definedUnaryOp,comments,location):
        if definedUnaryOp:  
            res = self.visit(primary)   
            return  {"type":"unary_op", "operator":self.visit(definedUnaryOp), "value": res, "pseudo_type":res["pseudo_type"]}
        res = self.visit(primary)
        return res
    
    def visit_primary(self, node, unsignedArithmeticConstant, \
                        nameDataRef,functionReference,expression, \
                        SCON,logicalConstant,arrayConstructor,LPAREN, RPAREN, comments,location\
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
            else: val = val.encode('utf-8')
            return {'type':'str', 'value': val, "pseudo_type":"str"}
        if logicalConstant : return {"type":"bool", "value": self.visit(logicalConstant), "pseudo_type":"bool"}
        if arrayConstructor : 
            return self.visit(arrayConstructor)
        else:
            print(f"visit_primary not implemented at {location}")

    def visit_unsignedarithmeticconstant(self, node,  ICON, RDCON, complexConst, UNDERSCORE, kindParam,comments, location):
        if ICON: return self.visit(ICON)
        elif RDCON: return self.visit(RDCON)
        else:
            print(location, "unsign")

        return 
    
    def visit_caseconstruct(self, node, NAME, expression, selectCaseRange,comments, location):
        self._if = 0
        selector = self.visit(expression)
        self.sel.append(selector)
        ##TODO check the type of selector 
        body = self.visit(selectCaseRange)
        """
        for b in body:
            if "case" in b:
                test
        R = {
            'type': 'if_statement',
            'test': test,
            'block': block,
            'pseudo_type': 'Void',
            'otherwise': otherwise,
            "comments":comments
        }"""
        return body

    def visit_selectcaserange(self, node, selectCaseBody, endSelectStmt, comments, location):
        if selectCaseBody:
            body = self.visit(selectCaseBody)
            self.sel.pop()
            self._if = 1
            return body
        elif endSelectStmt: 
            self.sel.pop()
            self._if = 1

    
    def visit_selectcasebody(self, node, caseStmt, selectCaseBody, caseBodyConstruct, comments, location):
        if caseStmt:
            r = self.visit(caseStmt)
            return r
        else:
            body = self.visit(selectCaseBody)
            casebody = self.visit(caseBodyConstruct)
            if self._if==1:
                body["block"].append(casebody)
            else:
                if not self.case:
                    body["otherwise"][-1]["block"].append(casebody)  
                else: body["otherwise"].append(casebody)
            self.case = False
            return body
    
    def visit_casebodyconstruct(self, node, caseStmt, executionPartConstruct, comments, location):
        self.case = False
        if caseStmt:
            self.case = True
            res = self.visit(caseStmt)
        else:
            res = self.visit(executionPartConstruct)
        return res
    
    def visit_casestmt(self, node, caseSelector,comments, location):
        res = self.visit(caseSelector)
        return res
    
    def visit_caseselector(self, node, caseValueRangeList, comments, location):
        if caseValueRangeList:
            res = self.visit(caseValueRangeList)
            if len(res)==1: 
                res = res[0]
                if "beforecolon" in dir(self) and self.beforecolon: test={"type":"comparison", "op": "<=", "left":self.sel[-1], "right":res}
                elif "aftercolon" in dir(self) and self.aftercolon: test={"type":"comparison", "op": ">=", "left":self.sel[-1], "right":res}
                elif "middlecolon" in dir(self) and self.middlecolon: test={"type":"comparison", "op": ">=", "left":self.sel[-1], "right":res}
                else: test={"type":"comparison", "op": "==", "left":self.sel[-1], "right":res}
                self.beforecolon, self.aftercolon = False, False
            else: 
                test = {'type': 'binary_op','op': 'and', 
                                            'left': {'type': 'comparison','op': '<=', 'left': res[0],'right': self.sel[-1],'pseudo_type': 'bool'},
                                            'right': {'type': 'comparison','op': '<=', 'left': self.sel[-1], 'right': res[1],'pseudo_type': 'bool'},
                                            'pseudo_type': 'bool'}
                self.middlecolon = False
            if self._if ==0:
                r = {"type":"if_statement", "test":test, "block":[],"otherwise":[]}
            else:
                r = {"type":"elseif_statement", "test":test, "block":[]}
        else: 
            r = {"type":"else_statement", "block":[]}
        self._if = self._if + 1
        return r
       
    def visit_casevaluerangelist(self, node, caseValueRange, comments, location):
        res = self.translate_list(caseValueRange)
        return res
    
    def visit_casevaluerange(self, node, expression, COLON, comments, location):
        expr =  self.visit(expression)
        return expr

    def visit_beforecolonexpression(self, node, expression, COLON, comments, location):
        expr =  self.visit(expression)
        self.beforecolon=True
        return expr

    def visit_aftercolonexpression(self, node, expression, COLON, comments, location):
        expr =  self.visit(expression)
        self.aftercolon=True
        return expr

    def visit_midllecolonexpression(self, node, expression, COLON, comments, location):
        expr =  self.visit(expression)
        self.middlecolon=True
        return expr

    def visit_ifconstruct(self, node,ifThenStmt, conditionalBody, elseIfConstruct, elseConstruct, comments,location):
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
            'otherwise': otherwise,
            "comments":comments
        }
        return R

    def visit_elseifconstruct(self, node, elseIfStmt,conditionalBody,comments, location):
        test = self.visit(elseIfStmt)
        body = self.visit(conditionalBody)
        return {'type': 'elseif_statement',
           'test': test,
           'block': body,
           'pseudo_type': 'Void',
            "comments":comments}
    
    def visit_elseifstmt(self, node, expression, comments,location):
        return self.visit(expression)
        

    def visit_elseconstruct(self, node, conditionalBody,comments,location):
        res = self.visit(conditionalBody)
        return {'type': 'else_statement',
            'block': res,
            'pseudo_type': 'Void',
            "comments":comments}
    
    def visit_ifstmt(self, node, IF ,LPAREN ,expression, RPAREN, actionStmt,comments, location):
        R = {
            'type': 'if_statement',
            'test': self.visit(expression),
            'block': self.visit(actionStmt),
            'pseudo_type': 'Void',
            'otherwise': [],
            "comments":comments
        }
        return R
    
    def visit_conditionalbody(self, node,  executionPartConstruct,comments, location):
        return self.translate_list(executionPartConstruct)
    
    def visit_printstmt(self, node, PRINT, formatIdentifier, outputItemList, comments,location):
        if outputItemList : 
            r = self.visit(outputItemList)
            return {"type":"standard_call", "namespace":"io", "function":"print", "args": r if isinstance(r, list) else [r]}
        else: 
            print("todo print")
            return {"type":"standard_call", "namespace":"io", "function":"print", "args": self.visit(formatIdentifier)}
    
    def visit_exitstmt(self, node, EXIT, endName, eos,comments, location):
        print("todo exitstmt")
        return
    
    def visit_functionreference(self, node,NAME,functionArgList,comments, location):
        args =self.visit(functionArgList)
        name = str(NAME).lower()
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
            
            #TODO
            if message =="NULL": return {"type":"custom_call", "function":"NULL", "args":[], "pseudo_type":"Void"}
            
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
    def visit_namedataref(self, node, NAME, SIZE, REAL, complexDataRefTail,comments, location):  
            

        if not complexDataRefTail:
            id = str(NAME)
            id_type = self.type_env.top[id]
            if id not in self.type_env.top.values:
                self.notdeclared.add(str(NAME))

            return {"type":"local", "name": id, "pseudo_type":id_type}
        
        else :
            if NAME :  func = str(NAME)
            if SIZE : func = str(SIZE)
            if REAL : func = str(REAL)
            args = self.translate_list(complexDataRefTail)
            if "attr" not in args[0]:
                res = self.translate_func(func, args, location)
                return res
            else:
                return   {'type': 'attr',
                    'object': {'type': 'local',
                    'name': func,
                    'pseudo_type': self.type_env[func]},
                    'name': args[0]["attr"],
                    'pseudo_type': self.type_env[args[0]["attr"]]}
        
        return
    
    def visit_complexdatareftail(self, node, sectionSubscriptRef, NAME, comments,location):
        if sectionSubscriptRef :
            return self.visit(sectionSubscriptRef)
        return {'attr':str(NAME)}

    def visit_sectionsubscriptref(self, node, sectionSubscriptList, comments,location):
        return self.visit(sectionSubscriptList)
    
    def visit_sectionsubscriptlist(self, node,sectionSubscript, comments,location ):
        return self.translate_list(sectionSubscript)
    
    def visit_sectionsubscript(self, node, expression,subscriptTripletTail,comments,location):
        if expression:
            res = self.visit(expression)
            #print("uuuuuuuuu", res)
            if subscriptTripletTail:
                r = self.visit(subscriptTripletTail)
                #print("uuuuuuuuu2", r)
                if "args" in r and r["colon"]==1:
                    res2 = {"sliceindex":[res, r["args"][0]]}
                    return res2
                else:
                    print(f" visit_sectionsubscript not implemented at {location}")
            else:
                return res
        else:
            return self.visit(subscriptTripletTail)

    def visit_subscripttriplettail(self, node, expression, COLON, DOUBLECOLON, comments, location):
        if expression:
            res = self.visit(expression)
            if COLON:
                if len(res)==1:
                    return {"args":res, "colon":1}
                else:
                    return {"args":res, "colon":2}
            elif DOUBLECOLON:
                return {"args":res, "colon":3}
        else:
            return {"colon":3}

        
    
    def visit_functionarglist(self, node, functionArg, functionArgList,sectionSubscriptList,comments, location):
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
    
    def visit_functionarg(self, node,NAME, expression,comments, location):

        return {"type":"assignment", "op":"=", "target":{"type":"local", "name":str(NAME), "pseudo_type":self.type_env[str(NAME)]},
                                            "value":self.visit(expression),
                                            "pseudo_type":"VOID" ,
                                             "comments":comments}
 
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
        id_type = self.type_env[name]
        if id_type and isinstance(id_type, list):
            args = args[0][0]
            if "sliceindex" in args:
                res = {'type': 'sliceindex',
                        'receiver': {'type': 'local',
                                    'name': name,
                                    'pseudo_type': id_type},
                        'message': 'sliceindex',
                        'args': [args["sliceindex"][0],args["sliceindex"][1]],
                        'pseudo_type': id_type}
                return res
            return {'type': 'index',
                    'sequence': {'type': 'local',
                    'name': name,
                    'pseudo_type': id_type},
                    'index': args,
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


        
        
    def visit_doconstruct(self, node, labelDoStmt, blockDoConstruct,comments, location):
        if labelDoStmt:
            print(f"visit_doconstruct not yet implemented at {location}")
        else:
            res = self.visit(blockDoConstruct)
            res["comments"] = comments
            return res
    
    def visit_blockdoconstruct(self, node,commaLoopControl,executionPartConstruct,nameColon,comments, location):
        if nameColon:
            print(f"visit_blockdoconstruct not yet implemented at {location}") 
        lpc = self.visit(commaLoopControl)
        block = {"block":self.visit(executionPartConstruct)}
        lpc.update(block)
        return lpc      

    def visit_executionpartconstruct(self, node,executableConstruct,formatStmt, dataStmt,entryStmt,doubleDoStmt , comments,location):
        if executableConstruct: res = self.visit(executableConstruct)
        if formatStmt: res = self.visit(formatStmt)
        if dataStmt: res = self.visit(dataStmt)
        if entryStmt: res = self.visit(entryStmt)
        if doubleDoStmt: res = self.visit(doubleDoStmt)
        if isinstance(res, dict): res["comments"] = comments
        if isinstance(res, list): res.append({"type":"comments", "comments":comments})
        return res
    
    def visit_executableConstruct(self, node,actionStmt, doConstruct, ifConstruct, caseConstruct, whereConstruct, comments,location):
        if actionStmt : res = self.visit(actionStmt)
        if doConstruct : res = self.visit(doConstruct)
        if ifConstruct: res = self.visit(ifConstruct)
        if caseConstruct: res = self.visit(caseConstruct)
        if whereConstruct: res = self.visit(whereConstruct)
        if res: 
            res["comments"] = comments
            return res
    
    def visit_commaloopcontrol(self, node, loopControl,comments, location):
        return self.visit(loopControl)
    
    def visit_loopcontrol(self, node,variableName,expression,commaExpr,WHILE,comments, location):
        if not WHILE : 
            nm = self.visit(variableName)
            index = {'type': 'local', 'pseudo_type': self.type_env[nm], 'name': nm}
            if nm not in self.indexnames:
                self.index.append(index)
                self.indexnames.append(nm)
            start = self.visit(expression[0])
            end = self.visit(expression[1])
            if commaExpr:
                step = self.visit(commaExpr)
            else : step = {"type":"int", "value":"1", "pseudo_type":"int"}
            return {"type":"for_range_statement","index":index, "start":start, "end":end, "step": step, 'pseudo_type': 'Void', "comments":comments}
        else :
            return {
            'type': 'while_statement',
            'test': self.visit(expression),
            'pseudo_type': 'Void'
        }
    
    def visit_callstmt(self, node, subroutineNameUse, subroutineArgList, comments,location):
        
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
                    z["comments"] = comments
                    return z
            else:
                res = {"type": "call_stmt",
                "args": args,
                "name": name,
                "pseudo_type": "None", "comments":comments}  
                return res     
        else:
            args = None
        return args
    
    def visit_functionsubprogram(self, node, functionPrefix, functionName, functionRange,comments, location):
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
        implicit_return = {}
        if self.out:
            return_type = [m["pseudo_type"] for m in d if self.out==m["name"] ]
            implicit_return = {"type": "implicit_return", "pseudo_type":return_type[0] , "comments":comments}
        else: return_type = out_pseudo_t if len(out_pseudo_t)==1 else [["tuple"]+out_pseudo_t]
        body = []
        for n in z["_body"] :
            if isinstance(n, dict) and n["type"]=="declaration":
                z = {}
                z["type"] = "declaration"
                z["decl"] = []
                z["comments"]=comments
                for m in  n["decl"]:
                    if m not in arguments and  self.recursive==False : #(self.out and self.out!=m["name"]"
                        z["decl"].append(m)
                        body.append(z)
                    if m not in arguments and  self.out and self.out==m["name"] and self.recursive==False: #self.out and self.out!=m["name"]
                        res = dict(m)
                        res["type"] = "local"
                        implicit_return["value"] = res
            else: body.append(n)
        body.append(implicit_return)
        res = {"type":"function_definition", 
                "name": str(name), 
                "params":arguments, 
                "pseudo_type":['Function']+in_pseudo_t+return_type,
                "return_type": return_type[0],
                "block":body,
                "comments":comments}
        self.type_env.top["functions"][res["name"]] = [res["return_type"]]
        return res


    def visit_functionrange(self,node,functionParList, NAME, RESULT, eos, body,bodyPlusInternals, comments,location):
        if RESULT:
            self.out = self.visit(NAME)
        if body :
            bod = self.visit(body.bodyConstruct)
        else : bod = self.visit(bodyPlusInternals)
        params = self.visit(functionParList)
        return {"_params":params, "_body": bod}
    
    def visit_deallocatestmt(self,node, allocateObjectList, STAT, variable, eos, comments,location):
        pass
    
    def visit_functionparlist(self, node, functionPars, comments,location):
        if functionPars: return self.visit(functionPars)
        else: return []
    
    def visit_functionpars(self, node, functionPar,comments, location):
        res = self.translate_list(functionPar)
        return res

    def visit_functionprefixrec(self, node,recursive, typeSpec,comments, location):
        if recursive : self.recursive = True
        if typeSpec: self.out["type"] = self.visit(typeSpec)

    def visit_returnstmt(self, node, expression,comments, location):
        if expression: return {"type": "implicit_return", "value":self.visit(expression), "comments":comments}
        else: return {"type": "comments", "comments":comments}
    
    
    
    def visit_openstmt(self, node, connectSpecList,comments, location):
        return 

    def visit_writestmt(self, node,ioControlSpecList, outputItemList,comments, location):
        return 
    
    def visit_formatstmt(self, node, fmtSpec, comments,location):
        return
    
    def visit_closestmt(self, node,closeSpecList,comments, location):
        return

    def visit_actionstmt(self, node, comments, arithmeticIfStmt, assignmentStmt, assignStmt, backspaceStmt, callStmt, closeStmt
	, continueStmt
	, endfileStmt
	, gotoStmt
	, computedGotoStmt
	, assignedGotoStmt
	, ifStmt
    , inquireStmt
	, openStmt
	, pauseStmt
	, printStmt
	, readStmt
	, returnStmt
	, rewindStmt
	, stmtFunctionStmt
	, stopStmt
	, writeStmt
    , allocateStmt
    , cycleStmt
    , deallocateStmt
    , exitStmt
    , nullifyStmt 
    , pointerAssignmentStmt  
    , whereStmt, location):
        if arithmeticIfStmt : res = self.visit(arithmeticIfStmt)
        if assignmentStmt: res = self.visit(assignmentStmt)
        if assignStmt : res = self.visit(assignStmt)
        if backspaceStmt: res = self.visit(backspaceStmt)
        if callStmt: res = self.visit(callStmt)
        if closeStmt: res = self.visit(closeStmt)
        if continueStmt: res = self.visit(continueStmt)
        if endfileStmt: res = self.visit(endfileStmt)
        if gotoStmt: res = self.visit(gotoStmt)
        if computedGotoStmt: res = self.visit(computedGotoStmt)
        if assignedGotoStmt: res = self.visit(assignedGotoStmt)
        if ifStmt: res = self.visit(ifStmt)
        if inquireStmt: res = self.visit(inquireStmt)
        if openStmt: res = self.visit(openStmt)
        if pauseStmt: res = self.visit(pauseStmt)
        if printStmt: res = self.visit(printStmt)
        if readStmt: res = self.visit(readStmt)
        if returnStmt: res = self.visit(returnStmt)
        if rewindStmt: res = self.visit(rewindStmt)
        if stmtFunctionStmt: res = self.visit(stmtFunctionStmt)
        if stopStmt: res = self.visit(stopStmt)
        if writeStmt: res = self.visit(writeStmt)
        if allocateStmt: res = self.visit(allocateStmt)
        if cycleStmt: res = self.visit(cycleStmt)
        if deallocateStmt: res = self.visit(deallocateStmt)
        if exitStmt: res = self.visit(exitStmt)
        if nullifyStmt : res = self.visit(nullifyStmt)
        if pointerAssignmentStmt: 
            print(f"pointerAssignmentStmt not already done at {location}")
            return
        if whereStmt: res = self.visit(whereStmt)
        if res:
            res.update({"comments":comments}) if isinstance(res, dict) else res.append( {"type":"comments", "comments":comments})
            return res
        else: return {"type":"comments", "comments":comments}

    def visit_interfaceblock(self, node, interfaceStmt, interfaceBlockBody, comments, location):
        return 

    def visit_interfaceblockbody(self, node, interfaceBlockBody, interfaceBodyPartConstruct, comments, location):
        return

    def visit_interfacebodypartconstruct(self, node, interfaceBody, moduleProcedureStmt, comments, location):
        return

    def visit_interfacebody(self, node, functionPrefix, NAME, functionInterfaceRange, SUBROUTINE, subroutineInterfaceRange, comments, location):
        return

    def visit_functioninterfacerange(self, node, functionParList, subprogramInterfaceBody, comments, location):
        return
    
    def visit_subroutineinterfacerange(self, node, subroutineParList, subprogramInterfaceBody, comments, location):
        return

    def visit_subprograminterfacebody(self, node, specificationPartConstruct, subprogramInterfaceBody, comments, location ):
        print(f"visit_subprograminterfacebody not implemented yet at {location}")
        return       
        

    def visit_allocatestmt(self, node,allocationList, variable, comments, location):
        if variable:
            print(f"visit_allocatestmt not yet implemented {location}")
        else:
            self.res = []
            r = self.visit(allocationList)
            return r
    
    def visit_allocationlist(self, node, allocation,comments, location):
        
        return self.visit(allocation)
    
    def visit_allocation(self, node, allocateObject,  allocatedShape, comments, location):
        if not allocatedShape:
            return self.visit(allocateObject)
        else:
            r1 = self.visit(allocateObject)
            r2 = self.visit(allocatedShape) 
            res =     {'type': 'ExprStatNode',
                        'expr': {'type': 'standard_method_call',
                        'receiver': r1,
                        'message': 'allocate',
                        'args': r2,
                        'pseudo_type': 'int'}} 
        return res
    
    def visit_allocateobject(self, node, variableName, allocateObject, fieldSelector, comments, location):
        if variableName:
            r = self.visit(variableName)
            id_type = self.type_env[r]
            if id_type is None:
                self.notdeclared.add(r)
            return {"type":"local", "name":r, "pseudo_type":id_type}
        else:
            r1 = self.visit(allocateObject)
            r2 = self.visit(fieldSelector)
            self.res.append(r2)     
            return self.res
    
    def visit_allocatedshape(self, node, sectionSubscriptList, comments, location):
        return self.visit(sectionSubscriptList)
    
    def visit_fieldselector(self, node, sectionSubscriptList, PCT, NAME, comments, location):
        if sectionSubscriptList:
            return self.visit(sectionSubscriptList)
        else:
            print(f"visit_fieldselector not yet implemented {location}")
            return
    
    def visit_subroutinearglist(self, node, subroutineArg,comments, location):
        return self.visit(subroutineArg)
    
    def visit_accessstmt(self, node, ACCESSSPEC, accessIdList ,comments, location):
        return

    def visit_outputitemlist1(self, node, expression, outputImpliedDo ,outputItemList1, comments, location):
        res = []
        if expression:
            r = self.visit(expression)
            if isinstance(r, list):
                res.extend(r)
            else: res.append(r)
            if outputImpliedDo:
                r = self.visit(outputImpliedDo)
                res.append(r)
                return res
            elif outputItemList1:
                r1 = self.visit(outputItemList1)
                r1.extend(r) if isinstance(r, list) else r1.append(r)
                return r1
            else: return r
        else:
            r = self.visit(outputImpliedDo)
            if outputItemList1:
                res = self.visit(outputItemList1)
                return res.extend(r) if isinstance(r, list) else res.append(r)
            else:
                return r
    
    #def visit_pointerassignmentstmt(self, node, comments, location):

    def visit_whereconstruct(self, node, where, endWhereStmt, elseWhere, comments, location ):
        if where: return self.visit(where)
        elif elseWhere: return self.visit(elseWhere)
    
    def visit_where(self, node, whereConstructStmt, where, assignmentStmt, comments, location):
        if whereConstructStmt:
            return self.visit(whereConstructStmt)
        else:
            r1 = self.visit(where)
            body = self.visit(assignmentStmt)
            return {"type":"whereconstruct", "test": r1, "body":body}
    
    def visit_whereconstructstmt(self, node,WHERE, LPAREN, maskExpr, RPAREN, comments, location):
        return self.visit(maskExpr)

    def visit_arrayconstructor(self, node, OBRACKETSLASH, CBRACKETSLASH, acValueList, comments, location):
        res = {}
        r =  self.visit(acValueList)
        res["type"] = "array"
        res["elements"] = r
        res["pseudo_type"] = ["array", r[0]["pseudo_type"]]  
        return res
    
    def visit_acimplieddo(self, node, acImpliedDo,impliedDoVariable ,expression, comments, location):
        print("akklll", location)
        return 
    
    def visit_sfexprlist(self, node, expression, COLON, DOUBLECOLON, comments, location):
        res = self.visit(expression)
        if not COLON and not DOUBLECOLON:
            return res
        elif COLON and expression:
            print("uiiiiiiii", "TODO") #TODO


            
        
                
        

       


    