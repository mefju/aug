import sys
from antlr4 import *
from sasmLexer import sasmLexer
from sasmParser import sasmParser
from sasmListener import sasmListener

memory={}

program={}

global current

current=0

class LinePrinter(sasmListener):
    def enterDatadef(self, ctx):
        memidx=0
        for x in ctx.NUMBER():
            memory[memidx]=int(x.getText())
            memidx+=1
        return super().enterDatadef(ctx)
    def enterLinecode(self, ctx):
        try:
            program[int(ctx.number().NUMBER().getText())]=""
            # ctx.opcode().getText()
            current=int(ctx.number().NUMBER().getText())
            print(f"Line: {current}")
        except AttributeError:
            pass
        return super().exitLinecode(ctx)
    def enterOpcode(self,ctx):
        program[current]=ctx.getText()
        print(ctx.getText())
        print(f"Opcode: {current}")
        return super().enterOpcode(ctx)
    def exitProg(self, ctx):
        print("OK")
        return super().exitProg(ctx)
    


def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    lexer = sasmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sasmParser(stream)
    tree = parser.prog()
    printer=LinePrinter()
    walker=ParseTreeWalker()
    walker.walk(printer,tree)
    print(f"{tree.toStringTree(recog=parser)}")

    print(memory)
    print(program)

if __name__ == '__main__':
    main(sys.argv)
