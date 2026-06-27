El primer paso esta dado, ya encontraste la tumba, sin embargo, tus problemas apenas comienzan, primero deberá abrir la puerta y una vez adentro deberás sortear todas la trampas en el camino al tesoro. ¡Pero comencemos por el principio, antes que cualquier cosa hay que abrir la puerta!

Al llegar a la tumba te encuentras con una puerta repleta de palancas, todas las palancas son negras, salvo una de ellas, la cual es de un color rojo sangre.
En la puerta hay además una inscripción y una secuencia de números.
Tras leer la inscripción descubres que para abrir la puerta es necesario bajar todas las palancas, sin embargo, las palancas se deberán ir bajando siguiendo la secuencia de números en la puerta, con la condición de que la última palanca que se baje sea la palanca roja. Hay que ser muy cuidadoso, porque la inscripción dice que si se rompe la secuencia o si se baja la palanca roja antes de bajar todas las negras "... su alma será condenada a los fuegos eternos mientras dure la era del quinto sol."

La forma de ir bajando las palancas es la siguiente:
inicialmente se baja una palanca, que puede ser cualquiera. A partir de ésta se cuenta un número x1 de palancas, donde x1 es el primer número de la secuencia escrita en la puerta y se baja la palanca en donde quedaste, de ahí, cuentas x2 palancas dónde x2 es el segundo número de la secuencia y nuevamente bajas la palanca correspondiente.
Continuando con la secuencia hasta que todas las palancas estén abajo. Las palancas siempre se cuentan en el mismo sentido, es decir, siempre hacia la derecha y si llegas al final debes de seguir contando por el principio. Al contar las palancas no debes tomar en cuenta las que ya estén abajo.

# Problema

Debes escribir un programa que conociendo el número de palancas, la posición de la palanca roja y la secuencia de números, te diga cual es la primera palanca que debes bajar para que siguiendo la secuencia de números, la última palanca que bajes sea la palanca roja.

# Entrada

Tu programa deberá leer los siguientes datos: en la primera línea el número 9 $\le$ P $\le$ 20000 de palancas en la puerta, en la segunda línea el número R, dónde 1 $\le$ R $\le$ P que indica la posición de la palanca roja contando a partir de 1 y por último en la tercera línea P-1 números separados por un espacio que indican la secuencia que se debe llevar en el conteo de palancas.Los números de la secuencia de saltos son todos entre 1 y 16.

# Salida

Tu programa deberá un único número indicando la posición de la primera palanca que se debe bajar.

# Ejemplo

||input
9
7
1 2 4 5 3 1 7 8

||output
5
||end

# Consideraciones

9 $\le$ P $\le$ 20000
1 $\le$ R $\le$ P
Los números de la secuencia de saltos son todos entre 1 y 16.
