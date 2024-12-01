grammar Lyric;

program
    : 'start'
      stmtlists
      'stop'
    ;

/** Statement Lists
* <stmts> ::= <stmts> <stmt> | ε
*/
stmtlists
    : stmtlists stmt
    | /* epsilon */
    ;

/** Statement
* <stmt> ::= <expr> ';'
*          | <dec_stmt> ';'
*          | <loop_stmt>
*          | <repeat_stmt>
*          | <check_stmt>
*          | '{' <stmts> '}'
*/
stmt
    : expr ';'
    | dec_stmt ';'
    | loop_stmt
    | repeat_stmt
    | check_stmt
    | '{' stmtlists '}'
    | 'release ' IDENT ';'
    | 'release ' num ';'
    | 'release ' STRING ';'
    ;

/** Expression
* <expr> ::= <id>
*          | <assign_expr>
*          | <math_expr>
*          | <cpr_expr>
*/
expr
    : IDENT
    | assign_expr
    | math_expr
    | cpr_expr
    ;

/** Declaration
* <dec_stmt> ::= <data_type> <id>
*              | <data_type> <assign_expr>
*/
dec_stmt
    : DATA_TYPE IDENT
    | DATA_TYPE assign_expr
    ;

/** Assignment
* <assign_expr> ::= play <id>  <expr>
*/
assign_expr
    : 'play ' IDENT expr
    ;

/** Arithmetic expression
* <math_expr> ::= <math_expr> '+' <math_term>
*               | <math_expr> '-' <math_term>
*               | <math_term>
*
* <math_term> ::= <math_term> '*' <math_factor>
*               | <math_term> '/' <math_factor>
*               | <math_factor>
*
* <math_factor> ::= <num> | '(' <math_expr> ')'
*
*/
math_expr
    : math_expr '+' math_term
    | math_expr '-' math_term
    | math_term
    ;

math_term
    : math_term '*' math_factor
    | math_term '/' math_factor
    | math_factor
    ;

math_factor
    : num
    | '(' math_expr ')'
    | IDENT
    ;


/** Iteration - While Loop
* <loop_stmt> ::= loop '(' <expr> ')' <stmt>
*
* <repeat_stmt> ::= repeat '(' <expr> ')' <stmt>
*/
loop_stmt
    : 'loop ' '(' expr ')' stmt ;

repeat_stmt
    : 'repeat ' '(' expr ')' stmt ;

/** Condition - Check Statement
* <check_stmt> ::= check '(' <expr> ')' here <stmt>
*             | check '(' <expr> ')' here <stmt> there <stmt>
*/
check_stmt
    : 'check ' '(' expr ')' 'here ' stmt (else_stmt)?
    ;

else_stmt
    : 'there' stmt
    ;

/** Comparison
* <cpr_expr> ::= <cpr_term> <cpr_symbol> <cpr_term>
* <cpr_term> ::= <id> | <num> | '(' <math_expr> ')'
*/
cpr_expr
    : cpr_term CPR_SYMBOL cpr_term
    ;

cpr_term
    : IDENT
    | num
    | '(' math_expr ')'
    ;


DATA_TYPE
    : 'num '
    | 'bool '
    | 'str '
    ;

IDENT
    : [a-z] ([a-zA-Z] | '0'..'9')*
    | STRING
    ;

DIGIT : [0-9] ;

CHAR : ([a-zA-Z]);

/** Numbers and Strings
* <num> ::= <num> <digit> | <digit>
* <str> ::= "{ <char> }"
*/
num
    : num DIGIT
    | DIGIT
    ;

STRING
    : '"' (CHAR)* '"'
    ;

/** Comparison Operators
* <cpr_symbol> ::= '<' | '<=' | '>' | '>=' | '=='
*/
CPR_SYMBOL : '<' | '<=' | '>' | '>=' | '==' ;

WS : [ \r\t\n]+ -> skip ;
