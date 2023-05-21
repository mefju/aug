# Generated from Simple.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#prog.
    def enterProg(self, ctx:SimpleParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleParser#prog.
    def exitProg(self, ctx:SimpleParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleParser#BRACKETEXPR.
    def enterBRACKETEXPR(self, ctx:SimpleParser.BRACKETEXPRContext):
        pass

    # Exit a parse tree produced by SimpleParser#BRACKETEXPR.
    def exitBRACKETEXPR(self, ctx:SimpleParser.BRACKETEXPRContext):
        pass


    # Enter a parse tree produced by SimpleParser#NUMER.
    def enterNUMER(self, ctx:SimpleParser.NUMERContext):
        pass

    # Exit a parse tree produced by SimpleParser#NUMER.
    def exitNUMER(self, ctx:SimpleParser.NUMERContext):
        pass


    # Enter a parse tree produced by SimpleParser#ADDEXP.
    def enterADDEXP(self, ctx:SimpleParser.ADDEXPContext):
        pass

    # Exit a parse tree produced by SimpleParser#ADDEXP.
    def exitADDEXP(self, ctx:SimpleParser.ADDEXPContext):
        pass


    # Enter a parse tree produced by SimpleParser#IDENTNUM.
    def enterIDENTNUM(self, ctx:SimpleParser.IDENTNUMContext):
        pass

    # Exit a parse tree produced by SimpleParser#IDENTNUM.
    def exitIDENTNUM(self, ctx:SimpleParser.IDENTNUMContext):
        pass


    # Enter a parse tree produced by SimpleParser#MULEXP.
    def enterMULEXP(self, ctx:SimpleParser.MULEXPContext):
        pass

    # Exit a parse tree produced by SimpleParser#MULEXP.
    def exitMULEXP(self, ctx:SimpleParser.MULEXPContext):
        pass


    # Enter a parse tree produced by SimpleParser#NOT.
    def enterNOT(self, ctx:SimpleParser.NOTContext):
        pass

    # Exit a parse tree produced by SimpleParser#NOT.
    def exitNOT(self, ctx:SimpleParser.NOTContext):
        pass


    # Enter a parse tree produced by SimpleParser#OR.
    def enterOR(self, ctx:SimpleParser.ORContext):
        pass

    # Exit a parse tree produced by SimpleParser#OR.
    def exitOR(self, ctx:SimpleParser.ORContext):
        pass


    # Enter a parse tree produced by SimpleParser#AND.
    def enterAND(self, ctx:SimpleParser.ANDContext):
        pass

    # Exit a parse tree produced by SimpleParser#AND.
    def exitAND(self, ctx:SimpleParser.ANDContext):
        pass


    # Enter a parse tree produced by SimpleParser#REL.
    def enterREL(self, ctx:SimpleParser.RELContext):
        pass

    # Exit a parse tree produced by SimpleParser#REL.
    def exitREL(self, ctx:SimpleParser.RELContext):
        pass


    # Enter a parse tree produced by SimpleParser#TRUE.
    def enterTRUE(self, ctx:SimpleParser.TRUEContext):
        pass

    # Exit a parse tree produced by SimpleParser#TRUE.
    def exitTRUE(self, ctx:SimpleParser.TRUEContext):
        pass


    # Enter a parse tree produced by SimpleParser#FALSE.
    def enterFALSE(self, ctx:SimpleParser.FALSEContext):
        pass

    # Exit a parse tree produced by SimpleParser#FALSE.
    def exitFALSE(self, ctx:SimpleParser.FALSEContext):
        pass


    # Enter a parse tree produced by SimpleParser#BRACKETEXPRBOOL.
    def enterBRACKETEXPRBOOL(self, ctx:SimpleParser.BRACKETEXPRBOOLContext):
        pass

    # Exit a parse tree produced by SimpleParser#BRACKETEXPRBOOL.
    def exitBRACKETEXPRBOOL(self, ctx:SimpleParser.BRACKETEXPRBOOLContext):
        pass


    # Enter a parse tree produced by SimpleParser#rel.
    def enterRel(self, ctx:SimpleParser.RelContext):
        pass

    # Exit a parse tree produced by SimpleParser#rel.
    def exitRel(self, ctx:SimpleParser.RelContext):
        pass


    # Enter a parse tree produced by SimpleParser#mul_op.
    def enterMul_op(self, ctx:SimpleParser.Mul_opContext):
        pass

    # Exit a parse tree produced by SimpleParser#mul_op.
    def exitMul_op(self, ctx:SimpleParser.Mul_opContext):
        pass


    # Enter a parse tree produced by SimpleParser#add_op.
    def enterAdd_op(self, ctx:SimpleParser.Add_opContext):
        pass

    # Exit a parse tree produced by SimpleParser#add_op.
    def exitAdd_op(self, ctx:SimpleParser.Add_opContext):
        pass


    # Enter a parse tree produced by SimpleParser#simple_instr.
    def enterSimple_instr(self, ctx:SimpleParser.Simple_instrContext):
        pass

    # Exit a parse tree produced by SimpleParser#simple_instr.
    def exitSimple_instr(self, ctx:SimpleParser.Simple_instrContext):
        pass


    # Enter a parse tree produced by SimpleParser#block_instr.
    def enterBlock_instr(self, ctx:SimpleParser.Block_instrContext):
        pass

    # Exit a parse tree produced by SimpleParser#block_instr.
    def exitBlock_instr(self, ctx:SimpleParser.Block_instrContext):
        pass


    # Enter a parse tree produced by SimpleParser#exit_stat.
    def enterExit_stat(self, ctx:SimpleParser.Exit_statContext):
        pass

    # Exit a parse tree produced by SimpleParser#exit_stat.
    def exitExit_stat(self, ctx:SimpleParser.Exit_statContext):
        pass


    # Enter a parse tree produced by SimpleParser#instr.
    def enterInstr(self, ctx:SimpleParser.InstrContext):
        pass

    # Exit a parse tree produced by SimpleParser#instr.
    def exitInstr(self, ctx:SimpleParser.InstrContext):
        pass


    # Enter a parse tree produced by SimpleParser#GOTO.
    def enterGOTO(self, ctx:SimpleParser.GOTOContext):
        pass

    # Exit a parse tree produced by SimpleParser#GOTO.
    def exitGOTO(self, ctx:SimpleParser.GOTOContext):
        pass


    # Enter a parse tree produced by SimpleParser#goto_target.
    def enterGoto_target(self, ctx:SimpleParser.Goto_targetContext):
        pass

    # Exit a parse tree produced by SimpleParser#goto_target.
    def exitGoto_target(self, ctx:SimpleParser.Goto_targetContext):
        pass


    # Enter a parse tree produced by SimpleParser#output_stat.
    def enterOutput_stat(self, ctx:SimpleParser.Output_statContext):
        pass

    # Exit a parse tree produced by SimpleParser#output_stat.
    def exitOutput_stat(self, ctx:SimpleParser.Output_statContext):
        pass


    # Enter a parse tree produced by SimpleParser#input_stat.
    def enterInput_stat(self, ctx:SimpleParser.Input_statContext):
        pass

    # Exit a parse tree produced by SimpleParser#input_stat.
    def exitInput_stat(self, ctx:SimpleParser.Input_statContext):
        pass


    # Enter a parse tree produced by SimpleParser#declaration.
    def enterDeclaration(self, ctx:SimpleParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SimpleParser#declaration.
    def exitDeclaration(self, ctx:SimpleParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SimpleParser#declarations.
    def enterDeclarations(self, ctx:SimpleParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by SimpleParser#declarations.
    def exitDeclarations(self, ctx:SimpleParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by SimpleParser#assign.
    def enterAssign(self, ctx:SimpleParser.AssignContext):
        pass

    # Exit a parse tree produced by SimpleParser#assign.
    def exitAssign(self, ctx:SimpleParser.AssignContext):
        pass


    # Enter a parse tree produced by SimpleParser#IFTHEN.
    def enterIFTHEN(self, ctx:SimpleParser.IFTHENContext):
        pass

    # Exit a parse tree produced by SimpleParser#IFTHEN.
    def exitIFTHEN(self, ctx:SimpleParser.IFTHENContext):
        pass


    # Enter a parse tree produced by SimpleParser#IFELSE.
    def enterIFELSE(self, ctx:SimpleParser.IFELSEContext):
        pass

    # Exit a parse tree produced by SimpleParser#IFELSE.
    def exitIFELSE(self, ctx:SimpleParser.IFELSEContext):
        pass


    # Enter a parse tree produced by SimpleParser#num.
    def enterNum(self, ctx:SimpleParser.NumContext):
        pass

    # Exit a parse tree produced by SimpleParser#num.
    def exitNum(self, ctx:SimpleParser.NumContext):
        pass



del SimpleParser