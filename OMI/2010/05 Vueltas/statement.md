#Descripción

Se tiene un tablero de $M$ filas por $N$ columnas donde $M$y $N$ son números impares mayores a uno. Sobre este tablero se desean realizar dos tipos de operaciones: Vueltas verticales y Vueltas horizontales.

.

Una Vuelta se refiere a un giro del tablero que utiliza como eje de giro, la fila central en el caso de las vueltas verticales y la columna central en el caso de las vueltas horizontales. Por ejemplo, si sobre un tablero se realiza una vuelta vertical entonces la fila que está hasta arriba ahora estará hasta abajo y viceversa, lo mismo con la segunda de arriba hacia abajo quedará ahora como segunda de abajo hacia arriba, etc.

#Problema

Escribe un programa que reciba como entrada el tablero y la secuencia de vueltas a realizar sobre él y escriba como salida la configuración final del tablero después de haber aplicado $K$ vueltas.

#Entrada

Tu programa debe leer del teclado los siguientes datos:

* En la primera línea los números $M$ y $N$ que indican el tamaño del tablero.
* En las siguientes $M$ líneas habrá $N$ números enteros separados por un espacio en cada una que indican el contenido del tablero en esa fila
* En la línea siguiente a la última del tablero, el número $K$ que indica la cantidad de vueltas a aplicar
* En las siguientes $K$ líneas habrá un carácter 'V' o 'H' (mayúsculas) que indica una vuelta Vertical o una vuelta Horizontal. Las vueltas al tablero se aplican en el orden en el que aparecen en la entrada.

#Salida

Tu programa debe escribir a la pantalla los siguientes datos: $M$ líneas con $N$ enteros separados por un espacio cada uno que indiquen el estado final del tablero después de haber aplicado las $K$ vueltas en el orden que se especifica en la entrada.

#Ejemplos

||input
3 5
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
1
V
||output
20 21 22 23 24
15 16 17 18 19
10 11 12 13 14
||input
3 5
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
1
H
||output
14 13 12 11 10
19 18 17 16 15
24 23 22 21 20
||end

#Limites
* $1 < M, N < 10^3$
* $1 \le K \le 5 \cdot 10^4$
* $1 \le a[i][j] < 1245$
