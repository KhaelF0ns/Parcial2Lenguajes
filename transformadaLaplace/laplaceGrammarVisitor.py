# Generated from laplaceGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .laplaceGrammarParser import laplaceGrammarParser
else:
    from laplaceGrammarParser import laplaceGrammarParser

# This class defines a complete generic visitor for a parse tree produced by laplaceGrammarParser.

class laplaceGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by laplaceGrammarParser#prog.
    def visitProg(self, ctx:laplaceGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#printExpr.
    def visitPrintExpr(self, ctx:laplaceGrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#blank.
    def visitBlank(self, ctx:laplaceGrammarParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#retrasoIdeal.
    def visitRetrasoIdeal(self, ctx:laplaceGrammarParser.RetrasoIdealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#impulsoUnitario.
    def visitImpulsoUnitario(self, ctx:laplaceGrammarParser.ImpulsoUnitarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#amortiguacionExp.
    def visitAmortiguacionExp(self, ctx:laplaceGrammarParser.AmortiguacionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#nPotenciaConDesplazamiento.
    def visitNPotenciaConDesplazamiento(self, ctx:laplaceGrammarParser.NPotenciaConDesplazamientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#escalonUnitario.
    def visitEscalonUnitario(self, ctx:laplaceGrammarParser.EscalonUnitarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#escalonRetraso.
    def visitEscalonRetraso(self, ctx:laplaceGrammarParser.EscalonRetrasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#nesimaPotencia.
    def visitNesimaPotencia(self, ctx:laplaceGrammarParser.NesimaPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#qesimaPotencia.
    def visitQesimaPotencia(self, ctx:laplaceGrammarParser.QesimaPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#seno.
    def visitSeno(self, ctx:laplaceGrammarParser.SenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#coseno.
    def visitCoseno(self, ctx:laplaceGrammarParser.CosenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#senoHiperbolico.
    def visitSenoHiperbolico(self, ctx:laplaceGrammarParser.SenoHiperbolicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#cosenoHiperbolico.
    def visitCosenoHiperbolico(self, ctx:laplaceGrammarParser.CosenoHiperbolicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#logaritmoNatural.
    def visitLogaritmoNatural(self, ctx:laplaceGrammarParser.LogaritmoNaturalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by laplaceGrammarParser#funcionDeBessel.
    def visitFuncionDeBessel(self, ctx:laplaceGrammarParser.FuncionDeBesselContext):
        return self.visitChildren(ctx)



del laplaceGrammarParser