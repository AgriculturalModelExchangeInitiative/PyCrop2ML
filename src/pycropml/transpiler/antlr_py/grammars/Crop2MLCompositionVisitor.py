# Generated from src/pycropml/transpiler/antlr_py/grammars/Crop2MLComposition.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Crop2MLCompositionParser import Crop2MLCompositionParser
else:
    from Crop2MLCompositionParser import Crop2MLCompositionParser

# This class defines a complete generic visitor for a parse tree produced by Crop2MLCompositionParser.

class Crop2MLCompositionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Crop2MLCompositionParser#composition.
    def visitComposition(self, ctx:Crop2MLCompositionParser.CompositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#documentation.
    def visitDocumentation(self, ctx:Crop2MLCompositionParser.DocumentationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#statement.
    def visitStatement(self, ctx:Crop2MLCompositionParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#modelCall.
    def visitModelCall(self, ctx:Crop2MLCompositionParser.ModelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#modelInputAssignment.
    def visitModelInputAssignment(self, ctx:Crop2MLCompositionParser.ModelInputAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#compositionOutputAssignment.
    def visitCompositionOutputAssignment(self, ctx:Crop2MLCompositionParser.CompositionOutputAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#source.
    def visitSource(self, ctx:Crop2MLCompositionParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#modelPort.
    def visitModelPort(self, ctx:Crop2MLCompositionParser.ModelPortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#modelName.
    def visitModelName(self, ctx:Crop2MLCompositionParser.ModelNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#portName.
    def visitPortName(self, ctx:Crop2MLCompositionParser.PortNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Crop2MLCompositionParser#identifier.
    def visitIdentifier(self, ctx:Crop2MLCompositionParser.IdentifierContext):
        return self.visitChildren(ctx)



del Crop2MLCompositionParser