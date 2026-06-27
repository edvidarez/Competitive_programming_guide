# Descripción
A Karel le gustan los rombos y desea dibujar uno. Para ello cuenta con un número de zumbadores en su mochila y un mundo cuadrado de longitud impar sin zumbadores ni paredes interiores.

La cantidad de zumbadores que tiene es tal que alcanzan de manera exacta para que usándolos todos en montones de 1 zumbador Karel pueda rellenar las 4 esquinas del mundo de modo que quede un rombo sin zumbadores en el centro. Para visualizar mejor a lo que nos referimos, te recomendamos ver las figuras de ejemplo.

# Problema

Ayuda a Karel a colocar TODOS los zumbadores de su mochila en el mundo para que obtenga su rombo.

# Consideraciones

 - Karel inicia en esquina inferior izquierda del mundo con orientación norte.
 - Karel inicia con un número múltiplo de 4 de zumbadores en su mochila.
 - El mundo inicial no tiene ningún zumbador ni pared interior y siempre será de longitud impar.
 - El espacio sin zumbadores que representa el rombo debe quedar centrado.
 - No es obligatorio que el rombo toque las paredes exteriores del mundo.
 - En ninguna posición Karel deberá dejar más de 1 zumbador
 - Karel siempre debe quedar con 0 zumbadores en la mochila.
 - No importa la posición ni la orientación final de Karel, sólo los lugares donde
dejaste zumbadores.

# Ejemplo

Mundo inicial 1 - Karel inicia con 12 zumbadores en la mochila

![Mundo inicial 1](mundoinicial1.png)

Mundo final 1

![Mundo final 1](mundofinal1.png)

Mundo inicial 2 - Karel inicia con 36 zumbadores en la mochila

![Mundo inicial 2](mundoinicial2.png)

Mundo final 2

![Mundo final 2](mundofinal2.png)
