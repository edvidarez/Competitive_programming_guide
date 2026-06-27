<div class="content-description screen">
        <div><p>Hay \(n\) magos en una fila numerados del 1 al n de izquierda a derecha. Cada mago tiene una capa de invisibilidad que puede llevar puesta en el lado izquierdo o en el lado derecha. Harry camina desde la posición del mago 1 hasta la posición del mago \(n\) \((1 \leq n \leq 105)\), y registra cuantos magos ve desde la posición de cada mago.</p>
<p>Un mago en la posición \(j\) es visible desde la posición \(i\) si:</p>
<ul>
<li>El mago en la posición \(j\) tiene la capa de invisibilidad a la izquierda de su traje y \(i \geq j\).</li>
<li>El mago en la posición \(j\) tiene capa de invisibilidad a la derecha de su traje \(i \leq j\).</li>
</ul>
<p>En particular nota que el mago \(i\) siempre es visible desde la posición \(i\).</p>
<p>La lista de Harry es muy antigua, pero después de investigar mucho lograste descifrarla.
La lista es un arreglo \(a\) de \(n\) elementos, tal que \(a_i\)  \((1 \leq a_i \leq n)\) es la cantidad de magos que vió desde la posición \(i\). Tu tarea es contar cuantas de todas las posibles formas en las que los magos pudieron llevar sus capas, son consistentes con la información de la lista.</p>
<p>Cuenta de cuantas formas distintos se pudieron haber organizado los magos. Dos arreglos de magos son distintos si existe alguna posición en la fila cuyos magos tienen orientaciones distintas de capas.</p>
<h3>Entrada</h3>
<ul>
<li>En la primera línea de la entreada un único entero \(t\), la cantidad de subcasos de prueba. siguen \(t\) casos de prueba, cada uno consiste de dos líneas.</li>
<li>En la primera línea de cada caso de prueba, un único entero \(n\), la cantidad de magos en la fila.</li>
<li>En la segunda línea \(n\) enteros separados por un espacio que indican el valor \(a_i\), la cantidad de magos visibles registrados desde la posición \(i\) en la lista de Harry.</li>
</ul>
<h3>Salida</h3>
<ul>
<li>Para cada subcaso de prueba, imprime un único entero indicando la cantidad formas distintas en las que se pudieron haber organizado los magos.</li>
</ul>
<h3>Ejemplo</h3>
<h4>Entrada</h4>

<pre><code>7
1
1
4
4 4 3 2
3
1 3 2
2
2 1
3
2 2 2
3
3 2 3
3
3 2 2</code></pre>
<h4>Salida</h4>

<pre><code>2
1
0
1
2
0
0</code></pre>
<p>A continuación se muestra una ilustración del segundo subcaso de prueba:</p>
<p><img src="images/b6886d99-c848-4d73-a233-7c32c246229e.png" alt="Explicación de los magos"></p>
<p>El mago \(1\) tiene la capa de invisibilidad a la izquierda, mientras que los magos \(2, 3\) y \(4\), la tienen a la derecha.</p>
<ul>
<li>Desde la posición \(1\), podemos ver a los magos \(1, 2, 3,\) y \(4\).</li>
<li>Desde la posición \(2\), podemos ver a los magos \(1, 2, 3,\) y \(4\).</li>
<li>Desde la posición \(3\), podemos ver a los magos \(1, 3,\) y \(4\).</li>
<li>Desde la posición \(4\), podemos ver a los magos \(1\) y \(4\).</li>
</ul>
<p>Por lo tanto, la lista de Harry termina siendo \(4, 4, 3, 2\). Se puede mostrar que este es el unicó arreglo de capas posible.</p>
<p>En el tercer caso, se puede mostrar que Harry no pudo haber obtenido su lista de ningún arreglo de capas. En el quinto caso, nota que hay dos posibles arreglos de capas a partir de los cuales Harry pudo haber obtenido la lista:</p>
<ul>
<li>El mago \(1\) portando la capa a la izquierda, el mago \(2\) a la derecha, y el mago \(3\) a la izquierda.</li>
<li>El mago \(1\) portando la capa a la derecha, el mago \(2\) a la izquierda, y el mago \(3\) a la derecha.</li>
</ul>
<h3>Consideraciones</h3>
<ul>
<li>\(1 \leq t \leq 104\).</li>
<li>\(1 \leq n \leq 105\).</li>
<li>\(1 \leq a_i \leq n\).</li>
<li>Se garantiza que la suma de \(n\) sobre todos los casos no excede \(10^5\).</li>
</ul>
<h3>Subtareas</h3>
<ul>
<li>Subtarea 1 <strong>(4 puntos):</strong> \(n = 2\).</li>
<li>Subtarea 2 <strong>(12 puntos):</strong> \(a_1 = n\).</li>
<li>Subtarea 3 <strong>(31 puntos):</strong> \(n \leq 12\).</li>
<li>Subtarea 4 <strong>(53 puntos): Sin restricciones adicionales.</strong></li>
</ul>
</div>

                    <hr>
            </div>
