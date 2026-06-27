# Historia
Karel tiene el súper poder de estirar su cuerpo. Su poder es limitado y puede estirarse a lo más $K$ casillas. Además, Karel está diseñando un nuevo cuarto de entrenamiento, el cuarto tiene internamente varias paredes en forma de L (ver figura). El cuarto se usa así:

* Karel inicia a correr en una de las L’s viendo al norte.
* Cada que Karel tope con una L deberá girar hacia la izquierda o hacia la derecha, dependiendo de que lado tenga libre, siempre tendrá un lado libre.
* Karel debe seguir corriendo en la nueva dirección hasta topar con la siguiente L, girar y continuar así indefinidamente. En la figura puede verse un cuarto de ejemplo y el circuito que debe correr Karel.

![](mrKarelTasticfig1.png "figura 1")

El recorrido del cuarto de entrenamiento siempre es un circuito, es decir, seguir las instrucciones de arriba siempre te lleva de nuevo al punto donde iniciaste, además se asegura que Karel sólo topa con L’s. Sin embargo a veces el camino puede cruzarse.
Karel desea practicar mientras usa su súper poder, es decir, mientras su cuerpo tiene un largo $K$, pero le preocupa que en algún momento, mientras está estirado, pueda chocar contra él mismo (ver ejemplos).
Para saber el largo $K$ al que puede estirarse Karel debes medir la distancia entre su casilla de inicio y la primera L a su derecha (Para que sea más claro, observa la figura).
En la figura puede observase que hay 4 casillas entre la posición donde inicia Karel y la primera L a su derecha, por lo tanto, para este ejemplo, $K$=4.
Debes ayudar a Karel a saber si es seguro para él recorrer el circuito en el cuarto de entrenamiento mientras su cuerpo está estirado.

![](mrKarelTasticfig2.png "figura 2")

# Problema
Escribe un programa que determine si Karel puede recorrer el circuito con su cuerpo estirado sin chocar contra él mismo. Tu programa deberá dejar a Karel viendo al sur si es posible y viendo al norte si choca con su propio cuerpo.

# Consideraciones
* Karel inicia en una L viendo al norte y con el frente y la derecha libre.
* El cuarto de entrenamiento nunca es mayor a 15 x 15.
* Para este programa en el entorno de evaluación Karel podrá ejecutar más de 10,000,000 de operaciones.
* Para obtener los puntos, tu programa deberá dejar a Karel viendo al sur si es seguro correr el circuito con su cuerpo estirado y al norte si corriendo el circuito estirado choca con él mismo. No importan la posición final de Karel ni los zumbadores que queden en el mundo.
* <bold>IMPORTANTE</bold>
* En un conjunto de casos que valen el 53% de los puntos, Karel inicia con infinitos zumbadores en la mochila.
* En otro conjunto que vale 29% de los puntos, Karel inicia con 1 zumbador en la mochila.
* En el último conjunto con valor de 18% de los puntos, Karel inicia con 0 zumbadores en la mochila.
* En cada uno de los conjuntos de casos es necesario resolver correctamente todos los casos para obtener puntos, es decir, todos los casos del conjunto están agrupados.

#Ejemplo
|Entrada|Descripción|
|---|---|
|![imagen0][0]|En este ejemplo $K=4$ porque hay 4 casillas entre la posición donde inicia Karel y la primera L que hay a su derecha.<br>En la figura se muestra a Karel con su cuerpo estirado 4 casillas recorriendo el circuito. Para visualizarlo mejor, puedes imaginar que Karel es una serpiente de largo $K$ que va avanzando por el circuito.<br>Este circuito es seguro para ser corrido por Karel ya que el circuito nunca se cruza sobre sí mismo, de modo que Karel nunca chocará contra su propio cuerpo.<br>Karel debe terminar viendo al SUR, como se muestra.|
|![imagen1][1]|En este ejemplo $K=5$ porque hay 5 casillas entre la posición donde inicia Karel y la primera L que hay a su derecha.<br>Este circuito tiene un cruce, si observas el cruce verás que con su cuerpo en largo 5 (o mayor), Karel chocaría contra si mismo, de modo que este circuito no es seguro. (Para este ejemplo, si $K$ fuera menor o igual que 4, no chocaría contra sí mismo).<br>Karel debe terminar viendo al NORTE, como se muestra.|
|![imagen2][2]|En este ejemplo $K=4$ porque hay 4 casillas entre la posición donde inicia Karel y la primera L que hay a su derecha.<br>Este circuito tiene un cruce, sin embargo el largo mínimo que se requeriría para que Karel chocara contra él mismo es de 9, por lo tanto este circuito es seguro para Karel.<br>Karel debe terminar viendo al SUR, como se muestra.|

[0]: mrKarelTasticin1.png
[1]: mrKarelTasticin2.png
[2]: mrKarelTasticin3.png
