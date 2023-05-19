# Generated from sasm.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sasmParser import sasmParser
else:
    from sasmParser import sasmParser

# This class defines a complete listener for a parse tree produced by sasmParser.
class sasmListener(ParseTreeListener):

    # Enter a parse tree produced by sasmParser#prog.
    def enterProg(self, ctx:sasmParser.ProgContext):
        pass

    # Exit a parse tree produced by sasmParser#prog.
    def exitProg(self, ctx:sasmParser.ProgContext):
        pass


    # Enter a parse tree produced by sasmParser#datadef.
    def enterDatadef(self, ctx:sasmParser.DatadefContext):
        pass

    # Exit a parse tree produced by sasmParser#datadef.
    def exitDatadef(self, ctx:sasmParser.DatadefContext):
        pass


    # Enter a parse tree produced by sasmParser#linecode.
    def enterLinecode(self, ctx:sasmParser.LinecodeContext):
        pass

    # Exit a parse tree produced by sasmParser#linecode.
    def exitLinecode(self, ctx:sasmParser.LinecodeContext):
        pass


    # Enter a parse tree produced by sasmParser#address.
    def enterAddress(self, ctx:sasmParser.AddressContext):
        pass

    # Exit a parse tree produced by sasmParser#address.
    def exitAddress(self, ctx:sasmParser.AddressContext):
        pass


    # Enter a parse tree produced by sasmParser#number.
    def enterNumber(self, ctx:sasmParser.NumberContext):
        pass

    # Exit a parse tree produced by sasmParser#number.
    def exitNumber(self, ctx:sasmParser.NumberContext):
        pass


    # Enter a parse tree produced by sasmParser#comment.
    def enterComment(self, ctx:sasmParser.CommentContext):
        pass

    # Exit a parse tree produced by sasmParser#comment.
    def exitComment(self, ctx:sasmParser.CommentContext):
        pass


    # Enter a parse tree produced by sasmParser#opcode.
    def enterOpcode(self, ctx:sasmParser.OpcodeContext):
        pass

    # Exit a parse tree produced by sasmParser#opcode.
    def exitOpcode(self, ctx:sasmParser.OpcodeContext):
        pass



del sasmParser