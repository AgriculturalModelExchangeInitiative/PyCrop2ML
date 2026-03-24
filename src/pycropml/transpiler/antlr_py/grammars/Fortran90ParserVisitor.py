# Generated from Fortran90Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Fortran90Parser import Fortran90Parser
else:
    from Fortran90Parser import Fortran90Parser

# This class defines a complete generic visitor for a parse tree produced by Fortran90Parser.

class Fortran90ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Fortran90Parser#program.
    def visitProgram(self, ctx:Fortran90Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#executableProgram.
    def visitExecutableProgram(self, ctx:Fortran90Parser.ExecutableProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#programUnit.
    def visitProgramUnit(self, ctx:Fortran90Parser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#mainProgram.
    def visitMainProgram(self, ctx:Fortran90Parser.MainProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#programStmt.
    def visitProgramStmt(self, ctx:Fortran90Parser.ProgramStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#mainRange.
    def visitMainRange(self, ctx:Fortran90Parser.MainRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#bodyPlusInternals.
    def visitBodyPlusInternals(self, ctx:Fortran90Parser.BodyPlusInternalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#internalSubprogram.
    def visitInternalSubprogram(self, ctx:Fortran90Parser.InternalSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#specificationPartConstruct.
    def visitSpecificationPartConstruct(self, ctx:Fortran90Parser.SpecificationPartConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#useStmt.
    def visitUseStmt(self, ctx:Fortran90Parser.UseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#onlyList.
    def visitOnlyList(self, ctx:Fortran90Parser.OnlyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#onlyStmt.
    def visitOnlyStmt(self, ctx:Fortran90Parser.OnlyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#renameList.
    def visitRenameList(self, ctx:Fortran90Parser.RenameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rename.
    def visitRename(self, ctx:Fortran90Parser.RenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#useName.
    def visitUseName(self, ctx:Fortran90Parser.UseNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#parameterStmt.
    def visitParameterStmt(self, ctx:Fortran90Parser.ParameterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namedConstantDefList.
    def visitNamedConstantDefList(self, ctx:Fortran90Parser.NamedConstantDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namedConstantDef.
    def visitNamedConstantDef(self, ctx:Fortran90Parser.NamedConstantDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endProgramStmt.
    def visitEndProgramStmt(self, ctx:Fortran90Parser.EndProgramStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#blockDataSubprogram.
    def visitBlockDataSubprogram(self, ctx:Fortran90Parser.BlockDataSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#blockDataStmt.
    def visitBlockDataStmt(self, ctx:Fortran90Parser.BlockDataStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#blockDataBody.
    def visitBlockDataBody(self, ctx:Fortran90Parser.BlockDataBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#blockDataBodyConstruct.
    def visitBlockDataBodyConstruct(self, ctx:Fortran90Parser.BlockDataBodyConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endBlockDataStmt.
    def visitEndBlockDataStmt(self, ctx:Fortran90Parser.EndBlockDataStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#formatStmt.
    def visitFormatStmt(self, ctx:Fortran90Parser.FormatStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#fmtSpec.
    def visitFmtSpec(self, ctx:Fortran90Parser.FmtSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#formatedit.
    def visitFormatedit(self, ctx:Fortran90Parser.FormateditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#editElement.
    def visitEditElement(self, ctx:Fortran90Parser.EditElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#mislexedFcon.
    def visitMislexedFcon(self, ctx:Fortran90Parser.MislexedFconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#module.
    def visitModule(self, ctx:Fortran90Parser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endModuleStmt.
    def visitEndModuleStmt(self, ctx:Fortran90Parser.EndModuleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#entryStmt.
    def visitEntryStmt(self, ctx:Fortran90Parser.EntryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineParList.
    def visitSubroutineParList(self, ctx:Fortran90Parser.SubroutineParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutinePars.
    def visitSubroutinePars(self, ctx:Fortran90Parser.SubroutineParsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutinePar.
    def visitSubroutinePar(self, ctx:Fortran90Parser.SubroutineParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#declarationConstruct.
    def visitDeclarationConstruct(self, ctx:Fortran90Parser.DeclarationConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#specificationStmt.
    def visitSpecificationStmt(self, ctx:Fortran90Parser.SpecificationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#targetStmt.
    def visitTargetStmt(self, ctx:Fortran90Parser.TargetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#targetObjectList.
    def visitTargetObjectList(self, ctx:Fortran90Parser.TargetObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#targetObject.
    def visitTargetObject(self, ctx:Fortran90Parser.TargetObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerStmt.
    def visitPointerStmt(self, ctx:Fortran90Parser.PointerStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerStmtObjectList.
    def visitPointerStmtObjectList(self, ctx:Fortran90Parser.PointerStmtObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerStmtObject.
    def visitPointerStmtObject(self, ctx:Fortran90Parser.PointerStmtObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#optionalStmt.
    def visitOptionalStmt(self, ctx:Fortran90Parser.OptionalStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#optionalParList.
    def visitOptionalParList(self, ctx:Fortran90Parser.OptionalParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#optionalPar.
    def visitOptionalPar(self, ctx:Fortran90Parser.OptionalParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namelistStmt.
    def visitNamelistStmt(self, ctx:Fortran90Parser.NamelistStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namelistGroups.
    def visitNamelistGroups(self, ctx:Fortran90Parser.NamelistGroupsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namelistGroupName.
    def visitNamelistGroupName(self, ctx:Fortran90Parser.NamelistGroupNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namelistGroupObject.
    def visitNamelistGroupObject(self, ctx:Fortran90Parser.NamelistGroupObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intentStmt.
    def visitIntentStmt(self, ctx:Fortran90Parser.IntentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intentParList.
    def visitIntentParList(self, ctx:Fortran90Parser.IntentParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intentPar.
    def visitIntentPar(self, ctx:Fortran90Parser.IntentParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dummyArgName.
    def visitDummyArgName(self, ctx:Fortran90Parser.DummyArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intentSpec.
    def visitIntentSpec(self, ctx:Fortran90Parser.IntentSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocatableStmt.
    def visitAllocatableStmt(self, ctx:Fortran90Parser.AllocatableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayAllocationList.
    def visitArrayAllocationList(self, ctx:Fortran90Parser.ArrayAllocationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayAllocation.
    def visitArrayAllocation(self, ctx:Fortran90Parser.ArrayAllocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayName.
    def visitArrayName(self, ctx:Fortran90Parser.ArrayNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#accessStmt.
    def visitAccessStmt(self, ctx:Fortran90Parser.AccessStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#accessIdList.
    def visitAccessIdList(self, ctx:Fortran90Parser.AccessIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#accessId.
    def visitAccessId(self, ctx:Fortran90Parser.AccessIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#genericName.
    def visitGenericName(self, ctx:Fortran90Parser.GenericNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#saveStmt.
    def visitSaveStmt(self, ctx:Fortran90Parser.SaveStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#savedEntityList.
    def visitSavedEntityList(self, ctx:Fortran90Parser.SavedEntityListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#savedEntity.
    def visitSavedEntity(self, ctx:Fortran90Parser.SavedEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#savedCommonBlock.
    def visitSavedCommonBlock(self, ctx:Fortran90Parser.SavedCommonBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intrinsicStmt.
    def visitIntrinsicStmt(self, ctx:Fortran90Parser.IntrinsicStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intrinsicList.
    def visitIntrinsicList(self, ctx:Fortran90Parser.IntrinsicListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#intrinsicProcedureName.
    def visitIntrinsicProcedureName(self, ctx:Fortran90Parser.IntrinsicProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#externalStmt.
    def visitExternalStmt(self, ctx:Fortran90Parser.ExternalStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#externalNameList.
    def visitExternalNameList(self, ctx:Fortran90Parser.ExternalNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#externalName.
    def visitExternalName(self, ctx:Fortran90Parser.ExternalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivalenceStmt.
    def visitEquivalenceStmt(self, ctx:Fortran90Parser.EquivalenceStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivalenceSetList.
    def visitEquivalenceSetList(self, ctx:Fortran90Parser.EquivalenceSetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivalenceSet.
    def visitEquivalenceSet(self, ctx:Fortran90Parser.EquivalenceSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivalenceObject.
    def visitEquivalenceObject(self, ctx:Fortran90Parser.EquivalenceObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivalenceObjectList.
    def visitEquivalenceObjectList(self, ctx:Fortran90Parser.EquivalenceObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dimensionStmt.
    def visitDimensionStmt(self, ctx:Fortran90Parser.DimensionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayDeclaratorList.
    def visitArrayDeclaratorList(self, ctx:Fortran90Parser.ArrayDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commonStmt.
    def visitCommonStmt(self, ctx:Fortran90Parser.CommonStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#comlist.
    def visitComlist(self, ctx:Fortran90Parser.ComlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commonBlockObject.
    def visitCommonBlockObject(self, ctx:Fortran90Parser.CommonBlockObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayDeclarator.
    def visitArrayDeclarator(self, ctx:Fortran90Parser.ArrayDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#comblock.
    def visitComblock(self, ctx:Fortran90Parser.ComblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commonBlockName.
    def visitCommonBlockName(self, ctx:Fortran90Parser.CommonBlockNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#typeDeclarationStmt.
    def visitTypeDeclarationStmt(self, ctx:Fortran90Parser.TypeDeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#attrSpecSeq.
    def visitAttrSpecSeq(self, ctx:Fortran90Parser.AttrSpecSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#attrSpec.
    def visitAttrSpec(self, ctx:Fortran90Parser.AttrSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#entityDeclList.
    def visitEntityDeclList(self, ctx:Fortran90Parser.EntityDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#entityDecl.
    def visitEntityDecl(self, ctx:Fortran90Parser.EntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#objectName.
    def visitObjectName(self, ctx:Fortran90Parser.ObjectNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arraySpec.
    def visitArraySpec(self, ctx:Fortran90Parser.ArraySpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assumedShapeSpecList.
    def visitAssumedShapeSpecList(self, ctx:Fortran90Parser.AssumedShapeSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assumedShapeSpec.
    def visitAssumedShapeSpec(self, ctx:Fortran90Parser.AssumedShapeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assumedSizeSpec.
    def visitAssumedSizeSpec(self, ctx:Fortran90Parser.AssumedSizeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#interfaceBlock.
    def visitInterfaceBlock(self, ctx:Fortran90Parser.InterfaceBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endInterfaceStmt.
    def visitEndInterfaceStmt(self, ctx:Fortran90Parser.EndInterfaceStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#interfaceStmt.
    def visitInterfaceStmt(self, ctx:Fortran90Parser.InterfaceStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#genericSpec.
    def visitGenericSpec(self, ctx:Fortran90Parser.GenericSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#definedOperator.
    def visitDefinedOperator(self, ctx:Fortran90Parser.DefinedOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#interfaceBlockBody.
    def visitInterfaceBlockBody(self, ctx:Fortran90Parser.InterfaceBlockBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#interfaceBodyPartConstruct.
    def visitInterfaceBodyPartConstruct(self, ctx:Fortran90Parser.InterfaceBodyPartConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#moduleProcedureStmt.
    def visitModuleProcedureStmt(self, ctx:Fortran90Parser.ModuleProcedureStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#procedureNameList.
    def visitProcedureNameList(self, ctx:Fortran90Parser.ProcedureNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#procedureName.
    def visitProcedureName(self, ctx:Fortran90Parser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#interfaceBody.
    def visitInterfaceBody(self, ctx:Fortran90Parser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineInterfaceRange.
    def visitSubroutineInterfaceRange(self, ctx:Fortran90Parser.SubroutineInterfaceRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endSubroutineStmt.
    def visitEndSubroutineStmt(self, ctx:Fortran90Parser.EndSubroutineStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#recursive.
    def visitRecursive(self, ctx:Fortran90Parser.RecursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionPrefixRec.
    def visitFunctionPrefixRec(self, ctx:Fortran90Parser.FunctionPrefixRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionPrefixTyp.
    def visitFunctionPrefixTyp(self, ctx:Fortran90Parser.FunctionPrefixTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionInterfaceRange.
    def visitFunctionInterfaceRange(self, ctx:Fortran90Parser.FunctionInterfaceRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionParList.
    def visitFunctionParList(self, ctx:Fortran90Parser.FunctionParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionPars.
    def visitFunctionPars(self, ctx:Fortran90Parser.FunctionParsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionPar.
    def visitFunctionPar(self, ctx:Fortran90Parser.FunctionParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subprogramInterfaceBody.
    def visitSubprogramInterfaceBody(self, ctx:Fortran90Parser.SubprogramInterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endFunctionStmt.
    def visitEndFunctionStmt(self, ctx:Fortran90Parser.EndFunctionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#derivedTypeDef.
    def visitDerivedTypeDef(self, ctx:Fortran90Parser.DerivedTypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endTypeStmt.
    def visitEndTypeStmt(self, ctx:Fortran90Parser.EndTypeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#derivedTypeStmt.
    def visitDerivedTypeStmt(self, ctx:Fortran90Parser.DerivedTypeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#derivedTypeBody.
    def visitDerivedTypeBody(self, ctx:Fortran90Parser.DerivedTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#derivedTypeBodyConstruct.
    def visitDerivedTypeBodyConstruct(self, ctx:Fortran90Parser.DerivedTypeBodyConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#privateSequenceStmt.
    def visitPrivateSequenceStmt(self, ctx:Fortran90Parser.PrivateSequenceStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentDefStmt.
    def visitComponentDefStmt(self, ctx:Fortran90Parser.ComponentDefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentDeclList.
    def visitComponentDeclList(self, ctx:Fortran90Parser.ComponentDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentDecl.
    def visitComponentDecl(self, ctx:Fortran90Parser.ComponentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentName.
    def visitComponentName(self, ctx:Fortran90Parser.ComponentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentAttrSpecList.
    def visitComponentAttrSpecList(self, ctx:Fortran90Parser.ComponentAttrSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentAttrSpec.
    def visitComponentAttrSpec(self, ctx:Fortran90Parser.ComponentAttrSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#componentArraySpec.
    def visitComponentArraySpec(self, ctx:Fortran90Parser.ComponentArraySpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#explicitShapeSpecList.
    def visitExplicitShapeSpecList(self, ctx:Fortran90Parser.ExplicitShapeSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#explicitShapeSpec.
    def visitExplicitShapeSpec(self, ctx:Fortran90Parser.ExplicitShapeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#lowerBound.
    def visitLowerBound(self, ctx:Fortran90Parser.LowerBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#upperBound.
    def visitUpperBound(self, ctx:Fortran90Parser.UpperBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#deferredShapeSpecList.
    def visitDeferredShapeSpecList(self, ctx:Fortran90Parser.DeferredShapeSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#deferredShapeSpec.
    def visitDeferredShapeSpec(self, ctx:Fortran90Parser.DeferredShapeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#typeSpec.
    def visitTypeSpec(self, ctx:Fortran90Parser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#kindSelector.
    def visitKindSelector(self, ctx:Fortran90Parser.KindSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#typeName.
    def visitTypeName(self, ctx:Fortran90Parser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#charSelector.
    def visitCharSelector(self, ctx:Fortran90Parser.CharSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#lengthSelector.
    def visitLengthSelector(self, ctx:Fortran90Parser.LengthSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#charLength.
    def visitCharLength(self, ctx:Fortran90Parser.CharLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#constant.
    def visitConstant(self, ctx:Fortran90Parser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#bozLiteralConstant.
    def visitBozLiteralConstant(self, ctx:Fortran90Parser.BozLiteralConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#structureConstructor.
    def visitStructureConstructor(self, ctx:Fortran90Parser.StructureConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#exprList.
    def visitExprList(self, ctx:Fortran90Parser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#namedConstantUse.
    def visitNamedConstantUse(self, ctx:Fortran90Parser.NamedConstantUseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#typeParamValue.
    def visitTypeParamValue(self, ctx:Fortran90Parser.TypeParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#moduleStmt.
    def visitModuleStmt(self, ctx:Fortran90Parser.ModuleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#moduleName.
    def visitModuleName(self, ctx:Fortran90Parser.ModuleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ident.
    def visitIdent(self, ctx:Fortran90Parser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#complexSubmodule.
    def visitComplexSubmodule(self, ctx:Fortran90Parser.ComplexSubmoduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#complexSpecPart.
    def visitComplexSpecPart(self, ctx:Fortran90Parser.ComplexSpecPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#submoduleStmt.
    def visitSubmoduleStmt(self, ctx:Fortran90Parser.SubmoduleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#specPartStmt.
    def visitSpecPartStmt(self, ctx:Fortran90Parser.SpecPartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#moduleSubprogramPartConstruct.
    def visitModuleSubprogramPartConstruct(self, ctx:Fortran90Parser.ModuleSubprogramPartConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#containsStmt.
    def visitContainsStmt(self, ctx:Fortran90Parser.ContainsStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#moduleSubprogram.
    def visitModuleSubprogram(self, ctx:Fortran90Parser.ModuleSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionSubprogram.
    def visitFunctionSubprogram(self, ctx:Fortran90Parser.FunctionSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionName.
    def visitFunctionName(self, ctx:Fortran90Parser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionRange.
    def visitFunctionRange(self, ctx:Fortran90Parser.FunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#body.
    def visitBody(self, ctx:Fortran90Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#bodyConstruct.
    def visitBodyConstruct(self, ctx:Fortran90Parser.BodyConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#executableConstruct.
    def visitExecutableConstruct(self, ctx:Fortran90Parser.ExecutableConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#whereConstruct.
    def visitWhereConstruct(self, ctx:Fortran90Parser.WhereConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elseWhere.
    def visitElseWhere(self, ctx:Fortran90Parser.ElseWhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elsewhereStmt.
    def visitElsewhereStmt(self, ctx:Fortran90Parser.ElsewhereStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endWhereStmt.
    def visitEndWhereStmt(self, ctx:Fortran90Parser.EndWhereStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#where.
    def visitWhere(self, ctx:Fortran90Parser.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#whereConstructStmt.
    def visitWhereConstructStmt(self, ctx:Fortran90Parser.WhereConstructStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#maskExpr.
    def visitMaskExpr(self, ctx:Fortran90Parser.MaskExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#caseConstruct.
    def visitCaseConstruct(self, ctx:Fortran90Parser.CaseConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#selectCaseRange.
    def visitSelectCaseRange(self, ctx:Fortran90Parser.SelectCaseRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endSelectStmt.
    def visitEndSelectStmt(self, ctx:Fortran90Parser.EndSelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#selectCaseBody.
    def visitSelectCaseBody(self, ctx:Fortran90Parser.SelectCaseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#caseBodyConstruct.
    def visitCaseBodyConstruct(self, ctx:Fortran90Parser.CaseBodyConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#caseStmt.
    def visitCaseStmt(self, ctx:Fortran90Parser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#caseSelector.
    def visitCaseSelector(self, ctx:Fortran90Parser.CaseSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#caseValueRangeList.
    def visitCaseValueRangeList(self, ctx:Fortran90Parser.CaseValueRangeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#litteralExpression.
    def visitLitteralExpression(self, ctx:Fortran90Parser.LitteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#afterColonExpression.
    def visitAfterColonExpression(self, ctx:Fortran90Parser.AfterColonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#beforeColonExpression.
    def visitBeforeColonExpression(self, ctx:Fortran90Parser.BeforeColonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#midlleColonExpression.
    def visitMidlleColonExpression(self, ctx:Fortran90Parser.MidlleColonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ifConstruct.
    def visitIfConstruct(self, ctx:Fortran90Parser.IfConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ifThenStmt.
    def visitIfThenStmt(self, ctx:Fortran90Parser.IfThenStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#conditionalBody.
    def visitConditionalBody(self, ctx:Fortran90Parser.ConditionalBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elseIfConstruct.
    def visitElseIfConstruct(self, ctx:Fortran90Parser.ElseIfConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elseIfStmt.
    def visitElseIfStmt(self, ctx:Fortran90Parser.ElseIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elseConstruct.
    def visitElseConstruct(self, ctx:Fortran90Parser.ElseConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#elseStmt.
    def visitElseStmt(self, ctx:Fortran90Parser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endIfStmt.
    def visitEndIfStmt(self, ctx:Fortran90Parser.EndIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#doConstruct.
    def visitDoConstruct(self, ctx:Fortran90Parser.DoConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#blockDoConstruct.
    def visitBlockDoConstruct(self, ctx:Fortran90Parser.BlockDoConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endDoStmt.
    def visitEndDoStmt(self, ctx:Fortran90Parser.EndDoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endName.
    def visitEndName(self, ctx:Fortran90Parser.EndNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#nameColon.
    def visitNameColon(self, ctx:Fortran90Parser.NameColonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#labelDoStmt.
    def visitLabelDoStmt(self, ctx:Fortran90Parser.LabelDoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#doLblRef.
    def visitDoLblRef(self, ctx:Fortran90Parser.DoLblRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#doLblDef.
    def visitDoLblDef(self, ctx:Fortran90Parser.DoLblDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#doLabelStmt.
    def visitDoLabelStmt(self, ctx:Fortran90Parser.DoLabelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#executionPartConstruct.
    def visitExecutionPartConstruct(self, ctx:Fortran90Parser.ExecutionPartConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#doubleDoStmt.
    def visitDoubleDoStmt(self, ctx:Fortran90Parser.DoubleDoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataStmt.
    def visitDataStmt(self, ctx:Fortran90Parser.DataStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataStmtSet.
    def visitDataStmtSet(self, ctx:Fortran90Parser.DataStmtSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dse1.
    def visitDse1(self, ctx:Fortran90Parser.Dse1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dse2.
    def visitDse2(self, ctx:Fortran90Parser.Dse2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataStmtValue.
    def visitDataStmtValue(self, ctx:Fortran90Parser.DataStmtValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataStmtObject.
    def visitDataStmtObject(self, ctx:Fortran90Parser.DataStmtObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#variable.
    def visitVariable(self, ctx:Fortran90Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subscriptListRef.
    def visitSubscriptListRef(self, ctx:Fortran90Parser.SubscriptListRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subscriptList.
    def visitSubscriptList(self, ctx:Fortran90Parser.SubscriptListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subscript.
    def visitSubscript(self, ctx:Fortran90Parser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#substringRange.
    def visitSubstringRange(self, ctx:Fortran90Parser.SubstringRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataImpliedDo.
    def visitDataImpliedDo(self, ctx:Fortran90Parser.DataImpliedDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataIDoObjectList.
    def visitDataIDoObjectList(self, ctx:Fortran90Parser.DataIDoObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#dataIDoObject.
    def visitDataIDoObject(self, ctx:Fortran90Parser.DataIDoObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#structureComponent.
    def visitStructureComponent(self, ctx:Fortran90Parser.StructureComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#fieldSelector.
    def visitFieldSelector(self, ctx:Fortran90Parser.FieldSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayElement.
    def visitArrayElement(self, ctx:Fortran90Parser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#impliedDoVariable.
    def visitImpliedDoVariable(self, ctx:Fortran90Parser.ImpliedDoVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commaLoopControl.
    def visitCommaLoopControl(self, ctx:Fortran90Parser.CommaLoopControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#loopControl.
    def visitLoopControl(self, ctx:Fortran90Parser.LoopControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#variableName.
    def visitVariableName(self, ctx:Fortran90Parser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commaExpr.
    def visitCommaExpr(self, ctx:Fortran90Parser.CommaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#actionStmt.
    def visitActionStmt(self, ctx:Fortran90Parser.ActionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#whereStmt.
    def visitWhereStmt(self, ctx:Fortran90Parser.WhereStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerAssignmentStmt.
    def visitPointerAssignmentStmt(self, ctx:Fortran90Parser.PointerAssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#target.
    def visitTarget(self, ctx:Fortran90Parser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#nullifyStmt.
    def visitNullifyStmt(self, ctx:Fortran90Parser.NullifyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerObjectList.
    def visitPointerObjectList(self, ctx:Fortran90Parser.PointerObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerObject.
    def visitPointerObject(self, ctx:Fortran90Parser.PointerObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pointerField.
    def visitPointerField(self, ctx:Fortran90Parser.PointerFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#exitStmt.
    def visitExitStmt(self, ctx:Fortran90Parser.ExitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#deallocateStmt.
    def visitDeallocateStmt(self, ctx:Fortran90Parser.DeallocateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocateObjectList.
    def visitAllocateObjectList(self, ctx:Fortran90Parser.AllocateObjectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#cycleStmt.
    def visitCycleStmt(self, ctx:Fortran90Parser.CycleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocateStmt.
    def visitAllocateStmt(self, ctx:Fortran90Parser.AllocateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocationList.
    def visitAllocationList(self, ctx:Fortran90Parser.AllocationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocation.
    def visitAllocation(self, ctx:Fortran90Parser.AllocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocateObject.
    def visitAllocateObject(self, ctx:Fortran90Parser.AllocateObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#allocatedShape.
    def visitAllocatedShape(self, ctx:Fortran90Parser.AllocatedShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#stopStmt.
    def visitStopStmt(self, ctx:Fortran90Parser.StopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#writeStmt.
    def visitWriteStmt(self, ctx:Fortran90Parser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ioControlSpecList.
    def visitIoControlSpecList(self, ctx:Fortran90Parser.IoControlSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#stmtFunctionStmt.
    def visitStmtFunctionStmt(self, ctx:Fortran90Parser.StmtFunctionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#stmtFunctionRange.
    def visitStmtFunctionRange(self, ctx:Fortran90Parser.StmtFunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sFDummyArgNameList.
    def visitSFDummyArgNameList(self, ctx:Fortran90Parser.SFDummyArgNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sFDummyArgName.
    def visitSFDummyArgName(self, ctx:Fortran90Parser.SFDummyArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#returnStmt.
    def visitReturnStmt(self, ctx:Fortran90Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rewindStmt.
    def visitRewindStmt(self, ctx:Fortran90Parser.RewindStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#readStmt.
    def visitReadStmt(self, ctx:Fortran90Parser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commaInputItemList.
    def visitCommaInputItemList(self, ctx:Fortran90Parser.CommaInputItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rdFmtId.
    def visitRdFmtId(self, ctx:Fortran90Parser.RdFmtIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rdFmtIdExpr.
    def visitRdFmtIdExpr(self, ctx:Fortran90Parser.RdFmtIdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inputItemList.
    def visitInputItemList(self, ctx:Fortran90Parser.InputItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inputItem.
    def visitInputItem(self, ctx:Fortran90Parser.InputItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inputImpliedDo.
    def visitInputImpliedDo(self, ctx:Fortran90Parser.InputImpliedDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rdCtlSpec.
    def visitRdCtlSpec(self, ctx:Fortran90Parser.RdCtlSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rdUnitId.
    def visitRdUnitId(self, ctx:Fortran90Parser.RdUnitIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#rdIoCtlSpecList.
    def visitRdIoCtlSpecList(self, ctx:Fortran90Parser.RdIoCtlSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ioControlSpec.
    def visitIoControlSpec(self, ctx:Fortran90Parser.IoControlSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#printStmt.
    def visitPrintStmt(self, ctx:Fortran90Parser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#outputItemList.
    def visitOutputItemList(self, ctx:Fortran90Parser.OutputItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#outputItemList1.
    def visitOutputItemList1(self, ctx:Fortran90Parser.OutputItemList1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#outputImpliedDo.
    def visitOutputImpliedDo(self, ctx:Fortran90Parser.OutputImpliedDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#formatIdentifier.
    def visitFormatIdentifier(self, ctx:Fortran90Parser.FormatIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#pauseStmt.
    def visitPauseStmt(self, ctx:Fortran90Parser.PauseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#openStmt.
    def visitOpenStmt(self, ctx:Fortran90Parser.OpenStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#connectSpecList.
    def visitConnectSpecList(self, ctx:Fortran90Parser.ConnectSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#connectSpec.
    def visitConnectSpec(self, ctx:Fortran90Parser.ConnectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inquireStmt.
    def visitInquireStmt(self, ctx:Fortran90Parser.InquireStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inquireSpecList.
    def visitInquireSpecList(self, ctx:Fortran90Parser.InquireSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#inquireSpec.
    def visitInquireSpec(self, ctx:Fortran90Parser.InquireSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assignedGotoStmt.
    def visitAssignedGotoStmt(self, ctx:Fortran90Parser.AssignedGotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#variableComma.
    def visitVariableComma(self, ctx:Fortran90Parser.VariableCommaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#gotoStmt.
    def visitGotoStmt(self, ctx:Fortran90Parser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#computedGotoStmt.
    def visitComputedGotoStmt(self, ctx:Fortran90Parser.ComputedGotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#lblRefList.
    def visitLblRefList(self, ctx:Fortran90Parser.LblRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#endfileStmt.
    def visitEndfileStmt(self, ctx:Fortran90Parser.EndfileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#continueStmt.
    def visitContinueStmt(self, ctx:Fortran90Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#closeStmt.
    def visitCloseStmt(self, ctx:Fortran90Parser.CloseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#closeSpecList.
    def visitCloseSpecList(self, ctx:Fortran90Parser.CloseSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#closeSpec.
    def visitCloseSpec(self, ctx:Fortran90Parser.CloseSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#cExpression.
    def visitCExpression(self, ctx:Fortran90Parser.CExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#cPrimary.
    def visitCPrimary(self, ctx:Fortran90Parser.CPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#cOperand.
    def visitCOperand(self, ctx:Fortran90Parser.COperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#cPrimaryConcatOp.
    def visitCPrimaryConcatOp(self, ctx:Fortran90Parser.CPrimaryConcatOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#callStmt.
    def visitCallStmt(self, ctx:Fortran90Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineNameUse.
    def visitSubroutineNameUse(self, ctx:Fortran90Parser.SubroutineNameUseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineArgList.
    def visitSubroutineArgList(self, ctx:Fortran90Parser.SubroutineArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineArg.
    def visitSubroutineArg(self, ctx:Fortran90Parser.SubroutineArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arithmeticIfStmt.
    def visitArithmeticIfStmt(self, ctx:Fortran90Parser.ArithmeticIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#lblRef.
    def visitLblRef(self, ctx:Fortran90Parser.LblRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#label.
    def visitLabel(self, ctx:Fortran90Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:Fortran90Parser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sFExprListRef.
    def visitSFExprListRef(self, ctx:Fortran90Parser.SFExprListRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sFExprList.
    def visitSFExprList(self, ctx:Fortran90Parser.SFExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#commaSectionSubscript.
    def visitCommaSectionSubscript(self, ctx:Fortran90Parser.CommaSectionSubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#assignStmt.
    def visitAssignStmt(self, ctx:Fortran90Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#backspaceStmt.
    def visitBackspaceStmt(self, ctx:Fortran90Parser.BackspaceStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#unitIdentifier.
    def visitUnitIdentifier(self, ctx:Fortran90Parser.UnitIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#positionSpecList.
    def visitPositionSpecList(self, ctx:Fortran90Parser.PositionSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#unitIdentifierComma.
    def visitUnitIdentifierComma(self, ctx:Fortran90Parser.UnitIdentifierCommaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#positionSpec.
    def visitPositionSpec(self, ctx:Fortran90Parser.PositionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#scalarVariable.
    def visitScalarVariable(self, ctx:Fortran90Parser.ScalarVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#uFExpr.
    def visitUFExpr(self, ctx:Fortran90Parser.UFExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#uFTerm.
    def visitUFTerm(self, ctx:Fortran90Parser.UFTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#uFFactor.
    def visitUFFactor(self, ctx:Fortran90Parser.UFFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#uFPrimary.
    def visitUFPrimary(self, ctx:Fortran90Parser.UFPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineSubprogram.
    def visitSubroutineSubprogram(self, ctx:Fortran90Parser.SubroutineSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineName.
    def visitSubroutineName(self, ctx:Fortran90Parser.SubroutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subroutineRange.
    def visitSubroutineRange(self, ctx:Fortran90Parser.SubroutineRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#includeStmt.
    def visitIncludeStmt(self, ctx:Fortran90Parser.IncludeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#implicitStmt.
    def visitImplicitStmt(self, ctx:Fortran90Parser.ImplicitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#implicitSpecList.
    def visitImplicitSpecList(self, ctx:Fortran90Parser.ImplicitSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#implicitSpec.
    def visitImplicitSpec(self, ctx:Fortran90Parser.ImplicitSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#implicitRanges.
    def visitImplicitRanges(self, ctx:Fortran90Parser.ImplicitRangesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#implicitRange.
    def visitImplicitRange(self, ctx:Fortran90Parser.ImplicitRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#expression.
    def visitExpression(self, ctx:Fortran90Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#definedBinaryOp.
    def visitDefinedBinaryOp(self, ctx:Fortran90Parser.DefinedBinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#level5Expr.
    def visitLevel5Expr(self, ctx:Fortran90Parser.Level5ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#equivOperand.
    def visitEquivOperand(self, ctx:Fortran90Parser.EquivOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#orOperand.
    def visitOrOperand(self, ctx:Fortran90Parser.OrOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#andOperand.
    def visitAndOperand(self, ctx:Fortran90Parser.AndOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#relOp.
    def visitRelOp(self, ctx:Fortran90Parser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#level4Expr.
    def visitLevel4Expr(self, ctx:Fortran90Parser.Level4ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#level3Expr.
    def visitLevel3Expr(self, ctx:Fortran90Parser.Level3ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#level2Expr.
    def visitLevel2Expr(self, ctx:Fortran90Parser.Level2ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sign.
    def visitSign(self, ctx:Fortran90Parser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#addOperand.
    def visitAddOperand(self, ctx:Fortran90Parser.AddOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#multOperand.
    def visitMultOperand(self, ctx:Fortran90Parser.MultOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#level1Expr.
    def visitLevel1Expr(self, ctx:Fortran90Parser.Level1ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#definedUnaryOp.
    def visitDefinedUnaryOp(self, ctx:Fortran90Parser.DefinedUnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#primary.
    def visitPrimary(self, ctx:Fortran90Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#arrayConstructor.
    def visitArrayConstructor(self, ctx:Fortran90Parser.ArrayConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#acValueList.
    def visitAcValueList(self, ctx:Fortran90Parser.AcValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#acValueList1.
    def visitAcValueList1(self, ctx:Fortran90Parser.AcValueList1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#acImpliedDo.
    def visitAcImpliedDo(self, ctx:Fortran90Parser.AcImpliedDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionReference.
    def visitFunctionReference(self, ctx:Fortran90Parser.FunctionReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionArgList.
    def visitFunctionArgList(self, ctx:Fortran90Parser.FunctionArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#functionArg.
    def visitFunctionArg(self, ctx:Fortran90Parser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#nameDataRef.
    def visitNameDataRef(self, ctx:Fortran90Parser.NameDataRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#complexDataRefTail.
    def visitComplexDataRefTail(self, ctx:Fortran90Parser.ComplexDataRefTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sectionSubscriptRef.
    def visitSectionSubscriptRef(self, ctx:Fortran90Parser.SectionSubscriptRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sectionSubscriptList.
    def visitSectionSubscriptList(self, ctx:Fortran90Parser.SectionSubscriptListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#sectionSubscript.
    def visitSectionSubscript(self, ctx:Fortran90Parser.SectionSubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#subscriptTripletTail.
    def visitSubscriptTripletTail(self, ctx:Fortran90Parser.SubscriptTripletTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#logicalConstant.
    def visitLogicalConstant(self, ctx:Fortran90Parser.LogicalConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#kindParam.
    def visitKindParam(self, ctx:Fortran90Parser.KindParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#unsignedArithmeticConstant.
    def visitUnsignedArithmeticConstant(self, ctx:Fortran90Parser.UnsignedArithmeticConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#complexConst.
    def visitComplexConst(self, ctx:Fortran90Parser.ComplexConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#complexComponent.
    def visitComplexComponent(self, ctx:Fortran90Parser.ComplexComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#constantExpr.
    def visitConstantExpr(self, ctx:Fortran90Parser.ConstantExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran90Parser#ifStmt.
    def visitIfStmt(self, ctx:Fortran90Parser.IfStmtContext):
        return self.visitChildren(ctx)



del Fortran90Parser