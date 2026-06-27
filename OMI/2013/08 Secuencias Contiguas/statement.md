Se tiene una lista desordenada de los números entre $1$ y $N$.
Llamaremos secuencia contigua a un conjunto de elementos de la lista tales que cumplan con las siguientes restricciones:

* Se elige un índice $i$, un índice $j$ tal que $j > i$ y todos los elementos entre $i$ y $j$ pertenecen al conjunto. Es decir, todos los elementos del conjunto estén contiguos en la lista.
* Cuando se ordenan los elementos del conjunto si el número menor en el conjunto es $x$ y el número mayor en el conjunto es $y$ entonces todos los números enteros $z$ tales que $x < z < y$ también están en el conjunto.

(Te recomendamos leer la explicación del ejemplo para que estas restricciones sean más claras)

El largo de una secuencia contigua se define como el número de elementos en el conjunto.

Llamaremos pareja de secuencias contiguas a dos secuencias contiguas con el mismo largo y que además estén consecutivas en la lista, es decir, entre la primera secuencia contigua $A$ y la segunda $B$ no existe ningún elemento.

El largo de una pareja de secuencias contiguas es el doble del largo de cualquiera de las secuencias contiguas que la componen.

# Problema
Escribe un programa que dada la lista desordenada de los números entre $1$ y $N$ encuentre el largo de la pareja de secuencias contiguas más larga en la lista.

# Entrada
Tu programa debe leer del teclado los siguientes datos:

* La primera línea contiene el entero $N$, la cantidad de elementos en la lista.
* La siguiente línea contiene $N$ números enteros separados por un espacio, la lista.

# Salida
Tu programa debe escribir en la pantalla un único entero que indique el largo de la pareja de secuencias contiguas más larga en la lista.

# Restricciones
$1 < N \le 50,000$

# Ejemplo
||input
10
4 6 1 3 2 9 7 8 5 10
||output
6
||description
El conjunto $(1, 3, 2)$ que están entre los índices $3$ y $5$ de la lista (asumiendo que la primera posición es el índice $1$) forman una secuencia contigua. Todos los elementos entre el índice $3$ y el $5$ están en el conjunto y además al ordenar el conjunto se cumple que todos los enteros entre el $1$ (menor del conjunto) y el $3$ (mayor del conjunto) pertenecen al mismo.
Igualmente el conjunto $(9, 7, 8)$ forman una secuencia contigua.
Ambos conjuntos forman una pareja de secuencias contiguas porque están consecutivos en la lista.
||end

# Evaluación

* Para un grupo de casos de prueba con valor de $26$ puntos, $N \le 200$.
* Para otro grupo de casos de prueba con valor de $29$ puntos, $N \le< 1,000$.
* Para el último grupo de casos de prueba con valor de $45$ puntos, $N \le< 50,000$.
