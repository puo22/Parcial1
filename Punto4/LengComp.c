#include <stdio.h>
#include <time.h>

int main() {
    long long resultado=0;
    long long limite =1000000;

    printf("Calculando con un bucle simple en C...\n");

    //CPU
    clock_t inicio = clock();

    //Bucle suma
    for (long long i= 0;i <limite;i++) {
        resultado +=i;
    }

    clock_t fin=clock();

    double duracion_ms=(double)(fin -inicio)/CLOCKS_PER_SEC *1000.0;

    printf("Resultado: %lld\n",resultado);
    printf("Tiempo de ejecucion: %.4f ms\n",duracion_ms);

    return 0;
}
