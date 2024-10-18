# Lenguaje de Programación para Map y Filter con ANTLR4

Este repositorio contiene una implementación de un lenguaje de programación personalizado basado en ANTLR4 que permite aplicar funciones de mapeo y filtrado a objetos iterables, como listas y tuplas, utilizando expresiones lambda al estilo de Python.

## Características
- **Funciones de mapeo**: Usa `map` para aplicar funciones a cada elemento de un iterable.
- **Funciones de filtrado**: Usa `filter` para seleccionar elementos que cumplen con una condición especificada.
- **Expresiones Lambda**: Soporta la sintaxis de expresiones lambda como `lambda x:`.
- **Operaciones**: Soporta operaciones básicas y manipulaciones en listas y cadenas.

## Gramática

La gramática del lenguaje está definida en el archivo `mapFilter.g4`. Las principales reglas gramaticales son:
```antlr
grammar mapFilter;

prog:   stat+ EOF;

stat:   mapFunction NEWLINE
    |   filterFunction NEWLINE
    |   NEWLINE
    ;

mapFunction: 'map' '(' lambdaExpr ',' iterable (',' iterable)* ')' ;

filterFunction: 'filter' '(' lambdaExpr ',' iterable (',' iterable)* ')' ;

lambdaExpr: 'lambda' ID (',' ID)* ':' function;

function: ID op var
        | ID op STRING
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
NEWLINE:'\r'? '\n' ;     // Retorna nuevas líneas al analizador (es señal de fin de declaración)
WS  :   [ \t]+ -> skip ; // Ignora espacios en blanco
```

## Uso

### Compilar la gramática ANTLR:

Ejecuta el siguiente comando para generar el código Python:

```sh
antlr4 -visitor -Dlanguage=Python3 mapFilter.g4
```

Esto generará los archivos Python necesarios para el analizador léxico y el analizador sintáctico.

Puedes ejecutar el programa utilizando el script mapFilter.py.

### Ejecución con expresiones de prueba

Para ejecutar el lenguaje con expresiones de prueba predefinidas:

```sh
python3 mapFilter.py test_input.txt
```

### Ejecución interactiva

Para ingresar tus propias expresiones de manera interactiva:

```sh
python3 mapFilter.py
```

Una vez que se inicie el programa, ingresa tus expresiones de mapeo o filtrado, y se calcularán los resultados.

Ejemplos de expresiones

```sh
map(lambda x: x * 2, [1, 2, 3, 4])
```

```sh
filter(lambda x: x > 2, (5, 1, 3, 4))
```
