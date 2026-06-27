La lotería es un juego antigüo que data del 1400. Cada participante tiene un tablero $G$ con $N$ filas y $M$ columnas. El "Gritón" va leyendo cartas en orden aleatorio y los jugadores van marcando las que aparecen en algún lugar de su tablero. El primer jugador en marcar su tablero completo grita *Lotería* y es declarado ganador.
<br /> <br />
En la OMI se organizó un juego de lotería, por supuesto, con reglas más *interesantes*. En la lotería OMI se gritan sólo algunas cartas y los jugadores marcan sus tableros. En la bolsa de frijoles, hay frijoles güeros y frijoles negros. Cuando se acaban las cartas sólo puede declarar lotería el participante cuyo tablero cumpla la siguiente condición:
<br /> <br />
Para cualquier subrectángulo del tablero que se elija, la cantidad de frijoles güeros en sus 4 esquinas debe ser par. Es decir, **para cualquier subrectángulo, si te fijas sólo en las 4 casillas de las esquinas, puede haber 0, 2 ó 4 frijoles güeros en total**.
<br /> <br />
Tu compañero de delegación estaba jugando pero tiene que ir al baño, así que te pidió que tomes su lugar. Su tablero ya tiene $K$ casillas marcadas y aun faltan $Q$ cartas por ser leídas. Además, te diste cuenta de que el gritón es un poco torpe, y seguido repite cartas que ya había dicho. En este caso, todos los competidores acordaron quitar el frijol que esté en esa casilla, por si el gritón vuelve a repetir esa carta.
<br /> <br />
Cómo el juego se te hizo un poco aburrido decidiste calcular lo siguiente:
<br /> <br />
Para la configuración inicial que te dejó tu compañero y para cada carta que se vaya leyendo, la cantidad de formas distintas que hay de colocar frijoles (güeros o negros) en las casillas vacías del tablero y tal que la condición de triunfo se siga cumpliendo. Dos formas de marcar un tablero se consideran distintas si difieren en al menos una casilla. Al momento de contar las formas distintas, tienes que considerar todas las casillas que ya tengan frijoles, es decir, no puedes quitar frijoles, únicamente agregar frijoles nuevos a casillas que no están marcadas.
<br /> <br />
Como las cantidad de opciones puede ser muy grandes, debes responder el residuo de cada respuesta al dividirla por $10^9 + 7$.

#Entrada

La primera línea de la entrada contiene un único entero $T$, **la cantidad de subcasos.** Lo siguiente es la descripción de los subcasos:

* La primera línea tiene los enteros N, M, K y Q. La cantidad de columnas y filas del tablero, el número de casillas marcadas que tiene inicialmente y la cantidad de cartas que se van a leer.
* Las siguientes $K$ líneas tienen tres enteros cada una $c_i, f_i$ y $v_i$ que representan la columna, la fila y el color del frijol que hay en cada una de las K casillas que ya tiene marcadas el tablero. $v_i = 1$ significa que el frijol es güero, $v_i = 0$ significa que el frijol es negro.
* Las últimas $Q$ líneas tienen tres enteros cada una $c_j , f_j$ y $v_i$ que representan la columna y la fila de la $j$-ésima carta que lee el gritón. El valor $v_i$ es un $1$ si al marcar la posición de la carta tomas un frijol güero, un $0$ si es un frijol negro, y un −1 si ya había un frijol ahí y lo quitas.

#Salida

Para cada subcaso, debes imprimir $Q + 1$ líneas, cada una con la cantidad de formas distintas de marcar el tablero para la configuración inicial y la configuración después de leer cada una de las siguientes $Q$ cartas.

||input
2
2 2 1 5
1 1 1
1 2 0
2 1 1
2 2 0
1 2 -1
1 2 1
3 3 8 2
1 1 1
1 3 1
2 1 0
1 2 0
2 3 0
3 1 1
2 2 1
3 2 0
3 3 0
||output
4
2
1
1
1
0
0
1
||input
2
2 2 1 0
1 1 0
2 5 1 0
1 1 1
||output
4
32
||end

A continuación se muestra una ilustración del primer subcaso del primer ejemplo, las celdas actualizadas en cada paso están coloreadas con azul claro.

<img src="https://i.imgur.com/FLQ6Vjp.jpeg" />

En el primer estado del tablero, hay 4 formas de rellenarlo de tal manera que se cumpla la propiedad, estas formas son:

<img src="https://i.imgur.com/SSL8bXL.jpeg" />

En el segundo estado, hay exactamente dos formas de rellenar el tablero:

<img src="https://i.imgur.com/qbKrqNE.jpeg" />

En el tercer estado, existen una única forma de rellenar el tablero:

<img src="https://i.imgur.com/oy416zX.jpeg" />

En el cuarto estado, el tablero está completo, pero cumple la condición. Por lo que existe una única forma de rellenar el tablero, que es no hacer nada.
<br /> <br />
En el quinto estado, existe una única forma de rellenar el tablero:

<img src="https://i.imgur.com/7bTJuQz.jpeg" />

Y en el sexto estado, el tablero está completo, sin embargo, hay 3 frijoles güeros en las esquinas del (único, para este caso) subrectángulo. Por lo que el tablero no cumple la condición, entonces no existe forma de rellenarlo para que la cumpla.
<br /> <br />
Para el segundo subcaso del primer ejemplo, el tablero se ve inicialmente así:

<img src="https://i.imgur.com/MTNy4z4.jpeg" />

Se puede demostrar que colocando un frijol güero en la casilla faltante, la condición se cumple. Si por el contrario colocamos un frijol negro en esa casilla, el subrectángulo que tiene por esquinas las casillas $(1, 2), (1, 3), (3, 3)$ y $(3, 2)$, contiene en total $1$ frijol güero en sus esquinas, por lo que la condición no se cumple. Estas esquinas est´an coloreadas con rojo en la siguiente imagen:

<img src="https://i.imgur.com/Wb6bn2V.jpeg" />

El caso anteriormente mencionado, es el estado que se obtiene después de la última carta mencionada, y como no cumple la condición, la respuesta es $0$.

#Condiciones

* $1 \leq T \leq 10^4$.
* $2 \le N, M \le 10^5$.
* $0 \le K, Q \le 10^5$.
* Se garantiza que la suma de cada una de las variables $N, M, K,$ y $Q$ sobre todos los casos, nunca excede $10^5$.
* Siempre se cumple que $K \le M\times N$.
* Para todo $1 \le i \le K$, se cumple que $1 \le c_i \le N$, $1 \le f_i \le M$ y $0 \le v_i \le 1$.
* Para todo $1 \le j \le Q$, se cumple que $1 \le c_j \le N$, $1 \le f_j \le M$ y $-1 \le v_j \le 1$.

#Subtareas

* Subtarea 1 (5 puntos): $N\times M \le 100$, $K = N \times M$ y  $Q = 0$. Se garantiza que la suma de $N\times M$ sobre todos los subasos es a lo más 100.
* Subtarea 2 (7 puntos): $N = 2$ y $Q = 0$.
* Subtarea 3 (8 puntos): $N = 2$. Además se garantiza que el gritón nunca va a repetir una carta.
* Subtarea 4 (10 puntos): $N\times M \le 10^5$, $K = N\times M$ y $Q = 0$. Se garantiza que la suma de $N\times M$ sobre todos los subasos es a lo más $10^5$.
* Subtarea 5 (19 puntos): $Q = 0$. Además se garantiza que el gritón nunca va a repetir una carta.
* Subtarea 6 (12 puntos): Se garantiza que siempre habrá al menos una forma de rellenar el tablero de manera válida, y que el gritón nunca va a repetir una carta.
* Subtarea 7 (18 puntos): Se garantiza que el gritón nunca va a repetir una carta.
* Subtarea 8 (21 puntos): Sin restricciones adicionales.
