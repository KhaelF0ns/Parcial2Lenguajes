# Lenguaje de Análisis de Laplace con ANTLR4

Este repositorio contiene una implementación de un lenguaje de programación personalizado basado en ANTLR4 que permite realizar análisis de transformadas de Laplace. La gramática permite evaluar expresiones matemáticas que representan funciones de transferencia y señales.

## Características
- **Funciones de Delta**: Soporta impulsos unitarios y retrasos ideales.
- **Funciones de Escalon**: Permite el uso de escalones unitarios y escalones con retraso.
- **Cálculos de Amortiguamiento**: Incluye expresiones para amortiguamiento y potencia.
- **Funciones Trigonométricas**: Permite calcular seno, coseno, seno hiperbólico y coseno hiperbólico.
- **Logaritmo Natural y Funciones de Bessel**: Admite operaciones logarítmicas y el uso de funciones especiales.

## Gramática

La gramática del lenguaje está definida en el archivo `laplaceGrammar.g4`. Las principales reglas gramaticales son:
```antlr
grammar laplaceGrammar;

prog:   stat+ EOF;

stat:   expr NEWLINE                #printExpr
    |   NEWLINE                     #blank
    ;

expr:   DELTA '(' T MINUS TAU ')'   #retrasoIdeal
    |   DELTA '(' T ')'             #impulsoUnitario
    |   EULER POW MINUS T           #amortiguacionExp
    |   T POW N MULT EULER POW MINUS ALPHA T #nPotenciaConDesplazamiento
    |   U '(' T ')'                 #escalonUnitario
    |   U '(' T MINUS TAU ')'       #escalonRetraso
    |   T POW N                     #nesimaPotencia
    |   T POW Q                     #qesimaPotencia
    |   SIN '(' OMEGA T ')'         #seno
    |   COS '(' OMEGA T ')'         #coseno 
    |   SINH '(' ALPHA T ')'        #senoHiperbolico
    |   COSH '(' ALPHA T ')'        #cosenoHiperbolico
    |   LOG '(' T DIV T0 ')'        #logaritmoNatural
    |   J '(' OMEGA T ')'           #funcionDeBessel
    ;


DIV:    '/';
MULT:   '*';
POW:    '^';
MINUS:  '-';
DELTA:  'd';
T:      't';
T0:     't0';
Q:      'q';
EULER:  'e';
ALPHA : 'a';
U:      'u';
J:      'J';
N:      'n';
SIN:    'Sin';
COS:    'Cos';
SINH:   'Sinh';
COSH:   'Cosh';
LOG:    'log';
OMEGA:  'w';
TAU:    'tau';

NEWLINE:'\r'? '\n' ;
```

## Uso

### Compilar la gramática ANTLR:

Ejecuta el siguiente comando para generar el código Python:

```sh
antlr4 -visitor -Dlanguage=Python3 laplaceGrammar.g4
```

Esto generará los archivos Python necesarios.

Puedes ejecutar el programa utilizando el script `laplace.py`.

### Ejecución con expresiones de prueba

Para ejecutar el lenguaje con expresiones de prueba predefinidas:

```sh
python3 laplaceGrammar.py t.expr
```

### Ejecución interactiva

Para ingresar tus propias expresiones de manera interactiva:

```sh
python3 laplaceGrammar.py
```

Una vez que se inicie el programa, ingresa tus expresiones matemáticas relacionadas con las transformadas de Laplace y se calcularán los resultados.

Ejemplos de expresiones:

```
d(t-tau)
u(t)
Sin(wt)
log(t/t0)
J(wt)
```
