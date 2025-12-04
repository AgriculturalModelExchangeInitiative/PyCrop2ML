# Generated from Comments.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\7\4F\n\4\f\4\16\4I\13\4\3\5\3\5\3\5\5\5N\n\5\3\6\3\6")
        buf.write("\3\6\5\6S\n\6\3\7\3\7\3\b\6\bX\n\b\r\b\16\bY\3\t\6\t]")
        buf.write("\n\t\r\t\16\t^\3\t\5\tb\n\t\3\t\3\t\2\2\n\3\3\5\4\7\5")
        buf.write("\t\6\13\2\r\2\17\2\21\7\3\2\7\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\4\2##%%\4\2\f\f\17\17\4\2\13\13\"\"\2g\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\21\3\2\2\2\3\23")
        buf.write("\3\2\2\2\5,\3\2\2\2\7C\3\2\2\2\tM\3\2\2\2\13R\3\2\2\2")
        buf.write("\rT\3\2\2\2\17W\3\2\2\2\21a\3\2\2\2\23\24\7#\2\2\24\25")
        buf.write("\7\'\2\2\25\26\7\'\2\2\26\27\7E\2\2\27\30\7{\2\2\30\31")
        buf.write("\7o\2\2\31\32\7n\2\2\32\33\7\"\2\2\33\34\7E\2\2\34\35")
        buf.write("\7q\2\2\35\36\7o\2\2\36\37\7o\2\2\37 \7g\2\2 !\7p\2\2")
        buf.write("!\"\7v\2\2\"#\7u\2\2#$\7\"\2\2$%\7D\2\2%&\7g\2\2&\'\7")
        buf.write("i\2\2\'(\7k\2\2()\7p\2\2)*\7\'\2\2*+\7\'\2\2+\4\3\2\2")
        buf.write("\2,-\7#\2\2-.\7\'\2\2./\7\'\2\2/\60\7E\2\2\60\61\7{\2")
        buf.write("\2\61\62\7o\2\2\62\63\7n\2\2\63\64\7\"\2\2\64\65\7E\2")
        buf.write("\2\65\66\7q\2\2\66\67\7o\2\2\678\7o\2\289\7g\2\29:\7p")
        buf.write("\2\2:;\7v\2\2;<\7u\2\2<=\7\"\2\2=>\7G\2\2>?\7p\2\2?@\7")
        buf.write("f\2\2@A\7\'\2\2AB\7\'\2\2B\6\3\2\2\2CG\t\2\2\2DF\t\3\2")
        buf.write("\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\b\3\2\2\2")
        buf.write("IG\3\2\2\2JN\t\4\2\2KL\7\61\2\2LN\7\61\2\2MJ\3\2\2\2M")
        buf.write("K\3\2\2\2N\n\3\2\2\2OP\7\17\2\2PS\7\f\2\2QS\t\5\2\2RO")
        buf.write("\3\2\2\2RQ\3\2\2\2S\f\3\2\2\2TU\4\62;\2U\16\3\2\2\2VX")
        buf.write("\t\6\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\20\3")
        buf.write("\2\2\2[]\5\17\b\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3")
        buf.write("\2\2\2_b\3\2\2\2`b\5\13\6\2a\\\3\2\2\2a`\3\2\2\2bc\3\2")
        buf.write("\2\2cd\b\t\2\2d\22\3\2\2\2\t\2GMRY^a\3\b\2\2")
        return buf.getvalue()


class CommentsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Identifier = 3
    Symbol = 4
    Ws = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'!%%Cyml Comments Begin%%'", "'!%%Cyml Comments End%%'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "Symbol", "Ws" ]

    ruleNames = [ "T__0", "T__1", "Identifier", "Symbol", "Newline", "Num", 
                  "Space", "Ws" ]

    grammarFileName = "Comments.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


