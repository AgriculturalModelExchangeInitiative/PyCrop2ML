# Generated from Fortran90Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Fortran90Parser import Fortran90Parser
else:
    from Fortran90Parser import Fortran90Parser

# This class defines a complete listener for a parse tree produced by Fortran90Parser.
class Fortran90ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Fortran90Parser#program.
    def enterProgram(self, ctx:Fortran90Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#program.
    def exitProgram(self, ctx:Fortran90Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#executableProgram.
    def enterExecutableProgram(self, ctx:Fortran90Parser.ExecutableProgramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#executableProgram.
    def exitExecutableProgram(self, ctx:Fortran90Parser.ExecutableProgramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#programUnit.
    def enterProgramUnit(self, ctx:Fortran90Parser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#programUnit.
    def exitProgramUnit(self, ctx:Fortran90Parser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#mainProgram.
    def enterMainProgram(self, ctx:Fortran90Parser.MainProgramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#mainProgram.
    def exitMainProgram(self, ctx:Fortran90Parser.MainProgramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#programStmt.
    def enterProgramStmt(self, ctx:Fortran90Parser.ProgramStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#programStmt.
    def exitProgramStmt(self, ctx:Fortran90Parser.ProgramStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#mainRange.
    def enterMainRange(self, ctx:Fortran90Parser.MainRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#mainRange.
    def exitMainRange(self, ctx:Fortran90Parser.MainRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#bodyPlusInternals.
    def enterBodyPlusInternals(self, ctx:Fortran90Parser.BodyPlusInternalsContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#bodyPlusInternals.
    def exitBodyPlusInternals(self, ctx:Fortran90Parser.BodyPlusInternalsContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#internalSubprogram.
    def enterInternalSubprogram(self, ctx:Fortran90Parser.InternalSubprogramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#internalSubprogram.
    def exitInternalSubprogram(self, ctx:Fortran90Parser.InternalSubprogramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#specificationPartConstruct.
    def enterSpecificationPartConstruct(self, ctx:Fortran90Parser.SpecificationPartConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#specificationPartConstruct.
    def exitSpecificationPartConstruct(self, ctx:Fortran90Parser.SpecificationPartConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#useStmt.
    def enterUseStmt(self, ctx:Fortran90Parser.UseStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#useStmt.
    def exitUseStmt(self, ctx:Fortran90Parser.UseStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#onlyList.
    def enterOnlyList(self, ctx:Fortran90Parser.OnlyListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#onlyList.
    def exitOnlyList(self, ctx:Fortran90Parser.OnlyListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#onlyStmt.
    def enterOnlyStmt(self, ctx:Fortran90Parser.OnlyStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#onlyStmt.
    def exitOnlyStmt(self, ctx:Fortran90Parser.OnlyStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#renameList.
    def enterRenameList(self, ctx:Fortran90Parser.RenameListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#renameList.
    def exitRenameList(self, ctx:Fortran90Parser.RenameListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rename.
    def enterRename(self, ctx:Fortran90Parser.RenameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rename.
    def exitRename(self, ctx:Fortran90Parser.RenameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#useName.
    def enterUseName(self, ctx:Fortran90Parser.UseNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#useName.
    def exitUseName(self, ctx:Fortran90Parser.UseNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#parameterStmt.
    def enterParameterStmt(self, ctx:Fortran90Parser.ParameterStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#parameterStmt.
    def exitParameterStmt(self, ctx:Fortran90Parser.ParameterStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namedConstantDefList.
    def enterNamedConstantDefList(self, ctx:Fortran90Parser.NamedConstantDefListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namedConstantDefList.
    def exitNamedConstantDefList(self, ctx:Fortran90Parser.NamedConstantDefListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namedConstantDef.
    def enterNamedConstantDef(self, ctx:Fortran90Parser.NamedConstantDefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namedConstantDef.
    def exitNamedConstantDef(self, ctx:Fortran90Parser.NamedConstantDefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endProgramStmt.
    def enterEndProgramStmt(self, ctx:Fortran90Parser.EndProgramStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endProgramStmt.
    def exitEndProgramStmt(self, ctx:Fortran90Parser.EndProgramStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#blockDataSubprogram.
    def enterBlockDataSubprogram(self, ctx:Fortran90Parser.BlockDataSubprogramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#blockDataSubprogram.
    def exitBlockDataSubprogram(self, ctx:Fortran90Parser.BlockDataSubprogramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#blockDataStmt.
    def enterBlockDataStmt(self, ctx:Fortran90Parser.BlockDataStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#blockDataStmt.
    def exitBlockDataStmt(self, ctx:Fortran90Parser.BlockDataStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#blockDataBody.
    def enterBlockDataBody(self, ctx:Fortran90Parser.BlockDataBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#blockDataBody.
    def exitBlockDataBody(self, ctx:Fortran90Parser.BlockDataBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#blockDataBodyConstruct.
    def enterBlockDataBodyConstruct(self, ctx:Fortran90Parser.BlockDataBodyConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#blockDataBodyConstruct.
    def exitBlockDataBodyConstruct(self, ctx:Fortran90Parser.BlockDataBodyConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endBlockDataStmt.
    def enterEndBlockDataStmt(self, ctx:Fortran90Parser.EndBlockDataStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endBlockDataStmt.
    def exitEndBlockDataStmt(self, ctx:Fortran90Parser.EndBlockDataStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#formatStmt.
    def enterFormatStmt(self, ctx:Fortran90Parser.FormatStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#formatStmt.
    def exitFormatStmt(self, ctx:Fortran90Parser.FormatStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#fmtSpec.
    def enterFmtSpec(self, ctx:Fortran90Parser.FmtSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#fmtSpec.
    def exitFmtSpec(self, ctx:Fortran90Parser.FmtSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#formatedit.
    def enterFormatedit(self, ctx:Fortran90Parser.FormateditContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#formatedit.
    def exitFormatedit(self, ctx:Fortran90Parser.FormateditContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#editElement.
    def enterEditElement(self, ctx:Fortran90Parser.EditElementContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#editElement.
    def exitEditElement(self, ctx:Fortran90Parser.EditElementContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#mislexedFcon.
    def enterMislexedFcon(self, ctx:Fortran90Parser.MislexedFconContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#mislexedFcon.
    def exitMislexedFcon(self, ctx:Fortran90Parser.MislexedFconContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#module.
    def enterModule(self, ctx:Fortran90Parser.ModuleContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#module.
    def exitModule(self, ctx:Fortran90Parser.ModuleContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endModuleStmt.
    def enterEndModuleStmt(self, ctx:Fortran90Parser.EndModuleStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endModuleStmt.
    def exitEndModuleStmt(self, ctx:Fortran90Parser.EndModuleStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#entryStmt.
    def enterEntryStmt(self, ctx:Fortran90Parser.EntryStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#entryStmt.
    def exitEntryStmt(self, ctx:Fortran90Parser.EntryStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineParList.
    def enterSubroutineParList(self, ctx:Fortran90Parser.SubroutineParListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineParList.
    def exitSubroutineParList(self, ctx:Fortran90Parser.SubroutineParListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutinePars.
    def enterSubroutinePars(self, ctx:Fortran90Parser.SubroutineParsContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutinePars.
    def exitSubroutinePars(self, ctx:Fortran90Parser.SubroutineParsContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutinePar.
    def enterSubroutinePar(self, ctx:Fortran90Parser.SubroutineParContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutinePar.
    def exitSubroutinePar(self, ctx:Fortran90Parser.SubroutineParContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#declarationConstruct.
    def enterDeclarationConstruct(self, ctx:Fortran90Parser.DeclarationConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#declarationConstruct.
    def exitDeclarationConstruct(self, ctx:Fortran90Parser.DeclarationConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#specificationStmt.
    def enterSpecificationStmt(self, ctx:Fortran90Parser.SpecificationStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#specificationStmt.
    def exitSpecificationStmt(self, ctx:Fortran90Parser.SpecificationStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#targetStmt.
    def enterTargetStmt(self, ctx:Fortran90Parser.TargetStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#targetStmt.
    def exitTargetStmt(self, ctx:Fortran90Parser.TargetStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#targetObjectList.
    def enterTargetObjectList(self, ctx:Fortran90Parser.TargetObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#targetObjectList.
    def exitTargetObjectList(self, ctx:Fortran90Parser.TargetObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#targetObject.
    def enterTargetObject(self, ctx:Fortran90Parser.TargetObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#targetObject.
    def exitTargetObject(self, ctx:Fortran90Parser.TargetObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerStmt.
    def enterPointerStmt(self, ctx:Fortran90Parser.PointerStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerStmt.
    def exitPointerStmt(self, ctx:Fortran90Parser.PointerStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerStmtObjectList.
    def enterPointerStmtObjectList(self, ctx:Fortran90Parser.PointerStmtObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerStmtObjectList.
    def exitPointerStmtObjectList(self, ctx:Fortran90Parser.PointerStmtObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerStmtObject.
    def enterPointerStmtObject(self, ctx:Fortran90Parser.PointerStmtObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerStmtObject.
    def exitPointerStmtObject(self, ctx:Fortran90Parser.PointerStmtObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#optionalStmt.
    def enterOptionalStmt(self, ctx:Fortran90Parser.OptionalStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#optionalStmt.
    def exitOptionalStmt(self, ctx:Fortran90Parser.OptionalStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#optionalParList.
    def enterOptionalParList(self, ctx:Fortran90Parser.OptionalParListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#optionalParList.
    def exitOptionalParList(self, ctx:Fortran90Parser.OptionalParListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#optionalPar.
    def enterOptionalPar(self, ctx:Fortran90Parser.OptionalParContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#optionalPar.
    def exitOptionalPar(self, ctx:Fortran90Parser.OptionalParContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namelistStmt.
    def enterNamelistStmt(self, ctx:Fortran90Parser.NamelistStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namelistStmt.
    def exitNamelistStmt(self, ctx:Fortran90Parser.NamelistStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namelistGroups.
    def enterNamelistGroups(self, ctx:Fortran90Parser.NamelistGroupsContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namelistGroups.
    def exitNamelistGroups(self, ctx:Fortran90Parser.NamelistGroupsContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namelistGroupName.
    def enterNamelistGroupName(self, ctx:Fortran90Parser.NamelistGroupNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namelistGroupName.
    def exitNamelistGroupName(self, ctx:Fortran90Parser.NamelistGroupNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namelistGroupObject.
    def enterNamelistGroupObject(self, ctx:Fortran90Parser.NamelistGroupObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namelistGroupObject.
    def exitNamelistGroupObject(self, ctx:Fortran90Parser.NamelistGroupObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intentStmt.
    def enterIntentStmt(self, ctx:Fortran90Parser.IntentStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intentStmt.
    def exitIntentStmt(self, ctx:Fortran90Parser.IntentStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intentParList.
    def enterIntentParList(self, ctx:Fortran90Parser.IntentParListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intentParList.
    def exitIntentParList(self, ctx:Fortran90Parser.IntentParListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intentPar.
    def enterIntentPar(self, ctx:Fortran90Parser.IntentParContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intentPar.
    def exitIntentPar(self, ctx:Fortran90Parser.IntentParContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dummyArgName.
    def enterDummyArgName(self, ctx:Fortran90Parser.DummyArgNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dummyArgName.
    def exitDummyArgName(self, ctx:Fortran90Parser.DummyArgNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intentSpec.
    def enterIntentSpec(self, ctx:Fortran90Parser.IntentSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intentSpec.
    def exitIntentSpec(self, ctx:Fortran90Parser.IntentSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocatableStmt.
    def enterAllocatableStmt(self, ctx:Fortran90Parser.AllocatableStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocatableStmt.
    def exitAllocatableStmt(self, ctx:Fortran90Parser.AllocatableStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayAllocationList.
    def enterArrayAllocationList(self, ctx:Fortran90Parser.ArrayAllocationListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayAllocationList.
    def exitArrayAllocationList(self, ctx:Fortran90Parser.ArrayAllocationListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayAllocation.
    def enterArrayAllocation(self, ctx:Fortran90Parser.ArrayAllocationContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayAllocation.
    def exitArrayAllocation(self, ctx:Fortran90Parser.ArrayAllocationContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayName.
    def enterArrayName(self, ctx:Fortran90Parser.ArrayNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayName.
    def exitArrayName(self, ctx:Fortran90Parser.ArrayNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#accessStmt.
    def enterAccessStmt(self, ctx:Fortran90Parser.AccessStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#accessStmt.
    def exitAccessStmt(self, ctx:Fortran90Parser.AccessStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#accessIdList.
    def enterAccessIdList(self, ctx:Fortran90Parser.AccessIdListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#accessIdList.
    def exitAccessIdList(self, ctx:Fortran90Parser.AccessIdListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#accessId.
    def enterAccessId(self, ctx:Fortran90Parser.AccessIdContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#accessId.
    def exitAccessId(self, ctx:Fortran90Parser.AccessIdContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#genericName.
    def enterGenericName(self, ctx:Fortran90Parser.GenericNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#genericName.
    def exitGenericName(self, ctx:Fortran90Parser.GenericNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#saveStmt.
    def enterSaveStmt(self, ctx:Fortran90Parser.SaveStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#saveStmt.
    def exitSaveStmt(self, ctx:Fortran90Parser.SaveStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#savedEntityList.
    def enterSavedEntityList(self, ctx:Fortran90Parser.SavedEntityListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#savedEntityList.
    def exitSavedEntityList(self, ctx:Fortran90Parser.SavedEntityListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#savedEntity.
    def enterSavedEntity(self, ctx:Fortran90Parser.SavedEntityContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#savedEntity.
    def exitSavedEntity(self, ctx:Fortran90Parser.SavedEntityContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#savedCommonBlock.
    def enterSavedCommonBlock(self, ctx:Fortran90Parser.SavedCommonBlockContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#savedCommonBlock.
    def exitSavedCommonBlock(self, ctx:Fortran90Parser.SavedCommonBlockContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intrinsicStmt.
    def enterIntrinsicStmt(self, ctx:Fortran90Parser.IntrinsicStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intrinsicStmt.
    def exitIntrinsicStmt(self, ctx:Fortran90Parser.IntrinsicStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intrinsicList.
    def enterIntrinsicList(self, ctx:Fortran90Parser.IntrinsicListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intrinsicList.
    def exitIntrinsicList(self, ctx:Fortran90Parser.IntrinsicListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#intrinsicProcedureName.
    def enterIntrinsicProcedureName(self, ctx:Fortran90Parser.IntrinsicProcedureNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#intrinsicProcedureName.
    def exitIntrinsicProcedureName(self, ctx:Fortran90Parser.IntrinsicProcedureNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#externalStmt.
    def enterExternalStmt(self, ctx:Fortran90Parser.ExternalStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#externalStmt.
    def exitExternalStmt(self, ctx:Fortran90Parser.ExternalStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#externalNameList.
    def enterExternalNameList(self, ctx:Fortran90Parser.ExternalNameListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#externalNameList.
    def exitExternalNameList(self, ctx:Fortran90Parser.ExternalNameListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#externalName.
    def enterExternalName(self, ctx:Fortran90Parser.ExternalNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#externalName.
    def exitExternalName(self, ctx:Fortran90Parser.ExternalNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivalenceStmt.
    def enterEquivalenceStmt(self, ctx:Fortran90Parser.EquivalenceStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivalenceStmt.
    def exitEquivalenceStmt(self, ctx:Fortran90Parser.EquivalenceStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivalenceSetList.
    def enterEquivalenceSetList(self, ctx:Fortran90Parser.EquivalenceSetListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivalenceSetList.
    def exitEquivalenceSetList(self, ctx:Fortran90Parser.EquivalenceSetListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivalenceSet.
    def enterEquivalenceSet(self, ctx:Fortran90Parser.EquivalenceSetContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivalenceSet.
    def exitEquivalenceSet(self, ctx:Fortran90Parser.EquivalenceSetContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivalenceObject.
    def enterEquivalenceObject(self, ctx:Fortran90Parser.EquivalenceObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivalenceObject.
    def exitEquivalenceObject(self, ctx:Fortran90Parser.EquivalenceObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivalenceObjectList.
    def enterEquivalenceObjectList(self, ctx:Fortran90Parser.EquivalenceObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivalenceObjectList.
    def exitEquivalenceObjectList(self, ctx:Fortran90Parser.EquivalenceObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dimensionStmt.
    def enterDimensionStmt(self, ctx:Fortran90Parser.DimensionStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dimensionStmt.
    def exitDimensionStmt(self, ctx:Fortran90Parser.DimensionStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayDeclaratorList.
    def enterArrayDeclaratorList(self, ctx:Fortran90Parser.ArrayDeclaratorListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayDeclaratorList.
    def exitArrayDeclaratorList(self, ctx:Fortran90Parser.ArrayDeclaratorListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commonStmt.
    def enterCommonStmt(self, ctx:Fortran90Parser.CommonStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commonStmt.
    def exitCommonStmt(self, ctx:Fortran90Parser.CommonStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#comlist.
    def enterComlist(self, ctx:Fortran90Parser.ComlistContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#comlist.
    def exitComlist(self, ctx:Fortran90Parser.ComlistContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commonBlockObject.
    def enterCommonBlockObject(self, ctx:Fortran90Parser.CommonBlockObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commonBlockObject.
    def exitCommonBlockObject(self, ctx:Fortran90Parser.CommonBlockObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayDeclarator.
    def enterArrayDeclarator(self, ctx:Fortran90Parser.ArrayDeclaratorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayDeclarator.
    def exitArrayDeclarator(self, ctx:Fortran90Parser.ArrayDeclaratorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#comblock.
    def enterComblock(self, ctx:Fortran90Parser.ComblockContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#comblock.
    def exitComblock(self, ctx:Fortran90Parser.ComblockContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commonBlockName.
    def enterCommonBlockName(self, ctx:Fortran90Parser.CommonBlockNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commonBlockName.
    def exitCommonBlockName(self, ctx:Fortran90Parser.CommonBlockNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#typeDeclarationStmt.
    def enterTypeDeclarationStmt(self, ctx:Fortran90Parser.TypeDeclarationStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#typeDeclarationStmt.
    def exitTypeDeclarationStmt(self, ctx:Fortran90Parser.TypeDeclarationStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#attrSpecSeq.
    def enterAttrSpecSeq(self, ctx:Fortran90Parser.AttrSpecSeqContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#attrSpecSeq.
    def exitAttrSpecSeq(self, ctx:Fortran90Parser.AttrSpecSeqContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#attrSpec.
    def enterAttrSpec(self, ctx:Fortran90Parser.AttrSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#attrSpec.
    def exitAttrSpec(self, ctx:Fortran90Parser.AttrSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#entityDeclList.
    def enterEntityDeclList(self, ctx:Fortran90Parser.EntityDeclListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#entityDeclList.
    def exitEntityDeclList(self, ctx:Fortran90Parser.EntityDeclListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#entityDecl.
    def enterEntityDecl(self, ctx:Fortran90Parser.EntityDeclContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#entityDecl.
    def exitEntityDecl(self, ctx:Fortran90Parser.EntityDeclContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#objectName.
    def enterObjectName(self, ctx:Fortran90Parser.ObjectNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#objectName.
    def exitObjectName(self, ctx:Fortran90Parser.ObjectNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arraySpec.
    def enterArraySpec(self, ctx:Fortran90Parser.ArraySpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arraySpec.
    def exitArraySpec(self, ctx:Fortran90Parser.ArraySpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assumedShapeSpecList.
    def enterAssumedShapeSpecList(self, ctx:Fortran90Parser.AssumedShapeSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assumedShapeSpecList.
    def exitAssumedShapeSpecList(self, ctx:Fortran90Parser.AssumedShapeSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assumedShapeSpec.
    def enterAssumedShapeSpec(self, ctx:Fortran90Parser.AssumedShapeSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assumedShapeSpec.
    def exitAssumedShapeSpec(self, ctx:Fortran90Parser.AssumedShapeSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assumedSizeSpec.
    def enterAssumedSizeSpec(self, ctx:Fortran90Parser.AssumedSizeSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assumedSizeSpec.
    def exitAssumedSizeSpec(self, ctx:Fortran90Parser.AssumedSizeSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#interfaceBlock.
    def enterInterfaceBlock(self, ctx:Fortran90Parser.InterfaceBlockContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#interfaceBlock.
    def exitInterfaceBlock(self, ctx:Fortran90Parser.InterfaceBlockContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endInterfaceStmt.
    def enterEndInterfaceStmt(self, ctx:Fortran90Parser.EndInterfaceStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endInterfaceStmt.
    def exitEndInterfaceStmt(self, ctx:Fortran90Parser.EndInterfaceStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#interfaceStmt.
    def enterInterfaceStmt(self, ctx:Fortran90Parser.InterfaceStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#interfaceStmt.
    def exitInterfaceStmt(self, ctx:Fortran90Parser.InterfaceStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#genericSpec.
    def enterGenericSpec(self, ctx:Fortran90Parser.GenericSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#genericSpec.
    def exitGenericSpec(self, ctx:Fortran90Parser.GenericSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#definedOperator.
    def enterDefinedOperator(self, ctx:Fortran90Parser.DefinedOperatorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#definedOperator.
    def exitDefinedOperator(self, ctx:Fortran90Parser.DefinedOperatorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#interfaceBlockBody.
    def enterInterfaceBlockBody(self, ctx:Fortran90Parser.InterfaceBlockBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#interfaceBlockBody.
    def exitInterfaceBlockBody(self, ctx:Fortran90Parser.InterfaceBlockBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#interfaceBodyPartConstruct.
    def enterInterfaceBodyPartConstruct(self, ctx:Fortran90Parser.InterfaceBodyPartConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#interfaceBodyPartConstruct.
    def exitInterfaceBodyPartConstruct(self, ctx:Fortran90Parser.InterfaceBodyPartConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#moduleProcedureStmt.
    def enterModuleProcedureStmt(self, ctx:Fortran90Parser.ModuleProcedureStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#moduleProcedureStmt.
    def exitModuleProcedureStmt(self, ctx:Fortran90Parser.ModuleProcedureStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#procedureNameList.
    def enterProcedureNameList(self, ctx:Fortran90Parser.ProcedureNameListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#procedureNameList.
    def exitProcedureNameList(self, ctx:Fortran90Parser.ProcedureNameListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#procedureName.
    def enterProcedureName(self, ctx:Fortran90Parser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#procedureName.
    def exitProcedureName(self, ctx:Fortran90Parser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#interfaceBody.
    def enterInterfaceBody(self, ctx:Fortran90Parser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#interfaceBody.
    def exitInterfaceBody(self, ctx:Fortran90Parser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineInterfaceRange.
    def enterSubroutineInterfaceRange(self, ctx:Fortran90Parser.SubroutineInterfaceRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineInterfaceRange.
    def exitSubroutineInterfaceRange(self, ctx:Fortran90Parser.SubroutineInterfaceRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endSubroutineStmt.
    def enterEndSubroutineStmt(self, ctx:Fortran90Parser.EndSubroutineStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endSubroutineStmt.
    def exitEndSubroutineStmt(self, ctx:Fortran90Parser.EndSubroutineStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#recursive.
    def enterRecursive(self, ctx:Fortran90Parser.RecursiveContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#recursive.
    def exitRecursive(self, ctx:Fortran90Parser.RecursiveContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionPrefixRec.
    def enterFunctionPrefixRec(self, ctx:Fortran90Parser.FunctionPrefixRecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionPrefixRec.
    def exitFunctionPrefixRec(self, ctx:Fortran90Parser.FunctionPrefixRecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionPrefixTyp.
    def enterFunctionPrefixTyp(self, ctx:Fortran90Parser.FunctionPrefixTypContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionPrefixTyp.
    def exitFunctionPrefixTyp(self, ctx:Fortran90Parser.FunctionPrefixTypContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionInterfaceRange.
    def enterFunctionInterfaceRange(self, ctx:Fortran90Parser.FunctionInterfaceRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionInterfaceRange.
    def exitFunctionInterfaceRange(self, ctx:Fortran90Parser.FunctionInterfaceRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionParList.
    def enterFunctionParList(self, ctx:Fortran90Parser.FunctionParListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionParList.
    def exitFunctionParList(self, ctx:Fortran90Parser.FunctionParListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionPars.
    def enterFunctionPars(self, ctx:Fortran90Parser.FunctionParsContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionPars.
    def exitFunctionPars(self, ctx:Fortran90Parser.FunctionParsContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionPar.
    def enterFunctionPar(self, ctx:Fortran90Parser.FunctionParContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionPar.
    def exitFunctionPar(self, ctx:Fortran90Parser.FunctionParContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subprogramInterfaceBody.
    def enterSubprogramInterfaceBody(self, ctx:Fortran90Parser.SubprogramInterfaceBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subprogramInterfaceBody.
    def exitSubprogramInterfaceBody(self, ctx:Fortran90Parser.SubprogramInterfaceBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endFunctionStmt.
    def enterEndFunctionStmt(self, ctx:Fortran90Parser.EndFunctionStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endFunctionStmt.
    def exitEndFunctionStmt(self, ctx:Fortran90Parser.EndFunctionStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#derivedTypeDef.
    def enterDerivedTypeDef(self, ctx:Fortran90Parser.DerivedTypeDefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#derivedTypeDef.
    def exitDerivedTypeDef(self, ctx:Fortran90Parser.DerivedTypeDefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endTypeStmt.
    def enterEndTypeStmt(self, ctx:Fortran90Parser.EndTypeStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endTypeStmt.
    def exitEndTypeStmt(self, ctx:Fortran90Parser.EndTypeStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#derivedTypeStmt.
    def enterDerivedTypeStmt(self, ctx:Fortran90Parser.DerivedTypeStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#derivedTypeStmt.
    def exitDerivedTypeStmt(self, ctx:Fortran90Parser.DerivedTypeStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#derivedTypeBody.
    def enterDerivedTypeBody(self, ctx:Fortran90Parser.DerivedTypeBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#derivedTypeBody.
    def exitDerivedTypeBody(self, ctx:Fortran90Parser.DerivedTypeBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#derivedTypeBodyConstruct.
    def enterDerivedTypeBodyConstruct(self, ctx:Fortran90Parser.DerivedTypeBodyConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#derivedTypeBodyConstruct.
    def exitDerivedTypeBodyConstruct(self, ctx:Fortran90Parser.DerivedTypeBodyConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#privateSequenceStmt.
    def enterPrivateSequenceStmt(self, ctx:Fortran90Parser.PrivateSequenceStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#privateSequenceStmt.
    def exitPrivateSequenceStmt(self, ctx:Fortran90Parser.PrivateSequenceStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentDefStmt.
    def enterComponentDefStmt(self, ctx:Fortran90Parser.ComponentDefStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentDefStmt.
    def exitComponentDefStmt(self, ctx:Fortran90Parser.ComponentDefStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentDeclList.
    def enterComponentDeclList(self, ctx:Fortran90Parser.ComponentDeclListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentDeclList.
    def exitComponentDeclList(self, ctx:Fortran90Parser.ComponentDeclListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentDecl.
    def enterComponentDecl(self, ctx:Fortran90Parser.ComponentDeclContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentDecl.
    def exitComponentDecl(self, ctx:Fortran90Parser.ComponentDeclContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentName.
    def enterComponentName(self, ctx:Fortran90Parser.ComponentNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentName.
    def exitComponentName(self, ctx:Fortran90Parser.ComponentNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentAttrSpecList.
    def enterComponentAttrSpecList(self, ctx:Fortran90Parser.ComponentAttrSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentAttrSpecList.
    def exitComponentAttrSpecList(self, ctx:Fortran90Parser.ComponentAttrSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentAttrSpec.
    def enterComponentAttrSpec(self, ctx:Fortran90Parser.ComponentAttrSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentAttrSpec.
    def exitComponentAttrSpec(self, ctx:Fortran90Parser.ComponentAttrSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#componentArraySpec.
    def enterComponentArraySpec(self, ctx:Fortran90Parser.ComponentArraySpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#componentArraySpec.
    def exitComponentArraySpec(self, ctx:Fortran90Parser.ComponentArraySpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#explicitShapeSpecList.
    def enterExplicitShapeSpecList(self, ctx:Fortran90Parser.ExplicitShapeSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#explicitShapeSpecList.
    def exitExplicitShapeSpecList(self, ctx:Fortran90Parser.ExplicitShapeSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#explicitShapeSpec.
    def enterExplicitShapeSpec(self, ctx:Fortran90Parser.ExplicitShapeSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#explicitShapeSpec.
    def exitExplicitShapeSpec(self, ctx:Fortran90Parser.ExplicitShapeSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#lowerBound.
    def enterLowerBound(self, ctx:Fortran90Parser.LowerBoundContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#lowerBound.
    def exitLowerBound(self, ctx:Fortran90Parser.LowerBoundContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#upperBound.
    def enterUpperBound(self, ctx:Fortran90Parser.UpperBoundContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#upperBound.
    def exitUpperBound(self, ctx:Fortran90Parser.UpperBoundContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#deferredShapeSpecList.
    def enterDeferredShapeSpecList(self, ctx:Fortran90Parser.DeferredShapeSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#deferredShapeSpecList.
    def exitDeferredShapeSpecList(self, ctx:Fortran90Parser.DeferredShapeSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#deferredShapeSpec.
    def enterDeferredShapeSpec(self, ctx:Fortran90Parser.DeferredShapeSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#deferredShapeSpec.
    def exitDeferredShapeSpec(self, ctx:Fortran90Parser.DeferredShapeSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#typeSpec.
    def enterTypeSpec(self, ctx:Fortran90Parser.TypeSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#typeSpec.
    def exitTypeSpec(self, ctx:Fortran90Parser.TypeSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#kindSelector.
    def enterKindSelector(self, ctx:Fortran90Parser.KindSelectorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#kindSelector.
    def exitKindSelector(self, ctx:Fortran90Parser.KindSelectorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#typeName.
    def enterTypeName(self, ctx:Fortran90Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#typeName.
    def exitTypeName(self, ctx:Fortran90Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#charSelector.
    def enterCharSelector(self, ctx:Fortran90Parser.CharSelectorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#charSelector.
    def exitCharSelector(self, ctx:Fortran90Parser.CharSelectorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#lengthSelector.
    def enterLengthSelector(self, ctx:Fortran90Parser.LengthSelectorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#lengthSelector.
    def exitLengthSelector(self, ctx:Fortran90Parser.LengthSelectorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#charLength.
    def enterCharLength(self, ctx:Fortran90Parser.CharLengthContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#charLength.
    def exitCharLength(self, ctx:Fortran90Parser.CharLengthContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#constant.
    def enterConstant(self, ctx:Fortran90Parser.ConstantContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#constant.
    def exitConstant(self, ctx:Fortran90Parser.ConstantContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#bozLiteralConstant.
    def enterBozLiteralConstant(self, ctx:Fortran90Parser.BozLiteralConstantContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#bozLiteralConstant.
    def exitBozLiteralConstant(self, ctx:Fortran90Parser.BozLiteralConstantContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#structureConstructor.
    def enterStructureConstructor(self, ctx:Fortran90Parser.StructureConstructorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#structureConstructor.
    def exitStructureConstructor(self, ctx:Fortran90Parser.StructureConstructorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#exprList.
    def enterExprList(self, ctx:Fortran90Parser.ExprListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#exprList.
    def exitExprList(self, ctx:Fortran90Parser.ExprListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#namedConstantUse.
    def enterNamedConstantUse(self, ctx:Fortran90Parser.NamedConstantUseContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#namedConstantUse.
    def exitNamedConstantUse(self, ctx:Fortran90Parser.NamedConstantUseContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#typeParamValue.
    def enterTypeParamValue(self, ctx:Fortran90Parser.TypeParamValueContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#typeParamValue.
    def exitTypeParamValue(self, ctx:Fortran90Parser.TypeParamValueContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#moduleStmt.
    def enterModuleStmt(self, ctx:Fortran90Parser.ModuleStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#moduleStmt.
    def exitModuleStmt(self, ctx:Fortran90Parser.ModuleStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#moduleName.
    def enterModuleName(self, ctx:Fortran90Parser.ModuleNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#moduleName.
    def exitModuleName(self, ctx:Fortran90Parser.ModuleNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ident.
    def enterIdent(self, ctx:Fortran90Parser.IdentContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ident.
    def exitIdent(self, ctx:Fortran90Parser.IdentContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#complexSubmodule.
    def enterComplexSubmodule(self, ctx:Fortran90Parser.ComplexSubmoduleContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#complexSubmodule.
    def exitComplexSubmodule(self, ctx:Fortran90Parser.ComplexSubmoduleContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#complexSpecPart.
    def enterComplexSpecPart(self, ctx:Fortran90Parser.ComplexSpecPartContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#complexSpecPart.
    def exitComplexSpecPart(self, ctx:Fortran90Parser.ComplexSpecPartContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#submoduleStmt.
    def enterSubmoduleStmt(self, ctx:Fortran90Parser.SubmoduleStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#submoduleStmt.
    def exitSubmoduleStmt(self, ctx:Fortran90Parser.SubmoduleStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#specPartStmt.
    def enterSpecPartStmt(self, ctx:Fortran90Parser.SpecPartStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#specPartStmt.
    def exitSpecPartStmt(self, ctx:Fortran90Parser.SpecPartStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#moduleSubprogramPartConstruct.
    def enterModuleSubprogramPartConstruct(self, ctx:Fortran90Parser.ModuleSubprogramPartConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#moduleSubprogramPartConstruct.
    def exitModuleSubprogramPartConstruct(self, ctx:Fortran90Parser.ModuleSubprogramPartConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#containsStmt.
    def enterContainsStmt(self, ctx:Fortran90Parser.ContainsStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#containsStmt.
    def exitContainsStmt(self, ctx:Fortran90Parser.ContainsStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#moduleSubprogram.
    def enterModuleSubprogram(self, ctx:Fortran90Parser.ModuleSubprogramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#moduleSubprogram.
    def exitModuleSubprogram(self, ctx:Fortran90Parser.ModuleSubprogramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionSubprogram.
    def enterFunctionSubprogram(self, ctx:Fortran90Parser.FunctionSubprogramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionSubprogram.
    def exitFunctionSubprogram(self, ctx:Fortran90Parser.FunctionSubprogramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionName.
    def enterFunctionName(self, ctx:Fortran90Parser.FunctionNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionName.
    def exitFunctionName(self, ctx:Fortran90Parser.FunctionNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionRange.
    def enterFunctionRange(self, ctx:Fortran90Parser.FunctionRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionRange.
    def exitFunctionRange(self, ctx:Fortran90Parser.FunctionRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#body.
    def enterBody(self, ctx:Fortran90Parser.BodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#body.
    def exitBody(self, ctx:Fortran90Parser.BodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#bodyConstruct.
    def enterBodyConstruct(self, ctx:Fortran90Parser.BodyConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#bodyConstruct.
    def exitBodyConstruct(self, ctx:Fortran90Parser.BodyConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#executableConstruct.
    def enterExecutableConstruct(self, ctx:Fortran90Parser.ExecutableConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#executableConstruct.
    def exitExecutableConstruct(self, ctx:Fortran90Parser.ExecutableConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#whereConstruct.
    def enterWhereConstruct(self, ctx:Fortran90Parser.WhereConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#whereConstruct.
    def exitWhereConstruct(self, ctx:Fortran90Parser.WhereConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elseWhere.
    def enterElseWhere(self, ctx:Fortran90Parser.ElseWhereContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elseWhere.
    def exitElseWhere(self, ctx:Fortran90Parser.ElseWhereContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elsewhereStmt.
    def enterElsewhereStmt(self, ctx:Fortran90Parser.ElsewhereStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elsewhereStmt.
    def exitElsewhereStmt(self, ctx:Fortran90Parser.ElsewhereStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endWhereStmt.
    def enterEndWhereStmt(self, ctx:Fortran90Parser.EndWhereStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endWhereStmt.
    def exitEndWhereStmt(self, ctx:Fortran90Parser.EndWhereStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#where.
    def enterWhere(self, ctx:Fortran90Parser.WhereContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#where.
    def exitWhere(self, ctx:Fortran90Parser.WhereContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#whereConstructStmt.
    def enterWhereConstructStmt(self, ctx:Fortran90Parser.WhereConstructStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#whereConstructStmt.
    def exitWhereConstructStmt(self, ctx:Fortran90Parser.WhereConstructStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#maskExpr.
    def enterMaskExpr(self, ctx:Fortran90Parser.MaskExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#maskExpr.
    def exitMaskExpr(self, ctx:Fortran90Parser.MaskExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#caseConstruct.
    def enterCaseConstruct(self, ctx:Fortran90Parser.CaseConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#caseConstruct.
    def exitCaseConstruct(self, ctx:Fortran90Parser.CaseConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#selectCaseRange.
    def enterSelectCaseRange(self, ctx:Fortran90Parser.SelectCaseRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#selectCaseRange.
    def exitSelectCaseRange(self, ctx:Fortran90Parser.SelectCaseRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endSelectStmt.
    def enterEndSelectStmt(self, ctx:Fortran90Parser.EndSelectStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endSelectStmt.
    def exitEndSelectStmt(self, ctx:Fortran90Parser.EndSelectStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#selectCaseBody.
    def enterSelectCaseBody(self, ctx:Fortran90Parser.SelectCaseBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#selectCaseBody.
    def exitSelectCaseBody(self, ctx:Fortran90Parser.SelectCaseBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#caseBodyConstruct.
    def enterCaseBodyConstruct(self, ctx:Fortran90Parser.CaseBodyConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#caseBodyConstruct.
    def exitCaseBodyConstruct(self, ctx:Fortran90Parser.CaseBodyConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#caseStmt.
    def enterCaseStmt(self, ctx:Fortran90Parser.CaseStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#caseStmt.
    def exitCaseStmt(self, ctx:Fortran90Parser.CaseStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#caseSelector.
    def enterCaseSelector(self, ctx:Fortran90Parser.CaseSelectorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#caseSelector.
    def exitCaseSelector(self, ctx:Fortran90Parser.CaseSelectorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#caseValueRangeList.
    def enterCaseValueRangeList(self, ctx:Fortran90Parser.CaseValueRangeListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#caseValueRangeList.
    def exitCaseValueRangeList(self, ctx:Fortran90Parser.CaseValueRangeListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#litteralExpression.
    def enterLitteralExpression(self, ctx:Fortran90Parser.LitteralExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#litteralExpression.
    def exitLitteralExpression(self, ctx:Fortran90Parser.LitteralExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#afterColonExpression.
    def enterAfterColonExpression(self, ctx:Fortran90Parser.AfterColonExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#afterColonExpression.
    def exitAfterColonExpression(self, ctx:Fortran90Parser.AfterColonExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#beforeColonExpression.
    def enterBeforeColonExpression(self, ctx:Fortran90Parser.BeforeColonExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#beforeColonExpression.
    def exitBeforeColonExpression(self, ctx:Fortran90Parser.BeforeColonExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#midlleColonExpression.
    def enterMidlleColonExpression(self, ctx:Fortran90Parser.MidlleColonExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#midlleColonExpression.
    def exitMidlleColonExpression(self, ctx:Fortran90Parser.MidlleColonExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ifConstruct.
    def enterIfConstruct(self, ctx:Fortran90Parser.IfConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ifConstruct.
    def exitIfConstruct(self, ctx:Fortran90Parser.IfConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ifThenStmt.
    def enterIfThenStmt(self, ctx:Fortran90Parser.IfThenStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ifThenStmt.
    def exitIfThenStmt(self, ctx:Fortran90Parser.IfThenStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#conditionalBody.
    def enterConditionalBody(self, ctx:Fortran90Parser.ConditionalBodyContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#conditionalBody.
    def exitConditionalBody(self, ctx:Fortran90Parser.ConditionalBodyContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elseIfConstruct.
    def enterElseIfConstruct(self, ctx:Fortran90Parser.ElseIfConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elseIfConstruct.
    def exitElseIfConstruct(self, ctx:Fortran90Parser.ElseIfConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elseIfStmt.
    def enterElseIfStmt(self, ctx:Fortran90Parser.ElseIfStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elseIfStmt.
    def exitElseIfStmt(self, ctx:Fortran90Parser.ElseIfStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elseConstruct.
    def enterElseConstruct(self, ctx:Fortran90Parser.ElseConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elseConstruct.
    def exitElseConstruct(self, ctx:Fortran90Parser.ElseConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#elseStmt.
    def enterElseStmt(self, ctx:Fortran90Parser.ElseStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#elseStmt.
    def exitElseStmt(self, ctx:Fortran90Parser.ElseStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endIfStmt.
    def enterEndIfStmt(self, ctx:Fortran90Parser.EndIfStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endIfStmt.
    def exitEndIfStmt(self, ctx:Fortran90Parser.EndIfStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#doConstruct.
    def enterDoConstruct(self, ctx:Fortran90Parser.DoConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#doConstruct.
    def exitDoConstruct(self, ctx:Fortran90Parser.DoConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#blockDoConstruct.
    def enterBlockDoConstruct(self, ctx:Fortran90Parser.BlockDoConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#blockDoConstruct.
    def exitBlockDoConstruct(self, ctx:Fortran90Parser.BlockDoConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endDoStmt.
    def enterEndDoStmt(self, ctx:Fortran90Parser.EndDoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endDoStmt.
    def exitEndDoStmt(self, ctx:Fortran90Parser.EndDoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endName.
    def enterEndName(self, ctx:Fortran90Parser.EndNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endName.
    def exitEndName(self, ctx:Fortran90Parser.EndNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#nameColon.
    def enterNameColon(self, ctx:Fortran90Parser.NameColonContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#nameColon.
    def exitNameColon(self, ctx:Fortran90Parser.NameColonContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#labelDoStmt.
    def enterLabelDoStmt(self, ctx:Fortran90Parser.LabelDoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#labelDoStmt.
    def exitLabelDoStmt(self, ctx:Fortran90Parser.LabelDoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#doLblRef.
    def enterDoLblRef(self, ctx:Fortran90Parser.DoLblRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#doLblRef.
    def exitDoLblRef(self, ctx:Fortran90Parser.DoLblRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#doLblDef.
    def enterDoLblDef(self, ctx:Fortran90Parser.DoLblDefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#doLblDef.
    def exitDoLblDef(self, ctx:Fortran90Parser.DoLblDefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#doLabelStmt.
    def enterDoLabelStmt(self, ctx:Fortran90Parser.DoLabelStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#doLabelStmt.
    def exitDoLabelStmt(self, ctx:Fortran90Parser.DoLabelStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#executionPartConstruct.
    def enterExecutionPartConstruct(self, ctx:Fortran90Parser.ExecutionPartConstructContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#executionPartConstruct.
    def exitExecutionPartConstruct(self, ctx:Fortran90Parser.ExecutionPartConstructContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#doubleDoStmt.
    def enterDoubleDoStmt(self, ctx:Fortran90Parser.DoubleDoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#doubleDoStmt.
    def exitDoubleDoStmt(self, ctx:Fortran90Parser.DoubleDoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataStmt.
    def enterDataStmt(self, ctx:Fortran90Parser.DataStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataStmt.
    def exitDataStmt(self, ctx:Fortran90Parser.DataStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataStmtSet.
    def enterDataStmtSet(self, ctx:Fortran90Parser.DataStmtSetContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataStmtSet.
    def exitDataStmtSet(self, ctx:Fortran90Parser.DataStmtSetContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dse1.
    def enterDse1(self, ctx:Fortran90Parser.Dse1Context):
        pass

    # Exit a parse tree produced by Fortran90Parser#dse1.
    def exitDse1(self, ctx:Fortran90Parser.Dse1Context):
        pass


    # Enter a parse tree produced by Fortran90Parser#dse2.
    def enterDse2(self, ctx:Fortran90Parser.Dse2Context):
        pass

    # Exit a parse tree produced by Fortran90Parser#dse2.
    def exitDse2(self, ctx:Fortran90Parser.Dse2Context):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataStmtValue.
    def enterDataStmtValue(self, ctx:Fortran90Parser.DataStmtValueContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataStmtValue.
    def exitDataStmtValue(self, ctx:Fortran90Parser.DataStmtValueContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataStmtObject.
    def enterDataStmtObject(self, ctx:Fortran90Parser.DataStmtObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataStmtObject.
    def exitDataStmtObject(self, ctx:Fortran90Parser.DataStmtObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#variable.
    def enterVariable(self, ctx:Fortran90Parser.VariableContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#variable.
    def exitVariable(self, ctx:Fortran90Parser.VariableContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subscriptListRef.
    def enterSubscriptListRef(self, ctx:Fortran90Parser.SubscriptListRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subscriptListRef.
    def exitSubscriptListRef(self, ctx:Fortran90Parser.SubscriptListRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subscriptList.
    def enterSubscriptList(self, ctx:Fortran90Parser.SubscriptListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subscriptList.
    def exitSubscriptList(self, ctx:Fortran90Parser.SubscriptListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subscript.
    def enterSubscript(self, ctx:Fortran90Parser.SubscriptContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subscript.
    def exitSubscript(self, ctx:Fortran90Parser.SubscriptContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#substringRange.
    def enterSubstringRange(self, ctx:Fortran90Parser.SubstringRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#substringRange.
    def exitSubstringRange(self, ctx:Fortran90Parser.SubstringRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataImpliedDo.
    def enterDataImpliedDo(self, ctx:Fortran90Parser.DataImpliedDoContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataImpliedDo.
    def exitDataImpliedDo(self, ctx:Fortran90Parser.DataImpliedDoContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataIDoObjectList.
    def enterDataIDoObjectList(self, ctx:Fortran90Parser.DataIDoObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataIDoObjectList.
    def exitDataIDoObjectList(self, ctx:Fortran90Parser.DataIDoObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#dataIDoObject.
    def enterDataIDoObject(self, ctx:Fortran90Parser.DataIDoObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#dataIDoObject.
    def exitDataIDoObject(self, ctx:Fortran90Parser.DataIDoObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#structureComponent.
    def enterStructureComponent(self, ctx:Fortran90Parser.StructureComponentContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#structureComponent.
    def exitStructureComponent(self, ctx:Fortran90Parser.StructureComponentContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#fieldSelector.
    def enterFieldSelector(self, ctx:Fortran90Parser.FieldSelectorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#fieldSelector.
    def exitFieldSelector(self, ctx:Fortran90Parser.FieldSelectorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayElement.
    def enterArrayElement(self, ctx:Fortran90Parser.ArrayElementContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayElement.
    def exitArrayElement(self, ctx:Fortran90Parser.ArrayElementContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#impliedDoVariable.
    def enterImpliedDoVariable(self, ctx:Fortran90Parser.ImpliedDoVariableContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#impliedDoVariable.
    def exitImpliedDoVariable(self, ctx:Fortran90Parser.ImpliedDoVariableContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commaLoopControl.
    def enterCommaLoopControl(self, ctx:Fortran90Parser.CommaLoopControlContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commaLoopControl.
    def exitCommaLoopControl(self, ctx:Fortran90Parser.CommaLoopControlContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#loopControl.
    def enterLoopControl(self, ctx:Fortran90Parser.LoopControlContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#loopControl.
    def exitLoopControl(self, ctx:Fortran90Parser.LoopControlContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#variableName.
    def enterVariableName(self, ctx:Fortran90Parser.VariableNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#variableName.
    def exitVariableName(self, ctx:Fortran90Parser.VariableNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commaExpr.
    def enterCommaExpr(self, ctx:Fortran90Parser.CommaExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commaExpr.
    def exitCommaExpr(self, ctx:Fortran90Parser.CommaExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#actionStmt.
    def enterActionStmt(self, ctx:Fortran90Parser.ActionStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#actionStmt.
    def exitActionStmt(self, ctx:Fortran90Parser.ActionStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#whereStmt.
    def enterWhereStmt(self, ctx:Fortran90Parser.WhereStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#whereStmt.
    def exitWhereStmt(self, ctx:Fortran90Parser.WhereStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerAssignmentStmt.
    def enterPointerAssignmentStmt(self, ctx:Fortran90Parser.PointerAssignmentStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerAssignmentStmt.
    def exitPointerAssignmentStmt(self, ctx:Fortran90Parser.PointerAssignmentStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#target.
    def enterTarget(self, ctx:Fortran90Parser.TargetContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#target.
    def exitTarget(self, ctx:Fortran90Parser.TargetContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#nullifyStmt.
    def enterNullifyStmt(self, ctx:Fortran90Parser.NullifyStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#nullifyStmt.
    def exitNullifyStmt(self, ctx:Fortran90Parser.NullifyStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerObjectList.
    def enterPointerObjectList(self, ctx:Fortran90Parser.PointerObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerObjectList.
    def exitPointerObjectList(self, ctx:Fortran90Parser.PointerObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerObject.
    def enterPointerObject(self, ctx:Fortran90Parser.PointerObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerObject.
    def exitPointerObject(self, ctx:Fortran90Parser.PointerObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pointerField.
    def enterPointerField(self, ctx:Fortran90Parser.PointerFieldContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pointerField.
    def exitPointerField(self, ctx:Fortran90Parser.PointerFieldContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#exitStmt.
    def enterExitStmt(self, ctx:Fortran90Parser.ExitStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#exitStmt.
    def exitExitStmt(self, ctx:Fortran90Parser.ExitStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#deallocateStmt.
    def enterDeallocateStmt(self, ctx:Fortran90Parser.DeallocateStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#deallocateStmt.
    def exitDeallocateStmt(self, ctx:Fortran90Parser.DeallocateStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocateObjectList.
    def enterAllocateObjectList(self, ctx:Fortran90Parser.AllocateObjectListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocateObjectList.
    def exitAllocateObjectList(self, ctx:Fortran90Parser.AllocateObjectListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#cycleStmt.
    def enterCycleStmt(self, ctx:Fortran90Parser.CycleStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#cycleStmt.
    def exitCycleStmt(self, ctx:Fortran90Parser.CycleStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocateStmt.
    def enterAllocateStmt(self, ctx:Fortran90Parser.AllocateStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocateStmt.
    def exitAllocateStmt(self, ctx:Fortran90Parser.AllocateStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocationList.
    def enterAllocationList(self, ctx:Fortran90Parser.AllocationListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocationList.
    def exitAllocationList(self, ctx:Fortran90Parser.AllocationListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocation.
    def enterAllocation(self, ctx:Fortran90Parser.AllocationContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocation.
    def exitAllocation(self, ctx:Fortran90Parser.AllocationContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocateObject.
    def enterAllocateObject(self, ctx:Fortran90Parser.AllocateObjectContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocateObject.
    def exitAllocateObject(self, ctx:Fortran90Parser.AllocateObjectContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#allocatedShape.
    def enterAllocatedShape(self, ctx:Fortran90Parser.AllocatedShapeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#allocatedShape.
    def exitAllocatedShape(self, ctx:Fortran90Parser.AllocatedShapeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#stopStmt.
    def enterStopStmt(self, ctx:Fortran90Parser.StopStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#stopStmt.
    def exitStopStmt(self, ctx:Fortran90Parser.StopStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#writeStmt.
    def enterWriteStmt(self, ctx:Fortran90Parser.WriteStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#writeStmt.
    def exitWriteStmt(self, ctx:Fortran90Parser.WriteStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ioControlSpecList.
    def enterIoControlSpecList(self, ctx:Fortran90Parser.IoControlSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ioControlSpecList.
    def exitIoControlSpecList(self, ctx:Fortran90Parser.IoControlSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#stmtFunctionStmt.
    def enterStmtFunctionStmt(self, ctx:Fortran90Parser.StmtFunctionStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#stmtFunctionStmt.
    def exitStmtFunctionStmt(self, ctx:Fortran90Parser.StmtFunctionStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#stmtFunctionRange.
    def enterStmtFunctionRange(self, ctx:Fortran90Parser.StmtFunctionRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#stmtFunctionRange.
    def exitStmtFunctionRange(self, ctx:Fortran90Parser.StmtFunctionRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sFDummyArgNameList.
    def enterSFDummyArgNameList(self, ctx:Fortran90Parser.SFDummyArgNameListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sFDummyArgNameList.
    def exitSFDummyArgNameList(self, ctx:Fortran90Parser.SFDummyArgNameListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sFDummyArgName.
    def enterSFDummyArgName(self, ctx:Fortran90Parser.SFDummyArgNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sFDummyArgName.
    def exitSFDummyArgName(self, ctx:Fortran90Parser.SFDummyArgNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#returnStmt.
    def enterReturnStmt(self, ctx:Fortran90Parser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#returnStmt.
    def exitReturnStmt(self, ctx:Fortran90Parser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rewindStmt.
    def enterRewindStmt(self, ctx:Fortran90Parser.RewindStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rewindStmt.
    def exitRewindStmt(self, ctx:Fortran90Parser.RewindStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#readStmt.
    def enterReadStmt(self, ctx:Fortran90Parser.ReadStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#readStmt.
    def exitReadStmt(self, ctx:Fortran90Parser.ReadStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commaInputItemList.
    def enterCommaInputItemList(self, ctx:Fortran90Parser.CommaInputItemListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commaInputItemList.
    def exitCommaInputItemList(self, ctx:Fortran90Parser.CommaInputItemListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rdFmtId.
    def enterRdFmtId(self, ctx:Fortran90Parser.RdFmtIdContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rdFmtId.
    def exitRdFmtId(self, ctx:Fortran90Parser.RdFmtIdContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rdFmtIdExpr.
    def enterRdFmtIdExpr(self, ctx:Fortran90Parser.RdFmtIdExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rdFmtIdExpr.
    def exitRdFmtIdExpr(self, ctx:Fortran90Parser.RdFmtIdExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inputItemList.
    def enterInputItemList(self, ctx:Fortran90Parser.InputItemListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inputItemList.
    def exitInputItemList(self, ctx:Fortran90Parser.InputItemListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inputItem.
    def enterInputItem(self, ctx:Fortran90Parser.InputItemContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inputItem.
    def exitInputItem(self, ctx:Fortran90Parser.InputItemContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inputImpliedDo.
    def enterInputImpliedDo(self, ctx:Fortran90Parser.InputImpliedDoContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inputImpliedDo.
    def exitInputImpliedDo(self, ctx:Fortran90Parser.InputImpliedDoContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rdCtlSpec.
    def enterRdCtlSpec(self, ctx:Fortran90Parser.RdCtlSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rdCtlSpec.
    def exitRdCtlSpec(self, ctx:Fortran90Parser.RdCtlSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rdUnitId.
    def enterRdUnitId(self, ctx:Fortran90Parser.RdUnitIdContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rdUnitId.
    def exitRdUnitId(self, ctx:Fortran90Parser.RdUnitIdContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#rdIoCtlSpecList.
    def enterRdIoCtlSpecList(self, ctx:Fortran90Parser.RdIoCtlSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#rdIoCtlSpecList.
    def exitRdIoCtlSpecList(self, ctx:Fortran90Parser.RdIoCtlSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ioControlSpec.
    def enterIoControlSpec(self, ctx:Fortran90Parser.IoControlSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ioControlSpec.
    def exitIoControlSpec(self, ctx:Fortran90Parser.IoControlSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#printStmt.
    def enterPrintStmt(self, ctx:Fortran90Parser.PrintStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#printStmt.
    def exitPrintStmt(self, ctx:Fortran90Parser.PrintStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#outputItemList.
    def enterOutputItemList(self, ctx:Fortran90Parser.OutputItemListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#outputItemList.
    def exitOutputItemList(self, ctx:Fortran90Parser.OutputItemListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#outputItemList1.
    def enterOutputItemList1(self, ctx:Fortran90Parser.OutputItemList1Context):
        pass

    # Exit a parse tree produced by Fortran90Parser#outputItemList1.
    def exitOutputItemList1(self, ctx:Fortran90Parser.OutputItemList1Context):
        pass


    # Enter a parse tree produced by Fortran90Parser#outputImpliedDo.
    def enterOutputImpliedDo(self, ctx:Fortran90Parser.OutputImpliedDoContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#outputImpliedDo.
    def exitOutputImpliedDo(self, ctx:Fortran90Parser.OutputImpliedDoContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#formatIdentifier.
    def enterFormatIdentifier(self, ctx:Fortran90Parser.FormatIdentifierContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#formatIdentifier.
    def exitFormatIdentifier(self, ctx:Fortran90Parser.FormatIdentifierContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#pauseStmt.
    def enterPauseStmt(self, ctx:Fortran90Parser.PauseStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#pauseStmt.
    def exitPauseStmt(self, ctx:Fortran90Parser.PauseStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#openStmt.
    def enterOpenStmt(self, ctx:Fortran90Parser.OpenStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#openStmt.
    def exitOpenStmt(self, ctx:Fortran90Parser.OpenStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#connectSpecList.
    def enterConnectSpecList(self, ctx:Fortran90Parser.ConnectSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#connectSpecList.
    def exitConnectSpecList(self, ctx:Fortran90Parser.ConnectSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#connectSpec.
    def enterConnectSpec(self, ctx:Fortran90Parser.ConnectSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#connectSpec.
    def exitConnectSpec(self, ctx:Fortran90Parser.ConnectSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inquireStmt.
    def enterInquireStmt(self, ctx:Fortran90Parser.InquireStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inquireStmt.
    def exitInquireStmt(self, ctx:Fortran90Parser.InquireStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inquireSpecList.
    def enterInquireSpecList(self, ctx:Fortran90Parser.InquireSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inquireSpecList.
    def exitInquireSpecList(self, ctx:Fortran90Parser.InquireSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#inquireSpec.
    def enterInquireSpec(self, ctx:Fortran90Parser.InquireSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#inquireSpec.
    def exitInquireSpec(self, ctx:Fortran90Parser.InquireSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assignedGotoStmt.
    def enterAssignedGotoStmt(self, ctx:Fortran90Parser.AssignedGotoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assignedGotoStmt.
    def exitAssignedGotoStmt(self, ctx:Fortran90Parser.AssignedGotoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#variableComma.
    def enterVariableComma(self, ctx:Fortran90Parser.VariableCommaContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#variableComma.
    def exitVariableComma(self, ctx:Fortran90Parser.VariableCommaContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#gotoStmt.
    def enterGotoStmt(self, ctx:Fortran90Parser.GotoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#gotoStmt.
    def exitGotoStmt(self, ctx:Fortran90Parser.GotoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#computedGotoStmt.
    def enterComputedGotoStmt(self, ctx:Fortran90Parser.ComputedGotoStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#computedGotoStmt.
    def exitComputedGotoStmt(self, ctx:Fortran90Parser.ComputedGotoStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#lblRefList.
    def enterLblRefList(self, ctx:Fortran90Parser.LblRefListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#lblRefList.
    def exitLblRefList(self, ctx:Fortran90Parser.LblRefListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#endfileStmt.
    def enterEndfileStmt(self, ctx:Fortran90Parser.EndfileStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#endfileStmt.
    def exitEndfileStmt(self, ctx:Fortran90Parser.EndfileStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#continueStmt.
    def enterContinueStmt(self, ctx:Fortran90Parser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#continueStmt.
    def exitContinueStmt(self, ctx:Fortran90Parser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#closeStmt.
    def enterCloseStmt(self, ctx:Fortran90Parser.CloseStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#closeStmt.
    def exitCloseStmt(self, ctx:Fortran90Parser.CloseStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#closeSpecList.
    def enterCloseSpecList(self, ctx:Fortran90Parser.CloseSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#closeSpecList.
    def exitCloseSpecList(self, ctx:Fortran90Parser.CloseSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#closeSpec.
    def enterCloseSpec(self, ctx:Fortran90Parser.CloseSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#closeSpec.
    def exitCloseSpec(self, ctx:Fortran90Parser.CloseSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#cExpression.
    def enterCExpression(self, ctx:Fortran90Parser.CExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#cExpression.
    def exitCExpression(self, ctx:Fortran90Parser.CExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#cPrimary.
    def enterCPrimary(self, ctx:Fortran90Parser.CPrimaryContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#cPrimary.
    def exitCPrimary(self, ctx:Fortran90Parser.CPrimaryContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#cOperand.
    def enterCOperand(self, ctx:Fortran90Parser.COperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#cOperand.
    def exitCOperand(self, ctx:Fortran90Parser.COperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#cPrimaryConcatOp.
    def enterCPrimaryConcatOp(self, ctx:Fortran90Parser.CPrimaryConcatOpContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#cPrimaryConcatOp.
    def exitCPrimaryConcatOp(self, ctx:Fortran90Parser.CPrimaryConcatOpContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#callStmt.
    def enterCallStmt(self, ctx:Fortran90Parser.CallStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#callStmt.
    def exitCallStmt(self, ctx:Fortran90Parser.CallStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineNameUse.
    def enterSubroutineNameUse(self, ctx:Fortran90Parser.SubroutineNameUseContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineNameUse.
    def exitSubroutineNameUse(self, ctx:Fortran90Parser.SubroutineNameUseContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineArgList.
    def enterSubroutineArgList(self, ctx:Fortran90Parser.SubroutineArgListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineArgList.
    def exitSubroutineArgList(self, ctx:Fortran90Parser.SubroutineArgListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineArg.
    def enterSubroutineArg(self, ctx:Fortran90Parser.SubroutineArgContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineArg.
    def exitSubroutineArg(self, ctx:Fortran90Parser.SubroutineArgContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arithmeticIfStmt.
    def enterArithmeticIfStmt(self, ctx:Fortran90Parser.ArithmeticIfStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arithmeticIfStmt.
    def exitArithmeticIfStmt(self, ctx:Fortran90Parser.ArithmeticIfStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#lblRef.
    def enterLblRef(self, ctx:Fortran90Parser.LblRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#lblRef.
    def exitLblRef(self, ctx:Fortran90Parser.LblRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#label.
    def enterLabel(self, ctx:Fortran90Parser.LabelContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#label.
    def exitLabel(self, ctx:Fortran90Parser.LabelContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assignmentStmt.
    def enterAssignmentStmt(self, ctx:Fortran90Parser.AssignmentStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assignmentStmt.
    def exitAssignmentStmt(self, ctx:Fortran90Parser.AssignmentStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sFExprListRef.
    def enterSFExprListRef(self, ctx:Fortran90Parser.SFExprListRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sFExprListRef.
    def exitSFExprListRef(self, ctx:Fortran90Parser.SFExprListRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sFExprList.
    def enterSFExprList(self, ctx:Fortran90Parser.SFExprListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sFExprList.
    def exitSFExprList(self, ctx:Fortran90Parser.SFExprListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#commaSectionSubscript.
    def enterCommaSectionSubscript(self, ctx:Fortran90Parser.CommaSectionSubscriptContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#commaSectionSubscript.
    def exitCommaSectionSubscript(self, ctx:Fortran90Parser.CommaSectionSubscriptContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#assignStmt.
    def enterAssignStmt(self, ctx:Fortran90Parser.AssignStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#assignStmt.
    def exitAssignStmt(self, ctx:Fortran90Parser.AssignStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#backspaceStmt.
    def enterBackspaceStmt(self, ctx:Fortran90Parser.BackspaceStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#backspaceStmt.
    def exitBackspaceStmt(self, ctx:Fortran90Parser.BackspaceStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#unitIdentifier.
    def enterUnitIdentifier(self, ctx:Fortran90Parser.UnitIdentifierContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#unitIdentifier.
    def exitUnitIdentifier(self, ctx:Fortran90Parser.UnitIdentifierContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#positionSpecList.
    def enterPositionSpecList(self, ctx:Fortran90Parser.PositionSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#positionSpecList.
    def exitPositionSpecList(self, ctx:Fortran90Parser.PositionSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#unitIdentifierComma.
    def enterUnitIdentifierComma(self, ctx:Fortran90Parser.UnitIdentifierCommaContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#unitIdentifierComma.
    def exitUnitIdentifierComma(self, ctx:Fortran90Parser.UnitIdentifierCommaContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#positionSpec.
    def enterPositionSpec(self, ctx:Fortran90Parser.PositionSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#positionSpec.
    def exitPositionSpec(self, ctx:Fortran90Parser.PositionSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#scalarVariable.
    def enterScalarVariable(self, ctx:Fortran90Parser.ScalarVariableContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#scalarVariable.
    def exitScalarVariable(self, ctx:Fortran90Parser.ScalarVariableContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#uFExpr.
    def enterUFExpr(self, ctx:Fortran90Parser.UFExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#uFExpr.
    def exitUFExpr(self, ctx:Fortran90Parser.UFExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#uFTerm.
    def enterUFTerm(self, ctx:Fortran90Parser.UFTermContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#uFTerm.
    def exitUFTerm(self, ctx:Fortran90Parser.UFTermContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#uFFactor.
    def enterUFFactor(self, ctx:Fortran90Parser.UFFactorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#uFFactor.
    def exitUFFactor(self, ctx:Fortran90Parser.UFFactorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#uFPrimary.
    def enterUFPrimary(self, ctx:Fortran90Parser.UFPrimaryContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#uFPrimary.
    def exitUFPrimary(self, ctx:Fortran90Parser.UFPrimaryContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineSubprogram.
    def enterSubroutineSubprogram(self, ctx:Fortran90Parser.SubroutineSubprogramContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineSubprogram.
    def exitSubroutineSubprogram(self, ctx:Fortran90Parser.SubroutineSubprogramContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineName.
    def enterSubroutineName(self, ctx:Fortran90Parser.SubroutineNameContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineName.
    def exitSubroutineName(self, ctx:Fortran90Parser.SubroutineNameContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subroutineRange.
    def enterSubroutineRange(self, ctx:Fortran90Parser.SubroutineRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subroutineRange.
    def exitSubroutineRange(self, ctx:Fortran90Parser.SubroutineRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#includeStmt.
    def enterIncludeStmt(self, ctx:Fortran90Parser.IncludeStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#includeStmt.
    def exitIncludeStmt(self, ctx:Fortran90Parser.IncludeStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#implicitStmt.
    def enterImplicitStmt(self, ctx:Fortran90Parser.ImplicitStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#implicitStmt.
    def exitImplicitStmt(self, ctx:Fortran90Parser.ImplicitStmtContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#implicitSpecList.
    def enterImplicitSpecList(self, ctx:Fortran90Parser.ImplicitSpecListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#implicitSpecList.
    def exitImplicitSpecList(self, ctx:Fortran90Parser.ImplicitSpecListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#implicitSpec.
    def enterImplicitSpec(self, ctx:Fortran90Parser.ImplicitSpecContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#implicitSpec.
    def exitImplicitSpec(self, ctx:Fortran90Parser.ImplicitSpecContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#implicitRanges.
    def enterImplicitRanges(self, ctx:Fortran90Parser.ImplicitRangesContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#implicitRanges.
    def exitImplicitRanges(self, ctx:Fortran90Parser.ImplicitRangesContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#implicitRange.
    def enterImplicitRange(self, ctx:Fortran90Parser.ImplicitRangeContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#implicitRange.
    def exitImplicitRange(self, ctx:Fortran90Parser.ImplicitRangeContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#expression.
    def enterExpression(self, ctx:Fortran90Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#expression.
    def exitExpression(self, ctx:Fortran90Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#definedBinaryOp.
    def enterDefinedBinaryOp(self, ctx:Fortran90Parser.DefinedBinaryOpContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#definedBinaryOp.
    def exitDefinedBinaryOp(self, ctx:Fortran90Parser.DefinedBinaryOpContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#level5Expr.
    def enterLevel5Expr(self, ctx:Fortran90Parser.Level5ExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#level5Expr.
    def exitLevel5Expr(self, ctx:Fortran90Parser.Level5ExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#equivOperand.
    def enterEquivOperand(self, ctx:Fortran90Parser.EquivOperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#equivOperand.
    def exitEquivOperand(self, ctx:Fortran90Parser.EquivOperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#orOperand.
    def enterOrOperand(self, ctx:Fortran90Parser.OrOperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#orOperand.
    def exitOrOperand(self, ctx:Fortran90Parser.OrOperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#andOperand.
    def enterAndOperand(self, ctx:Fortran90Parser.AndOperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#andOperand.
    def exitAndOperand(self, ctx:Fortran90Parser.AndOperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#relOp.
    def enterRelOp(self, ctx:Fortran90Parser.RelOpContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#relOp.
    def exitRelOp(self, ctx:Fortran90Parser.RelOpContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#level4Expr.
    def enterLevel4Expr(self, ctx:Fortran90Parser.Level4ExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#level4Expr.
    def exitLevel4Expr(self, ctx:Fortran90Parser.Level4ExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#level3Expr.
    def enterLevel3Expr(self, ctx:Fortran90Parser.Level3ExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#level3Expr.
    def exitLevel3Expr(self, ctx:Fortran90Parser.Level3ExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#level2Expr.
    def enterLevel2Expr(self, ctx:Fortran90Parser.Level2ExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#level2Expr.
    def exitLevel2Expr(self, ctx:Fortran90Parser.Level2ExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sign.
    def enterSign(self, ctx:Fortran90Parser.SignContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sign.
    def exitSign(self, ctx:Fortran90Parser.SignContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#addOperand.
    def enterAddOperand(self, ctx:Fortran90Parser.AddOperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#addOperand.
    def exitAddOperand(self, ctx:Fortran90Parser.AddOperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#multOperand.
    def enterMultOperand(self, ctx:Fortran90Parser.MultOperandContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#multOperand.
    def exitMultOperand(self, ctx:Fortran90Parser.MultOperandContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#level1Expr.
    def enterLevel1Expr(self, ctx:Fortran90Parser.Level1ExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#level1Expr.
    def exitLevel1Expr(self, ctx:Fortran90Parser.Level1ExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#definedUnaryOp.
    def enterDefinedUnaryOp(self, ctx:Fortran90Parser.DefinedUnaryOpContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#definedUnaryOp.
    def exitDefinedUnaryOp(self, ctx:Fortran90Parser.DefinedUnaryOpContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#primary.
    def enterPrimary(self, ctx:Fortran90Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#primary.
    def exitPrimary(self, ctx:Fortran90Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#arrayConstructor.
    def enterArrayConstructor(self, ctx:Fortran90Parser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#arrayConstructor.
    def exitArrayConstructor(self, ctx:Fortran90Parser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#acValueList.
    def enterAcValueList(self, ctx:Fortran90Parser.AcValueListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#acValueList.
    def exitAcValueList(self, ctx:Fortran90Parser.AcValueListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#acValueList1.
    def enterAcValueList1(self, ctx:Fortran90Parser.AcValueList1Context):
        pass

    # Exit a parse tree produced by Fortran90Parser#acValueList1.
    def exitAcValueList1(self, ctx:Fortran90Parser.AcValueList1Context):
        pass


    # Enter a parse tree produced by Fortran90Parser#acImpliedDo.
    def enterAcImpliedDo(self, ctx:Fortran90Parser.AcImpliedDoContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#acImpliedDo.
    def exitAcImpliedDo(self, ctx:Fortran90Parser.AcImpliedDoContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionReference.
    def enterFunctionReference(self, ctx:Fortran90Parser.FunctionReferenceContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionReference.
    def exitFunctionReference(self, ctx:Fortran90Parser.FunctionReferenceContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionArgList.
    def enterFunctionArgList(self, ctx:Fortran90Parser.FunctionArgListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionArgList.
    def exitFunctionArgList(self, ctx:Fortran90Parser.FunctionArgListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#functionArg.
    def enterFunctionArg(self, ctx:Fortran90Parser.FunctionArgContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#functionArg.
    def exitFunctionArg(self, ctx:Fortran90Parser.FunctionArgContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#nameDataRef.
    def enterNameDataRef(self, ctx:Fortran90Parser.NameDataRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#nameDataRef.
    def exitNameDataRef(self, ctx:Fortran90Parser.NameDataRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#complexDataRefTail.
    def enterComplexDataRefTail(self, ctx:Fortran90Parser.ComplexDataRefTailContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#complexDataRefTail.
    def exitComplexDataRefTail(self, ctx:Fortran90Parser.ComplexDataRefTailContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sectionSubscriptRef.
    def enterSectionSubscriptRef(self, ctx:Fortran90Parser.SectionSubscriptRefContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sectionSubscriptRef.
    def exitSectionSubscriptRef(self, ctx:Fortran90Parser.SectionSubscriptRefContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sectionSubscriptList.
    def enterSectionSubscriptList(self, ctx:Fortran90Parser.SectionSubscriptListContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sectionSubscriptList.
    def exitSectionSubscriptList(self, ctx:Fortran90Parser.SectionSubscriptListContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#sectionSubscript.
    def enterSectionSubscript(self, ctx:Fortran90Parser.SectionSubscriptContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#sectionSubscript.
    def exitSectionSubscript(self, ctx:Fortran90Parser.SectionSubscriptContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#subscriptTripletTail.
    def enterSubscriptTripletTail(self, ctx:Fortran90Parser.SubscriptTripletTailContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#subscriptTripletTail.
    def exitSubscriptTripletTail(self, ctx:Fortran90Parser.SubscriptTripletTailContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#logicalConstant.
    def enterLogicalConstant(self, ctx:Fortran90Parser.LogicalConstantContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#logicalConstant.
    def exitLogicalConstant(self, ctx:Fortran90Parser.LogicalConstantContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#kindParam.
    def enterKindParam(self, ctx:Fortran90Parser.KindParamContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#kindParam.
    def exitKindParam(self, ctx:Fortran90Parser.KindParamContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#unsignedArithmeticConstant.
    def enterUnsignedArithmeticConstant(self, ctx:Fortran90Parser.UnsignedArithmeticConstantContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#unsignedArithmeticConstant.
    def exitUnsignedArithmeticConstant(self, ctx:Fortran90Parser.UnsignedArithmeticConstantContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#complexConst.
    def enterComplexConst(self, ctx:Fortran90Parser.ComplexConstContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#complexConst.
    def exitComplexConst(self, ctx:Fortran90Parser.ComplexConstContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#complexComponent.
    def enterComplexComponent(self, ctx:Fortran90Parser.ComplexComponentContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#complexComponent.
    def exitComplexComponent(self, ctx:Fortran90Parser.ComplexComponentContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#constantExpr.
    def enterConstantExpr(self, ctx:Fortran90Parser.ConstantExprContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#constantExpr.
    def exitConstantExpr(self, ctx:Fortran90Parser.ConstantExprContext):
        pass


    # Enter a parse tree produced by Fortran90Parser#ifStmt.
    def enterIfStmt(self, ctx:Fortran90Parser.IfStmtContext):
        pass

    # Exit a parse tree produced by Fortran90Parser#ifStmt.
    def exitIfStmt(self, ctx:Fortran90Parser.IfStmtContext):
        pass



del Fortran90Parser