grammar sasm;

options { caseInsensitive = true; }


prog
    : (datadef EOL)? EOL* ((linecode EOL)* linecode EOL*)? EOF
    ;

datadef
    : DATA NUMBER
    | DATA NUMBER ',' NUMBER
    | DATA NUMBER (',' NUMBER) *
    ;

linecode
    : number opcode (comment)?
    | comment
    ;

address
    : ADR
    ;

number
    : NUMBER
    ;

comment
    : COMMENT
    ;

opcode
    : jump=JUMPS adr=ADR
    | comm=OPCODEZERO
    | pop=POP
    | pop=POP adr=ADR
    | push=PUSH adr=ADR
    | push=PUSH absol=NUMBER
    ;

DATA
    : 'DATA'
    ;

JUMPS
    : 'JMP'
    | 'JZ'
    | 'JNZ'
    | 'JLZ'
    | 'JLEZ'
    | 'JGZ'
    | 'JGEZ'
    ;

OPCODEZERO
    : 'DUP'
    | 'ADD'
    | 'SUB'
    | 'MUL'
    | 'DIV'
    | 'NEG'
    | 'READ'
    | 'PRINT'
    | 'STOP'
    | 'NOP'
    ;

POP
    : 'POP'
    ;

PUSH
    : 'PUSH'
    ;

ADR 
    : '$'NUMBER
    ;

NUMBER 
    : [0-9]+
    ;

COMMENT
    : '#' ~ [\r\n]*
    ;

EOL
    : [\r\n] +
    ;

WS
    : [ \t] -> skip
    ;
