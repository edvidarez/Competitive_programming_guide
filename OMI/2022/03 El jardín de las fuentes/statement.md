Un amigo tuyo diseña jardines con fuentes de agua y te ha pedido ayuda.

Un jardín se representa como una cuadrícula de $N$ filas por $M$ columnas en donde cada cuadro puede estar ocupado o libre. Tu amigo quiere **llenar de agua todos los cuadros libres del jardín**, para eso el va a colocar _fuentes de agua_ en **algunos de los cuadros libres**. Una vez que coloque y encienda las _fuentes_ pasará lo siguiente:

- Cada segundo, si hay un cuadro libre tal que dos de sus $4$ cuadros _adyacentes ortogonalmete_ (ver glosario) tengan agua, este cuadro se llenará de agua también. Dos cuadros se consideran _adyacentes ortogonalmente_ si comparten una _pared_ en la cuadrícula.

Tu amigo quiere saber dónde poner fuentes de modo que eventualmente todas las casillas libres se llenen de agua y se utilice el menor número de fuentes posible.

**Este es un problema de sólo salida.**  Esto quiere decir que podrás descargar los archivos de evaluación y deberás mandar un ".zip" con los archivos de salida correspondientes a cada uno de ellos.

# Problema

A partir de los mapas de los jardines que tu amigo está diseñando, devuelve como resultado el mismo mapa indicando las posiciones dónde se deben colocar las fuentes.

# Entrada

Este es un programa de **sólo salida**, esto quiere decir que tu puedes descargar los mapas de los jardines, procesarlos en tu máquina de la forma que desees y deberás devolver los mapas indicando los lugares con fuentes. El archivo del mapa del jardín tiene la siguiente estructura:

- En la primera línea, los números $N$ y $M$, el número de filas y de columnas del jardín respectivamente.
- En las siguientes $N$ líneas habrá una cadena con $M$ caracteres representando el mapa. Un carácter '.' representa un cuadro vacío y un carácter '#' representa un cuadro ocupado.
- **El contorno del jardín siempre está formado por cuadros ocupados.**

# Salida

Para cada mapa de entrada deberás enviar un mapa con fuentes colocadas con la siguiente estructura:

- En la primera línea los números $N$ y $M$, el número de filas y de columnas del jardín respectivamente.
- En las siguientes $N$ líneas debe haber una cadena con $M$ caracteres representando el mapa. Un carácter '.' representa un cuadro vacío, un caracter '#' representa un cuadro ocupado y un carácter 'F' representa una fuente.

# Evaluación

Obtendrás $0$ puntos en un caso si:
- Tu mapa no contiene los datos $N$ y $M$ en la primera fila.
- Tu mapa de respuesta no cumple la estructura especificada o usa caractéres inválidos.
- Tu mapa de respuesta es de distinto tamaño del mapa de entrada.
- Tu mapa de respuesta puso fuentes en cuadros que originalmente estaban ocupados.
- Tu mapa de respuesta marca como ocupados cuadros que originalmente estaban libres o viceversa.

Para asignarle puntos a tu mapa, el evaluador realizará el siguiente proceso:
- Simulará el _encendido_ de las fuentes hasta llenar todos los cuadros posibles con tu configuración de respuesta.
- Contará el número de cuadros libres que **quedaron sin llenar** y asignará ese número a la variable $L$.
- Contará el número de fuentes que se usaron y asignará ese número a la variable $F$.
- El puntaje que obtenga tu mapa será mayor mientras el valor $F + (2 \times L)$ sea menor.  Es decir, mientras menos fuentes uses y menos cuadros sin llenar dejes obtendrás mejor puntaje.

# Ejemplo

||input
7 7
#######
#..#..#
#..#..#
####..#
#.....#
#.....#
#######
||output
7 7
#######
#F.#F.#
#.F#.F#
####F.#
#.F.F.#
#F.F.F#
#######
||description
El mapa de salida coloca 10 fuentes (para este mapa existen soluciones con menos fuentes). Con esas 10 fuentes, al cabo de suficiente tiempo, todos los cuadros libres del mapa quedarán llenos de agua.
||end

# Envío de respuestas

Para subir las salidas, debes crear un zip que contenga los archivos de salida. Los archivos de salida deben tener extensión ".out" y deben tener el mismo nombre que el archivo de entrada ".in" al que corresponden.

Puedes descargar los casos de prueba de este problema aquí:

{{output-only:download}}

# Límites por caso

- Caso 1 (6 puntos): $N, M = 3$.
- Caso 2 (6 puntos): $N, M = 100$. No hay cuadros libres adyacentes en el jardín.
- Caso 3 (6 puntos): $N = 3$, $M = 500$
- Caso 4 (6 puntos): $N, M = 499$. Los únicos cuadros ocupados son los del contorno.
- Caso 5 (6 puntos): $N = 500$, $M = 250$. Los únicos cuadros ocupados son los del contorno.
- Caso 6 (6 puntos): $N, M = 500$. Los cuadros libres forman _áreas_ rectangulares.
- Caso 7 (8 puntos): $N, M = 500$. Los cuadros libres forman una _cruz_ en el centro.
- Caso 8 (8 puntos): $N, M = 500$. Los cuadros libres forman una _X_ en el centro.
- Caso 9 (12 puntos): $N, M = 500$. Aleatorio.
- Caso 10 (12 puntos): $N, M = 500$. Aleatorio.
- Caso 11 (12 puntos): $N, M = 500$. Aleatorio.
- Caso 12 (12 puntos): $N, M = 500$. Aleatorio.

# Experimentación

A continuación se incluye un código que puedes copiar en un proyecto de C++ y que te permitirá validar la calidad de tus soluciones.  Para usarlo realiza los siguientes pasos:

* Crea un nuevo proyecto de aplicación C++ en el IDE que estés usando.
* Sustituye el código del archivo principal por el que se comparte a continuación.
* Genera el ejecutable.
* Cuando quieras probar una salida guarda el archivo con el nombre `caso.out` en el mismo subdirectorio que el ejecutable.
* Corre el ejecutable desde una terminal y como salida te entregará el mapa luego de haber encendido las fuentes y un resumen de la cantidad de fuentes que usaste y espacios libres que quedaron sin llenar.

<details>

<summary>Haz clic para ver el código</summary>

```cpp
#include <bits/stdc++.h>

using namespace std;

#define MAX 500

#define libre 0
#define agua 1
#define bloqueo 2
#define fuente 3

int F, L;
int n, m, mapa[MAX + 2][MAX + 2], visitado[MAX + 2][MAX + 2];
int dfil[4], dcol[4];
string s;
queue<pair<int, int> > q;

int cuentaAgua(int fil, int col){
    int res = 0;
    for(int d = 0; d < 4; ++d){
        if (mapa[fil + dfil[d]][col + dcol[d]] & agua) ++res;
    }
    return res;
}

int main()
{
    // LEE LA ENTRADA
    ifstream f("caso.out");
    f >> n >> m;
    for(int fil = 0; fil < n; ++fil){
        f >> s;
        for(int col = 0; col < m; ++col){
            if(s[col] == '#') mapa[fil][col] = bloqueo;
            else if(s[col] == '.') mapa[fil][col] = libre;
            else mapa[fil][col] = fuente;
        }
    }

    // INICIALIZA LOS DESPLAZAMIENTOS PARA NAVEGAR EL MAPA
    dfil[0] = dfil[1] = dcol[2] = dcol[3] = 0;
    dfil[2] = dcol[0] = 1;
    dfil[3] = dcol[1] = -1;

    // LLENA LA COLA CON TODAS LAS CASILLAS QUE SE LLENAN
    // DE AGUA INMEDIATAMENTE
    for(int fil = 0; fil < n; ++fil){
        for(int col = 0; col < m; ++col){
            if(!visitado[fil][col] && mapa[fil][col] == libre){
                if(cuentaAgua(fil, col) >= 2){
                    visitado[fil][col] = 1;
                    q.push({fil, col});
                }
            }
        }
    }

    // SIMULA EL LLENADO DE AGUA
    while(!q.empty()){
        // OBTEN EL ELEMENTO AL FRENTE DE LA COLA Y SACALO.
        int fil = q.front().first;
        int col = q.front().second;
        q.pop();

        mapa[fil][col] = agua; // MARCALO COMO QUE SE LLENA DE AGUA

        // VALIDA SUS 4 VECINOS
        for(int d = 0; d < 4; ++d){
            int nf = fil + dfil[d];
            int nc = col + dcol[d];
            if (!visitado[nf][nc] && mapa[nf][nc] == libre && cuentaAgua(nf, nc) >= 2){
                visitado[nf][nc] = 1;
                q.push({nf, nc});
            }
        }
    }

    // FINALMENTE PROCESA EL COSTO
    cout << n << " " << m << "\n";
    for(int fil = 0; fil < n; ++fil){
        for(int col = 0; col < m; ++ col){
            if (mapa[fil][col] == fuente){
                ++F;
                cout << 'F';
            }
            else if (mapa[fil][col] == libre){
                ++L;
                cout << '.';
            }
            else if (mapa[fil][col] == bloqueo) cout << '#';
            else cout << '-';
        }
        cout << "\n";
    }
    cout << "Fuentes = " << F << "\n";
    cout << "Espacios sin llenar = " << L << "\n";
    cout << "Costo total = " << F + 2 * L << "\n";


    return 0;
}
```
</details>
