# -*- coding: utf-8 -*-

"""

Código utilizado para graficar primero los histogramas con la distribución de magnetización en el equilibrio para L = 10, ..., 100; segundo
las energías libres efectivas F_L y tercero la dependencia de la barrera de energía \Delta F_L con el tamaño L de la grilla.

Trabajo Práctico Final de Física Computacional.

Franco Caviglia - 16/10/2020

"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=9)       
plt.rc('axes', titlesize=9)
plt.rc('axes', labelsize=9)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('legend', fontsize=9)
plt.rc('figure', titlesize=9)

temperaturas = np.arange(0.5, 5.0, 0.02)

infile = open("Problema-7.txt", 'r')
l_nombres = []
for line in infile:
    l_nombres.append(line[:-1])
infile.close()

def fabrica_histograma(datos, L):
    
    ancho = 2/(L*L)
    limites    = np.round(np.arange(-L*L, L*L+1, 2)/(L*L), 12)                    
    histograma = np.zeros(L*L+1)

    for j in range(L*L+1):
        histograma[j] = np.count_nonzero(datos == limites[j])
    
    histograma /= ancho*datos.shape[0] 

    return limites, histograma, ancho

kb = 1 

for L in range(5, 16):
    for T in [1.6, 2.1, 2.5, 3.0]:
        for nombre in l_nombres:
            if nombre[:6] == f"{L}-{T:.2f}" or nombre[:7] == f"{L}-{T:.2f}":
                
                datos = np.round(np.loadtxt("Ejecuciones/"+nombre, delimiter = ' ').T[1][100000:]/(L*L),10)

                limites, histograma, ancho = fabrica_histograma(datos, L)

                plt.figure(figsize = (2.42,2.4), dpi = 300)
                plt.bar(x = limites, height = histograma, label = rf'$L={L},\ T={T}$', width = 0.86*ancho, alpha = 0.8, color = 'b')
                plt.xlim((-1-3*ancho/4,1+3*ancho/4))
                if T == 3.0:
                    plt.legend(loc = 'best')
                else:
                    plt.legend(loc = 'upper center')
                plt.xlabel(r'\textrm{Magnetización }$m$')
                plt.ylabel(r'\textrm{Densidad de probabilidad}')
                plt.tight_layout(pad = 0.04)
                plt.savefig(f"histograma-{L}-{T}.png")
                plt.show()

for L in range(5, 16):
    
    plt.figure(figsize = (3.54,3.1), dpi = 300)

    for T in [2.1, 2.5, 3.0]:
        for nombre in l_nombres:
            if nombre[:6] == f"{L}-{T:.2f}" or nombre[:7] == f"{L}-{T:.2f}":
                
                datos = np.round(np.loadtxt("Ejecuciones/"+nombre, delimiter = ' ').T[1][100000:]/(L*L), 12)

                limites, histograma, _ = fabrica_histograma(datos, L)

                plt.plot(limites, -kb*T*np.log(histograma), label = rf'$L={L},\ T={T}$')
    
    plt.xlim((-1,1))
    plt.legend(loc = 'upper center')
    plt.xlabel(r'\textrm{Magnetización }$m$')
    plt.ylabel(r'\textrm{Energía libre }$F_{L}$')
    plt.tight_layout(pad = 0.05)
    plt.savefig("FL-10.png")
    plt.show()

for T in [2.1]:    

    deltas_F = []
    
    plt.figure(figsize = (3.54,3.1), dpi = 300)

    for L in range(5, 17):
        for nombre in l_nombres:
            if nombre[:6] == f"{L}-{T:.2f}" or nombre[:7] == f"{L}-{T:.2f}":
                
                datos = np.round(np.loadtxt("Ejecuciones/"+nombre, delimiter = ' ').T[1][100000:]/(L*L), 12)
                
                limites, histograma, _ = fabrica_histograma(datos, L)
                
                plt.plot(limites, -kb*T*np.log(histograma), label = rf'$L={L}$')
                
                P_ms = (histograma[:histograma.size//2].max() + histograma[histograma.size//2:].max())/2
                P_0 = histograma[L*L//2] if not L % 2 else 0.5*(histograma[L*L//2]+histograma[L*L//2+1])
                
                deltas_F.append(-kb*T*np.log(P_0)-(-kb*T*np.log(P_ms)))
                
    plt.xlim((-1,1))
    plt.legend(loc = 'upper center', ncol=2)
    plt.xlabel(r'\textrm{Magneización }$m$')
    plt.ylabel(r'\textrm{Energía libre }$F_{L}$')
    plt.tight_layout(pad = 0.05)
    plt.savefig(f"varios-L-FL-{T}.png")
    plt.show()

    plt.figure(figsize = (3.54,3.1), dpi = 300)
    plt.plot(list(range(5,18)), deltas_F, color = 'b')
    plt.xlim((4,18))
    plt.legend(loc = 'upper center')
    plt.xlabel(r'\textrm{Tamaño lado }$L$')
    plt.ylabel(r'\textrm{Diferencia energía libre }$\Delta F_{L}$')
    plt.tight_layout(pad = 0.05)
    plt.savefig(f"varios-L-FL-{T}.png")
    plt.show()