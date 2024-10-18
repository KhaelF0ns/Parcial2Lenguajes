import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from laplaceGrammarLexer import laplaceGrammarLexer
from laplaceGrammarParser import laplaceGrammarParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = laplaceGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = laplaceGrammarParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
