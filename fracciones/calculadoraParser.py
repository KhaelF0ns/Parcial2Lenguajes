# Generated from calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,42,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,29,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,
        2,0,1,4,3,0,2,4,0,2,1,0,3,4,1,0,5,6,44,0,7,1,0,0,0,2,11,1,0,0,0,
        4,28,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,9,0,0,13,3,1,0,0,0,14,
        15,6,2,-1,0,15,16,5,6,0,0,16,29,3,4,2,6,17,18,5,7,0,0,18,19,3,4,
        2,0,19,20,5,7,0,0,20,29,1,0,0,0,21,22,5,8,0,0,22,23,5,4,0,0,23,29,
        5,8,0,0,24,25,5,1,0,0,25,26,3,4,2,0,26,27,5,2,0,0,27,29,1,0,0,0,
        28,14,1,0,0,0,28,17,1,0,0,0,28,21,1,0,0,0,28,24,1,0,0,0,29,38,1,
        0,0,0,30,31,10,5,0,0,31,32,7,0,0,0,32,37,3,4,2,6,33,34,10,4,0,0,
        34,35,7,1,0,0,35,37,3,4,2,5,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,4,9,
        28,36,38
    ]

class calculadoraParser ( Parser ):

    grammarFileName = "calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
                     "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "ABS", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MUL=3
    DIV=4
    ADD=5
    SUB=6
    ABS=7
    INT=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.StatContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.StatContext,i)


        def getRuleIndex(self):
            return calculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = calculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 450) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calculadoraParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(calculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = calculadoraParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            localctx = calculadoraParser.PrintExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.expr(0)
            self.state = 12
            self.match(calculadoraParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calculadoraParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraParser.ABS)
            else:
                return self.getToken(calculadoraParser.ABS, i)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(calculadoraParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative" ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def MUL(self):
            return self.getToken(calculadoraParser.MUL, 0)
        def DIV(self):
            return self.getToken(calculadoraParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def ADD(self):
            return self.getToken(calculadoraParser.ADD, 0)
        def SUB(self):
            return self.getToken(calculadoraParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class FractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(calculadoraParser.INT)
            else:
                return self.getToken(calculadoraParser.INT, i)
        def DIV(self):
            return self.getToken(calculadoraParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFract" ):
                listener.enterFract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFract" ):
                listener.exitFract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFract" ):
                return visitor.visitFract(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculadoraParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = calculadoraParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(calculadoraParser.SUB)
                self.state = 16
                self.expr(6)
                pass
            elif token in [7]:
                localctx = calculadoraParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(calculadoraParser.ABS)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(calculadoraParser.ABS)
                pass
            elif token in [8]:
                localctx = calculadoraParser.FractContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(calculadoraParser.INT)
                self.state = 22
                self.match(calculadoraParser.DIV)
                self.state = 23
                self.match(calculadoraParser.INT)
                pass
            elif token in [1]:
                localctx = calculadoraParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(calculadoraParser.T__0)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(calculadoraParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraParser.MulDivContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraParser.AddSubContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(5)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




