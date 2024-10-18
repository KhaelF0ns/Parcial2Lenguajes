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
prog: stat+ EOF;

stat: expr NEWLINE # printExpr
| NEWLINE # blank
;

expr: '-' expr # Negativo
| expr op=('*'|'/') expr # MulDiv
| expr op=('+'|'-') expr # AddSub
| ABS expr ABS # AbsExpr
| INT '/' INT # readFraction
| '(' expr ')' # paréntesis
;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
ABS : '|' ;
INT : [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS : [ \t]+ -> skip ;
```

## Instalación

### Requisitos previos

- **ANTLR4**: Asegúrese de que ANTLR4 esté instalado en su máquina. Puedes instalarlo siguiendo las instrucciones del [sitio web oficial](https://www.antlr.org/).
- **Python 3.x**: Asegúrate de que Python esté instalado.

### Pasos

1. **Instalar pip** (si aún no está instalado):

```bash
sudo apt install python-pip
```

2. **Configurar un entorno virtual**:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar las bibliotecas y dependencias requeridas**:

```bash
pip install -r requirements.txt
```

4. 

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
