# Generated from Comments.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,1,4,1,13,
        8,1,11,1,12,1,14,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,17,0,6,1,0,0,0,
        2,12,1,0,0,0,4,16,1,0,0,0,6,7,5,1,0,0,7,8,3,2,1,0,8,9,5,2,0,0,9,
        10,5,0,0,1,10,1,1,0,0,0,11,13,3,4,2,0,12,11,1,0,0,0,13,14,1,0,0,
        0,14,12,1,0,0,0,14,15,1,0,0,0,15,3,1,0,0,0,16,17,5,4,0,0,17,18,5,
        3,0,0,18,5,1,0,0,0,1,14
    ]

class CommentsParser ( Parser ):

    grammarFileName = "Comments.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!%%Cyml Comments Begin%%'", "'!%%Cyml Comments End%%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "Symbol", "Ws" ]

    RULE_documentation = 0
    RULE_documentationContent = 1
    RULE_comment_line = 2

    ruleNames =  [ "documentation", "documentationContent", "comment_line" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Identifier=3
    Symbol=4
    Ws=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def documentationContent(self):
            return self.getTypedRuleContext(CommentsParser.DocumentationContentContext,0)


        def EOF(self):
            return self.getToken(CommentsParser.EOF, 0)

        def getRuleIndex(self):
            return CommentsParser.RULE_documentation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocumentation" ):
                listener.enterDocumentation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocumentation" ):
                listener.exitDocumentation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocumentation" ):
                return visitor.visitDocumentation(self)
            else:
                return visitor.visitChildren(self)




    def documentation(self):

        localctx = CommentsParser.DocumentationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_documentation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(CommentsParser.T__0)
            self.state = 7
            self.documentationContent()
            self.state = 8
            self.match(CommentsParser.T__1)
            self.state = 9
            self.match(CommentsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentationContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommentsParser.Comment_lineContext)
            else:
                return self.getTypedRuleContext(CommentsParser.Comment_lineContext,i)


        def getRuleIndex(self):
            return CommentsParser.RULE_documentationContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocumentationContent" ):
                listener.enterDocumentationContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocumentationContent" ):
                listener.exitDocumentationContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocumentationContent" ):
                return visitor.visitDocumentationContent(self)
            else:
                return visitor.visitChildren(self)




    def documentationContent(self):

        localctx = CommentsParser.DocumentationContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_documentationContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.comment_line()
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comment_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Symbol(self):
            return self.getToken(CommentsParser.Symbol, 0)

        def Identifier(self):
            return self.getToken(CommentsParser.Identifier, 0)

        def getRuleIndex(self):
            return CommentsParser.RULE_comment_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment_line" ):
                listener.enterComment_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment_line" ):
                listener.exitComment_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment_line" ):
                return visitor.visitComment_line(self)
            else:
                return visitor.visitChildren(self)




    def comment_line(self):

        localctx = CommentsParser.Comment_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(CommentsParser.Symbol)
            self.state = 17
            self.match(CommentsParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





