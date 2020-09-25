# -*- coding: utf-8 -*-

"""

Código correspondiente al Problema 1 del Trabajo Práctico N°6 de Física Computacional. 

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

# Guarda una lista con los nombres de los archivos con M y E.
infile = open("nombres.txt", 'r')
l_nombres = []
for line in infile:
    if line[:2] == 'D-':
        l_nombres.append(line[:-1])
infile.close()

# Itera sobre las temperaturas
temperaturas = np.arange(0.5, 5, 0.04)
ca_calorifica = []
magnetizacion = []
e_magnetizacion = []

for T in temperaturas:
    estado = []
    magnet = []
    for nombre in l_nombres:
        if nombre[:6] == f"D-{T:0.2f}":
            datos = np.loadtxt("TODO/"+nombre, delimiter = ' ').T
            magnet.append(abs(datos[1][9999])/4096)
            estado.append(np.array(datos[0][-500:]).std()/4096)

    magnetizacion.append(np.array(magnet).std())
    e_magnetizacion.append(np.array(magnet).mean())
    ca_calorifica.append((np.array(estado).std()/T)**2)


plt.figure(dpi = 300, figsize = (4,3))
plt.plot(temperaturas, ca_calorifica, color = 'b')
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Capacidad calorífica }$C_{p}$')
plt.xlim((0.5,5))
plt.tight_layout()
plt.savefig("ca_calorifica.png")
plt.show()
plt.close()

plt.figure(dpi = 300, figsize = (4,3))
plt.errorbar(temperaturas, magnetizacion, e_magnetizacion, color = 'b')
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Magnetización }$\langle|M|\rangle$')
plt.xlim((0.5,5))
plt.tight_layout()
plt.savefig("magnetizacion.png")
plt.show()
plt.close()

