# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import imageio

import gc

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=9)
plt.rc('axes', titlesize=9)
plt.rc('axes', labelsize=9)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('legend', fontsize=9)
plt.rc('figure', titlesize=9)

def grafica_gif(lista_nombres, archivo_salida):

    # kargs = {'duration': 0.0001}
    
    lista_fotos = []
    for nombre_imagen in lista_nombres:
        lista_fotos.append(imageio.imread(nombre_imagen))
    imageio.mimsave(archivo_salida, lista_fotos, fps = 60)#,**kargs)

h = 0.005  # Paso de tiempo
N = 2000   # Cantidad de iteraciones (hasta t = 10)

tn = np.linspace(0, N * h, N, endpoint = False)

semilla = 1601589908

### Gráficas de energía ###

for folder in ["Datos - Libre", "Datos - Rigido", "Datos - Blando"]:

    datos = np.loadtxt(folder+"/ene-"+str(semilla)+".txt", delimiter = ' ').T

    e_inicial = datos[1][0]+datos[0][0]
    fig, (ax_1, ax_2) = plt.subplots(2,1, sharex = True, gridspec_kw={'height_ratios': [3, 1]})
    
    fig.set_figheight(3.9)
    fig.set_figwidth(4.1) 

    ax_1.plot(tn, datos[0],          color='b', label=r'\textrm{Energía cinética}')
    ax_1.plot(tn, datos[1],          color='r', label=r'\textrm{Energía potencial}')
    ax_1.plot(tn, datos[1]+datos[0], color='m', label=r'\textrm{Energía mecánica}')
    ax_2.plot(tn, 100*(datos[1]+datos[0]-e_inicial)/e_inicial, color='g', label=r'\textrm{Variación relativa}')

    plt.sca(ax_1)
    plt.xlim((0, 10))
    plt.ylim((-770, 1100))
    plt.ylabel(r'\textrm{Energia }$/\epsilon$')
    plt.legend(bbox_to_anchor = (1, 0.55))

    plt.sca(ax_2)
    plt.xlabel(r'\textrm{Tiempo }$t$')
    plt.ylabel(r'$\Delta E/E(0)\ \%$')  
    plt.ylim((-0.38, 0.38))
    plt.yticks([-0.3, 0, 0.3], [r"$-0.3$", r"$0.0$", r"$+0.3$"])
    plt.legend()
    
    plt.subplots_adjust(left = 0.145, right = 0.985, bottom = 0.10, top = 1, hspace = 0.025)
    plt.savefig(folder+"/grafica-energia.png", dpi = 300)
    plt.close()

### Distribuciones (histogramas) ###

for folder in ["Datos - Rigido"]:#, "Datos - Blando", "Datos - Libre"]:
    for tiempo in [0]:#650, 1350]:#, 2000]:

        datos = np.loadtxt(folder+"/vel-"+str(tiempo)+"-"+str(semilla)+".txt", delimiter = ' ').T

        vn = np.arange(-4,4,0.001)
        
        plt.figure(dpi=300, figsize=(3, 3))

        mu = datos[0].mean()
        s  = datos[0].std()
        plt.hist(datos[0], color='b', density = True, bins = 30)
        #plt.plot(vn, norm.pdf(vn, mu, s), 'k', linewidth=2)

        plt.xlabel(r'\textrm{Velocidad }$v_{x}$')
        plt.ylabel(r'\textrm{Densidad de probabilidad}')
        plt.xlim((-2,2))
        #plt.ylim((0,0.5))
        #plt.text(-3.6, .47, rf'$\mu={mu:.2f},\ \sigma={s:.2f}$')
        plt.tight_layout(pad = 0.1)
        plt.savefig("histo-x-"+str(tiempo)+".png")
        plt.show()
        plt.close()
            
        plt.figure(dpi=300, figsize=(3, 3))

        mu = datos[0].mean()
        s  = datos[0].std()
        plt.hist(datos[1], color='b', density = True, bins = 30)
        #plt.plot(vn, norm.pdf(vn, mu, s), 'k', linewidth=2)

        plt.xlabel(r'\textrm{Velocidad }$v_{y}$')
        plt.ylabel(r'\textrm{Densidad de probabilidad}')
        plt.xlim((-2,2))
        #plt.ylim((0,0.5))
        #plt.text(-3.6, .47, rf'$\mu={mu:.2f},\ \sigma={s:.2f}$')
        plt.tight_layout(pad = 0.1)
        plt.savefig("histo-y-"+str(tiempo)+".png")
        plt.show()
        plt.close()

        plt.figure(dpi=300, figsize=(3, 3))

        datos_v = np.concatenate((datos[1], datos[0]))
        mu = datos_v.mean()
        s  = datos_v.std()

        plt.hist(datos_v, color='b', density = True, bins = 30)
        #plt.plot(vn, norm.pdf(vn, mu, s), 'k', linewidth=2)
        
        plt.xlabel(r'\textrm{Velocidad}')
        plt.ylabel(r'\textrm{Densidad de probabilidad}')
        plt.xlim((-2,2))
        #plt.ylim((0,0.5))
        #plt.text(-3.6, .47, rf'$\mu={mu:.2f},\ \sigma={s:.2f}$')
        plt.tight_layout(pad = 0.1)
        plt.savefig("histo-v-"+str(tiempo)+".png")
        plt.show()
        plt.close()

        plt.figure(dpi=300, figsize=(4, 3))
        
        datos_v = np.sqrt(datos[1]**2 + datos[0]**2)
        
        plt.hist(datos_v, color='b', density = True, bins = 30)
        plt.plot(vn, vn*np.exp(-((vn/s)**2)/2)/(s**2), 'k', linewidth=2)
        
        plt.xlabel(r'\textrm{Velocidad}')
        plt.ylabel(r'\textrm{Densidad de probabilidad}')
        plt.xlim((0,4))
        plt.ylim((0,0.65))
        plt.text(2, .6, rf'$\mu={mu:.2f},\ \sigma={s:.2f}$')
        plt.tight_layout(pad = 0.1)
        plt.savefig("histo-norma-v-"+str(tiempo)+".png")
        plt.show()
        plt.close()

### GIF partículas moviéndose ### 

lista_nombres = [[],[],[]]

for tiempo in range(0,2001):

    datos_v = np.loadtxt("Datos - Rigido/vel-"+str(tiempo)+"-"+str(semilla)+".txt", delimiter = ' ').T
    datos_p = np.loadtxt("Datos - Rigido/pos-"+str(tiempo)+"-"+str(semilla)+".txt", delimiter = ' ').T

    f = plt.figure(dpi=100, figsize=(3, 3))

    plt.scatter(datos_p[0], datos_p[1], color='b', s = 0.1)

    plt.xlim((0,54.77226))
    plt.ylim((0,54.77226))
    plt.xticks([])
    plt.yticks([])
    
    plt.tight_layout(pad = 0)
    plt.savefig("Datos - Rigido/pos-"+str(tiempo)+".png")
    f.clear()
    plt.close()
  
    lista_nombres[0].append("Datos - Rigido/pos-"+str(tiempo)+".png")   

    for n in [1,2]:
                        
        f = plt.figure(dpi = 100, figsize=(3, 3))

        plt.hist(datos_v[n-1], color='b', density = True, bins = 30)
        plt.xlabel(r'\textrm{Velocidad }$v_{y}$')
        plt.ylabel(r'\textrm{Densidad de probabilidad}')
        plt.xlim((-4,4))
       # plt.ylim((0,0.45))
        plt.tight_layout(pad = 0.05)
        plt.savefig("Datos - Rigido/Histogramas/histo-"+str(n)+"-"+str(tiempo)+".png")
        f.clear()
        plt.close() 
            
        lista_nombres[n].append("Datos - Rigido/Histogramas/histo-"+str(n)+"-"+str(tiempo)+".png")
        lista_nombres[1].append("Datos - Rigido/Histogramas/histo-"+str(1)+"-"+str(tiempo)+".png")

grafica_gif(lista_nombres[0], 'Datos - Rigido/evolución.gif')
grafica_gif(lista_nombres[1], 'Datos - Rigido/GIF-Histo-x.gif')
grafica_gif(lista_nombres[2], 'Datos - Rigido/GIF-Histo-y.gif')

""" # Separa las partículas que se excedieron de la caja y las registra en una lista.
lista_particulas = []
for i in range(900):
    lista_particulas.append([])
for tiempo in range(2001):
    datos_p = np.loadtxt("Datos - Rigido/pos-"+str(tiempo)+"-"+str(semilla)+".txt", delimiter = ' ')
    for i in range(900):
        if datos_p[i][0] > 54.77226 or datos_p[i][0] < 0:
            lista_particulas[i].append(tiempo)
        if datos_p[i][1] > 54.77226 or datos_p[i][1] < 0:
            lista_particulas[i].append(tiempo)
print(lista_particulas)
"""