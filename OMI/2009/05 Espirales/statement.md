#Descripción
Se tiene una cuadrícula rectangular de $M$ por $N$ casillas. Iniciando de la casilla en la esquina superior izquierda, se desea dibujar una espiral en la cuadrícula.

Las reglas para dibujar la espiral son las siguientes:

- La espiral siempre se inicia a dibujar desde la esquina superior izquierda.
- La espiral siempre gira en sentido horario.
Puedes dejar de dibujar la espiral en cualquier momento.
- Un punto se considera una espiral, de igual forma una línea.
- La espiral nunca pasa dos veces sobre un cuadro.

Algunos ejemplos de espirales válidas son:

![Imagen ejemplo](imagenejemplo01.png)

#Problema
Dadas las dimensiones de una cuadrícula, escribe un programa que cuente el número total de espirales distintas que pueden dibujarse y escriba ese número módulo 1,000,000,000, es decir, el residuo que se obtiene de dividir el número por 1,000,000,000.

#Entrada
Tu programa deberá leer de la entrada estándar los siguientes datos:
En la primera línea dos números enteros separados por un espacio: $M$ y $N$ que representan el alto y el ancho de la cuadrícula respectivamente.

#Salida
Tu programa deberá escribir a la salida estándar un único número que indique el número total de espirales distintas que pueden dibujarse.



#EJEMPLO

||input
5 5
||output
251
||end

#Límites

* $1 <= N, M <= 1000$
* En un subconjunto de casos de prueba con un valor total de 30 puntos $N, M <= 10$
* En un subconjunto de casos de prueba con un valor total de 70 puntos $N, M <= 250$
