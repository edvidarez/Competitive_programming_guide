# Problema

Karel acaba de descubrir los números primos y está muy emocionado, tanto que ha decidido dedicar lo que resta del día a seguir caminos formados únicamente por montones que contengan un número primo de zumbadores.

Un número primo es aquel que sólo puede ser dividido de manera entera (sin que quede residuo) entre él mismo y entre el número $1$. Por ejemplo: $2$, $3$, $5$ y $7$ son números primos. **Nota**: El número $1$ NO ES UN NÚMERO PRIMO.

Karel estará en un mundo que contiene un cuadrado de zumbadores, que puede tener un tamaño de hasta $15x15$. Karel deberá seguir el camino formado por las casillas que contengan un número primo de zumbadores, y apagarse cuando llegue al final del mismo.

El final del camino es cuando ya no hay más primos que Karel pueda seguir.

# Datos

- La esquina inferior izquierda del cuadrado de zumbadores inicia siempre en la coordenada $(1,1)$.
- El cuadrado de zumbadores tendrá siempre un tamaño mínimo de $3x3$ y máximo de $15x15$.
- Karel lleva un infinito de zumbadores en la mochila.
- Karel puede iniciar en cualquier lugar dentro del cuadrado, con cualquier orientación.
- Karel iniciará siempre en una posición dentro del cuadrado que contenga un número primo de zumbadores.
- No hay paredes dentro del mundo.
- Sólo existirá un camino de primos dentro del cuadrado, que inicia en la posición donde empieza Karel. El camino no tiene bifurcaciones ni ciclos.
- Las casillas dentro del cuadrado tendrán una cantidad de zumbadores entre 1 y 99.
- Para obtener puntos en este problema, **SÓLO IMPORTA LA POSICIÓN FINAL DE KAREL**. No importa la orientación final de Karel ni la forma en la que queden los zumbadores al terminar.

# Ejemplos

## Entrada

![Mundo de entrada](camino.in.png)

## Salida

![Mundo de salida](camino.out.png)

