# Generated from Documents\THESE\pycropml_pheno\src\pycropml\antlr_grammarV4\fortran77\Fortran77Parser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Fortran77Parser import Fortran77Parser
else:
    from Fortran77Parser import Fortran77Parser

# This class defines a complete generic visitor for a parse tree produced by Fortran77Parser.

class Fortran77ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Fortran77Parser#program.
    def visitProgram(self, ctx:Fortran77Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#executableUnit.
    def visitExecutableUnit(self, ctx:Fortran77Parser.ExecutableUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#mainProgram.
    def visitMainProgram(self, ctx:Fortran77Parser.MainProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#functionSubprogram.
    def visitFunctionSubprogram(self, ctx:Fortran77Parser.FunctionSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subroutineSubprogram.
    def visitSubroutineSubprogram(self, ctx:Fortran77Parser.SubroutineSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#blockdataSubprogram.
    def visitBlockdataSubprogram(self, ctx:Fortran77Parser.BlockdataSubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#otherSpecificationStatement.
    def visitOtherSpecificationStatement(self, ctx:Fortran77Parser.OtherSpecificationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#executableStatement.
    def visitExecutableStatement(self, ctx:Fortran77Parser.ExecutableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#programStatement.
    def visitProgramStatement(self, ctx:Fortran77Parser.ProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#entryStatement.
    def visitEntryStatement(self, ctx:Fortran77Parser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#functionStatement.
    def visitFunctionStatement(self, ctx:Fortran77Parser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#blockdataStatement.
    def visitBlockdataStatement(self, ctx:Fortran77Parser.BlockdataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subroutineStatement.
    def visitSubroutineStatement(self, ctx:Fortran77Parser.SubroutineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#namelist.
    def visitNamelist(self, ctx:Fortran77Parser.NamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#statement.
    def visitStatement(self, ctx:Fortran77Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subprogramBody.
    def visitSubprogramBody(self, ctx:Fortran77Parser.SubprogramBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#wholeStatement.
    def visitWholeStatement(self, ctx:Fortran77Parser.WholeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#endStatement.
    def visitEndStatement(self, ctx:Fortran77Parser.EndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dimensionStatement.
    def visitDimensionStatement(self, ctx:Fortran77Parser.DimensionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayDeclarator.
    def visitArrayDeclarator(self, ctx:Fortran77Parser.ArrayDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayDeclarators.
    def visitArrayDeclarators(self, ctx:Fortran77Parser.ArrayDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayDeclaratorExtents.
    def visitArrayDeclaratorExtents(self, ctx:Fortran77Parser.ArrayDeclaratorExtentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayDeclaratorExtent.
    def visitArrayDeclaratorExtent(self, ctx:Fortran77Parser.ArrayDeclaratorExtentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#equivalenceStatement.
    def visitEquivalenceStatement(self, ctx:Fortran77Parser.EquivalenceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#equivEntityGroup.
    def visitEquivEntityGroup(self, ctx:Fortran77Parser.EquivEntityGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#equivEntity.
    def visitEquivEntity(self, ctx:Fortran77Parser.EquivEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commonStatement.
    def visitCommonStatement(self, ctx:Fortran77Parser.CommonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commonName.
    def visitCommonName(self, ctx:Fortran77Parser.CommonNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commonItem.
    def visitCommonItem(self, ctx:Fortran77Parser.CommonItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commonItems.
    def visitCommonItems(self, ctx:Fortran77Parser.CommonItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commonBlock.
    def visitCommonBlock(self, ctx:Fortran77Parser.CommonBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#commentStatement.
    def visitCommentStatement(self, ctx:Fortran77Parser.CommentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatement.
    def visitTypeStatement(self, ctx:Fortran77Parser.TypeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatementNameList.
    def visitTypeStatementNameList(self, ctx:Fortran77Parser.TypeStatementNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatementName.
    def visitTypeStatementName(self, ctx:Fortran77Parser.TypeStatementNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatementNameCharList.
    def visitTypeStatementNameCharList(self, ctx:Fortran77Parser.TypeStatementNameCharListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatementNameChar.
    def visitTypeStatementNameChar(self, ctx:Fortran77Parser.TypeStatementNameCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typeStatementLenSpec.
    def visitTypeStatementLenSpec(self, ctx:Fortran77Parser.TypeStatementLenSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typename.
    def visitTypename(self, ctx:Fortran77Parser.TypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#type.
    def visitType(self, ctx:Fortran77Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#typenameLen.
    def visitTypenameLen(self, ctx:Fortran77Parser.TypenameLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#pointerStatement.
    def visitPointerStatement(self, ctx:Fortran77Parser.PointerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#pointerDecl.
    def visitPointerDecl(self, ctx:Fortran77Parser.PointerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitStatement.
    def visitImplicitStatement(self, ctx:Fortran77Parser.ImplicitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitSpec.
    def visitImplicitSpec(self, ctx:Fortran77Parser.ImplicitSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitSpecs.
    def visitImplicitSpecs(self, ctx:Fortran77Parser.ImplicitSpecsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitNone.
    def visitImplicitNone(self, ctx:Fortran77Parser.ImplicitNoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitLetter.
    def visitImplicitLetter(self, ctx:Fortran77Parser.ImplicitLetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitRange.
    def visitImplicitRange(self, ctx:Fortran77Parser.ImplicitRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#implicitLetters.
    def visitImplicitLetters(self, ctx:Fortran77Parser.ImplicitLettersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lenSpecification.
    def visitLenSpecification(self, ctx:Fortran77Parser.LenSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#characterWithLen.
    def visitCharacterWithLen(self, ctx:Fortran77Parser.CharacterWithLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#cwlLen.
    def visitCwlLen(self, ctx:Fortran77Parser.CwlLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#parameterStatement.
    def visitParameterStatement(self, ctx:Fortran77Parser.ParameterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#paramlist.
    def visitParamlist(self, ctx:Fortran77Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#paramassign.
    def visitParamassign(self, ctx:Fortran77Parser.ParamassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#externalStatement.
    def visitExternalStatement(self, ctx:Fortran77Parser.ExternalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#intrinsicStatement.
    def visitIntrinsicStatement(self, ctx:Fortran77Parser.IntrinsicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#saveStatement.
    def visitSaveStatement(self, ctx:Fortran77Parser.SaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#saveEntity.
    def visitSaveEntity(self, ctx:Fortran77Parser.SaveEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataStatement.
    def visitDataStatement(self, ctx:Fortran77Parser.DataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataStatementItem.
    def visitDataStatementItem(self, ctx:Fortran77Parser.DataStatementItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataStatementMultiple.
    def visitDataStatementMultiple(self, ctx:Fortran77Parser.DataStatementMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataStatementEntity.
    def visitDataStatementEntity(self, ctx:Fortran77Parser.DataStatementEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dse1.
    def visitDse1(self, ctx:Fortran77Parser.Dse1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dse2.
    def visitDse2(self, ctx:Fortran77Parser.Dse2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataImpliedDo.
    def visitDataImpliedDo(self, ctx:Fortran77Parser.DataImpliedDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataImpliedDoRange.
    def visitDataImpliedDoRange(self, ctx:Fortran77Parser.DataImpliedDoRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataImpliedDoList.
    def visitDataImpliedDoList(self, ctx:Fortran77Parser.DataImpliedDoListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#dataImpliedDoListWhat.
    def visitDataImpliedDoListWhat(self, ctx:Fortran77Parser.DataImpliedDoListWhatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#gotoStatement.
    def visitGotoStatement(self, ctx:Fortran77Parser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#unconditionalGoto.
    def visitUnconditionalGoto(self, ctx:Fortran77Parser.UnconditionalGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#computedGoto.
    def visitComputedGoto(self, ctx:Fortran77Parser.ComputedGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lblRef.
    def visitLblRef(self, ctx:Fortran77Parser.LblRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#labelList.
    def visitLabelList(self, ctx:Fortran77Parser.LabelListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#assignedGoto.
    def visitAssignedGoto(self, ctx:Fortran77Parser.AssignedGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#ifStatement.
    def visitIfStatement(self, ctx:Fortran77Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arithmeticIfStatement.
    def visitArithmeticIfStatement(self, ctx:Fortran77Parser.ArithmeticIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#logicalIfStatement.
    def visitLogicalIfStatement(self, ctx:Fortran77Parser.LogicalIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#blockIfStatement.
    def visitBlockIfStatement(self, ctx:Fortran77Parser.BlockIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#firstIfBlock.
    def visitFirstIfBlock(self, ctx:Fortran77Parser.FirstIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#elseIfStatement.
    def visitElseIfStatement(self, ctx:Fortran77Parser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#elseStatement.
    def visitElseStatement(self, ctx:Fortran77Parser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#endIfStatement.
    def visitEndIfStatement(self, ctx:Fortran77Parser.EndIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#doStatement.
    def visitDoStatement(self, ctx:Fortran77Parser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#doVarArgs.
    def visitDoVarArgs(self, ctx:Fortran77Parser.DoVarArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#doWithLabel.
    def visitDoWithLabel(self, ctx:Fortran77Parser.DoWithLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#doBody.
    def visitDoBody(self, ctx:Fortran77Parser.DoBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#doWithEndDo.
    def visitDoWithEndDo(self, ctx:Fortran77Parser.DoWithEndDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#enddoStatement.
    def visitEnddoStatement(self, ctx:Fortran77Parser.EnddoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#continueStatement.
    def visitContinueStatement(self, ctx:Fortran77Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#stopStatement.
    def visitStopStatement(self, ctx:Fortran77Parser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#pauseStatement.
    def visitPauseStatement(self, ctx:Fortran77Parser.PauseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#writeStatement.
    def visitWriteStatement(self, ctx:Fortran77Parser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#readStatement.
    def visitReadStatement(self, ctx:Fortran77Parser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#printStatement.
    def visitPrintStatement(self, ctx:Fortran77Parser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:Fortran77Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlInfoList.
    def visitControlInfoList(self, ctx:Fortran77Parser.ControlInfoListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlErrSpec.
    def visitControlErrSpec(self, ctx:Fortran77Parser.ControlErrSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlInfoListItem.
    def visitControlInfoListItem(self, ctx:Fortran77Parser.ControlInfoListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#ioList.
    def visitIoList(self, ctx:Fortran77Parser.IoListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#ioListItem.
    def visitIoListItem(self, ctx:Fortran77Parser.IoListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#ioImpliedDoList.
    def visitIoImpliedDoList(self, ctx:Fortran77Parser.IoImpliedDoListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#openStatement.
    def visitOpenStatement(self, ctx:Fortran77Parser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#openControl.
    def visitOpenControl(self, ctx:Fortran77Parser.OpenControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlFmt.
    def visitControlFmt(self, ctx:Fortran77Parser.ControlFmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlUnit.
    def visitControlUnit(self, ctx:Fortran77Parser.ControlUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlRec.
    def visitControlRec(self, ctx:Fortran77Parser.ControlRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlEnd.
    def visitControlEnd(self, ctx:Fortran77Parser.ControlEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlErr.
    def visitControlErr(self, ctx:Fortran77Parser.ControlErrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlIostat.
    def visitControlIostat(self, ctx:Fortran77Parser.ControlIostatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlFile.
    def visitControlFile(self, ctx:Fortran77Parser.ControlFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlStatus.
    def visitControlStatus(self, ctx:Fortran77Parser.ControlStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlAccess.
    def visitControlAccess(self, ctx:Fortran77Parser.ControlAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlPosition.
    def visitControlPosition(self, ctx:Fortran77Parser.ControlPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlForm.
    def visitControlForm(self, ctx:Fortran77Parser.ControlFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlRecl.
    def visitControlRecl(self, ctx:Fortran77Parser.ControlReclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlBlank.
    def visitControlBlank(self, ctx:Fortran77Parser.ControlBlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlExist.
    def visitControlExist(self, ctx:Fortran77Parser.ControlExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlOpened.
    def visitControlOpened(self, ctx:Fortran77Parser.ControlOpenedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlNumber.
    def visitControlNumber(self, ctx:Fortran77Parser.ControlNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlNamed.
    def visitControlNamed(self, ctx:Fortran77Parser.ControlNamedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlName.
    def visitControlName(self, ctx:Fortran77Parser.ControlNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlSequential.
    def visitControlSequential(self, ctx:Fortran77Parser.ControlSequentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlDirect.
    def visitControlDirect(self, ctx:Fortran77Parser.ControlDirectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlFormatted.
    def visitControlFormatted(self, ctx:Fortran77Parser.ControlFormattedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlUnformatted.
    def visitControlUnformatted(self, ctx:Fortran77Parser.ControlUnformattedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#controlNextrec.
    def visitControlNextrec(self, ctx:Fortran77Parser.ControlNextrecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#closeStatement.
    def visitCloseStatement(self, ctx:Fortran77Parser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#closeControl.
    def visitCloseControl(self, ctx:Fortran77Parser.CloseControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#inquireStatement.
    def visitInquireStatement(self, ctx:Fortran77Parser.InquireStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#inquireControl.
    def visitInquireControl(self, ctx:Fortran77Parser.InquireControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#backspaceStatement.
    def visitBackspaceStatement(self, ctx:Fortran77Parser.BackspaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#endfileStatement.
    def visitEndfileStatement(self, ctx:Fortran77Parser.EndfileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#rewindStatement.
    def visitRewindStatement(self, ctx:Fortran77Parser.RewindStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#berFinish.
    def visitBerFinish(self, ctx:Fortran77Parser.BerFinishContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#berFinishItem.
    def visitBerFinishItem(self, ctx:Fortran77Parser.BerFinishItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#unitIdentifier.
    def visitUnitIdentifier(self, ctx:Fortran77Parser.UnitIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#formatIdentifier.
    def visitFormatIdentifier(self, ctx:Fortran77Parser.FormatIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#formatStatement.
    def visitFormatStatement(self, ctx:Fortran77Parser.FormatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#fmtSpec.
    def visitFmtSpec(self, ctx:Fortran77Parser.FmtSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#formatsep.
    def visitFormatsep(self, ctx:Fortran77Parser.FormatsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#formatedit.
    def visitFormatedit(self, ctx:Fortran77Parser.FormateditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#editElement.
    def visitEditElement(self, ctx:Fortran77Parser.EditElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#statementFunctionStatement.
    def visitStatementFunctionStatement(self, ctx:Fortran77Parser.StatementFunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#sfArgs.
    def visitSfArgs(self, ctx:Fortran77Parser.SfArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#callStatement.
    def visitCallStatement(self, ctx:Fortran77Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subroutineCall.
    def visitSubroutineCall(self, ctx:Fortran77Parser.SubroutineCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#callArgumentList.
    def visitCallArgumentList(self, ctx:Fortran77Parser.CallArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#callArgument.
    def visitCallArgument(self, ctx:Fortran77Parser.CallArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#returnStatement.
    def visitReturnStatement(self, ctx:Fortran77Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#expression.
    def visitExpression(self, ctx:Fortran77Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#ncExpr.
    def visitNcExpr(self, ctx:Fortran77Parser.NcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lexpr0.
    def visitLexpr0(self, ctx:Fortran77Parser.Lexpr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lexpr1.
    def visitLexpr1(self, ctx:Fortran77Parser.Lexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lexpr2.
    def visitLexpr2(self, ctx:Fortran77Parser.Lexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lexpr3.
    def visitLexpr3(self, ctx:Fortran77Parser.Lexpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#lexpr4.
    def visitLexpr4(self, ctx:Fortran77Parser.Lexpr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#aexpr0.
    def visitAexpr0(self, ctx:Fortran77Parser.Aexpr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#aexpr1.
    def visitAexpr1(self, ctx:Fortran77Parser.Aexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#aexpr2.
    def visitAexpr2(self, ctx:Fortran77Parser.Aexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#aexpr3.
    def visitAexpr3(self, ctx:Fortran77Parser.Aexpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#aexpr4.
    def visitAexpr4(self, ctx:Fortran77Parser.Aexpr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexpr.
    def visitIexpr(self, ctx:Fortran77Parser.IexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexprCode.
    def visitIexprCode(self, ctx:Fortran77Parser.IexprCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexpr1.
    def visitIexpr1(self, ctx:Fortran77Parser.Iexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexpr2.
    def visitIexpr2(self, ctx:Fortran77Parser.Iexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexpr3.
    def visitIexpr3(self, ctx:Fortran77Parser.Iexpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#iexpr4.
    def visitIexpr4(self, ctx:Fortran77Parser.Iexpr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#constantExpr.
    def visitConstantExpr(self, ctx:Fortran77Parser.ConstantExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:Fortran77Parser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#integerExpr.
    def visitIntegerExpr(self, ctx:Fortran77Parser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#intRealDpExpr.
    def visitIntRealDpExpr(self, ctx:Fortran77Parser.IntRealDpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arithmeticConstExpr.
    def visitArithmeticConstExpr(self, ctx:Fortran77Parser.ArithmeticConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#intConstantExpr.
    def visitIntConstantExpr(self, ctx:Fortran77Parser.IntConstantExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#characterExpression.
    def visitCharacterExpression(self, ctx:Fortran77Parser.CharacterExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#concatOp.
    def visitConcatOp(self, ctx:Fortran77Parser.ConcatOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#logicalExpression.
    def visitLogicalExpression(self, ctx:Fortran77Parser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#logicalConstExpr.
    def visitLogicalConstExpr(self, ctx:Fortran77Parser.LogicalConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayElementName.
    def visitArrayElementName(self, ctx:Fortran77Parser.ArrayElementNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subscripts.
    def visitSubscripts(self, ctx:Fortran77Parser.SubscriptsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#varRef.
    def visitVarRef(self, ctx:Fortran77Parser.VarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#varRefCode.
    def visitVarRefCode(self, ctx:Fortran77Parser.VarRefCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#substringApp.
    def visitSubstringApp(self, ctx:Fortran77Parser.SubstringAppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#variableName.
    def visitVariableName(self, ctx:Fortran77Parser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#arrayName.
    def visitArrayName(self, ctx:Fortran77Parser.ArrayNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#subroutineName.
    def visitSubroutineName(self, ctx:Fortran77Parser.SubroutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#functionName.
    def visitFunctionName(self, ctx:Fortran77Parser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#constant.
    def visitConstant(self, ctx:Fortran77Parser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#unsignedArithmeticConstant.
    def visitUnsignedArithmeticConstant(self, ctx:Fortran77Parser.UnsignedArithmeticConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#complexConstant.
    def visitComplexConstant(self, ctx:Fortran77Parser.ComplexConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#logicalConstant.
    def visitLogicalConstant(self, ctx:Fortran77Parser.LogicalConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#identifier.
    def visitIdentifier(self, ctx:Fortran77Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Fortran77Parser#to.
    def visitTo(self, ctx:Fortran77Parser.ToContext):
        return self.visitChildren(ctx)



del Fortran77Parser