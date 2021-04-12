# Generated from Documents\THESE\pycropml_pheno\src\pycropml\antlr_grammarV4\r\R.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete generic visitor for a parse tree produced by RParser.

class RVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RParser#prog.
    def visitProg(self, ctx:RParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RParser#expr.
    def visitExpr(self, ctx:RParser.ExprContext):
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