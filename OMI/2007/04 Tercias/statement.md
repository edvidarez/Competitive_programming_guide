# Descripción

Se dice que $3$ números $a$, $b$, y $c$ están en sucesión aritmética si, $a\lt b\lt c$, y $c-b=b-a$. Por ejemplo los números $1$, $2$ y $3$ están en sucesión aritmética, los números $2$, $20$ y $38$ también lo están. Pero los números $2$, $3$ y $20$ no lo están.

Determinar si $3$ números están en sucesión aritmética es una tarea simple, pero dado un conjunto de números determinar cuántos de ellos están en sucesión aritmética es algo un poco más difícil.

Debes escribir un programa que lea un conjunto de números distintos e imprima en pantalla cuantas tercias de esos números están en sucesión aritmética.

# Entrada

En la primera línea el número $N$ que representa la cantidad de números en el conjunto. Cada una de las siguientes $N$ líneas contendrá un número del conjunto el cuál será un entero mayor a $0$ y menor o igual a $1,000,000,000$, además, estos números estarán ordenados de manera creciente.
# Salida

En la primera linea un solo número entero indicando cuántas tercias de los números hay en sucesión aritmética.

# Ejemplo

||input
5
1
2
3
20
38
||output
2
||end

# Límites

* $1 \leq N \leq 7000$
