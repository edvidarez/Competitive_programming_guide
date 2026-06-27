Hay N olímpicos en un entrenamiento, y como es natural, juegan asesino en su tiempo libre. El día de hoy decidieron usar la siguiente variante, que tiene 4 roles:

* **Honesto:** Una persona que siempre dice la verdad.
* **Mentiroso:** Una persona que siempre dice la mentira.
* **Impostor tipo 1:** Una persona que el resto de jugadores piensa que es honesta, pero actúa como mentiroso.
* **Impostor tipo 2:** Una persona que el resto de jugadores piensa que es mentirosa, pero actúa como honesto.

Además en esta variante, siempre existe exactamente un impostor, pero puede ser de tipo 1 o de tipo 2.

Llegaste tarde a la noche de juegos, por lo que todos los roles estaban asignados. Entonces decidieron ponerte un reto.

Todos los jugadores actuarán de acuerdo a su rol. Puedes preguntarle al olímpico $i$ si piensa que el olímpico $j$ es honesto (con $i \neq j$). En la siguiente tabla se ilustran las respuestas de acuerdo al rol.

| | Honesto| Mentiroso | Impostor tipo 1 | Impostor tipo 2 |
| :--------: | :-------: | :-------: | :-------: | :-------: |
| Honesto| Sí | No | Sí | No |
| Mentiroso| No | Sí | No | Sí |
| Impostor tipo 1    | No  | Sí | --- | --- |
| Impostor tipo 2    | Sí   | No | --- | --- |

<p style="text-align:center;">La respuesta de la celda en la fila $a$ y la columna $b$ es el resultado de hacer una pregunta cuando la persona $i$ tiene el rol $a$ y la persona $j$ tiene el rol $b$. Por ejemplo, el “No” en en la esquina superior derecha, le corresponde a la fila “Honesto” y la columna “Impostor tipo 2”.
Por lo que es la respuesta cuando $i$ es honesto y $j$ es un Impostor de tipo 2.</p>

Tú no sabes qué rol tiene cada olímpico, y además, no le puedes preguntar a un olímpico si piensa que él mismo es honesto.

Debes encontrar al impostor en la menor cantidad de preguntas posibles.

Formalmente, sea $f(n)$ la máxima cantidad de preguntas que hace la estrategia óptima en el peor caso, para $n$ olímpicos, obtendrás el 100% de los puntos si logras encontrar al impostor en a lo más $f(n)$ preguntas.

#Detalles de implementación

Deberás implementar la siguiente función:

    int asesino(int N);

Esta función recibe un parámetro:

* Un entero $N$, la cantidad de olímpicos jugando el juego.

Y regresa un entero, el índice del impostor. los olímpicos están indexados a partir del 1. Si el valor que regresas es menor que 1 o mayor a $N$, recibirás un veredicto de respuesta incorrecta.

En tu código, podrás invocar la siguiente función para hacer una pregunta:

    int pregunta(int i, int j);

La función recibe los siguientes parámetros:

* Un entero $i$, el olímpico al que le haces la pregunta.
* Un entero $j$, el olímpico sobre el cuál preguntas

Cuando llames esta función, los valores tienen que ser mayores o iguales a 1 y menores o iguales a $N$, y el valor de $i$ debe ser distinto al de $j$. De lo contrario, recibirás un veredicto de respuesta incorrecta.

La función regresa un entero, un 1 si la respuesta fue sí, y un 0 en caso contrario.

El evaluador llamará la función *asesino()* **múltiples veces por caso**, por lo que recuerda limpiar variables globales en caso de usarlas.

El evaluador es **adaptativo**, esto significa que los roles de los jugadores no están fijos al inicio del proceso y pueden cambiar dependiendo de tus preguntas. Sin embargo, se garantiza que siempre existe una forma de asignar los roles que es consistente con todas las preguntas previas.

#Ejemplo

* El evaluador corre tu programa, y llama la función: *asesino(3)*
* Digamos que el primer olímpico es un impostor de tipo 1, el segundo es Honesto y el tercero es Mentiroso. Estas son todas las posibles llamadas que puede hacer tu código en este caso:

|Parámetros | Proceso| Valor que regresa la función |
| :--------: | :-------: | :-------: |
| *pregunta(1,2)*| Le preguntas al olímpico 1 sobre el olímpico 2| 0|
| *pregunta(1,3)*| Le preguntas al olímpico 1 sobre el olímpico 3|1|
| *pregunta(2,1)*| Le preguntas al olímpico 2 sobre el olímpico 1|1 |
| *pregunta(2,3)*| Le preguntas al olímpico 2 sobre el olímpico 3|0 |
| *pregunta(3,1)*| Le preguntas al olímpico 3 sobre el olímpico 1|0 |
| *pregunta(3,2)*| Le preguntas al olímpico 3 sobre el olímpico 2|0 |

* Después de hacer algunas preguntas, la función *asesino()* debe responder con el valor 1, la posición del impostor en este caso.

#Límites

* $3 \leq N \leq 10^5$.
* El evaluador llamará a lo más 10,000 veces la función *asesino()*, y la suma de $N$ sobre todas las llamadas por caso no excede $10^5$.
* Los olímpicos están indexados a partir del 1.
* Cada olímpico tiene un rol, pero no se garantiza que siempre habrá alguien con el rol de Honesto o Mentiroso. Solo se garantiza que existe exactamente un impostor. Puede ser de tipo 1 o de tipo 2.

#Subtareas

* Subtarea 1 (4 puntos): $N = 3$, hay 1 impostor de tipo 1, una persona honesta y un mentiroso. Encuentra al impostor en a lo más 6 preguntas.
* Subtarea 2 (6 puntos): Encuentra el impostor con a lo más $N(N − 1)$ preguntas.
* Subtarea 3 (12 puntos): Encuentra el impostor en a lo más 2N preguntas.
* Subtarea 4 (15 puntos): $N \leq 4$, Encuentra el impostor con la mínima cantidad de preguntas que hace la estrategia óptima.
* Subtarea 5 (18 puntos): Encuentra el impostor en a lo más $N + 29$ preguntas.
* Subtarea 6 (20 puntos): Encuentra el impostor en a lo más $N + 1$ preguntas.
* Subtarea 7 (25 puntos): Sin restricciones adicionales.

{{libinteractive:download}}
