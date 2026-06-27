 El 12  de octubre se conmemora la llegada a América del navegante Cristóbal Colón en 1492. Este acontecimiento propició el encuentro de dos mundos. Con ello, llegaron muchos problemas, como *probablemente* el siguiente:

# Problema

 Para un valor de $k$ fijo, definamos la secuencia de listas de números enteros $S_k$ de la siguiente manera:

<img src="https://i.imgur.com/vEeJzCR.jpeg" />

Donde $+$ representa concatenación de listas.
<br /> <br />
Por ejemplo, para $k = 1$, los primeros términos de la secuencia se verían así:
<br /> <br />
$S_{1, 1} = \\{0\\}, S_1 = \\{0, 1, 0\\}, S_{1, 2} = \\{0, 1, 0, 2, 0, 1, 0\\}, . . . $
<br /> <br />
Para $k = 2$, los primeros términos de la secuencia se verían así:
<br /> <br />
$S_{2, 0} = \\{0,0\\}, S_{2, 1} = \\{0,0,1,0,0,1,0,0\\},$

$S_{2, 2} = \\{0,0,1,0,0,1,0,0,2,0,0,1,0,0,1,0,0,2,0,0,1,0,0,1,0,0\\}, . . .$
<br /> <br />
Dado un entero $Q$, responde $Q$ preguntas. En la $i$-ésima pregunta, te serán dados dos enteros, $k_i$, y $x_i$. Debes responder con el valor en la posición $x_i$ en la lista $S_{k_i, 2024}$.

#Entrada

* La primera línea contiene el entero $Q$. La cantidad de preguntas a responder.
* Las siguientes $Q$ líneas tienen dos enteros cada una $k_i$ y $x_i$. Debes responder el valor del número en la posición $x_i$ en la lista $S_{k_i, 2024}$

#Salida

Debes imprimir $Q$ líneas, cada una con la respuesta de la pregunta correspondiente.

||input
3
1 24
2 12
3 20
||output
3
1
1
||input
3
9 48
6 49
4 50
||output
0
2
2
||end

#Consideraciones

* $1 \le Q \le 10^6$.
* para todo $1 \le i \le Q$, se cumple que $1 \le k_i, x_i \le 10^{9}$.

#Subtareas

* Subtarea 1 (5 puntos): Para todo $1 \le i \le Q$, se cumple que $x_i = 2$.
* Subtarea 2 (10 puntos): $Q \le 1000$ y para todo $1 \le i \le Q$, se cumple que $x_i \le 1000$.
* Subtarea 3 (15 puntos): Para todo $1 \le i \le Q$, se cumple que $k_i = 1$ y $x_i \le 10^6$.
* Subtarea 4 (30 puntos): Para todo $1 \le i \le Q$, se cumple que $k_i \le 10$.
* Subtarea 5 (40 puntos): Sin restricciones adicionales.
