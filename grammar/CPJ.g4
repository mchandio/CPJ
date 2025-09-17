// ANTLR4 grammar for a CPJ subset (initial draft)
// Captures GUI block, widget statements, types maps (token and dict-style), and expressions
// This grammar is intended as a starting point for migrating or generating a parser.

grammar CPJ;

// Parser rules
program
    : (statement | NEWLINE)* EOF
    ;

statement
    : guiBlock
    | funcDef
    | typeDef
    | exprStmt
    ;

// User-defined type declaration
typeDef
    : TYPE_KW Identifier LBRACE typeFieldList RBRACE NEWLINE*
    ;

typeFieldList
    : typeField (COMMA typeField)* (COMMA)?
    ;

typeField
    : Identifier COLON Identifier
    ;


// Function definition with optional type annotations and return type
funcDef
    : DEF Identifier LPAREN paramList? RPAREN (ARROW Identifier)? COLON (NEWLINE suite | suite)
    ;

paramList
    : param (COMMA param)*
    ;

param
    : Identifier (COLON Identifier)?
    ;
// New lexer tokens for type system
TYPE_KW: [tT][yY][pP][eE] ;
ARROW: '->' ;

suite
    : INDENT NEWLINE* statement+ DEDENT
    | simpleStmt
    ;

simpleStmt
    : exprStmt
    ;

exprStmt
    : expression NEWLINE
    ;

// GUI block
guiBlock
    : GUI_KW Identifier COLON NEWLINE INDENT guiBody+ DEDENT
    | GUI_CAP LBRACE NEWLINE* INDENT guiBody+ DEDENT RBRACE NEWLINE*
    ;

guiBody
    : typesLine
    | widgetStmt
    | callStmt
    | guiProp
    | expression (NEWLINE)?
    | NEWLINE+
    ;

guiProp
    : Identifier COLON expression NEWLINE
    ;

// types support: token-style or dict-style
typesLine
    : TYPES_KW (typesTokens | typesDict)
    ;

// token-style: one or more key:type pairs on the same line
typesTokens
    : (Identifier COLON Identifier | Identifier '=' Identifier)+ NEWLINE
    ;

// dict-style: allow either inline {"x":"int",...} or block style with INDENT/DEDENT
typesDict
    : LBRACE (typeEntries RBRACE NEWLINE | NEWLINE INDENT NEWLINE* typeLine+ DEDENT RBRACE NEWLINE)
    ;

typeEntries
    : typeEntry (',' typeEntry)* (',')?
    ;

typeLine
    : typeEntry (',')? NEWLINE
    ;

// allow Identifier or StringLiteral for keys and for type names
typeEntry
    : (StringLiteral | Identifier) COLON (StringLiteral | Identifier)
    ;

// Widget statements (a subset)
widgetStmt
    : ADD_TEXT LPAREN args? RPAREN
    | ADD_BTN LPAREN args? RPAREN
    | ADD_CHECK LPAREN args? RPAREN
    | ADD_SLIDER LPAREN args? RPAREN
    ;

args
    : arg (',' arg)*
    ;

arg
    : StringLiteral
    | expression
    ;

// expression variant without requiring trailing NEWLINE — used inside GUI bodies
exprNoNewline
    : expression
    ;

// Expressions (basic, with dotted identifiers and function calls)
expression
    : lambdaExpr
    ;
lambdaExpr
    : logicalOr
    ;

logicalOr
    : logicalAnd ('or' logicalAnd)*
    ;

logicalAnd
    : equality ('and' equality)*
    ;

equality
    : comparison ((EQ | NEQ) comparison)*
    ;

comparison
    : bitwiseOr ((LT | GT | LE | GE | IN | IS) bitwiseOr)*
    ;

bitwiseOr
    : bitwiseXor (BITOR bitwiseXor)*
    ;

bitwiseXor
    : bitwiseAnd (BITXOR bitwiseAnd)*
    ;

bitwiseAnd
    : shift (BITAND shift)*
    ;

shift
    : sum ((LSHIFT | RSHIFT) sum)*
    ;

sum
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((STAR | DIV | MOD) factor)*
    ;

factor
    : (PLUS | MINUS | TILDE) factor
    | power
    ;

power
    : atom (POW factor)?
    ;

atom
    : LPAREN expression RPAREN
    | literal
    | dottedName ( LPAREN argList? RPAREN )?
    ;

argList
    : expression (',' expression)*
    ;

// Bare function-call statement (e.g. show()) used inside GUI bodies
callStmt
    : dottedName '(' argList? ')' (NEWLINE | INDENT | DEDENT)?
    ;


dottedName
    : Identifier (DOT Identifier)*
    ;

literal
    : Integer
    | Float
    | StringLiteral
    | TRUE | FALSE | NULL
    ;

// Lexer rules

// Structural tokens
NEWLINE: ('\r'? '\n')+ ;
INDENT: '<INDENT>' ;
DEDENT: '<DEDENT>' ;

// Punctuation and operators (named tokens to avoid ambiguous implicit numbering)
LPAREN: '(' ;
RPAREN: ')' ;
COLON: ':' ;
COMMA: ',' ;
LBRACE: '{' ;
RBRACE: '}' ;
DOT: '.' ;

PLUS: '+' ;
MINUS: '-' ;
STAR: '*' ;
DIV: '/' ;
MOD: '%' ;
POW: '**' ;
TILDE: '~' ;

LT: '<' ;
GT: '>' ;
LE: '<=' ;
GE: '>=' ;
EQ: '==' ;
NEQ: '!=' ;
LSHIFT: '<<' ;
RSHIFT: '>>' ;
BITOR: '|' ;
BITXOR: '^' ;
BITAND: '&' ;

// Keywords and widget names
// Keywords (case-insensitive where appropriate). Widget function names are case-sensitive.
DEF: [dD][eE][fF] ;
GUI_CAP: 'GUI' ;
GUI_KW: [gG][uU][iI] ;
TYPES_KW: [tT][yY][pP][eE][sS] ;
ADD_TEXT: 'addTextField' ;
ADD_BTN: 'addButton' ;
ADD_CHECK: 'addCheckBox' ;
ADD_SLIDER: 'addSlider' ;
OR: [oO][rR] ;
AND: [aA][nN][dD] ;
IN: [iI][nN] ;
IS: [iI][sS] ;
TRUE: [tT][rR][uU][eE] ;
FALSE: [fF][aA][lL][sS][eE] ;
NULL: [nN][uU][lL][lL] ;

// Numeric literals: Float must come before Integer so multi-part numbers are matched first.
fragment DIGIT: [0-9] ;
fragment DIGITS: DIGIT+ ;

Float
    : DIGITS '.' DIGITS? ([eE] [+-]? DIGITS)?
    | '.' DIGITS ([eE] [+-]? DIGITS)?
    | DIGITS [eE] [+-]? DIGITS
    ;

Integer: DIGITS ;
StringLiteral
    : '"' (~["\\] | '\\' .)* '"'
    | '\'' (~['\\] | '\\' .)* '\''
    ;

Identifier
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

WS: [ \t]+ -> channel(HIDDEN) ;

// Note: Real indentation-sensitive grammar requires custom handling or the Python-style
// INDENT/DEDENT preprocessing used by the ANTLR Python grammar. Here we use placeholders
// to indicate block structure; a later pass should replace them with real handling.
