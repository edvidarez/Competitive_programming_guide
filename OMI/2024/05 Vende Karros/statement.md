Karel abrió una agencia de carros de lujo donde los millonarios de la ciudad vienen a despilfarrar su dinero. En su agencia, Karel ofrece carros de $N$ marcas distintas. De la marca $i$ tiene $a_i$ unidades disponibles.
<br /> <br />
Karel, que todo lo sabe, conoce una técnica milenaria para vender carros que es efectiva con los clientes excéntricos que visitan su agencia: cuando un cliente llega con la intención de comprar un carro de cualquiera de las marcas, Karel puede convencerlo de comprar hasta 3 carros siempre y cuando sean de marcas distintas.
<br /> <br />
Karel se aburrió muy pronto de atender la agencia y prefiere irse a recorrer el mundo de mochilazo. Obvio, primero quiere vender todos los carros para tener fondos con que hacerlo.
<br /> <br />
Dada la cantidad de carros que tiene en su agencia en este momento, ¿cuál es la mínima cantidad de clientes que necesita Karel para vender todos sus carros?

#Ejemplos

||input
3
1 2 3
||output
3
||input
6
2 3 2 4 1 5
||output
6
||end

<img src="https://i.imgur.com/LH000BJ.jpeg" />

La tabla de la izquierda explica cómo Karel pudo haber vendido los carros en el primer ejemplo. La tabla de la derecha explica cómo pudo haber vendido los carros en el segundo ejemplo.

#Entrada

* En la primera línea un único entero $N$, la cantidad de marcas distintas.
* En la segunda línea $N$ enteros separados por un espacio que indican la cantidad $a_i$ de unidades del carro de la marca $i$.

#Salida

* Un único entero indicando la cantidad mínima de clientes necesarios para vender todos los carros.

#Consideraciones

* $1 \leq N \leq 5 \times 10^5$.
* $1 \leq A_i \leq 10^9$.

#Subtareas

* Subtarea 1 (10 puntos): $N=3$.
* Subtarea 2 (20 puntos): $N \leq 1000$ y se asegura que la suma de los $a_i$ es menor o igual a $1000$.
* Subtarea 3 (30 puntos): Se asegura que la suma de los $a_i$ es menor o igual a $5 \times 10^5$.
* Subtarea 4 (40 puntos): Sin consideraciones adicionales.
