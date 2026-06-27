 El juego de la ruleta ha sido objeto de innumerables intentos de descubrir alguna flaqueza que permitiera diseñar un método para obtener ganancias sistemáticas. Numerosos autores han escrito tratados de cómo saltar la banca. Norman Leigh escribió una obra clásica donde expone como, junto con doce compañeros, saltaron la banca de Montecarlo. La obra, magistralmente escrita, cuenta hechos “verídicos”. Pero con el auxilio de la ciencia de la computación podemos ver que esos hechos tal como los relata Leigh en su libro no pueden haber sucedido.

 El método que Leigh relata en su libro es el Labouchere inverso. El apostador comienza anotando en una libreta los números 1, 2, 3 y 4. Siempre apuesta una ficha igual a la suma de los números de los extremos de la lista. Si gana agrega al final de la lista un número de igual valor al de su última apuesta, que acaba de ganar. Si pierde tacha los dos números de los extremos de la lista. Si en principio pierde las dos apuestas iniciales, la lista se acaba y en total ha perdido \$10 y entonces vuelve a comenzar anotando los números 1, 2, 3 y 4 en su libreta y reiniciando el método. Si la apuesta llega a superar el límite de la mesa el jugador también reinicia el método anotando una nueva lista de 1, 2, 3 y 4 en su libreta y apostando \$5.

 Recordamos que la ruleta europea consta de los números del 0 al 36 y que, jugando a par se gana si se obtiene un número par distinto de cero, el que juega a impar gana si el número es impar y en caso de salir cero ambos pierden. La apuesta máxima es de $100, recuerde que cuando se supera esta apuesta el método se reinicia. En cada apuesta se gana o se pierde el monto apostado.

 Con dos jugadores uno jugando a par y otro a impar el método se comporta así en unas bolas de ejemplo (el primer renglón muestra las bolas de ejemplo, el último la ganancia acumulada y los demás la lista en cada momento):

    +───────────+─────+─────+─────+─────+─────+─────+─────+────────+───────────+─────+─────+─────+─────+──────+─────+──────+────────+
    | Par       | 31  | 22  | 26  | 11  | 4   | 36  |     | 4      | Impar     | 31  | 22  | 26  | 11  | 4    | 36  |      | 4      |
    +───────────+─────+─────+─────+─────+─────+─────+─────+────────+───────────+─────+─────+─────+─────+──────+─────+──────+────────+
    | 1         | 2   | 2   | 2   | 3   | 3   | 3   | 5   | 5      | 1         | 1   | 2   | 3   | 3   | 1    | 2   | 1    | 2      |
    | 2         | 3   | 3   | 3   | 5   | 5   | 5   | 8   | 8      | 2         | 2   | 3   |     | 3   | 2    | 3   | 2    | 3      |
    | 3         |     | 5   | 5   |     | 8   | 8   |     | 13     | 3         | 3   | 4   |     |     | 3    |     | 3    |        |
    | 4         |     |     | 7   |     |     | 11  |     |        | 4         | 4   |     |     |     | 4    |     | 4    |        |
    |           |     |     |     |     |     |     |     |        |           | 5   |     |     |     |      |     |      |        |
    | Ganancia  | -5  |     | +7  | -2  | +6  | +17 | +3  | P=+16  | Ganancia  | +5  | -1  | -7  | -4  | -10  | -15 | -20  | Q=-25  |
    +───────────+─────+─────+─────+─────+─────+─────+─────+────────+───────────+─────+─────+─────+─────+──────+─────+──────+────────+

# Problema

 Debes escribir un programa que calcule la ganancia o pérdida lograda luego de jugarse cierta cantidad de bolas de ruleta.

# Entrada

 Tu programa deberá leer del teclado de la PC los siguientes datos:

- En la primera línea el número 0 $\lt$ N $\le$ 30,000 de tiradas de ruleta.

- En cada una de las siguientes *N* líneas un número entero entre 0 y 36 representando la bola obtenida en cada uno de los *N* giros de la ruleta.

# Salida

Tu programa deberá escribir en la pantalla de la PC dos enteros *P* y *Q* separados por un espacio indicando respectivamente la ganancia o pérdida de par e impar, proveniente de aplicar el método de Labouchere inverso a las apuestas de par e impar en la serie de bolas contenidas en la entrada.

# Ejemplo

||input
8
31
22
26
11
4
36
0
4

||output
16 -25
||end

# Consideraciones

 El número de tiradas de la ruleta nunca superará los 30,000
