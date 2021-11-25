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


program
   : COMMENTORNEWLINE* executableProgram COMMENTORNEWLINE* 
   ;

executableProgram : programUnit+  ;

programUnit
    : mainProgram            
	| functionSubprogram      
	| subroutineSubprogram    
	| blockDataSubprogram  
    | module 
    ;

mainProgram : programStmt? mainRange ;

programStmt : PROGRAM NAME EOS ;

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
    : USE NAME EOS                      
	| USE NAME COMMA ONLY COLON EOS     
	| USE NAME COMMA renameList EOS     
	| USE NAME COMMA ONLY COLON onlyList EOS 
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

parameterStmt : PARAMETER LPAREN namedConstantDefList RPAREN EOS ;

namedConstantDefList : namedConstantDef+;

namedConstantDef: NAME ASSIGN expression ;

endProgramStmt 
    : END EOS 
    | END PROGRAM NAME? EOS
    ;
    

blockDataSubprogram 
    : blockDataStmt blockDataBody endBlockDataStmt
	| blockDataStmt endBlockDataStmt
    ;

blockDataStmt 
    : BLOCKDATA NAME? EOS 
    | BLOCK DATA NAME? EOS 
    ;

blockDataBody : blockDataBodyConstruct
	| blockDataBody blockDataBodyConstruct
    ;

blockDataBodyConstruct : specificationPartConstruct;

endBlockDataStmt : 
	ENDBLOCKDATA NAME? EOS
	| END BLOCKDATA NAME? EOS
	| ENDBLOCK DATA NAME? EOS
	| END BLOCK DATA NAME? EOS
    | END EOS
    ;

formatStmt: FORMAT LPAREN fmtSpec? RPAREN EOS ;

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
    : END MODULE NAME? EOS 
	| ENDMODULE NAME? EOS
	| END EOS
    ;

entryStmt 
    : ENTRY NAME subroutineParList RESULT LPAREN NAME RPAREN EOS 
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

targetStmt : TARGET DOUBLECOLON? targetObjectList EOS ;

targetObjectList : targetObject (COMMA targetObject)* ;

targetObject
    : objectName
	| objectName LPAREN arraySpec RPAREN
    ;

pointerStmt : POINTER DOUBLECOLON? pointerStmtObjectList EOS ;

pointerStmtObjectList : pointerStmtObject (COMMA pointerStmtObject)* ;

pointerStmtObject 
    : objectName
	| objectName LPAREN deferredShapeSpecList RPAREN
    ;

optionalStmt : OPTIONAL DOUBLECOLON? optionalParList EOS ;

optionalParList : optionalPar (COMMA optionalPar)* ;

optionalPar : dummyArgName ;

namelistStmt : NAMELIST namelistGroups EOS ;

namelistGroups 
    : DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups COMMA DIV namelistGroupName DIV namelistGroupObject
	| namelistGroups COMMA namelistGroupObject
    ;

namelistGroupName : NAME ;

namelistGroupObject : variableName ;

intentStmt : INTENT LPAREN intentSpec RPAREN DOUBLECOLON? intentParList EOS ;

intentParList : intentPar (COMMA intentPar) ;

intentPar : dummyArgName ;

dummyArgName : NAME;

intentSpec : (IN | OUT | INOUT);

allocatableStmt : ALLOCATABLE DOUBLECOLON? arrayAllocationList EOS ;

arrayAllocationList : arrayAllocation (COMMA arrayAllocation)* ;

arrayAllocation 
    : arrayName
    | arrayName LPAREN deferredShapeSpecList RPAREN
    ;

arrayName : ident ;

accessStmt 
    : ACCESSSPEC DOUBLECOLON? accessIdList EOS
	| ACCESSSPEC EOS 
    ;

accessIdList : accessId (COMMA accessId) ;

accessId : genericName | genericSpec ;

genericName : ident ;

saveStmt 
    : SAVE EOS
	| SAVE savedEntityList EOS
    | SAVE DOUBLECOLON savedEntityList EOS
    ;

savedEntityList : savedEntity+ ;

savedEntity : variableName  | savedCommonBlock;

savedCommonBlock : DIV commonBlockName DIV ;

intrinsicStmt : INTRINSIC intrinsicList EOS;

intrinsicList : intrinsicProcedureName+ ;

intrinsicProcedureName : NAME ;

externalStmt : EXTERNAL externalNameList EOS ;

externalNameList : externalName+ ;

externalName : NAME;

equivalenceStmt : EQUIVALENCE equivalenceSetList EOS ;

equivalenceSetList : equivalenceSet+ ; 

equivalenceSet : LPAREN equivalenceObject COMMA equivalenceObjectList RPAREN ;

equivalenceObject : variable;

equivalenceObjectList : equivalenceObject+ ;

dimensionStmt 
    : DIMENSION arrayDeclaratorList EOS 
    | DIMENSION DOUBLECOLON arrayDeclaratorList EOS
    ;

arrayDeclaratorList : arrayDeclarator+ ;

commonStmt : COMMON comlist EOS; 

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
    : typeSpec entityDeclList EOS                           
    | typeSpec attrSpecSeq? DOUBLECOLON entityDeclList EOS  
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
    : ENDINTERFACE EOS
	| END INTERFACE EOS 
    ;

interfaceStmt
    : INTERFACE NAME EOS
	| INTERFACE genericSpec EOS
	| INTERFACE EOS
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
    : MODULE PROCEDURE procedureNameList EOS
    ;

procedureNameList : procedureName (COMMA procedureName)* ;

procedureName : ident ;

interfaceBody 
    : functionPrefix NAME functionInterfaceRange
	| SUBROUTINE NAME subroutineInterfaceRange
    ;

subroutineInterfaceRange 
    : subroutineParList EOS subprogramInterfaceBody? endSubroutineStmt
    ;

endSubroutineStmt
    : END EOS 
	| END SUBROUTINE NAME? EOS;


recursive : RECURSIVE ;
functionPrefix
    :  recursive? typeSpec? FUNCTION #functionPrefixRec
	| typeSpec RECURSIVE FUNCTION #functionPrefixTyp
    ;

functionInterfaceRange
    : functionParList EOS subprogramInterfaceBody? endFunctionStmt
    ;

functionParList :LPAREN functionPars? RPAREN ;

functionPars : functionPar (COMMA functionPar)* ;

functionPar : dummyArgName;

subprogramInterfaceBody 
    : specificationPartConstruct
	| subprogramInterfaceBody specificationPartConstruct   
    ;

endFunctionStmt 
    : END EOS
    | END FUNCTION NAME? EOS
    ;

derivedTypeDef : derivedTypeStmt derivedTypeBody endTypeStmt ;

endTypeStmt 
    : ENDTYPE NAME EOS
	| ENDTYPE EOS
	| END TYPE NAME EOS
	| END TYPE EOS
    ;

derivedTypeStmt 
    : TYPE NAME EOS
	| TYPE DOUBLECOLON NAME EOS
	| TYPE COMMA ACCESSSPEC DOUBLECOLON NAME EOS
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
    : PRIVATE EOS
	| SEQUENCE EOS
    ;

componentDefStmt
    : typeSpec COMMA componentAttrSpecList DOUBLECOLON componentDeclList EOS
	| typeSpec DOUBLECOLON componentDeclList EOS
	| typeSpec componentDeclList EOS
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
    : MODULE moduleName EOS
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

containsStmt : CONTAINS EOS ;

moduleSubprogram : functionSubprogram | subroutineSubprogram ;

functionSubprogram : functionPrefix functionName functionRange ;

functionName : NAME;

functionRange 
    : functionParList EOS body? endFunctionStmt 
	| functionParList RESULT LPAREN NAME RPAREN EOS body? endFunctionStmt
    | functionParList RESULT LPAREN NAME RPAREN EOS bodyPlusInternals endFunctionStmt
	| functionParList EOS bodyPlusInternals endFunctionStmt
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

elsewhereStmt : ELSEWHERE EOS ;

endWhereStmt 
    : ENDWHERE EOS
	| END WHERE EOS
    ;

where 
    : whereConstructStmt
	| where assignmentStmt 
    ;

whereConstructStmt : WHERE LPAREN maskExpr RPAREN EOS ;

maskExpr : expression ;

caseConstruct
    : NAME COLON SELECTCASE LPAREN expression RPAREN EOS selectCaseRange
	| SELECTCASE LPAREN expression RPAREN EOS selectCaseRange
	| NAME COLON SELECT CASE LPAREN expression RPAREN EOS selectCaseRange
	| SELECT CASE LPAREN expression RPAREN EOS selectCaseRange
    ;

selectCaseRange 
    : selectCaseBody endSelectStmt
	| endSelectStmt
    ;

endSelectStmt : (ENDSELECT NAME? EOS) | ( END SELECT NAME? EOS);

selectCaseBody
    : caseStmt
	| selectCaseBody caseBodyConstruct
    ;

caseBodyConstruct : caseStmt | executionPartConstruct;

caseStmt
    : CASE caseSelector EOS
	| CASE caseSelector NAME EOS
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

ifThenStmt : IF LPAREN expression RPAREN THEN EOS;

conditionalBody : executionPartConstruct*;

elseIfConstruct :  elseIfStmt conditionalBody;

elseIfStmt 
    : ELSEIF LPAREN expression RPAREN THEN 
    | ELSE IF LPAREN expression RPAREN THEN EOS
    ;

elseConstruct : elseStmt conditionalBody ;

elseStmt : ELSE EOS;

endIfStmt 
    : ENDIF EOS
    | END IF EOS
    ;

doConstruct 
    : labelDoStmt
    | blockDoConstruct 
    ;

blockDoConstruct : nameColon? DO commaLoopControl? EOS executionPartConstruct* endDoStmt
    ;

endDoStmt 
    : ENDDO endName? EOS
    | END DO endName? EOS 
    ;

endName : ident;

nameColon : NAME COLON ;

labelDoStmt : DO doLblRef commaLoopControl EOS executionPartConstruct* doLblDef doLabelStmt;

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

doubleDoStmt : DO lblRef commaLoopControl EOS ;

dataStmt : DATA dataStmtSet ((COMMA)? dataStmtSet)* EOS;

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
    : NAME IMPLIEDT target EOS
	| NAME sFExprListRef? PCT nameDataRef IMPLIEDT target EOS
    ;

target : expression;

nullifyStmt : NULLIFY LPAREN pointerObjectList RPAREN EOS ;

pointerObjectList : pointerObject (COMMA pointerObject)* ;

pointerObject : NAME | pointerField ;

pointerField 
    : NAME sFExprListRef? PCT NAME 
    | pointerField fieldSelector
    ;

exitStmt : EXIT endName? EOS ;

deallocateStmt 
    : DEALLOCATE LPAREN allocateObjectList COMMA STAT ASSIGN variable RPAREN EOS
	| DEALLOCATE LPAREN allocateObjectList RPAREN EOS
    ;

allocateObjectList : allocateObject (COMMA allocateObject)*;


cycleStmt : CYCLE endName? EOS
    ;

allocateStmt 
    : ALLOCATE LPAREN allocationList COMMA STAT ASSIGN variable RPAREN EOS
	| ALLOCATE LPAREN allocationList RPAREN EOS
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


stopStmt : STOP (ICON | SCON)? EOS ;

writeStmt : WRITE LPAREN ioControlSpecList RPAREN outputItemList? EOS;

ioControlSpecList 
    : unitIdentifier DOLLAR COMMA
	| unitIdentifier COMMA formatIdentifier
	| unitIdentifier COMMA ioControlSpec
	| ioControlSpec
	| ioControlSpecList COMMA ioControlSpec
    ;

stmtFunctionStmt : NAME stmtFunctionRange ;

stmtFunctionRange : LPAREN sFDummyArgNameList? RPAREN ASSIGN expression EOS;

sFDummyArgNameList : sFDummyArgName (COMMA sFDummyArgName)*;

sFDummyArgName : NAME ;

returnStmt : RETURN expression? EOS ;

rewindStmt : (REWIND unitIdentifier EOS) | (REWIND LPAREN positionSpecList RPAREN EOS) ;

readStmt 
    : READ rdCtlSpec inputItemList? EOS
	| READ rdFmtId commaInputItemList? EOS
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
    : PRINT formatIdentifier COMMA outputItemList EOS
	| PRINT formatIdentifier EOS
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

pauseStmt : PAUSE (ICON | SCON)? EOS ;

openStmt : OPEN LPAREN connectSpecList RPAREN EOS ;

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
    : INQUIRE LPAREN inquireSpecList RPAREN EOS 
    | INQUIRE LPAREN IOLENGTH ASSIGN scalarVariable RPAREN outputItemList EOS
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
    : (GOTO | GO TO) variableName EOS
	| (GOTO | GO TO) variableName LPAREN lblRefList RPAREN EOS
	| (GOTO | GO TO) variableComma LPAREN lblRefList RPAREN EOS
    ;

variableComma : variableName COMMA ;

gotoStmt : (GOTO | GO TO) lblRef EOS ;

computedGotoStmt : GOTO LPAREN lblRefList RPAREN COMMA? expression EOS ;

lblRefList : lblRef (COMMA lblRef)* ;

endfileStmt : ((ENDFILE| END FILE) unitIdentifier EOS) | ((ENDFILE| END FILE) LPAREN positionSpecList RPAREN EOS);

continueStmt : CONTINUE EOS ;

closeStmt : CLOSE LPAREN closeSpecList RPAREN EOS ;

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
    : CALL subroutineNameUse EOS
	| CALL subroutineNameUse LPAREN subroutineArgList RPAREN EOS
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

arithmeticIfStmt : IF LPAREN expression RPAREN lblRef COMMA lblRef COMMA lblRef EOS;

lblRef : label;

label : ICON;

assignmentStmt 
    : label? NAME sFExprListRef? substringRange? ASSIGN expression EOS
    | NAME sFExprListRef? PCT nameDataRef ASSIGN expression EOS
	| NAME LPAREN sFDummyArgNameList RPAREN PCT nameDataRef ASSIGN expression EOS
    ;

sFExprListRef : LPAREN sFExprList commaSectionSubscript* RPAREN ;

sFExprList 
    : expression COLON? expression?
	| COLON expression?
    | expression? COLON expression COLON expression
	| expression? DOUBLECOLON expression
    ;

commaSectionSubscript : COMMA sectionSubscript;

assignStmt : ASSIGNSTMT lblRef TO variableName EOS;

backspaceStmt 
    : BACKSPACE unitIdentifier EOS
	| BACKSPACE LPAREN positionSpecList RPAREN EOS
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
    : subroutineParList EOS body? endSubroutineStmt 
    | subroutineParList EOS bodyPlusInternals endSubroutineStmt
    ;

includeStmt 
    : INCLUDE SCON EOS
    ;

implicitStmt 
    : IMPLICIT  implicitSpecList EOS
    | IMPLICIT NONE EOS ;

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