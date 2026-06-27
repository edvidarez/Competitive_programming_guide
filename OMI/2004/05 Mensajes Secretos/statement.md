# Descripción

Dos amigos necesitan enviarse por correo electrónico mensajes muy importantes y extremadamente reservados. Ante el temor de que alguien pueda leer los correos, deciden codificar los men¬sajes.

El método de codificación que utilizan es el siguiente: ciertos trozos del mensaje los escriben al revés, y estos trozos los encierran entre paréntesis, de modo que al decodificar el mensaje, cualquier texto que esté entre paréntesis deberá ser leído de manera inversa.

Para complicar aún mas la decodificación, el sistema permite tener paréntesis anidados.  En el caso de los paréntesis anidados, se debe primero, invertir el texto en los paréntesis interiores e ir escalando a los exteriores, tal como se resolverían los paréntesis si fuera una ecuación

# Problema

Conocedores de tu habilidad para programar, los amigos te han solicitado que les escribas un programa que si recibe un mensaje codificado, pueda decodificarlo y entregar el mensaje original.

# Entrada

En la primera línea, vendrá una cadena de caracteres representando el mensaje a decodificar.

El mensaje codificado tendrá una longitud máxima de 10,000 caracteres, incluyendo los paréntesis.

El mensaje codificado únicamente contendrá caracteres del siguiente conjunto {'A'-'Z', 'a'-'z', ' ', '(', ')'}

# Salida

Una sola línea, representando el mensaje decodificado.

# Ejemplo

||input
(ada(impi)lO) d(I e)nfor(am)tica
||output
Olimpiada de Informatica
||end
