# -*- coding: utf-8 -*-

"""

Código correspondiente al Problema 1 del Trabajo Práctico N°3 de Física Computacional. 

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

""" Este código crea la carpeta donde guardar las figuras """

import os

script_dir  = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Figuras/')

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
    
""" --- """

def logistica(x, r):
    return r*x*(1-x)

def d_logistica(x, r):
    return r*(1-2*x)

def trayectoria(func, r, x, I = 0, F = 5000):
    
    """
    Parámetros
    ----------
    func : function
        Ecuación de recurrencia del elemento x_(n+1) como función de x_(n).
 
    r, x : float
        Coeficiente de func y condición inicial.
 
    I : int
        Iteración a partir de la cual retorna la sucesión.
 
    F : int
        Cantidad de iteraciones totales a realizar.
        
    Retorna
    -------
    [x] : list
        Lista con los valores de la secuencia generada por func desde el I-ésimo
        hasta el último.
    """
    
    if I == 0:
        trayecto = [x]
    else:
        trayecto = []

    for i in range(F):
        x = func(x, r)
        if i >= I:
            trayecto.append(x)
            
    return trayecto
    
def grafica_cobweb(func, r, trayecto, N):
    
    """
    Parámetros
    ----------
    func : function
        Ecuación de recurrencia del elemento x_(n+1) como función de x_(n).
 
    r : float
        Coeficiente de func y condición inicial.
 
    trayecto : lista
        Lista con los valores de la sucesión generada por func con alguna 
        condición inicial.
 
    N : int
        Orden de composición de la relación de recurrencia que se desea 
        graficar junto a la propia relación.
        
    """   
    
    plt.figure(figsize = (4.5, 3.5), dpi = 200)     # Comienza armando la figura
    plt.plot([0,1], [0,1], color = 'b', label = r'\textrm{Identidad}')

    x = np.linspace(0, 1, 1000)
    y = np.array([func(xi, r) for xi in x])         # y = f(x)

    plt.plot(x, y, color = 'g', label = r'$f(x)$')  # Grafica f(x)

    if N>1:                                         # z = f^(N)(x)
        z = y
        for i in range(N-1):
            z = np.array([func(zi, r) for zi in z])
        plt.plot(x, z, color = 'm', label = fr'$f^{N}(x)$') 
    
    # Comienza a armar los escalones dados por "trayectoria".
    plt.plot([trayecto[0], trayecto[0]], [-0.02, trayecto[0]], ls = '--', color = 'red', alpha = 0.5)
    for p, s in zip(trayecto[:-1], trayecto[1:]):
        plt.plot([p, p, s], [p, s, s], linestyle = '-', color = 'r', alpha = 0.5)
    
    plt.xlabel(r'$x_{n}$')                          # Configura parámetros de la gráfica.
    plt.ylabel(r'$x_{n+1}$')
    plt.xlim((-0.01,1.01))
    plt.ylim((0,1))
    plt.legend()
    plt.tight_layout(pad = 0.05)
    plt.savefig("Figuras/cobweb-"+str(r)+".png")  
    plt.close()
    
def lyapunov(func, func_der, r, x, I, F):
    
    """
    Parámetros
    ----------
    func, func_der : function
        Ecuación de recurrencia del elemento x_(n+1) como función de x_(n) y su
        derivada.
 
    r, x : float
        Coeficiente de func y condición inicial.
 
    I : int
        Iteración a partir de la cual realiza la sumatoria.
 
    F : int
        Iteración final que entra en la sumatoria..
        
    Retorna
    -------
    l : float
        Coeficiente de Lyapunov
    """
    
    trayecto = trayectoria(func, r, x, I, F)
    derivadas = []

    for punto in trayecto:
        derivadas.append(abs(func_der(punto, r)))

    return (np.log(derivadas).sum())/len(trayecto)
    
def ejercicio_1_a():
   
    """ Arma las 8 gráficas usando las funciones "logistica" y "trayectoria". """
    
    N = 5000        # Cantidad de iteraciones para el histograma
    J = 100         # Cantidad de iteraciones a graficar 
    
    for r in [1.5, 2.9, 3.3, 3.5, 3.55, 3.59, 3.83, 4.0]:
        
        histo_r = []

        fig, (ax_1, ax_2) = plt.subplots(1,2, sharey = True, gridspec_kw={'width_ratios': [3, 1]})
        fig.set_figheight(3)
        fig.set_figwidth(4.5)        
        fig.suptitle(fr'$r = {r}$')
        
        for x in np.linspace(0.05,0.95,10): # Se excluyen el 0 y 1.
            
            trayecto = trayectoria(logistica, r, x, I = 0, F = N)            
            histo_r += trayecto 
            
            ax_1.plot(np.arange(0,J), trayecto[:J], c = plt.cm.gist_rainbow(x), alpha = 0.6)#, label = fr'$x_{0}={x}$')

      # A partir de n ~ 70 los errores numéricos hacen saltar la inestabilidad del equilibrio en x = 1-1/r. 
      # ax_1.plot(np.arange(0,J), trayectoria(logistica, r, 1-(1/r), N)[:J], c = 'k', alpha = 0.6, label = r'$x_{0}=1-\frac{1}{r}$')
        ax_1.plot([0,J], [1-(1/r), 1-(1/r)], c = 'k', alpha = 0.6)#, label = r'$x_{0}=1-\frac{1}{r}$')

        plt.sca(ax_1)           # Configura la parte con las trayectorias
        plt.xscale('symlog', basex = 5)
        plt.xlim((0,J))
        plt.ylim((0,1))
        plt.xticks([0,1,2,5,10,25,50,100], [r'$0$',r'$1$',r'$2$', r'$5$',r'$10$',r'$25$', r'$50$',r'$100$'])
        plt.xlabel(r'\textrm{Índice }$n$')
        plt.ylabel(r'$x_{n}$')

        plt.sca(ax_2)           # Configura la parte con el histograma
        plt.hist(histo_r, density = True, bins = 500, color = 'b', orientation="horizontal")
        plt.xscale('symlog', basex = 10)
        plt.xlabel(r'\textrm{Frecuencia}')
        plt.ylim((0,1))
        plt.xticks([1,10,100], [r'$1$',r'$10$',r'$100$'])

        plt.setp(ax_2.get_yticklabels(), visible = False)

        xticks = ax_2.xaxis.get_major_ticks()
        xticks[0].label1.set_visible(False)
    
        plt.subplots_adjust(left = 0.09, right = 0.98, bottom = 0.12, top = 0.94, wspace = 0.0)
        
        plt.savefig("Figuras/trayecto-histograma-"+str(r)+".png", dpi = 600)
        plt.close()

def ejercicio_1_b():
    
    N = 1000     # Cantidad de iteraciones a graficar.
    x = 0.1      # Condición inicial relativamente cerca del 0 para que se pueda ver con comodidad.
    
    r = 2.9      # r para periodo-1
    grafica_cobweb(logistica, r, trayectoria(logistica, r, x, F = N), 1)
    r = 3.2      # r para periodo-2
    grafica_cobweb(logistica, r, trayectoria(logistica, r, x, F = N), 2)
    r = 3.5      # r para periodo-4
    grafica_cobweb(logistica, r, trayectoria(logistica, r, x, F = N), 4)
    r = 3.56     # r para periodo-8
    grafica_cobweb(logistica, r, trayectoria(logistica, r, x, F = N), 8)

def ejercicio_1_c():
    
    # Para el primer gráfico se arma una grilla para r no completamente equiespaciada.
    rs_1 = np.concatenate([np.linspace(1.0,  2.95, 195, endpoint = False), 
                           np.linspace(2.95, 3.05, 200, endpoint = False), # 2000 pts./ 0.1
                           np.linspace(3.05,  3.4, 105, endpoint = False), # 300  pts./ 1
                           np.linspace(3.4,  3.46, 120, endpoint = False), # 2000 pts./ 1
                           np.linspace(3.46, 3.54,  24, endpoint = False), # 300  pts./ 1
                           np.linspace(3.54, 4.0,  921, endpoint = True)]) # 2000 pts./ 1
    rs_2 = np.linspace(3,          3.678, 1200, endpoint = True)
    rs_3 = np.linspace(3.45122,  3.59382, 1200, endpoint = True)
    rs_4 = np.linspace(3.54416, 3.574905, 1200, endpoint = True)

    si_1 = np.concatenate([np.ones(195)*0.40, np.ones(200)*0.05, np.ones(105)*0.20,
                           np.ones(120)*0.05, np.ones(24)*0.20,  np.ones(921)*0.05])       

    xs_1, xs_2 = np.linspace(0.01,    0.99, 50), np.linspace(0.2722, 0.7287, 50)    # Evito 0 y 1 por ambos terminar directamente en 0
    xs_3, xs_4 = np.linspace(0.4105, 0.594, 50), np.linspace(0.46,   0.5359, 50)
    
    for lim_r, lim_x, rs, xs, si in zip([(1,4),        (3,3.678), (3.45122, 3.59383), (3.54416, 3.57490)],
                                        [(0,1), (0.2722, 0.7287),    (0.4105, 0.594),     (0.46, 0.5359)],
                                        [rs_1,              rs_2,               rs_3,               rs_4],
                                        [xs_1,              xs_2,               xs_3,               xs_4],                                        
                                        [si_1, 0.2*np.ones(1500),  0.2*np.ones(1500),  0.2*np.ones(1500)]):
        
        plt.figure(dpi = 1000, figsize = (4, 3.5))      # Crea la figura
        for r, s in zip(rs, si):
            for x in xs:
                trayecto = trayectoria(logistica, r, x, I = 4000, F = 5000)  # Me quedo con los últimos 1000 puntos para evitar el transitorio.
                plt.plot(r*np.ones(len(trayecto)), trayecto, alpha = 0.05, linestyle = '', marker = '.',
                         markersize = s, markeredgewidth = s, markerfacecolor = 'k', markeredgecolor = 'k')
        
        # Señala las secciones que luego se muestran recortadas.            
        plt.plot([3, 3, 3.678, 3.678, 3],                       [0.7287, 0.2722, 0.2722, 0.7287, 0.7287], color = 'b', linewidth = 1)
        plt.plot([3.45122, 3.45122, 3.59383, 3.59383, 3.45122], [0.4105,  0.594,  0.594, 0.4105, 0.4105], color = 'g', linewidth = 1)
        plt.plot([3.54416, 3.54416, 3.57490, 3.57490, 3.54416],     [0.46,   0.5359, 0.5359, 0.46, 0.46], color = 'r', linewidth = 1)
        
        # Ajusta los parámetros de la figura
        plt.xlabel(r'$r$')
        plt.ylabel(r'$x$')
        plt.xlim(lim_r)
        plt.ylim(lim_x)
        plt.tight_layout(pad = 0.05)
        plt.savefig("Figuras/"+str(lim_r)+"-"+str(lim_x)+".png")
        plt.close()

def ejercicio_1_d():
    
    """ Hace uso de lo implementado en lyapunov() """
    
    rs_p, rs_n = [], []
    ls_p, ls_n = [], []
    
    x = 0.2     # Condición inicial
    I = 5000    # Punto a partir del cual considerar que terminó el transitorio
    F = 6000    # Cantidad total de iteraciones
    
    for r in np.linspace(2.5, 4, 6000):     # Barrido en r
        l = lyapunov(logistica, d_logistica, r, x, I, F)
        if l >= 0:                          # Separa en mayores y menores a 0
            ls_p.append(l)
            rs_p.append(r)
        else:
            ls_n.append(l)
            rs_n.append(r)
    
    plt.figure(dpi = 1000)  # Comienza a armar la figura
    plt.plot(rs_p, ls_p, marker = '.', markersize = 0.8, markeredgewidth = 0.8, markerfacecolor = 'r', markeredgecolor = 'r', linestyle = '')
    plt.plot(rs_n, ls_n, marker = '.', markersize = 0.8, markeredgewidth = 0.8, markerfacecolor = 'b', markeredgecolor = 'b', linestyle = '')
    plt.plot([2.5, 4], [0,0], color = 'k', linestyle = '--', linewidth = 1)
    plt.xlabel(r'$r$')
    plt.ylabel(r'$\lambda$')
    plt.xlim((2.5, 4))
    plt.ylim((-3.25, 0.75))
    plt.xticks([2.5, 2.75, 3, 3.25, 3.5, 3.75, 4])
    plt.grid()
    plt.tight_layout(pad = 0.05)
    plt.savefig("Figuras/liapunov-"+str(x)+".png")
    plt.close()
    
""" Descomentar cada instrucción para obtener las gráficas """

#ejercicio_1_a()
#ejercicio_1_b()
#ejercicio_1_c()
#ejercicio_1_d()