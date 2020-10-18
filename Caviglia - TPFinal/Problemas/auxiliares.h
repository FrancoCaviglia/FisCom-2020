/*

C�digo auxiliar correspondiente a la entrega del Trabajo Final: Modelo de Ising

Instituto Balseiro - F�sica Computacional - Franco Caviglia

�ltima edici�n: 16-10-2020

Es necesario para compilar los c�digos con nombre Simulaci�n-PN.cpp

*/

#include <iostream>      // Incluye los objetos cin, cout, cerr, clog
#include <fstream>       // Incluye las clases ifstream, ofstream.
#include <cstdlib>       // Incluye funci�n srand() y rand().
#include <cmath>         // Permite evaluar la exponencial
#include <time.h>        // Incluye la funci�n time() y clock()
#include <random>        // Permite evaluar la exponencial
#include <iomanip>       // Permite guardar en archivos .txt valores con decimales.

using namespace std;

template<class tipo>
tipo **alocaMatriz(int nfils, int ncols) {  // Funci�n auxiliar: permite tener m�s control sobre la vida de los array

    tipo **pmat = new tipo*[nfils];         // aloca un arreglo nativo de nfils punteros a enteros

    for( int i=0; i < nfils; ++i){          // aloca cada fila de la matriz como un arreglo nativo de ncols enteros
        pmat[i]= new tipo[ncols];
    }

    return pmat;
}

template<class tipo>
void liberaMatriz(tipo **pmat, int nfils) { // Funci�n auxiliar: permite tener m�s control sobre la vida de los array

    for (int i=0; i < nfils; i++){          // primero debo liberar los elementos de pmat (filas)
        delete [] pmat[i];
    }

    delete [] pmat;                         // y finalmente libero pmat
}

template<class tipo>
void guardar(tipo *matriz[], unsigned int X, unsigned int Y, string P){  // Guarda la grilla en el estado final.

    ofstream archivo_guardar(P+".txt");
    if (archivo_guardar.is_open()) {
        for (unsigned int y = 0; y < Y; y++){
            for (unsigned int x = 0; x < X-1; x++){
                archivo_guardar << fixed << setprecision(12) << matriz[y][x] << " ";
                }
            archivo_guardar << (int)matriz[y][X-1] << endl;  // El �ltimo valor de cada columna lo castea a entero pues en general
        }                                                    // ser� la semilla.
        archivo_guardar.close();
    }
}

int energia(int8_t* estado[], unsigned int L, int J){    // Retorna la energ�a debida a la interacci�n entre espines.

    int s = 0;                                           // Inicializa la variable de la sumatoria

    for (unsigned int y = 0; y < L; y++){                // Itera y suma sobre las interacciones a lo largo de x.
        for (unsigned int x = 0; x < L-1; x++){
            s += estado[y][x]*estado[y][x+1];
        }
        s += estado[y][L-1]*estado[y][0];                // A�ade la interacci�n en el borde derecho (periodicidad).
    }

    for (unsigned int x = 0; x < L; x++){                // Itera y suma sobre las interacciones a lo largo de y.
        for (unsigned int y = 0; y < L-1; y++){
            s += estado[y][x]*estado[y+1][x];
        }
        s += estado[L-1][x]*estado[0][x];                // A�ade la interacci�n en el borde inferior(periodicidad).
    }
    return -J*s;
}

int magne(int8_t* estado[], unsigned int L){             // Retorna la magnetizaci�n como la suma de los espines.

    int m = 0;                                           // Inicializa la variable de la sumatoria.

    for (unsigned int y = 0; y < L; y++){                // Suma sobre todas las celdas.
        for (unsigned int x = 0; x < L; x++){
            m += estado[y][x];
        }
    }
    return m;
}
