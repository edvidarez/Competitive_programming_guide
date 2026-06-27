# Descripción

Existe una variante del conocido juego de gato que se conoce como gato ruso, en ésta versión, al igual que en la original, hay dos jugadores y una cuadrícula, a diferencia del original, en el gato ruso  el tamaño de la cuadrícula se define por los jugadores.

Al inicio del juego, se define el tamaño de la cuadrícula y el primer jugador escoge las bolitas y el segundo los taches.  Cada jugador coloca su símbolo en una casilla vacía de la cuadrícula de manera alternada.

El ganador del juego es el primer jugador que logre formar una línea de 5 o más.

Las líneas pueden formarse de manera horizontal, vertical o diagonal.

# Problema

Eres el primer jugador y te toca tirar con bolitas, estás actualmente a la mitad de un juego.  Deseas escribir un programa, que conociendo la configuración actual de la cuadrícula, encuentre todas las posiciones de la misma en las que dibujando una bolita ganas el juego.

# Entrada

Tu programa deberá leer lo siguiente

* En la primera línea el número entero $3<=L<=100$, que indica el tamaño de la cuadrícula donde se esta jugando
* En la segunda línea el número $2<=N<=5000$ que representa el número total de símbolos que se han dibujado en la cuadrícula, sean 'bolitas' o 'taches'
* En la siguientes $N$ líneas, dos números enteros $1<=X<=L, 1<=Y<=L$ y un número $S$. Donde los números $X$ y $Y$ indican las coordenadas $(x,y)$ de la tirada y el número $S$ puede ser el número $0$ para indicar una 'bolita' o el número $1$ para indicar un 'tache'

NOTA: Las tiradas en la entrada no necesariamente están en el orden en el que se efectuaron

# Salida

Tu programa deberá escribir $todas$ las jugadas ganadoras utilizando el siguiente formato:

* En cada línea dos números enteros separados por un espacio, estos dos números indican la coordenada $(x,y)$ de la tirada ganadora.

NOTA: Para los casos de evaluación, siempre habrá al menos una jugada ganadora.

No importa el órden en el que escribas las jugadas ganadoras.

# Ejemplo

||input
7
12
1 5 1
1 6 1
1 7 1
2 1 0
2 2 0
2 3 0
2 5 0
3 4 1
3 6 0
4 5 1
4 6 0
5 4 1
||output
2 4
||end

La entrada anterior representa el siguiente juego:

![Entrada](1.jpg)

En donde la esquina inferior izquierda representa la coordenada (1,1)
