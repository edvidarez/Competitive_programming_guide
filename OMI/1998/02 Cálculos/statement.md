# Descripción

Tienes una calculadora de $4$ dígitos decimales que sólo puede realizar $2$ operaciones: multiplicar por $A$ y dividir entre $B$. Si el resultado de multiplicar un número por $A$ es un número de más de $4$ dígitos la calculadora da como resultado $1$. Si el resultado de dividir entre $B$ no es un número entero, entonces la calculadora trunca el resultado entregando únicamente la parte entera. Por ejemplo, si $A = 2$ y $B = 3$ entonces $20\times A = 40$ y $20/B = 6$ mientras que $6000\times A = 1$ y $6000/B = 2000$. La calculadora siempre comienza con el número $1$ y almacena el último resultado obtenido para utilizarlo en la siguiente operación.

<br>

Escribe un programa que dados $A$ y $B$ encuentre el número mínimo de pasos que se tienen que realizar con la calculadora para obtener un número $N$ comenzando en el $1$ y utilizando únicamente las dos operaciones válidas.

# Entrada

En la primera linea los enteros $A, B$ y $N$.

# Salida

En la primera linea la cantidad mínima de pasos para obtener N.

# Ejemplo

||input
2 3 10
||output
6
||end

# Límites

 - $1 \leq A, B, N < 10^4$
