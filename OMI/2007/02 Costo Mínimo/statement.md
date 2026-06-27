# Historia

Karel entró a una nueva escuela para aprender un poco más sobre ciencias de la computación. De tarea le dejaron resolver este problema de optimización.

Dado un conjunto de números enteros positivos definamos el costo de sumar dos números (a,b) de dicho conjunto como costo(a,b)=a+b. Suponiendo que Karel solamente puede hacer sumas de dos números,  calcula el costo mínimo necesario para obtener la suma total de todos los elementos del conjunto.  Para una explicación más detallada lee abajo.

# Explicación

Supongamos que el conjunto de números inicial es {6,3,5,7} queremos obtener la suma de todos los elementos del conjunto, sin embargo, cada suma tiene un costo equivalente al valor de la suma misma. Supongamos que decidimos sumar en el siguiente orden:

![tabla](tabla.jpg)

En este ejemplo primero sumamos los elementos 6 y 3 para obtener 9, esto nos deja el conjunto con los elementos {9,5,7}, el costo de la suma es de (6+3)=9, el costo total acumulado es de 9.  En el paso dos sumamos los elementos 9 y 5 para obtener 14, el conjunto queda ahora como {14,7}, el costo de la suma es de (9+5)=14 y el costo total acumulado es de (9+14)=23 sumando los costos del paso 1 y del 2. Por último en el tercer paso sumamos el 14 y el 7 para obtener 21 con un costo de 21 y un costo total de (23+21)=44. En resumen obtuvimos la suma de todos los elementos del conjunto inicial con un costo de 44.

Sin embargo, el costo varía dependiendo del orden en el que decidamos sumar los elementos, abajo se muestra un segundo ejemplo sumando en distinto orden.

![tabla2](tabla2.jpg)

En este segundo ejemplo se observa que al variar el orden en el que se suman los números se puede obtener un costo total de 42 el cual es menor al del primer ejemplo.

Para el ejemplo anterior, 42 es el costo mínimo posible que se puede obtener.

# Problema

Dado el conjunto de números representado como una línea de beepers que se encuentra en la primera fila, ayuda a Karel a calcular el costo mínimo posible para obtener la suma de los elementos y dejar un número de beepers igual a dicho costo en la posición (1,2) del mundo.

NOTA: El resultado debe ser el COSTO MÍNIMO posible, NO LA SUMA de los elementos del conjunto.

# Consideraciones

* Karel inicia en la posición (1,1) del mundo viendo hacia el este.
* Karel inicia con un número INFINITO de beepers en su mochila.
* El conjunto de números se representa como una línea de beepers SIN ESPACIOS que se encuentra en la fila 1 comenzando a partir de la posición (1,1).
* El conjunto de números nunca tendrá más de 10 elementos.
* Los elementos del conjunto son valores entre 1 y 100.
* No hay paredes dentro del mundo.
* Karel debe dejar un número de beepers en la posición (1,2) igual al costo mínimo posible para obtener la suma de los elementos del conjunto.
* No importa la posición ni orientación finales de Karel.
* A excepción de la posición (1,2) no importa la cantidad de beepers que haya en cualquier posición del mundo al finalizar la ejecución del programa.

# Ejemplo

![ejem](ejemplo.jpg)
