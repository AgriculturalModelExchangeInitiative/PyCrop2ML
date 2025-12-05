# Generated from CSharpPreprocessorParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSharpPreprocessorParser import CSharpPreprocessorParser
else:
    from CSharpPreprocessorParser import CSharpPreprocessorParser

# This class defines a complete generic visitor for a parse tree produced by CSharpPreprocessorParser.

class CSharpPreprocessorParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorDeclaration.
    def visitPreprocessorDeclaration(self, ctx:CSharpPreprocessorParser.PreprocessorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorConditional.
    def visitPreprocessorConditional(self, ctx:CSharpPreprocessorParser.PreprocessorConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorLine.
    def visitPreprocessorLine(self, ctx:CSharpPreprocessorParser.PreprocessorLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorDiagnostic.
    def visitPreprocessorDiagnostic(self, ctx:CSharpPreprocessorParser.PreprocessorDiagnosticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorRegion.
    def visitPreprocessorRegion(self, ctx:CSharpPreprocessorParser.PreprocessorRegionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorPragma.
    def visitPreprocessorPragma(self, ctx:CSharpPreprocessorParser.PreprocessorPragmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessorNullable.
    def visitPreprocessorNullable(self, ctx:CSharpPreprocessorParser.PreprocessorNullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#directive_new_line_or_sharp.
    def visitDirective_new_line_or_sharp(self, ctx:CSharpPreprocessorParser.Directive_new_line_or_sharpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpPreprocessorParser#preprocessor_expression.
    def visitPreprocessor_expression(self, ctx:CSharpPreprocessorParser.Preprocessor_expressionContext):
        return self.visitChildren(ctx)



del CSharpPreprocessorParser