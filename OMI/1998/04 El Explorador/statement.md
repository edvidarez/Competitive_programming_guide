# Descripción

Un explorador tiene que decidir donde construir un camino para llegar de un punto $A$ a un punto $B$. Para auxiliarse el explorador ha hecho un mapa con los obstáculos que existen. Cuadriculó su mapa y quiere un camino que pase por el menor número de cuadros.

<br>

El camino sólo puede ir de un cuadro a otro si tienen un lado en común, es decir, no puede avanzar en diagonal, y no puede pasar por un cuadro que contenga un obstáculo. Cada cuadro del mapa se identifica por sus coordenadas, primero la fila y después la columna. Las filas están numeradas de arriba hacia abajo iniciando con el $0$. Las columnas están numeradas de izquierda a derecha iniciando con el $0$.

<br>

El objetivo de la construcción del camino es encontrar el menor número de cuadros por los que debe pasar un camino que vaya del punto $A$ al punto $B$, incluyendo a los cuadros que contienen a $A$ y a $B$.

# Entrada

En la primera línea los enteros $N$ y $M$, el número de filas y columnas del mapa. En cada una de las siguientes $N$ líneas hay $M$ números que pueden ser $0$ ó $1$, $0$ si no hay obstáculo en el cuadro correspondiente y $1$ si lo hay.

<br>

En la siguiente línea (la penúltima), la fila $(A_f)$ y columna $(A_c)$ del punto $A$. En la última línea, la fila $(B_f)$ y columna $(B_f)$ del punto $B$.

# Salida

Una única línea con el número de cuadros por los que pasa un camino mínimo entre $A$ y $B$.

# Ejemplo

||input
4 5
0 1 0 0 0
0 0 1 1 0
0 1 0 0 0
0 0 0 0 0
3 1
0 2
||output
9
||end

# Límites

 - $1 \leq N, M \leq 50$
 - $0 \le A_f, B_f < N $
 - $0 \le A_c, B_c < M $
