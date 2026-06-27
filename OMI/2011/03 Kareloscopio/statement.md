# Descripción

Kareleo Karelei se ha propuesto inventar un aparato para ampliar imágenes al que llamará kareloscopio. Para poder desarrollarlo necesita hacer varios experimentos en los cuales tú serás su asistente. Kareleo te pondrá en un mundo que contiene una
imagen, la imagen está formada espacios que tienen exactamente $N$ zumbadores que representan puntos negros y espacios sin zumbadores que representan puntos blancos.

Tú tarea como asistente consiste en ampliar la imagen de modo que cada espacio se amplíe por un factor de $N$ tanto horizontal como verticalmente. Por ejemplo, si en la imagen inicial había un espacio con 2 ($N=2$) zumbadores, deberás convertirlo en un
cuadro de 4 montones (2x2) de **1 (al ampliar la imagen basta dejar un zumbador por cada punto negro)** zumbador cada uno, igualmente, si en esa imagen hay un espacio sin zumbadores, deberás convertirla en un cuadro de 2x2 espacios sin zumbadores.

Al ampliar deberás hacerlo partiendo de la esquina inferior izquierda, y ampliar la imagen hacia arriba y hacia la derecha.

# Problema

Escribe un programa que dada la imagen inicial en un mundo, genere la ampliación solicitada.

# Consideraciones

- Karel inicia siempre en la posición (1,1) con dirección norte.
- Karel lleva un número infinito de zumbadores en su mochila.
- Para obtener los puntos de este problema los únicos zumbadores que deben quedar en el mundo son aquellos que representan la imagen ampliada.
- Te aseguramos que en todos los casos de prueba será posible ampliar la imagen sin que ningún punto negro salga del mundo al ser ampliado.
- No importa la posición ni orientación final de Karel.
- $N$ es menor o igual a 10, todos los puntos negros del mapa tendrán exactamente $N$ zumbadores.

# Ejemplo

Mundo inicial

![Mundo inicial](mundoinicial.png)

Mundo final

![Mundo final](mundofinal.png)
