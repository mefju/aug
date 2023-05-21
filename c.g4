grammar c;
 
// parser
 
start : expr | <EOF> ;
 
expr : sign expr     # USIGN
   | expr mulop expr # MULOPGRP
   | expr addop expr # ADDOPGRP
   | '(' expr ')'   # PARENGRP
   | NUMBER      # DOUBLE
   ;
 
sign : '+' | '-'
    ;

addop : '+' 
    | '-' ;
 
mulop : '*' 
    | '/' ;
 
// lexer
 
NUMBER : ('0' .. '9') + ('.' ('0' .. '9') +)? ;
 
WS : [ \r\n\t] + -> skip ;