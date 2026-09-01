# Generated from src/pycropml/transpiler/antlr_py/grammars/Crop2MLComposition.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6%\n\6\f\6\16\6(\13")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\62\n\6\f\6\16\6")
        buf.write("\65\13\6\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\7\7>\n\7\f\7\16")
        buf.write("\7A\13\7\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\b\5\bK\n\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\7\tS\n\t\f\t\16\tV\13\t\3\t\3")
        buf.write("\t\3\n\5\n[\n\n\3\n\3\n\3\13\6\13`\n\13\r\13\16\13a\3")
        buf.write("\13\3\13\4&\63\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\4\2\13\13")
        buf.write("\"\"\4\2\f\f\17\17\2m\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5")
        buf.write("\31\3\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\139\3\2\2\2\r;\3")
        buf.write("\2\2\2\17B\3\2\2\2\21P\3\2\2\2\23Z\3\2\2\2\25_\3\2\2\2")
        buf.write("\27\30\7*\2\2\30\4\3\2\2\2\31\32\7+\2\2\32\6\3\2\2\2\33")
        buf.write("\34\7\60\2\2\34\b\3\2\2\2\35\36\7?\2\2\36\n\3\2\2\2\37")
        buf.write(" \7$\2\2 !\7$\2\2!\"\7$\2\2\"&\3\2\2\2#%\13\2\2\2$#\3")
        buf.write("\2\2\2%(\3\2\2\2&\'\3\2\2\2&$\3\2\2\2\')\3\2\2\2(&\3\2")
        buf.write("\2\2)*\7$\2\2*+\7$\2\2+:\7$\2\2,-\7)\2\2-.\7)\2\2./\7")
        buf.write(")\2\2/\63\3\2\2\2\60\62\13\2\2\2\61\60\3\2\2\2\62\65\3")
        buf.write("\2\2\2\63\64\3\2\2\2\63\61\3\2\2\2\64\66\3\2\2\2\65\63")
        buf.write("\3\2\2\2\66\67\7)\2\2\678\7)\2\28:\7)\2\29\37\3\2\2\2")
        buf.write("9,\3\2\2\2:\f\3\2\2\2;?\t\2\2\2<>\t\3\2\2=<\3\2\2\2>A")
        buf.write("\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\16\3\2\2\2A?\3\2\2\2BF\7")
        buf.write("^\2\2CE\t\4\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2")
        buf.write("\2GJ\3\2\2\2HF\3\2\2\2IK\7\17\2\2JI\3\2\2\2JK\3\2\2\2")
        buf.write("KL\3\2\2\2LM\7\f\2\2MN\3\2\2\2NO\b\b\2\2O\20\3\2\2\2P")
        buf.write("T\7%\2\2QS\n\5\2\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2UW\3\2\2\2VT\3\2\2\2WX\b\t\2\2X\22\3\2\2\2Y[\7\17")
        buf.write("\2\2ZY\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7\f\2\2]\24\3\2")
        buf.write("\2\2^`\t\4\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2")
        buf.write("bc\3\2\2\2cd\b\13\2\2d\26\3\2\2\2\f\2&\639?FJTZa\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class Crop2MLCompositionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    DOT = 3
    ASSIGN = 4
    DOCSTRING = 5
    IDENTIFIER = 6
    LINE_CONTINUATION = 7
    COMMENT = 8
    NEWLINE = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "DOT", "ASSIGN", "DOCSTRING", "IDENTIFIER", 
            "LINE_CONTINUATION", "COMMENT", "NEWLINE", "WS" ]

    ruleNames = [ "LPAREN", "RPAREN", "DOT", "ASSIGN", "DOCSTRING", "IDENTIFIER", 
                  "LINE_CONTINUATION", "COMMENT", "NEWLINE", "WS" ]

    grammarFileName = "Crop2MLComposition.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


