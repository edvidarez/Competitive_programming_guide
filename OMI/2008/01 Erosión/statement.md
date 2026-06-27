# Descripción
<p>Las montañas del mundo de Karel son columnas de beepers apilados, y como cualquier formación geológica, están sujetas a un proceso de erosión. La erosión se da cuando una montaña alta deja caer el beeper en su cima hacia otra montaña contigua de menor altura.</p>
<p>Las reglas siguientes de erosión siempre son válidas:</p>
<ul>
<li>Sólo se da entre MONTAÑAS CONTIGUAS, es decir, que no exista NINGUNA SEPARACIÓN entre ellas</li>
<li>Sólo se da si la DIFERENCIA DE ALTURAS entre ambas montañas es AL MENOS DE 2 beepers</li>
<li>Sólo sucede de IZQUIERDA A DERECHA</li>
<li>En cada era geológica erosiona MÁXIMO UN BEEPER por montaña</li>
<li>Durante una era geológica, TODAS LAS MONTAÑAS erosionan AL MISMO TIEMPO</li>
</ul>

# Problema
Dada la formación de una cordillera montañosa, ayuda a Karel a determinar cómo se verá dentro de un cierto número de eras geológicas.

# Consideraciones
<ul>
<li>Karel inicia en la posición (1,1) mirando hacia el norte</li>
<li>No hay paredes dentro del mundo</li>
<li>Karel debe de determinar el estado final de la cordillera cuando hayan pasado un número de eras geológicas igual a la camtidad de beepers que lleva en la mochila</li>
<li>EL NÚMERO DE ERAS GEOLÓGICAS SERÁ A LO MÁS DE 50</li>
<li>Las montañas tinene su base en la fila 1 y pueden tener una altura máxima de 50</li>
<li>La cordillera comienza a partir de la columna 2</li>
<li>Si una columna no tiene beepers, no se considera montaña, es decir, no hay montañas con altura inicial 0</li>
<li>Puede haber columnas sin montañas dentro de la cordillera</li>
<li>No importa la posición ni la orientación final de Karel así como la cantidad de zumbadores que tenga en su mochila, el mundo resultado debe representar EXACTAMENTE el estado de la cordillera después de que hayan pasado las eras geológicas. No debes dejar NINGÚN ZUMBADOR además de los de la cordillera</li>
</ul>

# Entrada ejemplo
![Ejemplo de entrada](erosion_entrada.jpg)
# Después de una 1ª era geológica
![Ejemplo después de 1 era geológica](erosion_1_era.jpg)
# Salida ejemplo
![Ejemplo de entrada](erosion_salida.jpg)
