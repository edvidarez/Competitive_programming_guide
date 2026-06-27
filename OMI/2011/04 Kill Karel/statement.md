# Descripción

¡Karel ha hecho enojar a la temida asesina conocida como La Mamba Negra! A causa de ello, la Mamba, le ha aplicado a Karel el golpe secreto de los $4N$ pasos. Este golpe ocasionará que el corazón de Karel explote si llega a avanzar $4N$ veces. Por suerte
para Karel, existe un antídoto para dicho golpe.

Después de darle el golpe, la Mamba dejó a Karel en un cuarto cerrado, junto a una de las paredes del mismo. Karel sabe que ocultó en la pared del cuarto hay un frasco con el antídoto. Más aún, sabe que si avanza manteniéndose siempre junto a la pared podrá encontrar el frasco a una distancia de $N$ pasos, sin embargo no sabe hacia qué lado debe buscar.

# Problema

Ayuda a Karel a encontrar el antídoto avanzando menos de $4N$ veces.

El cuarto está totalmente delimitado por paredes y la posición donde se encuentra el frasco está representada por una casilla con 1 zumbador. Karel deberá apagarse en cuanto encuentre el antídoto.

# Consideraciones

- Karel inicia junto a una de las paredes del cuarto en alguna dirección.
- Karel lleva 0 zumbadores en la mochila.
- El cuarto no necesariamente es rectangular.
- Karel **no conoce** el número $N$.
- Para obtener puntos en este problema, Karel deberá encontrar el frasco y  apagarse antes de haber avanzado $4N$ veces. **NOTA:** El número $N$ varía con cada caso de prueba, al momento de ser evaluado, se verificará que para cada caso, tu ejecución no avance más veces de las permitidas. **ES IMPORTANTE
QUE ENTIENDAS QUE NO BASTA ENCONTRAR EL FRASCO, TIENES QUE ENCONTRARLO AVANZANDO MENOS DE 4N VECES.**
- No importa la orientación final de Karel, únicamente su posición.
- En este problema cada caso de prueba constará de 2 mundos los cuales son un reflejo horizontal uno del otro, para obtener los puntos, tu programa deberá
resolver correctamente ambos.


# Ejemplo

Mundo inicial y final (1)

![Mundo inicial y final 1](mundoinicialfinal1.png)

La figura a) muestra a Karel en su posición de inicio junto a la pared del cuarto. Para este mundo $N=2$ ya que el frasco está a 2 avances. La figura b) muestra a Karel después de detenerse al encontrar el frasco.

Mundo inicial y final (2)

![Mundo inicial y final 2](mundoinicialfinal2.png)

Las figuras c) y d) muestran la misma entrada y salida, pero esta vez con el mundo reflejado.

# Información Util

**Durante el examen nacional de la OMI 2011, se hicieron ajustes al valor de $4N$, en algunos momentos se dijo que el valor sería $9N$ y en otros $12N$. Es por esto, que en los casos que se estan usando en este problema, el 50% tiene el valor de $9N$ y el otro 50% tiene el valor de $12N$.**
