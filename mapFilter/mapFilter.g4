grammar mapFilter;

prog:   stat+ EOF;

stat:   mapFunction NEWLINE
    |   filterFunction NEWLINE
    |   NEWLINE
    ;

mapFunction: 'map' '(' lambdaExpr ',' iterable (',' iterable)* ')' ;

filterFunction: 'filter' '(' lambdaExpr ',' iterable (',' iterable)*')' ;

lambdaExpr: 'lambda' ID (',' ID)* ':' function;

function: ID op var
        | ID'.upper()'
        | ID'.lower()'
        | ID'.capitalize()'
        | 'sorted(' (ID | iterable) ')'
        | 'len(' ID ')'(op var)?
        | 'sum(' ID ')'
        | 'max(' ID ')'
        | 'min(' ID ')'
        | ID'.replace(' STRING ',' STRING ')'
        | ID'.split(' STRING ')'
        | ID'.join(' (iterable | ID) ')'
        | 'abs(' ID ')'
        | 'round(' ID ')'
        | ID op var op var (' and '|' or ')? function?
        | ID'['INT']' (op var)?
        ;

op:   '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '**'
    | '.'ID'()'
    | '=='
    | '!='
    | '<'
    | '>'
    | '<='
    | '>='
    ;

iterable: list
        | tuple
        | ID
        ;

list: '[' elements? ']' ;

tuple: '(' elements? ')' ;

elements: expr (',' expr)*
        | iterable (',' iterable)*
        ;

var:  ID
    | INT
    | FLOAT
    ;

expr: INT
    | FLOAT
    | STRING
    ;

INT: '-'?[0-9]+;
ID: [a-zA-Z][a-zA-Z0-9_]*;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' .*? '"';
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
