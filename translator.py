import sys
from antlr4 import *
# from antlr4.tree.Tree import ParserRuleContext
from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from SimpleListener import SimpleListener
from SimpleVisitor import SimpleVisitor

global current

current=0

variables={}
labels={}
    
def secondTranslation(first_program):

    #sprawdzenie czy etykiety i zmienne się pokrywają:

    if len(set(variables.keys()).intersection(set(labels.keys()))) > 0:
        for x in set(variables.keys()).intersection(set(labels.keys())):
            print(f"{x} występuje jaki zmienna i etykieta, przerywam")
        exit(1)

    # program będzie trzymany w słowniku, gdzie kluczem będzie numer linii programu wynikowego
    # ułatwi to obliczanie skoków
    second_program={}
    
    # Stworzenie linii inicjalizacji zmiennych: 
    data_line="DATA "
    for x in range(0,len(variables.keys())):
        data_line=data_line+"0,"
    data_line=data_line.strip(",")+"\n"

    # numeracja zmiennych - będzie przydatne do zamiany zmiennych na numery - wykorzystany słownik,
    # w którym kluczami są nazwy zmiennych
    counter=0
    for x in variables.keys():
        variables[x]=counter
        counter+=1

    #przepisanie

    line_num=0
    label_jmp_from=[]
    for x in first_program:
        
        # podzielenie każdej linii programu na polecenie i argument
        tmp = x.split(" ")
        polecenie=tmp[0]
        try:
            argument=tmp[1]
        except IndexError:
            argument=""

        match polecenie:
            # jeżeli polecenie dotyczy dostępu do stosu (POP lub PUSH)
            case "POP" | "PUSH":
                # zamiana zmiennej na numer komórki pamięci
                # jeżeli zmiennej nie ma w słowniku zmiennych, to znaczy, że na stos kładziemy wartość
                try:
                    argument=f"${variables[argument]}"
                except KeyError:
                    pass
            case "JMP" | "JZ" | "JNZ" | "JLZ" | "JLEZ" | "JGZ" | "JGEZ":
                #jeżeli jest to skok, to musimy go zamienić ze względnego, na bezwględny
                
                #Jeżeli skok jest bezpośredni, to go przepisujemy na skok bezwględny:
                #Jeżeli skok do etykiety, to zapisujemy linię gdzie występuje
                match argument[0]:
                    case "#":
                        argument=f"{int(argument[1:])+line_num }"
                    case "@":
                        label_jmp_from.append(line_num)
            
            case "NOP":
                #NOP oznacza, że jest to etykieta, więc zapiszemy ją w słowniku etykiet
                
                #Jeżeli poniższa etykieta jest już zdefiniowana (wartość inna niż początkowa -1)
                # to oznacza, że etykiata występuje podwójnie i należy przerwać działanie translatora  
                if labels[argument[1:]]!= -1:
                    print(f"etykieta {argument[1:]} występuje dwa razy. przerywam translację")
                    exit(1)

                labels[argument[1:]]=line_num
                
        #zapisanie do docelowego programu wszystkich poleceń po zamianach (w wypadku POP PUSH J*)
        #jeżeli nie było zmian to łączymy to co wcześniej tylko podzieliliśmy
        second_program[line_num]=f"{polecenie} {argument}".strip()

        # zwiększenie lciznika linii o jeden
        line_num+=1

    #dodanie na końcu programu STOP, by się prawidłowo zakończył
    second_program[line_num]="STOP"

    #zamiana skoków etykietowanych na bezpośrednie
    for x in label_jmp_from:
        tmp=second_program[x].split(" ")
        polecenie=tmp[0]
        argument=tmp[1]
        second_program[x]=f"{polecenie} {labels[argument[1:]]} #{argument[1:]}"

    #przygotowanie pierwszej linijki kodu wynikowego
    output=data_line

    #wpisanie wszsytkich linni kodu razem z numerami
    for x in sorted(second_program.keys()):
        output+=f"{x} {second_program[x]}\n"

    return output


#klasa z visitorami
class LineVisitor(SimpleVisitor):

    #mnożenie i dzielenie
    def visitMULEXP(self, ctx):
        out=[]
        
        #wizyta subdrzew (albo liści) odpowiedzialnych za argumenty
        #docelowo położą one na stosie wartość albo jedną ze zmiennych
        out+=self.visit(ctx.left)
        out+=self.visit(ctx.right)
        

        #W zależności od znaku wykonanie mnożenia albo dzielenia
        match ctx.op.getText():
            case '*':
                out+=[f"MUL"]
            case '/':
                out+=[f"DIV"]

        return out
    
    #dodawania odejmowanie
    def visitADDEXP(self, ctx):
        out=[]

        #analogicznie jak mnożenie
        out+=self.visit(ctx.left)
        out+=self.visit(ctx.right)

        match ctx.op.getText():
            case '+':
                out+=[f"ADD"]
            case '-':
                out+=[f"SUB"]

        return out
    
    def visitIDENTNUM(self, ctx):
        #Jeżeli w wartościach numerycznych występuje identyfikator, to jest to zmienna

        #sprawdzenie, czy zmienna została zadeklarowania
        if str(ctx.IDENT()) not in variables:
            print(f"Linia {ctx.start.line}: zmienna {ctx.IDENT()} użyta ale nie zadeklarowana. przerywam translację!")
            exit(1)

        #zwracamy komendę PUSH <nazwa zmiennej>
        return [f"PUSH {ctx.getText()}"]
    
    
    def visitBRACKETEXPR(self, ctx):
        #jeżeli coś jest w nawiasach w wyrażeniach arytmetycznych, to odwiedźmy środkowe dziecko.
        #dzieci 0 i 2 to nawiasy
        return self.visit(ctx.getChild(1))
    
    def visitBRACKETEXPRBOOL(self,ctx):
        #analogicznie w nawiasach w wyrażeniach logicznych
        return self.visit(ctx.getChild(1))
    


    def visitNUMER(self, ctx):
        #Numer w postaci +INTEGER lub -INTEGER lub INTEGER.
        #Zamieniamy ją na liczbę i kładziemy na stosie
        return [f"PUSH {int(ctx.getText())}"]
    
    def visitAND(self, ctx):
        
        #Prawda to 1, fałsz to 0
        #AND - kładziemy dwa argumenty na stosie
        out=[]
        out+=self.visit(ctx.left)
        out+=self.visit(ctx.right)

        #mnożymy oba argumenty
        #jeżeli chociaż jeden argument będzie zero, to
        #wartość działania logicznego też będzie zero, czyli fałsz
        out+=[f"MUL"]
        return out
    
    def visitOR(self, ctx):

        #OR
        #Kładziemy argumenty na stosie
        out=[]
        out+=self.visit(ctx.left)
        out+=self.visit(ctx.right)

        #Sumujemu je
        #Wykonujemy skok
        #jeżeli suma jest większa od zera, czyli co najmniej jeden argument jest true(1)
        #to skaczemy o 3 do przodu, by ustawić stos na true (1)
        #jeżeli suma wynosi 0, to ustawiamy na stosie false (0)
        #po ustawieniu 0 skaczemu bezwarunkowo o 2 by nie nadpisywać stosu 
        out+=[(f"SUM")]
        out+=[f"JGZ #3"]
        out+=[f"PUSH 0"]
        out+=[f"JMP #2"]
        out+=[f"PUSH 1"]

        return out

    def visitNOT(self,ctx):

        #NOT 
        #Kładziemy argument na stosie
        #jeżeli jest równy 1 (większy od zera) to ustawiamy go na 0
        #i odwrotnie
        out=[]
        out+=self.visit(ctx.right)
        out+=[f"JGZ #3"]
        out+=[f"PUSH 1"]
        out+=[f"JMP #2"]
        out+=[f"PUSH 0"]
        
        return out

    def visitFALSE(self, ctx):
        #FALSE
        # na stos kładziemy 0
        out=[f"PUSH 0"]
        return out

    def visitTRUE(self, ctx):
        #TRUE
        # na stos kładziemy 1
        out=[f"PUSH 1"]
        return out

    def visitAssign(self,ctx):
        
        #przypisanie
        #sprawdzamy czy zmienna do której przypisujemy została zdefiniowana
        if str(ctx.IDENT()) not in variables:
        
            print(f"Linia {ctx.start.line}: zmienna {ctx.IDENT()} użyta ale nie zadeklarowana. przerywam translację!")
            exit(1)

        #obliczamy wartoś do przypisania i kładziemy na stosie
        out=[]
        out+=self.visit(ctx.right)
        #zdejmujemy ze stosu i przenosimy do zmiennej
        out+=[f"POP {ctx.IDENT()}"]
        return out
    
    def visitREL(self, ctx):
        #Relacja arytmetyczna
        #Kładziemy na stosie dwa argumenty
        out=[]
        out+=self.visit(ctx.left)
        out+=self.visit(ctx.right)

        #Odejmujemy argumenty od siebie.
        #następnie, w zależności od tego jaki jest znak relacji
        #sprawdzamy czy róznica zmiennych jest mniejsza, większa, czy równa 0
        out+=[f"SUB"]
    
        match ctx.rel().getText():
            case ">":
                out+=[f"JGZ #3"]
                out+=[f"PUSH 0"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 1"]
            case "<":
                out+=[f"JLZ #3"]
                out+=[f"PUSH 0"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 1"]
            case ">=":
                out+=[f"JLZ #3"]
                out+=[f"PUSH 1"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 0"]            
            case "<=":
                out+=[f"JGZ #3"]
                out+=[f"PUSH 1"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 0"]            
            case "<>":
                out+=[f"JNZ #3"]
                out+=[f"PUSH 0"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 1"]
            case "=":
                out+=[f"JNZ #3"]
                out+=[f"PUSH 1"]
                out+=[f"JMP #2"]
                out+=[f"PUSH 0"]
        
        return out

    def visitGOTO(self,ctx):
        #GOTO
        #sprawdzamy czy zostało zdefiniowana etykieta do skoku
        if str(ctx.IDENT()) not in labels.keys():
            print(f"Linia {ctx.start.line}: etykieta {ctx.IDENT()} użyta ale nie zadeklarowana. przerywam translację!")
            exit(1)
        
        #Ustawiamy skok do etykiety, w drugiej fazie będziemy zamieniać etykietę na właściwy adres
        return [f"JMP @{ctx.IDENT()}"]
    
    def visitGoto_target(self, ctx):

        #GOTO cel skoku
        #Sprawdzamy, czy etykieta została zadeklarowana
        if str(ctx.IDENT()) not in labels.keys():
            print(f"Linia {ctx.start.line}: etykieta {ctx.IDENT()} użyta ale nie zadeklarowana. przerywam translację!")
            exit(1)
        return [f"NOP #{ctx.IDENT()}"]
    

    def visitOutput_stat(self, ctx):
        #argument print zostaje obliczony i położony na stosie.
        #print zostaje zamieniony na PRINT
        out=[]
        out+=self.visit(ctx.right)
        out+=[f"PRINT"]
        return out

    def visitInput_stat(self, ctx):
        out=[]

        #sprawdzenie, czy zmienna została zadeklarowana
        if str(ctx.IDENT()) not in variables.keys():
            print(f"Linia {ctx.start.line}: zmienna {ctx.IDENT()} użyta ale nie zadeklarowana. przerywam translację!")
            exit(1)
        
        #Wczytanie zmiennej i odłożenie jej na zmienną
        out+=[f"READ"]
        out+=[f"POP {ctx.IDENT()}"]
        return out


    def visitIFTHEN(self, ctx):
        out = []
        # wygenerowanie warunku logicznego
        out+=self.visit(ctx.boo)

        # wygenerowanie instrukcji do zmiennej pomocniczej
        instr=[]
        instr+=self.visit(ctx.ins)

        # sprawdzenie dlugosci instrukcji pomocniczej
        jump_length=len(instr)

        #wygenerowanie skoku - jeżeli na stosie jest 0-fałsz, to skok
        # za instrukcje 
        out+=[f"JZ #{jump_length+1}"]

        #dodanie instrukcji
        out+=instr

        return out
    
    def visitIFELSE(self, ctx):
        out = []
        # wygenerowanie warunku logicznego
        out+=self.visit(ctx.boo)

        # wygenerowanie instrukcji do zmiennej pomocniczej
        instr=[]
        instr+=self.visit(ctx.ins)

        # wygenerowanie instrukcji else do zmiennej pomocniczej
        instr_else=[]
        instr_else+=[self.visit(ctx.els)]

        # sprawdzenie dlugosci instrukcji pomocniczej i else
        jump_length=len(instr)
        jump_length_else=len(instr_else)

        # wygenerowanie skoku - jeżeli na stosie jest 0-fałsz, to skok
        # za instrukcje i za jedną dodatkową instrukcję JMP która zostanie dodana
        # w następnym kroku, czyli skos o długość instrukcji+2
        out+=[f"JZ #{jump_length+2}"]

        #dodanie instrukcji
        out+=instr
        
        # dodanie bezwarunkowego skoku, by ominąć instrukcje klauzuli else
        out+=[f"JMP #{jump_length_else+1}"]

        #dodanie instrukcji else
        out+=instr_else

        return super().visitIFELSE(ctx)

    
    def visitDeclarations(self, ctx):
        #odwiedzenie wszystkich dzieci deklaracji
        #nie zwaracają one wartości, bo dopisanie zmiennych robimy na poziomie 
        #liścia z deklaracjami
        for x in range(0,ctx.getChildCount()): 
            self.visit(ctx.getChild(x))

    def visitDeclaration(self, ctx):
        
        #w zależności od tego, czy zajmujemy się deklaracją zmiennych czy etykiet
        #to dodajemy je do opdowiednich słowników
        #Zmienne są inicjowane do 0, a etykiety do -1 -- taki numer linii nie występuje nigdzie
        match ctx.kind.text:
            case 'var':
                variables[ctx.right.text]=0
            case 'label':
                labels[ctx.right.text]=-1

    def visitInstr(self, ctx):
        #jeżeli mamy instrukcję, to odwiedzamy wszystkie potomki 
        out=[]
        for x in range (0,ctx.getChildCount()):
            out+=self.visit(ctx.getChild(x))
        return out

    def visitSimple_instr(self, ctx):
        #Simple_instr może zawierać tylko jedną instrukcję   
        return self.visit(ctx.getChild(0))
        
    
    def visitBlock_instr(self, ctx):
        #blok zawiera 3 dzieci : begin instr end. Odwiedzić trzeba tylko środkowe, czyli o numerze 1
        return self.visit(ctx.getChild(1))

    def visitExit_stat(self,ctx):
        #jeżeli w instrukcji występuje komenda exit, to generujemy STOP
        return[f"STOP"]
    
    def visitProg(self, ctx):

        #robimy przejście po wszystkich elementach z prog, czyli wejścia do programu

        return super().visitProg(ctx)

        
def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    lexer = SimpleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    tree = parser.prog()
    
    visitor=LineVisitor()
    
    #przejście po całym drzewie i zebranie całego wygenerowanego (pierwszej wersji) kodu
    first_program=visitor.visit(tree)
    
    #dokonanie drugiej translacji i wydruk programu
    print(secondTranslation(first_program))

   
if __name__ == '__main__':
    main(sys.argv)
