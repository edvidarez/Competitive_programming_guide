Nieves, un famoso integrante del COMI, se ha aficionado a cocinar pizzas. Lo que diferencia a Nieves de cualquier otro pizzero es que Nieves puede cocinar pizzas de cualquier diámetro. Por si fuera poco, Nieves está haciendo su maestría en visión computacional.

Nieves cocina pizzas una por una. Cada que termina una pizza, Nieves la coloca encima de las pizzas anteriores de modo que su centro quede alineado con los centros de todas las pizzas anteriores. Cuando alguien le pide una de las pizzas de la pila, Nieves toma esa pizza y tira a la basura todas las pizzas que estaban arriba de ella.

Como proyecto de maestría Nieves ha desarrollado un sistema de visión computacional para supervisar sus pizzas, dicho sistema funciona de la siguiente manera: hay una cámara colocada en el techo, justo encima del centro de la pila de pizzas. En cualquier momento, Nieves puede solicitarle a su sistema que le diga ¿cuántas pizzas ve?. Dado que la cámara está arriba, las pizzas de mayor diámetro tapan a las pizzas pequeñas que están debajo de ellas en la pila. Si hay dos pizzas del mismo diámetro juntas, la cámara sólo ve la que esté más arriba.

Nieves desea que le ayudes a comprobar si su sistema funciona correctamente.

###Problema
Escribe un programa que sea capaz de procesar 3 tipos de comandos:

* Comando $0$: Al recibir este comando tu programa deberá contestar cuántas pizzas ve la cámara en ese momento.
* Comando $1$  $d$: Este comando le indica a tu programa que Nieves apiló una nueva pizza de diámetro $d$.
* Comando $2$  $q$: Este comando le indica a tu programa que Nieves quitó $q$ pizzas de la pila. Nieves nunca quita más pizzas de las que hay en la pila en un momento dado.

###Entrada

Tu programa debe leer del teclado la siguiente información:

* En la primer línea el número $N$, la cantidad de comandos que recibirá tu programa.
* En las siguientes $N$ líneas puede haber 1 ó 2 números. El primer número será un 0, 1 ó 2 e indicará el tipo del comando.  En el caso de los comandos 1 y 2 habrá un segundo número que indica el valor de $d$ o $q$ respectivamente.

###Salida

Por cada comando del tipo $0$ que haya en la entrada tu programa deberá escribir una línea con un número que indique la cantidad de pizzas que veía la cámara en ese momento.

###Restricciones

* $1 \le N \le 500,000$		La cantidad de comandos a ejecutar.
* $1 \le q \le N$			El número de pizzas que se quitan de una pila en un comando.
* $1 \le d \le 1,000,000,000$	Diámetro de una pizza.


#Ejemplo

||input
9
0
1 3
1 1
0
1 4
0
1 2
2 2
0
||output
0
2
1
2
||description
En la entrada hay 4 comandos del tipo 0.

El primer comando tipo 0 llega cuando no hay pizzas en la pila por lo que la respuesta es 0.

Después se apilan dos pizzas, una de diámetro 3 y encima una de diámetro 1,
la de diámetro 1 no tapa a la de diámetro 3.

En el segundo comando tipo 0 la cámara ve 2 pizzas.

Posteriormente se apila una pizza de diámetro 4 que al ser mayor tapa todas las anteriores.

Con el tercer comando tipo 0 la cámara ve sólo 1 pizza.

Finalmente se quitan dos pizzas, las dos pizzas de arriba son las de diámetro 2 y 4 respectivamente,
al quitarlas quedan únicamente las pizzas de diámetro 3 y 1.

Cuando llega el último comando tipo 0, la cámara ve 2 pizzas.
||end

#Evaluación

* Para un conjunto **agrupado** de casos de prueba con valor de $11$ puntos los diámetros de las pizzas serán decrecientes, es decir, cada nueva pizza es menor que las pizzas anteriores.
* Para otro conjunto **agrupado** de casos de prueba con valor de $17$ puntos, $N \le 5,000$.
* Para otro conjunto **agrupado** de casos de prueba con valor de $29$ puntos no existe el comando quitar.
* Para el último conjunto **agrupado** de casos de prueba con valor de $43$ puntos, $N \le 500,000$ y $d \le 1,000,000,000$.

-------------------------------------------------------

> Ahí véale... reevalúele bien.
