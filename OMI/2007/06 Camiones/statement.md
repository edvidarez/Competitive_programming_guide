# Descripción

Recientemente se inauguró el Parque de los Clonosaurios, Juanito, el gerente del parque se enfrenta a un dilema difícil de resolver. Por lo que ha pedido tu ayuda.

El parque se encuentra retirado de la civilización, para llegar a el es necesario tomar un camión. Los camiones del parque funcionan de la siguiente manera:

* A cierta hora del día, llamémosle *H*, llega a la parada el primer camión de ese día.
* El camión espera *t* nanosegundos en la parada y se retira.
* En el instante en el que el camión se retira, llega un siguiente camión a la parada.
* El proceso se repite hasta que se retira el último camión del día.

Juanito renta los camiones, si al momento de retirarse el camión no tiene pasajeros inmediatamente regresa y no es necesario que se pague la corrida. Como buen gerente, Juanito desea cortar los gastos de su parque, por lo que necesita minimizar el número de camiones que se pagan en el día.

En base a estadísticas, Juanito sabe en qué momento llega gente a la parada. El tiempo *t* de nanosegundos que espera cada camión no es negociable, sin embargo Juanito tiene opción de recorrer la hora de llegada del primer camión hasta un máximo de t nanosegundos, de modo que puede decidir que el primer camión llegue en cualquier momento entre *H* y (*H* + *t*).

# Problema

Dados dos números *t* y *n*, donde *t* representa el número de nanosegundos que espera cada camión en la parada y *n* el número de personas que se esperan ese día y una lista de números que representan el nanosegundo del día en el que cada persona llega a la parada, escribe un programa que determine en qué momentos puede llegar el primer camión de modo que se minimice el número de camiones en donde subió al menos una persona.

# Entrada

Tu programa debe leer del teclado de la PC los siguientes datos:

* En la primera línea los números *t* y *n* separados por un espacio, con 1<= *t, n* <=100,000, donde *t* representa el tiempo en nanosegundos que espera cada camión y n el número de personas que se esperan ese día.
* La segunda línea contiene *n* números enteros separados por un espacio que representan el nanosegundo en que cada una de las n personas llegó a la parada, esta lista de números SIEMPRE ESTARÁ ORDENADA DE MANERA CRECIENTE.

# Consideraciones

* No hay dos personas que lleguen en el mismo nanosegundo a la parada.
* Si una persona llega a la parada antes que el primer camión, la persona se va a su casa y presenta una queja contra el administrador del parque.
* Si alguien pone una queja contra Juanito, éste será despedido. Por lo que Juanito requiere que TODAS las personas de ese día lleguen al parque.
* El nanosegundo en que llega cada persona a la parada esta contado a partir de *H*, es decir *H* corresponde al nanosegundo 0.
* El nanosegundo de llegada de las personas está representado por un número mayor o igual a 0 y menor o igual a 2,000,000,000.
* Si una persona llega a la parada en el nanosegundo en el que se está retirando un camión, no puede subir a ese camión, debe hacerlo en el siguiente. Por ejemplo, si el tiempo de espera de cada camión es de 10 ns, y el camión llega en el nanosegundo 0, entonces a ese camión suben las personas que lleguen entre el nanosegundo 0 y el 9, una persona que llegue en el nanosegundo 10, tiene que subir al siguiente camión.
* La capacidad de cada camión es suficiente para alojar a todas las personas que llegan en ese día.

# Salida

Tu programa deberá escribir en la pantalla de la PC los siguientes datos:

* En la primera línea un número entero indicando el número mínimo de camiones que se requieren para llevar a toda la gente.
* La segunda línea deberá contener una lista de enteros separados por un espacio que representan todos los posibles inicios que obtienen dicho mínimo.

Por ejemplo, si el tiempo de espera de cada camión es de 10 ns, esto quiere decir que Juanito puede decidir que el primer camión llegue en cualquier momento entre el nanosegundo 0 y el nanosegundo 10. En la salida deberán aparecer todos los nanosegundos entre 0 y 10 en donde el número de camiones utilizados sea igual al mínimo posible.

# Ejemplo

||input
3 5
4 5 7 8 9
||output
2
1
||input
4 3
7 14 15
||output
2
1 2 4
||input
2 10
3 4 7 8 12 13 14 15 20 21
||output
7
1 2
||end
