# Generated from Comments.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommentsParser import CommentsParser
else:
    from CommentsParser import CommentsParser

# This class defines a complete listener for a parse tree produced by CommentsParser.
class CommentsListener(ParseTreeListener):

    # Enter a parse tree produced by CommentsParser#documentation.
    def enterDocumentation(self, ctx:CommentsParser.DocumentationContext):
        pass

    # Exit a parse tree produced by CommentsParser#documentation.
    def exitDocumentation(self, ctx:CommentsParser.DocumentationContext):
        pass


    # Enter a parse tree produced by CommentsParser#documentationContent.
    def enterDocumentationContent(self, ctx:CommentsParser.DocumentationContentContext):
        pass

    # Exit a parse tree produced by CommentsParser#documentationContent.
    def exitDocumentationContent(self, ctx:CommentsParser.DocumentationContentContext):
        pass


    # Enter a parse tree produced by CommentsParser#comment_line.
    def enterComment_line(self, ctx:CommentsParser.Comment_lineContext):
        pass

    # Exit a parse tree produced by CommentsParser#comment_line.
    def exitComment_line(self, ctx:CommentsParser.Comment_lineContext):
        pass



del CommentsParser