# Descripción

Como nos lo ha mostrado Hollywood una y otra vez, en el mundo existe toda una red
de espías dedicados a conseguir información valiosa para sus empresas o gobiernos.

Acabas de ser contratado por una nueva agencia de inteligencia y tu tarea es
conseguir información. Para lograrlo se te permite utilizar un dispositivo lector de
mentes en la mente de uno y sólo uno de los espías que tu agencia tiene localizados.

Los espías funcionan de la siguiente manera:

- Cada espía se encarga de espiar a uno y sólo uno de los otros espías.
- Si el espía $A$ espía al $B$ se considera que tiene acceso a toda la información en
la mente de $B$, de esta forma, si $B$ espía a $C$ automáticamente la mente de $A$
contiene, además de su información, la información de las mentes de $B$ y $C$.

Tu agencia sabe quién espía a quién. Tu tarea es decidir en qué espía utilizar el lector
de mentes, de modo que el número de mentes leídas sea el máximo posible.

Escribe un programa que dado el número $E$ de espías y la lista de quién espía a quién
determine cuál es la cantidad máxima de mentes que puedes leer.

# Entrada

Tu programa debe leer del teclado la siguiente información:

- En la primer línea el número $E$ que indica la cantidad de espías de los que se tiene información.
- En las siguientes $E$ líneas habrá un único entero que indica el espía espiado por el espía que corresponde a esa línea. Por ejemplo, la primera de estas  líneas tendrá un número que indica a quien espía el espía 1, la segunda uno que indica a quien espía el espía 2, etc.

# Salida

Tu programa debe escribir a la pantalla un único número que indica el número máximo
de mentes que puedes leer utilizando el lector de mentes sólo una vez.

# Ejemplo

||input
7
4
3
2
5
6
1
3
||output
4
||description
Por ejemplo, si se utiliza el lector de mentes en el espía 5, automáticamente se tiene la información de las
mentes de los espías 5, 6, 1 y 4. Ya que 5 espía a 6, 6 a 1, 1 a 4 y 4 a 5.
||end

# Límites
* $2 < E <= 10^6$
* Puedes estar seguro de que:
1. Ningún espía se espía a sí mismo.
2. Ningún espía espía a un espía que no esté en el grupo, es decir, nunca espiará
a un espía cuyo número sea mayor a $E$ ni menor a 1.
