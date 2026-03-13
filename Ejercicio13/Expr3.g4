grammar Expr3;

expr: term ((ADD | REST) term)* ;
term: factor ((MULT | DIV) factor)* ;

ADD: '+' ;
REST : '-'; 
MULT: '*'; 
DIV: '/'; 

factor: NUM;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip;