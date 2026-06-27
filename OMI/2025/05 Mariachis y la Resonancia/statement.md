<div class="content-description screen">
        <div><p>La \(30^a\) <strong>Olimpiada Mexicana de Informática (OMI)</strong> preparó un reto especial inspirado en la acústica del emblemático <strong>Teatro Degollado</strong>.</p>
<p>En el escenario hay un conjunto de \(n\) <strong>mariachis</strong> organizados en un arreglo \(a\) de tamaño \(n\). Cada posición del arreglo representa a un mariachi, y cada uno puede estar <strong>ausente</strong> (representado con \(-1\)) o presente tocando una nota musical con un cierto <strong>volumen</strong> (representado con un entero positivo).</p>
<p>El teatro tiene una <strong>resonancia característica</strong> descrita por un número entero \(k\). Al sonido final se le llama <strong>armonioso</strong> si se cumple que el volumen máximo entre todos los mariachis es exactamente igual a \(k\).</p>
<p>Te preguntas cuántas formas hay de asignar volúmenes a los mariachis ausentes de forma que su sonido sea armonioso, a lo cual responderás de la siguiente forma:</p>
<ul>
<li>Si hay una cantidad par de asignaciones válidas, imprime \(0\). </li>
<li>Si hay una cantidad impar de asignaciones válidas, imprime \(1\).</li>
</ul>
<p>Dos formas de asignar volúmenes se consideran diferentes si existe al menos un mariachi ausente que toca una nota distinta en una de las formas.
Una sola operación como la anterior se le hace insuficiente al COMI (Consejo Operador de Música Innovadora), por lo que te piden responder de la forma descrita en el párrafo anterior después de cada una de \(q\) operaciones. Las operaciones (escritas en líneas separadas) son de la forma</p>
<p>\(i\)  \(x\)</p>
<p>y consisten en actualizar la posición \(i\) con el valor \(x\) (puede ser \(-1\) si el mariachi está ausente, o un entero positivo si toca con ese volumen).</p>
<h3>Entrada</h3>
<ul>
<li>La primera línea contiene tres enteros \(n, q\) y \(k\).</li>
<li>La segunda línea contiene \(n\) enteros \(a_1, a_2, . . . , a_n\), representando el arreglo inicial de notas que tocan los mariachis.</li>
</ul>
<p>A continuación siguen \(q\) operaciones, cada una con el formato \(i\) \(x\) con \((1 \leq i \leq n)\) y \(x = -1\) o \(1 \leq x \leq 10^6\). Esto indica que debes asignarle el valor \(x\) a la posición \(i\).
Imprime la respuesta para el arreglo después de cada operación.</p>
<h3>Salida</h3>
<p>Por cada operación, imprime una línea con un entero:</p>
<ul>
<li>\(0\) si el número de formas de llenar los lugares vacíos para que el máximo de todos los volúmenes sea exactamente \(k\) es par.</li>
<li>\(1\) si el número de formas de llenar los lugares vacíos para que el máximo de todos los volúmenes sea exactamente \(k\) es impar.</li>
</ul>
<h3>Ejemplo</h3>
<h4>Entrada</h4>

<pre><code>5 3 7
2 -1 6 1 6
1 3
2 1
3 7</code></pre>
<h4>Salida</h4>

<pre><code>1
0
1</code></pre>
<ul>
<li>Después de la primera actualización, el arreglo es \([3, -1, 6, 1, 6]\). Existe una única asignación válida, que es el arreglo \([3, 7, 6, 1, 6]\).</li>
<li>Después de la segunda actualización, el arreglo es \([3, 1, 6, 1, 6]\), y como no hay ningún mariachi ausente, no existe ninguna asignación posible.</li>
<li>Después de la tercera actualización, el arreglo es \([3, 1, 7, 1, 6]\). Por lo que existe una unicá asignación válida, que es no hacer nada.</li>
</ul>
<h3>Consideraciones</h3>
<ul>
<li>\(1 \leq n \leq 10^5\). </li>
<li>\(0 \leq q \leq 10^5\).</li>
<li>\(1 \leq k \leq 10^6\).</li>
<li>\(a_i = -1\) o \(1 \leq a_i \leq 10^6\) \((1 \leq i \leq n)\).</li>
</ul>
<h3>Subtareas</h3>
<ul>
<li>Subtarea 1 <strong>(15 puntos)</strong>: \(k = 1\)</li>
<li>Subtarea 2 <strong>(15 puntos)</strong>: \(k = 10^6\)</li>
<li>Subtarea 3 <strong>(15 puntos)</strong>: \(Q,N \leq 10^3\)</li>
<li>Subtarea 4 <strong>(25 puntos)</strong>: Ninguna actualización modificará a un valor del arreglo distinto de \(-1\). Además, un valor positivo ya existente nunca se volverá \(-1\) con una actualización.</li>
<li>Subtarea 5 <strong>(30 puntos)</strong>: Sin restricciones adicionales.</li>
</ul>
</div>

                    <hr>
            </div>
