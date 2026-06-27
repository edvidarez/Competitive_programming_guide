# Descripción

Un trimino en forma de L es una pieza compuesta por 3 cuadrados, cada uno de dimensiones 1x1 que forman cualquiera de las siguientes figuras:

![Triminos](triminos.png)

Cierto día, paseando por la calle, viste a un par de personas jugando un juego de mesa, del cual no lograste entenderlas reglas, pero si notaste algunas cosas:

* Se juega en un tablero cuadriculado de *H* cuadros de alto por *B* cuadros de ancho, las piezas son cuadrados de 1x1.
* En su turno, cada jugador coloca 3 piezas en el tablero, las piezas pueden colocarse en cualquier posición sin importar si ya está ocupada por otra pieza.

Como te gustan mucho los triminos quieres saber en qué turnos se colocó algún trimino. Además te gustaría saber cuántos cuadros del tablero quedaron libres (sin ninguna pieza) al final del juego.

# Problema

Deberás escribir un programa que reciba como entrada las dimensiones del tablero, las jugadas que se realizan durante el juego y que determine en qué jugadas alguien colocó sus piezas en forma de un trimino como los de arriba y cuántos cuadros quedaron libres al final.

# Entrada

Tu programa deberá leer del teclado de la PC los siguientes datos:

* En la primera línea los números 0 < ***H, B*** ≤ 100 los cuales representan el alto y el ancho del tablero.
* En la segunda línea un número 0 < ***N*** <= 100 representando la cantidad de movidas que se hicieron durante el juego.
* Cada una de las siguientes ***N*** líneas representará una movida de un jugador y contendrá 6 números enteros positivos ***a, b, c, d, e*** y ***f*** separados por espacios, donde ***a*** y ***b*** representarán la fila y columna donde se colocó la primera pieza de ese movimiento, ***c*** y ***d*** la segunda pieza y ***e*** y ***f*** la tercera pieza. La esquina superior izquierda del tablero está representada por la coordenada (1,1)

# Salida

Tu programa deberá escribir en la pantalla de la computadora ***N***+1 líneas, en cada una de las primeras ***N*** líneas deberá haber un 1 si las fichas de esa jugada corresponden a un trimino con forma de L y un 0 en caso contrario. La última línea deberá contener un solo número que representa la cantidad de cuadros libres al final del juego.

# Ejemplo

||input
5 6
4
2 3 3 3 2 4
1 1 4 2 2 5
2 6 2 6 2 6
5 4 5 5 4 5
||output
1
0
0
1
20
||end
