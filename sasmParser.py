# Generated from sasm.g4 by ANTLR 4.12.0
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
        4,1,11,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,3,0,18,8,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,
        1,0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,
        9,0,3,0,41,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,55,8,1,10,1,12,1,58,9,1,3,1,60,8,1,1,2,1,2,1,2,3,2,65,8,2,1,2,
        3,2,68,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,87,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,97,0,17,1,
        0,0,0,2,59,1,0,0,0,4,67,1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,73,
        1,0,0,0,12,86,1,0,0,0,14,15,3,2,1,0,15,16,5,10,0,0,16,18,1,0,0,0,
        17,14,1,0,0,0,17,18,1,0,0,0,18,22,1,0,0,0,19,21,5,10,0,0,20,19,1,
        0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,40,1,0,0,0,24,
        22,1,0,0,0,25,26,3,4,2,0,26,27,5,10,0,0,27,29,1,0,0,0,28,25,1,0,
        0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,
        1,0,0,0,33,37,3,4,2,0,34,36,5,10,0,0,35,34,1,0,0,0,36,39,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,40,30,1,
        0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,
        45,5,2,0,0,45,60,5,8,0,0,46,47,5,2,0,0,47,48,5,8,0,0,48,49,5,1,0,
        0,49,60,5,8,0,0,50,51,5,2,0,0,51,56,5,8,0,0,52,53,5,1,0,0,53,55,
        5,8,0,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,
        57,60,1,0,0,0,58,56,1,0,0,0,59,44,1,0,0,0,59,46,1,0,0,0,59,50,1,
        0,0,0,60,3,1,0,0,0,61,62,3,8,4,0,62,64,3,12,6,0,63,65,3,10,5,0,64,
        63,1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,68,3,10,5,0,67,61,1,0,
        0,0,67,66,1,0,0,0,68,5,1,0,0,0,69,70,5,7,0,0,70,7,1,0,0,0,71,72,
        5,8,0,0,72,9,1,0,0,0,73,74,5,9,0,0,74,11,1,0,0,0,75,76,5,3,0,0,76,
        87,5,7,0,0,77,87,5,4,0,0,78,87,5,5,0,0,79,80,5,5,0,0,80,87,5,7,0,
        0,81,87,5,6,0,0,82,83,5,6,0,0,83,87,5,7,0,0,84,85,5,6,0,0,85,87,
        5,8,0,0,86,75,1,0,0,0,86,77,1,0,0,0,86,78,1,0,0,0,86,79,1,0,0,0,
        86,81,1,0,0,0,86,82,1,0,0,0,86,84,1,0,0,0,87,13,1,0,0,0,10,17,22,
        30,37,40,56,59,64,67,86
    ]

class sasmParser ( Parser ):

    grammarFileName = "sasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'DATA'", "<INVALID>", "<INVALID>", 
                     "'POP'", "'PUSH'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DATA", "JUMPS", "OPCODEZERO", 
                      "POP", "PUSH", "ADR", "NUMBER", "COMMENT", "EOL", 
                      "WS" ]

    RULE_prog = 0
    RULE_datadef = 1
    RULE_linecode = 2
    RULE_address = 3
    RULE_number = 4
    RULE_comment = 5
    RULE_opcode = 6

    ruleNames =  [ "prog", "datadef", "linecode", "address", "number", "comment", 
                   "opcode" ]

    EOF = Token.EOF
    T__0=1
    DATA=2
    JUMPS=3
    OPCODEZERO=4
    POP=5
    PUSH=6
    ADR=7
    NUMBER=8
    COMMENT=9
    EOL=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(sasmParser.EOF, 0)

        def datadef(self):
            return self.getTypedRuleContext(sasmParser.DatadefContext,0)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(sasmParser.EOL)
            else:
                return self.getToken(sasmParser.EOL, i)

        def linecode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sasmParser.LinecodeContext)
            else:
                return self.getTypedRuleContext(sasmParser.LinecodeContext,i)


        def getRuleIndex(self):
            return sasmParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = sasmParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 14
                self.datadef()
                self.state = 15
                self.match(sasmParser.EOL)


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 19
                self.match(sasmParser.EOL)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 25
                        self.linecode()
                        self.state = 26
                        self.match(sasmParser.EOL) 
                    self.state = 32
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 33
                self.linecode()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 34
                    self.match(sasmParser.EOL)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 42
            self.match(sasmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatadefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(sasmParser.DATA, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(sasmParser.NUMBER)
            else:
                return self.getToken(sasmParser.NUMBER, i)

        def getRuleIndex(self):
            return sasmParser.RULE_datadef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatadef" ):
                listener.enterDatadef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatadef" ):
                listener.exitDatadef(self)




    def datadef(self):

        localctx = sasmParser.DatadefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datadef)
        self._la = 0 # Token type
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(sasmParser.DATA)
                self.state = 45
                self.match(sasmParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(sasmParser.DATA)
                self.state = 47
                self.match(sasmParser.NUMBER)
                self.state = 48
                self.match(sasmParser.T__0)
                self.state = 49
                self.match(sasmParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(sasmParser.DATA)
                self.state = 51
                self.match(sasmParser.NUMBER)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 52
                    self.match(sasmParser.T__0)
                    self.state = 53
                    self.match(sasmParser.NUMBER)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinecodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(sasmParser.NumberContext,0)


        def opcode(self):
            return self.getTypedRuleContext(sasmParser.OpcodeContext,0)


        def comment(self):
            return self.getTypedRuleContext(sasmParser.CommentContext,0)


        def getRuleIndex(self):
            return sasmParser.RULE_linecode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinecode" ):
                listener.enterLinecode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinecode" ):
                listener.exitLinecode(self)




    def linecode(self):

        localctx = sasmParser.LinecodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_linecode)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.number()
                self.state = 62
                self.opcode()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 63
                    self.comment()


                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.comment()
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


    class AddressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADR(self):
            return self.getToken(sasmParser.ADR, 0)

        def getRuleIndex(self):
            return sasmParser.RULE_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddress" ):
                listener.enterAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddress" ):
                listener.exitAddress(self)




    def address(self):

        localctx = sasmParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(sasmParser.ADR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(sasmParser.NUMBER, 0)

        def getRuleIndex(self):
            return sasmParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = sasmParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(sasmParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(sasmParser.COMMENT, 0)

        def getRuleIndex(self):
            return sasmParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = sasmParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(sasmParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JUMPS(self):
            return self.getToken(sasmParser.JUMPS, 0)

        def ADR(self):
            return self.getToken(sasmParser.ADR, 0)

        def OPCODEZERO(self):
            return self.getToken(sasmParser.OPCODEZERO, 0)

        def POP(self):
            return self.getToken(sasmParser.POP, 0)

        def PUSH(self):
            return self.getToken(sasmParser.PUSH, 0)

        def NUMBER(self):
            return self.getToken(sasmParser.NUMBER, 0)

        def getRuleIndex(self):
            return sasmParser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)




    def opcode(self):

        localctx = sasmParser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_opcode)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(sasmParser.JUMPS)
                self.state = 76
                self.match(sasmParser.ADR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(sasmParser.OPCODEZERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(sasmParser.POP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(sasmParser.POP)
                self.state = 80
                self.match(sasmParser.ADR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.match(sasmParser.PUSH)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(sasmParser.PUSH)
                self.state = 83
                self.match(sasmParser.ADR)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.match(sasmParser.PUSH)
                self.state = 85
                self.match(sasmParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





