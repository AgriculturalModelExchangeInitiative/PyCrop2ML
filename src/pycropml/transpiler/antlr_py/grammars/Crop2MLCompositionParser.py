# Generated from src/pycropml/transpiler/antlr_py/grammars/Crop2MLComposition.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\2\3\2\6\2!\n\2\r\2\16\2\"\3\2\3\2")
        buf.write("\6\2\'\n\2\r\2\16\2(\7\2+\n\2\f\2\16\2.\13\2\3\2\5\2\61")
        buf.write("\n\2\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\5\4@\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\5\bP\n\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\2\2Y\2\33\3\2\2\2\4:\3\2\2\2\6?\3\2\2\2\bA\3\2\2")
        buf.write("\2\nE\3\2\2\2\fI\3\2\2\2\16O\3\2\2\2\20Q\3\2\2\2\22U\3")
        buf.write("\2\2\2\24W\3\2\2\2\26Y\3\2\2\2\30\32\7\13\2\2\31\30\3")
        buf.write("\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\36")
        buf.write("\3\2\2\2\35\33\3\2\2\2\36 \5\4\3\2\37!\7\13\2\2 \37\3")
        buf.write("\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#,\3\2\2\2$&\5")
        buf.write("\6\4\2%\'\7\13\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3")
        buf.write("\2\2\2)+\3\2\2\2*$\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2")
        buf.write("\2-\60\3\2\2\2.,\3\2\2\2/\61\5\6\4\2\60/\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61\65\3\2\2\2\62\64\7\13\2\2\63\62\3\2\2\2\64")
        buf.write("\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67")
        buf.write("\65\3\2\2\289\7\2\2\39\3\3\2\2\2:;\7\7\2\2;\5\3\2\2\2")
        buf.write("<@\5\b\5\2=@\5\n\6\2>@\5\f\7\2?<\3\2\2\2?=\3\2\2\2?>\3")
        buf.write("\2\2\2@\7\3\2\2\2AB\5\22\n\2BC\7\3\2\2CD\7\4\2\2D\t\3")
        buf.write("\2\2\2EF\5\20\t\2FG\7\6\2\2GH\5\16\b\2H\13\3\2\2\2IJ\5")
        buf.write("\26\f\2JK\7\6\2\2KL\5\20\t\2L\r\3\2\2\2MP\5\26\f\2NP\5")
        buf.write("\20\t\2OM\3\2\2\2ON\3\2\2\2P\17\3\2\2\2QR\5\22\n\2RS\7")
        buf.write("\5\2\2ST\5\24\13\2T\21\3\2\2\2UV\5\26\f\2V\23\3\2\2\2")
        buf.write("WX\5\26\f\2X\25\3\2\2\2YZ\7\b\2\2Z\27\3\2\2\2\n\33\"(")
        buf.write(",\60\65?O")
        return buf.getvalue()


class Crop2MLCompositionParser ( Parser ):

    grammarFileName = "Crop2MLComposition.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "DOT", "ASSIGN", 
                      "DOCSTRING", "IDENTIFIER", "LINE_CONTINUATION", "COMMENT", 
                      "NEWLINE", "WS" ]

    RULE_composition = 0
    RULE_documentation = 1
    RULE_statement = 2
    RULE_modelCall = 3
    RULE_modelInputAssignment = 4
    RULE_compositionOutputAssignment = 5
    RULE_source = 6
    RULE_modelPort = 7
    RULE_modelName = 8
    RULE_portName = 9
    RULE_identifier = 10

    ruleNames =  [ "composition", "documentation", "statement", "modelCall", 
                   "modelInputAssignment", "compositionOutputAssignment", 
                   "source", "modelPort", "modelName", "portName", "identifier" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    DOT=3
    ASSIGN=4
    DOCSTRING=5
    IDENTIFIER=6
    LINE_CONTINUATION=7
    COMMENT=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompositionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def documentation(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.DocumentationContext,0)


        def EOF(self):
            return self.getToken(Crop2MLCompositionParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Crop2MLCompositionParser.NEWLINE)
            else:
                return self.getToken(Crop2MLCompositionParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Crop2MLCompositionParser.StatementContext)
            else:
                return self.getTypedRuleContext(Crop2MLCompositionParser.StatementContext,i)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_composition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposition" ):
                listener.enterComposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposition" ):
                listener.exitComposition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposition" ):
                return visitor.visitComposition(self)
            else:
                return visitor.visitChildren(self)




    def composition(self):

        localctx = Crop2MLCompositionParser.CompositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_composition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Crop2MLCompositionParser.NEWLINE:
                self.state = 22
                self.match(Crop2MLCompositionParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.documentation()
            self.state = 30 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 29
                    self.match(Crop2MLCompositionParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.statement()
                    self.state = 36 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 35
                            self.match(Crop2MLCompositionParser.NEWLINE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 38 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Crop2MLCompositionParser.IDENTIFIER:
                self.state = 45
                self.statement()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Crop2MLCompositionParser.NEWLINE:
                self.state = 48
                self.match(Crop2MLCompositionParser.NEWLINE)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(Crop2MLCompositionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOCSTRING(self):
            return self.getToken(Crop2MLCompositionParser.DOCSTRING, 0)

        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_documentation

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

        localctx = Crop2MLCompositionParser.DocumentationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_documentation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(Crop2MLCompositionParser.DOCSTRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelCall(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelCallContext,0)


        def modelInputAssignment(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelInputAssignmentContext,0)


        def compositionOutputAssignment(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.CompositionOutputAssignmentContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Crop2MLCompositionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.modelCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.modelInputAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.compositionOutputAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelName(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelNameContext,0)


        def LPAREN(self):
            return self.getToken(Crop2MLCompositionParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Crop2MLCompositionParser.RPAREN, 0)

        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_modelCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelCall" ):
                listener.enterModelCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelCall" ):
                listener.exitModelCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelCall" ):
                return visitor.visitModelCall(self)
            else:
                return visitor.visitChildren(self)




    def modelCall(self):

        localctx = Crop2MLCompositionParser.ModelCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modelCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.modelName()
            self.state = 64
            self.match(Crop2MLCompositionParser.LPAREN)
            self.state = 65
            self.match(Crop2MLCompositionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelInputAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelPort(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelPortContext,0)


        def ASSIGN(self):
            return self.getToken(Crop2MLCompositionParser.ASSIGN, 0)

        def source(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.SourceContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_modelInputAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelInputAssignment" ):
                listener.enterModelInputAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelInputAssignment" ):
                listener.exitModelInputAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelInputAssignment" ):
                return visitor.visitModelInputAssignment(self)
            else:
                return visitor.visitChildren(self)




    def modelInputAssignment(self):

        localctx = Crop2MLCompositionParser.ModelInputAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_modelInputAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.modelPort()
            self.state = 68
            self.match(Crop2MLCompositionParser.ASSIGN)
            self.state = 69
            self.source()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositionOutputAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(Crop2MLCompositionParser.ASSIGN, 0)

        def modelPort(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelPortContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_compositionOutputAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompositionOutputAssignment" ):
                listener.enterCompositionOutputAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompositionOutputAssignment" ):
                listener.exitCompositionOutputAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositionOutputAssignment" ):
                return visitor.visitCompositionOutputAssignment(self)
            else:
                return visitor.visitChildren(self)




    def compositionOutputAssignment(self):

        localctx = Crop2MLCompositionParser.CompositionOutputAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compositionOutputAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.identifier()
            self.state = 72
            self.match(Crop2MLCompositionParser.ASSIGN)
            self.state = 73
            self.modelPort()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.IdentifierContext,0)


        def modelPort(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelPortContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = Crop2MLCompositionParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_source)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.modelPort()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelPortContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelName(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.ModelNameContext,0)


        def DOT(self):
            return self.getToken(Crop2MLCompositionParser.DOT, 0)

        def portName(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.PortNameContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_modelPort

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelPort" ):
                listener.enterModelPort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelPort" ):
                listener.exitModelPort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelPort" ):
                return visitor.visitModelPort(self)
            else:
                return visitor.visitChildren(self)




    def modelPort(self):

        localctx = Crop2MLCompositionParser.ModelPortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_modelPort)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.modelName()
            self.state = 80
            self.match(Crop2MLCompositionParser.DOT)
            self.state = 81
            self.portName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.IdentifierContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_modelName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelName" ):
                listener.enterModelName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelName" ):
                listener.exitModelName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelName" ):
                return visitor.visitModelName(self)
            else:
                return visitor.visitChildren(self)




    def modelName(self):

        localctx = Crop2MLCompositionParser.ModelNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_modelName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PortNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Crop2MLCompositionParser.IdentifierContext,0)


        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_portName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPortName" ):
                listener.enterPortName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPortName" ):
                listener.exitPortName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPortName" ):
                return visitor.visitPortName(self)
            else:
                return visitor.visitChildren(self)




    def portName(self):

        localctx = Crop2MLCompositionParser.PortNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_portName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Crop2MLCompositionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Crop2MLCompositionParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = Crop2MLCompositionParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(Crop2MLCompositionParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





