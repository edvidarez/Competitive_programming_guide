# Llegando en K movimientos

El COMI acaba de inventar un nuevo juego. El objetivo del juego es hacer llegar una ficha de la posición de salida a una posición destino en exactamente k movimientos.

En total hay N posiciones numeradas del 1 al N. Además hay M caminos que unen, cada uno, un par de posiciones.  El juego inicia siempre con la ficha en la posición 1. En cada turno, si la ficha está en la posición i  y hay un camino entre la posición i y la j es posible mover la ficha de la posición i a la j. Si hay un camino entre la posición i  y la j, ese camino puede usarse para moverse tanto de i a j como de j a i. Durante el juego, está permitido que la ficha pase por la misma posición cualquier cantidad de veces. Es obligatorio mover la ficha en cada turno.

# Problema

Escribe un programa que recibiendo el número N de posiciones y la lista de M caminos en el juego pueda contestar preguntas del tipo: “¿Es posible llegar, desde la posición 1 a la posición d en k movimientos?”

# Entrada

Tu programa debe leer del teclado la siguiente información:

*En la primer línea los números N y M, el número de posiciones y de caminos, respectivamente.
* En las siguientes M líneas hay dos números enteros separados por un espacio que representan las casillas que une ese camino.
* En la siguiente línea, el número P que representa la cantidad de preguntas que se le harán a tu programa.
* En las últimas P líneas hay dos enteros separados por un espacio que representan la posición destino di a la que se quiere llegar y el número k<sub>i</sub> de movimientos que se deben utilizar.

# Salida

Tu programa debe escribir en pantalla P líneas con un número cada una. La i-ésima línea debe contener 1 si es posible llegar desde la posición de salida (posición 1) a la posición destino d<sub>i</sub> en exactamente k<sub>i</sub> movimientos, en caso contrario debe contener 0 como respuesta.

# Restricciones

<pre>
1 < N <= 5,000           Número de posiciones.
1 <= M <= 500,000        Número de caminos en el juego.
1 <= P <= 5,000          Número de preguntas que tu programa debe contestar.
1 <= K <= 1,000,000,000  Máximo de movimientos.
</pre>


# Ejemplo

<img src="http://gestii.com/omi/llegando.png" />

<table width="100%" border="1">
	<tr>
		<th>Entrada</th>
		<th>Salida</th>
		<th>Explicación</th>
	</tr>
	<tr>
		<td valign="top">
<pre>
6 8
1 2
1 4
3 4
2 5
4 6
5 6
4 5
3 6
3
3 2
6 5
6 1
</pre>
		</td>
		<td valign="top">
<pre>
1
1
0
</pre>
		</td>
		<td valign="top">
			La imagen muestra 6 posiciones y 8 caminos.<br />
			Hay 3 preguntas que se responden de la siguiente manera:
			<br /><br />
			1.¿Es posible llegar a la posición 3 en 2 movimientos? La respuesta es SI y por lo tanto se contesta 1. Se llega en 2 movimientos es moverse del 1 al 4 y del 4 al 3.
			<br /><br />
			2.¿Es posible llegar a la posición 6 en 5 movimientos? De nuevo es SI y se responde 1. La ruta es 1-2-5-4-3-6
			<br /><br />
			3.¿Es posible llegar a la posición 6 en 1 movimiento? La respuesta es NO, se responde 0.
		</td>
	</tr>
</table>

# Evaluación

Para un grupo de casos de prueba con un valor total de 30 puntos K siempre será menor o igual que 10.
Para otro grupo de casos distinto con un valor total de 30 puntos K siempre será menor o igual que 1,000.
Para obtener los últimos 40 puntos será necesario que resuelvas correctamente todos los casos de prueba cuya K sea mayor que 1,000.
