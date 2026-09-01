grammar Crop2MLComposition;

/*
 * Parser rules
 */

composition
    : NEWLINE*
      documentation
      NEWLINE+
      (statement NEWLINE+)*
      statement?
      NEWLINE*
      EOF
    ;

/* YAML metadata enclosed in a Python-style module docstring. */
documentation
    : DOCSTRING
    ;

statement
    : modelCall
    | modelInputAssignment
    | compositionOutputAssignment
    ;

/*
 * Calls a ModelUnit.
 *
 * Example:
 *     SoilTemperature()
 */
modelCall
    : modelName LPAREN RPAREN
    ;

/*
 * Supplies a ModelUnit input.
 *
 * External composition input:
 *     SoilTemperature.timeStep = timeStep
 *
 * Internal connection:
 *     SoilTemperature.surfaceTemperature =
 *         SurfaceModel.surfaceTemperature
 */
modelInputAssignment
    : modelPort ASSIGN source
    ;

/*
 * Publishes a ModelUnit output as a composition output.
 *
 * Example:
 *     surfaceTemperature =
 *         SurfaceModel.soilSurfaceTemperature
 */
compositionOutputAssignment
    : identifier ASSIGN modelPort
    ;

/*
 * A bare identifier is a composition input.
 * A qualified port is the output of another ModelUnit.
 */
source
    : identifier
    | modelPort
    ;

modelPort
    : modelName DOT portName
    ;

modelName
    : identifier
    ;

portName
    : identifier
    ;

identifier
    : IDENTIFIER
    ;


/*
 * Lexer rules
 */

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

DOT
    : '.'
    ;

ASSIGN
    : '='
    ;

/* Keep the complete YAML document as one token, including newlines. */
DOCSTRING
    : '"""' .*? '"""'
    | '\'\'\'' .*? '\'\'\''
    ;

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

/*
 * Explicit line continuation:
 *
 *     surfaceTemperature = \
 *         Model.surfaceTemperature
 *
 * The backslash, following whitespace, and newline are discarded.
 */
LINE_CONTINUATION
    : '\\' [ \t]* '\r'? '\n' -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

NEWLINE
    : '\r'? '\n'
    ;

WS
    : [ \t]+ -> skip
    ;
