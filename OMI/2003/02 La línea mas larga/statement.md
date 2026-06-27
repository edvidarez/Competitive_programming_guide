# Descripción

El juego de la línea más larga es un juego para dos personas que se desarrolla de la siguiente manera: inicialmente se tiene un tablero vacío que puede tener hasta 100,000 casillas, estas casillas están ordenadas en forma de una larga línea.

![enter image description here][1]

Cada jugador tiene fichas de un color diferente, el jugador uno tiene fichas negras y el jugador dos tiene fichas azules.  Durante su turno cada jugador puede colocar una de sus fichas en cualquiera de las casillas del tablero que este vacía.

El ganador del juego es aquél que después de un cierto número de turnos que se determinó al inicio del juego, haya formado la línea ininterrumpida más larga con sus fichas.

# Problema

Eres el jugador número dos, y te encuentras en la última tirada del juego.  Tu tarea consiste en escribir un programa que determine cual es la mejor jugada posible que puedes hacer.

La mejor jugada posible es aquella que forme la línea de fichas de tu color más larga.

# Entrada

Tu programa deberá leer del archivo de texto ENTRADA.TXT los siguientes datos.

En la primera línea del archivo de entrada esta el número $N$ el cual indica el número de casillas con las que cuenta el tablero.

En la segunda línea habrá $N$ números separados por un espacio.  Estos números representan el estado del tablero al momento de la última tirada. Cada uno de estos números puede tomar el valor 0, 1 ó 2, donde el número cero indica que la casilla en cuestión esta vacía.  El número uno indica que la casilla tiene una ficha del jugador uno y el número dos indica una ficha del jugador dos, en este caso, una de tus fichas.

# Salida

Tu programa deberá escribir en el archivo de texto SALIDA.TXT dos números, cada uno de ellos en una línea diferente.

En la primera línea deberá ir un número que indique la casilla en la que colocaste tu ficha.  En la segunda línea deberá aparecer el largo de la línea que formaste con esa tirada.

# Ejemplo

Para ejemplo consideremos que hay un tablero de 16 casillas y que al momento de la última tirada la configuración del tablero es la siguiente:

![enter image description here][2]

Como se explicó es el último tiro y le corresponde al jugador dos (fichas azules). Del diagrama se puede observar que la mejor jugada que puede hacer el jugador azul es tirar su ficha en la posición 4, ya que con esa tirada forma una línea de longitud 3 con las fichas de las posiciones 4, 5 y 6.

||input
16
2 1 1 0 2 2 1 0 0 2 1 1 0 0 0 0
||output
4
3
||end


<strong>NOTA:</strong> Si existe más de una solución óptima, cualquiera de estas será considerada correcta.

# Límites
* $4 <= N <= 100,000$


  [1]: 0c03c6246aecc017c406d251a1bc11f175fecc69.png
  [2]: 0d76818c0b51bbebd41366cde3d2ff1fcd49d9ce.png
