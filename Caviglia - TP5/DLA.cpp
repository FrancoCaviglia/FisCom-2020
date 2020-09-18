#include <iostream>      // Incluye los objetos cin, cout, cerr, clog
#include <fstream>       // Incluye las clases ifstream, ofstream.
#include <cstdlib>       // Incluye función srand() y rand().
#include <thread>        // Incluye la opción de ejecutar en varios hilos a la vez.
#include <time.h>        // Para la semilla

using namespace std;

/* Alocacíon Dinámica de Memoria: código tomado de las clases de ICOM. */

int **alocaMatriz_int(int nfils, int ncols) {
    // aloco un arreglo nativo de nfils punteros a enteros
    int **pmat = new int*[nfils];
    // aloco cada fila de la matriz como un arreglo nativo de ncols enteros
    for( int i=0; i < nfils; ++i)
        pmat[i]= new int[ncols];
    return pmat;
}
void liberaMatriz_int(int **pmat, int nfils) {
    // primero debo liberar los elementos de pmat (filas)
    for( int i=0; i < nfils; i++)
    delete [] pmat[i];
    // y finalmente libero pmat
    delete [] pmat;
}

void caminar(int *caminan[], int L, int N){

    /* Toma la lista con los caminantes y los hace moverse un paso en una
    de las 8 posiciones adyacentes. */

    for(int k = 0; k < N; k++){
        if(caminan[k][2]){
            int R = rand() % 8;
            switch(R){
                case 0:
                    caminan[k][0] = (caminan[k][0]+1) % L;
                    break;
                case 1:
                    caminan[k][0] = (caminan[k][0]-1+L) % L;
                    break;
                case 2:
                    caminan[k][1] = (caminan[k][1]+1) % L;
                    break;
                case 3:
                    caminan[k][1] = (caminan[k][1]-1+L) % L;
                    break;
                case 4:
                    caminan[k][0] = (caminan[k][0]+1) % L;
                    caminan[k][1] = (caminan[k][1]+1) % L;
                    break;
                case 5:
                    caminan[k][0] = (caminan[k][0]+1) % L;
                    caminan[k][1] = (caminan[k][1]-1+L) % L;
                    break;
                case 6:
                    caminan[k][0] = (caminan[k][0]-1+L) % L;
                    caminan[k][1] = (caminan[k][1]+1) % L;
                    break;
                case 7:
                    caminan[k][0] = (caminan[k][0]-1+L) % L;
                    caminan[k][1] = (caminan[k][1]-1+L) % L;
                    break;
            }
        }
    }
}

void revisar(int* camin[], int* grilla[], int L, int N, int t){

    /* Revisa si hay al lado de cada caminante una celda pertenenciante al agregado. */

    for(int k = 0; k < N; k++){
        if(camin[k][2]){
            int x_m = (camin[k][0] - 1 + L) % L;
            int x_p = (camin[k][0] + 1) % L;
            int y_m = (camin[k][1] - 1 + L) % L;
            int y_p = (camin[k][1] + 1) % L;

            if( grilla[x_m][y_m]         || grilla[camin[k][0]][y_m] || grilla[x_p][y_m] ||
                grilla[x_m][camin[k][1]] ||                             grilla[x_p][camin[k][1]] ||
                grilla[x_m][y_p]         || grilla[camin[k][0]][y_p] || grilla[x_p][y_p] ){
                grilla[camin[k][0]][camin[k][1]] = t;      // En general se fijará t = 1, salvo cuando se quiera
                camin[k][2] = 0;                           // graficar con información del tiempo.
            }
        }
    }
}

int main(){//(int R, int th){

    const int L = 2048;              // Tamaño de la grilla
    const int N = 180000;            // Cantidad inicial de caminantes
    const int T = 6000000;           // Pasos de tiempo
    const int R = 1;                 // Repeticiones del proceso

    const time_t semilla = time(0);  // Semilla de tiempo

    const int n = N/2;               // Divide la cantidad de caminantes. Según la compu esto puede
                                     // el equipo esto puede mejorarse.

    srand(semilla);                  // Semilla para los números random

    for(int r = 0; r < R; r++){

        int **grilla = alocaMatriz_int(L, L);

        int **caminantes_1 = alocaMatriz_int(n, 3);
        int **caminantes_2 = alocaMatriz_int(n, 3);

        for (int i = 0; i < L; i++){            // Establece los valores iniciales de la grilla
            for (int j = 0; j < L; j++){
                grilla[i][j] = 0;
            }
        }

        grilla[L/2][L/2] = 1;                   // Semilla para el agregado ubicada en el centro.

        cout << "[*] CREO GRILLA " << endl;

       for (int k = 0; k < n; k++){            // Valores iniciales de los caminantes
            caminantes_1[k][0] = rand() % L;
            caminantes_1[k][1] = rand() % L;
            caminantes_1[k][2] = 1;

            caminantes_2[k][0] = rand() % L;
            caminantes_2[k][1] = rand() % L;
            caminantes_2[k][2] = 1;
        }

        cout << "[*] CREO CAMINANTES " << endl;

        for (int t = 2; t < T; t++){           // Bucle temporal

            thread hilo_1(caminar, caminantes_1, L, n);
            thread hilo_2(caminar, caminantes_2, L, n);

            hilo_1.join();
            hilo_2.join();

            revisar(caminantes_1, grilla, L, n, t);
            revisar(caminantes_2, grilla, L, n, t);

            cout << t << endl;

        }

        cout << "[*] TERMINO" << endl;

        ofstream archivo_guardar("Dendritas/"+to_string(L)+"-"+to_string(r)+".txt");     // Guarda la grilla en el estado final.
        if(archivo_guardar.is_open()) {
            for (int i = 0; i < L; i++){
                for (int j = 0; j < L-1; j++){
                    archivo_guardar << grilla[i][j] << " ";
                }
                archivo_guardar << grilla[i][L-1] << endl;
            }
            archivo_guardar.close();
        }

        else{cout << "[+] ERROR AL GUARDAR GRILLA" << endl;}

        liberaMatriz_int(grilla, L);            // Libera el espacio de memoria ocupado por la grilla.
        liberaMatriz_int(caminantes_1, n);      // Libera el espacio de memoria ocupado por los caminantes (1).
        liberaMatriz_int(caminantes_2, n);      // Libera el espacio de memoria ocupado por los caminantes (2).

        cout << "[*] FIN EJECUCION" << endl;
    }

    return 0;
}
