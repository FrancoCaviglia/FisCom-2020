/*

Código correspondiente a la entrega del Trabajo Final: Modelo de Ising

Instituto Balseiro - Física Computacional - Franco Caviglia


Última edición: 16-10-2020
*/

#include "auxiliares.h"

using namespace std;

int main(){

    /*** Parámetros y constantes ***/

    const int Tm = 25000000;        // Pasos de tiempo, fijo.

    const double J  = 1.0;          // Parámetro del Hamiltoniano.
    const double kb = 1.0;          // Constante de Boltzmann.

    const double T = 2.1;           // Temperatura.

    long double proba[3][5];        // Espacio para las probabilidades. Se desperdician tres posiciones, pero la memoria no es tanto un problema.

    int delta_m;                    // Crea las variables donde guardar los cambios en la magnetización
    int x, y;                       // Inicializa las coordenadas del spin que se puede o no flippear.
    int8_t cambio;                  // Parámetro proporcional al cambio en energía al flippear.
    long double H;

    int N;

    /*** Ciclos anidados ***/
    for (int L : {5, 6, 7, 8, 10, 12, 15, 18, 19, 20}){                            // 1er. iteración: tamaño de la grilla

        N = L*L;                                                  // Guarda el cuadrado para no calcularlo siempre.

        long double **estadistica = alocaMatriz<long double>(101, 3);          // sobre este se computen.
        long double magnet;                               // sobre este se computen.

        for (int i = 0; i < 101; i++){                        // Establece los valores iniciales de la grilla
            for (int j = 0; j < 3; j++){
                estadistica[i][j] = 0;                       // Posibles valores random -1 y +1.
            }
        }

        for (int k = 0; k < 101; k++){                     // 2da. iteración: campo magnético

            H = -0.1 + k*0.002;

            unsigned int semilla = time(0) % 400000000;   // Guarda la semilla de la secuencia random.

            proba[0][0] = exp(-2*(J*0-H)/(T*kb));                      // Probabilidades si el spin a flipar es -1.
            proba[0][2] = exp(-2*(J*2-H)/(T*kb));               // Guarda una única vez las probabilidades que son distintas de 1.
            proba[0][4] = exp(-2*(J*4-H)/(T*kb));

            proba[2][0] = exp(-2*(J*0+H)/(T*kb));                    // Probabilidades si el spin a flipar es +1.
            proba[2][2] = exp(-2*(J*2+H)/(T*kb));                      // Guarda una única vez las probabilidades que son distintas de 1.
            proba[2][4] = exp(-2*(J*4+H)/(T*kb));

            int8_t **estado = alocaMatriz<int8_t>(L, L);        // Van a haber dos variables: el estado del sistema, y parámetros que de

            mt19937 rg(semilla);                                // Utiliza la semilla para inicializar los números random.

            uniform_int_distribution<int> rand_int(0, 1);       // Para la condición inicial
            uniform_int_distribution<int> rand_int_L(0, L-1);   // Para elegir el punto en el paso de MC
            uniform_real_distribution<long double> rand_real(0.0, 1.0); // Para decidir en el paso de MC

            for (int i = 0; i < L; i++){                        // Establece los valores iniciales de la grilla
                for (int j = 0; j < L; j++){
                    estado[i][j] = 2*rand_int(rg)-1;          // Posibles valores random -1 y +1.
                }
            }

            magnet = magne(estado, L);                  // en tiempo incial. Luego usa diferencias.

            for (int t = 1; t < Tm; t++){                    // 3da. iteracción: tiempo

                delta_m = 0;

                for (int p = 0; p < N; p++){                // 4da. iteracción: NxN sorteos

                    x = rand_int_L(rg);                             // Toma la coordenada del punto al azar entre 0 y L-1.
                    y = rand_int_L(rg);

                    cambio = (estado[y][(x-1+L) % L] + estado[y][(x+1) % L] + estado[(y-1+L) % L][x] + estado[(y+1) % L][x])*estado[y][x];

                    // 'cambio' sólo puede tomar los valores -4, -2, 0, +2, +4.

                    if (cambio < 0 || proba[estado[y][x]+1][cambio] >= rand_real(rg) ){

                        estado[y][x] *= -1;     // En el rango de H usado, no el signo de Delta E aun depende sólo de los vecinos.

                        delta_m += estado[y][x];
                    }
                }
                magnet += 2*delta_m;

                if (t > 100000){
                    estadistica[k][0] += magnet;
                    estadistica[k][1] += magnet*magnet;
                }
            }
            estadistica[k][0] /= (Tm-100000);
            estadistica[k][1] /= (Tm-100000);
            estadistica[k][2] = (long double)semilla;

            liberaMatriz<int8_t>(estado, L);                    // Libera el espacio de memoria ocupado por el array nativo 'estado'.
        }

        string P = "Ejecuciones/"+to_string(L)+"-estadistica";

        guardar<long double>(estadistica, 3, 101, P);       // Guarda la magnetización y energía en cada instante de tiempo.

        cout << "[*] FIN ITERLACIÓN L=" << L << endl;
    }
    return 0;
}
