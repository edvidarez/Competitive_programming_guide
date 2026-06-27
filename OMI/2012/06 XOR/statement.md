El XOR es un operador que se incluye en la mayoría de los lenguajes de programación. En el caso de C/C++ se utiliza el símbolo ^ (por ejemplo: a = b ^ c; ) y en el caso de Pascal la palabra xor (por ejemplo: a := b xor c;).
La operación XOR funciona bit por bit. Si aplicas la operación XOR a un par de números, el resultado es el siguiente: para cada dígito binario (bit), si estos los bits en ambos números son iguales (ambos 0 o ambos 1) ese bit, en el resultado, tendrá valor 0. Si los bits en ambos números son distintos (en uno 0 y en el otro 1) ese bit, en el resultado tendrá valor 1.

Por ejemplo si se aplica la operación XOR a 7 y a 12 el resultado será el siguiente:

    7 xor 12 =
         0111
     xor 1100
    ----------
         1011

Un resultado interesante es que si se aplica la operación XOR a un número con él mismo,  ya  que todos los bits son iguales, el resultado es 0.

# Problema

Escribe un programa que dada una lista de números encuentre cuántas subsecuencias de números contiguos distintas existen tales que al aplicar la operación XOR a los números de la subsecuencia en el orden en que aparecen se obtiene como resultado 0.

Una subsecuencia de números contiguos es diferente de otra si inician y/o terminan en posiciones distintas.

# Entrada

Tu programa debe leer del teclado la siguiente información:

* En la primera línea el número entero $N$, la cantidad de números en la lista
* En las siguientes $N$ líneas un número entero $a_i$ que representa al número en la posición $i$-ésima de la lista.

# Salida

Tu programa debe escribir en la pantalla un único número entero que representa la cantidad de subsecuencias distintas tales que al aplicar la operación XOR entre sus elementos se obtiene como resultado 0.

# Restricciones

* $1 < N \le 1,000,000$    Cantidad de números en la lista.
* $1 \le a_i \le 1,000,000$  Valor máximo de cualquier elemento de la lista.

# Ejemplo

||input
6
15
6
9
15
15
5
||output
4
||description
Hay 4 subsecuencias distintas de números consecutivos con las que se obtiene 0:

* `15 xor 6 xor 9 = (1111)xor(0110)xor(1001) = (1001)xor(1001) = (0000)`
* `6 xor 9 xor 15 = (0110)xor(1001)xor(1111) = (1111)xor(1111) = (0000)`
* `15 xor 15 = (1111)xor(1111) = (0000)`
* `15 xor 6 xor 9 xor 15 xor 15 = (1111)xor(0110)xor(1001)xor(1111)xor(1111) = (0000)`
||end

# Evaluación

Para un grupo de casos con valor de 40 puntos $N$ será menor o igual que 1,000.

Para otro grupo distinto de casos con valor de 40 puntos $N$ será menor o igual que 100,000.

Para obtener los últimos 20 puntos será necesario que resuelvas correctamente todos los casos de prueba cuya $N$ sea mayor que 100,000.
