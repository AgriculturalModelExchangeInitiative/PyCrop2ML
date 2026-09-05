# Generated from RFilter.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if "." in __name__:
    from .RFilterBase import RFilterBase
else:
    from RFilterBase import RFilterBase

def serializedATN():
    return [
        4,1,50,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,4,1,23,8,1,11,1,12,1,24,
        1,2,1,2,3,2,29,8,2,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,1,2,1,2,5,2,40,
        8,2,10,2,12,2,43,9,2,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,
        9,2,1,2,1,2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,1,2,1,2,1,2,
        5,2,68,8,2,10,2,12,2,71,9,2,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,1,2,5,
        2,81,8,2,10,2,12,2,84,9,2,1,2,1,2,3,2,88,8,2,1,2,1,2,3,2,92,8,2,
        1,2,1,2,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,2,1,2,3,2,104,8,2,1,2,
        1,2,3,2,108,8,2,1,2,1,2,1,2,5,2,113,8,2,10,2,12,2,116,9,2,1,2,1,
        2,3,2,120,8,2,1,2,1,2,3,2,124,8,2,1,2,1,2,1,2,5,2,129,8,2,10,2,12,
        2,132,9,2,1,2,1,2,3,2,136,8,2,1,2,1,2,3,2,140,8,2,1,3,1,3,1,4,1,
        4,1,4,0,0,5,0,2,4,6,8,0,2,2,0,20,27,41,46,6,0,1,4,9,9,12,12,17,19,
        28,36,47,47,181,0,15,1,0,0,0,2,22,1,0,0,0,4,139,1,0,0,0,6,141,1,
        0,0,0,8,143,1,0,0,0,10,14,3,4,2,0,11,14,5,48,0,0,12,14,5,49,0,0,
        13,10,1,0,0,0,13,11,1,0,0,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,
        0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,
        1,1,0,0,0,20,21,5,48,0,0,21,23,6,1,-1,0,22,20,1,0,0,0,23,24,1,0,
        0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,28,3,8,4,0,27,29,
        3,2,1,0,28,27,1,0,0,0,28,29,1,0,0,0,29,140,1,0,0,0,30,140,3,6,3,
        0,31,33,5,39,0,0,32,34,3,2,1,0,33,32,1,0,0,0,33,34,1,0,0,0,34,35,
        1,0,0,0,35,41,6,2,-1,0,36,40,3,4,2,0,37,40,5,48,0,0,38,40,5,49,0,
        0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,
        1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,6,2,-1,0,
        45,140,5,40,0,0,46,51,5,37,0,0,47,50,3,4,2,0,48,50,3,2,1,0,49,47,
        1,0,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,
        52,54,1,0,0,0,53,51,1,0,0,0,54,140,5,38,0,0,55,60,5,15,0,0,56,59,
        3,4,2,0,57,59,3,2,1,0,58,56,1,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,
        60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,140,5,
        16,0,0,64,69,5,13,0,0,65,68,3,4,2,0,66,68,3,2,1,0,67,65,1,0,0,0,
        67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,
        0,0,0,71,69,1,0,0,0,72,140,5,14,0,0,73,75,5,10,0,0,74,76,3,2,1,0,
        75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,82,5,37,0,0,78,81,3,
        4,2,0,79,81,3,2,1,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,
        80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,87,5,38,
        0,0,86,88,3,2,1,0,87,86,1,0,0,0,87,88,1,0,0,0,88,140,1,0,0,0,89,
        91,5,7,0,0,90,92,3,2,1,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,
        0,93,98,5,37,0,0,94,97,3,4,2,0,95,97,3,2,1,0,96,94,1,0,0,0,96,95,
        1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,
        0,100,98,1,0,0,0,101,103,5,38,0,0,102,104,3,2,1,0,103,102,1,0,0,
        0,103,104,1,0,0,0,104,140,1,0,0,0,105,107,5,8,0,0,106,108,3,2,1,
        0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,114,5,37,0,
        0,110,113,3,4,2,0,111,113,3,2,1,0,112,110,1,0,0,0,112,111,1,0,0,
        0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,
        0,116,114,1,0,0,0,117,119,5,38,0,0,118,120,3,2,1,0,119,118,1,0,0,
        0,119,120,1,0,0,0,120,140,1,0,0,0,121,123,5,6,0,0,122,124,3,2,1,
        0,123,122,1,0,0,0,123,124,1,0,0,0,124,125,1,0,0,0,125,130,5,37,0,
        0,126,129,3,4,2,0,127,129,3,2,1,0,128,126,1,0,0,0,128,127,1,0,0,
        0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,
        0,132,130,1,0,0,0,133,135,5,38,0,0,134,136,3,2,1,0,135,134,1,0,0,
        0,135,136,1,0,0,0,136,140,1,0,0,0,137,138,5,11,0,0,138,140,6,2,-1,
        0,139,26,1,0,0,0,139,30,1,0,0,0,139,31,1,0,0,0,139,46,1,0,0,0,139,
        55,1,0,0,0,139,64,1,0,0,0,139,73,1,0,0,0,139,89,1,0,0,0,139,105,
        1,0,0,0,139,121,1,0,0,0,139,137,1,0,0,0,140,5,1,0,0,0,141,142,7,
        0,0,0,142,7,1,0,0,0,143,144,7,1,0,0,144,9,1,0,0,0,30,13,15,24,28,
        33,39,41,49,51,58,60,67,69,75,80,82,87,91,96,98,103,107,112,114,
        119,123,128,130,135,139
    ]

class RFilter ( RFilterBase ):

    grammarFileName = "RFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'~'", "','", "'...'", "'.'", "'if'", 
                     "'for'", "'while'", "'repeat'", "'function'", "'else'", 
                     "'in'", "'[['", "']]'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "'?'", "'next'", "'break'", "'NULL'", 
                     "'NA'", "'inf'", "'NaN'", "'TRUE'", "'FALSE'", "'!'", 
                     "':'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "<INVALID>", "<INVALID>", "'('", "')'", "'{'", 
                     "'}'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "FOR", "WHILE", "REPEAT", 
                      "FUNCTION", "ELSE", "IN", "LIST_ACCESS_START", "LIST_ACCESS_END", 
                      "ARRAY_ACCESS_START", "ARRAY_ACCESS_END", "NAMESPACE_ACCESS", 
                      "COMPONENT_ACCESS", "HELP", "NEXT", "BREAK", "NULL", 
                      "NA", "INF", "NAN", "TRUE", "FALSE", "NOT", "RANGE_OPERATOR", 
                      "MULT_DIV", "ADD_SUB", "COMPARATOR", "ASSIGN", "EQUALS", 
                      "AND", "OR", "PAREN_L", "PAREN_R", "CURLY_L", "CURLY_R", 
                      "HEX", "INT", "FLOAT", "COMPLEX", "STRING", "ID", 
                      "USER_OP", "NL", "SEMICOLON", "WS" ]

    RULE_stream = 0
    RULE_eat = 1
    RULE_elem = 2
    RULE_atom = 3
    RULE_op = 4

    ruleNames =  [ "stream", "eat", "elem", "atom", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IF=6
    FOR=7
    WHILE=8
    REPEAT=9
    FUNCTION=10
    ELSE=11
    IN=12
    LIST_ACCESS_START=13
    LIST_ACCESS_END=14
    ARRAY_ACCESS_START=15
    ARRAY_ACCESS_END=16
    NAMESPACE_ACCESS=17
    COMPONENT_ACCESS=18
    HELP=19
    NEXT=20
    BREAK=21
    NULL=22
    NA=23
    INF=24
    NAN=25
    TRUE=26
    FALSE=27
    NOT=28
    RANGE_OPERATOR=29
    MULT_DIV=30
    ADD_SUB=31
    COMPARATOR=32
    ASSIGN=33
    EQUALS=34
    AND=35
    OR=36
    PAREN_L=37
    PAREN_R=38
    CURLY_L=39
    CURLY_R=40
    HEX=41
    INT=42
    FLOAT=43
    COMPLEX=44
    STRING=45
    ID=46
    USER_OP=47
    NL=48
    SEMICOLON=49
    WS=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StreamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RFilter.EOF, 0)

        def elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RFilter.ElemContext)
            else:
                return self.getTypedRuleContext(RFilter.ElemContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RFilter.NL)
            else:
                return self.getToken(RFilter.NL, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(RFilter.SEMICOLON)
            else:
                return self.getToken(RFilter.SEMICOLON, i)

        def getRuleIndex(self):
            return RFilter.RULE_stream

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStream" ):
                listener.enterStream(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStream" ):
                listener.exitStream(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStream" ):
                return visitor.visitStream(self)
            else:
                return visitor.visitChildren(self)




    def stream(self):

        localctx = RFilter.StreamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124525517225950) != 0):
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                    self.state = 10
                    self.elem()
                    pass
                elif token in [48]:
                    self.state = 11
                    self.match(RFilter.NL)
                    pass
                elif token in [49]:
                    self.state = 12
                    self.match(RFilter.SEMICOLON)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(RFilter.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NL = None # Token

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RFilter.NL)
            else:
                return self.getToken(RFilter.NL, i)

        def getRuleIndex(self):
            return RFilter.RULE_eat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEat" ):
                listener.enterEat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEat" ):
                listener.exitEat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEat" ):
                return visitor.visitEat(self)
            else:
                return visitor.visitChildren(self)




    def eat(self):

        localctx = RFilter.EatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_eat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 20
                    localctx._NL = self.match(RFilter.NL)
                    self.hideToken(localctx._NL)

                else:
                    raise NoViableAltException(self)
                self.state = 24 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(RFilter.OpContext,0)


        def eat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RFilter.EatContext)
            else:
                return self.getTypedRuleContext(RFilter.EatContext,i)


        def atom(self):
            return self.getTypedRuleContext(RFilter.AtomContext,0)


        def CURLY_L(self):
            return self.getToken(RFilter.CURLY_L, 0)

        def CURLY_R(self):
            return self.getToken(RFilter.CURLY_R, 0)

        def elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RFilter.ElemContext)
            else:
                return self.getTypedRuleContext(RFilter.ElemContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RFilter.NL)
            else:
                return self.getToken(RFilter.NL, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(RFilter.SEMICOLON)
            else:
                return self.getToken(RFilter.SEMICOLON, i)

        def PAREN_L(self):
            return self.getToken(RFilter.PAREN_L, 0)

        def PAREN_R(self):
            return self.getToken(RFilter.PAREN_R, 0)

        def ARRAY_ACCESS_START(self):
            return self.getToken(RFilter.ARRAY_ACCESS_START, 0)

        def ARRAY_ACCESS_END(self):
            return self.getToken(RFilter.ARRAY_ACCESS_END, 0)

        def LIST_ACCESS_START(self):
            return self.getToken(RFilter.LIST_ACCESS_START, 0)

        def LIST_ACCESS_END(self):
            return self.getToken(RFilter.LIST_ACCESS_END, 0)

        def FUNCTION(self):
            return self.getToken(RFilter.FUNCTION, 0)

        def FOR(self):
            return self.getToken(RFilter.FOR, 0)

        def WHILE(self):
            return self.getToken(RFilter.WHILE, 0)

        def IF(self):
            return self.getToken(RFilter.IF, 0)

        def ELSE(self):
            return self.getToken(RFilter.ELSE, 0)

        def getRuleIndex(self):
            return RFilter.RULE_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElem" ):
                listener.enterElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElem" ):
                listener.exitElem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = RFilter.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 9, 12, 17, 18, 19, 28, 29, 30, 31, 32, 33, 34, 35, 36, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.op()
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 27
                    self.eat()


                pass
            elif token in [20, 21, 22, 23, 24, 25, 26, 27, 41, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.atom()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(RFilter.CURLY_L)
                self.state = 33
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.eat()


                self.curlies += 1
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124525517225950) != 0):
                    self.state = 39
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 36
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 37
                        self.match(RFilter.NL)
                        pass
                    elif token in [49]:
                        self.state = 38
                        self.match(RFilter.SEMICOLON)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.curlies -= 1
                self.state = 45
                self.match(RFilter.CURLY_R)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(RFilter.PAREN_L)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 49
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 47
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 48
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 54
                self.match(RFilter.PAREN_R)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.match(RFilter.ARRAY_ACCESS_START)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 58
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 56
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 57
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self.match(RFilter.ARRAY_ACCESS_END)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.match(RFilter.LIST_ACCESS_START)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 67
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 65
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 66
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(RFilter.LIST_ACCESS_END)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 73
                self.match(RFilter.FUNCTION)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 74
                    self.eat()


                self.state = 77
                self.match(RFilter.PAREN_L)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 80
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 78
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 79
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self.match(RFilter.PAREN_R)
                self.state = 87
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 86
                    self.eat()


                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.match(RFilter.FOR)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 90
                    self.eat()


                self.state = 93
                self.match(RFilter.PAREN_L)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 96
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 94
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 95
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self.match(RFilter.PAREN_R)
                self.state = 103
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.eat()


                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 105
                self.match(RFilter.WHILE)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 106
                    self.eat()


                self.state = 109
                self.match(RFilter.PAREN_L)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 112
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 110
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 111
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 117
                self.match(RFilter.PAREN_R)
                self.state = 119
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self.eat()


                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 10)
                self.state = 121
                self.match(RFilter.IF)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 122
                    self.eat()


                self.state = 125
                self.match(RFilter.PAREN_L)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 561575563804638) != 0):
                    self.state = 128
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47]:
                        self.state = 126
                        self.elem()
                        pass
                    elif token in [48]:
                        self.state = 127
                        self.eat()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 133
                self.match(RFilter.PAREN_R)
                self.state = 135
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 134
                    self.eat()


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 11)
                self.state = 137
                self.match(RFilter.ELSE)

                tok = self._input.LT(-2)
                if self.curlies > 0 and tok.type == self.NL:
                    self.hideToken(tok)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEXT(self):
            return self.getToken(RFilter.NEXT, 0)

        def BREAK(self):
            return self.getToken(RFilter.BREAK, 0)

        def ID(self):
            return self.getToken(RFilter.ID, 0)

        def STRING(self):
            return self.getToken(RFilter.STRING, 0)

        def HEX(self):
            return self.getToken(RFilter.HEX, 0)

        def INT(self):
            return self.getToken(RFilter.INT, 0)

        def FLOAT(self):
            return self.getToken(RFilter.FLOAT, 0)

        def COMPLEX(self):
            return self.getToken(RFilter.COMPLEX, 0)

        def NULL(self):
            return self.getToken(RFilter.NULL, 0)

        def NA(self):
            return self.getToken(RFilter.NA, 0)

        def INF(self):
            return self.getToken(RFilter.INF, 0)

        def NAN(self):
            return self.getToken(RFilter.NAN, 0)

        def TRUE(self):
            return self.getToken(RFilter.TRUE, 0)

        def FALSE(self):
            return self.getToken(RFilter.FALSE, 0)

        def getRuleIndex(self):
            return RFilter.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RFilter.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138538732486656) != 0)):
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


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_SUB(self):
            return self.getToken(RFilter.ADD_SUB, 0)

        def MULT_DIV(self):
            return self.getToken(RFilter.MULT_DIV, 0)

        def COMPARATOR(self):
            return self.getToken(RFilter.COMPARATOR, 0)

        def AND(self):
            return self.getToken(RFilter.AND, 0)

        def USER_OP(self):
            return self.getToken(RFilter.USER_OP, 0)

        def REPEAT(self):
            return self.getToken(RFilter.REPEAT, 0)

        def IN(self):
            return self.getToken(RFilter.IN, 0)

        def HELP(self):
            return self.getToken(RFilter.HELP, 0)

        def NOT(self):
            return self.getToken(RFilter.NOT, 0)

        def EQUALS(self):
            return self.getToken(RFilter.EQUALS, 0)

        def RANGE_OPERATOR(self):
            return self.getToken(RFilter.RANGE_OPERATOR, 0)

        def COMPONENT_ACCESS(self):
            return self.getToken(RFilter.COMPONENT_ACCESS, 0)

        def ASSIGN(self):
            return self.getToken(RFilter.ASSIGN, 0)

        def NAMESPACE_ACCESS(self):
            return self.getToken(RFilter.NAMESPACE_ACCESS, 0)

        def OR(self):
            return self.getToken(RFilter.OR, 0)

        def getRuleIndex(self):
            return RFilter.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = RFilter.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140874659795486) != 0)):
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





