# Jardín de Niños

En un jardín de niños decidieron jugar un juego muy peculiar. El juego es así:

Hay N niños numerados del 1 al N, cada niño trae un pañuelo. Luego, todos se acomodan en posiciones distintas sobre una línea. Por último cada uno decide hacia dónde correr (hacia la izquierda o la derecha).  Acto seguido y de manera simultánea todos los niños empiezan a correr en la dirección que eligieron.

Los niños corren todos a la misma velocidad (1 unidad cada segundo). Si dos niños se topan de frente, intercambian sus pañuelos instantáneamente y cambian de dirección. El jardín de niños es muy grande por lo que los niños pueden continuar corriendo siempre sin miedo a salirse de él.

Mientras jugaban muy divertidos, dio la hora de la salida y las mamás comenzaron a llegar. Para que cada niño se pueda ir necesita volver a tener su pañuelo. Esto se puede si la maestra sabe en qué posición se encuentra el pañuelo del i-ésimo niño y qué niño es el que lo trae.

# Problema

Escribe un programa que dado un tiempo k en segundos contados desde el inicio del juego pueda responder preguntas de cualquiera de los siguientes tipos:

* ¿En qué posición de la línea se encuentra en ese momento el pañuelo del i-ésimo niño?
* ¿El pañuelo de qué niño tiene en ese momento el i-ésimo niño?

_NOTA_: El índice i de i-ésimo se refiere al número del niño, no a la posición en la que se acomodó. Recuerda que los niños están numerados del 1 al N.

# Entrada

Tu programa debe leer del teclado los siguientes datos:

* La primera línea contiene el entero N, la cantidad de niños.
* Las siguientes N líneas tienen dos enteros p<sub>i</sub> y d<sub>i</sub>, la posición inicial en la línea del i-ésimo niño y la dirección en la que corre cuando empiezan a jugar (1 indica derecha; -1 indica izquierda)
* La línea N+1 contiene el entero Q que indica cuántas preguntas se te harán.
* Las últimas Q líneas son preguntas: inician con un caracter 'P' o 'N' y después dos enteros i y k.
  * Si el carácter es 'P', la pregunta es: ¿En que posición está el pañuelo del i-ésimo niño en el segundo k del juego?
  * Si es 'N', la pregunta es: ¿El pañuelo de qué niño trae el i-ésimo niño en el segundo k del juego?

_NOTA_: El intercambio de pañuelos es instantáneo, por lo que si se pregunta por el pañuelo que trae un niño en el momento en el que acaba de chocar, se debe reportar como respuesta el pañuelo que se intercambió, es decir, primero sucede el intercambio y luego se reporta.

# Salida

Tu programa debe escribir en la pantalla Q líneas cada una con un entero. La j-ésima de estas líneas debe contener la respuesta a la j-ésima pregunta.

# Restricciones

<pre>
1 <= N <= 1,000,000	       El número total de niños
1 <= pi <= 1,000,000,000   La posición inicial de cada niño en la línea
1 <= Q <= 50               El número de preguntas que se le harán a tu programa
1 <= kj <= 1,000,000,000   La cantidad de segundos que ha durado el juego en la pregunta j
</pre>


# Ejemplo

<table width="100%" border="1">
	<tr>
		<th>Entrada</th>
		<th>Salida</th>
		<th>Explicación</th>
	</tr>
	<tr>
		<td valign="top">
<pre>
4
4 1
1 1
6 -1
8 -1
2
P 2 2
N 3 4
</pre>
		</td>
		<td valign="top">
<pre>
3
2
</pre>
		</td>
		<td valign="top">
La primera pregunta es: ¿En qué posición está el pañuelo del niño 2 en el segundo 2?
<br /><br />
El niño 2 empieza en la posición 1 corriendo hacia la derecha, para el tiempo 2 no ha chocado con nadie y ha avanzado 2 unidades, por lo que él y su pañuelo se encuentran en la posición 3.
<br /><br />
La segunda pregunta es: ¿Qué pañuelo trae el niño 3 en el segundo 4?
<br /><br />
El niño 3 empieza en la posición 6 corriendo hacia la izquierda, en el primer segundo se topa con el niño 1 en la posición 5, intercambian pañuelos y cambian de dirección, el niño 3 trae ahora el pañuelo 1. En el segundo 2 se topa con el niño 4 en la posición 6, intercambia pañuelo y cambia dirección. Ahora trae el pañuelo 4. Finalmente en el segundo 3.5 choca por última vez con el niño 1 (que choco previamente con el niño 2 y trae su pañuelo) en la posición 4.5 intercambian pañuelos y para el segundo 4 lleva el pañuelo del niño 2.
		</td>
	</tr>
</table>

# Evaluación

Para un grupo de casos de prueba con valor de 50 puntos, k es menor o igual que 100 en todas las preguntas.

Además, para un grupo de casos de prueba con valor de 30 puntos (algunos de los cuales están incluidos en los 50 puntos de la línea anterior), el caso contendrá únicamente preguntas del tipo P.

