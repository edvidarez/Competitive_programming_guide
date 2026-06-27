# Descripción

Hay una cuadrícula cuadrada llena de 0’s y 1’s. Dentro de ésta cuadrícula hay varios subcuadrados de diferentes tamaños que están formados exclusivamente por 0’s. Por ejemplo en la siguiente cuadrícula:

<center>![Cuadrícula](cuadrados_html_730b365b.gif)</center>

Hay 1 subcuadrado de $3 \times 3$ formado únicamente por ceros, además hay 5 subcuadrados de $2 \times 2$ formados únicamente por ceros. Por último hay 12 subcuadrados de $1 \times 1$ que están formados por ceros.

# Problema

Tu tarea consiste en escribir un programa que, dada una cuadrícula de $N \times N$, determine cuantos subcuadrados de ceros hay que sean de $1 \times 1$, $2 \times 2$, $...$ , $N-1 \times N-1$ y $N \times N$.

# Entrada

En la primera línea recibirás un entero $N$ indicando el tamaño de la cuadrícula. En las siguientes $N$ líneas habrá $N$ caracteres `0` o `1` separados por espacios: los valores de cada cuadro en la cuadrícula.

# Salida

Tu programa deberá imprimir $N$ líneas. La $i$-ésima línea deberá contener únicamente un entero que indique la cantidad de subcuadrados de 0's de tamaño $i \times i$ que hay en la cuadrícula.

# Ejemplo

|| input
4
0 0 0 1
0 0 0 1
0 0 0 1
1 0 0 0
|| output
12
5
1
0
|| end

# Límites

 $2 \leq N \leq 1,000$

<img src="c540f123f4a4fa18093e327c2aca2e160b1771c6.png" style="float: right" />
