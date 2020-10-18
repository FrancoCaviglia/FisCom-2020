# -*- coding: utf-8 -*-

"""

Código utilizado para graficar la energía, magnetización, capacidad calorífica y susceptibilidad por partícula en función de la temperaturas.

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

colores = plt.cm.jet(np.linspace(0,1,10))

datos = np.empty(10, np.ndarray)
for i, L in zip(range(10), range(10,101,10)):
    datos[i] = np.loadtxt(f"procesado-{L}.txt",  delimiter = ' ').T

""" Magnetización """

plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    plt.plot(datos[i][0], datos[i][5]/((10*(i+1))**2), color = colores[i])
    
plt.xlim((0.5,5.0))
plt.ylim((-0.04, 1.04))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Magnetización }$\langle m\rangle$', labelpad = 8)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("magnetizacion-todos.png")
plt.show()
plt.close()

""" Energía """

plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    plt.plot(datos[i][0], datos[i][2]/((10*(i+1))**2), color = colores[i])
    
plt.xlim((0.5,5.0))
plt.ylim((-2, -0.3))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Energía }$\langle e\rangle$', labelpad = 8)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("energia-todos.png")
plt.show()
plt.close()

""" Susceptibilidad """

plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    plt.plot(datos[i][0], (datos[i][3]-datos[i][1]**2)/(datos[i][0]*((10*(i+1))**2)), color = colores[i])
    
plt.xlim((0.5,5.0))
plt.ylim((0,150))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Susceptibilidad }$\chi$', labelpad = 9)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("susceptibilidad.png")
plt.show()
plt.close()


plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    plt.plot(datos[i][0], (datos[i][3]-datos[i][5]**2)/(datos[i][0]*((10*(i+1))**2)), color = colores[i])
    
plt.xlim((2.0,5.0))
plt.ylim((0,150))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Susceptibilidad }$\chi$', labelpad = 9)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("susceptibilidad-mod.png")
plt.show()
plt.close()

""" Capacidad calorífica """

plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    plt.plot(datos[i][0], (datos[i][4]-datos[i][2]**2)/((datos[i][0]*(10*(i+1)))**2), color = colores[i])
    
plt.xlim((0.5,5.0))
plt.ylim((0,3))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Capacidad calorífica }$\chi$', labelpad = 9)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("capacidad.png")
plt.show()
plt.close()
    
    