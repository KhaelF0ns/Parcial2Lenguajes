import sys
from antlr4 import *
from mapFilterLexer import mapFilterLexer
from mapFilterParser import mapFilterParser
from MyVisitor import MyVisitor

def process_line(line, visitor):
    input_stream = InputStream(line)
    lexer = mapFilterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = mapFilterParser(token_stream)
    tree = parser.prog()

    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"Error al procesar la línea: {line.strip()}")
        print(e)


if __name__ == '__main__':
    visitor = MyVisitor()

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                print(line, end="")
                process_line(line, visitor)
    else:
        try:
            line = input()
            process_line(line, visitor)
        except EOFError:
            pass
