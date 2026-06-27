# Descripción

Homero Simpson y su equipo de zorros (agentes secretos) se han dado a la tarea de capturar al criminal internacional conocido como el gato. El plan de Homero es crear un cerco de vigilancia alrededor del Museo de Springfield, próximo objetivo del criminal.

.

Si se traza un círculo alrededor del museo existen $N$ lugares adecuados para que un zorro ponga su puesto de vigilancia. Homero quiere poner el máximo número de zorros posibles alrededor del Museo, sin embargo hay una limitante. El método de comunicación entre los zorros (inventado por el mismo Homero) es el teléfono de hilo. Este teléfono consta de dos vasos unidos por un hilo el cual debe estar tenso para que funcione. El círculo de zorros estará comunicado por teléfonos de la siguiente forma: cada zorro tendrá dos teléfonos, uno para comunicarse con el zorro a su derecha y otro para comunicarse con el zorro a su izquierda. Para que la comunicación sea funcional, el círculo deberá estar cerrado.

.

Homero no es un buen ingeniero y aunque puede hacer muchos teléfonos, requiere que el hilo de todos tenga la misma longitud.

.

Ayuda a Homero a determinar cuál es el máximo número de zorros que puede colocar alrededor del Museo de modo que todos estén comunicados por teléfonos cuyo hilo sea de la misma longitud.

# Entrada

En la primera línea el número $N$, la cantidad de posiciones posibles para zorros En las siguientes $N$ líneas un entero $d_i$ que representa la distancia que hay entre el
puesto $i$ y el puesto $i+1$. El entero en la última de estas líneas representa la distancia del último puesto hacia el primero para cerrar el círculo.

# Salida

Tu programa debe escribir a la pantalla un único número entero que representa la cantidad máxima de zorros que se pueden colocar.

# Ejemplo

||input
6
3
2
1
4
5
5
||output
4
||description
![Imagen de ejemplo](imagenejemplo.png)

Hay 6 posiciones posibles las cuales se muestran con un punto negro. Entre puntos se muestran las distancias de un punto al siguiente avanzando en sentido horario.

.

Una posibilidad es utilizar dos zorros, el de la primera y quinta posición, sin embargo, el máximo número de zorros que se pueden poner en el círculo es 4. Utilizando las posiciones 1, 3, 5 y 6. La distancia entre todos ellos es de 5.
||end

# Límites

-  $1 \le N \le 5000$
-  $\displaystyle 1 \le \sum_{i=1}^{N} d_i \le 2 \cdot 10^9$

# Evaluación

 - **Subtask 1 (75%):** $0 < N \le 10^3$ y los casos no están agrupados.
 - **Subtask 2 (25%):** No hay restricciones adicionales.
