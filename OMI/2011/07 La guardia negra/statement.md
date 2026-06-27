# Descripción

Según *la canción del fuego y el hielo*, la guardia de los centinelas negros ha defendido al reino de Westeros de las amenazas del norte durante los últimos 8,000 años. A últimas fechas un gran número de huestes enemigas se ha venido concentrando en la frontera norte de Westeros. El comandante de la guardia, Lord Snow, ha mandado llamar por ti para que le ayudes a planear la defensa.

La guardia tiene representado el campamento enemigo como una cuadrícula de $M$ filas por $N$ columnas, en cada casilla de la cuadrícula hay un número $s_{i,j}$ que representa la cantidad de soldados enemigos en esa casilla.

La guardia cuenta con una catapulta capaz de lanzar un proyectil explosivo a cualquier lugar de esta cuadrícula. Al explotar, el proyectil eliminará a todos los soldados enemigos que se encuentren a una distancia menor o igual a un número $d_i$ que depende del proyectil en cuestión. La distancia entre dos casillas se define como la suma del valor absoluto de la diferencia de sus columnas mas el valor absoluto de la diferencia de sus filas.

El comandante de la guardia quiere que desarrolles un programa para calcular la cantidad de soldados que eliminaría un proyectil específico si fuera lanzado en una cierta casilla.

# Problema

Escribe un programa que dada la cuadrícula del campamento, el número de soldados en cada casilla, el número de proyectiles, la distancia de alcance de cada uno y el lugar donde quieres lanzarlo, calcule el número de enemigos que serán eliminados con cada proyectil.

# Entrada

Tu programa debe leer del teclado la siguiente información:

- En la primer línea los números $M$ y $N$ que representan el número de filas y columnas del campamento.
- En cada una de las siguientes $M$ líneas hay $N$ números enteros ($s_{i,j}$) separados por un espacio que representan los soldados en cada casilla del campamento.
- En la siguiente línea el número $P$ de proyectiles que tiene la guardia.
- En las últimas $P$ líneas hay 3 enteros separados por espacios en cada una que representan la fila y columna donde se lanzará un proyectil y la distancia de alcance del mismo.

Tanto las filas como las columnas inician numeradas a partir del 0 y hasta $M-1$ y $N-1$ respectivamente. La fila 0 es la fila superior y la columna 0 es la columna hasta la izquierda.

Puedes estar seguro de que los proyectiles serán lanzados de tal forma que su alcance no exceda el campamento, es decir, ninguna explosión llegará a una casilla que este fuera de la cuadrícula.


# Salida

Tu programa deberá escribir a la pantalla $P$ líneas con un número cada una. La **$i$-ésima** línea debe contener la cantidad de enemigos que serían eliminados al lanzar el proyectil $i$.

# Ejemplo

||input
5 5
1 2 3 4 5
5 4 3 2 1
1 1 1 1 1
2 3 4 3 0
7 8 9 6 5
3
1 0 0
2 2 2
3 1 1
||output
5
36
18
||description
![Imagen de ejemplo](imagenejemplo.png)

La **imagen izquierda** muestra los primeros 2 proyectiles.

El primer proyectil, lanzado en la fila 1, columna 0 y con alcance 0, sólo elimina a los soldados de esa casilla.

El proyectil 2 se lanza en la casilla 2,2 y elimina todos los soldados a distancia menor o
igual que 2.

La **imagen derecha** muestra el tercer proyectil.

**NOTA:** Observa que los proyectiles no se lanzan
realmente, de modo que al calcular la cantidad de
enemigos que podrías eliminar, debes considerar todas las casillas sin importar si se intersectan con el alcance de algún proyectil previo.
||end

# Límites

* $1 \le M, N \le 10^3$
* $0 \le s_{i,j} \le 10^9$
* $1 \le P \le 10^5$
* $0 \le di \le 500$

* Para este problema los casos de prueba se agruparán en 3 grupos distintos. Para obtener los puntos de un grupo es necesario que tu programa resuelva correctamente TODOS los casos de ese grupo, de otra forma obtendrás 0 puntos por ese grupo aun cuando hayas resuelto correctamente algunos de los casos.

* **RESTRICCIONES ESPECIALES PARA EL GRUPO 1 (Valor del grupo, 25 puntos)** : $1 \le M, N \le 100$, $1 \le P \le 100$, $0 \le s_{i,j} \le 10^5$ y $0 \le di \le 50$.

* **RESTRICCIONES ESPECIALES PARA EL GRUPO 2 (Valor del grupo, 50 puntos)**: $1 \le M, N \le 10^3$, $1 \le P \le 10^3$, $0 \le s_{i,j} \le 10^6$ y $0 \le di \le 500$.

* **RESTRICCIONES ESPECIALES PARA EL GRUPO 3 (Valor del grupo, 25 puntos)**: Las restricciones para el grupo 3 son las especificadas en la primera sección de límites.
