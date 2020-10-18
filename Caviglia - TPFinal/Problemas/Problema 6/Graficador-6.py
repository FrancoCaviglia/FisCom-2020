# -*- coding: utf-8 -*-

"""

Código utilizado para graficar el cumulante de Binder para L = 10, ..., 100 como función primero de la temperatura y luego de L^(1/nu)(T-T_c). 

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

##############################################################################

plt.figure(figsize = (3.54, 2.9), dpi = 300)

for i in range(10):
    
    L = 10*(i+1)
    datos = np.loadtxt(f"procesado-{L}.txt", delimiter = ' ').T

    g_coef = 1 - (datos[5]**4)/(3*(datos[3]**2))
    
    plt.plot(datos[0], g_coef, label = f'{L}', color = colores[i], alpha = 0.8)

plt.xlim((0.5,5.0))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Cumulante de Binder }$g$', labelpad = 7)
plt.grid()
plt.tight_layout(pad = 0.55)
plt.savefig("binder-1.png")
plt.show()
plt.close()

##############################################################################

plt.figure(figsize = (3.54, 2.9), dpi = 300)
for i in range(10):
    
    L = 10*(i+1)    
    datos = np.loadtxt(f"procesado-{L}.txt", delimiter = ' ').T

    g_coef = 1 - (datos[5]**4)/(3*(datos[3]**2))
    
    plt.plot(L*(datos[0]-2.2629), g_coef, label = f'{L}', color = colores[i], alpha = 0.7)
    
plt.xlim((-180,280))
#plt.ylim((-0.05, 1.05))
plt.xlabel(r'$L^{\frac{1}{\nu}}(T-T_{c})$')
plt.ylabel(r'\textrm{Cumulante de Binder }$g$', labelpad = 7)
plt.grid()
plt.tight_layout(pad = 0.55)
plt.savefig("binder-2.png")
plt.show()
plt.close()


plt.figure(figsize = (3.54, 2.9), dpi = 300)

for i in range(10):
    
    L = 10*(i+1)
    datos = np.loadtxt(f"procesado-{L}.txt", delimiter = ' ').T

    g_coef = 1 - (datos[5]**4)/(3*(datos[3]**2))
    
    plt.plot(datos[0], g_coef, label = f'{L}', color = colores[i], alpha = 0.5)

plt.xlim((2.2, 2.3))
plt.xlabel(r'\textrm{Temperatura }$T$')
plt.ylabel(r'\textrm{Cumulante de Binder }$g$', labelpad = 7)
plt.grid()
plt.tight_layout(pad = 0.55)
plt.savefig("binder-fino.png")
plt.show()
plt.close()