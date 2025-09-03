# Parcial1
Solución parcial corte 1

---
## Estructura del parcial 1
Puntos 1, 2, 3, 4, 5
---
## Punto 1 
Para el siguiente ejercicio, de una expresión regular que
represente el conjunto descrito. [El conjunto de cadenas
sobre {𝑎, 𝑏, 𝑐} en el cual todas las 𝑎′𝑠 preceden a las 𝑏′𝑠 y
éstas a su vez preceden a las 𝑐′𝑠. Es posible que no haya
𝑎′𝑠, 𝑏′𝑠 o 𝑐′𝑠]. Implemente el AFD para esta expresión
regular. Use Python.

### Desarrollo
se coloco un automata de 3 estados siendo q0 el inicial.
- Segun el texto, la cadena vacia es valida.
- Siempre se inicia con una a y se termina con una c
- Puede tener la cantidad de a's, b´s y c's que quieras, pero con las reglas de que despues de una a va una b y despues de una b va una c.

## Punto 2
Si la expresión regular para un ID es la siguiente: [𝐴 −
𝑍𝑎 − 𝑍][𝐴 − 𝑍𝑎 − 𝑧0 − 9] ∗. Implemente un AFD en Python. Realice
mínimo 5 pruebas, tres donde “ACEPTE” y dos donde “NO
ACEPTE” 


### Desarrollo

La expreción regular indica que se acepta tanto letras como digitos 
-Las letras pueden ser tanto mayúsculas como minúsculas y cubren todo el alfabeto
-El primer carácter debe ser una letra (mayúscula o minúscula).
-Los digitos estan entre el 0 y 9
-No puede empezar con número ni contener caracteres raros.

## Punto 3
Escriba un programa en C que implemente una calculadora
que pueda sacar raíz cuadrada de números reales. Use flex
y Bison. La entrada debe ser por un archivo de texto y la
salida debe ser por consola.

---

### Desarrollo

- Entrada: archivo de texto con expresiones matemáticas.
- Operaciones soportadas: sqrt(x) y valores numéricos reales.
- Salida: resultados mostrados en consola.

Ejemplo de entrada (pruebas.txt):

---
- sqrt(9)
- sqrt(2.25)
- sqrt(16)
---

Salida en consola:
- Resultado: 3.000000
- Resultado: 1.500000
- Resultado: 25.000000


### Archivos del proyecto

- Calc.l → archivo de Flex (análisis léxico).
- Calc.y → archivo de Bison (análisis sintáctico).
- lex.yy.c → generado automáticamente por Flex.
- Calc.tab.c y Calc.tab.h → generados automáticamente por Bison.
- Calc → ejecutable final.
- pruebas.txt → archivo de entrada con expresiones a evaluar.

### Compilación
Generar los archivos con Bison y Flex:

---
- bison -d Calc.y
- flex Calc.l
---

Compilar con gcc:
gcc Calc.tab.c lex.yy.c -o Calc -lm

---

## Punto 4
Realice la comparación del rendimiento de un lenguaje de
programación compilado y un lenguaje de programación
interpretado. Utilice la función recursiva para la
comparación.

```
### Desarrollo

C (Compilado)	
Velocidad	Muy rápido (milisegundos)
- Razón	El código se convierte a código de máquina optimizado antes de ejecutarse.

Python (interpretado)
Más lento (cientos de milisegundos)
- El intérprete debe analizar y ejecutar cada línea de código en tiempo real.

```

## Punto 5
Escriba un programa en ANTLR que pueda calcular la
secuencia de Fibonacci de un numero dado. La forma de
calcular el Fibonacci debe ser: FIBO(20) y debe retornar:
0, 1, 1, 2, 3, 5, 8, 13. La entrada y la salida debe ser
por consola. El lenguaje objetivo debe ser Python.

### Desarrollo

---

## Autor

Paula Alejandra Ortiz Salon
