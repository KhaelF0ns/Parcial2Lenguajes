# Generated from mapFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .mapFilterParser import mapFilterParser
else:
    from mapFilterParser import mapFilterParser

# This class defines a complete listener for a parse tree produced by mapFilterParser.
class mapFilterListener(ParseTreeListener):

    # Enter a parse tree produced by mapFilterParser#prog.
    def enterProg(self, ctx:mapFilterParser.ProgContext):
        pass

    # Exit a parse tree produced by mapFilterParser#prog.
    def exitProg(self, ctx:mapFilterParser.ProgContext):
        pass


    # Enter a parse tree produced by mapFilterParser#stat.
    def enterStat(self, ctx:mapFilterParser.StatContext):
        pass

    # Exit a parse tree produced by mapFilterParser#stat.
    def exitStat(self, ctx:mapFilterParser.StatContext):
        pass


    # Enter a parse tree produced by mapFilterParser#mapFunction.
    def enterMapFunction(self, ctx:mapFilterParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by mapFilterParser#mapFunction.
    def exitMapFunction(self, ctx:mapFilterParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by mapFilterParser#filterFunction.
    def enterFilterFunction(self, ctx:mapFilterParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by mapFilterParser#filterFunction.
    def exitFilterFunction(self, ctx:mapFilterParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by mapFilterParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:mapFilterParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by mapFilterParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:mapFilterParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by mapFilterParser#function.
    def enterFunction(self, ctx:mapFilterParser.FunctionContext):
        pass

    # Exit a parse tree produced by mapFilterParser#function.
    def exitFunction(self, ctx:mapFilterParser.FunctionContext):
        pass


    # Enter a parse tree produced by mapFilterParser#op.
    def enterOp(self, ctx:mapFilterParser.OpContext):
        pass

    # Exit a parse tree produced by mapFilterParser#op.
    def exitOp(self, ctx:mapFilterParser.OpContext):
        pass


    # Enter a parse tree produced by mapFilterParser#iterable.
    def enterIterable(self, ctx:mapFilterParser.IterableContext):
        pass

    # Exit a parse tree produced by mapFilterParser#iterable.
    def exitIterable(self, ctx:mapFilterParser.IterableContext):
        pass


    # Enter a parse tree produced by mapFilterParser#list.
    def enterList(self, ctx:mapFilterParser.ListContext):
        pass

    # Exit a parse tree produced by mapFilterParser#list.
    def exitList(self, ctx:mapFilterParser.ListContext):
        pass


    # Enter a parse tree produced by mapFilterParser#tuple.
    def enterTuple(self, ctx:mapFilterParser.TupleContext):
        pass

    # Exit a parse tree produced by mapFilterParser#tuple.
    def exitTuple(self, ctx:mapFilterParser.TupleContext):
        pass


    # Enter a parse tree produced by mapFilterParser#elements.
    def enterElements(self, ctx:mapFilterParser.ElementsContext):
        pass

    # Exit a parse tree produced by mapFilterParser#elements.
    def exitElements(self, ctx:mapFilterParser.ElementsContext):
        pass


    # Enter a parse tree produced by mapFilterParser#var.
    def enterVar(self, ctx:mapFilterParser.VarContext):
        pass

    # Exit a parse tree produced by mapFilterParser#var.
    def exitVar(self, ctx:mapFilterParser.VarContext):
        pass


    # Enter a parse tree produced by mapFilterParser#expr.
    def enterExpr(self, ctx:mapFilterParser.ExprContext):
        pass

    # Exit a parse tree produced by mapFilterParser#expr.
    def exitExpr(self, ctx:mapFilterParser.ExprContext):
        pass



del mapFilterParser