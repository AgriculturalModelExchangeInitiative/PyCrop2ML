lexer grammar Fortran90Lexer;


RECURSIVE 
   : 'RECURSIVE' | 'recursive' ;


CONTAINS
   :
   ('contains'|'CONTAINS')
   ;

MODULE
   : 'MODULE' | 'module'
   ;

ENDMODULE
   : 'ENDMODULE' | 'endmodule'
   ;

PROGRAM
   : 'program' | 'PROGRAM'
   ;

ENTRY
   : 'entry' | 'ENTRY'
   ;

FUNCTION
   : 'function' | 'FUNCTION'
   ;


BLOCK
   : 'block' | 'BLOCK'
   ;

SUBROUTINE
   : 'subroutine' | 'SUBROUTINE'
   ;

ENDINTERFACE
   : 'ENDINTERFACE' | ' endinterface'
   ;

PROCEDURE
   : 'procedure'  | 'PROCEDURE'
   ;

END
   : 'END' | 'end'| 'End'
   ;

DIMENSION
   : 'dimension' | 'DIMENSION'
   ;

TARGET : 'TARGET' | 'target' ;

ALLOCATABLE : 'ALLOCATABLE' | 'allocatable' ;

OPTIONAL : 'OPTIONAL' | 'optional' ;

NAMELIST : 'NAMELIST' | 'namelist' ;

INTENT : 'INTENT' | 'intent' ;

IN : 'IN' | 'in' ;

OUT : 'OUT' | 'out' ;

INOUT : 'INOUT' | 'inout' ;

OPERATOR : 'operator' | 'OPERATOR';

USE : 'USE' | 'use' ;

ONLY : 'ONLY' | 'only' ;

IMPLIEDT : '=>' ;

ASSIGNMENT : 'ASSIGNMENT' | 'assignment' ;

DOP : '.''\\a'+'.';

OP 
   :'=='
   | '!='
   | '<='
   |'>='
   |'<'
   |'>'
   |'/='
   ; 

DOUBLEPRECISION : 'DOUBLEPRECISION' | 'doubleprecision' | 'double precision' | 'DOUBLE PRECISION';

DOUBLECOLON : '::' ;

ASSIGNSTMT : 'assign' | 'ASSIGN' ;

COMMON : 'COMMON' | 'common' ;

ELSEWHERE : 'ELSEWHERE' | 'elsewhere' ;

REAL
   : 'REAL' | 'real'
   ;



EQUIVALENCE
   : 'EQUIVALENCE' | 'equivalence'
   ;


BLOCKDATA
   : 'blockdata' | 'BLOCKDATA'
   ;


POINTER
   : 'pointer' | 'POINTER'
   ;

fragment PRIVATES
    : 'private' | 'PRIVATE'
    ;

PRIVATE : PRIVATES ;

SEQUENCE
   : 'sequence' | 'SEQUENCE'
   ;
   
fragment PUBLIC 
    : 'public' | 'PUBLIC'
    ;

ACCESSSPEC
   : PRIVATE | PUBLIC
   ;

IMPLICIT
   : 'implicit' | 'IMPLICIT'
   ;

NONE
   : 'none' | 'NONE'
   ;

CHARACTER
   : 'character' | 'CHARACTER'
   ;


PARAMETER
   : 'parameter' | 'PARAMETER'
   ;


EXTERNAL
   : 'external' | 'EXTERNAL'
   ;


INTRINSIC
   : 'intrinsic' | 'INTRINSIC'
   ;


SAVE
   : 'save' | 'SAVE'
   ;


DATA
   : 'data' | 'DATA'
   ;


GO
   : 'GO' | 'go'
   ;


GOTO
   : 'GOTO' | 'goto' 
   ;


IF
   : 'IF' | 'if'
   ;


THEN
   : 'THEN' | 'then'
   ;


ELSE
   : 'ELSE' | 'else'
   ;


ENDIF
   : 'ENDIF' | 'endif'
   ;

RESULT
   : 'RESULT' | 'result'
   ;


ELSEIF
   : 'ELSEIF' | 'elseif'
   ;


DO
   : 'DO' | 'do'
   ;

INCLUDE : 'INCLUDE' | 'include' ;

CONTINUE
   : 'CONTINUE' | 'continue'
   ;

ENDWHERE : 'ENDWHERE' | 'endwhere' ;

WHERE : 'WHERE' | 'where' ;

ENDSELECT : 'ENDSELECT' | 'endselect' ;

SELECTCASE : 'SELECTCASE' | 'selectcase';

SELECT: 'SELECT' | 'select' ;

CASE : 'case' | 'CASE' ;

DEFAULT : 'DEFAULT' | 'default';

DIRECT : 'DIRECT' | 'direct' ;

STOP
   : 'STOP' | 'stop'
   ;

 REC : 'REC' | 'rec'
   ;

ENDDO
   : 'ENDDO' | 'enddo'
   ;


PAUSE
   : 'pause' | 'PAUSE'
   ;


WRITE
   : 'WRITE' | 'write'
   ;


READ
   : 'READ' | 'read'
   ;


PRINT
   : 'PRINT' | 'print'
   ;


OPEN
   : 'OPEN' | 'open'
   ;


FMT
   : 'FMT' | 'fmt'
   ;


UNIT
   : 'UNIT' | 'unit'
   ;

PAD : 'PAD' | 'pad' ;

ACTION : 'ACTION' | 'action' ;

DELIM : 'DELIM' | 'delim' ;

IOLENGTH : 'IOLENGTH' | 'iolength' ;

READWRITE : 'READWRITE' | 'readwrite' ;

ERR
   : 'err' | 'ERR'
   ;

SIZE : 'SIZE' | 'size' ;

ADVANCE : 'ADVANCE' | 'advance' ;

NML : 'NML' | 'nml' ;


IOSTAT
   : 'IOSTAT' | 'iostat'
   ;


FORMAT
   : 'FORMAT' | 'format'
   ;


LET
   : 'LET' | 'let'
   ;


CALL
   : 'CALL' | 'call'
   ;


RETURN
   : 'RETURN' | 'return'
   ;


CLOSE
   : 'CLOSE' | 'close'
   ;


DOUBLE
   : 'DOUBLE' | 'double'
   ;


IOSTART
   : 'IOSTART' | 'iostart'
   ;


SEQUENTIAL
   : 'SEQUENTIAL' | 'sequential'
   ;


LABEL
   : 'LABEL' | 'label'
   ;


FILE
   : 'file' | 'FILE'
   ;


STATUS
   : 'STATUS' | 'status'
   ;


ACCESS
   : 'ACCESS' | 'access'
   ;


POSITION
   : 'POSITION' | 'position'
   ;


FORM
   : 'FORM' | 'form'
   ;


RECL
   : 'RECL' | 'recl'
   ;


EXIST
   : 'EXIST' | 'exist'
   ;


OPENED
   : 'OPENED' | 'opened'
   ;


NUMBER
   : 'NUMBER' | 'number'
   ;


NAMED
   : 'NAMED' | 'named'
   ;


NAME_
   : 'NAME' | 'name'
   ;


FORMATTED
   : 'FORMATTED' | 'formatted'
   ;


UNFORMATTED
   : 'UNFORMATTED' | 'unformatted'
   ;


NEXTREC
   : 'NEXTREC' | 'nextrec'
   ;


INQUIRE
   : 'INQUIRE' | 'inquire'
   ;


BACKSPACE
   : 'BACKSPACE' | 'backspace'
   ;


ENDFILE
   : 'ENDFILE' | 'endfile'
   ;


REWIND
   : 'REWIND' | 'rewind'
   ;

ENDBLOCKDATA : 'endblockdata' | 'ENDBLOCKDATA' ;

ENDBLOCK : 'ENDBLOCK' | 'endblock' ;


fragment NEWLINE
	: '\r\n' | '\r' | '\n'
	| '\u0085' // <Next Line CHARACTER (U+0085)>'
	| '\u2028' //'<Line Separator CHARACTER (U+2028)>'
	| '\u2029' //'<Paragraph Separator CHARACTER (U+2029)>'
	;
 

KIND : 'KIND' | 'kind' ;

LEN : 'LEN' | 'len' ;

//EOS : COMMENTORNEWLINE+ ;
//EOS : (COMMENTORNEWLINE? SPACES* [\r\n] [ \t]* )+;

//RN : NEWLINE -> skip;

WS
   :  ([ \t]  | NEWLINE)+ -> skip
   ;

COMMENT
    : (('\t'* '\u0020'* '!'(~ [\r\n])*[\r\n]* ) |({self.column == 0}? ('c'| 'C') (~ [\r\n])* [\r\n]*)) -> skip  ;

/*
COMMENTORNEWLINE 
   : COMMENT
   |
   NEWLINE

   ;
*/



DOLLAR
   : '$'
   ;


COMMA
   : ','
   ;


LPAREN
   : '('
   ;

PCT : '%';

WHILE : 'while' | 'WHILE';

ALLOCATE : 'ALLOCATE' | 'allocate' ;

STAT : 'STAT' | 'stat';

RPAREN
   : ')'
   ;


COLON
   : ':'
   ;


ASSIGN
   : '='
   ;


MINUS
   : '-'
   ;


PLUS
   : '+'
   ;


DIV
   : '/'
   ;

fragment STARCHAR
   : '*'
   ;

FORMATSEP 
   : '/' | ':'
   ;


POWER
   : '**'
   ;


LNOT
   : '.not.' | '.NOT.'
   ;


LAND
   : '.and.' | '.AND.'
   ;


LOR
   : '.or.' | '.OR.'
   ;


EQV
   : '.eqv.' | '.EQV.'
   ;


NEQV
   : '.neqv.' | '.NEQV.'
   ;


XOR
   : '.xor.' | '.XOR.'
   ;


EOR
   : '.eor.' | '.EOR.'
   ;


LT
   : '.lt.' | '.LT.'
   ;


LE
   : '.le.' | '.LE.'
   ;


GT
   : '.gt.' | '.GT.'
   ;


GE
   : '.ge.' | '.GE.'
   ;


NE
   : '.ne.' | '.NE.'
   ;


EQ
   : '.eq.' | '.EQ.'
   ;


TRUE
   : '.true.' | '.TRUE.'
   ;


FALSE
   : '.false.' | '.FALSE.'
   ;


XCON
   : NUM+ [xX]
   ;


PCON
   : [+-]?NUM+[pP]
   ;


FCON
   : ('a'|'A'|'b'|'B'|'e'|'E'|'d'|'D'|(('e'|'E')('n'|'N'|'s'|'S'))|'q'|'Q'|'f'|'F'|'g'|'G'|'i'|'I'|'l'|'L'|'o'|'O'|'z'|'Z')(NUM+|'*')('.'NUM+(('e'|'E'|'d'|'D'|'q'|'Q')NUM+)?)
   ;


CCON
   : 'CCON'
   ;


HOLLERITH
   : 'HOLLERITH'
   ;


CONCATOP
   : 'CONCATOP'
   ;


CTRLDIRECT
   : 'CTRLDIRECT'
   ;


CTRLREC
   : 'CTRLREC'
   ;


TO
   : 'TO'
   ;


SUBPROGRAMBLOCK
   : 'SUBPROGRAMBLOCK'
   ;


DOBLOCK
   : 'DOBLOCK'
   ;


AIF
   : 'AIF'
   ;


THENBLOCK
   : 'THENBLOCK'
   ;


ELSEBLOCK
   : 'ELSEBLOCK'
   ;


CODEROOT
   : 'CODEROOT'
   ;


COMPLEX
   : 'COMPLEX' | 'complex'
   ;


PRECISION
   : 'PRECISION' | 'precision'
   ;


INTEGER
   : 'INTEGER' | 'integer'
   ;


LOGICAL
   : 'LOGICAL' | 'logical'
   ;

fragment SCORE : '_';

UNDERSCORE : SCORE ;

OBRACKETSLASH : '(/';

DOT : '.' ;

CBRACKETSLASH : '/)';

ZCON :  [zZ]'\''[abcdefABCDEF0-9] + '\''
   | [zZ] '"'[abcdefABCDEF0-9] +'"' ;

BCON : [bB]'\'' [01] + '\''
   | [bB]'"'[01] + '"'
   ;

 OCON 
   : [oO]'"'[01234567] + '"'
   | [oO]'\''[01234567] + '\''
   ;

SCON
   : '\'' ('\'' '\'' | ~ ('\'' | '\n' | '\r') | (('\n' | '\r' ('\n')?) '     ' CONTINUATION) ('\n' | '\r' ('\n')?) '     ' CONTINUATION)* '\''
   |
   '\'' (~('\'') | ('\'''\''))*  ('\'' )
   |
   ('"') (~('"') | '""')*  ('"')
   ;

RDCON : NUM+ '.' NUM* EXPON?
      ;

DEALLOCATE : 'DEALLOCATE' | 'deallocate' ;

NULLIFY : 'NULLIFY' | 'nullify' ;

EXIT : 'EXIT' | 'exit' ;

CYCLE : 'CYCLE' | 'cycle' ;
   
ENDTYPE : 'ENDTYPE' | 'endtype' | 'Endtype' |'EndType';

INTERFACE : 'INTERFACE' | 'interface' | 'Interface' ;
   
SPOFF : 'SPOFF';

SPON : 'SPON';

ICON
   : NUM+
   ;

TYPE 
   : 'type' | 'TYPE' | 'Type'
   ;

NAME
   :LETTER ( ALPHANUMERIC_CHARACTER )*
   ;

BLANK
   : 'BLANK' | 'blank'
   ;


ALPHANUMERIC_CHARACTER : LETTER | NUM | SCORE ;

fragment LETTER : ('a'..'z' | 'A'..'Z') ;


STAR
   : STARCHAR
   ;

STRINGLITERAL
   : '"' ~ ["\r\n]* '"'
   ;
   
EOL
   : [\r\n] +
   ;

fragment SPACES
 : [ \t] +
 ;

LINECONT
   :  (('&' SPACES? COMMENT? NEWLINE (SPACES* [ \t] * '&' )?) | ( SPACES? COMMENT? NEWLINE SPACES* [ \t] * '&' )) -> skip
   ;

fragment CONTINUATION
   : ~ ('0' | ' ')
   ;


fragment ALNUM
   : (ALPHA | NUM)
   ;


fragment HEX
   : (NUM | 'a' .. 'f')
   ;


fragment SIGN
   : ('+' | '-')
   ;


fragment FDESC
   : ('i' | 'f' | 'd') (NUM) + '.' (NUM) + | ('e' | 'g') (NUM) + '.' (NUM) + ('e' (NUM) +)?
   ;


fragment EXPON
   : ('e' | 'E' | 'd' | 'D') (SIGN)? (NUM) +
   ;


fragment ALPHA
   : ('a' .. 'z') | ('A' .. 'Z')
   ;


fragment NUM
   : ('0' .. '9')
   ;

// '' is used to drop the charater when forming the lexical token
// Strings are assumed to start with a single quote (') and two
// single quotes is meant as a literal single quote


   
