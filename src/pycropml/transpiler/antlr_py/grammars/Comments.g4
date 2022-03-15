/*
Copyright (c) 2022  Cyrille.

License for use and distribution: Eclipse Public License

CyML comments language grammar

*/

grammar Comments;

documentation
	: '!%%Cyml Comments Begin%%' documentationContent '!%%Cyml Comments End%%' EOF
	;

documentationContent: comment_line +;

comment_line
	: Symbol Identifier /* DESCRIPTION  '('Unit')' '('Value ',' '['Value '-' Value ']' ')' '('CATEGORY ')'*/
	;


Identifier
	: [A-Za-z_][A-Za-z0-9_]*
	;
/*
CATEGORY : 'state' | 'rate' | 'exogenous' | 'soil' |'genotypic' | 'constant';

Value : NUM+ '.' NUM*;
*/
/*
Unit
	: (~[ \t\r\n()#"\\] | Escape_sequence)+
	;

Escape_sequence
	: Escape_identity | Escape_encoded | Escape_semicolon
	;
*/

Symbol: ('!'|'#'|'//');



fragment Newline
	: '\r\n' | '\r' | '\n' 
	;

fragment Num
   : ('0' .. '9')
   ;
/*
fragment
Escape_identity
	: '\\' ~[A-Za-z0-9;]
	;

fragment
Escape_encoded
	: '\\t' | '\\r' | '\\n'
	;

fragment
Escape_semicolon
	: '\\;'
	;
*/
/*
fragment
Quoted_cont
	: '\\' ('\r' '\n'? | '\n')
	;

Bracket_argument
	: '[' Bracket_arg_nested ']'
	;

fragment
Bracket_arg_nested
	: '=' Bracket_arg_nested '='
	| '[' .*? ']'
	;
*/
fragment Space
	: (' '|'\t')+
	;

Ws
   :  (Space+|Newline) -> skip
   ;


/*DESCRIPTION
	: ~[()! ] + .
	;*/

/*LINECONT
   :  (SPACE? NEWLINE SPACE* [ \t] * '!              ') -> skip
   ;*/

