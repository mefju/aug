grammar Simple;

prog: dec=declarations ins=instr
    | ins=instr
; 

num_expr : num              # NUMER
    | '-' num               # NUMER
    | '+' num               # NUMER
    | left=num_expr op=mul_op right=num_expr # MULEXP
    | left=num_expr op=add_op right=num_expr # ADDEXP
    | '(' num_expr ')'      # BRACKETEXPR
    | IDENT                 # IDENTNUM
;

bool_expr : 'true'          # TRUE
    | 'false'               # FALSE
    | '(' bool_expr ')'     # BRACKETEXPRBOOL
    | left=bool_expr 'or' right=bool_expr # OR
    | left=bool_expr 'and' right=bool_expr # AND
    | 'not' right=bool_expr       # NOT
    | left=num_expr rel right=num_expr # REL
;

rel : '=' | '<' | '>' | '<=' | '>=' | '<>';

mul_op: '*'|'/' ;
add_op: '+'|'-' ;


simple_instr : assign ';'
    | if_stat 
    | goto_stat ';'
    | block_instr ';'
    | output_stat ';'
    | input_stat ';'
    | exit_stat ';'
    | goto_target
;


block_instr: 'begin' instr 'end'
;

exit_stat: 'exit'
;


instr: simple_instr +
;

goto_stat: 'goto' IDENT # GOTO
;

goto_target: IDENT ':'
;

output_stat: 'print' right=num_expr
;

input_stat: 'read' IDENT
;

declaration: kind='label' right=IDENT
    | kind='var' right=IDENT
;

declarations: (declaration ';')*
;

assign : left=IDENT ':=' right=num_expr
;


if_stat : 'if' boo=bool_expr 'then' ins=simple_instr # IFTHEN
    | 'if' boo=bool_expr 'then' ins=simple_instr 'else' els=simple_instr # IFELSE
;

num : NUM
;

KEYWORDS: 'and'
    | 'or'
    | 'not'
    | 'if'
    | 'then'
    | 'else'
    | 'goto'
    | 'print'
    | 'read'
    | 'begin'
    | 'end'
    | 'exit'
    | 'label'
    | 'var'
;


IDENT : [a-zA-Z]+;

NUM : NonZeroDigit Digit*
| '0'
;

fragment
NonZeroDigit: [1-9]
;

fragment
Digit: [0-9]
;

WS : [ \t\n\r]+ -> skip
;