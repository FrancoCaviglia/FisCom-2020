/*

Código correspondiente a la entrega del Trabajo Práctico N°7

Instituto Balseiro - Física Computacional - Franco Caviglia

*/

#include <iostream>      // Incluye los objetos cin, cout.
#include <fstream>       // Incluye las clases ifstream, ofstream.
#include <cstdlib>       // Incluye función srand() y rand().
#include <cmath>         // Permite evaluar la potencia.
#include <time.h>        // Incluye la función time().

using namespace std;

void guardar(long double matriz[][2], int X, int Y, string P){  // Guarda la matriz en un archivo .txt

    ofstream archivo_guardar("Datos/"+P+".txt");
    if(archivo_guardar.is_open()) {
        for (int y = 0; y < Y; y++){
            for (int x = 0; x < X-1; x++){
                archivo_guardar << matriz[y][x] << " ";
                }
            archivo_guardar << matriz[y][X-1] << endl;
        }
        archivo_guardar.close();
    }
}

long double vector_fuerza(long double fn[][2], long double xn[][2], int N){ // Calcula el vector con las componentes x,y la fuerza sobre cada N.

    long double dist_x, dist_y, norma, v_fuerza, fuerza_x, fuerza_y, aux;
    long double e = 0;                              // Además usa parte de lo calculado para obtener la energía potencial

    for(int i = 0; i < N; i++){                     // Pensando en la matriz F_ij, itera sobre los elementos bajo la diagonal prinicipal.
        fn[i][0] = 0.0;
        fn[i][1] = 0.0;
        for (int k = 0; k < i; k++){

            dist_x = xn[i][0] - xn[k][0];
            dist_y = xn[i][1] - xn[k][1];
            norma  = dist_x*dist_x + dist_y*dist_y;
            aux = pow(norma, -3.0);

            e += 4.0*aux*(aux-1.0);

            v_fuerza = 24.0*aux*(2.0*aux-1.0)/norma;
            fuerza_x = v_fuerza*dist_x; // Fuerza que siente i debido a k
            fuerza_y = v_fuerza*dist_y;

            fn[i][0] += fuerza_x;
            fn[i][1] += fuerza_y;
            fn[k][0] -= fuerza_x;       // Hace uso de la antisimetría de F_ij
            fn[k][1] -= fuerza_y;
        }
    }
    return e;
}

long double e_cinetica(long double vn[][2], int N){     // Retorna la energía cinética dadas las velocidades de las N partículas

    long double e = 0;

    for (int k = 0; k < N; k++){
        e += (pow(vn[k][0], 2.0) + pow(vn[k][1], 2.0));
    }
    e = 0.5*e;

    return e;
}

void chequea(long double vn[][2], long double xn[][2], int N, int L){ // Revisa que las partículas sigan las condiciones de borde, y corrige si no lo hacen.
    for (int k = 0; k < N; k++){
        if (xn[k][0] >= L){
            vn[k][0] *= -1;
            xn[k][0]  = 2*L-xn[k][0];
        }
        else if (xn[k][0] <= 0){
            vn[k][0] *= -1;
            xn[k][0] *= -1;
        }
        if (xn[k][1] >= L){
            vn[k][1] *= -1;
            xn[k][1]  = 2*L-xn[k][1];
        }
        else if (xn[k][1] <= 0){
            vn[k][1] *= -1;
            xn[k][1] *= -1;
        }
    }
}

int main(){

    /*** Parámetros y constantes ***/

    const int Nc = 30;                  // Raíz de la cantidad de partículas
    const int T  = 2000;                // Cantidad de pasos de tiempo
    const int N  = Nc*Nc;               // Cantidad de partículas: Guarda el cuadrado para no calcularlo siempre.

    const long double L  = 54.77226;    // Tamaño de la caja cuadrada en dos dimensiones dada la densidad igual a 0.3

    const long double h  = 0.005;       // Paso de tiempo.
    const long double h1 = 0.5*h;       // Mitad del paso de tiempo
    const long double h2 = 0.5*h*h;     // Mitad del cuadrado del paso de tiempo. Se guarda para no calcularo siempre.

    const long double v0 = 1.1;         // Módulo de la coordenada x de la velocidad inicial.
    const long double a  = L/(Nc+1);    // Espaciado de la grilla cuadrada donde se ubican inicialmente las partículas.

    unsigned int semilla = 1601589908; // time(0);     // 1601317248; // Guarda la semilla de la secuencia random.

    long double fn_0[N][2];        // Vector de fuerzas en el tiempo n
    long double fn_1[N][2];        // Vector de fuerzas en el tiempo n+1 (casi siempre)
    long double xn[N][2];          // Vector de Nx2 con las posiciones
    long double vn[N][2];          // Vector de Nx2 con las velocidades
    long double en[T][2];          // Vector de Tx2 con las energías cinética y potencial.

    srand(semilla);                                // Utiliza la semilla para inicializar los números random.

    /* Arma las condiciones iniciales */

    for (int i = 0; i < N; i++){                   // Establece los valores iniciales de la grilla
        vn[i][0] = v0*(2*(rand() % 2)-1);          // Posibles valores random -1 y +1.
        vn[i][1] = 0.0;                            // Posibles valores random -1 y +1.
    }

    int n;
    for (int i = 0; i < Nc; i++){                  // Establece los valores iniciales de la grilla
        for (int j = 0; j < Nc; j++){              // Establece los valores iniciales de la grill
            n = i*Nc + j;
            xn[n][0] = (i+1)*a;                    // Posibles valores random -1 y +1.
            xn[n][1] = (j+1)*a;                    // Posibles valores random -1 y +1.
        }
    }

    /* Guarda las condiciones iniciales */

    guardar(xn, 2, N, "pos-"+to_string(0)+"-"+to_string(semilla));
    guardar(vn, 2, N, "vel-"+to_string(0)+"-"+to_string(semilla));

    /* Actualiza las energías y fuerzas iniciales */

    en[0][0] = e_cinetica(vn, N);
    en[0][1] = vector_fuerza(fn_0, xn, N);              // Como fn_0 no se pasa por copia, no es necesario que lo retorne para actualizarlo.

    /* Bucle temporal. El valor n = 0 ya lo tiene */

    for(int t = 0; t < T; t++){

        for (int k = 0; k < N; k++){                    // Actualiza las N posiciones.
            xn[k][0] += (vn[k][0]*h + fn_0[k][0]*h2);
            xn[k][1] += (vn[k][1]*h + fn_0[k][1]*h2);
        }

        chequea(vn, xn, N, L);                          // Revisa que se sigan las condiciones de borde.

        en[t][1] = vector_fuerza(fn_1, xn, N);          // Actualiza la fuerza fn_1 del paso n al paso n+1. Al mismo tiempo calcula la energía potencial.

        for (int k = 0; k < N; k++){                    // Actualiza las N velocidades.
            vn[k][0] += (fn_0[k][0] + fn_1[k][0])*h1;
            vn[k][1] += (fn_0[k][1] + fn_1[k][1])*h1;
        }

        en[t][0] = e_cinetica(vn, N);                   // Calcula el valor de la energía cinética dadas las nuevas velocidades.

        for (int k = 0; k < N; k++){                    // Copia la fuerza a tiempo n sobre la fuerza a tiempo n-1.
            fn_0[k][0] = fn_1[k][0];
            fn_0[k][1] = fn_1[k][1];
        }

        guardar(xn, 2, N, "pos-"+to_string(t+1)+"-"+to_string(semilla));  // Guarda la posición de todas las partículas en cada instante de tiempo.
        guardar(vn, 2, N, "vel-"+to_string(t+1)+"-"+to_string(semilla));  // Guarda la velocidad de todas las partículas en cada instante de tiempo.
    }

    guardar(en, 2, T, "ene-"+to_string(semilla));       // Guarda los valores de energía cinética y potencial calculados en cada instante.

    return 0;
}
