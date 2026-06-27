Para tu clase de biología te encuentras realizando un estudio con una cierta raza de moscas. El objetivo de tu experimento es encontrar el modelo que rige el crecimiento demográfico de esta raza de moscas.

Para hacer un modelo de la población de tu grupo de moscas, identificas cada mosca con dos datos: el momento en que nace la mosca y el momento en que muere. Todas las moscas viven por lo menos una unidad de tiempo.

# Problema

Para un grupo de $1 \le n \le 10 000$ moscas, de las cuales tienes apuntados el momento de su nacimiento y el de su muerte como dos números enteros $1 \le n_i, m_i \le 60000$, escribe un programa que encuentre cuál es la población máxima del grupo de moscas y que escriba el rango de tiempo en que se puede encontrar esta población.

# Entrada

Tu programa deberá leer los siguientes datos:

En la primera línea el número N indicando la cantidad total de moscas en el experimento.

En las siguientes N líneas una pareja de números enteros separados por un espacio, indicando el momento del nacimiento y el momentos de la muerte de la mosca respectiva.

# Salida

Tu programa deberá escribir en el los siguientes datos: en la primera línea el número P indicando cual fue la máxima población alcanzada para el experimento y en la siguiente línea los rangos de tiempo en los que esta población se alcanzo. Los rangos de tiempo en los que se alcanzó la población máxima deberán ir escritos en una línea como inicio del rango, fin del rango, inicio del rango, fin del rango...

# Ejemplo

||input
5
1 10
12 18
20 30
5 12
25 33

||output
2
5 10
25 30
||end

# Consideraciones

 Nunca habrá mas de 20,000 moscas y los rangos de vida de las moscas siempre se encontraran entre 1 y 60,000.
