Tienes una lista desordenada con $N$ números distintos los cuales tienen valores entre $0$ y $M$. Llamemos al primer número de esta lista $a_0$. Debes ordenar los números de la lista y ver en qué posición queda el número $a_0$.
En este problema la primera posición de la lista es la posición $0$ y la última es la posición $N-1$.

# Problema
Escribe un programa que dada la lista de $N$ números determine en qué posición queda el elemento $a_0$
(el primero de la lista) después que ésta se ordena.

# Entrada
Tu programa debe leer del teclado la siguiente información:

* En la primera línea el número entero $N$, la cantidad de números en la lista.
* En la segunda línea los $N$ números de la lista separados cada uno por un espacio.

# Salida
Tu programa debe escribir en la pantalla un único número entero que representa la posición final del elemento $a_0$ en la lista ordenada.

# Restricciones
$1 < N \le 2,000,000$
$0 \le M \le 10^9$

# Ejemplo
||input
5
14 2 1 17 23
||output
2
||description
Recuerda que las posiciones de la lista se cuentan a partir de $0$.
La lista ordenada queda $1, 2, 14, 17, 23$, de modo que $14$, que era el primer elemento en la lista desordenada, quedó en la posición $2$.
||end

# Evaluación

Para un grupo de casos con valor de $51$ puntos $N \le 5,000$.
