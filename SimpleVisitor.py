# Generated from Simple.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete generic visitor for a parse tree produced by SimpleParser.

class SimpleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleParser#prog.
    def visitProg(self, ctx:SimpleParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#BRACKETEXPR.
    def visitBRACKETEXPR(self, ctx:SimpleParser.BRACKETEXPRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#NUMER.
    def visitNUMER(self, ctx:SimpleParser.NUMERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#ADDEXP.
    def visitADDEXP(self, ctx:SimpleParser.ADDEXPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#IDENTNUM.
    def visitIDENTNUM(self, ctx:SimpleParser.IDENTNUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#MULEXP.
    def visitMULEXP(self, ctx:SimpleParser.MULEXPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#NOT.
    def visitNOT(self, ctx:SimpleParser.NOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#OR.
    def visitOR(self, ctx:SimpleParser.ORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#AND.
    def visitAND(self, ctx:SimpleParser.ANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#REL.
    def visitREL(self, ctx:SimpleParser.RELContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#TRUE.
    def visitTRUE(self, ctx:SimpleParser.TRUEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#FALSE.
    def visitFALSE(self, ctx:SimpleParser.FALSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#BRACKETEXPRBOOL.
    def visitBRACKETEXPRBOOL(self, ctx:SimpleParser.BRACKETEXPRBOOLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#rel.
    def visitRel(self, ctx:SimpleParser.RelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#mul_op.
    def visitMul_op(self, ctx:SimpleParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#add_op.
    def visitAdd_op(self, ctx:SimpleParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#simple_instr.
    def visitSimple_instr(self, ctx:SimpleParser.Simple_instrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#block_instr.
    def visitBlock_instr(self, ctx:SimpleParser.Block_instrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#exit_stat.
    def visitExit_stat(self, ctx:SimpleParser.Exit_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#instr.
    def visitInstr(self, ctx:SimpleParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#GOTO.
    def visitGOTO(self, ctx:SimpleParser.GOTOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#goto_target.
    def visitGoto_target(self, ctx:SimpleParser.Goto_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#output_stat.
    def visitOutput_stat(self, ctx:SimpleParser.Output_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#input_stat.
    def visitInput_stat(self, ctx:SimpleParser.Input_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#declaration.
    def visitDeclaration(self, ctx:SimpleParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#declarations.
    def visitDeclarations(self, ctx:SimpleParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#assign.
    def visitAssign(self, ctx:SimpleParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#IFTHEN.
    def visitIFTHEN(self, ctx:SimpleParser.IFTHENContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#IFELSE.
    def visitIFELSE(self, ctx:SimpleParser.IFELSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#num.
    def visitNum(self, ctx:SimpleParser.NumContext):
        return self.visitChildren(ctx)



del SimpleParser