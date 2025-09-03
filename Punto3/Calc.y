%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int yylex(void);
void yyerror(const char *s);
extern FILE *yyin;
%}

%union {
    double fval;
}

%token <fval>NUM
%token SQRT
%token EOL

%type <fval>expr

%%

input:
    /*vacío*/
    | input line
    ;

line:
    expr EOL { printf("Resultado: %f\n", $1); }
    | EOL
    ;

expr:
    NUM                { $$ = $1; }
    | SQRT '(' expr ')' { $$ = sqrt($3); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char *argv[]) {
    if (argc>1) {
        yyin=fopen(argv[1], "r");
        if (!yyin) {
            perror(" No se puede abrir el archivo");
            return 1;
        }
    }
    yyparse();
    return 0;
}
