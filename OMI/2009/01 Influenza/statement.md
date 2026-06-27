# Historia

A raíz del cambio de fecha de la OMI este mayo pasado, el doctor Karel House se dio a la tarea de encontrar una vacuna para el virus de la influenza A(H1N1). La vacuna ya está lista, pero ahora, Karel requiere saber cuántas dosis debe fabricar.
Fabricar las dosis (sin importar el número) toma exactamente N días. Cada día que pasa, el virus se dispersa por las casillas del mundo.  Por cada casilla que contenga virus (sin importar el número de virus en esa casilla), Karel necesita una dosis de vacuna. Para erradicar el virus del mundo, Karel necesita saber cuántas casillas contendrán virus transcurridos N días a partir de hoy.
Actualmente hay ciertas casillas que contienen virus, los virus están representados por un zumbador. Cada día que pasa, un virus se mantiene en la casilla que ocupa y se dispersa a las cuatro casillas contiguas (norte, sur, este y oeste).  Los virus nunca abandonan el mundo de Karel.

# Problema

Ayuda al doctor Karel House a saber cuántas dosis debe fabricar para erradicar el virus de la influenza dejando una cantidad de zumbadores igual al número de dosis en la casilla (1,1) del mundo.

# Consideraciones

* Karel inicia en la posición (1,1) con orientación norte.
* En la posición (1,1) se encuentra el número N de días que se requieren para fabricar la vacuna.
* En el mundo habrá varias casillas que contienen 1 zumbador y representan las casillas inicialmente con virus.
* Además de las paredes que limitan el mundo, no hay ninguna otra pared.
* Karel lleva un número infinito de zumbadores en la mochila.
* Karel debe de dejar en la posición (1,1) un número de zumbadores igual a la cantidad de vacunas que se necesitan.
* No importa la posición ni la orientación final de Karel.
* No importan los zumbadores que dejes en el mundo exceptuando los de la posición (1,1), los cuales deben representar el número de vacunas
* No olvides lavarte bien las manos constantemente.

# Ejemplo
<img src="https://omegaup.com/influenza1.png"/>
<img src="https://omegaup.com/influenza2.png"/>

