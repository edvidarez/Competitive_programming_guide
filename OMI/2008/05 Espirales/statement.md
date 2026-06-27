# Descripción

Tenemos una cuadrícula de números enteros sobre la que deseamos formar espirales. Las reglas para formar una espiral sobre la cuadrícula son las siguientes:

 - La espiral puede iniciar en cualquier casilla de la cuadrícula

 - La espiral puede girar hacia la izquierda o hacia la derecha.

 - A partir de la posición de inicio de la espiral, está puede iniciar con dirección norte, este, sur u oeste.

 - No debe quedar ningún espacio vacío en la espiral.

 - La espiral sólo puede continuar si la siguiente casilla contiene un número mayor  que el contenido en la última casilla de la espiral hasta ese momento.

![Espiral válida](valida.jpeg)

*Espiral válida (cuadrada).  A partir del inicio avanzas en cada dirección (1,1,2,2,3,3,4,4,...) casillas.*

![Espiral inválida](invalida.jpeg)

*Espiral NO VÁLIDA (rectangular).  A partir del inicio se avanzó 2 casillas en la misma dirección.*

El largo de una espiral se mide como el número de casillas que contiene.

# Problema

Dada una cuadrícula determina cual es la espiral más larga que se puede formar

# Entrada

Tu programa deberá leer de la entrada estándar los siguientes datos:

 - La primera línea contiene un número $N$ entre 4 y 100 que determina el lado de la cuadrícula.

 - Las siguientes $N$ líneas contienen $N$ números enteros $a_i$ entre 0 y 30,000 cada una separados por espacios.

# Salida

Tu  programa deberá  escribir  a  la  salida  estándar  una  línea  que  contenga  un  único  número $L$ que  indique  la  longitud de la espiral más grande que se pueda dibujar en la cuadrícula

# Ejemplo

||input
5
1 3 2 10 5
2 4 3 9 2
3 6 7 8 1
8 9 6 5 2
8 6 5 3 1
||output
7
||description
La  espiral  de  largo  7  se  logra  iniciando  en  el  3  de  la  segunda  fila,  tercera  columna  arrancando  hacia  el  oeste  con el giro hacia la derecha.  De modo que la espiral queda formada por la sucesión {3,4,6,7,8,9,10} y tiene un largo de 7.
||end

# Límites

* $4 \leq N \leq 100$
* $a_i \leq 0 \leq 30000$
