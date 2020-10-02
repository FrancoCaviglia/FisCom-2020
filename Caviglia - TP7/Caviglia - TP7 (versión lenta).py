# -*- coding: utf-8 -*-

import numpy as np
import time

def fuerza(r2):
    aux = r2**(-3)
    return 24*aux*(2*aux - 1)/r2
    
def matriz_fuerza(fn, xn, N2):
    """ No existe una copia, así que no es necesario retornan nada """
    for i in range(N2):   
        for k in range(i):
            dist = xn[i]-xn[k]
            norma2 = dist[0]*dist[0]+dist[1]*dist[1]
            fn[i][k] = fuerza(norma2)*dist  # Fuerza que siente i debido a k
            fn[k][i] = -fn[i][k]            # Matriz antisimétrica: no es necesario calcular todo

def chequea(xp, vp):    
    for pos, vel in zip(xp, vp):
        if pos[0] <= 0 or pos[0] >= L:
            vel[0] *= -1
        if pos[1] <= 0 or pos[1] >= L:
            vel[1] *= -1

### Parámetros dados ###

h  = 0.005   # Paso de tiempo
N  = 2000    # Cantidad de iteraciones (hasta t = 10)
Nc = 30 #2   # Raíz de la cantidad de átomos
L  = 55 #10  # Tamaño de la caja

### Parámetros auxiliares ###

h0 = h*h/2   # Evita calcularlo muchas veces    
h1 = h/2     # Evita calcularlo muchas veces

N2 = Nc*Nc   # Cantidad de átomos

a  = L/(Nc + 1) # Espaciado para las posiciones iniciales
v0 = 1.1        # Velocidad inicial en la dirección de x

### Iniciación números random ###

semilla = round(time.time())
np.random.seed(semilla)

### Matrices auxiliares ###

fn_0 = np.array([[0., 0.]]*N2*N2).reshape((N2, N2, 2)) # Matriz de fuerzas en instante n-1
fn_1 = np.array([[0., 0.]]*N2*N2).reshape((N2, N2, 2)) # Matriz de fuerzas en instante n

### Condiciones iniciales ###

xn = np.array([[n*a, m*a] for n in range(1, Nc+1) for m in range(1, Nc+1)]) # Este array tendrá el estado de las posiciones en cada tiempo

vn = np.array([[v, 0.] for v in np.random.choice([-v0, +v0], N2)]) # Único uso de random # Este array tendrá el estado de las posiciones en cada tiempo
#vn = np.array([[0., 0.] for v in np.random.choice([-v0, +v0], N2)]) # Único uso de random # Este array tendrá el estado de las posiciones en cada tiempo
tn = np.linspace(0, N*h, N, endpoint = False)                      # Esta lista contiene los tiempo de cada iteración

np.savetxt(f'Datos\{tn[0]:.3f}.txt', np.hstack((xn, vn)), delimiter = ' ')
#np.savetxt(f'Datos2\{tn[0]:.3f}.txt', xn, delimiter = ' ')
matriz_fuerza(fn_0, xn, N2)                                        # Calcula la fuerza en tiempo 0

for n in range(1, N):   # El paso 0 ya lo tiene

    xn += h*vn + np.sum(fn_0, axis = 1)*h0  # Crea la posición en el tiempo siguiente
    
    matriz_fuerza(fn_1, xn, N2) # fn_1 sube un nivel
    
    vn += np.sum(fn_0 + fn_1, axis = 1)*h1
    
    chequea(xn, vn)         # Corrige las velocidades según la posición de la partícula
    
    fn_0 = fn_1.copy()      # fn_0 sube un nivel a fn_1
    
    np.savetxt(f'Datos\{tn[n]:.3f}.txt', np.hstack((xn, vn)), delimiter = ' ') # Guarda el estado
   #np.savetxt(f'Datos2\{tn[n]:.3f}.txt', xn, delimiter = ' ') # Guarda el estado