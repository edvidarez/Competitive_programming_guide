# Descripción

En su última misión, el súper agente Jaime Papel Blanco, debe hackear una red mientras se encuentra dentro de un edificio enemigo. El edificio está lleno de guardias y para poder hackear la red, Jaime Papel Blanco necesita esconderse y pasar desapercibido. Ahora debe encontrar el lugar óptimo para esconderse. Jaime Papel Blanco tiene un mapa de la planta del edificio, el cual está representado como una cuadrícula de MxN que tiene tres tipos de cuadros: pared, por la que nadie puede pasar, representado por un '#'; pasillo, representado por '.'; y guardia, representado por 'G'. El edificio no tiene cuartos cerrados, es decir, desde cualquier cuadro se puede llegar a cualquier otro. Jaime Papel Blanco sabe que los guardias solo lo detectaron si se encuentran en el mismo cuadro del mapa que él. Los guardias solo pueden moverse hacia arriba, abajo, izquierda o derecha. Para lograr su misión, debe encontrar un cuadro cuya distancia al guardia más cercano sea la máxima posible. Con distancia, el agente Jaime Papel Blanco, se refiere al mínimo de cuadros que tendrá que recorrer un guardia para llegar a él.

#Problema#

Escribe un programa que dado un mapa, encuentra un cuadro óptimo para el escondite de Jaime Papel Blanco, es decir, aquel que maximice la distancia al guardia más cercano y deberás reportar esa distancia.

#Entrada#

Tu programa debe leer del teclado la siguiente información:

- En la primer línea los números M y N, las dimensiones del mapa.
- Las siguientes M líneas contendrán N caracteres del tipo '#', '.' o 'G' indicando si en ese cuadro del mapa hay una pared, un pasillo o un guardia, respectivamente.

#Salida#

Tu programa debe escribir en la pantalla un único entero D seguido de un salto de línea, representando la distancia máxima al guardia más cercano a Jaime Papel Blanco.

#Ejemplo#

||input
5 5
G..#.
##.G.
G...#
....#
#####
||output
3
||end

#Explicación de la salida
La posición que deja al agente Jaime Papel Blanco más lejos del guardia más cercano es la posición en la tercera columna, cuarta fila. Esta posición esta a 3 cuadros de distancia de los guardias más cercanos, cualquier otra posición está a menos de 3 cuadros de distancia de algún guardia.

#Límites#

1 < N, M <= 2,000 Dimensiones del mapa.
1 <= G <= 1,000	 Número máximo de guardias en el mapa.
