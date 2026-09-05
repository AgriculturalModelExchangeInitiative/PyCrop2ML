# Generated from RFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RFilter import RFilter
else:
    from RFilter import RFilter

# This class defines a complete generic visitor for a parse tree produced by RFilter.

class RFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RFilter#stream.
    def visitStream(self, ctx:RFilter.StreamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RFilter#eat.
    def visitEat(self, ctx:RFilter.EatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RFilter#elem.
    def visitElem(self, ctx:RFilter.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RFilter#atom.
    def visitAtom(self, ctx:RFilter.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RFilter#op.
    def visitOp(self, ctx:RFilter.OpContext):
        return self.visitChildren(ctx)



del RFilter