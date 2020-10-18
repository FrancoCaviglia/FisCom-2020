# -*- coding: utf-8 -*-

"""

Código utilizado para graficar el estado de la energía y magnetización por partícula del sistema en cada instante de tiempo.

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

infile = open("datos.txt", 'r')
l_nombres = []
for line in infile:
    l_nombres.append("Datos/"+line[:-1])
infile.close()

for i, c in zip(range(0,4,2), [['m','r'], ['b','c']]):
    
    L = int(l_nombres[i][6:8])
    
    fig, (ax_1, ax_2) = plt.subplots(2,1, sharex = True, gridspec_kw={'height_ratios': [1, 1]})
    
    fig.set_figheight(3.1)
    fig.set_figwidth(3.51)        
    
    for j, T in zip([0,1], [2.1, 2.5]):
        
        datos = (np.loadtxt(l_nombres[i+j], delimiter = ' ')/(L*L)).T
            
        plt.sca(ax_1)
        plt.plot(list(range(len(datos[1]))), datos[1], color = c[j], linewidth=0.2,alpha = 0.7, label = rf'$T={T}$')
        plt.sca(ax_2)
        plt.plot(list(range(len(datos[0]))), datos[0], color = c[j], linewidth=0.2, alpha = 0.7, label = rf'$T={T}$')
                        
    plt.sca(ax_1)
    plt.ylabel(r'\textrm{Magnetización }$M/L^{2}$')
    plt.ylim((-1,1))
    
    plt.sca(ax_2)
    plt.xlabel(r'\textrm{Tiempo (MCS) }$t$')
    plt.ylabel(r'\textrm{Energía }$E/L^{2}$')
    plt.legend(loc = 'upper right')
    plt.ylim((-2,0))
    
#    plt.tight_layout(pad = 0.1)
    plt.xlim((-100,len(datos[1])))
    
    plt.subplots_adjust(left = 0.16, right = 0.95, bottom = 0.13, top = 0.98, hspace = 0.1)
    plt.savefig(f"evolucion-{L}.png", dpi = 600)
    plt.show()
    plt.close()

"""


fig, ax = plt.subplots(3,3)

fig.set_figheight(7)
fig.set_figwidth(7)

#          ["G-1.550000-0-1477782780.txt", ax[2][0]],

for x in [["G-1.450000-1-1312934972.txt", ax[0][0]],
          ["G-1.500000-0-1477982928.txt", ax[1][0]],
          ["G-2.300000-0-1600899119.txt", ax[0][1]],
          ["G-2.350000-0-1600899063.txt", ax[1][1]],
          ["G-2.400000-0-1341117432.txt", ax[2][1]],
          ["G-4.400000-0-503344376.txt",  ax[0][2]],
          ["G-5.000000-0-503344376.txt",  ax[1][2]],
          ["G-5.600000-0-503344376.txt",  ax[2][2]]]:
    
    estado = np.loadtxt(x[0], delimiter = ' ')
    plt.sca(x[1])
    plt.imshow(estado, cmap = 'binary', vmin = -1, vmax = 1, extent = [0, 128, 0, 128])
    plt.xticks([])
    plt.yticks([])
    #plt.xlabel(r'\textrm{Coordenada }$x$')
    #plt.ylabel(r'\textrm{Coordenada }$y$')

estado = np.loadtxt("G-1.550000-0-1477782780.txt", delimiter = ' ')
plt.sca(ax[2][0])
plt.imshow(estado, cmap = 'binary', vmin = -1, vmax = 1, extent = [0, 128, 0, 128])
plt.xticks([0, 32, 64, 96, 128])
plt.yticks([0, 32, 64, 96, 128])
    
plt.subplots_adjust(hspace = 0, wspace = 0)
plt.tight_layout(pad = 0.18)
plt.savefig("estados.png", dpi = 600)
plt.show()
plt.close()
"""
"""
estado = np.loadtxt("energias.txt", delimiter = ' ')
c_calor = []
for elem, T in zip(estado, np.linspace(1, 4, 150, endpoint = False)):
    c_calor.append((elem/T)**2)
plt.figure(dpi = 300)
plt.plot(np.linspace(1, 4, 150, endpoint = False), c_calor)
plt.xlim((1,4))
plt.show()

plt.figure(dpi = 300)
plt.plot(np.linspace(1, 4, 150, endpoint = False), estado)
plt.xlim((1,4))
plt.show()
"""
"""
estado = np.loadtxt("fases.txt", delimiter = ' ')
c_calor = []
for elem, T in zip(estado, np.linspace(1, 4, 150, endpoint = False)):
    c_calor.append((elem/T)**2)
plt.figure(dpi = 300)
plt.plot(np.linspace(1, 4, 150, endpoint = False), c_calor)
plt.xlim((1,4))
plt.show()

plt.figure(dpi = 300)
plt.plot(np.linspace(1, 4, 150, endpoint = False), estado)
plt.xlim((1,4))
plt.show()

estado = np.loadtxt("fases.txt", delimiter = ' ')
plt.figure(dpi = 300)
plt.plot(np.linspace(1, 4, 150, endpoint = False), estado[1])
plt.xlim((1,4))
plt.show()

estado = np.loadtxt("magneto.txt", delimiter = ' ')
plt.figure(dpi = 300)
plt.scatter(estado[0], estado[1], s = 0.5, alpha = 0.2)
plt.xlim((1,4))
plt.show()
"""