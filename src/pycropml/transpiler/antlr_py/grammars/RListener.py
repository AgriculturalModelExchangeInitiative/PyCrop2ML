# Generated from R.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete listener for a parse tree produced by RParser.
class RListener(ParseTreeListener):

    # Enter a parse tree produced by RParser#prog.
    def enterProg(self, ctx:RParser.ProgContext):
        pass

    # Exit a parse tree produced by RParser#prog.
    def exitProg(self, ctx:RParser.ProgContext):
        pass


    # Enter a parse tree produced by RParser#Inf.
    def enterInf(self, ctx:RParser.InfContext):
        pass

    # Exit a parse tree produced by RParser#Inf.
    def exitInf(self, ctx:RParser.InfContext):
        pass


    # Enter a parse tree produced by RParser#Null.
    def enterNull(self, ctx:RParser.NullContext):
        pass

    # Exit a parse tree produced by RParser#Null.
    def exitNull(self, ctx:RParser.NullContext):
        pass


    # Enter a parse tree produced by RParser#Help.
    def enterHelp(self, ctx:RParser.HelpContext):
        pass

    # Exit a parse tree produced by RParser#Help.
    def exitHelp(self, ctx:RParser.HelpContext):
        pass


    # Enter a parse tree produced by RParser#Or.
    def enterOr(self, ctx:RParser.OrContext):
        pass

    # Exit a parse tree produced by RParser#Or.
    def exitOr(self, ctx:RParser.OrContext):
        pass


    # Enter a parse tree produced by RParser#Exponent.
    def enterExponent(self, ctx:RParser.ExponentContext):
        pass

    # Exit a parse tree produced by RParser#Exponent.
    def exitExponent(self, ctx:RParser.ExponentContext):
        pass


    # Enter a parse tree produced by RParser#IfElse.
    def enterIfElse(self, ctx:RParser.IfElseContext):
        pass

    # Exit a parse tree produced by RParser#IfElse.
    def exitIfElse(self, ctx:RParser.IfElseContext):
        pass


    # Enter a parse tree produced by RParser#Break.
    def enterBreak(self, ctx:RParser.BreakContext):
        pass

    # Exit a parse tree produced by RParser#Break.
    def exitBreak(self, ctx:RParser.BreakContext):
        pass


    # Enter a parse tree produced by RParser#True.
    def enterTrue(self, ctx:RParser.TrueContext):
        pass

    # Exit a parse tree produced by RParser#True.
    def exitTrue(self, ctx:RParser.TrueContext):
        pass


    # Enter a parse tree produced by RParser#Repeat.
    def enterRepeat(self, ctx:RParser.RepeatContext):
        pass

    # Exit a parse tree produced by RParser#Repeat.
    def exitRepeat(self, ctx:RParser.RepeatContext):
        pass


    # Enter a parse tree produced by RParser#String.
    def enterString(self, ctx:RParser.StringContext):
        pass

    # Exit a parse tree produced by RParser#String.
    def exitString(self, ctx:RParser.StringContext):
        pass


    # Enter a parse tree produced by RParser#False.
    def enterFalse(self, ctx:RParser.FalseContext):
        pass

    # Exit a parse tree produced by RParser#False.
    def exitFalse(self, ctx:RParser.FalseContext):
        pass


    # Enter a parse tree produced by RParser#Newline.
    def enterNewline(self, ctx:RParser.NewlineContext):
        pass

    # Exit a parse tree produced by RParser#Newline.
    def exitNewline(self, ctx:RParser.NewlineContext):
        pass


    # Enter a parse tree produced by RParser#Int.
    def enterInt(self, ctx:RParser.IntContext):
        pass

    # Exit a parse tree produced by RParser#Int.
    def exitInt(self, ctx:RParser.IntContext):
        pass


    # Enter a parse tree produced by RParser#Complex.
    def enterComplex(self, ctx:RParser.ComplexContext):
        pass

    # Exit a parse tree produced by RParser#Complex.
    def exitComplex(self, ctx:RParser.ComplexContext):
        pass


    # Enter a parse tree produced by RParser#Assignment.
    def enterAssignment(self, ctx:RParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RParser#Assignment.
    def exitAssignment(self, ctx:RParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RParser#AddOrSub.
    def enterAddOrSub(self, ctx:RParser.AddOrSubContext):
        pass

    # Exit a parse tree produced by RParser#AddOrSub.
    def exitAddOrSub(self, ctx:RParser.AddOrSubContext):
        pass


    # Enter a parse tree produced by RParser#ArrayAccess.
    def enterArrayAccess(self, ctx:RParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by RParser#ArrayAccess.
    def exitArrayAccess(self, ctx:RParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by RParser#Na.
    def enterNa(self, ctx:RParser.NaContext):
        pass

    # Exit a parse tree produced by RParser#Na.
    def exitNa(self, ctx:RParser.NaContext):
        pass


    # Enter a parse tree produced by RParser#ComponentAccess.
    def enterComponentAccess(self, ctx:RParser.ComponentAccessContext):
        pass

    # Exit a parse tree produced by RParser#ComponentAccess.
    def exitComponentAccess(self, ctx:RParser.ComponentAccessContext):
        pass


    # Enter a parse tree produced by RParser#Comparison.
    def enterComparison(self, ctx:RParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RParser#Comparison.
    def exitComparison(self, ctx:RParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RParser#UserDefinedOperation.
    def enterUserDefinedOperation(self, ctx:RParser.UserDefinedOperationContext):
        pass

    # Exit a parse tree produced by RParser#UserDefinedOperation.
    def exitUserDefinedOperation(self, ctx:RParser.UserDefinedOperationContext):
        pass


    # Enter a parse tree produced by RParser#FunctionDefinition.
    def enterFunctionDefinition(self, ctx:RParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by RParser#FunctionDefinition.
    def exitFunctionDefinition(self, ctx:RParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by RParser#FunctionCall.
    def enterFunctionCall(self, ctx:RParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by RParser#FunctionCall.
    def exitFunctionCall(self, ctx:RParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by RParser#MultOrDiv.
    def enterMultOrDiv(self, ctx:RParser.MultOrDivContext):
        pass

    # Exit a parse tree produced by RParser#MultOrDiv.
    def exitMultOrDiv(self, ctx:RParser.MultOrDivContext):
        pass


    # Enter a parse tree produced by RParser#BracketTerm.
    def enterBracketTerm(self, ctx:RParser.BracketTermContext):
        pass

    # Exit a parse tree produced by RParser#BracketTerm.
    def exitBracketTerm(self, ctx:RParser.BracketTermContext):
        pass


    # Enter a parse tree produced by RParser#ModelFormulaePrefix.
    def enterModelFormulaePrefix(self, ctx:RParser.ModelFormulaePrefixContext):
        pass

    # Exit a parse tree produced by RParser#ModelFormulaePrefix.
    def exitModelFormulaePrefix(self, ctx:RParser.ModelFormulaePrefixContext):
        pass


    # Enter a parse tree produced by RParser#CompoundStatement.
    def enterCompoundStatement(self, ctx:RParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by RParser#CompoundStatement.
    def exitCompoundStatement(self, ctx:RParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by RParser#ModelFormulaeInfix.
    def enterModelFormulaeInfix(self, ctx:RParser.ModelFormulaeInfixContext):
        pass

    # Exit a parse tree produced by RParser#ModelFormulaeInfix.
    def exitModelFormulaeInfix(self, ctx:RParser.ModelFormulaeInfixContext):
        pass


    # Enter a parse tree produced by RParser#ListAccess.
    def enterListAccess(self, ctx:RParser.ListAccessContext):
        pass

    # Exit a parse tree produced by RParser#ListAccess.
    def exitListAccess(self, ctx:RParser.ListAccessContext):
        pass


    # Enter a parse tree produced by RParser#For.
    def enterFor(self, ctx:RParser.ForContext):
        pass

    # Exit a parse tree produced by RParser#For.
    def exitFor(self, ctx:RParser.ForContext):
        pass


    # Enter a parse tree produced by RParser#While.
    def enterWhile(self, ctx:RParser.WhileContext):
        pass

    # Exit a parse tree produced by RParser#While.
    def exitWhile(self, ctx:RParser.WhileContext):
        pass


    # Enter a parse tree produced by RParser#Range.
    def enterRange(self, ctx:RParser.RangeContext):
        pass

    # Exit a parse tree produced by RParser#Range.
    def exitRange(self, ctx:RParser.RangeContext):
        pass


    # Enter a parse tree produced by RParser#Float.
    def enterFloat(self, ctx:RParser.FloatContext):
        pass

    # Exit a parse tree produced by RParser#Float.
    def exitFloat(self, ctx:RParser.FloatContext):
        pass


    # Enter a parse tree produced by RParser#Not.
    def enterNot(self, ctx:RParser.NotContext):
        pass

    # Exit a parse tree produced by RParser#Not.
    def exitNot(self, ctx:RParser.NotContext):
        pass


    # Enter a parse tree produced by RParser#And.
    def enterAnd(self, ctx:RParser.AndContext):
        pass

    # Exit a parse tree produced by RParser#And.
    def exitAnd(self, ctx:RParser.AndContext):
        pass


    # Enter a parse tree produced by RParser#Next.
    def enterNext(self, ctx:RParser.NextContext):
        pass

    # Exit a parse tree produced by RParser#Next.
    def exitNext(self, ctx:RParser.NextContext):
        pass


    # Enter a parse tree produced by RParser#Sign.
    def enterSign(self, ctx:RParser.SignContext):
        pass

    # Exit a parse tree produced by RParser#Sign.
    def exitSign(self, ctx:RParser.SignContext):
        pass


    # Enter a parse tree produced by RParser#Hex.
    def enterHex(self, ctx:RParser.HexContext):
        pass

    # Exit a parse tree produced by RParser#Hex.
    def exitHex(self, ctx:RParser.HexContext):
        pass


    # Enter a parse tree produced by RParser#Nan.
    def enterNan(self, ctx:RParser.NanContext):
        pass

    # Exit a parse tree produced by RParser#Nan.
    def exitNan(self, ctx:RParser.NanContext):
        pass


    # Enter a parse tree produced by RParser#NamespaceAccess.
    def enterNamespaceAccess(self, ctx:RParser.NamespaceAccessContext):
        pass

    # Exit a parse tree produced by RParser#NamespaceAccess.
    def exitNamespaceAccess(self, ctx:RParser.NamespaceAccessContext):
        pass


    # Enter a parse tree produced by RParser#Id.
    def enterId(self, ctx:RParser.IdContext):
        pass

    # Exit a parse tree produced by RParser#Id.
    def exitId(self, ctx:RParser.IdContext):
        pass


    # Enter a parse tree produced by RParser#If.
    def enterIf(self, ctx:RParser.IfContext):
        pass

    # Exit a parse tree produced by RParser#If.
    def exitIf(self, ctx:RParser.IfContext):
        pass


    # Enter a parse tree produced by RParser#exprlist.
    def enterExprlist(self, ctx:RParser.ExprlistContext):
        pass

    # Exit a parse tree produced by RParser#exprlist.
    def exitExprlist(self, ctx:RParser.ExprlistContext):
        pass


    # Enter a parse tree produced by RParser#formlist.
    def enterFormlist(self, ctx:RParser.FormlistContext):
        pass

    # Exit a parse tree produced by RParser#formlist.
    def exitFormlist(self, ctx:RParser.FormlistContext):
        pass


    # Enter a parse tree produced by RParser#form.
    def enterForm(self, ctx:RParser.FormContext):
        pass

    # Exit a parse tree produced by RParser#form.
    def exitForm(self, ctx:RParser.FormContext):
        pass


    # Enter a parse tree produced by RParser#sublist.
    def enterSublist(self, ctx:RParser.SublistContext):
        pass

    # Exit a parse tree produced by RParser#sublist.
    def exitSublist(self, ctx:RParser.SublistContext):
        pass


    # Enter a parse tree produced by RParser#sub.
    def enterSub(self, ctx:RParser.SubContext):
        pass

    # Exit a parse tree produced by RParser#sub.
    def exitSub(self, ctx:RParser.SubContext):
        pass



del RParser