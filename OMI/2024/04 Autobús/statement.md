Hay *n* familias que están viajando en un autobús a Pénjamo, Guanajuato, para ver el maratón más grande de “correr con una gallina”. Cada familia tiene $a_i$ integrantes. El autobús tiene 2 columnas y $f$ filas.
<br /> <br />
Una persona está contenta si:

* alguien de su familia se sienta en la misma fila,
* o no hay nadie más sentado en su misma fila.

Solamente hay un autobús. **Se garantiza que todas las personas caben en el autobús**. Encuentra el **número máximo de personas felices**, si asignas los lugares de manera óptima. **Todas las personas deben tener un lugar en el autobús**.

#Entrada

La primera línea consiste de un entero $n$ y un entero $f$. El número de familias y la cantidad de filas en el autobús. La segunda línea consiste de $n$ enteros $a_1, a_2, ..., a_n$, la
cantidad de integrantes de cada familia.

#Salida

Un solo entero, el máximo número de personas felices que puedes obtener, asignando óptimamente los lugares del autobús a las personas.

#Ejemplos

||input
3 3
2 3 1
||output
4
||input
3 3
2 2 2
||output
6
||input
4 5
1 1 2 2
||output
6
||input
4 5
3 1 1 3
||output
6
||end

En el primer ejemplo, los dos integrantes de la primera familia se pueden sentar juntos en la primera fila, dos de la segunda familia se pueden sentar juntos en la segunda fila. El que falta de la segunda familia se puede sentar en la tercera fila junto al único miembro de la tercera familia. Esta asignación de asientos se muestra en la imagen de abajo, donde las 4 personas felices están coloreadas con azul claro.

<img src="https://i.imgur.com/776IxH0.jpeg" />

En el segundo ejemplo, una posible asignación de asientos con 6 personas felices se muestra en la imagen de abajo.

<img src="https://i.imgur.com/FQjTQG3.jpeg" />

En el tercer ejemplo, una posible asignación de asientos con 6 personas felices se muestra en la imagen de abajo.

<img src="https://i.imgur.com/6XpEH3R.jpeg" />

#Consideraciones

* $1 \leq n \leq 100$.
* Para todo $i$ con $1 \leq i \leq n$, se cumple que $1 \leq a_i \leq 10$
* $1 \leq f \leq 500$
* Se garantiza que todas las personas caben en el autobús. Formalmente se garantiza que $\sum_{i=1}^n a_i \leq 2f$
* Solamente hay un autobús y **todas** las personas deben tener un lugar en el autobús/

#Subtareas

* Subtarea 1 (10 puntos); Se garantiza que $n = 1$, es decir, solo hay una familia.
* Subtarea 2 (20 puntos): Se garantiza que para todo $i$ con $1 \leq i \leq n$, se cumple que $a_i$ es par, es decir, todas las familias tienen una cantidad par de integrantes.
* Subtarea 3 (30 puntos): Se garantiza que $n = 2$, es decir, solo hay dos familias.
* Subtarea 4 (40 puntos): Sin restricciones adicionales.
