# Generated from CMake.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3")
        buf.write("\32\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5#\n\5\f\5\16\5")
        buf.write("&\13\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\4\2\5\6\b\t\2*\2")
        buf.write("\r\3\2\2\2\4\22\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n\f")
        buf.write("\5\4\3\2\13\n\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3")
        buf.write("\2\2\2\16\20\3\2\2\2\17\r\3\2\2\2\20\21\7\2\2\3\21\3\3")
        buf.write("\2\2\2\22\23\7\5\2\2\23\30\7\3\2\2\24\27\5\6\4\2\25\27")
        buf.write("\5\b\5\2\26\24\3\2\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2")
        buf.write("\33\34\7\4\2\2\34\5\3\2\2\2\35\36\t\2\2\2\36\7\3\2\2\2")
        buf.write("\37$\7\3\2\2 #\5\6\4\2!#\5\b\5\2\" \3\2\2\2\"!\3\2\2\2")
        buf.write("#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'")
        buf.write("(\7\4\2\2(\t\3\2\2\2\7\r\26\30\"$")
        return buf.getvalue()


class CMakeParser ( Parser ):

    grammarFileName = "CMake.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "Unquoted_argument", "Escape_sequence", "Quoted_argument", 
                      "Bracket_argument", "Bracket_comment", "Line_comment", 
                      "Newline", "Space" ]

    RULE_file_c = 0
    RULE_command_invocation = 1
    RULE_single_argument = 2
    RULE_compound_argument = 3

    ruleNames =  [ "file_c", "command_invocation", "single_argument", "compound_argument" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Identifier=3
    Unquoted_argument=4
    Escape_sequence=5
    Quoted_argument=6
    Bracket_argument=7
    Bracket_comment=8
    Line_comment=9
    Newline=10
    Space=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_cContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CMakeParser.EOF, 0)

        def command_invocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMakeParser.Command_invocationContext)
            else:
                return self.getTypedRuleContext(CMakeParser.Command_invocationContext,i)


        def getRuleIndex(self):
            return CMakeParser.RULE_file_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_c" ):
                listener.enterFile_c(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_c" ):
                listener.exitFile_c(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_c" ):
                return visitor.visitFile_c(self)
            else:
                return visitor.visitChildren(self)




    def file_c(self):

        localctx = CMakeParser.File_cContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_c)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CMakeParser.Identifier:
                self.state = 8
                self.command_invocation()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(CMakeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Command_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMakeParser.Identifier, 0)

        def single_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMakeParser.Single_argumentContext)
            else:
                return self.getTypedRuleContext(CMakeParser.Single_argumentContext,i)


        def compound_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMakeParser.Compound_argumentContext)
            else:
                return self.getTypedRuleContext(CMakeParser.Compound_argumentContext,i)


        def getRuleIndex(self):
            return CMakeParser.RULE_command_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand_invocation" ):
                listener.enterCommand_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand_invocation" ):
                listener.exitCommand_invocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand_invocation" ):
                return visitor.visitCommand_invocation(self)
            else:
                return visitor.visitChildren(self)




    def command_invocation(self):

        localctx = CMakeParser.Command_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(CMakeParser.Identifier)
            self.state = 17
            self.match(CMakeParser.T__0)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CMakeParser.T__0) | (1 << CMakeParser.Identifier) | (1 << CMakeParser.Unquoted_argument) | (1 << CMakeParser.Quoted_argument) | (1 << CMakeParser.Bracket_argument))) != 0):
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CMakeParser.Identifier, CMakeParser.Unquoted_argument, CMakeParser.Quoted_argument, CMakeParser.Bracket_argument]:
                    self.state = 18
                    self.single_argument()
                    pass
                elif token in [CMakeParser.T__0]:
                    self.state = 19
                    self.compound_argument()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(CMakeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMakeParser.Identifier, 0)

        def Unquoted_argument(self):
            return self.getToken(CMakeParser.Unquoted_argument, 0)

        def Bracket_argument(self):
            return self.getToken(CMakeParser.Bracket_argument, 0)

        def Quoted_argument(self):
            return self.getToken(CMakeParser.Quoted_argument, 0)

        def getRuleIndex(self):
            return CMakeParser.RULE_single_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_argument" ):
                listener.enterSingle_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_argument" ):
                listener.exitSingle_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_argument" ):
                return visitor.visitSingle_argument(self)
            else:
                return visitor.visitChildren(self)




    def single_argument(self):

        localctx = CMakeParser.Single_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_single_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CMakeParser.Identifier) | (1 << CMakeParser.Unquoted_argument) | (1 << CMakeParser.Quoted_argument) | (1 << CMakeParser.Bracket_argument))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMakeParser.Single_argumentContext)
            else:
                return self.getTypedRuleContext(CMakeParser.Single_argumentContext,i)


        def compound_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMakeParser.Compound_argumentContext)
            else:
                return self.getTypedRuleContext(CMakeParser.Compound_argumentContext,i)


        def getRuleIndex(self):
            return CMakeParser.RULE_compound_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_argument" ):
                listener.enterCompound_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_argument" ):
                listener.exitCompound_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_argument" ):
                return visitor.visitCompound_argument(self)
            else:
                return visitor.visitChildren(self)




    def compound_argument(self):

        localctx = CMakeParser.Compound_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compound_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CMakeParser.T__0)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CMakeParser.T__0) | (1 << CMakeParser.Identifier) | (1 << CMakeParser.Unquoted_argument) | (1 << CMakeParser.Quoted_argument) | (1 << CMakeParser.Bracket_argument))) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CMakeParser.Identifier, CMakeParser.Unquoted_argument, CMakeParser.Quoted_argument, CMakeParser.Bracket_argument]:
                    self.state = 30
                    self.single_argument()
                    pass
                elif token in [CMakeParser.T__0]:
                    self.state = 31
                    self.compound_argument()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(CMakeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





