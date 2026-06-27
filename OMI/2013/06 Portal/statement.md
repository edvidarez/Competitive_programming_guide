Probablemente hayas jugado Portal, si no lo has hecho, Portal es un videojuego en el que el personaje principal recorre diversos laberintos para llegar a su objetivo: un pastel.
El personaje cuenta con un arma capaz de disparar portales, es decir, si se apunta con el arma a una pared (no importa si la pared está retirada, basta con que sea visible desde donde se está) se abre un portal en esa pared. Después de disparar, el jugador puede moverse y el portal seguirá abierto. El arma puede mantener abierto solo un portal a la vez, de modo que si se utiliza el arma para disparar un nuevo portal, el primero se cerrará en el momento que se abre el nuevo.
El jugador cuenta con 2 armas, una dispara portales azules y la otra, naranjas. Es sólo usando ambas que los portales son de utilidad. Los portales funcionan así:

* Cuando se dispara un portal a una pared, al llegar a esta pared (el portal puede dispararse desde lejos), el jugador puede entrar al portal.
* Si se entra al portal azul, se sale por el lugar donde esté el portal naranja. Si no hay portal naranja abierto, entonces el portal azul no sirve y no tiene ningún efecto tratar de entrar en él.
* Viceversa, si se entra al portal naranja, se sale por donde esté el portal azul. Igualmente, si no hay portal azul, entrar al portal naranja no causa ningún efecto.

Para este problema recibirás el mapa de un mundo representado por una cuadrícula rectangular de $M$ filas $\times$ $N$ columnas, el mapa marca los cuadros por los que se puede avanzar y los cuadros que son pared, además marca la posición inicial del jugador $(x_j,y_j)$ y la posición del pastel $(x_p,y_p)$. Como jugador puedes dar un paso, siempre y cuando no exista una pared que te lo impida, en las direcciones norte, sur, este u oeste. Además puedes disparar cualquiera de los portales, azul o naranja, igualmente en dirección norte, sur, este u oeste. En caso de disparar un portal éste avanzará hasta la próxima pared en esa dirección. El mundo está rodeado por paredes, de modo que al disparar siempre habrá una pared en donde se abra el portal.

# Problema
Escribe un programa que recibiendo el mapa, las coordenadas de inicio del jugador y las coordenadas del pastel, determine cuál es el menor número de pasos que tiene que dar el jugador para llegar hasta el pastel o que imprima ‘THE CAKE IS A LIE’ (en mayúsculas) si no hay ninguna manera de hacerlo.

# Entrada
Tu programa debe leer del teclado los siguientes datos:

* La primera línea contiene dos enteros $M$, $N$, la cantidad de filas y de columnas en el mapa.
* Las siguientes $M$ líneas tienen $N$ caracteres que representan el mapa, cada uno de estos caracteres puede tener los siguientes valores:
	* ‘.’ (punto): Es un cuadro por donde se puede caminar.
	* ‘#’ (gato): Indica un cuadro por donde no se puede caminar (pared).
	* 'O’ (o mayúscula): Indica la posición donde inicia el jugador.
	* 'X’ (x mayúscula): Indica la posición donde está el pastel.

# Salida
Tu programa debe escribir en la pantalla un único número que indica la cantidad mínima de pasos necesarios para que el jugador llegue al pastel.

# Restricciones
$1 \le M,N \le 1,250$

# Ejemplo

||input
    10 10
    ##########
    ###..##O.#
    #....##..#
    #........#
    #........#
    #...X....#
    #........#
    #........#
    #..#.....#
    ##########
||output
5
||description
Para llegar en 5 pasos el jugador tiene que hacer lo siguiente (para que los entiendas sigue los pasos en el mapa de la imagen):

* Disparar el portal azul hacia el sur.
* Disparar el portal naranja hacia el norte.
* Avanzar hacia el norte para entrar al portal naranja y salga por la parte de abajo del mapa. Hasta aquí ha dado 1 paso.
* Disparar el portal naranja hacia el oeste.
* Avanzar hacia el sur para entrar al portal azul y salir por el naranja abajo del pastel. Hasta aquí llevas 2 pasos.
* Avanzar 3 pasos al norte para llegar al pastel. En total se dieron 5 pasos.

![](portal.gif)

||end

# Evaluación

* Para un grupo de casos con valor de $21$ puntos $M,N \le 15$ y el camino óptimo al pastel no requiere del uso de portales.
* Para un grupo de casos con valor de $34$ puntos $M,N \le 15$ y el camino óptimo al pastel requiere del uso de portales.
* Para un grupo de casos con valor de $23$ puntos $M,N \le 50$ y el camino óptimo al pastel requiere del uso de portales.
* Para un grupo de casos con valor de $22$ puntos $M,N \le 1,250$ y el camino óptimo al pastel requiere del uso de portales.
