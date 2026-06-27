Cada vez estas más cerca de tu objetivo, sin embargo te has topado con un nuevo obstáculo. Para llegar al cuarto en donde se encuentran los tesoros del patriarca es necesario atravesar un piso cuadriculado lleno de trampas mortales. Cada cuadro en el piso puede esconder una trampa mortal, por lo que es necesario saber cuales cuadros son los que no tienen ninguna trampa.

Afortunadamente los OMIncas eran muy olvidadizos y siempre dejaban anotadas instrucciones acerca de cómo evitar sus propias trampas y esta vez no fue la excepción. Hay dibujada en el piso una cuadrícula más pequeña de M columnas por N filas, ésta cuadrícula tiene algunas posiciones marcadas, dichas posiciones indican los cuadros que son seguros para pisar, sin embargo la cuadrícula pequeña tiene menos cuadros que la del piso que mide 100 x 100 cuadros. Junto a la cuadrícula pequeña hay una serie de parejas de números.

Después de meditar un rato y hacer algunas pruebas, te das cuenta que estos números indican dobleces. El primer número indica la orientación del doblez (horizontal o vertical) y el segundo indica cuantos cuadros se doblaron. Observas que si "desdoblas" por completo la cuadrícula pequeña siguiendo las instrucciones, obtienes una cuadrícula de 100 x 100 con marcas en diferentes lugares que indican los cuadros seguros.

Cuando se hace un desdoble las marcas en la cuadrícula se reflejan utilizando como eje de simetría el extremo de la cuadrícula. Los desdobles horizontales siempre se harán por el lado izquierdo y los verticales siempre por abajo. Nunca se pueden desdoblar más cuadros de los que tiene la cuadrícula inicial.

Un "desdoble" se hace de la siguiente forma, supongamos que la cuadrícula pequeña es de 5x5 y que el desdoble dice (horizontal, 3 seguido por un vertical, 2). Después de desdoblar se tendría:

# Problema

Debes escribir un programa que lea la cuadrícula inicial y la secuencia de desdobles que vaya "desdoblando" la cuadrícula inicial para determinar todos los puntos de la cuadrícula del piso que se pueden pisar.

# Entrada

Tu programa deberá leer los siguientes datos, en la primera línea 2 números, 3 $\le$ M, N $\le$ 16, en las siguientes N líneas deberás leer M números en cada línea indicando si las posiciones de la cuadrícula inicial son seguras o no, un '0' indica una posición marcada con trampa y un '1' indica una posición marcada como segura.

Después de leer la cuadrícula en la siguiente línea esta el número 1 $\le$ D $\le$ 200 que indica el número de desdobles que se van a realizar sobre la cuadrícula y en las últimas D líneas hay 2 números en cada línea indicando la orientación del doblez y el número de cuadros doblados. Para la orientación del doblez un '0' indica un doblez horizontal y un '1' indica un doblez vertical.

# Salida

Tu programa deberá escribir todas las posiciones de la cuadrícula grande que se pueden pisar, las posiciones deberán estar dadas como coordenadas (x, y), considerando que la esquina inferior izquierda de la cuadrícula del piso es la coordenada (1,1).

# Ejemplo

||input
16 16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
7 0 16 0 32 0 36 1 10 1 20 1 4 1 50

||output
18 3
23 3
50 3
55 3
82 3
87 3
18 98
23 98
50 98
55 98
82 98
87 98
||end

# Consideraciones

Después de hacer todos los desdobles, siempre obtendrás un cuadrado de 100 x 100 cuadros que representa el piso cuadriculado

3 $\le$ M, N $\le$ 16 y 1 $\le$ D $\le$ 200
