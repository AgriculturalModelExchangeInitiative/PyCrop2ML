# Generated from gram\xml\XMLParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx:XMLParser.DocumentContext):
        pass

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx:XMLParser.DocumentContext):
        pass


    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx:XMLParser.PrologContext):
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx:XMLParser.PrologContext):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx:XMLParser.ElementContext):
        pass

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx:XMLParser.ElementContext):
        pass


    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx:XMLParser.ReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx:XMLParser.ReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx:XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx:XMLParser.ChardataContext):
        pass


    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx:XMLParser.MiscContext):
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx:XMLParser.MiscContext):
        pass



del XMLParser