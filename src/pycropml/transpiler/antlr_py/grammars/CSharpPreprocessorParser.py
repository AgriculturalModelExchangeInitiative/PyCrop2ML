# Generated from CSharpPreprocessorParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if "." in __name__:
    from .CSharpPreprocessorParserBase import CSharpPreprocessorParserBase
else:
    from CSharpPreprocessorParserBase import CSharpPreprocessorParserBase

def serializedATN():
    return [
        4,1,198,128,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,38,8,0,1,0,1,0,3,0,42,8,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,59,
        8,0,1,0,1,0,1,0,1,0,1,0,3,0,66,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,81,8,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,101,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,2,0,1,4,3,0,2,4,0,1,1,1,196,
        196,149,0,80,1,0,0,0,2,82,1,0,0,0,4,100,1,0,0,0,6,7,5,183,0,0,7,
        8,5,195,0,0,8,9,3,2,1,0,9,10,6,0,-1,0,10,81,1,0,0,0,11,12,5,184,
        0,0,12,13,5,195,0,0,13,14,3,2,1,0,14,15,6,0,-1,0,15,81,1,0,0,0,16,
        17,5,52,0,0,17,18,3,4,2,0,18,19,3,2,1,0,19,20,6,0,-1,0,20,81,1,0,
        0,0,21,22,5,185,0,0,22,23,3,4,2,0,23,24,3,2,1,0,24,25,6,0,-1,0,25,
        81,1,0,0,0,26,27,5,36,0,0,27,28,3,2,1,0,28,29,6,0,-1,0,29,81,1,0,
        0,0,30,31,5,186,0,0,31,32,3,2,1,0,32,33,6,0,-1,0,33,81,1,0,0,0,34,
        41,5,187,0,0,35,37,5,182,0,0,36,38,5,91,0,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,42,1,0,0,0,39,42,5,30,0,0,40,42,5,194,0,0,41,35,1,0,0,
        0,41,39,1,0,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,44,3,2,1,0,44,45,
        6,0,-1,0,45,81,1,0,0,0,46,47,5,188,0,0,47,48,5,197,0,0,48,49,3,2,
        1,0,49,50,6,0,-1,0,50,81,1,0,0,0,51,52,5,189,0,0,52,53,5,197,0,0,
        53,54,3,2,1,0,54,55,6,0,-1,0,55,81,1,0,0,0,56,58,5,190,0,0,57,59,
        5,197,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,3,2,1,
        0,61,62,6,0,-1,0,62,81,1,0,0,0,63,65,5,191,0,0,64,66,5,197,0,0,65,
        64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,3,2,1,0,68,69,6,0,-1,
        0,69,81,1,0,0,0,70,71,5,192,0,0,71,72,5,197,0,0,72,73,3,2,1,0,73,
        74,6,0,-1,0,74,81,1,0,0,0,75,76,5,193,0,0,76,77,5,197,0,0,77,78,
        3,2,1,0,78,79,6,0,-1,0,79,81,1,0,0,0,80,6,1,0,0,0,80,11,1,0,0,0,
        80,16,1,0,0,0,80,21,1,0,0,0,80,26,1,0,0,0,80,30,1,0,0,0,80,34,1,
        0,0,0,80,46,1,0,0,0,80,51,1,0,0,0,80,56,1,0,0,0,80,63,1,0,0,0,80,
        70,1,0,0,0,80,75,1,0,0,0,81,1,1,0,0,0,82,83,7,0,0,0,83,3,1,0,0,0,
        84,85,6,2,-1,0,85,86,5,96,0,0,86,101,6,2,-1,0,87,88,5,42,0,0,88,
        101,6,2,-1,0,89,90,5,195,0,0,90,101,6,2,-1,0,91,92,5,129,0,0,92,
        93,3,4,2,0,93,94,5,130,0,0,94,95,6,2,-1,0,95,101,1,0,0,0,96,97,5,
        143,0,0,97,98,3,4,2,5,98,99,6,2,-1,0,99,101,1,0,0,0,100,84,1,0,0,
        0,100,87,1,0,0,0,100,89,1,0,0,0,100,91,1,0,0,0,100,96,1,0,0,0,101,
        124,1,0,0,0,102,103,10,4,0,0,103,104,5,156,0,0,104,105,3,4,2,5,105,
        106,6,2,-1,0,106,123,1,0,0,0,107,108,10,3,0,0,108,109,5,157,0,0,
        109,110,3,4,2,4,110,111,6,2,-1,0,111,123,1,0,0,0,112,113,10,2,0,
        0,113,114,5,153,0,0,114,115,3,4,2,3,115,116,6,2,-1,0,116,123,1,0,
        0,0,117,118,10,1,0,0,118,119,5,154,0,0,119,120,3,4,2,2,120,121,6,
        2,-1,0,121,123,1,0,0,0,122,102,1,0,0,0,122,107,1,0,0,0,122,112,1,
        0,0,0,122,117,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,
        0,0,0,125,5,1,0,0,0,126,124,1,0,0,0,8,37,41,58,65,80,100,122,124
    ]

class CSharpPreprocessorParser ( CSharpPreprocessorParserBase ):

    grammarFileName = "CSharpPreprocessorParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u00EF\\u00BB\\u00BF'", "<INVALID>", 
                     "'/***/'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'#'", "'abstract'", "'add'", "'alias'", "'__arglist'", 
                     "'as'", "'ascending'", "'async'", "'await'", "'base'", 
                     "'bool'", "'break'", "'by'", "'byte'", "'case'", "'catch'", 
                     "'char'", "'checked'", "'class'", "'const'", "'continue'", 
                     "'decimal'", "'default'", "'delegate'", "'descending'", 
                     "'do'", "'double'", "'dynamic'", "'else'", "'enum'", 
                     "'equals'", "'event'", "'explicit'", "'extern'", "'false'", 
                     "'finally'", "'fixed'", "'float'", "'for'", "'foreach'", 
                     "'from'", "'get'", "'goto'", "'group'", "'if'", "'implicit'", 
                     "'in'", "'int'", "'interface'", "'internal'", "'into'", 
                     "'is'", "'join'", "'let'", "'lock'", "'long'", "'nameof'", 
                     "'namespace'", "'new'", "'null'", "'object'", "'on'", 
                     "'operator'", "'orderby'", "'out'", "'override'", "'params'", 
                     "'partial'", "'private'", "'protected'", "'public'", 
                     "'readonly'", "'ref'", "'remove'", "'return'", "'sbyte'", 
                     "'sealed'", "'select'", "'set'", "'short'", "'sizeof'", 
                     "'stackalloc'", "'static'", "'string'", "'struct'", 
                     "'switch'", "'this'", "'throw'", "'true'", "'try'", 
                     "'typeof'", "'uint'", "'ulong'", "'unchecked'", "'unmanaged'", 
                     "'unsafe'", "'ushort'", "'using'", "'var'", "'virtual'", 
                     "'void'", "'volatile'", "'when'", "'where'", "'while'", 
                     "'yield'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "'('", "')'", "'.'", "','", "':'", "';'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", 
                     "'!'", "'~'", "'='", "'<'", "'>'", "'?'", "'::'", "'??'", 
                     "'++'", "'--'", "'&&'", "'||'", "'->'", "'=='", "'!='", 
                     "'<='", "'>='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'&='", "'|='", "'^='", "'<<'", "'<<='", "'??='", "'..'", 
                     "'{{'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'define'", "'undef'", "'elif'", 
                     "'endif'", "'line'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'hidden'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'}}'" ]

    symbolicNames = [ "<INVALID>", "BYTE_ORDER_MARK", "SINGLE_LINE_DOC_COMMENT", 
                      "EMPTY_DELIMITED_DOC_COMMENT", "DELIMITED_DOC_COMMENT", 
                      "SINGLE_LINE_COMMENT", "DELIMITED_COMMENT", "WHITESPACES", 
                      "SHARP", "ABSTRACT", "ADD", "ALIAS", "ARGLIST", "AS", 
                      "ASCENDING", "ASYNC", "AWAIT", "BASE", "BOOL", "BREAK", 
                      "BY", "BYTE", "CASE", "CATCH", "CHAR", "CHECKED", 
                      "CLASS", "CONST", "CONTINUE", "DECIMAL", "DEFAULT", 
                      "DELEGATE", "DESCENDING", "DO", "DOUBLE", "DYNAMIC", 
                      "ELSE", "ENUM", "EQUALS", "EVENT", "EXPLICIT", "EXTERN", 
                      "FALSE", "FINALLY", "FIXED", "FLOAT", "FOR", "FOREACH", 
                      "FROM", "GET", "GOTO", "GROUP", "IF", "IMPLICIT", 
                      "IN", "INT", "INTERFACE", "INTERNAL", "INTO", "IS", 
                      "JOIN", "LET", "LOCK", "LONG", "NAMEOF", "NAMESPACE", 
                      "NEW", "NULL_", "OBJECT", "ON", "OPERATOR", "ORDERBY", 
                      "OUT", "OVERRIDE", "PARAMS", "PARTIAL", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "READONLY", "REF", "REMOVE", 
                      "RETURN", "SBYTE", "SEALED", "SELECT", "SET", "SHORT", 
                      "SIZEOF", "STACKALLOC", "STATIC", "STRING", "STRUCT", 
                      "SWITCH", "THIS", "THROW", "TRUE", "TRY", "TYPEOF", 
                      "UINT", "ULONG", "UNCHECKED", "UNMANAGED", "UNSAFE", 
                      "USHORT", "USING", "VAR", "VIRTUAL", "VOID", "VOLATILE", 
                      "WHEN", "WHERE", "WHILE", "YIELD", "IDENTIFIER", "LITERAL_ACCESS", 
                      "INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                      "REAL_LITERAL", "CHARACTER_LITERAL", "REGULAR_STRING", 
                      "VERBATIUM_STRING", "INTERPOLATED_REGULAR_STRING_START", 
                      "INTERPOLATED_VERBATIUM_STRING_START", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_PARENS", 
                      "CLOSE_PARENS", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "PLUS", "MINUS", "STAR", "DIV", "PERCENT", "AMP", 
                      "BITWISE_OR", "CARET", "BANG", "TILDE", "ASSIGNMENT", 
                      "LT", "GT", "INTERR", "DOUBLE_COLON", "OP_COALESCING", 
                      "OP_INC", "OP_DEC", "OP_AND", "OP_OR", "OP_PTR", "OP_EQ", 
                      "OP_NE", "OP_LE", "OP_GE", "OP_ADD_ASSIGNMENT", "OP_SUB_ASSIGNMENT", 
                      "OP_MULT_ASSIGNMENT", "OP_DIV_ASSIGNMENT", "OP_MOD_ASSIGNMENT", 
                      "OP_AND_ASSIGNMENT", "OP_OR_ASSIGNMENT", "OP_XOR_ASSIGNMENT", 
                      "OP_LEFT_SHIFT", "OP_LEFT_SHIFT_ASSIGNMENT", "OP_COALESCING_ASSIGNMENT", 
                      "OP_RANGE", "DOUBLE_CURLY_INSIDE", "OPEN_BRACE_INSIDE", 
                      "REGULAR_CHAR_INSIDE", "VERBATIUM_DOUBLE_QUOTE_INSIDE", 
                      "DOUBLE_QUOTE_INSIDE", "REGULAR_STRING_INSIDE", "VERBATIUM_INSIDE_STRING", 
                      "CLOSE_BRACE_INSIDE", "FORMAT_STRING", "DIRECTIVE_WHITESPACES", 
                      "DIGITS", "DEFINE", "UNDEF", "ELIF", "ENDIF", "LINE", 
                      "ERROR", "WARNING", "REGION", "ENDREGION", "PRAGMA", 
                      "NULLABLE", "DIRECTIVE_HIDDEN", "CONDITIONAL_SYMBOL", 
                      "DIRECTIVE_NEW_LINE", "TEXT", "DOUBLE_CURLY_CLOSE_INSIDE" ]

    RULE_preprocessor_directive = 0
    RULE_directive_new_line_or_sharp = 1
    RULE_preprocessor_expression = 2

    ruleNames =  [ "preprocessor_directive", "directive_new_line_or_sharp", 
                   "preprocessor_expression" ]

    EOF = Token.EOF
    BYTE_ORDER_MARK=1
    SINGLE_LINE_DOC_COMMENT=2
    EMPTY_DELIMITED_DOC_COMMENT=3
    DELIMITED_DOC_COMMENT=4
    SINGLE_LINE_COMMENT=5
    DELIMITED_COMMENT=6
    WHITESPACES=7
    SHARP=8
    ABSTRACT=9
    ADD=10
    ALIAS=11
    ARGLIST=12
    AS=13
    ASCENDING=14
    ASYNC=15
    AWAIT=16
    BASE=17
    BOOL=18
    BREAK=19
    BY=20
    BYTE=21
    CASE=22
    CATCH=23
    CHAR=24
    CHECKED=25
    CLASS=26
    CONST=27
    CONTINUE=28
    DECIMAL=29
    DEFAULT=30
    DELEGATE=31
    DESCENDING=32
    DO=33
    DOUBLE=34
    DYNAMIC=35
    ELSE=36
    ENUM=37
    EQUALS=38
    EVENT=39
    EXPLICIT=40
    EXTERN=41
    FALSE=42
    FINALLY=43
    FIXED=44
    FLOAT=45
    FOR=46
    FOREACH=47
    FROM=48
    GET=49
    GOTO=50
    GROUP=51
    IF=52
    IMPLICIT=53
    IN=54
    INT=55
    INTERFACE=56
    INTERNAL=57
    INTO=58
    IS=59
    JOIN=60
    LET=61
    LOCK=62
    LONG=63
    NAMEOF=64
    NAMESPACE=65
    NEW=66
    NULL_=67
    OBJECT=68
    ON=69
    OPERATOR=70
    ORDERBY=71
    OUT=72
    OVERRIDE=73
    PARAMS=74
    PARTIAL=75
    PRIVATE=76
    PROTECTED=77
    PUBLIC=78
    READONLY=79
    REF=80
    REMOVE=81
    RETURN=82
    SBYTE=83
    SEALED=84
    SELECT=85
    SET=86
    SHORT=87
    SIZEOF=88
    STACKALLOC=89
    STATIC=90
    STRING=91
    STRUCT=92
    SWITCH=93
    THIS=94
    THROW=95
    TRUE=96
    TRY=97
    TYPEOF=98
    UINT=99
    ULONG=100
    UNCHECKED=101
    UNMANAGED=102
    UNSAFE=103
    USHORT=104
    USING=105
    VAR=106
    VIRTUAL=107
    VOID=108
    VOLATILE=109
    WHEN=110
    WHERE=111
    WHILE=112
    YIELD=113
    IDENTIFIER=114
    LITERAL_ACCESS=115
    INTEGER_LITERAL=116
    HEX_INTEGER_LITERAL=117
    BIN_INTEGER_LITERAL=118
    REAL_LITERAL=119
    CHARACTER_LITERAL=120
    REGULAR_STRING=121
    VERBATIUM_STRING=122
    INTERPOLATED_REGULAR_STRING_START=123
    INTERPOLATED_VERBATIUM_STRING_START=124
    OPEN_BRACE=125
    CLOSE_BRACE=126
    OPEN_BRACKET=127
    CLOSE_BRACKET=128
    OPEN_PARENS=129
    CLOSE_PARENS=130
    DOT=131
    COMMA=132
    COLON=133
    SEMICOLON=134
    PLUS=135
    MINUS=136
    STAR=137
    DIV=138
    PERCENT=139
    AMP=140
    BITWISE_OR=141
    CARET=142
    BANG=143
    TILDE=144
    ASSIGNMENT=145
    LT=146
    GT=147
    INTERR=148
    DOUBLE_COLON=149
    OP_COALESCING=150
    OP_INC=151
    OP_DEC=152
    OP_AND=153
    OP_OR=154
    OP_PTR=155
    OP_EQ=156
    OP_NE=157
    OP_LE=158
    OP_GE=159
    OP_ADD_ASSIGNMENT=160
    OP_SUB_ASSIGNMENT=161
    OP_MULT_ASSIGNMENT=162
    OP_DIV_ASSIGNMENT=163
    OP_MOD_ASSIGNMENT=164
    OP_AND_ASSIGNMENT=165
    OP_OR_ASSIGNMENT=166
    OP_XOR_ASSIGNMENT=167
    OP_LEFT_SHIFT=168
    OP_LEFT_SHIFT_ASSIGNMENT=169
    OP_COALESCING_ASSIGNMENT=170
    OP_RANGE=171
    DOUBLE_CURLY_INSIDE=172
    OPEN_BRACE_INSIDE=173
    REGULAR_CHAR_INSIDE=174
    VERBATIUM_DOUBLE_QUOTE_INSIDE=175
    DOUBLE_QUOTE_INSIDE=176
    REGULAR_STRING_INSIDE=177
    VERBATIUM_INSIDE_STRING=178
    CLOSE_BRACE_INSIDE=179
    FORMAT_STRING=180
    DIRECTIVE_WHITESPACES=181
    DIGITS=182
    DEFINE=183
    UNDEF=184
    ELIF=185
    ENDIF=186
    LINE=187
    ERROR=188
    WARNING=189
    REGION=190
    ENDREGION=191
    PRAGMA=192
    NULLABLE=193
    DIRECTIVE_HIDDEN=194
    CONDITIONAL_SYMBOL=195
    DIRECTIVE_NEW_LINE=196
    TEXT=197
    DOUBLE_CURLY_CLOSE_INSIDE=198

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Preprocessor_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None


        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_preprocessor_directive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value = ctx.value



    class PreprocessorDiagnosticContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ERROR(self):
            return self.getToken(CSharpPreprocessorParser.ERROR, 0)
        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def WARNING(self):
            return self.getToken(CSharpPreprocessorParser.WARNING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDiagnostic" ):
                listener.enterPreprocessorDiagnostic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDiagnostic" ):
                listener.exitPreprocessorDiagnostic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorDiagnostic" ):
                return visitor.visitPreprocessorDiagnostic(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorNullableContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULLABLE(self):
            return self.getToken(CSharpPreprocessorParser.NULLABLE, 0)
        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorNullable" ):
                listener.enterPreprocessorNullable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorNullable" ):
                listener.exitPreprocessorNullable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorNullable" ):
                return visitor.visitPreprocessorNullable(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorRegionContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGION(self):
            return self.getToken(CSharpPreprocessorParser.REGION, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def ENDREGION(self):
            return self.getToken(CSharpPreprocessorParser.ENDREGION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorRegion" ):
                listener.enterPreprocessorRegion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorRegion" ):
                listener.exitPreprocessorRegion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorRegion" ):
                return visitor.visitPreprocessorRegion(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorDeclarationContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEFINE(self):
            return self.getToken(CSharpPreprocessorParser.DEFINE, 0)
        def CONDITIONAL_SYMBOL(self):
            return self.getToken(CSharpPreprocessorParser.CONDITIONAL_SYMBOL, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def UNDEF(self):
            return self.getToken(CSharpPreprocessorParser.UNDEF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDeclaration" ):
                listener.enterPreprocessorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDeclaration" ):
                listener.exitPreprocessorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorDeclaration" ):
                return visitor.visitPreprocessorDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorConditionalContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.expr = None # Preprocessor_expressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CSharpPreprocessorParser.IF, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def preprocessor_expression(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Preprocessor_expressionContext,0)

        def ELIF(self):
            return self.getToken(CSharpPreprocessorParser.ELIF, 0)
        def ELSE(self):
            return self.getToken(CSharpPreprocessorParser.ELSE, 0)
        def ENDIF(self):
            return self.getToken(CSharpPreprocessorParser.ENDIF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorConditional" ):
                listener.enterPreprocessorConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorConditional" ):
                listener.exitPreprocessorConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorConditional" ):
                return visitor.visitPreprocessorConditional(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorPragmaContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRAGMA(self):
            return self.getToken(CSharpPreprocessorParser.PRAGMA, 0)
        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorPragma" ):
                listener.enterPreprocessorPragma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorPragma" ):
                listener.exitPreprocessorPragma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorPragma" ):
                return visitor.visitPreprocessorPragma(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorLineContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LINE(self):
            return self.getToken(CSharpPreprocessorParser.LINE, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def DIGITS(self):
            return self.getToken(CSharpPreprocessorParser.DIGITS, 0)
        def DEFAULT(self):
            return self.getToken(CSharpPreprocessorParser.DEFAULT, 0)
        def DIRECTIVE_HIDDEN(self):
            return self.getToken(CSharpPreprocessorParser.DIRECTIVE_HIDDEN, 0)
        def STRING(self):
            return self.getToken(CSharpPreprocessorParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorLine" ):
                listener.enterPreprocessorLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorLine" ):
                listener.exitPreprocessorLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorLine" ):
                return visitor.visitPreprocessorLine(self)
            else:
                return visitor.visitChildren(self)



    def preprocessor_directive(self):

        localctx = CSharpPreprocessorParser.Preprocessor_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_preprocessor_directive)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [183]:
                localctx = CSharpPreprocessorParser.PreprocessorDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(CSharpPreprocessorParser.DEFINE)
                self.state = 7
                self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                self.state = 8
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveDefine(); 
                pass
            elif token in [184]:
                localctx = CSharpPreprocessorParser.PreprocessorDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(CSharpPreprocessorParser.UNDEF)
                self.state = 12
                self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                self.state = 13
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveUndef(); 
                pass
            elif token in [52]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(CSharpPreprocessorParser.IF)
                self.state = 17
                localctx.expr = self.preprocessor_expression(0)
                self.state = 18
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveIf(); 
                pass
            elif token in [185]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(CSharpPreprocessorParser.ELIF)
                self.state = 22
                localctx.expr = self.preprocessor_expression(0)
                self.state = 23
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveElif(); 
                pass
            elif token in [36]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(CSharpPreprocessorParser.ELSE)
                self.state = 27
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveElse(); 
                pass
            elif token in [186]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(CSharpPreprocessorParser.ENDIF)
                self.state = 31
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveEndif(); 
                pass
            elif token in [187]:
                localctx = CSharpPreprocessorParser.PreprocessorLineContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 34
                self.match(CSharpPreprocessorParser.LINE)
                self.state = 41
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [182]:
                    self.state = 35
                    self.match(CSharpPreprocessorParser.DIGITS)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==91:
                        self.state = 36
                        self.match(CSharpPreprocessorParser.STRING)


                    pass
                elif token in [30]:
                    self.state = 39
                    self.match(CSharpPreprocessorParser.DEFAULT)
                    pass
                elif token in [194]:
                    self.state = 40
                    self.match(CSharpPreprocessorParser.DIRECTIVE_HIDDEN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 43
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveLine(); 
                pass
            elif token in [188]:
                localctx = CSharpPreprocessorParser.PreprocessorDiagnosticContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.match(CSharpPreprocessorParser.ERROR)
                self.state = 47
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 48
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveError(); 
                pass
            elif token in [189]:
                localctx = CSharpPreprocessorParser.PreprocessorDiagnosticContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.match(CSharpPreprocessorParser.WARNING)
                self.state = 52
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 53
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveWarning(); 
                pass
            elif token in [190]:
                localctx = CSharpPreprocessorParser.PreprocessorRegionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 56
                self.match(CSharpPreprocessorParser.REGION)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==197:
                    self.state = 57
                    self.match(CSharpPreprocessorParser.TEXT)


                self.state = 60
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveRegion(); 
                pass
            elif token in [191]:
                localctx = CSharpPreprocessorParser.PreprocessorRegionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 63
                self.match(CSharpPreprocessorParser.ENDREGION)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==197:
                    self.state = 64
                    self.match(CSharpPreprocessorParser.TEXT)


                self.state = 67
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveEndregion(); 
                pass
            elif token in [192]:
                localctx = CSharpPreprocessorParser.PreprocessorPragmaContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 70
                self.match(CSharpPreprocessorParser.PRAGMA)
                self.state = 71
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 72
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectivePragma(); 
                pass
            elif token in [193]:
                localctx = CSharpPreprocessorParser.PreprocessorNullableContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 75
                self.match(CSharpPreprocessorParser.NULLABLE)
                self.state = 76
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 77
                self.directive_new_line_or_sharp()
                 this.OnPreprocessorDirectiveNullable(); 
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


    class Directive_new_line_or_sharpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_NEW_LINE(self):
            return self.getToken(CSharpPreprocessorParser.DIRECTIVE_NEW_LINE, 0)

        def EOF(self):
            return self.getToken(CSharpPreprocessorParser.EOF, 0)

        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_directive_new_line_or_sharp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective_new_line_or_sharp" ):
                listener.enterDirective_new_line_or_sharp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective_new_line_or_sharp" ):
                listener.exitDirective_new_line_or_sharp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective_new_line_or_sharp" ):
                return visitor.visitDirective_new_line_or_sharp(self)
            else:
                return visitor.visitChildren(self)




    def directive_new_line_or_sharp(self):

        localctx = CSharpPreprocessorParser.Directive_new_line_or_sharpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive_new_line_or_sharp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==-1 or _la==196):
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


    class Preprocessor_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.expr1 = None # Preprocessor_expressionContext
            self.expr = None # Preprocessor_expressionContext
            self.expr2 = None # Preprocessor_expressionContext

        def TRUE(self):
            return self.getToken(CSharpPreprocessorParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpPreprocessorParser.FALSE, 0)

        def CONDITIONAL_SYMBOL(self):
            return self.getToken(CSharpPreprocessorParser.CONDITIONAL_SYMBOL, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpPreprocessorParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpPreprocessorParser.CLOSE_PARENS, 0)

        def preprocessor_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpPreprocessorParser.Preprocessor_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpPreprocessorParser.Preprocessor_expressionContext,i)


        def BANG(self):
            return self.getToken(CSharpPreprocessorParser.BANG, 0)

        def OP_EQ(self):
            return self.getToken(CSharpPreprocessorParser.OP_EQ, 0)

        def OP_NE(self):
            return self.getToken(CSharpPreprocessorParser.OP_NE, 0)

        def OP_AND(self):
            return self.getToken(CSharpPreprocessorParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(CSharpPreprocessorParser.OP_OR, 0)

        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_preprocessor_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessor_expression" ):
                listener.enterPreprocessor_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessor_expression" ):
                listener.exitPreprocessor_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessor_expression" ):
                return visitor.visitPreprocessor_expression(self)
            else:
                return visitor.visitChildren(self)



    def preprocessor_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_preprocessor_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [96]:
                self.state = 85
                self.match(CSharpPreprocessorParser.TRUE)
                 this.OnPreprocessorExpressionTrue(); 
                pass
            elif token in [42]:
                self.state = 87
                self.match(CSharpPreprocessorParser.FALSE)
                 this.OnPreprocessorExpressionFalse(); 
                pass
            elif token in [195]:
                self.state = 89
                self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                 this.OnPreprocessorExpressionConditionalSymbol(); 
                pass
            elif token in [129]:
                self.state = 91
                self.match(CSharpPreprocessorParser.OPEN_PARENS)
                self.state = 92
                localctx.expr = self.preprocessor_expression(0)
                self.state = 93
                self.match(CSharpPreprocessorParser.CLOSE_PARENS)
                 this.OnPreprocessorExpressionConditionalOpenParens(); 
                pass
            elif token in [143]:
                self.state = 96
                self.match(CSharpPreprocessorParser.BANG)
                self.state = 97
                localctx.expr = self.preprocessor_expression(5)
                 this.OnPreprocessorExpressionConditionalBang(); 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 122
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 103
                        self.match(CSharpPreprocessorParser.OP_EQ)
                        self.state = 104
                        localctx.expr2 = self.preprocessor_expression(5)
                         this.OnPreprocessorExpressionConditionalEq(); 
                        pass

                    elif la_ == 2:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 108
                        self.match(CSharpPreprocessorParser.OP_NE)
                        self.state = 109
                        localctx.expr2 = self.preprocessor_expression(4)
                         this.OnPreprocessorExpressionConditionalNe(); 
                        pass

                    elif la_ == 3:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 113
                        self.match(CSharpPreprocessorParser.OP_AND)
                        self.state = 114
                        localctx.expr2 = self.preprocessor_expression(3)
                         this.OnPreprocessorExpressionConditionalAnd(); 
                        pass

                    elif la_ == 4:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 117
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 118
                        self.match(CSharpPreprocessorParser.OP_OR)
                        self.state = 119
                        localctx.expr2 = self.preprocessor_expression(2)
                         this.OnPreprocessorExpressionConditionalOr(); 
                        pass

             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.preprocessor_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def preprocessor_expression_sempred(self, localctx:Preprocessor_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




