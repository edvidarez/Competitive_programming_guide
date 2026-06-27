#Descripción

Hay una caja fuerte cuya cerradura se abre girando discos concéntricos.  En vez de números, los discos de la cerradura tienen una secuencia con letras del alfabeto de la $a$ a la $z$.

Para abrir la cerradura se gira cada uno de los discos en sentido horario o contra-horario, según se quiera, hasta llegar a una posición deseada.  Cada que se avanza una letra en uno de los discos, sin importar el sentido se dice que se está girando un paso.

La cerradura se representa como una matriz cuadrada de largo n en donde cada casilla contiene una letra y cada cuadrado concéntrico representa un disco de la cerradura.

#Problema

Dadas dos matrices, la primera representando el estado actual de los discos y la segunda el estado de los mismos que abre la caja, escribe un programa que determine el número mínimo de pasos que se requieren para colocar todos los discos en la posición necesaria para abrir la caja.

#Entrada

Tu programa deberá leer de la entrada estándar los siguientes datos:

- En la primera línea el número entero $N$ que representa el largo de la matriz.
- En las líneas de la 2 a la $N+1$ habrá $N$ letras consecutivas en cada una que representan el estado actual de los discos de la cerradura.
- En las líneas de la $N + 2$ a la $2N + 1$ habrá $N$ letras consecutivas en cada una que representan el estado en el que deben quedar los discos para abrir la cerradura.

#Salida

Tu programa deberá escribir en salida estándar lo siguiente:
Un único número entero que representa el número mínimo de pasos necesarios para abrir la cerradura.

#Ejemplos

||input
3
abc
def
ghi
gda
heb
ifc
||output
2
||description
Para abrir la cerradura es necesario girar el disco exterior dos pasos en sentido horario.

    abc    dab    gda

    d f -> g c -> h b

    ghi    hif    ifc

||input
4
abcd
efgh
abcd
efgh
eabc
agcd
efbh
fghd
||output
2
||description
Para abrir la cerradura es necesario girar el disco exterior un paso en sentido horario y el interior un paso en sentido contra-horario

    abcd    eabc
    e  h -> a  d    fg -> gc
    a  d    e  h    bc    fb
    efgh    fghd

||end

#Limites

* $2 \le N \le 2,000$
* En un subconjunto de los casos de prueba, con valor total de 85 puntos $N \le 100$

#Información útil

En los casos oficiales de la OMI 2009, hay 3 casos que estan mal, el caso 7, 8 y 9 (incluso la solución oficial no los resuelve). En este problema ya se corrigieron estos errores.
