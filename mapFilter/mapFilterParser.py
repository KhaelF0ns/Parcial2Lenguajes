# Generated from mapFilter.g4 by ANTLR 4.13.2
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
        4,1,44,217,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,1,3,1,
        3,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,8,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,105,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        130,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        145,8,5,1,5,3,5,148,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,157,8,5,
        3,5,159,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,176,8,6,1,7,1,7,1,7,3,7,181,8,7,1,8,1,8,3,8,185,8,8,
        1,8,1,8,1,9,1,9,3,9,191,8,9,1,9,1,9,1,10,1,10,1,10,5,10,198,8,10,
        10,10,12,10,201,9,10,1,10,1,10,1,10,5,10,206,8,10,10,10,12,10,209,
        9,10,3,10,211,8,10,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,3,1,0,21,22,1,0,35,37,2,0,35,35,37,38,249,
        0,27,1,0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,56,1,0,0,0,8,70,1,0,0,0,
        10,158,1,0,0,0,12,175,1,0,0,0,14,180,1,0,0,0,16,182,1,0,0,0,18,188,
        1,0,0,0,20,210,1,0,0,0,22,212,1,0,0,0,24,214,1,0,0,0,26,28,3,2,1,
        0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,
        1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,34,3,4,2,0,34,35,5,43,0,0,
        35,41,1,0,0,0,36,37,3,6,3,0,37,38,5,43,0,0,38,41,1,0,0,0,39,41,5,
        43,0,0,40,33,1,0,0,0,40,36,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,
        43,5,1,0,0,43,44,5,2,0,0,44,45,3,8,4,0,45,46,5,3,0,0,46,51,3,14,
        7,0,47,48,5,3,0,0,48,50,3,14,7,0,49,47,1,0,0,0,50,53,1,0,0,0,51,
        49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,4,0,
        0,55,5,1,0,0,0,56,57,5,5,0,0,57,58,5,2,0,0,58,59,3,8,4,0,59,60,5,
        3,0,0,60,65,3,14,7,0,61,62,5,3,0,0,62,64,3,14,7,0,63,61,1,0,0,0,
        64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,
        0,0,0,68,69,5,4,0,0,69,7,1,0,0,0,70,71,5,6,0,0,71,76,5,36,0,0,72,
        73,5,3,0,0,73,75,5,36,0,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,
        0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,7,0,0,80,81,
        3,10,5,0,81,9,1,0,0,0,82,83,5,36,0,0,83,84,3,12,6,0,84,85,3,22,11,
        0,85,159,1,0,0,0,86,87,5,36,0,0,87,159,5,8,0,0,88,89,5,36,0,0,89,
        159,5,9,0,0,90,91,5,36,0,0,91,159,5,10,0,0,92,95,5,11,0,0,93,96,
        5,36,0,0,94,96,3,14,7,0,95,93,1,0,0,0,95,94,1,0,0,0,96,97,1,0,0,
        0,97,159,5,4,0,0,98,99,5,12,0,0,99,100,5,36,0,0,100,104,5,4,0,0,
        101,102,3,12,6,0,102,103,3,22,11,0,103,105,1,0,0,0,104,101,1,0,0,
        0,104,105,1,0,0,0,105,159,1,0,0,0,106,107,5,13,0,0,107,108,5,36,
        0,0,108,159,5,4,0,0,109,110,5,14,0,0,110,111,5,36,0,0,111,159,5,
        4,0,0,112,113,5,15,0,0,113,114,5,36,0,0,114,159,5,4,0,0,115,116,
        5,36,0,0,116,117,5,16,0,0,117,118,5,38,0,0,118,119,5,3,0,0,119,120,
        5,38,0,0,120,159,5,4,0,0,121,122,5,36,0,0,122,123,5,17,0,0,123,124,
        5,38,0,0,124,159,5,4,0,0,125,126,5,36,0,0,126,129,5,18,0,0,127,130,
        3,14,7,0,128,130,5,36,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,131,
        1,0,0,0,131,159,5,4,0,0,132,133,5,19,0,0,133,134,5,36,0,0,134,159,
        5,4,0,0,135,136,5,20,0,0,136,137,5,36,0,0,137,159,5,4,0,0,138,139,
        5,36,0,0,139,140,3,12,6,0,140,141,3,22,11,0,141,142,3,12,6,0,142,
        144,3,22,11,0,143,145,7,0,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,
        147,1,0,0,0,146,148,3,10,5,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        159,1,0,0,0,149,150,5,36,0,0,150,151,5,23,0,0,151,152,5,35,0,0,152,
        156,5,24,0,0,153,154,3,12,6,0,154,155,3,22,11,0,155,157,1,0,0,0,
        156,153,1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,82,1,0,0,0,158,
        86,1,0,0,0,158,88,1,0,0,0,158,90,1,0,0,0,158,92,1,0,0,0,158,98,1,
        0,0,0,158,106,1,0,0,0,158,109,1,0,0,0,158,112,1,0,0,0,158,115,1,
        0,0,0,158,121,1,0,0,0,158,125,1,0,0,0,158,132,1,0,0,0,158,135,1,
        0,0,0,158,138,1,0,0,0,158,149,1,0,0,0,159,11,1,0,0,0,160,176,5,41,
        0,0,161,176,5,42,0,0,162,176,5,39,0,0,163,176,5,40,0,0,164,176,5,
        25,0,0,165,176,5,26,0,0,166,167,5,27,0,0,167,168,5,36,0,0,168,176,
        5,28,0,0,169,176,5,29,0,0,170,176,5,30,0,0,171,176,5,31,0,0,172,
        176,5,32,0,0,173,176,5,33,0,0,174,176,5,34,0,0,175,160,1,0,0,0,175,
        161,1,0,0,0,175,162,1,0,0,0,175,163,1,0,0,0,175,164,1,0,0,0,175,
        165,1,0,0,0,175,166,1,0,0,0,175,169,1,0,0,0,175,170,1,0,0,0,175,
        171,1,0,0,0,175,172,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,
        13,1,0,0,0,177,181,3,16,8,0,178,181,3,18,9,0,179,181,5,36,0,0,180,
        177,1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,15,1,0,0,0,182,184,
        5,23,0,0,183,185,3,20,10,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,
        1,0,0,0,186,187,5,24,0,0,187,17,1,0,0,0,188,190,5,2,0,0,189,191,
        3,20,10,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,
        5,4,0,0,193,19,1,0,0,0,194,199,3,24,12,0,195,196,5,3,0,0,196,198,
        3,24,12,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,
        1,0,0,0,200,211,1,0,0,0,201,199,1,0,0,0,202,207,3,14,7,0,203,204,
        5,3,0,0,204,206,3,14,7,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,
        1,0,0,0,207,208,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,194,
        1,0,0,0,210,202,1,0,0,0,211,21,1,0,0,0,212,213,7,1,0,0,213,23,1,
        0,0,0,214,215,7,2,0,0,215,25,1,0,0,0,19,29,40,51,65,76,95,104,129,
        144,147,156,158,175,180,184,190,199,207,210
    ]

class mapFilterParser ( Parser ):

    grammarFileName = "mapFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'map'", "'('", "','", "')'", "'filter'", 
                     "'lambda'", "':'", "'.upper()'", "'.lower()'", "'.capitalize()'", 
                     "'sorted('", "'len('", "'sum('", "'max('", "'min('", 
                     "'.replace('", "'.split('", "'.join('", "'abs('", "'round('", 
                     "' and '", "' or '", "'['", "']'", "'%'", "'**'", "'.'", 
                     "'()'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "ID", 
                      "FLOAT", "STRING", "MUL", "DIV", "ADD", "SUB", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_mapFunction = 2
    RULE_filterFunction = 3
    RULE_lambdaExpr = 4
    RULE_function = 5
    RULE_op = 6
    RULE_iterable = 7
    RULE_list = 8
    RULE_tuple = 9
    RULE_elements = 10
    RULE_var = 11
    RULE_expr = 12

    ruleNames =  [ "prog", "stat", "mapFunction", "filterFunction", "lambdaExpr", 
                   "function", "op", "iterable", "list", "tuple", "elements", 
                   "var", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    INT=35
    ID=36
    FLOAT=37
    STRING=38
    MUL=39
    DIV=40
    ADD=41
    SUB=42
    NEWLINE=43
    WS=44

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

        def EOF(self):
            return self.getToken(mapFilterParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.StatContext,i)


        def getRuleIndex(self):
            return mapFilterParser.RULE_prog

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

        localctx = mapFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.stat()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8796093022242) != 0)):
                    break

            self.state = 31
            self.match(mapFilterParser.EOF)
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

        def mapFunction(self):
            return self.getTypedRuleContext(mapFilterParser.MapFunctionContext,0)


        def NEWLINE(self):
            return self.getToken(mapFilterParser.NEWLINE, 0)

        def filterFunction(self):
            return self.getTypedRuleContext(mapFilterParser.FilterFunctionContext,0)


        def getRuleIndex(self):
            return mapFilterParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = mapFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.mapFunction()
                self.state = 34
                self.match(mapFilterParser.NEWLINE)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.filterFunction()
                self.state = 37
                self.match(mapFilterParser.NEWLINE)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(mapFilterParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(mapFilterParser.LambdaExprContext,0)


        def iterable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.IterableContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.IterableContext,i)


        def getRuleIndex(self):
            return mapFilterParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = mapFilterParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(mapFilterParser.T__0)
            self.state = 43
            self.match(mapFilterParser.T__1)
            self.state = 44
            self.lambdaExpr()
            self.state = 45
            self.match(mapFilterParser.T__2)
            self.state = 46
            self.iterable()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 47
                self.match(mapFilterParser.T__2)
                self.state = 48
                self.iterable()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(mapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(mapFilterParser.LambdaExprContext,0)


        def iterable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.IterableContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.IterableContext,i)


        def getRuleIndex(self):
            return mapFilterParser.RULE_filterFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunction" ):
                listener.enterFilterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunction" ):
                listener.exitFilterFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterFunction" ):
                return visitor.visitFilterFunction(self)
            else:
                return visitor.visitChildren(self)




    def filterFunction(self):

        localctx = mapFilterParser.FilterFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(mapFilterParser.T__4)
            self.state = 57
            self.match(mapFilterParser.T__1)
            self.state = 58
            self.lambdaExpr()
            self.state = 59
            self.match(mapFilterParser.T__2)
            self.state = 60
            self.iterable()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 61
                self.match(mapFilterParser.T__2)
                self.state = 62
                self.iterable()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(mapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(mapFilterParser.ID)
            else:
                return self.getToken(mapFilterParser.ID, i)

        def function(self):
            return self.getTypedRuleContext(mapFilterParser.FunctionContext,0)


        def getRuleIndex(self):
            return mapFilterParser.RULE_lambdaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpr(self):

        localctx = mapFilterParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lambdaExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(mapFilterParser.T__5)
            self.state = 71
            self.match(mapFilterParser.ID)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 72
                self.match(mapFilterParser.T__2)
                self.state = 73
                self.match(mapFilterParser.ID)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(mapFilterParser.T__6)
            self.state = 80
            self.function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(mapFilterParser.ID)
            else:
                return self.getToken(mapFilterParser.ID, i)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.OpContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.OpContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.VarContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.VarContext,i)


        def iterable(self):
            return self.getTypedRuleContext(mapFilterParser.IterableContext,0)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(mapFilterParser.STRING)
            else:
                return self.getToken(mapFilterParser.STRING, i)

        def function(self):
            return self.getTypedRuleContext(mapFilterParser.FunctionContext,0)


        def INT(self):
            return self.getToken(mapFilterParser.INT, 0)

        def getRuleIndex(self):
            return mapFilterParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = mapFilterParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(mapFilterParser.ID)
                self.state = 83
                self.op()
                self.state = 84
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(mapFilterParser.ID)
                self.state = 87
                self.match(mapFilterParser.T__7)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(mapFilterParser.ID)
                self.state = 89
                self.match(mapFilterParser.T__8)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(mapFilterParser.ID)
                self.state = 91
                self.match(mapFilterParser.T__9)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(mapFilterParser.T__10)
                self.state = 95
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.match(mapFilterParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 94
                    self.iterable()
                    pass


                self.state = 97
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.match(mapFilterParser.T__11)
                self.state = 99
                self.match(mapFilterParser.ID)
                self.state = 100
                self.match(mapFilterParser.T__3)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8280394956800) != 0):
                    self.state = 101
                    self.op()
                    self.state = 102
                    self.var()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 106
                self.match(mapFilterParser.T__12)
                self.state = 107
                self.match(mapFilterParser.ID)
                self.state = 108
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.match(mapFilterParser.T__13)
                self.state = 110
                self.match(mapFilterParser.ID)
                self.state = 111
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 112
                self.match(mapFilterParser.T__14)
                self.state = 113
                self.match(mapFilterParser.ID)
                self.state = 114
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 115
                self.match(mapFilterParser.ID)
                self.state = 116
                self.match(mapFilterParser.T__15)
                self.state = 117
                self.match(mapFilterParser.STRING)
                self.state = 118
                self.match(mapFilterParser.T__2)
                self.state = 119
                self.match(mapFilterParser.STRING)
                self.state = 120
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 121
                self.match(mapFilterParser.ID)
                self.state = 122
                self.match(mapFilterParser.T__16)
                self.state = 123
                self.match(mapFilterParser.STRING)
                self.state = 124
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 125
                self.match(mapFilterParser.ID)
                self.state = 126
                self.match(mapFilterParser.T__17)
                self.state = 129
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 127
                    self.iterable()
                    pass

                elif la_ == 2:
                    self.state = 128
                    self.match(mapFilterParser.ID)
                    pass


                self.state = 131
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 132
                self.match(mapFilterParser.T__18)
                self.state = 133
                self.match(mapFilterParser.ID)
                self.state = 134
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 135
                self.match(mapFilterParser.T__19)
                self.state = 136
                self.match(mapFilterParser.ID)
                self.state = 137
                self.match(mapFilterParser.T__3)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 138
                self.match(mapFilterParser.ID)
                self.state = 139
                self.op()
                self.state = 140
                self.var()
                self.state = 141
                self.op()
                self.state = 142
                self.var()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21 or _la==22:
                    self.state = 143
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68721113088) != 0):
                    self.state = 146
                    self.function()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 149
                self.match(mapFilterParser.ID)
                self.state = 150
                self.match(mapFilterParser.T__22)
                self.state = 151
                self.match(mapFilterParser.INT)
                self.state = 152
                self.match(mapFilterParser.T__23)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8280394956800) != 0):
                    self.state = 153
                    self.op()
                    self.state = 154
                    self.var()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(mapFilterParser.ADD, 0)

        def SUB(self):
            return self.getToken(mapFilterParser.SUB, 0)

        def MUL(self):
            return self.getToken(mapFilterParser.MUL, 0)

        def DIV(self):
            return self.getToken(mapFilterParser.DIV, 0)

        def ID(self):
            return self.getToken(mapFilterParser.ID, 0)

        def getRuleIndex(self):
            return mapFilterParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = mapFilterParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(mapFilterParser.ADD)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(mapFilterParser.SUB)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(mapFilterParser.MUL)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.match(mapFilterParser.DIV)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.match(mapFilterParser.T__24)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.match(mapFilterParser.T__25)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 7)
                self.state = 166
                self.match(mapFilterParser.T__26)
                self.state = 167
                self.match(mapFilterParser.ID)
                self.state = 168
                self.match(mapFilterParser.T__27)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.match(mapFilterParser.T__28)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 9)
                self.state = 170
                self.match(mapFilterParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 10)
                self.state = 171
                self.match(mapFilterParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 11)
                self.state = 172
                self.match(mapFilterParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 12)
                self.state = 173
                self.match(mapFilterParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 13)
                self.state = 174
                self.match(mapFilterParser.T__33)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(mapFilterParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(mapFilterParser.TupleContext,0)


        def ID(self):
            return self.getToken(mapFilterParser.ID, 0)

        def getRuleIndex(self):
            return mapFilterParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = mapFilterParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iterable)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.tuple_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(mapFilterParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(mapFilterParser.ElementsContext,0)


        def getRuleIndex(self):
            return mapFilterParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = mapFilterParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(mapFilterParser.T__22)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 515404464132) != 0):
                self.state = 183
                self.elements()


            self.state = 186
            self.match(mapFilterParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(mapFilterParser.ElementsContext,0)


        def getRuleIndex(self):
            return mapFilterParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = mapFilterParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(mapFilterParser.T__1)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 515404464132) != 0):
                self.state = 189
                self.elements()


            self.state = 192
            self.match(mapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.ExprContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.ExprContext,i)


        def iterable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mapFilterParser.IterableContext)
            else:
                return self.getTypedRuleContext(mapFilterParser.IterableContext,i)


        def getRuleIndex(self):
            return mapFilterParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = mapFilterParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.expr()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 195
                    self.match(mapFilterParser.T__2)
                    self.state = 196
                    self.expr()
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2, 23, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.iterable()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 203
                    self.match(mapFilterParser.T__2)
                    self.state = 204
                    self.iterable()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(mapFilterParser.ID, 0)

        def INT(self):
            return self.getToken(mapFilterParser.INT, 0)

        def FLOAT(self):
            return self.getToken(mapFilterParser.FLOAT, 0)

        def getRuleIndex(self):
            return mapFilterParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = mapFilterParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def INT(self):
            return self.getToken(mapFilterParser.INT, 0)

        def FLOAT(self):
            return self.getToken(mapFilterParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(mapFilterParser.STRING, 0)

        def getRuleIndex(self):
            return mapFilterParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = mapFilterParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 446676598784) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





