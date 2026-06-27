En los días previos a la competencia, en el COMI quisimos probar los tradicionales pastes. Sin dudarlo entramos en una sucursal de pastes Kikos y pedimos un menú. El menú era una cuadrícula de $m$ filas por $n$ columnas con un sabor de paste en cada cuadro.

Siempre buscando sistematizar y optimizar, numeramos los sabores de la siguiente forma:

* Los sabores de la fila superior se numeraron del $1$ al $n$ comenzando por la izquierda.
* Los de la siguiente fila hacia abajo se numeraron del $n+1$ al $2n$ comenzando, de nuevo, por la izquierda.
* Y así con cada fila hasta que los sabores de la fila inferior quedaron con los números del $n(m-1)+1$ a $nm$

Los miembros del COMI pidieron entonces $p$ pastes diciendo el número de sabor que querían.

Desgraciadamente, al tomar la orden giraron el menú 90 grados en el sentido de las manecillas del reloj cambiando así los sabores que recibió cada miembro del COMI (**para que te quede más claro, revisa la explicación del ejemplo**).

#Problema

Escribe un programa que dadas las dimensiones del menú: $m$, $n$, el número $p$ de pastes que se pidieron y la lista de números de sabores pedidos entregue como resultado los números de sabor que realmente se recibieron en el mismo orden en que fueron pedidos.

#Entrada
Tu programa debe leer del teclado la siguiente información:

* En la primera línea los números $m$, $n$, las dimensiones del menú.
* En la segunda línea el número $p$ de pastes a pedir.
* En la tercera línea $p$ números enteros separados por un espacio que representan los pastes que se ordenaron.

#Salida

Tu programa debe escribir en la pantalla $p$ números enteros separados por una línea que representan los números de paste que se recibieron después de que se giró el menú.

#Restricciones

* $1 \le m, n \le 2,000,000$		Dimensiones del menú
* $1 \le p \le 1,000$				Número de pastes que se pidieron.

#Ejemplo

||input
2 3
5
1 3 5 6 1
||output
4 5 6 3 4
||description
El menú tiene una dimensión de $m=2$ filas por $n=3$ columnas. Según el método de numeración los sabores se numeraron así:
1	2	3
4	5	6

Y los miembros del COMI pidieron los sabores 1, 3, 5, 6, 1
Al girar el menú 90 grados quedó de la siguiente forma:
4	1
5	2
6	3

Por lo que ahora al servir un paste 1 en realidad se está sirviendo un paste 4 del menú original.
||end

#Evaluación
* Para un grupo de casos de prueba con valor de $47$ puntos, $n,m \le 1,000$.
* Para un grupo de casos de prueba con valor de $53$ puntos, $n,m \le 2,000,000$.

*Recuerda que los compiladores no te permiten definir una matriz de 2 millones x 2 millones de enteros. Si tu solución para este problema ocupa una matriz, sólo funcionará para los primeros 47 puntos en donde $m$ y $n$ son menores o iguales a $1,000$, por lo que de ser así, te recomendamos que envíes tu código definiendo matrices de tamaño $1,000 \times 1,000$.*

-------------------------------------------------------

> ¿Y mis 50 mil puntos qué?
