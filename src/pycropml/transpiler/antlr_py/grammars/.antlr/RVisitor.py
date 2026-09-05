# Generated from R.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete generic visitor for a parse tree produced by RParser.

class RVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RParser#prog.
    def visitProg(self, ctx:RParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Inf.
    def visitInf(self, ctx:RParser.InfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Null.
    def visitNull(self, ctx:RParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Help.
    def visitHelp(self, ctx:RParser.HelpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Or.
    def visitOr(self, ctx:RParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Exponent.
    def visitExponent(self, ctx:RParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#IfElse.
    def visitIfElse(self, ctx:RParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Break.
    def visitBreak(self, ctx:RParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#True.
    def visitTrue(self, ctx:RParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Repeat.
    def visitRepeat(self, ctx:RParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#String.
    def visitString(self, ctx:RParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#False.
    def visitFalse(self, ctx:RParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Newline.
    def visitNewline(self, ctx:RParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Int.
    def visitInt(self, ctx:RParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Complex.
    def visitComplex(self, ctx:RParser.ComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Assignment.
    def visitAssignment(self, ctx:RParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#AddOrSub.
    def visitAddOrSub(self, ctx:RParser.AddOrSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#ArrayAccess.
    def visitArrayAccess(self, ctx:RParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Na.
    def visitNa(self, ctx:RParser.NaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#ComponentAccess.
    def visitComponentAccess(self, ctx:RParser.ComponentAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Comparison.
    def visitComparison(self, ctx:RParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#UserDefinedOperation.
    def visitUserDefinedOperation(self, ctx:RParser.UserDefinedOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#FunctionDefinition.
    def visitFunctionDefinition(self, ctx:RParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#FunctionCall.
    def visitFunctionCall(self, ctx:RParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#MultOrDiv.
    def visitMultOrDiv(self, ctx:RParser.MultOrDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#BracketTerm.
    def visitBracketTerm(self, ctx:RParser.BracketTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#ModelFormulaePrefix.
    def visitModelFormulaePrefix(self, ctx:RParser.ModelFormulaePrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#CompoundStatement.
    def visitCompoundStatement(self, ctx:RParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#ModelFormulaeInfix.
    def visitModelFormulaeInfix(self, ctx:RParser.ModelFormulaeInfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#ListAccess.
    def visitListAccess(self, ctx:RParser.ListAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#For.
    def visitFor(self, ctx:RParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#While.
    def visitWhile(self, ctx:RParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Range.
    def visitRange(self, ctx:RParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Float.
    def visitFloat(self, ctx:RParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Not.
    def visitNot(self, ctx:RParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#And.
    def visitAnd(self, ctx:RParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Next.
    def visitNext(self, ctx:RParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Sign.
    def visitSign(self, ctx:RParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Hex.
    def visitHex(self, ctx:RParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Nan.
    def visitNan(self, ctx:RParser.NanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#NamespaceAccess.
    def visitNamespaceAccess(self, ctx:RParser.NamespaceAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#Id.
    def visitId(self, ctx:RParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#If.
    def visitIf(self, ctx:RParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#exprlist.
    def visitExprlist(self, ctx:RParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#formlist.
    def visitFormlist(self, ctx:RParser.FormlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#form.
    def visitForm(self, ctx:RParser.FormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#sublist.
    def visitSublist(self, ctx:RParser.SublistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#sub.
    def visitSub(self, ctx:RParser.SubContext):
        return self.visitChildren(ctx)



del RParser