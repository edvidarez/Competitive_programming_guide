# Descripción

Enojado por el saqueo de sus tesoros, Karel Sparrow, ha decidido crear un nuevo sistema de codificación para sus mapas. El nuevo sistema es una secuencia de montones de zumbadores que indican la dirección en la que se debe dar cada paso. Un zumbador significa un paso al norte, dos zumbadores un paso al este, tres un paso al sur y cuatro uno al oeste.

<br>

Pasado el tiempo, ya viejo, Sparrow ha regresado a la isla y te ha pedido que lo ayudes a seguir el recorrido indicado por la secuencia de montones. Ayuda a Karel a encontrar su tesoro y ganarás el 10% de su botín.

# Problema

Escribe un programa que permita a Karel seguir las instrucciones del mapa. Las instrucciones (secuencia de montones) se encuentran de manera consecutiva a lo largo de la primera fila, comenzando en la columna 1 y siguiendo hacia la derecha.

<br>

El punto donde inicia el recorrido siempre es la esquina de la fila 1 con la columna 1.

<br>

Las instrucciones del recorrido son tales que nunca te llevarán de vuelta a la primera fila, y el camino jamás se cruzará sobre si mismo.

# Consideraciones

 - Karel inicia en la esquina de la primera fila con la primera columna mirando al este.
 - Las instrucciones terminan cuando encuentras el primer espacio vacío sobre la primera fila o llegas a la pared, un mapa puede tener hasta 100 instrucciones.
 - No llevas ningún zumbador en la mochila.
 - No hay paredes dentro del mundo ni zumbadores aparte de los de la secuencia de instrucciones.
 - No importa la orientación final de Karel.
 - Karel debe terminar en la posición final del camino indicado por el mapa.
 - No importa si dejas zumbadores en algún lugar del mapa.

# Ejemplo

Mundo inicial

<br>

![Mundo inicial](mundoinicial.png)

<br>

Mundo final

<br>

![Mundo final](mundofinal.png)
