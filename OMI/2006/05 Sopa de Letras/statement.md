De camino a la OMI has pasado horas interminables en el autobús y para pasar el rato te has puesto a resolver una sopa de letras.

Como ya te imaginarás, una sopa de letras consiste de un arreglo rectangular en cada una de cuyas posiciones se encuentra una letra minúscula.

Además, se tiene una lista de palabras (formadas cada una exclusivamente por letras minúsculas) que se deben de buscar en el arreglo. Una palabra puede aparecer en el arreglo en ocho posibles direcciones comenzando desde su primera letra: hacia arriba, hacia abajo, hacia la derecha, hacia la izquierda y en las cuatro direcciones diagonales. Además, una palabra puede aparecer en más de un lugar.

# Problema

Deberás escribir un programa que reciba como entrada las dimensiones del arreglo rectangular, las letras que aparecen en el mismo, el tamaño de la lista y la lista de palabras a buscar y que determine cuántas veces aparece cada una de estas palabras en el arreglo.

# Entrada

Tu programa deberá leer del teclado de la PC los siguientes datos:

* En la primera línea los números 0 < N, M $\le$ 100 los cuales representan el número de renglones y el número de columnas del arreglo, respectivamente.
* En cada una de las siguientes N líneas una cadena de M letras minúsculas, las cuales representan el arreglo.
* En la siguiente línea el número 0 < K $\le$ 20000 que representa el tamaño de la lista de palabras.
* En cada una de las siguientes K líneas una palabra Pi de 2 a 100 letras minúsculas.

# Salida

Tu programa deberá escribir en la pantalla de la computadora K líneas y en cada una de ellas debe aparecer la cantidad X<sub>i</sub> de veces que aparece la palabra P<sub>i</sub>.

# Ejemplo

||input
2 3
aal
ala
2
al
ala

||output
6
2
||end

# Consideraciones

Puedes asumir que 0 < N, M $\le$ 100 y 0 < K $\le$ 20000.
