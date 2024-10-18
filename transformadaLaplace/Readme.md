# Laplace Transform Calculator using ANTLR4

This repository contains a Laplace transform calculator based on a custom grammar defined using ANTLR4. The calculator supports various mathematical expressions relevant to Laplace transformations, such as unit steps, delayed impulses, exponential damping, and trigonometric functions.

## Features
- **Laplace-related functions**: Impulse (`d(t)`), unit step (`u(t)`), delayed step (`u(t - tau)`), and exponential damping (`e^(-t)`)
- **Polynomials**: N-th and Q-th power terms (`t^n`, `t^q`)
- **Trigonometric functions**: Sine and cosine (`Sin(wt)`, `Cos(wt)`)
- **Hyperbolic functions**: Hyperbolic sine and cosine (`Sinh(at)`, `Cosh(at)`)
- **Logarithms and Bessel functions**: `log(t/t0)`, Bessel function (`J(wt)`)

## Grammar

The Laplace transform grammar is defined in the `laplace.g4` file. The main grammar rules are as follows:

```antlr
prog:   stat+ EOF;

stat:   expr NEWLINE                            #printExpr
    |   NEWLINE                                 #blank
    ;

expr:   DELTA '(' T MINUS TAU ')'               #retrasoIdeal
    |   DELTA '(' T ')'                         #impulsoUnitario
    |   EULER POW MINUS T                       #amortiguacionExp
    |   T POW N MULT EULER POW MINUS ALPHA T    #nPotenciaConDesplazamiento
    |   U '(' T ')'                             #escalonUnitario
    |   U '(' T MINUS TAU ')'                   #escalonRetraso
    |   T POW N                                 #nesimaPotencia
    |   T POW Q                                 #qesimaPotencia
    |   SIN '('OMEGA T')'                       #seno
    |   COS '('OMEGA T')'                       #coseno 
    |   SINH '('ALPHA T')'                      #senoHiperbolico
    |   COSH '('ALPHA T')'                      #cosenoHiperbolico
    |   LOG '(' T DIV T0')'                     #logaritmoNatural
    |   J   '(' OMEGA T ')'                     #funcionDeBessel
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
