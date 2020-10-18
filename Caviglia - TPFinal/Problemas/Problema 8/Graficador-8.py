# -*- coding: utf-8 -*-

"""

Código utilizado para graficar primero la susceptibilidad magnética en presencia de campo B para L entre 5 y 20; y segundo del valor de
chi en a B = 0 con el tamaño L del sistema. De los gráficos usados, sólo el primero y el último se presentan en el Informe.

Trabajo Práctico Final de Física Computacional.

Franco Caviglia - 16/10/2020

"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=10)       
plt.rc('axes', titlesize=10)
plt.rc('axes', labelsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('legend', fontsize=10)
plt.rc('figure', titlesize=10)

T = 2.1

##### Gráfica completa ######

plt.figure(figsize = (3.54,3.1), dpi = 300)

for L, c, v in zip([  5,   6,   8,  10,  12,  15,  18,  19,  20],
                   ['m', 'b', 'royalblue', 'darkcyan', 'g', 'gold', 'orange', 'orangered', 'r'],
                   ['o', 'v', '^', '>', '<', 'h', 'p', 's', '*']):
    
    susceptibilidad = []
    magnetizacion = []
    
    datos = np.loadtxt(f"Ejecuciones/{L}-estadistica.txt", delimiter = ' ').T
    suscp = (datos[1]-datos[0]**2)/(T*L*L)
    campos_H = np.linspace(-0.1, 0.1, suscp.shape[0])

    plt.plot(campos_H, suscp, label = f"$L={L}$", marker = v, color = c, linewidth = 1, markersize = 3, alpha = 0.5)     
    
plt.xlim((-0.1,0.1))
plt.xlabel(r'\textrm{Campo externo }$B$')
plt.ylabel(r'\textrm{Susceptibilidad }$\chi$')
plt.legend()
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("chi-todos.png")
plt.show()
plt.close()

##### Gráfica parcial ######

plt.figure(figsize = (3.54,3.1), dpi = 300)

for L, c, v in zip([  5,   6,   8,  10],
                   ['m', 'b', 'royalblue', 'darkcyan'],
                   ['o', 'v', '^', '>']):
    
    susceptibilidad = []
    magnetizacion = []
    
    datos = np.loadtxt(f"Ejecuciones/{L}-estadistica.txt", delimiter = ' ').T
    suscp = (datos[1]-datos[0]**2)/(T*L*L)
    campos_H = np.linspace(-0.1, 0.1, suscp.shape[0])

    plt.plot(campos_H, suscp, label = f"$L={L}$", marker = v, color = c, linewidth = 1, markersize = 3, alpha = 0.5)     
    
plt.xlim((-0.1,0.1))
plt.xlabel(r'\textrm{Campo externo }$B$')
plt.ylabel(r'\textrm{Susceptibilidad }$\chi$', labelpad = 9)
plt.legend()
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("chi-chicos.png")
plt.show()
plt.close()

##### Gráfica L^2 ######

Ls = []
Cs = []

plt.figure(figsize = (3.54,3.1), dpi = 300)

for L, v in zip([  5,   6,   8,  10,  12,  15,  18,  19,  20],
                ['o', 'v', '^', '>', '<', 'h', 'p', 's', '*']):
    
    datos = np.loadtxt(f"Ejecuciones/{L}-estadistica.txt", delimiter = ' ').T
    suscp = (datos[1]-datos[0]**2)/(T*L*L)
    chi_max = suscp.max()
    
    plt.scatter(L, chi_max, color = 'b', marker = v)
    Ls.append(L)
    Cs.append(chi_max)
    
plt.plot(np.linspace(0,20,50), 0.356*np.linspace(0,20,50)**2, label = r"$\propto\, L^{2}$", color = 'm')

plt.xlim((0,21))
plt.legend()
plt.xlabel(r"\textrm{Tamaño lado }$L$")
plt.ylabel(r"\textrm{Susceptibilidad }$\chi(H=0)$")
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("chi-L2.png")
plt.show()
plt.close()

np.polyfit(np.log(Ls), 2*np.log(Cs), deg = 2)