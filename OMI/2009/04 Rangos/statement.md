# Descripción

Se tiene un renglón con casillas numeradas del 1 al $N$. Inicialmente cada casilla contiene el número 0. Los valores en las casillas del renglón se pueden actualizar utilizando el siguiente mecanismo:

- Se define un rango de casillas del renglón como $i$,  $j$, donde $i < j$.  Por ejemplo $i=3$, $j=6$.
- Se le suma 1 a la casilla $i$, 2 a la casilla $i+1$, 3 a la $i+2$, y así hasta llegar a la casilla $j$.

Por ejemplo, si $N=7$ se tiene un renglón de 7 posiciones que originalmente está lleno con 7 ceros {0,0,0,0,0,0,0}, al actualizar el rango 3, 6 el renglón queda {0,0,1,2,3,4,0}, una siguiente actualización al rango 4,7 dejaría el renglón como sigue: {0,0,1,3,5,7,4}.

Después de aplicar actualizaciones al renglón, se requiere poder responder preguntas del siguiente tipo:

- Se define un rango de casillas del renglón como $u$, $v$, donde $u < v$. Por ejemplo $u=4$, $v=6$.
- Se debe dar como respuesta la suma de los valores de todas las casillas comprendidas en el rango, módulo 10,000, es decir, el residuo que se obtiene si se divide el total entre 10,000.

#Problema
Dado el número $N$ y una serie de $A$ rangos de actualización escribe un programa que sea capaz de contestar $P$ preguntas en el tiempo dado.

# Entrada

Tu programa deberá leer de la entrada estándar los siguientes datos:

- La primera línea contiene 3 números enteros separados por un espacio: $N$, $A$ y $P$ que representan el largo del renglón, el número de actualizaciones y el número de preguntas respectivamente.
- Las siguientes $A$ líneas contienen $2$ números enteros cada una y representan un rango de actualización.
- Las siguientes $P$ líneas contienen 2 números enteros cada una y representan el rango de una pregunta.

# Salida

Tu programa deberá escribir a la salida estándar $P$ líneas, cada una con un número entero que representa la respuesta a la pregunta correspondiente.
**NOTA: Recuerda que las respuestas a las preguntas deberán ser módulo 10,000**.

#Ejemplo

||input
7 2 2
3 6
4 7
4 6
1 7
||output
15
20
||end

#Límites

* $1 <= N <= 1,000,000,000$
* $1 <= A <= 1,000$
* $1 <= P <= 1,000$
* En un subconjunto de los casos de prueba con un valor total de 30 puntos $N <= 1000$ y $A, P <= 100$
* En otro subconjunto de casos de prueba (distinto del anterior) con un valor total de 30 puntos, el rango de cada una de las preguntas nunca tendrá una longitud mayor a 1001 y  $A, P <= 100$

#Información útil
La fórmula para calcular la sumatoria de los números desde 1 hasta $k$  es la siguiente:

Suma de todos los números desde 1 hasta $k$ es igual a $$\frac{k(k + 1)}{2}$$
