# Calculadora de fracciones con ANTLR4

Este repositorio contiene una calculadora de fracciones basada en una gramática personalizada definida con ANTLR4. La calculadora admite operaciones con fracciones como suma, resta, multiplicación y división, así como cálculos de negación y valor absoluto.

## Características
- **Aritmética básica**: `+`, `-`, `*`, `/`
- **Compatibilidad con fracciones**: Operaciones aritméticas entre fracciones
- **Valores absolutos**: Encapsula expresiones con símbolos `|` para calcular valores absolutos
- **Negación**: Negación con el operador `-`

## Gramática

La gramática de la calculadora está definida en el archivo `calculadora.g4`. Las principales reglas gramaticales son:
```antlr
grammar calculadora;

prog:   stat+;

stat:   expr NEWLINE                # printExpr
    ;

expr:   '-' expr                    # Negative
    |   expr op=('*'|'/') expr      # MulDiv 
    |   expr op=('+'|'-') expr      # AddSub
    |   ABS expr ABS                # Abs
    |   INT '/' INT                 # Fract
    |   '(' expr ')'                # parens
    ;

MUL     : '*' ;
DIV     : '/' ;
ADD     : '+' ;
SUB     : '-' ;
ABS     : '|' ;
INT     : [0-9]+ ;
NEWLINE:'\r'? '\n' ;                         
WS      : [ \t]+ -> skip ;
```

## Uso

### Compilar la gramática ANTLR:

Ejecutar el siguiente comando para generar el código Python:

```bash
antlr4 -visitor -Dlanguage=Python3 calculadora.g4
```

Esto generará los archivos Python necesarios para el analizador léxico y el analizador sintáctico.

Puede ejecutar la calculadora utilizando el script `calc.py`.

### Ejecución con expresiones de prueba

Para ejecutar la calculadora con expresiones de prueba predefinidas:

```bash
python3 calc.py t.expr
```

### Ejecución interactiva

Para ingresar sus propias expresiones de manera interactiva:

```bash
python3 calc.py
```

Una vez que se inicia el programa, ingrese sus expresiones matemáticas y calculará el resultado.

### Expresiones de ejemplo

```txt
1 / 2 + 3 / 4
| -1 / 2 |
- (3 / 4)
```
