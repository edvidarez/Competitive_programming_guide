La industria de los pastes en Pachuca demanda una gran cantidad de ingredientes. En total se necesitan $N$ ingredientes
distintos de origen agrícola. En los alrededores de Pachuca hay $N$ granjas, cada una de estas granjas planta uno de los
ingredientes.

Las granjas cambian cada año de ingrediente para optimizar el uso del suelo. Para asegurarse de que ningún ingrediente
quedará desabastecido, las granjas se organizaron de la siguiente forma:

* Se numeraron las granjas del $1$ al $N$.
* Llenaron el arreglo $A$ con los números del $1$ al $N$ ordenados de manera aleatoria.
* Cada cambio de año la granja $i$ plantará el ingrediente que plantó en el año anterior la granja $A[i]$.

#Problema

Escribe un programa que, recibiendo el número $N$ de granjas/ingredientes y el arreglo $A$, determine ¿cuántos años pasarán
antes de que todas las granjas vuelvan a plantar exactamente los mismos ingredientes que plantaron este año?

#Entrada

Tu programa debe leer del teclado los siguientes datos:

* La primera línea contiene el entero $N$, la cantidad de granjas/ingredientes.
* En la segunda línea $N$ números enteros separados por un espacio que representan los valores del arreglo $A$.

#Salida

Tu programa debe escribir en la pantalla un único número que indica la cantidad de años que pasarán antes de que todas las
granjas vuelvan a plantar exactamente los mismos ingredientes que plantaron este año.

#Restricciones

$1 \le N \le 50,000$ Cantidad de granjas/ingredientes

#Ejemplo


||input
5
3 4 5 1 2
||output
5
||description
Este año la granja 1 plantó el ingrediente 1, la granja 2 el ingrediente 2,
la 3 el ingrediente 3, la 4 el 4 y la 5 el 5.

Para el segundo año, de acuerdo con el arreglo, la granja 1 plantará
lo que el año anterior había plantado la granja 3, ya que $A[1]=3$, la
granja 2 plantará lo que había plantado la granja 4, etc.

El segundo año entonces las granjas plantaran: 3, 4, 5, 1, 2.

El tercer año las granjas plantarán: 5, 1, 2, 3, 4.

El cuarto año plantarán: 2, 3, 4, 5, 1.

El quinto: 4, 5, 1, 2, 3.

El sexto: 1, 2, 3, 4, 5 **(Exactamente lo mismo que el primer año)**.

**Por lo tanto, al pasar 5 años las granjas volverán a plantar
exactamente los mismos ingredientes que el primer año.**
||end

#Evaluación

* Para un conjunto de casos **sin agrupar** con valor de $33$ puntos el número máximo de años que pasarán es de 1,000.
* Para otro conjunto de casos **agrupados** con valor de $31$ puntos el número máximo de años que pasarán es de 100,000,000.
* Para un grupo de casos **agrupados** con valor de $36$ puntos el número máximo de años que pasarán cabe en un entero signado de 64 bits.

-------------------------------------------------------

> Envié 100 problemas de a 500... ¿'on 'tan?
