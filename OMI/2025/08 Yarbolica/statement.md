<div class="content-description screen">
        <div><p>Yarbolica es una ciudad única en Jalisco conocida porque, entre cada par de casas, existe un único camino simple. Por estas propiedades, Santiago se dió cuenta de que la estructura de la ciudad puede ser representada como un <strong>árbol</strong>. Debido a esto, recientemente decidieron renombrarla de Yahualica a Y<strong>arbol</strong>ica. Entre sus habitantes más célebres está Ma Inés - la querida maestra de matemáticas del pueblo. Ella tiene \(n\) amigas numeradas del \(1\) al \(n\) que viven en las casas \(1, 2, ... , n\) de Yarbolica respectivamente. Hay \(n - 1\) caminos directos bidireccionales que conectan entre esas \(n\) casas.</p>
<p>La maestra y sus amigas, son aficionadas a las telenovelas turcas, y actualmente hay \(k\) novelas transmitiéndose en Yarbolica, numeradas de la \(1\) a la \(k\). La amiga \(j\) ha visto algunas de las \(k\) novelas, representemos esas novelas con el conjuto \(C_j\). Digamos que la suma total de novelas turcas totales que ha visto alguna de las amigas es \(s\).</p>
<p>Ma Inés ya cumplió 80 y ahora más que nunca le encantaría pasar su tiempo con sus amigas. En el \(i-ésimo\) de los siguientes \(q\) días, Ma Inés va a hacer una reunión con todas las amigas que vivan en casas ubicadas en el camino simple entre las casas \(a_i\) y \(b_i\), incluyendo a las casas \(a_i\) y \(b_i\) (recuerda que en Yarbolica hay un único camino simple entre cada par de casas).</p>
<p>Como no le gusta excluir a ninguna amiga, en cada reunión solo van a hablar de las novelas turcas que <strong>todas</strong> las amigas invitadas vean. Es decir, si Ma Inés hace una reunión con un conjunto \(D\) de amigas, solo van a hablar de las novelas que pertenezcan a la intersección de \(C_d\) (para todo \(d\) en \(D\)).</p>
<p>Determina para todos los días \(i\) \((1 \leq i \leq q)\) la cantidad de novelas turcas que se hablarán en la reunión \(i\).</p>
<h3>Entrada</h3>
<ul>
<li>En la primera línea un único entero \(t\) - la cantidad de casos de prueba.</li>
<li>En la primera línea de cada caso de prueba, \(4\) enteros \(n, k, s, q\) - que representan respectivamente las cantidades de: amigas de Ma Inés, novelas turcas, \(s\) y reuniones en total.</li>
<li>En la \(i-ésima\) de las siguientes \(n - 1\) líneas, \(2\) enteros \(u_i\) \(v_i\) - que representan que en Yarbolica hay un camino directo bidireccional entre las casas \(u_i\) y \(v_i\).</li>
<li>En la \(i-ésima\) de las siguientes \(s\) líneas, 2 enteros \(x_i\) \(c_i\) - que representa que la amiga \(x_i\) ve la novela turca \(c_i\), o dicho de otro modo: \(c_i \in C_xi\) . En la \(i-ésima\) de las siguientes \(q\) líneas, \(2\) enteros \(a_i\) \(b_i\) - los extremos del camino que define a las amigas invitadas a la reunión \(i\).</li>
</ul>
<h3>Salida</h3>
<p>Para cada uno de los \(t\) casos de prueba, imprime una línea de enteros separados por espacios: la cantidad de novelas turcas que se hablarán durante la reunión \(1, 2, ... , q\).</p>
<h3>Ejemplo</h3>
<h4>Entrada</h4>

<pre><code>2
4 3 6 4
4 2
2 1
3 2
2 3
2 2
2 1
3 1
3 2
4 2
4 1
3 4
2 3
2 2
2 7 13 2
1 2
1 2
1 3
2 1
2 2
2 3
2 4
2 5
2 6
2 7
1 4
1 5
1 6
1 7
2 1
2 2</code></pre>
<h4>Salida</h4>

<pre><code>0 1 2 3
6 7</code></pre>
<h3>Consideraciones</h3>
<p>Sea \(N\) la suma de \(n\) sobre todos los casos de prueba. Similarmente sean \(K, S, Q\) las sumas de \(k, s, q\) respectivamente sobre todos los casos de prueba.</p>
<ul>
<li>\(1 \leq t \leq 10^4\).</li>
<li>\(1 \leq n, k, s, q\).</li>
<li>\(N,K, S, Q \leq 3 × 10^5\).</li>
<li>\(1 \leq u_i , v_i \leq n\) \((1 \leq i \leq n - 1)\).</li>
<li>\(1 \leq x_i \leq n\), \(1 \leq c_i \leq k\) \((1 \leq i \leq s)\).</li>
<li>\(1 \leq a_i , b_ i \leq n\) \((1 \leq i \leq q)\).</li>
</ul>
<h3>Subtareas</h3>
<ul>
<li>Subtarea 1 <strong>(7 puntos)</strong>: \(N,K, Q \leq 250\), \(S \leq 10^4\).</li>
<li>Subtarea 2 <strong>(8 puntos)</strong>: \(k = 1\).</li>
<li>Subtarea 3 <strong>(8 puntos)</strong>: \(k \leq 30, u_i = i, v_i = i+1\) y \(a_j \leq b_j\) \((1 \leq i \leq n-1 , 1 \leq j \leq q)\). Es decir, el árbol es una línea.</li>
<li>Subtarea 4 <strong>(6 puntos)</strong>: \(k \leq 30\).</li>
<li>Subtarea 5 <strong>(16 puntos)</strong>: \(K, Q \leq 5000\).</li>
<li>Subtarea 6 <strong>(16 puntos)</strong>: \(N,K, S \leq 5000\).</li>
<li>Subtarea 7 <strong>(16 puntos)</strong>: \(u_i = i, v_i = i + 1\) y \(a_j \leq b_j\) \((1 \leq i \leq n - 1 , 1 \leq j \leq q)\). Es decir, el árbol es una línea.</li>
<li>Subtarea 8 <strong>(23 puntos)</strong>: Sin restricciones adicionales.</li>
</ul>
</div>

                    <hr>
            </div>
