IOI 2024, la selección mexicana acaba de llegar al aeropuerto del Cairo. Como suele suceder, coordinar el transporte de 800 personas es tardado, hoy no fue la excepción.
<br /> <br />
Después de 7 horas de tránsito, los participantes llegaron al hotel sede del evento, y como es fisiológicamente esperado, un gran número de ellos requiere usar los mingitorios del único baño en el hotel.
<br /> <br />
Como siempre, José Andrés tardó tanto en llegar a la fila que tuvo que formarse al final, por lo que decide entretenerse simulando mentalmente la configuración de uso de los mingitorios.
<br /> <br />
José Andrés sabe que dada una configuración de mingitorios el siguiente usuario tomará la posición definida por el siguiente algoritmo:

* El usuario tomará la posición cuya distancia sea lo máximo al mingitorio más cercano ocupado.
* En caso de existir más de una posición con la misma distancia, elegirá la que pertenezca al rango consecutivo de mingitorios libres más grande.
* Y en caso de existir qué más de una posición con las mismas características, se elige la posición más a la izquierda (ya que la puerta del baño está a la derecha).

<img src="https://i.imgur.com/T1hj44T.jpeg" />

(Revisa la sección de ejemplos para una explicación detallada)

José Andrés se pregunta cómo se verá la configuración final de los mingitorios después de que todos los olímpicos pasen. Sabemos que hay 2 tipos de evento:

* Un olímpico llega al baño y toma la **única** posición válida para la configuración actual de mingitorios.
* Un olímpico que viste entrar previamente, sale del baño.

¡Ayuda a José Andrés a resolver este problema!

#Problema

Dados $N$ mingitorios y los $Q$ eventos, determina qué mingitorios estarán ocupados después de los $Q$ eventos.

#Entrada

* En la primera línea dos enteros separados por un espacio $N$ y $Q$. La cantidad de mingitorios y de eventos.
* Las siguientes $Q$ líneas describen un evento cada una. Los eventos pueden ser de dos tipos:
   * $1$, un número $1$ indica que llegó un olímpico.
   * $0$ $t$, un número $0$ seguido de un número $t$ indica que sale el olímpico que llegó en el tiempo $t$.

**Los eventos se numeran empezando desde $0$ hasta $Q-1$**

**Antes del evento $0$, todos los mingitorios están vacíos**

#Salida

Debes imprimir $N$ enteros separados por espacio, $1$ en caso de que el $i$-ésimo mingitorio esté ocupado ó $0$ en caso contrario.

#Ejemplos

||input
3 1
1
||output
1 0 0
||end

<img src="https://i.imgur.com/wV3AluO.jpeg" />

* Todos los mingitorios empiezan vacíos y con la misma distancia al mingitorio ocupado más cercano (en este caso la distancia es indefinida por no haber ningún mingitorio ocupado).
* Los mingitorios válidos pertenecen al mismo rango, que es de tamaño 3.
* De entre todos los mingitorios válidos se elige el que está más a la izquierda.

||input
3 2
1
1
||output
1 0 1
||end

<img src="https://i.imgur.com/6aC8e12.jpeg" />

* Continuando de la configuración del ejemplo anterior.
* El olímpico que llega en $t=1$, dispone de 2 mingitorios libres, uno de ellos con distancia 1 al mingitorio ocupado más cercano y el otro con distancia 2. Por lo tanto elige el mingitorio a 2 posiciones de distancia.

||input
3 8
1
1
0 0
1
1
0 4
1
0 3
||output
0 1 1
||end

<img src="https://i.imgur.com/sBLuztV.jpeg" />

* Continuando la configuración del ejemplo anterior.
* En $t=2$ se va el olímpico que llegó en $t=0$.

<img src="https://i.imgur.com/ZM1Dz2D.jpeg" />

* En $t=3$ llega un olímpico. Hay 2 mingitorios libres, pero solo uno de ellos tiene la distancia al mingitorio ocupado más grande.

<img src="https://i.imgur.com/GA1abTS.jpeg" />

* En $t=4$ llega un olímpico y ocupa el único mingitorio disponible.

<img src="https://i.imgur.com/9CIZFWU.jpeg" />

* En $t=5$ se va el olímpico que llegó en $t=4$.

<img src="https://i.imgur.com/sBLuztV.jpeg" />

* En $t=6$ llega un olímpico y ocupa el único mingitorio disponible.

<img src="https://i.imgur.com/9CIZFWU.jpeg" />

* En $t=7$ se va el olímpico que llegó en $t=34$.

<img src="https://i.imgur.com/6WcNYGH.jpeg" />

||input
7 6
1
1
1
1
1
1
||output
1 1 1 1 1 0 1
||input
8 14
1
1
1
1
1
1
1
1
0 4
0 5
0 6
0 3
0 7
1
||output
1 0 0 1 0 1 0 1
||end

#Consideraciones

* $1 \le N, Q \le 10^5$.
* $0 \le t_i < Q$ para toda $0 \le i < Q.$
* Se asegura que nunca llegará un olímpico cuando todos los mingitorios están ocupados.
* Se asegura que para todo evento de la forma $0$ $t_i$ siempre existirá un olímpico en algún mingitorio que llegó en el momento $t_i$.

#Subtareas

* Subtarea 1 (20 puntos): $1 \le N, Q \le 10^3$.
* Subtarea 2 (20 puntos): $1 \le N \le 10^5$ y $1 \le Q \le 5\times 10^2$.
* Subtarea 3 (20 puntos): $1 \le N, Q \le 10^5$, no hay eventos de tipo $0$. Es decir, ningún olímpico sale.
* Subtarea 4 (40 puntos): Sin restricciones adicionales.
