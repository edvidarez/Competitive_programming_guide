La situación económica mundial se encuentra en crisis, lo que te ha llevado a
buscar nuevas formas de obtener ingresos económicos. En vista del éxito
obtenido por personajes como Alan Quartermain, Indiana Jones, Lara Croft y
algunos otros, has decidido que la mejor forma de asegurar tu futuro es la
búsqueda de tesoros de culturas antiguas. Investigando sobre las viejas
civilizaciones encontraste información sobre los OMIncas, esta cultura aparece
mencionada en algunos códices como un pueblo de grandes riquezas y sin embargo
su civilización prácticamente no ha sido explorada, lo que la hace el objetivo
perfecto de tus planes.

El primer paso para buscar un tesoro es conocer la ubicación geográfica en
donde se encuentra, durante tus pesquizas encontraste un mapa que indica la
localización de la tumba de su más grande patriarca, desgraciadamente las
instrucciones se encuentran escritas en jeroglíficos, por lo que primero
tendrás que descifrarlas.

El mapa indica un punto de partida y a partir de este da instrucciones sobre
como llegar a la entrada de la tumba. Después de estudiar ampliamente el mapa
has descubierto que hay 14 jeroglíficos diferentes, 10 de ellos simbolizan los
diez dígitos de la numeración decimal (0,1,2,3,4,5,6,7,8,9), otro mas significa
girar a la derecha 90 grados, hay otro que indica girar a la izquierda 90
grados, uno mas simboliza avanzar y el último significa fin del mensaje.

Las
instrucciones del mapa son del estilo de "avanza 20 pasos, gira a la derecha,
avanza 10 pasos ...", una característica importante es que después de un
símbolo de avanzar siempre siguen dos jeroglíficos de número que indican una
cantidad de dos cifras que equivale al número de pasos que hay que avanzar (por
ejemplo, si hay que avanzar 5 pasos seguirían las cifras "05", si hubiera que
avanzar 15 seguirían las cifras "15"). Los jeroglíficos de número irán
únicamente después del símbolo de avanza.

Para encontrar las coordenadas de
entrada a la tumba debes posicionarte en el punto de partida y seguir las
instrucciones.

El jeroglífico "fin del mensaje" solamente aparece una vez en el mapa al final
de las instrucciones, siempre para indicar que se ha llegado al final de ellas.

# Problema

Debes escribir un programa que conociendo los símbolos de los 14 jeroglíficos
diferentes, y el mensaje del mapa, siga las instrucciones y determine el punto
exacto de la entrada de la tumba.

Los jeroglíficos están representados siempre en una cuadrícula de 5 x 5
caracteres. Por ejemplo, los siguientes serían jeroglíficos válidos.

    ...\.     .....     .000.     .11..      .ffff
    .--->     ./|\.     0...0     1.1..      .f...
    .|./.     ..|..     0...0     ..1..      .fff.
    .|...     ..|..     0...0     ..1..      .f...
    .|...     ..|..     .000.     11111      .f...

El mapa contiene un mensaje con instrucciones para llegar a la entrada de la tumba, este mensaje puede contener desde 2 hasta 40 símbolos, seguidos uno del otro, todos en una sola línea de símbolos o 5 líneas de texto. Por ejemplo, suponiendo que las instrucciones fueran: "avanza 10 pasos, gira a la derecha, avanza 1 paso, fin del mensaje", utilizando los símbolos de arriba, el mensaje del mapa se vería así.

    ......11...000....\.......000..11...ffff
    ./|\.1.1..0...0.--->./|\.0...01.1...f...
    ..|....1..0...0.|./...|..0...0..1...fff.
    ..|....1..0...0.|.....|..0...0..1...f...
    ..|..11111.000..|.....|...000.11111.f...


Para este problema se considerará que la posición inicial siempre es la
coordenada (0,0) y la dirección inicial siempre es el norte, considerando la
figura

# Entrada

Tu programa deberá leer los siguientes datos: los 14 jeroglíficos, cada uno en
5 líneas de texto, con 5 caracteres cada una, en el siguiente orden (0, 1, 2,
3, 4, 5, 6, 7, 8, 9, Avanza, Gira derecha, Gira Izquierda, Fin del mensaje),
los caracteres de cada línea no tienen ningún espacio entre ellos. Después de
los 14 jeroglíficos vendrán 5 líneas que pueden tener desde 10 hasta 200
caracteres cada una conteniendo las instrucciones del mapa.

# Salida

Tu programa deberá escribir dos números, escritos en una sola línea y separados
por un espacio, los cuales indiquen la coordenada (horizontal, vertical) en la
que se encuentra la entrada de la tumba.

||input
.000.
0...0
0...0
0...0
.000.
.11..
1.1..
..1..
..1..
11111
.222.
2...2
..22.
22...
22222
.333.
3...3
..33.
3...3
.333.
4..4.
4..4.
44444
...4.
...4.
55555
5....
5555.
....5
5555.
.666.
6....
6666.
6...6
.666.
77777
....7
...7.
..7..
..7..
.888.
8...8
.888.
8...8
.888.
.999.
9...9
.9999
....9
.999.
.....
./|\.
..|..
..|..
..|..
...\.
.--->
.|./.
.|...
.|...
./...
<---.
.\.|.
...|.
...|.
.FFFF
.F...
.FFF.
.F...
.F...
......11...000....\.......000..11...FFFF
./|\.1.1..0...0.--->./|\.0...01.1...F...
..|....1..0...0.|./...|..0...0..1...FFF.
..|....1..0...0.|.....|..0...0..1...F...
..|..11111.000..|.....|...000.11111.F...
||output
1 10
||end

# Consideraciones

NOTA: Los jeroglíficos de este ejemplo y los carácteres que los representan son
sólo para éste caso, los jeroglíficos de los casos de evaluación utilizarán
carácteres ASCII y representaciones diferentes.

Por ejemplo:

    Asfui
    Desfe
    Ikkel
    U93'3
    0*o92

es un jeroglífico válido y puede representar cualquiera de los 14 símbolos.
