# -*- coding: utf-8 -*-

"""
Código correspondiente al los Problemas 3 y 4 del 1er. Trabajo Práctico
de Física Computacional.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

plt.rc('text', usetex=True)
plt.rc('font', size=9)       
plt.rc('axes', titlesize=9)
plt.rc('axes', labelsize=9)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('legend', fontsize=9)
plt.rc('figure', titlesize=9)
    
def RK4_quimica(x_0, y_0, a, b, h, N):
    
    """
    Parámetros
    ----------
    x_0, y_0 : float
        Valores iniciales para las variables x e y.
 
    a, b : float
        Parámetros del sistema de reacciones
 
    h : float
        Paso fijo.
 
    N : int
        Cantidad de pasos a realizar.
        
    Retorna
    -------
    x, y, t : list
        Tres listas con los N+1 valores secuenciales de la simulación, 
        tanto de x, y como el tiempo discretizado t.
    """
    
    x = [x_0]           # Arma las listas con los resultados comenzando con 
    y = [y_0]           # la condición inicial
    t = [0]
    
    for i in range(N):  # Ejecuta el ciclo N veces
        # Las constantes k_i son de la forma de listas [k_i(x), k_i(y)]
        k_1 = [h*( a-(b+1)*x[-1]           +(x[-1]**2)*y[-1]),                       h*(b*x[-1]-(x[-1]**2)*y[-1]) ]
        k_2 = [h*( a-(b+1)*(x[-1]+k_1[0]/2)+((x[-1]+k_1[0]/2)**2)*(y[-1]+k_1[1]/2)), h*(b*(x[-1]+k_1[0]/2)-((x[-1]+k_1[0]/2)**2)*(y[-1]+k_1[1]/2)) ]
        k_3 = [h*( a-(b+1)*(x[-1]+k_2[0]/2)+((x[-1]+k_2[0]/2)**2)*(y[-1]+k_2[1]/2)), h*(b*(x[-1]+k_2[0]/2)-((x[-1]+k_2[0]/2)**2)*(y[-1]+k_2[1]/2)) ]
        k_4 = [h*( a-(b+1)*(x[-1]+k_3[0])  +((x[-1]+k_3[0]  )**2)*(y[-1]+k_3[1])  ), h*(b*(x[-1]+k_3[0])  -((x[-1]+k_3[0]  )**2)*(y[-1]+k_3[1])  ) ]
        
        x.append(x[-1]+(k_1[0]+2*(k_2[0]+k_3[0])+k_4[0])/6) # Calcula el valor siguiente
        y.append(y[-1]+(k_1[1]+2*(k_2[1]+k_3[1])+k_4[1])/6) # y lo agrega a cada lista
        t.append(t[-1]+h)
        
    return x, y, t

def ejercicio_3_a():
    
    """ Toma lo hecho en la función RK4_quimica y pasando distintos parámetros arma
        cada una de las curvas para luego juntarlas en una única gráfica """
    
    a = 1
    b = 1
    x_0 = np.float64(1.5)
    y_0 = np.float64(1.5)
    
    # La cantidad de pasos N se ajusta de forma que h*N sea mantenga constate.
    
    plt.figure(dpi=300)
    
    x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.1), 1000)
    plt.plot(x, y, markersize = 0.5, marker = "o", color = 'b', label = "h=0.1")

    x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.2), 500)
    plt.plot(x, y, markersize = 1.0, marker = "o", color = 'r', label = "h=0.2")

    x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.5), 200)
    plt.plot(x, y, markersize = 1.5, marker = "o", color = 'g', label = "h=0.5")

    x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(1.0), 100)
    plt.plot(x, y, markersize = 2.0, marker = "o", color = 'm', label = "h=1.0")
    
    plt.title(r'\textrm{Ejercicio 3a: diagrama de fases $(x,y)$}')
    plt.xlabel(r'$x(t)$')                   # Título eje x
    plt.ylabel(r'$y(t)$')                   # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    plt.savefig('3a')                       # Guarda la imagen como png en el directorio de ejecución.


def ejercicio_3_b():
    
    """ Toma lo hecho en la función RK4_quimica y pasando distintos parámetros arma
        cada una de las curvas para luego juntarlas en una única gráfica """

    a = 1       # Parámetros
    b = 3
        
    for x_0, y_0, nombre in zip( [np.float64(3.0), np.float64(0.1), np.float64(3.0), np.float64(1.5), np.float64(1.0)],
                                 [np.float64(3.0), np.float64(0.1), np.float64(1.0), np.float64(3.0), np.float64(3.0)],
                                 ['3b-fuera-1', '3b-fuera-2', '3b-dentro', '3b-cerca-fijo', '3b-fijo']):
        
        plt.figure(dpi=300)
    
        x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.10), 1500)
        plt.plot(x, y, markersize = 0.4, color = 'b', alpha = 0.6, label = r'$h=0.10$')
    
        x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.15), 1000)
        plt.plot(x, y, markersize = 0.8, color = 'r', alpha = 0.6, label = r'$h=0.15$')
    
        x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.20), 200)
        plt.plot(x, y, markersize = 1.2, color = 'g', alpha = 0.6, label = r'$h=0.20$')
    
        x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.25), 750)
        plt.plot(x, y, markersize = 1.6, color = 'c', alpha = 0.6, label = r'$h=0.25$')

        x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.30), 500)
        plt.plot(x, y, markersize = 2.0, color = 'm', alpha = 0.6, label = r'$h=0.30$')
        
        #x, y, _ = RK4_quimica(x_0, y_0, a, b, np.float64(0.35), 500)
        #plt.plot(x, y, markersize = 2.0, color = 'k', alpha = 0.6, label = r'$h=0.35$')
        
        plt.title(r'\textrm{Ejercicio 3b: diagrama de fases $(x,y)$}')
        plt.xlabel(r'$x(t)$')                   # Título eje x
        plt.ylabel(r'$y(t)$')                   # Título eje y
        plt.legend(loc='best')
        plt.grid()                              # Activa la grilla
        plt.tight_layout()                      # Recorta los gráficos
        plt.savefig(nombre)                     # Guarda la imagen como png en el directorio de ejecución. 

def RK4_adapatativo(x_0, y_0, a, b, h, e, factor):
    
    """
    Parámetros
    ----------
    x_0, y_0 : float
        Valores iniciales para las variables x e y.
 
    a, b : float
        Parámetros del sistema de reacciones
 
    h, e : float
        Paso fijo inicial y tolerancia.
  
    N : int
        Cantidad de pasos a realizar.
        
    Retorna
    ------- 
    x, y, t : list
        Tres listas con los N+1 valores secuenciales de la simulación, 
        tanto de x, y como el tiempo discretizado t.
    """
        
    x = [x_0]           # Arma las listas con los resultados comenzando con 
    y = [y_0]           # la condición inicial. Se toma siempre t_0 = 0.
    t = [0]
    
    while t[-1] <= 16:  # Bucle temporal: hace uso de la función RK4_quimica
        
        x_1, y_1, _ = RK4_quimica(x[-1], y[-1], a, b,   h, 1)      # Si se toma h
        x_m, y_m, _ = RK4_quimica(x[-1], y[-1], a, b, h/2, 1)      # Si se toma h/2 (intermedio)
        x_2, y_2, _ = RK4_quimica(x_m[-1], y_m[-1], a, b, h/2, 1)  # Si se toma h/2 (final)
        
        delta_1 = abs(x_2[-1]-x_1[-1])  # Calcula los errores absolutos
        delta_2 = abs(y_2[-1]-y_1[-1])
        
        while delta_1 > e or delta_2 > e:                       # Si algún error excede e, se corrige h.
                        
            h = h/factor
            
            x_1, y_1, _ = RK4_quimica(x[-1], y[-1], a, b,   h, 1)
            x_m, y_m, _ = RK4_quimica(x[-1], y[-1], a, b, h/2, 1)
            x_2, y_2, _ = RK4_quimica(x_m[-1], y_m[-1], a, b, h/2, 1)
            
            delta_1 = abs(x_2[-1]-x_1[-1])
            delta_2 = abs(y_2[-1]-y_1[-1])
        
        x.append(x_2[-1])                   # Una vez con los errores acotados superiormente,
        y.append(y_2[-1])                   # se pasa a guardar los datos.
        t.append(t[-1]+h)

        if delta_1 < e/2 and delta_2 < e/2: # Si ninguno excedia, aún puede que ambos estén por debajo.
            h = factor*h
        
    return x, y, t

def ejercicio_4(name, e=0.00001, factor = 1.5):   # Lo estructuro como función para pasar distintos e.     
    
    """ Toma lo hecho en la función RK4_adaptativo y pasando distintos parámetros calcula
        cada una de las curvas para luego juntarlas en una única gráfica """
    
    a = np.float64(1.0)         # Parámetros
    b = np.float64(3.0)
    h = np.float64(0.1)         # Paso inicial

    x_0, y_0, t_0 = RK4_adapatativo(np.float64(3.0), np.float64(3.0), a, b, h, e, factor)
    x_1, y_1, t_1 = RK4_adapatativo(np.float64(2.0), np.float64(2.0), a, b, h, e, factor)
    x_2, y_2, t_2 = RK4_adapatativo(np.float64(1.0), np.float64(1.0), a, b, h, e, factor)

    # Primero grafica el diagrama de fases
    plt.figure(dpi=300)    
    plt.plot(x_0, y_0, '-o', markersize = 2.0, color = 'g', label = r'$(x,t)(0) = (3,3)$')
    plt.plot(x_1, y_1, '-o', markersize = 2.0, color = 'b', label = r'$(x,t)(0) = (2,2)$')
    plt.plot(x_2, y_2, '-o', markersize = 2.0, color = 'm', label = r'$(x,t)(0) = (1,1)$')
    plt.title(r'\textrm{Ejercicio 4: diagrama de fases $(x,y)$}')
    plt.xlabel(r'$x(t)$')                   # Título eje x
    plt.ylabel(r'$y(t)$')                   # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    
    plt.savefig('4-'+name+'-fase')    

    # Segundo grafica las soluciones como función del tiempo
    plt.figure(dpi=300)    
    
    for i in range(len(t_0)):                 # Marcas de tiempo
        plt.plot([t_0[i],t_0[i]],[0,0.2], linewidth=0.8, color = 'r')
    
    plt.plot(t_0, x_0, '-o', markersize = 2.0, color = 'g', label = "x(t)")
    plt.plot(t_0, y_0, '-o', markersize = 2.0, color = 'r', label = "y(t)")    
    
    plt.title(r'\textrm{Ejercicio 4: $(x,y)(t)$ para $(x,t)(0) = (3,3)$}')
    plt.xlabel(r'\textrm{Tiempo }$t$')               # Título eje x
    plt.ylabel(r'\textrm{Soluciones }$x(t),\ y(t)$') # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    
    plt.savefig('4-'+name+'-tiempo')                 # Guarda la imagen como png en el directorio de ejecución. 
    
def precision():

    a = np.float64(1.0)         # Parámetros
    b = np.float64(3.0)
    h = np.float64(0.01)         # Paso inicial
    e = 0.00001
    factor = 1.5
    
    x_0, y_0, t_0 = RK4_adapatativo(np.float64(1.0), np.float64(4.5), a, b, h, e, factor)    
    x_1, y_1, t_1 = RK4_quimica(np.float64(1.0), np.float64(4.5), a, b, h, N=int(200/h))    
    
    for i in range(len(t_1)):
        if x_1[i] <= 3.76 and x_1[i] >= 3.74:
            print(i, [x_1[i], y_1[i]])
        
    plt.figure()
    plt.plot(x_1, y_1, '-o', markersize = 2.0, color = 'r', alpha = 0.6, label = "Paso fijo")
    #plt.plot(x_0, y_0, '-o', markersize = 2.0, color = 'g', alpha = 0.6, label = "Paso adaptativo")    
    plt.title(r'\textrm{Ejercicio 4: $(x,y)(t)$ para $(x,t)(0) = (1,4.5)$}')
    plt.xlabel(r'\textrm{Tiempo }$t$')               # Título eje x
    plt.ylabel(r'\textrm{Soluciones }$x(t),\ y(t)$') # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    
    plt.figure(dpi=300)    
    
    for i in range(len(t_0)):                 # Marcas de tiempo
        plt.plot([t_0[i],t_0[i]],[0,0.2], linewidth=0.8, color = 'r')
    
    plt.plot(t_0, x_0, '-o', markersize = 2.0, color = 'g', label = "x(t)")
    plt.plot(t_0, y_0, '-o', markersize = 2.0, color = 'r', label = "y(t)")    
    
    plt.title(r'\textrm{Ejercicio 4: $(x,y)(t)$ para $(x,t)(0) = (3,3)$}')
    plt.xlabel(r'\textrm{Tiempo }$t$')               # Título eje x
    plt.ylabel(r'\textrm{Soluciones }$x(t),\ y(t)$') # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    
    plt.savefig('4-b-tiempo-fijo')          # Guarda la imagen como png en el directorio de ejecución. 

    plt.figure(dpi=300)    
    
    for i in range(len(t_1)):                 # Marcas de tiempo
        plt.plot([t_1[i],t_1[i]],[0,0.2], linewidth=0.2, color = 'r')
    
    plt.plot(t_1, x_1, '-o', markersize = 2.0, color = 'g', label = "x(t)")
    plt.plot(t_1, y_1, '-o', markersize = 2.0, color = 'r', label = "y(t)")    
    
    plt.title(r'\textrm{Ejercicio 4: $(x,y)(t)$ para $(x,t)(0) = (3,3)$}')
    plt.xlabel(r'\textrm{Tiempo }$t$')               # Título eje x
    plt.ylabel(r'\textrm{Soluciones }$x(t),\ y(t)$') # Título eje y
    plt.legend(loc='best')
    plt.grid()                              # Activa la grilla
    plt.tight_layout()                      # Recorta los gráficos
    
    plt.savefig('4-b-tiempo-adaptativo')          # Guarda la imagen como png en el directorio de ejecución. 

ejercicio_3_a()
ejercicio_3_b()
ejercicio_4('1')
ejercicio_4('2', e=0.0001)
ejercicio_4('3', e=0.001)
ejercicio_4('4', e=0.01)
ejercicio_4('5', factor=2)
#precision()