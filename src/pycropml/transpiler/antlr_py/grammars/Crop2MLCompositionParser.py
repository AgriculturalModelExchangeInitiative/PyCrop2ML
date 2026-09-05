# Generated from Crop2MLComposition.g4 by ANTLR 4.13.2
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
        4,1,10,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,4,0,31,8,0,11,0,12,0,32,1,0,1,0,4,0,37,8,0,11,0,12,0,
        38,5,0,41,8,0,10,0,12,0,44,9,0,1,0,3,0,47,8,0,1,0,5,0,50,8,0,10,
        0,12,0,53,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,3,6,78,8,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,
        18,20,0,0,87,0,25,1,0,0,0,2,56,1,0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,
        8,67,1,0,0,0,10,71,1,0,0,0,12,77,1,0,0,0,14,79,1,0,0,0,16,83,1,0,
        0,0,18,85,1,0,0,0,20,87,1,0,0,0,22,24,5,9,0,0,23,22,1,0,0,0,24,27,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,
        28,30,3,2,1,0,29,31,5,9,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,
        0,0,0,32,33,1,0,0,0,33,42,1,0,0,0,34,36,3,4,2,0,35,37,5,9,0,0,36,
        35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,
        0,40,34,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,46,47,1,0,0,0,
        47,51,1,0,0,0,48,50,5,9,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,
        1,1,0,0,0,56,57,5,5,0,0,57,3,1,0,0,0,58,62,3,6,3,0,59,62,3,8,4,0,
        60,62,3,10,5,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,5,1,
        0,0,0,63,64,3,16,8,0,64,65,5,1,0,0,65,66,5,2,0,0,66,7,1,0,0,0,67,
        68,3,14,7,0,68,69,5,4,0,0,69,70,3,12,6,0,70,9,1,0,0,0,71,72,3,20,
        10,0,72,73,5,4,0,0,73,74,3,14,7,0,74,11,1,0,0,0,75,78,3,20,10,0,
        76,78,3,14,7,0,77,75,1,0,0,0,77,76,1,0,0,0,78,13,1,0,0,0,79,80,3,
        16,8,0,80,81,5,3,0,0,81,82,3,18,9,0,82,15,1,0,0,0,83,84,3,20,10,
        0,84,17,1,0,0,0,85,86,3,20,10,0,86,19,1,0,0,0,87,88,5,6,0,0,88,21,
        1,0,0,0,8,25,32,38,42,46,51,61,77
    ]

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
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompositionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            while _la==9:
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
            if _la==6:
                self.state = 45
                self.statement()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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





