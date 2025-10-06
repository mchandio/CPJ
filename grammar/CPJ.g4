grammar CPJ;

tokens { INDENT, DEDENT }

// Common operators
MUL: '*';
DIV: '/';
FDIV: '//';
MOD: '%';
ADD: '+';
SUB: '-';
LSH: '<<';
RSH: '>>';
URSH: '>>>';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
EQ: '==';
NE: '!=';
BAND: '&';
BXOR: '^';
BOR: '|';
AND: '&&';
OR: '||';
NOT: '!';
BNOT: '~';
ASSIGN: '=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
LSH_ASSIGN: '<<=';
RSH_ASSIGN: '>>=';
URSH_ASSIGN: '>>>=';
BAND_ASSIGN: '&=';
BXOR_ASSIGN: '^=';
BOR_ASSIGN: '|=';
INC: '++';
DEC: '--';
ARROW: '->';
SCOPE: '::';
ELVIS: '?:';
DOT: '.';
LAMBDA: '=>';
POW: '**';
POW_ASSIGN: '**=';
AT: '@';

// Keywords
ABSTRACT: 'abstract';
AS: 'as';
ASSERT: 'assert';
ASYNC: 'async';
AWAIT: 'await';
BREAK: 'break';
CASE: 'case';
CATCH: 'catch';
CLASS: 'class';
CONST: 'const';
CONTINUE: 'continue';
DEF: 'def';
DEFAULT: 'default';
DEL: 'del';
DO: 'do';
ELIF: 'elif';
ELSE: 'else';
ENUM: 'enum';
EXTENDS: 'extends';
FALSE: 'false';
FINAL: 'final';
FINALLY: 'finally';
FOR: 'for';
FROM: 'from';
GLOBAL: 'global';
IF: 'if';
IMPLEMENTS: 'implements';
IMPORT: 'import';
IN: 'in';
INSTANCEOF: 'instanceof';
INTERFACE: 'interface';
IS: 'is';
NEW: 'new';
NONE: 'None';
NONLOCAL: 'nonlocal';
NULL: 'null';
PASS: 'pass';
PRIVATE: 'private';
PROTECTED: 'protected';
PUBLIC: 'public';
RAISE: 'raise';
RETURN: 'return';
STATIC: 'static';
SUPER: 'super';
SWITCH: 'switch';
SYNCHRONIZED: 'synchronized';
THIS: 'this';
THROW: 'throw';
THROWS: 'throws';
TRUE: 'true';
TRY: 'try';
VOID: 'void';
WHILE: 'while';
WITH: 'with';
YIELD: 'yield';

// Preprocessor directives
PRAGMA: '#pragma';
DEFINE: '#define';
UNDEF: '#undef';
IFDEF: '#ifdef';
IFNDEF: '#ifndef';
ENDIF: '#endif';

// Python built-ins
PRINT: 'print';
LEN: 'len';
RANGE: 'range';
LIST: 'list';
DICT: 'dict';
SET: 'set';
TUPLE: 'tuple';
ZIP: 'zip';
MAP: 'map';
FILTER: 'filter';
SORTED: 'sorted';

// Parser Rules
program 
    : NEWLINE* statement (NEWLINE+ statement)* NEWLINE* EOF
    ;

statement 
    : guiBlock
    | funcDef
    | classDef
    | interfaceDef
    | enumDef
    | typeDef
    | eventHandler
    | importStmt
    | exportStmt
    | returnStmt
    | throwStmt
    | tryStmt
    | ifStmt
    | forStmt
    | whileStmt
    | doWhileStmt
    | switchStmt
    | withStmt
    | asyncStmt
    | awaitExpr
    | assertStmt
    | breakStmt
    | continueStmt
    | passStmt
    | raiseStmt
    | yieldStmt
    | globalStmt
    | nonlocalStmt
    | deleteStmt
    | exprStmt SEMICOLON?
    | block
    ;

// Expression rules with precedence
expr
    : primary                                               #PrimaryExpr
    | expr DOT ID                                          #DotExpr
    | expr LPAREN argList? RPAREN                          #CallExpr
    | expr LBRACKET expr RBRACKET                          #IndexExpr
    | AWAIT expr                                           #AwaitExpr
    | NEW creator                                          #NewExpr
    | LPAREN typeRef RPAREN expr                          #CastExpr
    | expr op=(INC | DEC)                                 #PostfixExpr
    | op=(ADD | SUB | INC | DEC | NOT | BNOT) expr       #UnaryExpr
    | expr POW expr                                       #PowerExpr
    | expr op=(MUL | DIV | FDIV | MOD) expr              #MultiplicativeExpr
    | expr op=(ADD | SUB) expr                           #AdditiveExpr
    | expr op=(LSH | RSH | URSH) expr                    #ShiftExpr
    | expr op=(LT | GT | LE | GE | INSTANCEOF | IS) expr #RelationalExpr
    | expr op=(EQ | NE) expr                             #EqualityExpr
    | expr BAND expr                                      #BitAndExpr
    | expr BXOR expr                                      #BitXorExpr
    | expr BOR expr                                       #BitOrExpr
    | expr AND expr                                       #LogicalAndExpr
    | expr OR expr                                        #LogicalOrExpr
    | <assoc=right> expr ELVIS expr                      #ElvisExpr
    | <assoc=right> expr QUESTION expr COLON expr        #TernaryExpr
    | <assoc=right> expr
      op=(ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN 
        | DIV_ASSIGN | MOD_ASSIGN | POW_ASSIGN | LSH_ASSIGN 
        | RSH_ASSIGN | URSH_ASSIGN | BAND_ASSIGN 
        | BXOR_ASSIGN | BOR_ASSIGN) expr                 #AssignmentExpr
    | LAMBDA paramList? ARROW expr                       #LambdaExpr
    ;

typeDef
    : TYPE_KW ID LBRACE (typeField (COMMA typeField)*)? RBRACE
    ;

typeField
    : ID COLON typeRef
    ;

typeRef
    : VOID                                                       #VoidType
    | primitiveType                                             #PrimitiveType
    | ID (DOT ID)*                                             #ClassType
    | typeRef LBRACKET RBRACKET                                #ArrayType
    | typeRef LT typeRef (COMMA typeRef)* GT                   #GenericType
    | QUESTION (EXTENDS typeRef | SUPER typeRef)?              #WildcardType
    | LPAREN typeRef (COMMA typeRef)* RPAREN ARROW typeRef    #FunctionType
    ;

primitiveType
    : BOOLEAN | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE | CHAR
    ;

classDef
    : (modifier)* CLASS ID 
      (LT typeParameter (COMMA typeParameter)* GT)?
      (EXTENDS typeRef)?
      (IMPLEMENTS typeRef (COMMA typeRef)*)?
      classBody
    ;

interfaceDef
    : (modifier)* INTERFACE ID
      (LT typeParameter (COMMA typeParameter)* GT)?
      (EXTENDS typeRef (COMMA typeRef)*)?
      interfaceBody
    ;

enumDef
    : (modifier)* ENUM ID (IMPLEMENTS typeRef (COMMA typeRef)*)?
      LBRACE enumConstants? (COMMA)? enumBodyDeclarations? RBRACE
    ;

modifier
    : PUBLIC | PRIVATE | PROTECTED | STATIC | FINAL | ABSTRACT
    | SYNCHRONIZED | NATIVE | STRICTFP | TRANSIENT | VOLATILE
    | ASYNC | CONST
    ;

typeParameter
    : ID (EXTENDS typeRef (BAND typeRef)*)?
    ;

funcDef
    : (PUBLIC? STATIC?)? DEF ID LPAREN paramList? RPAREN 
      (ARROW typeRef)? (COLON suite | block)
    ;

paramList
    : param (COMMA param)*
    ;

param
    : ID (COLON typeRef)?
    ;

suite
    : INDENT statement+ DEDENT
    ;

block
    : LBRACE statement* RBRACE
    ;

importStmt
    : IMPORT (DOT | MUL | ID)+ (AS ID)?
    | FROM (DOT | ID)+ IMPORT (MUL | LPAREN importNames RPAREN | importNames)
    ;

importNames
    : ID (AS ID)? (COMMA ID (AS ID)?)*
    ;

ifStmt
    : IF test COLON suite (ELIF test COLON suite)* (ELSE COLON suite)?
    | IF parExpr block (ELIF parExpr block)* (ELSE block)?
    ;

forStmt
    : FOR LPAREN forControl RPAREN (block | COLON suite)
    | asyncForStmt
    ;

asyncForStmt
    : ASYNC FOR LPAREN forControl RPAREN (block | COLON suite)
    ;

forControl
    : ID IN expr
    | variableDecl IN expr
    | forInit? SEMICOLON expr? SEMICOLON forUpdate?
    ;

whileStmt
    : WHILE parExpr (block | COLON suite)
    ;

doWhileStmt
    : DO block WHILE parExpr SEMICOLON
    ;

tryStmt
    : TRY block 
      (catchClause+ finallyBlock? | finallyBlock)
    ;

catchClause
    : CATCH LPAREN variableModifier* catchType ID RPAREN block
    ;

catchType
    : qualifiedName (BOR qualifiedName)*
    ;

finallyBlock
    : FINALLY block
    ;

switchStmt
    : SWITCH parExpr LBRACE switchBlock* RBRACE
    ;

switchBlock
    : (CASE expr | DEFAULT) COLON statement*
    ;

withStmt
    : WITH expr (AS ID)? COLON suite
    ;

assertStmt
    : ASSERT expr (COMMA expr)?
    ;

yieldStmt
    : YIELD (FROM)? expr
    ;

globalStmt
    : GLOBAL ID (COMMA ID)*
    ;

nonlocalStmt
    : NONLOCAL ID (COMMA ID)*
    ;

returnStmt
    : RETURN expr?
    ;

throwStmt
    : THROW expr
    ;

breakStmt
    : BREAK ID?
    ;

continueStmt
    : CONTINUE ID?
    ;

passStmt
    : PASS
    ;

deleteStmt
    : DEL expr (COMMA expr)*
    ;

raiseStmt
    : RAISE (expr (FROM expr)?)?
    ;
    : LBRACE statement* RBRACE
    ;

exprStmt
    : expr
    ;

expr
    : primary
    | expr op=(MUL | DIV) expr
    | expr op=(PLUS | MINUS) expr
    | expr ARROW ID
    | expr ASSIGN expr
    | expr LPAREN argList? RPAREN
    ;

primary
    : INT
    | FLOAT
    | STRING
    | BOOL
    | ID
    | LPAREN expr RPAREN
    ;

argList
    : expr (COMMA expr)*
    ;

guiBlock
    : GUI COLON suite
    ;

eventHandler
    : ON ID (FROM ID)? DO COLON suite
    ;

// Lexer Rules
GUI : 'gui';
ON : 'on';
DO : 'do';
FROM : 'from';
DEF : 'def';
PUBLIC : 'public';
STATIC : 'static';
TYPE_KW : 'type';
VOID : 'void';

ARROW : '->';
COLON : ':';
COMMA : ',';
SEMICOLON : ';';
ASSIGN : '=';
PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACKET : '[';
RBRACKET : ']';

INT : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]*;
STRING : '"' ~["\r\n]* '"' | '\'' ~['\r\n]* '\'';
BOOL : 'true' | 'false';
ID : [a-zA-Z_][a-zA-Z0-9_]*;

INDENT : 'INDENT';
DEDENT : 'DEDENT';
NEWLINE : [\r\n]+;
WS : [ \t]+ -> skip;
