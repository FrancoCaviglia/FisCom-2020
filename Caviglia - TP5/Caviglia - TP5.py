# -*- coding: utf-8 -*-

"""

Código correspondiente al Problema 1 del Trabajo Práctico N°5 de Física Computacional. 


Franco Caviglia - 17/09/2020

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as stats

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=9)       
plt.rc('axes', titlesize=9)
plt.rc('axes', labelsize=9)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('legend', fontsize=9)
plt.rc('figure', titlesize=9)

def fmt(x, pos):
    """ Función para graficar """
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)

def grafica_color(grilla):
    
    """
    Parámetros
    ----------
    grilla : np.ndarray
        Matriz cuadrada que contiene codificados como 0 o 1 el estado de cada celda.
 
    """    
    
    # Primero modifico un poco una paleta de colores para que no pinte todas las
    # celdas sin agregado de rojo.
    
    # [1,1,1,1] indica R=G=B=1, y alpha = 1. Color blanco opaco.
    
    colores = np.vstack(([1,1,1,1], mpl.cm.gist_rainbow(np.linspace(0,1,4*256))))
    cmap    = mpl.colors.ListedColormap(colores)
    
    plt.figure(dpi = 1000, figsize = (7,7))      # Arma y guarda la figura.
    plt.imshow(grilla, cmap = cmap, extent = (0, grilla.shape[0], 0, grilla.shape[0]))
    
    plt.colorbar(fraction = 0.03, pad = 0.03, aspect = 40, shrink = 0.7, 
                 orientation='vertical', format=mpl.ticker.FuncFormatter(fmt),
                 label = r'\textrm{Pasos de tiempo}')
    
    plt.xlabel(r'\textrm{Coordenada }$x$')
    plt.ylabel(r'\textrm{Coordenada }$y$')
    plt.tight_layout()
    plt.savefig("grilla.png")
    plt.close()
        
def fractal(grilla, semilla, r):

    """
    Parámetros
    ----------
    grilla : np.ndarray
        Matriz cuadrada que contiene codificados como 0 o 1 el estado de cada celda.
 
    semilla : list
        Posición de la semilla central.
 
    r : float
        Radio de la circunferencia donde se va a contar la masa.

    Retorna
    -------
    M : int
        Cantidad de celdas activadas dentro de la circunferencia de radio r.
    """
    
    x, y = np.mgrid[:grilla.shape[0], :grilla.shape[1]]
    
    circulo = (x - semilla[0]) ** 2 + (y - semilla[0]) ** 2
    
    mascara = circulo <= r*r

    M = np.count_nonzero(grilla[mascara])
    
    return M

def box_counting(grilla, d):
    
    """
    Parámetros
    ----------
    grilla : np.ndarray
        Matriz cuadrada que contiene codificados como 0 o 1 el estado de cada celda.
 
    d : int
        Longitud de los cuadrados con los que rellenar la grilla. Se supone que es 
        divisor de la longitud de los lados de la grilla.

    Retorna
    -------
    M : int
        Cantidad de cuadrados necesarios para cubrir todas las celdas activas de grilla.
    """
    
    M = 0
    for x in range(0, grilla.shape[1], d):
        for y in range(0, grilla.shape[0], d):
            M += grilla[y : y+d, x : x+d].any()
    return M

def divisores(num):
    
    """
    Parámetros
    ----------
    num : int
        Número entero (en este caso el tamaño de los lados de la grilla).

    Retorna
    -------
    N: list
        Lista con los divisores. Incluye al 1 y al propio número.
    """
    
    N = [num]
    for x in reversed(range(1, (num//2)+1)):
        if not (num % x):
            N.append(x)            
    return N

### A partir de acá comienzan las instrucciones que va a ejecutar el programa ###
### Con los valores dados demora bastante tiempo, pero es razonable.          ###

for D, N in zip([2048], [100]):
    
    """ El for barre sobre los tres tamaños utilizados junto con la cantidad 
    de simulaciones viables que se obtuvieron. Para los gráficos se utiliza
    un promedio sobre todas las simulaciones. """
    
    f = D/64
    m_fractal = np.zeros((64, N))  # Comienza armando donde va a guardar 
    for i in range(0, N, 1):       # Barre sobre cada simulación
        grilla = np.loadtxt(f"Agregados/{D}/{D}-{i:04}.txt", delimiter = " ")
        m_fractal[0][i] = 0
        
        for r in range(1, 64, 1):  # Para cada simulación, barre sobre los radios.
            m_fractal[r][i] = fractal(grilla, [D//2, D//2], f*r) # La semilla siempre en el medio.
    
    p_fractal = np.zeros((2, 64))  # En este array se van a guardar los valores medios y su desv. estándar.
    for r in range(0, 64, 1):
        p_fractal[0][r] = m_fractal[r].mean() 
        p_fractal[1][r] = m_fractal[r].std() 
    
    # Finalmente, arma la gráfica.
    
    plt.figure(dpi = 500, figsize = (3.8,3.3))
    plt.errorbar(list(range(0,64)), p_fractal[0], yerr = p_fractal[1], color = 'b', alpha = 1, marker = "o", markersize = 3, linestyle = '--')
    plt.xscale('symlog', base = 10)
    plt.yscale('symlog', base = 5)
    plt.xlabel(r'$r$')
    plt.ylabel(r'\textrm{Masa }$M$')
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"FRACTAL-{D}.png")
    plt.close()
    
    ###########################################################################
    
    div = divisores(D)               # Obtiene los valores para los tamaños de las cajas.
    m_box = np.zeros((len(div), N))  # Para cada tamaño de caja, es donde va a guardar M.
        
    for i in range(0, N):            # Itera sobre cada gráfico
        grilla = np.loadtxt(f"Agregados/{D}/{D}-{i:04}.txt", delimiter = " ")
        
        m_box[0][i]  = 1             # Estos dos valores los conozco de antemano.
        m_box[-1][i] = np.count_nonzero(grilla) 
        
        for j in range(1, len(div)-1):    # Y luego sobre todos los tamaños
            m_box[j][i] = box_counting(grilla, div[j])
    
    p_box = np.zeros((2, len(div)))  # En este array se van a guardar los valores medios y su desv. estándar.
    for i in range(len(div)):
        p_box[0][i] = m_box[i].mean() 
        p_box[1][i] = m_box[i].std() 

    # Finalmente, arma la gráfica.
    
    plt.figure(dpi = 500, figsize = (3.8,3.3))
    plt.errorbar(1/np.array(div), p_box[0], yerr = p_box[1], color = 'b', alpha = 1, marker = "o", markersize = 3, linestyle = '--')
    plt.xscale('log', base = 2)
    plt.yscale('log', base = 10)
    plt.xlabel(r'$r = 1/M$')
    plt.ylabel(r'\textrm{Cantidad de cajas}')
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"BOX-{D}.png")
    plt.close()

    # Guarda lo obtenido para cada tamaño de la grilla en dos archivos .txt
    
    np.savetxt(f'FRACTAL-{D}.txt', p_fractal.T, delimiter = " ", fmt = '%d')
    np.savetxt(f'BOX-{D}.txt',     p_box.T,     delimiter = " ", fmt = '%d')
    
""" Finalmente, el ajuste lineal con scipy """

for D in [512, 1024, 2048]:
    
    datos = np.loadtxt(f"BOX-{D}.txt", delimiter = ' ')
    p = stats.linregress(np.log(1/np.array(divisores(D)[1:-2])), np.log(datos.T[0][1:-2]))
    print(p)
    
    datos = np.loadtxt(f"FRACTAL-{D}.txt", delimiter = ' ')
    p = stats.linregress(np.log(np.array(list(range(0,64,1)[1:-20]))), np.log(datos.T[0][1:-20]))
    print(p)