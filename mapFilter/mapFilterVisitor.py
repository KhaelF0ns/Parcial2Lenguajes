# Generated from mapFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .mapFilterParser import mapFilterParser
else:
    from mapFilterParser import mapFilterParser

# This class defines a complete generic visitor for a parse tree produced by mapFilterParser.

class mapFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mapFilterParser#prog.
    def visitProg(self, ctx:mapFilterParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#stat.
    def visitStat(self, ctx:mapFilterParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#mapFunction.
    def visitMapFunction(self, ctx:mapFilterParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#filterFunction.
    def visitFilterFunction(self, ctx:mapFilterParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:mapFilterParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#function.
    def visitFunction(self, ctx:mapFilterParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#op.
    def visitOp(self, ctx:mapFilterParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#iterable.
    def visitIterable(self, ctx:mapFilterParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#list.
    def visitList(self, ctx:mapFilterParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#tuple.
    def visitTuple(self, ctx:mapFilterParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#elements.
    def visitElements(self, ctx:mapFilterParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#var.
    def visitVar(self, ctx:mapFilterParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mapFilterParser#expr.
    def visitExpr(self, ctx:mapFilterParser.ExprContext):
        return self.visitChildren(ctx)



del mapFilterParser