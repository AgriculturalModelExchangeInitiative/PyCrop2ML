# Generated from CMake.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMakeParser import CMakeParser
else:
    from CMakeParser import CMakeParser

# This class defines a complete generic visitor for a parse tree produced by CMakeParser.

class CMakeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CMakeParser#file_c.
    def visitFile_c(self, ctx:CMakeParser.File_cContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMakeParser#command_invocation.
    def visitCommand_invocation(self, ctx:CMakeParser.Command_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMakeParser#single_argument.
    def visitSingle_argument(self, ctx:CMakeParser.Single_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMakeParser#compound_argument.
    def visitCompound_argument(self, ctx:CMakeParser.Compound_argumentContext):
        return self.visitChildren(ctx)



del CMakeParser