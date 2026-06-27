Se acerca el cumpleaños del Hurón Legendario. Tú, como su buen amigo, quieres regalarle uno de sus muchos objetos favoritos: Un arreglo.
<br /> <br />
Los gustos del Hurón son *un poco* complicados. El arreglo que le regales al Hurón debe cumplir lo siguiente:

* Debe tener exactamente $N$ elementos.
* Cada elemento debe ser un valor entre $1$ y $M$.
* No debe tener subarreglos \textit{prohibidos}. En el siguiente párrafo se explica qué es un subarreglo prohibido.

El Hurón tiene una matriz $V$ de tamaño $N \times M$ que contiene valores enteros. Para algún subarreglo $S$ del arreglo, sea $S_{largo}$ el tamaño del subarreglo y $S_{max}$ el elemento máximo en ese subarreglo. El subarreglo es *prohibido* si la celda $V[S_{largo}][S_{max}]=-1$. **Recuerda que un subarreglo es cualquier sección contigua del arreglo, incluyendo el arreglo completo. Los arreglos $\\{2, 3\\}$ y $\\{3, 4\\}$ son subarreglos de $\\{1, 2, 3, 4\\}$, pero $\\{1, 3, 4\\}$ no.**

Además, el Hurón califica sus regalos. Si le regalas un arreglo que cumpla con sus requisitos, el Hurón le asignará un valor de la siguiente forma:

* Para **cada uno** de los subarreglos del arreglo, el Hurón obtendrá su $S_{largo_i}$ y $S_{max_i}$.
* Luego calculara la suma de $V[S_{largo_i}][S_{max_i}]$ para todos los subarreglos. La suma total será el valor del arreglo.

Como aprecias mucho al Hurón, quieres darle todos los posibles arreglos que le gusten. Para esto, necesitas contar cuántos arreglos diferentes existen que cumplen sus requisitos y calcular la suma total de los valores de todos esos arreglos.

#Problema

Dados $N$, $M$ y la matriz $V$ de tamaño $N \times M$, encuentra:

* La cantidad de arreglos diferentes que le gustan al Hurón. Como este número puede ser muy grande, imprímelo módulo $10^9+7$.
* La suma total de los valores de todos los arreglos que le gustan al Hurón. Como este número puede ser muy grande, imprímelo módulo $10^9+7$.

#Entrada

* La primera línea de la entrada contiene los enteros $N$ y $M$.
* Las siguientes $N$ líneas contienen $M$ enteros cada una. Los enteros de la línea $i+1$ son
$V[i][1], V[i][2], \dots, V[i][M]$ (los valores de la $i$-ésima fila de la matriz $V$).

#Salida

Imprime dos enteros separados por un espacio: la cantidad de arreglos diferentes que cumplen con los requisitos del Hurón Legendario y la suma de los valores de todos esos arreglos, ambos módulo $10^9+7$.

#Ejemplos

||input
2 3
1 1 1
1 1 1
||output
9 27
||end

Existen $9$ arreglos que cumplen los requisitos del Hurón: $[1, 1]$, $[1, 2]$, $[1, 3]$, $[2, 1]$, $[2, 2]$, $[2, 3]$, $[3, 1]$, $[3, 2]$ y $[3, 3]$. Cada uno tiene valor igual a $3$, por lo tanto la suma total de los valores es $27$.

* Se toman todos los suibarreglos, en este caso serían $\\{1\\}, \\{3\\}$ y $\\{1, 3\\}$
* El primer subarreglo tiene $largo = 1$ y elemento $maximo = 1$, revisando la table $V[1][1] = 1$ por lo que ese subarreglo vale 1.
* El segundo subarreglo tiene $largo = 1$ y elemento $maximo = 3$, revisando la table $V[1][3] = 1$ por lo que ese subarreglo vale 1.
* El último subarreglo tiene $largo = 2$ y elemento $maximo = 3$, revisando la table $V[2][3] = 1$ por lo que ese subarreglo vale 1.
* El valor final del arreglo es la suma de todos sus subarreglos $res = 1 + 1 + 1 = 3$.

||input
2 2
2 4
-1 1
||output
3 23
||end

#Consideraciones

* $1 \leq N, M \leq 400$.
* $-1 \leq V[i][j] \leq 10^9$, para toda $1 \leq i \leq n$ y $1 \leq j \leq m$.

#Subtaras

* Subtarea 1 (5 puntos): Para toda $i$ y $j$ con $1 \le i \le N$ y $1 \le j \le M$, se cumple que $V[i][j]=1$.
* Subtarea 2 (10 puntos): Se cumple que $N, M \leq 6$.
* Subtarea 3 (25 puntos): Para toda $i$ y $j$ con $1 \le i \le N$ y $1 \le j \le M$, se cumple que $V[i][j] \in \{-1, 1\}$ y $1 \leq n,m \leq 50$.
* Subtarea 4 (15 puntos): Para toda $i$ y $j$ con $1 \le i \le N$ y $1 \le j \le M$, se cumple que $V[i][j] \in \{-1, 1\}$ y $1 \leq N, M \leq 400$.
* Subtarea 5 (15 puntos): Se cumple que $N, M \leq 50$.
* Subtarea 6 (30 puntos): Sin restricciones adicionales.
