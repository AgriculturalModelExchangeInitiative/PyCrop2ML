/*	
 * Fortran 90 grammar for ANTLR 4.8
 * Adadpted from Fortran 90 PCCTS grammar by Olivier Dragon
 * Original PCCTS grammar by Terence Parr
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA
 *
 */

parser grammar  Fortran90Parser;
options
   { tokenVocab = Fortran90Lexer; }


eos : EOS;
commentOrNewLine : COMMENTORNEWLINE ;


program
   : executableProgram commentOrNewLine* 
   ;

executableProgram :  programUnit+  ;

programUnit
    :  eos* mainProgram            
	| eos* functionSubprogram      
	| eos* subroutineSubprogram    
	| eos* blockDataSubprogram  
    | eos* module 
    ;

mainProgram : programStmt? mainRange ;

programStmt : PROGRAM NAME eos ;

mainRange : (body? endProgramStmt) | (bodyPlusInternals endProgramStmt) ;

bodyPlusInternals 
    : body containsStmt internalSubprogram
	| containsStmt internalSubprogram
	| bodyPlusInternals internalSubprogram
    ;

internalSubprogram : specificationPartConstruct ;

specificationPartConstruct :
	implicitStmt                        #implicitStatement
	| parameterStmt                     #parameterStatement
	| formatStmt                        #formatStatement
	| entryStmt                         #entryStatment
	| declarationConstruct              #declarationConstruction
	| includeStmt                       #includeStatement
    | useStmt                           #useStatement
    ;

useStmt 
    : USE NAME eos                      
	| USE NAME COMMA ONLY COLON eos     
	| USE NAME COMMA renameList eos     
	| USE NAME COMMA ONLY COLON onlyList eos 
    ;

onlyList : onlyStmt (COMMA onlyStmt)* ;

onlyStmt
    : genericSpec
	| ident IMPLIEDT useName
	| useName
    ;

renameList : rename (COMMA rename)* ;

rename : ident IMPLIEDT useName ;

useName : ident;

parameterStmt : PARAMETER LPAREN namedConstantDefList RPAREN eos ;

namedConstantDefList : namedConstantDef+;

namedConstantDef: NAME ASSIGN expression ;

endProgramStmt 
    : END eos 
    | END PROGRAM NAME? eos
    ;
    

blockDataSubprogram 
    : blockDataStmt blockDataBody endBlockDataStmt
	| blockDataStmt endBlockDataStmt
    ;

blockDataStmt 
    : BLOCKDATA NAME? eos 
    | BLOCK DATA NAME? eos 
    ;

blockDataBody : blockDataBodyConstruct
	| blockDataBody blockDataBodyConstruct
    ;

blockDataBodyConstruct : specificationPartConstruct;

endBlockDataStmt : 
	ENDBLOCKDATA NAME? eos
	| END BLOCKDATA NAME? eos
	| ENDBLOCK DATA NAME? eos
	| END BLOCK DATA NAME? eos
    | END eos
    ;

formatStmt: FORMAT LPAREN fmtSpec? RPAREN eos ;

fmtSpec 
    : formatedit
	| FORMATSEP
	| FORMATSEP formatedit
	| fmtSpec FORMATSEP
	| fmtSpec FORMATSEP formatedit
	| fmtSpec COMMA formatedit
	| fmtSpec COMMA FORMATSEP
	| fmtSpec COMMA FORMATSEP formatedit
    ;

formatedit
    : editElement
	| ICON editElement
	| XCON
	| PCON
	| PCON editElement
	| PCON ICON editElement
    ;
   
editElement 
    : FCON
	| mislexedFcon
	| SCON
	| HOLLERITH
	| NAME
	| LPAREN fmtSpec RPAREN  
    ;

mislexedFcon 
    : RDCON SPOFF RDCON SPON
	| NAME SPOFF RDCON SPON
    ;


module 
    : moduleStmt moduleBody endModuleStmt 
    | moduleStmt endModuleStmt
    ;

endModuleStmt
    : END MODULE NAME? eos 
	| ENDMODULE NAME? eos
	| END eos
    ;

entryStmt 
    : ENTRY NAME subroutineParList RESULT LPAREN NAME RPAREN eos 
    ;

subroutineParList : (LPAREN subroutinePars?  RPAREN)? ;

subroutinePars : subroutinePar (COMMA  subroutinePar)* ;

subroutinePar : dummyArgName | STAR ;

declarationConstruct 
    : derivedTypeDef
	| interfaceBlock
    | typeDeclarationStmt
	| specificationStmt
    ;

specificationStmt 
    : commonStmt
	| dataStmt
	| dimensionStmt
	| equivalenceStmt
	| externalStmt
	| intrinsicStmt
	| saveStmt
    | accessStmt
	| allocatableStmt
	| intentStmt
	| namelistStmt
	| optionalStmt
	| pointerStmt
	| targetStmt
    ;

targetStmt : TARGET DOUBLECOLON? targetObjectList eos ;

targetObjectList : targetObject (COMMA targetObject)* ;

targetObject
    : objectName
	| objectName LPAREN arraySpec RPAREN
    ;

pointerStmt : POINTER DOUBLECOLON? pointerStmtObjectList eos ;

pointerStmtObjectList : pointerStmtObject (COMMA pointerStmtObject)* ;

pointerStmtObject 
    : objectName
	| objectName LPAREN deferredShapeSpecList RPAREN
    ;

optionalStmt : OPTIONAL DOUBLECOLON? optionalParList eos ;

optionalParList : optionalPar (COMMA optionalPar)* ;

optionalPar : dummyArgName ;

namelistStmt : NAMELIST namelistGroups eos ;

namelistGroups 
    : DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups COMMA DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups COMMA namelistGroupObject
    ;

namelistGroupName : NAME ;

namelistGroupObject : variableName ;

intentStmt : INTENT LPAREN intentSpec RPAREN DOUBLECOLON? intentParList eos ;

intentParList : intentPar (COMMA intentPar) ;

intentPar : dummyArgName ;

dummyArgName : NAME;

intentSpec : (IN | OUT | INOUT);

allocatableStmt : ALLOCATABLE DOUBLECOLON? arrayAllocationList eos ;

arrayAllocationList : arrayAllocation (COMMA arrayAllocation)* ;

arrayAllocation 
    : arrayName
    | arrayName LPAREN deferredShapeSpecList RPAREN
    ;

arrayName : ident ;

accessStmt 
    : ACCESSSPEC DOUBLECOLON? accessIdList eos
	| ACCESSSPEC eos 
    ;

accessIdList : accessId (COMMA accessId) ;

accessId : genericName | genericSpec ;

genericName : ident ;

saveStmt 
    : SAVE eos
	| SAVE savedEntityList eos
    | SAVE DOUBLECOLON savedEntityList eos
    ;

savedEntityList : savedEntity+ ;

savedEntity : variableName  | savedCommonBlock;

savedCommonBlock : DIV commonBlockName DIV ;

intrinsicStmt : INTRINSIC intrinsicList eos;

intrinsicList : intrinsicProcedureName+ ;

intrinsicProcedureName : NAME ;

externalStmt : EXTERNAL externalNameList eos ;

externalNameList : externalName+ ;

externalName : NAME;

equivalenceStmt : EQUIVALENCE equivalenceSetList eos ;

equivalenceSetList : equivalenceSet+ ; 

equivalenceSet : LPAREN equivalenceObject COMMA equivalenceObjectList RPAREN ;

equivalenceObject : variable;

equivalenceObjectList : equivalenceObject+ ;

dimensionStmt 
    : DIMENSION arrayDeclaratorList eos 
    | DIMENSION DOUBLECOLON arrayDeclaratorList eos
    ;

arrayDeclaratorList : arrayDeclarator+ ;

commonStmt : COMMON comlist eos; 

comlist 
    : comblock? commonBlockObject
	| comlist COMMA comblock? commonBlockObject
	| comlist comblock commonBlockObject
    ;

commonBlockObject : variableName | arrayDeclarator ;

arrayDeclarator : variableName LPAREN arraySpec RPAREN ;

comblock 
    : DIV SPOFF DIV SPON
	| DIV commonBlockName DIV
    ;

commonBlockName : NAME ;

typeDeclarationStmt
    : typeSpec entityDeclList eos                           
    | typeSpec attrSpecSeq? DOUBLECOLON entityDeclList eos  
    ;

attrSpecSeq 
    : COMMA attrSpec
	| attrSpecSeq COMMA attrSpec
    ;

attrSpec 
    : PARAMETER
	| ACCESSSPEC
	| ALLOCATABLE
	| DIMENSION LPAREN arraySpec RPAREN
	| EXTERNAL
	| INTENT LPAREN intentSpec RPAREN
	| INTRINSIC
	| OPTIONAL
	| POINTER
	| SAVE
	| TARGET
    ;

entityDeclList : entityDecl (COMMA entityDecl)*;

entityDecl  
    : objectName
	| objectName LPAREN arraySpec RPAREN
	| objectName STAR charLength
	| objectName LPAREN arraySpec RPAREN STAR charLength
    | objectName ASSIGN expression
	| objectName LPAREN arraySpec RPAREN ASSIGN expression
	| objectName STAR charLength ASSIGN expression
	| objectName STAR charLength LPAREN arraySpec RPAREN ASSIGN expression
    ;

objectName  : NAME ;

arraySpec 
    : explicitShapeSpecList | assumedSizeSpec 
    | assumedShapeSpecList
	| deferredShapeSpecList
    ;

assumedShapeSpecList 
    : lowerBound COLON
	| deferredShapeSpecList COMMA lowerBound COLON
	| assumedShapeSpecList COMMA assumedShapeSpec
    ;

assumedShapeSpec 
    : lowerBound COLON
	| COLON
    ;

assumedSizeSpec 
    : STAR
	| lowerBound COLON STAR
	| explicitShapeSpecList COMMA STAR
	| explicitShapeSpecList COMMA lowerBound COLON STAR
    ;

interfaceBlock : interfaceStmt interfaceBlockBody endInterfaceStmt ;

endInterfaceStmt 
    : ENDINTERFACE eos
	| END INTERFACE eos 
    ;

interfaceStmt
    : INTERFACE NAME eos
	| INTERFACE genericSpec eos
	| INTERFACE eos
    ;

genericSpec
    : OPERATOR LPAREN definedOperator RPAREN
	| ASSIGNMENT LPAREN ASSIGN RPAREN
    ;

definedOperator 
    : DOP
    | POWER
	| STAR
	| (PLUS | MINUS)
	| (LT | LE | EQ | NE | GT | GE) 
	| DIV SPOFF DIV SPON
	| LNOT
	| LAND
	| LOR
	| (NEQV | EQV)
    ;

interfaceBlockBody 
    : interfaceBodyPartConstruct
	| interfaceBlockBody interfaceBodyPartConstruct
    ;

interfaceBodyPartConstruct
    : interfaceBody
	| moduleProcedureStmt
    ;

moduleProcedureStmt
    : MODULE PROCEDURE procedureNameList eos
    ;

procedureNameList : procedureName (COMMA procedureName)* ;

procedureName : ident ;

interfaceBody 
    : functionPrefix NAME functionInterfaceRange
	| SUBROUTINE NAME subroutineInterfaceRange
    ;

subroutineInterfaceRange 
    : subroutineParList eos subprogramInterfaceBody? endSubroutineStmt
    ;

endSubroutineStmt
    : END eos 
	| END SUBROUTINE NAME? eos;


recursive : RECURSIVE ;
functionPrefix
    :  recursive? typeSpec? FUNCTION #functionPrefixRec
	| typeSpec RECURSIVE FUNCTION #functionPrefixTyp
    ;

functionInterfaceRange
    : functionParList eos subprogramInterfaceBody? endFunctionStmt
    ;

functionParList :LPAREN functionPars? RPAREN ;

functionPars : functionPar (COMMA functionPar)* ;

functionPar : dummyArgName;

subprogramInterfaceBody 
    : specificationPartConstruct
	| subprogramInterfaceBody specificationPartConstruct   
    ;

endFunctionStmt 
    : END eos
    | END FUNCTION NAME? eos
    ;

derivedTypeDef : derivedTypeStmt derivedTypeBody endTypeStmt ;

endTypeStmt 
    : ENDTYPE NAME eos
	| ENDTYPE eos
	| END TYPE NAME eos
	| END TYPE eos
    ;

derivedTypeStmt 
    : TYPE NAME eos
	| TYPE DOUBLECOLON NAME eos
	| TYPE COMMA ACCESSSPEC DOUBLECOLON NAME eos
    ;

derivedTypeBody
    : derivedTypeBodyConstruct
	| derivedTypeBody derivedTypeBodyConstruct
    ;

derivedTypeBodyConstruct
    : privateSequenceStmt
	| componentDefStmt
    ;

privateSequenceStmt
    : PRIVATE eos
	| SEQUENCE eos
    ;

componentDefStmt
    : typeSpec COMMA componentAttrSpecList DOUBLECOLON componentDeclList eos
	| typeSpec DOUBLECOLON componentDeclList eos
	| typeSpec componentDeclList eos
    ;

componentDeclList : componentDecl (COMMA componentDecl);

componentDecl 
    : componentName LPAREN componentArraySpec RPAREN STAR charLength
	| componentName LPAREN componentArraySpec RPAREN
	| componentName STAR charLength
	| componentName
    ;
componentName : NAME ;

componentAttrSpecList : componentAttrSpec ( COMMA componentAttrSpec)*;

componentAttrSpec 
    : POINTER
	| DIMENSION LPAREN componentArraySpec RPAREN
    ;

componentArraySpec : explicitShapeSpecList | deferredShapeSpecList ;
    
explicitShapeSpecList  : explicitShapeSpec (COMMA explicitShapeSpec)* ;

explicitShapeSpec : (lowerBound COLON upperBound) | upperBound;

lowerBound : expression ;

upperBound : expression ;

deferredShapeSpecList : deferredShapeSpec (COMMA deferredShapeSpec)* ;

deferredShapeSpec : COLON;

typeSpec
    : INTEGER
	| REAL
	| DOUBLEPRECISION
	| COMPLEX
	| LOGICAL
	| CHARACTER
	| CHARACTER lengthSelector
    | INTEGER kindSelector
	| REAL kindSelector
	| DOUBLE PRECISION
	| COMPLEX kindSelector
	| CHARACTER charSelector
	| LOGICAL kindSelector
	| TYPE LPAREN typeName RPAREN
    ;

kindSelector 
    : LPAREN KIND ASSIGN expression RPAREN
	| LPAREN expression RPAREN
    ;

typeName : ident ;

charSelector 
    : LPAREN LEN ASSIGN typeParamValue COMMA KIND ASSIGN expression RPAREN
	| LPAREN LEN ASSIGN typeParamValue COMMA expression RPAREN
	| LPAREN LEN ASSIGN typeParamValue RPAREN
	| LPAREN KIND ASSIGN expression RPAREN
	| LPAREN expression RPAREN
    ;

lengthSelector
    : STAR charLength
    | LPAREN typeParamValue RPAREN
    ;

charLength 
    : LPAREN typeParamValue RPAREN
	| constant
    ;

constant 
    : namedConstantUse
	| (PLUS | MINUS)? unsignedArithmeticConstant
	| SCON
	| HOLLERITH
	| logicalConstant
    | ICON UNDERSCORE SCON
	| namedConstantUse UNDERSCORE SCON
    | structureConstructor
	| bozLiteralConstant
    ;

bozLiteralConstant : BCON | OCON | ZCON ;

structureConstructor : typeName LPAREN exprList RPAREN;

exprList : expression (COMMA expression) ;

namedConstantUse : NAME ;

typeParamValue
    : expression
    | STAR
    ;


moduleStmt 
    : MODULE moduleName eos
    ;

moduleName
    : ident
    ;

ident 
    : NAME
    ;

moduleBody
    : specificationPartConstruct                    #specPartStmt
	| moduleSubprogramPartConstruct                 #submoduleStmt
	| moduleBody specificationPartConstruct         #complexSpecPart
	| moduleBody moduleSubprogramPartConstruct      #complexSubmodule
    ;

moduleSubprogramPartConstruct 
    : containsStmt
	| moduleSubprogram
    ;

containsStmt : CONTAINS eos ;

moduleSubprogram : functionSubprogram | subroutineSubprogram ;

functionSubprogram : functionPrefix functionName functionRange ;

functionName : NAME;

functionRange 
    : functionParList eos body? endFunctionStmt 
	| functionParList RESULT LPAREN NAME RPAREN eos body? endFunctionStmt
    | functionParList RESULT LPAREN NAME RPAREN eos bodyPlusInternals endFunctionStmt
	| functionParList eos bodyPlusInternals endFunctionStmt
    ;

body : bodyConstruct+ ;

bodyConstruct
    : specificationPartConstruct
	| executableConstruct
    ;

executableConstruct
    : actionStmt
	| doConstruct
	| ifConstruct
    | caseConstruct
    | whereConstruct
    ;

whereConstruct 
    : where endWhereStmt
	| elseWhere endWhereStmt
    ;

elseWhere 
    : where elsewhereStmt
	| elseWhere assignmentStmt
    ;

elsewhereStmt : ELSEWHERE eos ;

endWhereStmt 
    : ENDWHERE eos
	| END WHERE eos
    ;

where 
    : whereConstructStmt
	| where assignmentStmt 
    ;

whereConstructStmt : WHERE LPAREN maskExpr RPAREN eos ;

maskExpr : expression ;

caseConstruct
    : NAME COLON SELECTCASE LPAREN expression RPAREN eos selectCaseRange
	| SELECTCASE LPAREN expression RPAREN eos selectCaseRange
	| NAME COLON SELECT CASE LPAREN expression RPAREN eos selectCaseRange
	| SELECT CASE LPAREN expression RPAREN eos selectCaseRange
    ;

selectCaseRange 
    : selectCaseBody endSelectStmt
	| endSelectStmt
    ;

endSelectStmt : (ENDSELECT NAME? eos) | ( END SELECT NAME? eos);

selectCaseBody
    : caseStmt
	| selectCaseBody caseBodyConstruct
    ;

caseBodyConstruct : caseStmt | executionPartConstruct;

caseStmt
    : CASE caseSelector eos
	| CASE caseSelector NAME eos
    ;

caseSelector 
    : LPAREN caseValueRangeList RPAREN
	| DEFAULT
    ;

caseValueRangeList : caseValueRange+ ;

caseValueRange 
    : expression
	| expression COLON
	| COLON expression
    | expression COLON expression
    ;

ifConstruct : ifThenStmt conditionalBody elseIfConstruct* elseConstruct? endIfStmt ;

ifThenStmt : IF LPAREN expression RPAREN THEN eos;

conditionalBody : executionPartConstruct*;

elseIfConstruct :  elseIfStmt conditionalBody;

elseIfStmt 
    : ELSEIF LPAREN expression RPAREN THEN eos
    | ELSE IF LPAREN expression RPAREN THEN eos
    ;

elseConstruct : elseStmt conditionalBody ;

elseStmt : ELSE eos;

endIfStmt 
    : ENDIF eos
    | END IF eos
    ;

doConstruct 
    : labelDoStmt
    | blockDoConstruct 
    ;

blockDoConstruct : nameColon? DO commaLoopControl? eos executionPartConstruct* endDoStmt
    ;

endDoStmt 
    : ENDDO endName? eos
    | END DO endName? eos 
    ;

endName : ident;

nameColon : NAME COLON ;

labelDoStmt : DO doLblRef commaLoopControl eos executionPartConstruct* doLblDef doLabelStmt;

doLblRef : ICON ;

doLblDef : ICON ;

doLabelStmt : actionStmt ;

executionPartConstruct 
    : executableConstruct
	| formatStmt
	| dataStmt
	| entryStmt
    | doubleDoStmt   
    ;

doubleDoStmt : DO lblRef commaLoopControl eos ;

dataStmt : DATA dataStmtSet ((COMMA)? dataStmtSet)* eos;

dataStmtSet
   : dse1 dse2
   ;

dse1
   : dataStmtObjectList (COMMA dataStmtObjectList)* DIV
   ;

dse2
   : dataStmtValueList (COMMA dataStmtValueList)* DIV
   ;

dataStmtValueList : dataStmtValue+;

dataStmtValue 
    : constant
	| constant STAR constant
	| namedConstantUse STAR constant
    ;

dataStmtObjectList : dataStmtObject+ ;

dataStmtObject : variable | dataImpliedDo ;

variable :  variableName subscriptListRef? substringRange? ;

subscriptListRef : LPAREN subscriptList RPAREN ;

subscriptList : subscript+ ;

subscript : expression ;

substringRange : LPAREN expression? subscriptTripletTail RPAREN ;

dataImpliedDo 
    : LPAREN dataIDoObjectList COMMA impliedDoVariable ASSIGN expression COMMA expression RPAREN
	| LPAREN dataIDoObjectList COMMA impliedDoVariable ASSIGN expression COMMA expression COMMA expression RPAREN
    ;
dataIDoObjectList : dataIDoObject+ ;

dataIDoObject 
    : arrayElement | dataImpliedDo
    | structureComponent 
    ;

structureComponent 
    : variableName fieldSelector
	| structureComponent fieldSelector
    ;

fieldSelector 
    : LPAREN sectionSubscriptList RPAREN PCT NAME
	| PCT NAME
    ;

arrayElement 
    : variableName LPAREN sectionSubscriptList RPAREN 
    | structureComponent LPAREN sectionSubscriptList RPAREN
    ;

impliedDoVariable : NAME;

commaLoopControl : COMMA? loopControl ;

loopControl 
    : variableName ASSIGN expression COMMA expression commaExpr?
    | WHILE LPAREN expression RPAREN
    ;

variableName : NAME;

commaExpr: COMMA expression;

actionStmt :
	arithmeticIfStmt
	| assignmentStmt
	| assignStmt
	| backspaceStmt
	| callStmt
	| closeStmt
	| continueStmt
	| endfileStmt
	| gotoStmt
	| computedGotoStmt
	| assignedGotoStmt
	| ifStmt
    | inquireStmt
	| openStmt
	| pauseStmt
	| printStmt
	| readStmt
	| returnStmt
	| rewindStmt
	| stmtFunctionStmt
	| stopStmt
	| writeStmt
    | allocateStmt
    | cycleStmt
    | deallocateStmt
    | exitStmt
    | nullifyStmt 
    | pointerAssignmentStmt  
    | whereStmt
    ;

whereStmt : WHERE LPAREN maskExpr RPAREN assignmentStmt;

pointerAssignmentStmt 
    : NAME IMPLIEDT target eos
	| NAME sFExprListRef? PCT nameDataRef IMPLIEDT target eos
    ;

target : expression;

nullifyStmt : NULLIFY LPAREN pointerObjectList RPAREN eos ;

pointerObjectList : pointerObject (COMMA pointerObject)* ;

pointerObject : NAME | pointerField ;

pointerField 
    : NAME sFExprListRef? PCT NAME 
    | pointerField fieldSelector
    ;

exitStmt : EXIT endName? eos ;

deallocateStmt 
    : DEALLOCATE LPAREN allocateObjectList COMMA STAT ASSIGN variable RPAREN eos
	| DEALLOCATE LPAREN allocateObjectList RPAREN eos
    ;

allocateObjectList : allocateObject (COMMA allocateObject)*;


cycleStmt : CYCLE endName? eos
    ;

allocateStmt 
    : ALLOCATE LPAREN allocationList COMMA STAT ASSIGN variable RPAREN eos
	| ALLOCATE LPAREN allocationList RPAREN eos
    ;

allocationList : allocation (COMMA allocation)* ;

allocation 
    : allocateObject
    | allocateObject allocatedShape
    ;

allocateObject 
    : variableName
    | allocateObject fieldSelector
    ;

allocatedShape 
    : LPAREN sectionSubscriptList RPAREN
    ;


stopStmt : STOP (ICON | SCON)? eos ;

writeStmt : WRITE LPAREN ioControlSpecList RPAREN outputItemList? eos;

ioControlSpecList 
    : unitIdentifier DOLLAR COMMA
	| unitIdentifier COMMA formatIdentifier
	| unitIdentifier COMMA ioControlSpec
	| ioControlSpec
	| ioControlSpecList COMMA ioControlSpec
    ;

stmtFunctionStmt : NAME stmtFunctionRange ;

stmtFunctionRange : LPAREN sFDummyArgNameList? RPAREN ASSIGN expression eos;

sFDummyArgNameList : sFDummyArgName (COMMA sFDummyArgName)*;

sFDummyArgName : NAME ;

returnStmt : RETURN expression? eos ;

rewindStmt : (REWIND unitIdentifier eos) | (REWIND LPAREN positionSpecList RPAREN eos) ;

readStmt 
    : READ rdCtlSpec inputItemList? eos
	| READ rdFmtId commaInputItemList? eos
    ;

commaInputItemList : COMMA inputItemList ;

rdFmtId 
    : lblRef
	| STAR
	| cOperand
	| cOperand DIV SPOFF DIV SPON cPrimary
	| rdFmtIdExpr DIV SPOFF DIV SPON cPrimary
    ;

rdFmtIdExpr : LPAREN uFExpr RPAREN ;

inputItemList : inputItem (COMMA inputItem)* ;

inputItem : nameDataRef | inputImpliedDo ;

inputImpliedDo : LPAREN inputItemList COMMA impliedDoVariable ASSIGN expression COMMA expression commaExpr? RPAREN;

rdCtlSpec : rdUnitId | (LPAREN rdIoCtlSpecList RPAREN) ;

rdUnitId : (LPAREN uFExpr RPAREN) | (LPAREN STAR RPAREN) ;

rdIoCtlSpecList 
    : unitIdentifier COMMA ioControlSpec
    | unitIdentifier COMMA formatIdentifier
    | ioControlSpec
    | rdIoCtlSpecList COMMA ioControlSpec
    ;

ioControlSpec 
    : FMT ASSIGN formatIdentifier
	| UNIT ASSIGN unitIdentifier
	| REC ASSIGN expression
	| END ASSIGN lblRef
	| ERR ASSIGN lblRef
	| IOSTAT ASSIGN scalarVariable
    | NML ASSIGN namelistGroupName
	| ADVANCE ASSIGN cExpression
	| SIZE ASSIGN variable
	| EOR ASSIGN lblRef
    ; 

printStmt 
    : PRINT formatIdentifier COMMA outputItemList eos
	| PRINT formatIdentifier eos
    ;

outputItemList : expression | outputItemList1 ;

outputItemList1 
    : expression COMMA expression 
	| expression COMMA outputImpliedDo
	| outputImpliedDo
	| outputItemList1 COMMA expression
	| outputItemList1 COMMA outputImpliedDo
    ;


outputImpliedDo 
    : LPAREN expression COMMA impliedDoVariable ASSIGN expression COMMA expression commaExpr? RPAREN
	| LPAREN outputItemList1 COMMA impliedDoVariable ASSIGN expression COMMA expression commaExpr? RPAREN
    ;

formatIdentifier : lblRef | cExpression | STAR ;

pauseStmt : PAUSE (ICON | SCON)? eos ;

openStmt : OPEN LPAREN connectSpecList RPAREN eos ;

connectSpecList : unitIdentifierComma? connectSpec? (COMMA connectSpec )*;

connectSpec 
    : UNIT ASSIGN unitIdentifier
	| ERR ASSIGN lblRef
	| FILE ASSIGN cExpression
	| STATUS ASSIGN cExpression
	| ACCESS ASSIGN cExpression
	| FORM ASSIGN cExpression
	| RECL ASSIGN expression
	| BLANK ASSIGN cExpression
	| IOSTAT ASSIGN scalarVariable
    | POSITION ASSIGN cExpression
	| ACTION ASSIGN cExpression
	| DELIM ASSIGN cExpression
	| PAD ASSIGN cExpression
    ;


inquireStmt 
    : INQUIRE LPAREN inquireSpecList RPAREN eos 
    | INQUIRE LPAREN IOLENGTH ASSIGN scalarVariable RPAREN outputItemList eos
    ;

inquireSpecList : unitIdentifier? inquireSpec? (COMMA inquireSpec)*;

inquireSpec 
    : UNIT ASSIGN unitIdentifier
	| FILE ASSIGN cExpression
	| ERR ASSIGN lblRef
	| IOSTAT ASSIGN scalarVariable
	| EXIST ASSIGN scalarVariable
	| OPENED ASSIGN scalarVariable
	| NUMBER ASSIGN scalarVariable
	| NAMED ASSIGN scalarVariable
	| NAME ASSIGN scalarVariable
	| ACCESS ASSIGN scalarVariable
	| SEQUENTIAL ASSIGN scalarVariable
	| DIRECT ASSIGN scalarVariable
	| FORM ASSIGN scalarVariable
	| FORMATTED ASSIGN scalarVariable
	| UNFORMATTED ASSIGN scalarVariable
	| RECL ASSIGN expression
	| NEXTREC ASSIGN scalarVariable
	| BLANK ASSIGN scalarVariable
    | POSITION ASSIGN scalarVariable
	| ACTION ASSIGN scalarVariable
	| READ ASSIGN scalarVariable
	| WRITE ASSIGN scalarVariable
	| READWRITE ASSIGN scalarVariable
	| DELIM ASSIGN scalarVariable
	| PAD ASSIGN scalarVariable
    ;

assignedGotoStmt 
    : (GOTO | GO TO) variableName eos
	| (GOTO | GO TO) variableName LPAREN lblRefList RPAREN eos
	| (GOTO | GO TO) variableComma LPAREN lblRefList RPAREN eos
    ;

variableComma : variableName COMMA ;

gotoStmt : (GOTO | GO TO) lblRef eos ;

computedGotoStmt : GOTO LPAREN lblRefList RPAREN COMMA? expression eos ;

lblRefList : lblRef (COMMA lblRef)* ;

endfileStmt : ((ENDFILE| END FILE) unitIdentifier eos) | ((ENDFILE| END FILE) LPAREN positionSpecList RPAREN eos);

continueStmt : CONTINUE eos ;

closeStmt : CLOSE LPAREN closeSpecList RPAREN eos ;

closeSpecList : unitIdentifierComma? closeSpec? (COMMA closeSpec)* ;

closeSpec 
    : UNIT ASSIGN unitIdentifier
	| ERR ASSIGN lblRef
	| STATUS ASSIGN cExpression
	| IOSTAT scalarVariable
    ;

cExpression : cPrimary cPrimaryConcatOp* ; 

cPrimary : cOperand | (LPAREN cExpression RPAREN);

cOperand 
    : SCON
    | nameDataRef
	| functionReference 
    ;

cPrimaryConcatOp : cPrimary DIV SPOFF DIV SPON ;

callStmt 
    : CALL subroutineNameUse eos
	| CALL subroutineNameUse LPAREN subroutineArgList RPAREN eos
    ;
subroutineNameUse : NAME;

subroutineArgList : subroutineArg? (COMMA subroutineArg )*;

subroutineArg 
    : expression
	| HOLLERITH
	| STAR lblRef
    | NAME ASSIGN expression
	| NAME ASSIGN HOLLERITH
	| NAME ASSIGN STAR lblRef
    ;

arithmeticIfStmt : IF LPAREN expression RPAREN lblRef COMMA lblRef COMMA lblRef eos;

lblRef : label;

label : ICON;

assignmentStmt 
    : label? NAME sFExprListRef? substringRange? ASSIGN expression eos
    | NAME sFExprListRef? PCT nameDataRef ASSIGN expression eos
	| NAME LPAREN sFDummyArgNameList RPAREN PCT nameDataRef ASSIGN expression eos
    ;

sFExprListRef : LPAREN sFExprList commaSectionSubscript* RPAREN ;

sFExprList 
    : expression COLON? expression?
	| COLON expression?
    | expression? COLON expression COLON expression
	| expression? DOUBLECOLON expression
    ;

commaSectionSubscript : COMMA sectionSubscript;

assignStmt : ASSIGNSTMT lblRef TO variableName eos;

backspaceStmt 
    : BACKSPACE unitIdentifier eos
	| BACKSPACE LPAREN positionSpecList RPAREN eos
    ;
unitIdentifier : uFExpr | STAR;

positionSpecList : unitIdentifierComma? positionSpec+ ;

unitIdentifierComma : unitIdentifier COMMA ;

positionSpec 
    : UNIT ASSIGN unitIdentifier
	| ERR ASSIGN lblRef
	| IOSTAT ASSIGN scalarVariable
    ;

scalarVariable : variableName | arrayElement ;

uFExpr 
    : uFTerm
	| (PLUS | MINUS) uFTerm
	| uFExpr (PLUS | MINUS) uFTerm
    ;

uFTerm 
    : uFFactor
	| uFTerm (STAR | DIV) uFFactor
	| uFTerm (DIV DIV) uFPrimary
    ;

uFFactor 
    : uFPrimary
	| uFPrimary POWER uFFactor
    ;

uFPrimary 
    : ICON
	| SCON
	| nameDataRef
	| functionReference
	| LPAREN uFExpr RPAREN
    ;

subroutineSubprogram 
    : SUBROUTINE subroutineName subroutineRange       
    | RECURSIVE SUBROUTINE subroutineName subroutineRange;

subroutineName : NAME ;

subroutineRange 
    : subroutineParList eos body? endSubroutineStmt 
    | subroutineParList eos bodyPlusInternals endSubroutineStmt
    ;

includeStmt 
    : INCLUDE SCON eos
    ;

implicitStmt 
    : IMPLICIT  implicitSpecList eos
    | IMPLICIT NONE eos ;

implicitSpecList : implicitSpec (COMMA implicitSpec)* ;

implicitSpec
   : typeSpec implicitRanges 
   | typeSpec LPAREN implicitRanges RPAREN
   ;

implicitRanges : implicitRange? (COMMA implicitRange)* ;

implicitRange : NAME MINUS NAME ;

expression 
    : level5Expr 
    | expression definedBinaryOp level5Expr
    ;

definedBinaryOp : DOP;

level5Expr : equivOperand ((NEQV | EQV) equivOperand)* ;

equivOperand
   : orOperand (LOR orOperand)*
   ;

orOperand
   : andOperand  (LAND andOperand )*
   ;

andOperand
   : level4Expr (LNOT level4Expr)*
   ;


relOp: LT | LE | EQ | NE | GT | GE| OP ;


level4Expr
   : level3Expr  (relOp level3Expr)*
   ;

level3Expr
   : level2Expr (DIV SPOFF DIV SPON level2Expr)*
   ;

level2Expr
   : sign? addOperand ((PLUS | MINUS) addOperand)*
   ;

sign : PLUS | MINUS ;

addOperand
   : multOperand ((STAR | DIV) multOperand)*
   ;

multOperand
   : level1Expr (POWER level1Expr)*
   ;

level1Expr 
    : primary 
    | definedUnaryOp primary
    ;

definedUnaryOp : DOP ;

primary
   : unsignedArithmeticConstant
   | nameDataRef
   | functionReference
   | LPAREN expression RPAREN
   | SCON
   | logicalConstant  
   | arrayConstructor
   ;

arrayConstructor : OBRACKETSLASH acValueList CBRACKETSLASH ;

acValueList : expression |acValueList1 ;

acValueList1 
    : expression COMMA expression
	| expression COMMA acImpliedDo
	| acImpliedDo
	| acValueList1 COMMA expression
	| acValueList1 COMMA acImpliedDo
    ;

acImpliedDo 
    : LPAREN expression COMMA impliedDoVariable ASSIGN expression COMMA expression RPAREN
	| LPAREN expression COMMA impliedDoVariable ASSIGN expression COMMA expression COMMA expression RPAREN
	| LPAREN acImpliedDo COMMA impliedDoVariable ASSIGN expression COMMA expression RPAREN
	| LPAREN acImpliedDo COMMA impliedDoVariable ASSIGN expression COMMA expression COMMA expression RPAREN 	
     ;


functionReference 
    : NAME LPAREN RPAREN
    | NAME LPAREN functionArgList RPAREN
    ;

functionArgList 
    : functionArg
	| functionArgList COMMA functionArg
	| sectionSubscriptList COMMA functionArg
    ;

functionArg 
    : NAME ASSIGN expression 
    ;
    
nameDataRef
    : (NAME|REAL|SIZE) complexDataRefTail*
    ;

complexDataRefTail 
    : sectionSubscriptRef 
    | PCT NAME;


sectionSubscriptRef : LPAREN sectionSubscriptList RPAREN ;

sectionSubscriptList : sectionSubscript (COMMA sectionSubscript)* ;

sectionSubscript 
    : expression subscriptTripletTail?
	| subscriptTripletTail
    ;

subscriptTripletTail 
    : COLON expression? 
    | COLON expression COLON expression
	| DOUBLECOLON expression
    ;

logicalConstant
   : (TRUE | FALSE)
   | TRUE  UNDERSCORE kindParam
   | FALSE UNDERSCORE kindParam DOT
   ;

kindParam : ICON | namedConstantUse ;


unsignedArithmeticConstant
   : (ICON | RDCON)
   | complexConst
   | ICON UNDERSCORE kindParam 
   | RDCON UNDERSCORE kindParam
   ;

complexConst
   : LPAREN complexComponent COMMA  RPAREN
   ;

complexComponent 
    : ((PLUS | MINUS))? ICON 
    | RDCON
    | NAME
    ;

constantExpr : expression ;

ifStmt : IF LPAREN expression RPAREN actionStmt ;