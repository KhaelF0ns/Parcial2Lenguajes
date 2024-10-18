# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete listener for a parse tree produced by calculadoraParser.
class calculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraParser#prog.
    def enterProg(self, ctx:calculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by calculadoraParser#prog.
    def exitProg(self, ctx:calculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by calculadoraParser#printExpr.
    def enterPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#printExpr.
    def exitPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#parens.
    def enterParens(self, ctx:calculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by calculadoraParser#parens.
    def exitParens(self, ctx:calculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Abs.
    def enterAbs(self, ctx:calculadoraParser.AbsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Abs.
    def exitAbs(self, ctx:calculadoraParser.AbsContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Negative.
    def enterNegative(self, ctx:calculadoraParser.NegativeContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Negative.
    def exitNegative(self, ctx:calculadoraParser.NegativeContext):
        pass


    # Enter a parse tree produced by calculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by calculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by calculadoraParser#AddSub.
    def enterAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by calculadoraParser#AddSub.
    def exitAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Fract.
    def enterFract(self, ctx:calculadoraParser.FractContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Fract.
    def exitFract(self, ctx:calculadoraParser.FractContext):
        pass



del calculadoraParser