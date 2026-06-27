#**Descripción**

Karel debe salir de un laberinto, pero este laberinto es poco común, las casillas del laberinto contienen zumbadores. Para salir de él, Karel debe encontrar un camino desde el inicio hasta la salida que cumpla con las siguientes dos condiciones:

 1. El camino no debe pasar dos veces por la misma casilla.
 2. La casilla $i$ del camino debe contener un número de zumbadores que sea divisible por $i$. Es decir, la segunda casilla del camino debe contener un número de zumbadores divisible por 2, la tercera uno divisible por 3, la cuarta por 4, etc. Por ejemplo, si se tiene un camino cuyas casillas contengan los números {1,4,3,8,15,12} es válido, sin embargo un camino {1,4,3,7,5,12} es inválido ya que la cuarta casilla del camino (7) no contiene un número divisible por 4.
Tanto la casilla de inicio, como la de salida tienen 0 zumbadores. El resto de las casillas contendrá un número de zumbadores entre 1 y 100.

#**Problema**

Ayuda a Karel a encontrar el camino más corto posible que cumpla las condiciones entre el inicio y la salida. Karel deberá dejar en la casilla de salida un número de zumbadores igual a la longitud del camino más corto.

#**Consideraciones**

 - El laberinto puede tener cualquier forma y contener paredes internas.
 - Las casillas del laberinto, a excepción del inicio y la salida contienen un número de zumbadores entre 1 y 100.
 - Karel empieza en la casilla de inicio, la cual está dentro del laberinto con una orientación aleatoria.
 - Karel tiene un número infinito de zumbadores en la mochila.
 - Siempre existirá al menos un camino válido hacia la salida.
 - En cada laberinto hay sólo una salida. Y siempre será una casilla rodeada de 3 paredes.
 - Además de la salida no hay otra casilla rodeada por 3 paredes en el laberinto.Recuerda que el 0 es divisible por cualquier número, por lo que siempre se puede avanzar hacia la salida.
 - No importa la posición ni la orientación final de Karel, sólo importa el número de zumbadores que deje Karel en la casilla de salida.
 - El laberinto nunca tendrá más de 100 casillas.

#**Ejemplo**

Mundo inicial

![Mundo inicial](mundoinicial.jpg)

Mundo final

![Mundo final](mundofinal.jpg)
