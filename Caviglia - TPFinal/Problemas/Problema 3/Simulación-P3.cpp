/*

Código correspondiente a la entrega del Trabajo Final: Modelo de Ising

Instituto Balseiro - Física Computacional - Franco Caviglia

Última edición: 16-10-2020

*/

#include "auxiliares.h"

using namespace std;

int main(){

    /*** Parámetros y constantes ***/

    const int Tm = 50000;           // Pasos de tiempo (MCS).
    const int R  = 500;             // Repeticiones del proceso

    const double J  = 1.0;          // Parámetro del Hamiltoniano.
    const double kb = 1.0;          // Constante de Boltzmann.

    const double Tmin = 0.50;       // Temperatura mínima.
    const double Tmax = 2.21;       // Temperatura máxima.
    const double T_paso = 0.02;     // Paso en las iteraciones sobre la temperatura

    double proba[5];                // Espacio para las probabilidades. Se desperdician tres posiciones, pero la memoria no es tanto un problema.

    int delta_e, delta_m;           // Crea las variables donde guardar los cambios en la magnetización
    unsigned int x, y;              // Crea las coordenadas del spin que se puede o no flippear.
    int8_t cambio;                  // Parámetro proporcional al cambio en energía al flippear.

    /*** Ciclos anidados ***/

    int L = 20;
    const int N = L*L;              // Guarda el cuadrado para no calcularlo siempre.

    for (double T = Tmin; T <= Tmax; T += T_paso){        // 3ra. iteración: temperatura

        long double **estadistica = alocaMatriz<long double>(R, 6);                            // sobre este se computen.

        for (unsigned int i = 0; i < R; i++){                        // Establece los valores iniciales de la grilla
            for (unsigned int j = 0; j < 6; j++){
                estadistica[i][j] = 0;            // Posibles valores random -1 y +1.
            }
        }

        for (int r = 0; r < R; r++){                              // 2da. iteración: repeticiones

            unsigned int semilla = (clock()*time(0)) % 4000000000;  // Guarda la semilla de la secuencia random.

            proba[2] = exp(-J*2*2/(T*kb));                      // Guarda una única vez las probabilidades que son distintas de 1.
            proba[4] = exp(-J*2*4/(T*kb));

            int8_t **estado = alocaMatriz<int8_t>(L, L);        // Van a haber dos variables: el estado del sistema, y parámetros que de
            int   param[2] = {0,0};                            // sobre este se computen.

            /* Inicializa lo referente a los números aleatorios */

            mt19937 rg(semilla);                                // Utiliza la semilla para inicializar los números random.

            uniform_int_distribution<int> rand_int(0, 1);       // Para la condición inicial
            uniform_int_distribution<int> rand_int_L(0, L-1);   // Para elegir el punto en el paso de MC
            uniform_real_distribution<long double> rand_real(0.0, 1.0); // Para decidir en el paso de MC

            for (unsigned int i = 0; i < L; i++){                        // Establece los valores iniciales de la grilla
                for (unsigned int j = 0; j < L; j++){
                    estado[i][j] = 2*rand_int(rg)-1;            // Posibles valores random -1 y +1.
                }
            }

            param[0] = energia(estado, L, J);                // Sólo calcula directamente la energía y magnetización
            param[1] = magne(estado, L);                     // en tiempo incial. Luego usa diferencias.

            int Tmp = Tm - 5000;

            for (int t = 1; t < Tmp; t++){                    // 3da. iteracción: tiempo

                delta_e = 0;
                delta_m = 0;

                for (int p = 0; p < N; p++){                // 4da. iteracción: NxN sorteos

                    x = rand_int_L(rg);                             // Toma la coordenada del punto al azar entre 0 y L-1.
                    y = rand_int_L(rg);

                    cambio = (estado[y][(x-1+L) % L] + estado[y][(x+1) % L] + estado[(y-1+L) % L][x] + estado[(y+1) % L][x])*estado[y][x];

                    // 'cambio' sólo puede tomar los valores -4, -2, 0, +2, +4.

                    if (cambio <= 0 || proba[cambio] >= rand_real(rg) ){

                        estado[y][x] *= -1;

                        delta_e += cambio;
                        delta_m += estado[y][x];
                    }
                }
                param[0] += 2*J*delta_e;
                param[1] += 2*delta_m;
            }

            for (int t = 0; t < 5000; t++){                    // 3da. iteracción: tiempo

                delta_e = 0;
                delta_m = 0;

                for (int p = 0; p < N; p++){                // 4da. iteracción: NxN sorteos

                    x = rand_int_L(rg);                             // Toma la coordenada del punto al azar entre 0 y L-1.
                    y = rand_int_L(rg);

                    cambio = (estado[y][(x-1+L) % L] + estado[y][(x+1) % L] + estado[(y-1+L) % L][x] + estado[(y+1) % L][x])*estado[y][x];

                    if (cambio <= 0 || proba[cambio] >= rand_real(rg) ){

                        estado[y][x] *= -1;

                        delta_e += cambio;
                        delta_m += estado[y][x];
                    }
                }
                param[0] += 2*J*delta_e;
                param[1] += 2*delta_m;

                estadistica[r][0] += param[0];
                estadistica[r][1] += param[0]*param[0];
                estadistica[r][2] += param[1];
                estadistica[r][3] += abs(param[1]);
                estadistica[r][4] += param[1]*param[1];
            }

            estadistica[r][0] /= 5000;
            estadistica[r][1] /= 5000;
            estadistica[r][2] /= 5000;
            estadistica[r][3] /= 5000;
            estadistica[r][4] /= 5000;
            estadistica[r][5] = semilla;

            liberaMatriz<int8_t>(estado, L);                    // Libera el espacio de memoria ocupado por el array nativo 'estado'.
        }

        string P = to_string(L)+"/"+to_string(T);
        guardar<long double>(estadistica, 6, R, P);                      // Guarda la magnetización y energía en cada instante de tiempo.
        liberaMatriz<long double>(estadistica, R);                    // Libera el espacio de memoria ocupado por el array nativo 'param'.
        cout << "[*] FIN REPETICION " << T << endl;
    }
    cout << "[*] FIN EJECUCION" << endl;
    return 0;
}
