Las familias Escocesas solían identificarse por sus tejidos de Tartán, probablemente los hayas visto, son esos tejidos de cuadros parecidos a los uniformes escolares. Cada familia tenía su propio patrón de tejido.
El COMI ha decidido crear un patrón de tejido para identificar a los miembros de la OMI, pero los cuadros no nos gustan, así que nuestro patrón utilizará rombos. Como somos informáticos, para elegir nuestro patrón, utilizamos un programa de computadora. Este programa generó, mediante un algoritmo secreto, una cuadrícula de $N \times N$ cuadros. Cada uno de ellos puede ser blanco o negro.
Dentro de la cuadrícula quedaron varios rombos blancos sobre fondo negro como el que se muestra en la figura. Debes buscar, dentro de la cuadrícula, cuál es el rombo blanco sobre fondo negro de mayor tamaño (no basta con tener un rombo blanco, se requiere además que todos los cuadros en el resto del cuadrado que lo delimita sean negros, como se observa en la figura). El tamaño del rombo es el largo de su diagonal, para el rombo de la figura su tamaño es $7$. Un punto no se considera rombo, el tamaño mínimo para un rombo es $3$.

# Problema
Escribe un programa que recibiendo $N$, el tamaño de la cuadrícula, y el color de cada uno de los cuadros en ella encuentre el rombo blanco sobre negro de mayor tamaño. En caso de que no exista ningún rombo, tu programa deberá escribir $-1$.

# Entrada
Tu programa debe leer del teclado la siguiente información:

* En la primer línea el número $N$, el tamaño de la cuadrícula.
* En las siguientes $N$ líneas hay $N$ caracteres sin espacios entre ellos. Cada una representa una línea de la cuadrícula, cada carácter representa el color del cuadro correspondiente. Una ‘O’ (o mayúscula) representa un cuadro blanco, un ‘.’ (punto) representa un cuadro negro.

# Salida
Tu programa debe escribir en pantalla un único número entero que indique el tamaño del rombo blanco sobre negro más grande dentro de la cuadrícula.

# Restricciones
$1 < N \le 2,000$

# Ejemplo
||input
9
..O..O...
.OOO.OO.O
OOOOOO...
.OOO.....
O.O...O..
.....OOO.
.O..OOOOO
OOO..OOO.
.O....O..
||output
5
||description
En la imagen puedes observar que hay dos rombos que cumplen con la descripción, uno de tamaño $3$ en la esquina inferior izquierda y uno de tamaño $5$ en la esquina inferior derecha.
El rombo en la parte superior izquierda no es válido porque el fondo no es totalmente negro.
Al ser el rombo de tamaño $5$ el más grande, la respuesta es $5$.
||end

# Evaluación
Para un grupo de casos de prueba con un valor de $60$ puntos $N \le 100$.
