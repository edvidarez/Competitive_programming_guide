Hace algún tiempo conociste a un hippie que se dedica a hacer collares con cuentas (bolitas) de vidrio, como anda muy escaso de dinero tu amigo tiene únicamente un hilo en donde guarda todas las cuentas que utiliza.

Hace poco tu amigo recibió un pedido de un collar que debe llevar únicamente C cuentas negras. En su hilo tu amigo puede tener cuentas de diversos colores, y cada vez que hace un collar saca todas las cuentas, escoge las que necesita y vuelve a meter las que le sobraron. Como éste método le resulta muy tedioso, te ha pedido que le ayudes a encontrar una forma de optimizarlo.

# Problema

Cuando abres el hilo, puedes obtener una a una cuentas de cualquiera de los lados del hilo que abriste, si la cuenta que obtienes es negra, la puedes utilizar en el collar, si es de otro color deberás “desperdiciar” esa cuenta.

Debes escribir un programa que determine donde abrir el hilo para que puedas obtener las C cuentas negras desperdiciando el menor número de cuentas posibles de otro color.

# Entrada

Tu programa deberá leer del teclado de la PC los siguientes datos:

- En la primera línea el número 0 < C $\le$ 3,000 de cuentas negras que necesitas.
- En la segunda línea el número C < N $\le$ 30,000 que indica la cantidad de cuentas en el hilo.
- En la tercera línea habrá N números enteros separados cada uno por un espacio que indican el color de las cuentas del hilo, si el número es un 0 indica que la cuenta en esa posición es negra, si el número es 1 indica que la cuenta es de un color distinto.

NOTA: El número de cuentas negras en el hilo siempre será mayor o igual al número de cuentas que necesitas.

# Salida

Tu programa deberá escribir en la pantalla de la PC un número entero que indique el mínimo número de cuentas que debes “desperdiciar” para poder obtener todas las cuentas negras que necesitas.

# Ejemplo

||input
4
8
0 0 1 1 1 0 0 1

||output
1
||end

Recuerda que las cuentas están en un hilo en forma de circulo, por lo que el final y el inicio están unidos. En el ejemplo si abres el hilo entre el último 0 y el último 1, puedes obtener 2 cuentas negras del lado izquierdo del hilo y 2 cuentas negras con 1 de otro color del lado derecho. Por lo tanto el número de cuentas desperdiciadas fue de uno.
