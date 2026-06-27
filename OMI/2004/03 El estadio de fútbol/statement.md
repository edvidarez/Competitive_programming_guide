# Descripción

Como buen mexicano, Karel es un aficionado al fútbol.  Al llegar a Morelia se ha enterado que el estadio de fútbol se encuentra en la cima del Cerro Quinceo.

Desgraciadamente, Karel no conoce el camino a dicho cerro, por lo que tu deberás escribir un programa que le ayude a encontrarlo.

# Problema

Deberás escribir un programa que le permita a Karel llegar al punto más alto del Cerro Quinceo desde su posición inicial.

# Entrada

En el mundo de entrada se representa un mapa del Cerro de Quinceo como un rectángulo cuya esquina inferior izquierda esta en la posición (1,1).   En cada casilla de dicho rectángulo hay al menos un zumbador, el número de zumbadores en cada casilla indica la altura del cerro en ese punto.  La altura máxima en cualquier punto del cerro no sobrepasará los 99 zumbadores.

Como el Cerro Quinceo es muy regular, se puede asegurar lo siguiente:

Si Karel se sitúa en el extremo oeste del mapa, sin importar la fila, podrá avanzar hacia el este y la altura ira siempre creciendo hasta llegar a una altura máxima de esa fila, a partir de ese punto si se sigue avanzando hacia el este la altura ira siempre decreciendo.

De igual manera sucede con las columnas, si Karel se sitúa en el extremo sur del mapa, sin importar la columna, podrá avanzar al norte, la altura ira siempre creciendo hasta encontrar una fila con altura máxima, a partir de ese momento si se sigue avanzando hacia el norte, los valores de altura irán siempre decreciendo.

El mapa cuenta además con la singularidad de que todas las columnas tienen su máxima altura en la misma fila, al igual que todas las filas tienen su máximo en la misma columna.

El mapa tiene una dimensión máxima de 50 x 50.

Karel siempre iniciará en la posición (1,1) orientado hacia el norte y con cero zumbadores en su mochila.

A continuación se muestra un mundo de ejemplo:

![estadio](estadio.jpg)

NOTA:  Aunque en el ejemplo el mapa del cerro es un cuadrado, en los casos de evaluación podrá tener forma rectángular.

# Salida

Tu programa deberá hacer que Karel encuentre la casilla con altura máxima de todo el mapa y se posicione en ella.  Al llegar a ese punto, Karel deberá apagarse.

A continuación se muestra como debe quedar Karel para el mundo de ejemplo.

![estadio22][1]

Para la evaluación de este problema únicamente importa la posición final de Karel, no importa ni su orientación ni los zumbadores del mapa.


  [1]: estadio1.jpeg
