# -*- coding: utf-8 -*-

"""

Código utilizado para graficar la magnetización y susceptibilidad de forma independiente del tamaño L de la grilla.

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


# Primero levanta el nombre los archivos que necesita.

datos = np.empty(10, np.ndarray)
for i, L in zip(range(10), range(10,101,10)):
    datos[i] = np.loadtxt(f"procesado-{L}.txt",  delimiter = ' ').T

##############################################################################

fig, axis = plt.subplots(10,1, sharex = True, gridspec_kw={'height_ratios': np.ones(10)})

fig.set_figheight(4.3)
fig.set_figwidth(3.54) 

for i in range(10):

    L = (i+1)*10

    plt.sca(axis[i])

    plt.plot(L*(datos[i][0]-2.2692), (L**(0.125))*datos[i][5]/(L**2), color = colores[i])
    plt.ylim((0, 1.7))
    if i == 5:
        plt.ylabel(r'$\langle m\rangle\,L^{\frac{\beta}{\nu}}$', labelpad = 9)

plt.xlim((-180,180))
plt.xlabel(r'$L^{\frac{1}{\nu}}(T-T_{c})$')
plt.tight_layout(pad = 0.05)
plt.savefig("escaleo-m.png", dpi = 400)
plt.close()

##############################################################################

fig, axis = plt.subplots(10,1, sharex = True, gridspec_kw={'height_ratios': np.ones(10)})

fig.set_figheight(4.3)
fig.set_figwidth(3.54) 

for i in range(10):

    L = (i+1)*10    
    
    plt.sca(axis[i])
    plt.plot(L*(datos[i][0]-2.2692), (L**(-1.75))*(datos[i][3]-datos[i][5]**2)/(datos[i][0]*(L*L)), color = colores[i])
    plt.ylim((0, 0.06))
    if i == 5:
        plt.ylabel(r'$\chi L^{-\frac{\gamma}{\nu}}$', labelpad = 9)

plt.xlim((-20,60))
plt.xlabel(r'$L^{\frac{1}{\nu}}(T-T_{c})$')
plt.subplots_adjust(left = 0.10, right = 0.97, bottom = 0.09, top = 0.995, hspace = 0.02)
plt.tight_layout(pad = 0.05)
plt.savefig("escaleo-chi.png", dpi = 400)
plt.close()

##############################################################################

tc_s = np.empty(10)
be_s = np.empty(10)
ga_s = np.empty(10)

for i in range(10):
    L = 10*(i+1)
    for j in range(len(datos[i][0])-1):
        if datos[i][5][j]/(L*L) >= 0.5 and datos[i][5][j+1]/(L*L) <= 0.5:
            tc_s[i] = 0.5*(datos[i][0][j]+datos[i][0][j+1])
    
    #be_s[i] = np.polyfit(np.log(datos[i][0][:53]-tc_s[i])[20:], np.log(datos[i][5][:53]-0.5)[20:], deg = 1)[0]

plt.figure(figsize = (3.54,3.1), dpi = 300)

plt.plot(list(range(10,101,10)), tc_s, color = 'r')
#plt.plot(list(range(10,101,10)), be_s, color = 'b')

plt.show()