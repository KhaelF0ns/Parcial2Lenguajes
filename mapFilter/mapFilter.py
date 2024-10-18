import sys
from antlr4 import *
from mapFilterLexer import mapFilterLexer
from mapFilterParser import mapFilterParser
from mapFilterVisitor import mapFilterVisitor

from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = mapFilterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = mapFilterParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
