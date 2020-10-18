# -*- coding: utf-8 -*-

"""

Código utilizado para graficar la magnetización y susceptibilidad por partícula en función de la temperaturas para L = 100 y barrido fino.

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

temperaturas = np.arange(2.0, 2.501, 0.005)

datos = np.loadtxt("promedio-2.txt", delimiter = ' ')/(100*100)
valores_1 = (datos[3] - datos[0]**2)/temperaturas
valores_2 = (datos[3] - datos[2]**2)/temperaturas

plt.figure(figsize = (3.54, 2.9), dpi = 300)

plt.plot(temperaturas, valores_1, color = 'r', alpha = 0.5, linewidth=2, label = r'\textrm{Curva numérica}')
plt.plot(temperaturas, 123+abs(2.2782597107541385-temperaturas)**(-1.76), color = 'b', alpha = 0.5, linewidth=2, label = r"\textrm{Ajuste}")
plt.xlim((2.0,2.5))
plt.ylim((0,500))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Susceptibilidad }$\chi$', labelpad = 9)
plt.legend()
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("100-fino-chi.png")
plt.show()
plt.close()

##############################################################################

plt.figure(figsize = (3.54, 2.9), dpi = 300)

plt.plot(temperaturas, datos[0], color = 'r', alpha = 0.5, linewidth=2, label = r"\textrm{Promedio con ensamble}")
plt.plot(temperaturas[:57], 0.4+0.62*(2.2647-temperaturas[:57])**(0.19), color = 'b', label = r"\textrm{Ajuste }$|T_{c}-T|^{\beta}$")
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Magnetzación }$\langle|m|\rangle$', labelpad = 9)
plt.legend()
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("100-fino-m.png")
plt.show()
plt.close()

#plt.plot(2.2782597107541385-temperaturas, datos[0], color = 'r', alpha = 0.5, linewidth=2, label = r"\textrm{Promedio con ensamble}$")
derivada = np.gradient(datos[0], 0.005)
for T, V, D in zip(temperaturas, datos[0], derivada):
    print(T,V,D)

"""
plt.plot(temperaturas, 100000*(datos[1]**2)/temperaturas, color = 'b')
plt.plot(temperaturas, 100000*(datos[2]**2)/temperaturas, color = 'r')
plt.plot(temperaturas, abs(temperaturas-2.29)**(-7/4), color = 'g')

#plt.scatter(temperaturas, abs(2.277-temperaturas)**(1/8), color = 'r')
plt.show()

plt.figure(dpi = 100)
plt.plot(np.log(abs(temperaturas-2.277)), np.log((datos[1]**2)/temperaturas), color = 'g')
plt.plot(np.log(abs(temperaturas-2.277)), -(7/4)*np.log(abs(2.277-temperaturas)), color = 'r')
plt.show()

#np.polyfit(np.log(temperaturas)[60:],  np.log((datos[2]**2)/temperaturas)[60:], 1)


plt.figure(dpi = 100)
plt.scatter(temperaturas, abs(2.277-temperaturas)**(1/8), color = 'b')
plt.show()

plt.figure(dpi = 100)
plt.scatter(np.log(2.277-temperaturas[:52])[22:], np.log(datos[0][:52])[22:], color = 'r')
plt.show()

plt.figure(dpi = 100)
#plt.scatter(temperaturas, datos[0], color = 'b')
plt.plot(temperaturas, 0.5+(2.25-temperaturas)**(1/8), color = 'r')
plt.show()

plt.figure(dpi = 100)
plt.scatter(temperaturas[53:69], datos[0][53:69], color = 'b')
plt.show()

plt.figure(dpi = 100)
plt.scatter(log(temperaturas[53:69]), np.log(datos[0][53:69]-0.5), color = 'r')
plt.show()

numpy.polyfit(temperaturas[53:69], np.log(datos[0][53:69]-0.5), 1)

plt.figure(dpi = 100)
plt.plot(temperaturas, np.log(datos[1]))
plt.show()
"""