grammar CPJ;

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

// Additional type keywords
BOOLEAN: 'boolean';
BYTE: 'byte';
SHORT: 'short';
LONG: 'long';
DOUBLE: 'double';
CHAR: 'char';

// Other tokens
QUESTION: '?';
NATIVE: 'native';
STRICTFP: 'strictfp';
TRANSIENT: 'transient';
VOLATILE: 'volatile';
NUMBER: INT | FLOAT;
STRING_LITERAL: STRING;
ON: 'on';
EXPORT: 'export';
STAR: '*';
FUNCTION: 'function';

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
    | primitiveType                                             #PrimitiveTypeRef
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
      (COLON suite | classBody)
    ;

interfaceDef
    : (modifier)* INTERFACE ID
      (LT typeParameter (COMMA typeParameter)* GT)?
      (EXTENDS typeRef (COMMA typeRef)*)?
      (COLON suite | interfaceBody)
    ;

enumDef
    : (modifier)* ENUM ID (IMPLEMENTS typeRef (COMMA typeRef)*)?
      (COLON suite | LBRACE enumConstants? (COMMA)? enumBodyDeclarations? RBRACE)
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
    : (modifier)* DEF ID LPAREN paramList? RPAREN
      (ARROW typeRef)? (COLON suite | block)
    | (modifier)* typeRef ID LPAREN paramList? RPAREN
      (COLON suite | block)
    ;

paramList
    : param (COMMA param)*
    ;

param
    : ID (COLON typeRef)?
    | typeRef ID
    ;

suite
    : INDENT statement+ DEDENT
    | statement
    ;

block
    : LBRACE NEWLINE* statement* RBRACE NEWLINE*
    | COLON suite
    ;

importStmt
    : IMPORT (DOT | MUL | ID)+ (AS ID)?
    | FROM (DOT | ID)+ IMPORT (MUL | LPAREN importNames RPAREN | importNames)
    ;

importNames
    : ID (AS ID)? (COMMA ID (AS ID)?)*
    ;

ifStmt
    : IF test block (ELIF test block)* (ELSE block)?
    ;

test
    : parExpr
    | expr
    ;

forStmt
    : FOR LPAREN forControl RPAREN block
    | asyncForStmt
    ;

asyncForStmt
    : ASYNC FOR LPAREN forControl RPAREN block
    ;

forControl
    : ID IN expr
    | variableDecl IN expr
    | forInit? SEMICOLON expr? SEMICOLON forUpdate?
    ;

whileStmt
    : WHILE test block
    ;

doWhileStmt
    : DO block WHILE parExpr SEMICOLON?
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
    : (CASE test | DEFAULT) COLON statement*
    ;

withStmt
    : WITH expr (AS ID)? block
    ;

assertStmt
    : ASSERT expr (COMMA expr)? SEMICOLON?
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

exprStmt
    : expr
    ;

// Previous expr rule removed (using the one defined earlier)

primary
    : NUMBER
    | STRING_LITERAL
    | TRUE
    | FALSE
    | NULL
    | THIS
    | SUPER
    | ID
    | NONE
    | LPAREN expr RPAREN
    | functionLiteral
    | arrayLiteral
    | dictionaryLiteral
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
TYPE_KW : 'type';
COLON : ':';
COMMA : ',';
SEMICOLON : ';';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACKET : '[';
RBRACKET : ']';

INT : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]*;
STRING : '"' ~["\r\n]* '"' | '\'' ~['\r\n]* '\'';
ID : [a-zA-Z_][a-zA-Z0-9_]*;

INDENT : 'INDENT';
DEDENT : 'DEDENT';
NEWLINE : [\r\n]+;
WS : [ \t]+ -> skip;
// Missing rules to add to CPJ.g4

exportStmt
    : EXPORT (DEFAULT | STAR | LBRACE exportList RBRACE) (FROM qualifiedName)?
    ;

exportList
    : ID (AS ID)? (COMMA ID (AS ID)?)*
    ;

parExpr
    : LPAREN expr RPAREN
    ;

variableDecl
    : (FINAL | CONST)? typeRef ID (ASSIGN expr)?
    ;

classBody
    : LBRACE classMember* RBRACE
    ;

classMember
    : (modifier)* (fieldDecl | methodDecl | constructorDecl | classDef)
    ;

interfaceBody
    : LBRACE interfaceMember* RBRACE
    ;

interfaceMember
    : (modifier)* (abstractMethodDecl | defaultMethodDecl | interfaceDef)
    ;

abstractMethodDecl
    : typeRef ID LPAREN paramList? RPAREN SEMICOLON
    ;

defaultMethodDecl
    : DEFAULT typeRef ID LPAREN paramList? RPAREN block
    ;

constructorDecl
    : (modifier)* ID LPAREN paramList? RPAREN block
    ;

methodDecl
    : typeRef ID LPAREN paramList? RPAREN (THROWS typeRef (COMMA typeRef)*)? block
    ;

fieldDecl
    : typeRef ID (ASSIGN expr)? SEMICOLON
    ;

enumConstants
    : enumConstant (COMMA enumConstant)*
    ;

enumConstant
    : ID (LPAREN argList? RPAREN)? (classBody)?
    ;

enumBodyDeclarations
    : SEMICOLON classMember*
    ;

forInit
    : variableDecl
    | expr (COMMA expr)*
    ;

forUpdate
    : expr (COMMA expr)*
    ;

creator
    : nonArrayCreator
    | arrayCreator
    ;

nonArrayCreator
    : typeRef LPAREN argList? RPAREN
    ;

arrayCreator
    : typeRef LBRACKET (expr | RBRACKET (LBRACKET expr? RBRACKET)*) RBRACKET
    ;

functionLiteral
    : FUNCTION? LPAREN paramList? RPAREN (COLON typeRef)? block
    ;

asyncStmt
    : ASYNC (funcDef | withStmt | forStmt)
    ;

arrayLiteral
    : LBRACKET (expr (COMMA expr)* COMMA?)? RBRACKET
    ;

dictionaryLiteral
    : LBRACE (keyValue (COMMA keyValue)* COMMA?)? RBRACE
    ;

keyValue
    : expr COLON expr
    ;

qualifiedName
    : ID (DOT ID)*
    ;

variableModifier
    : FINAL
    | CONST
    ;