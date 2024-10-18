from calculadoraVisitor import calculadoraVisitor
from calculadoraParser import calculadoraParser
from fractions import Fraction


class MyVisitor(calculadoraVisitor):

    def __init__(self):
        self.memory = {}

    def visitPrintExpr(self, ctx: calculadoraParser.PrintExprContext):
        value = self.visit(ctx.expr())
        fract = Fraction(value)
        return f"= {fract.numerator}/{fract.denominator}"

    def visitFract(self, ctx):
        return Fraction(ctx.getText())

    def visitNegative(self, ctx: calculadoraParser.NegativeContext):
        value = self.visit(ctx.expr())
        return -value

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraParser.MUL:
            return left * right
        if right == 0:
            raise ValueError("Error: Division por cero")
        return left / right

    def visitAbs(self, ctx):
        value = self.visit(ctx.expr())
        return abs(value)

    def visitAddSub(self, ctx: calculadoraParser.AddSubContext):
        
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        if ctx.op.type == calculadoraParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
