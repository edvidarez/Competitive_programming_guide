Se tiene una secuencia de números enteros S = {s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>N</sub>}. Los números de la secuencia tienen valores entre –100 y 100. Llamemos recorrido circular de la secuencia a tomar cualquier número de la secuencia, por ejemplo si y a continuación sumar todos los números de la secuencia en el orden si, si+1,..., sN, s1,... si-1 es decir, al llegar al final de la secuencia deberás seguir sumando los números del principio hasta darle toda la vuelta.

Dependiendo del número de la secuencia en donde empieces, el valor máximo y mínimo al que llegará la suma será distinto. Por ejemplo, si se tiene la secuencia S = {3, 1, -2, 2, -5} y decides comenzar por el 3, el valor de la suma tomará los siguientes valores: inicia con 3, 4 (al sumar el 3 y el 1), 2 (al sumar el cuatro que llevábamos con el –2), 4, -1. De modo que el valor máximo que alcanzó la suma fue de 4 y el valor mínimo fue de –1. Sin embargo, si hubiéramos iniciado del –2, los valores de la suma serían: -2, 0, -5, -2, -1. De modo que el valor máximo de la suma fue de 0 y el valor mínimo fue de –5.

Le llamaremos absoluto circular al valor absoluto de la suma del valor máximo y el mínimo alcanzado. Para nuestros dos ejemplos anteriores, el absoluto circular es: para el primer caso |4 + (-1)| = 3, para el segundo caso |0 + (-5)| = 5.

# Problema

Escribe un programa, que dada una secuencia de números, determine en que elemento de la secuencia se debe iniciar el recorrido circular para que el absoluto circular sea el mínimo posible.

# Entrada

Tu programa deberá leer del teclado de la PC los siguientes datos.

- En la primera línea el número 0 < N $\le$ 30,000.
- En la segunda línea habrá N números enteros separados por un espacio cada uno que representan los elementos de la secuencia.

# Salida

Tu programa deberá escribir en la pantalla de la PC un único número indicando la posición en la que debe comenzar el recorrido circular para que el absoluto circular sea el mínimo posible.

# Ejemplo

||input
5
3 1 -2 2 -5

||output
4
||end

Si se inicia de la posición 4, el valor máximo de la suma será 2 y el valor mínimo será –3. El absoluto circular es 1, y es el mínimo para la secuencia de ejemplo.
