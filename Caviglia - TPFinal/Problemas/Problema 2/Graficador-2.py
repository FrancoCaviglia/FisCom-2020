# -*- coding: utf-8 -*-

"""

Código utilizado para graficar las funciones de correlación temporal para la energía y magnetización.

Trabajo Práctico Final de Física Computacional.

Franco Caviglia - 16/10/2020

"""

import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=10)       
plt.rc('axes', titlesize=10)
plt.rc('axes', labelsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('legend', fontsize=10)
plt.rc('figure', titlesize=10)

colores = plt.cm.jet(np.linspace(0,1,6))

infile = open("30.txt", 'r')
l_nombres = []
for line in infile:
    l_nombres.append(line[:-1])
infile.close()

colores = plt.cm.jet(np.linspace(0,1,9))

def correlacion(f_nombre):
    
    """
    Calcula las funciones de correlación con los datos en el archivo 'f_nombre'.
    """
    
    datos = np.loadtxt(f_nombre, delimiter = ' ').T

    e_corr = acf(datos[0], nlags = datos[0].size, unbiased = True, fft = True)
    m_corr = acf(datos[1], nlags = datos[1].size, unbiased = True, fft = True)
    
    np.savetxt("A-"+f_nombre, np.array([e_corr, m_corr]), delimiter = ' ')

##############################################################################

plt.figure(figsize = (3.54,3.1), dpi = 300)
for r in range(29, 37, 1):
    MCS = 50
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), datos[0][:MC], label = f'$T={l_nombres[r][3:7]}$', color = colores[r-29])
plt.xlim((0,MCS))
plt.ylim((-0.02,1.02))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$C_{e}(t)$")
plt.tight_layout(pad = 0.05)
plt.savefig("E-30-lin-pre.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(37, 45, 1):
    MCS = 50
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), datos[0][:MC], label = f'$T={l_nombres[r][3:7]}$', color = colores[r-37])
plt.xlim((0,MCS))
plt.ylim((-0.02,1.02))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$C_{e}(t)$")
plt.tight_layout(pad = 0.05)
plt.savefig("E-30-lin-pos.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(29, 37, 1):
    MCS = 20
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), np.log(datos[0][:MC]), label = f'$T={l_nombres[r][3:7]}$', color = colores[r-29])
plt.xlim((0,MCS))
plt.ylim((-3.5,0))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$\ln[C_{e}(t)]$")
plt.tight_layout(pad = 0.05)
plt.savefig("E-30-log-pre.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(37, 45, 1):
    MCS = 20
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), np.log(datos[0][:MC]), label = f'$T={l_nombres[r][3:7]}$', color = colores[r-37])
plt.xlim((0,MCS))
plt.ylim((-3.5,0))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$\ln[C_{e}(t)]$")
plt.tight_layout(pad = 0.05)
plt.savefig("E-30-log-pos.png")
plt.show()

##############################################################################

plt.figure(figsize = (3.54,2.8), dpi = 300)
for r in range(25,33,1):
    MCS = 30
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), datos[1][:MC], label = f'$T={l_nombres[r][3:7]}$', color = colores[r-25])
plt.xlim((0,MCS))
plt.ylim((-0.02,1.02))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$C_{m}(t)$")
plt.tight_layout(pad = 0.05)
plt.savefig("M-30-lin-pre.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(36, 44, 1):
    MCS = 200
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), datos[1][:MC], label = f'$T={l_nombres[r][3:7]}$', color = colores[r-36])
plt.xlim((0,MCS))
plt.ylim((-0.02,1.02))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$C_{m}(t)$")
plt.tight_layout(pad = 0.05)
plt.savefig("M-30-lin-pos.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(25,33,1):
    MCS = 30
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), np.log(datos[1][:MC]), label = f'$T={l_nombres[r][3:7]}$', color = colores[r-25])
plt.xlim((0,MCS))
plt.ylim((-4,0))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$\ln[C_{m}(t)]$")
plt.tight_layout(pad = 0.05)
plt.savefig("M-30-log-pre.png")
plt.show()

plt.figure(figsize = (3.54, 2.8), dpi = 300)
for r in range(36, 44, 1):
    MCS = 200
    MC  = 30*30*MCS
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    plt.plot(np.linspace(0, MCS, MC), np.log(datos[1][:MC]), label = f'$T={l_nombres[r][3:7]}$', color = colores[r-36])
plt.xlim((0,MCS))
plt.ylim((-1,0))
plt.legend()
plt.xlabel(r"\textrm{Pasos de Montecarlo MCS}")
plt.ylabel(r"\textrm{Correlación }$\ln[C_{m}(t)]$")
plt.tight_layout(pad = 0.05)
plt.savefig("M-30-log-pos.png")
plt.show()

###########################################################3333

coef_e = []
coef_m = []

temperaturas = np.arange(0.5, 5.0, 0.05)

f, (ax_1, ax_2) = plt.subplots(dpi = 300, ncols = 2)

for r in range(23, 37, 1):
    
    mcs_min = int(0.5*(r-23))
    mcs_max = int(mcs_min + 5)
    
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    
    coef_e.append(-1/np.polyfit(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[0][30*30*mcs_min:30*30*mcs_max]), deg = 1)[0])
    coef_m.append(-1/np.polyfit(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[1][30*30*(mcs_min):30*30*(mcs_max)]), deg = 1)[0])
    
    plt.sca(ax_1)
    plt.plot(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)),  np.log(datos[0][30*30*mcs_min:30*30*mcs_max]))

    plt.sca(ax_2)
    plt.plot(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[1][30*30*mcs_min:30*30*mcs_max]))

plt.show()
f.clear()

f, (ax_1, ax_2) = plt.subplots(dpi = 300, ncols = 2)

for r in range(37, 56, 1):

    mcs_min = int(10 - 0.5*(r-37))
    mcs_max = int(mcs_min + 6)
        
    datos = np.loadtxt("A-"+l_nombres[r], delimiter = ' ')
    
    coef_e.append(-1/np.polyfit(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[0][30*30*mcs_min:30*30*mcs_max]), deg = 1)[0])
    coef_m.append(-1/np.polyfit(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[1][30*30*mcs_min:30*30*mcs_max]), deg = 1)[0])

    plt.sca(ax_1)
    plt.plot(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[0][30*30*mcs_min:30*30*mcs_max]))

    plt.sca(ax_2)
    plt.plot(np.linspace(mcs_min, mcs_max, 30*30*(mcs_max-mcs_min)), np.log(datos[1][30*30*mcs_min:30*30*mcs_max]))

plt.show()
f.clear()

fig, ax_1 = plt.subplots(figsize = (3.54, 2.7))

ax_1.plot(temperaturas[23:56], coef_e, color = 'r')
ax_1.set_ylabel(r"$\tau_{m}$\textrm{ (MCS)}", color = 'r')
plt.legend()

ax_2 = ax_1.twinx()
ax_2.plot(temperaturas[23:56], coef_m, color = 'b')
ax_2.set_ylabel(r"$\tau_{e}$\textrm{ (MCS)}", color = 'b', rotation = 270, labelpad = 12)
ax_2.set_xlabel(r"\textrm{Temperatura }$T$")

plt.tight_layout(pad = 0.05)
fig.savefig("coeff.png", dpi = 300)
plt.show()