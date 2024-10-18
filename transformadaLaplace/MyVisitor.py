from laplaceGrammarParser import laplaceGrammarParser
from laplaceGrammarVisitor import laplaceGrammarVisitor

class MyVisitor(laplaceGrammarVisitor):
    
    def visitPrintExpr(self, ctx: laplaceGrammarParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitRetrasoIdeal(self, ctx: laplaceGrammarParser.RetrasoIdealContext):
        tau = ctx.TAU().getText()
        return f"e^(-{tau}*s)"  

    def visitImpulsoUnitario(self, ctx: laplaceGrammarParser.ImpulsoUnitarioContext):
        return "1"  

    def visitAmortiguacionExp(self, ctx: laplaceGrammarParser.AmortiguacionExpContext):
        return "1/(s + a)"

    def visitNesimaPotencia(self, ctx: laplaceGrammarParser.NesimaPotenciaContext):
        n = int(ctx.N().getText())
        print("Por aqui pase")
        return f"{n}!/(s^{n+1})" 

    def visitQesimaPotencia(self, ctx: laplaceGrammarParser.QesimaPotenciaContext):
        q = ctx.Q().getText()
        return f"Γ({q}+1)/s^{q+1}"  

    def visitEscalonUnitario(self, ctx: laplaceGrammarParser.EscalonUnitarioContext):
        return "1/s"

    def visitEscalonRetraso(self, ctx: laplaceGrammarParser.EscalonRetrasoContext):
        tau = ctx.TAU().getText()
        return f"e^(-{tau}*s)/s"  

    def visitSeno(self, ctx: laplaceGrammarParser.SenoContext):
        omega = ctx.OMEGA().getText()
        return f"{omega}/(s^2 + {omega}^2)" 

    def visitCoseno(self, ctx: laplaceGrammarParser.CosenoContext):
        omega = ctx.OMEGA().getText()
        return f"s/(s^2 + {omega}^2)"  # Transformada de Cos(omega * t)

    def visitSenoHiperbolico(self, ctx: laplaceGrammarParser.SenoHiperbolicoContext):
        alpha = ctx.alpha().getText()
        return f"{alpha}/(s^2 - {alpha}^2)"  # Transformada de Sinh(alpha * t)

    def visitCosenoHiperbolico(self, ctx: laplaceGrammarParser.CosenoHiperbolicoContext):
        alpha = ctx.alpha().getText()
        return f"s/(s^2 - {alpha}^2)"  # Transformada de Cosh(alpha * t)

    def visitLogaritmoNatural(self, ctx: laplaceGrammarParser.LogaritmoNaturalContext):
        t0 = ctx.T0().getText()
        log = ctx.LOG().getText()
        return f"(-{log}({t0}*s) + gamma) / s"  # Transformada de log(t/t0)

    def visitFuncionDeBessel(self, ctx: laplaceGrammarParser.FuncionDeBesselContext):
        omega = ctx.OMEGA().getText()
        return f"({omega}^n * (s + (s^2+{omega}^2)^1/2)^-n)/ s^2+{omega}^2)^1/2 "  # Placeholder para función de Bessel

    def visitProg(self, ctx: laplaceGrammarParser.ProgContext):
        results = []
        for stat in ctx.stat():
            results.append(self.visit(stat))
        return results
