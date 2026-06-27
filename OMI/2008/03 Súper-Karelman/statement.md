# Problema

¿Has notado que Karel tiene complejo de superhéroe? ¿A quién no le ha pasado que al ejecutar un programa de Karel aparezca un letrero que diga "¡Karel intentó atravesar una pared!"? Y por si fuera poco, gracias al complejo de Karel, te quitan los puntos de ese caso de prueba.

En esta OMI queremos proporcionarle la ayuda psicológica... ehmm... algorítmica, que Karel necesita para que pueda jugar a ser Súper-Karelman sin matarse en el intento.

Ayuda a Karel a atravesar las paredes que se le pongan enfrente utilizando las ventanas que existan, y dejar un camino de zumbadores, empezando en la posición inicial y terminando al cruzar la última pared, que sirva de rastro para poder atravesar cada vez que lo desee.

# Consideraciones

- Karel inicia en algún lugar del mundo, detrás de la primera pared a atravesar, mirando hacia el este. ¡Ojo!, que podría iniciar justo donde haya alguna ventana.
- Karel tendrá suficientes zumbadores en su mochila para trazar un camino que atraviese todas las paredes.
- Las paredes a atravesar son todas verticales del mismo largo (mínimo dos filas) y están limitadas en sus extremos por dos paredes horizontales.
- Las ventanas en las paredes siempre tendrán un tamaño de 1.
- Una pared puede tener más de una ventana, sin embargo, cualesquiera dos ventanas de una misma pared deben tener una separación mímina de 1.
- Las paredes que debes atravesar estarán una tras otra, separadas siempre por una distancia de una columna.
- De haber más de una solución con los requisitos anteriores, cualquiera será considerada correcta.
- No importa la posición ni la orientación final de Karel.
- Karel debe dejar un camino de zumbadores desde su posición de inicio hasta la posición final, inmediatamente después de haber cruzado la última pared.

# Ejemplos

## Entrada

![Mundo de entrada](entrada.png)

## Salida

![Mundo de salida](salida.png)

