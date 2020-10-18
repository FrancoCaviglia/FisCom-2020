/*

Código correspondiente a la entrega del Trabajo Final: Modelo de Ising

Instituto Balseiro - Física Computacional - Franco Caviglia

Versión "standalone" de los códigos usados para generar los datos de interés. Tanto la temperatura como el tamaño del sistema es fijo.
Al final de la ejecución guarda dos matrices con (1) la energía y magnetizacíon a cada tiempo t, (2) el estado del sistema final.

Para encontrar las versiones optimizadas para cada parte del trabajo por favor difirise a  github.com/FrancoCaviglia/FisCom-2020,
carpeta "Caviglia - TPFinal".

Última edición: 17-10-2020

*/

#include "auxiliares.h"

using namespace std;

int main(){

    /*** Parámetros y constantes ***/

    const int Tm = 10000;           // Pasos de tiempo (MCS).
    const int L  = 10;              // Tamaño de la grilla

    const int N = L*L;              // Guarda el cuadrado para no calcularlo siempre.

    const double T = 2.1            // Temperatura

    const double J  = 1.0;          // Parámetro del Hamiltoniano.
    const double kb = 1.0;          // Constante de Boltzmann.

    double proba[5];                // Espacio para las probabilidades. Se desperdician tres posiciones, pero la memoria no es tanto un problema.

    int delta_e, delta_m;           // Crea las variables donde guardar los cambios en la magnetización
    unsigned int x, y;              // Crea las coordenadas del spin que se puede o no flippear.
    int8_t cambio;                  // Parámetro proporcional al cambio en energía al flippear.

    unsigned int semilla = (clock()*time(0)) % 4000000000;  // Guarda la semilla de la secuencia random.

    proba[2] = exp(-J*2*2/(T*kb));                      // Guarda una única vez las probabilidades que son distintas de 1.
    proba[4] = exp(-J*2*4/(T*kb));

    int8_t **estado = alocaMatriz<int8_t>(L, L);        // Van a haber dos variables: el estado del sistema, y parámetros que de
    int    **param  = alocaMatriz<int>(Tm, 2);          // sobre este se computen.

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

    param[0][1] = magne(estado, L);                     // en tiempo incial. Luego usa diferencias.
    param[0][0] = energia(estado, L, J);                // Sólo calcula directamente la energía y magnetización

    for (int t = 1; t < Tm; t++){                       // 1ra. iteracción: tiempo

        delta_e = 0;
        delta_m = 0;

        for (int p = 0; p < N; p++){                    // 2da. iteracción: NxN sorteos

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
        param[t][0] = param[t-1][0]+2*J*delta_e;
        param[t][1] = param[t-1][1]+2*delta_m;
    }

    string P = "Datos/"+to_string(L)+"-"+to_string(T)+"-"+to_string(semilla);
    guardar<int>(param, 2, Tm, P);                      // Guarda la magnetización y energía en cada instante de tiempo.
    string J = "Datos/E-"+to_string(L)+"-"+to_string(T)+"-"+to_string(semilla);
    guardar<int8_t>(estado, L, L, J);                   // Guarda el estado final del sistema. No es necesario para los ensambles.

    liberaMatriz<int8_t>(estado, L);                    // Libera el espacio de memoria ocupado por el array nativo 'estado'.
    liberaMatriz<int>(param,    Tm);                    // Libera el espacio de memoria ocupado por el array nativo 'param'.

    cout << "[*] FIN EJECUCION" << endl;

    return 0;
}
