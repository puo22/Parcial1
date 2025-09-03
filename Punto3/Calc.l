%{
#include "Calc.tab.h"
#include <stdlib.h>
%}

%%
[0-9]+(\.[0-9]+)?   { yylval.fval = atof(yytext); return NUM; }
sqrt                 { return SQRT; }
\n                   { return EOL; }
[ \t]                ;
.                    { return yytext[0]; }
%%

int yywrap() { return 1; }
