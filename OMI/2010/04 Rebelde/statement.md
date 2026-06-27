# Descripción

Este año Karel cumple 6 años. Como todo niño de esa edad comienza a cuestionar la autoridad y le gusta empezar a tomar sus propias decisiones, por suerte, aún lo hace con cierta medida.

A Karel se le ha dado el mapa de un laberinto que contiene instrucciones claras a seguir para llegar a una salida (este laberinto tiene varias salidas). En su rebeldía, Karel ha decidido hacer $N$ cambios a dichas instrucciones y aun así llegar a una de las
salidas del laberinto.

El mapa del laberinto se representa como un rectángulo sin paredes interiores en donde cada casilla tiene un montón de zumbadores con alguno de los siguientes valores:

 - 0 zumbadores: Indica una salida del laberinto
 - 1 zumbador: Indica que el siguiente avance debe hacerse hacia el norte
 - 2 zumbadores: El siguiente avance debe hacerse hacia el este
 - 3 zumbadores: El siguiente avance debe hacerse hacia el sur
 - 4 zumbadores: El siguiente avance debe hacerse hacia el oeste

Karel quiere iniciar de la esquina inferior izquierda del mapa y llegar a una de las salidas del laberinto cambiando EXACTAMENTE $N$ de las instrucciones del camino por el que pasa.

Por si fuera poco, Karel está decidido a no pasar nunca sobre sus pasos de modo que el camino que tome hacia la salida nunca pasará dos veces por el mismo lugar.

Para saber el número $N$ de instrucciones que Karel quiere cambiar, el rectángulo tiene además una protuberancia hacia abajo en la esquina inferior izquierda cuya casilla tiene un número de zumbadores igual al número $N$. (**NOTA: La protuberancia no
forma parte del laberinto y no debe considerarse una casilla de salida o de instrucción**). Para mayor claridad mira la figura del ejemplo

# Problema

Ayuda a Karel a encontrar una salida del laberinto a la que pueda llegar partiendo desde la esquina inferior izquierda del mapa y cambiando EXACTAMENTE $N$ instrucciones en el camino. Se considera un cambio de instrucción si Karel hace algo distinto de lo que se le indica en el recuadro. Recuerda que en su camino hacia una salida Karel nunca pasa dos veces por el mismo lugar.

Karel deberá apagarse en una de las salidas del laberinto a la que pueda llegar partiendo de la esquina inferior izquierda del laberinto y realizando EXACTAMENTE $N$ cambios a las instrucciones en el camino.

# Consideraciones

 - Karel inicia siempre en la protuberancia del mapa que contiene el número N
viendo hacia el norte.
 - A excepción de la protuberancia, el mapa se representa como un mundo
rectangular sin paredes internas.
 - Karel lleva un número infinito de zumbadores en su mochila.
 - Para obtener los puntos sólo importa la posición final de Karel, y no su orientación ni el estado final del mundo (ver la configuración final del ejemplo).

# Ejemplo

Mundo inicial

![Mundo inicial](mundoinicial.png)

Mundo final

![Mundo final 1](mundofinal.png)

Si sigue las instrucciones del mapa, Karel llega a la salida que está en la esquina superior izquierda del laberinto. Sin embargo, también es posible llegar a esa salida  haciendo exactamente 2 cambios. Los cambios son:

 - Cambiar el 1 en la posición (1,1) del mapa por un 2.
 - Cambiar el 4 en la posición (2,1) por un 1.
 - El camino que sigue Karel con dichos cambios es: (1,1) cambia el 1 por 2, (2,1) cambia 4 por 1, (2,2) (1,2), (1,3), (1,4), (2,4), (2,5), (1,5) y ahí se detiene porque llegó a una salida después de haber hecho EXACTAMENTE 2 cambios.
