/*

Código correspondiente a la entrega del Trabajo Práctico N°6

Instituto Balseiro - Física Computacional - Franco Caviglia

*/

#include <iostream>      // Incluye los objetos cin, cout, cerr, clog
#include <fstream>       // Incluye las clases ifstream, ofstream.
#include <cstdlib>       // Incluye función srand() y rand().
#include <cmath>         // Permite evaluar la exponencial
#include <time.h>        // Incluye la función time() y clock()

using namespace std;

template <class tipo>
tipo **alocaMatriz(int nfils, int ncols) {  // Función auxiliar: permite tener más control sobre la vida de los array

    tipo **pmat = new tipo*[nfils];         // aloca un arreglo nativo de nfils punteros a enteros

    for( int i=0; i < nfils; ++i){          // aloca cada fila de la matriz como un arreglo nativo de ncols enteros
        pmat[i]= new tipo[ncols];
    }                                       // Tomada de las prácticas de ICOM.

    return pmat;
}

template <class tipo>
void liberaMatriz(tipo **pmat, int nfils) { // Función auxiliar: permite tener más control sobre la vida de los array

    for( int i=0; i < nfils; i++){          // primero debo liberar los elementos de pmat (filas)
        delete [] pmat[i];
    }

    delete [] pmat;                         // y finalmente libero pmat
}

template <class tipo>
void guardar(tipo *matriz[], int X, int Y, int R, double T, unsigned int S){  // Guarda la grilla en el estado final.

    ofstream archivo_guardar("Lising/"+to_string(X)+"-"+to_string(T)+"-"+to_string(R)+"-"+to_string(S)+".txt");
    if(archivo_guardar.is_open()) {
        for (int y = 0; y < Y; y++){
            for (int x = 0; x < X-1; x++){
                archivo_guardar << (int)matriz[y][x] << " ";
                }
            archivo_guardar << (int)matriz[y][X-1] << endl;
        }
        archivo_guardar.close();
    }
}

int energia(int8_t* estado[], int L, int J){    // Retorna la energía debida a la interacción entre espines.

    int s = 0;                                  // Inicializa la variable de la sumatoria

    for (int y = 0; y < L; y++){                // Itera y suma sobre las interacciones a lo largo de x.
        for (int x = 0; x < L-1; x++){
            s += estado[y][x]*estado[y][x+1];
        }
        s += estado[y][L-1]*estado[y][0];       // Añade la interacción en el borde derecho (periodicidad).
    }

    for (int x = 0; x < L; x++){                // Itera y suma sobre las interacciones a lo largo de y.
        for (int y = 0; y < L-1; y++){
            s += estado[y][x]*estado[y+1][x];
        }
        s += estado[L-1][x]*estado[0][x];       // Añade la interacción en el borde inferior(periodicidad).
    }
    return -J*s;
}

int magne(int8_t* estado[], int L){             // Retorna la magnetización como la suma de los espines.

    int m = 0;                                  // Inicializa la variable de la sumatoria.

    for (int y = 0; y < L; y++){                // Suma sobre todas las celdas.
        for (int x = 0; x < L; x++){
            m += estado[y][x];
        }
    }
    return m;
}

int main(){

    /*** Parámetros y constantes ***/

    const int L  = 64;              // Tamaño de la grilla
    const int Tm = 10000;           // Pasos de tiempo
    const int R  = 100;             // Repeticiones del proceso
    const int J  = 1;               // Parámetro del Hamiltoniano.

    const int L2 = L*L;             // Guarda el cuadrado para no calcularlo siempre.

    const double kb = 1.0;          // Constante de Boltzmann.
    const double Tmin = 0.50;       // Temperatura mínima.
    const double Tmax = 5.01;       // Temperatura máxima.

    const double P_MAX = RAND_MAX;  // Retipifica RAND_MAX, para que al dividir no de un entero.

    double proba[4];                // Espacio para las probabilidades. Se desperdician tres posiciones, pero la memoria no es tanto un problema.

    /*** Ciclos anidados ***/

    for (int r = 0; r < R; r++){                            // 1er. iteración: repeticiones
        cout << "[*] COMIENZO REPETICION " << r << endl;
        for (double T = Tmin; T <= Tmax; T += 0.02){        // 2da. iteración: temperatura

            unsigned int semilla = (clock()*time(0)) % 4000000000;  // Guarda la semilla de la secuencia random.

            proba[2] = exp(-J*2*2/(T*kb));                      // Guarda una única vez las probabilidades que son distintas de 1.
            proba[4] = exp(-J*2*4/(T*kb));

            //cout << "[*] CREO GRILLA " << endl;

            int8_t **estado = alocaMatriz<int8_t>(L, L);        // Van a haber dos variables: el estado del sistema, y parámetros que de
            int    **param  = alocaMatriz<int>(Tm, 2);          // sobre este se computen.

            srand(semilla);                                     // Utiliza la semilla para inicializar los números random.

            for (int i = 0; i < L; i++){                        // Establece los valores iniciales de la grilla
                for (int j = 0; j < L; j++){
                    estado[i][j] = 2*(rand() % 2)-1;            // Posibles valores random -1 y +1.
                }
            }

            param[0][0] = energia(estado, L, J);                // Sólo calcula directamente la energía y magnetización
            param[0][1] = magne(estado, L);                     // en tiempo incial. Luego usa diferencias.

            int x = 0;                                          // Inicializa las coordenadas del spin que se puede o no flippear.
            int y = 0;
            int8_t cambio = 0;                                  // Parámetro proporcional al cambio en energía al flippear.

            for(int t = 1; t < Tm; t++){                    // 3da. iteracción: tiempo

                int delta_e = 0;
                int delta_m = 0;

                for(int p = 0; p < L2; p++){                // 4da. iteracción: NxN sorteos

                    x = rand() % L;                             // Toma la coordenada del punto al azar entre 0 y L-1.
                    y = rand() % L;

                    cambio = (estado[y][(x-1+L) % L] + estado[y][(x+1) % L] + estado[(y-1+L) % L][x] + estado[(y+1) % L][x])*estado[y][x];

                    // 'cambio' sólo puede tomar los valores -4, -2, 0, +2, +4.

                    if (cambio <= 0 || proba[cambio] >= (rand() / P_MAX) ){

                        estado[y][x] *= -1;

                        delta_e += cambio;
                        delta_m += estado[y][x];
                    }
                }
                param[t][0] = param[t-1][0]+2*delta_e;          // Actualiza los valores según el estado anterior y el cambio.
                param[t][1] = param[t-1][1]+2*delta_m;
            }

            //cout << "[*] TERMINAN ITERACIONES" << endl;

            guardar<int>(param, 2,    Tm, r, T, semilla);       // Guarda la magnetización y energía en cada instante de tiempo.
            //guardar<int8_t>(estado, L, L, r, T, semilla);     // Guarda el estado final del sistema. No es necesario para los ensambles.

            //cout << "[*] TERMINAN GUARDADO" << endl;

            liberaMatriz<int8_t>(estado, L);                    // Libera el espacio de memoria ocupado por el array nativo 'estado'.
            liberaMatriz<int>(param,    Tm);                    // Libera el espacio de memoria ocupado por el array nativo 'param'.
        }
        cout << "[*] FIN REPETICION " << r << endl;
    }
    cout << "[*] FIN EJECUCION" << endl;

    return 0;
}
