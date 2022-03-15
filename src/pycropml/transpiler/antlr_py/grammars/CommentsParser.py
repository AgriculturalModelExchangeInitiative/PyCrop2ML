# Generated from Comments.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\26\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\3\6")
        buf.write("\3\17\n\3\r\3\16\3\20\3\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2")
        buf.write("\2\23\2\b\3\2\2\2\4\16\3\2\2\2\6\22\3\2\2\2\b\t\7\3\2")
        buf.write("\2\t\n\5\4\3\2\n\13\7\4\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r")
        buf.write("\17\5\6\4\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2\20")
        buf.write("\21\3\2\2\2\21\5\3\2\2\2\22\23\7\6\2\2\23\24\7\5\2\2\24")
        buf.write("\7\3\2\2\2\3\20")
        return buf.getvalue()


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
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentationContext(ParserRuleContext):

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
                if not (_la==CommentsParser.Symbol):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comment_lineContext(ParserRuleContext):

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





