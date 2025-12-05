# Generated from Comments.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CommentsParser import CommentsParser
else:
    from CommentsParser import CommentsParser

# This class defines a complete generic visitor for a parse tree produced by CommentsParser.

class CommentsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommentsParser#documentation.
    def visitDocumentation(self, ctx:CommentsParser.DocumentationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommentsParser#documentationContent.
    def visitDocumentationContent(self, ctx:CommentsParser.DocumentationContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommentsParser#comment_line.
    def visitComment_line(self, ctx:CommentsParser.Comment_lineContext):
        return self.visitChildren(ctx)



del CommentsParser