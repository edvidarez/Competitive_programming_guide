# Descripción

¿Alguna vez has oído decir que siempre es bueno recordar el lugar de donde saliste? Pues el día de hoy, para Karel. ¡Va a ser indispensable!

Karel está participando en un rally. Como cualquier rally, el objetivo es seguir una  serie de pistas. Las reglas son sencillas:

1. Desde su posición y orientación, Karel debe avanzar hasta encontrar una  casilla con zumbadores
2. En esa casilla deberá:
- Recoger todos los zumbadores
- Girar a la izquierda tantas veces como zumbadores había en la casilla
3. Regresar al paso 1.
4. Si en algún momento Karel pasa por la casilla de donde salió al inicio del rally, se deberá apagar en esa casilla. El rally habrá terminado.

# Problema

Escribe un programa que ayude a Karel a seguir las pistas del rally y a recordar la casilla de donde salió para poder apagarse cuando vuelva a pasar por ella.

Karel deberá apagarse en la posición donde inició con la orientación que tiene cuando  vuelve a pasar por ella, deberá recoger los zumbadores de todas las pistas por las que pasó durante el rally y dejar todos los demás montones de zumbadores que aparezcan en el mundo tal como estaban al inicio.

# Consideraciones

- El rally se lleva a cabo en un mundo rectangular que puede tener cualquier cantidad de montones de zumbadores y paredes intermedias.
- Karel inicia en alguna posición del mundo con alguna orientación.
- Karel lleva 1 zumbador en la mochila.
- Los organizadores del rally te aseguran que si sigues correctamente las pistas,  nunca chocarás con una pared.
- Los organizadores también te aseguran que si sigues correctamente las pistas, siempre volverás a pasar por la casilla de donde saliste.

# Ejemplo

Mundo inicial

![Mundo inicial](mundoinicial.png)

Mundo final

![Mundo final 1](mundofinal.png)

Karel avanza hasta encontrar el montón con 2 zumbadores. Recoge los zumbadores, da dos giros y vuelve a avanzar. Cuando pasa otra vez por la casilla de origen, inmediatamente se apaga.
