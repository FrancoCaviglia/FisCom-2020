# -*- coding: utf-8 -*-

"""

Código correspondiente al Problema 1 del Trabajo Práctico N°2 de Física Computacional. 

"""

import numpy as np
import matplotlib.pyplot as plt
import imageio
from IPython.display import Image


""" Este código crea la carpeta donde guardar las imágenes """

import os

script_dir  = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Figuras/')

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
    
""" --- """

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=10)       
plt.rc('axes', titlesize=10)
plt.rc('axes', labelsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('legend', fontsize=10)
plt.rc('figure', titlesize=10)

def grafica_polar(u, x_i, x_f, t_i, t_f, nombre):

    """ Arma un gráfico en coordenadas polares con un mapa de colores dado por u.
    
    Parámetros
    ----------
    u : float
        Lista de listas con los valores en cada instante temporal.
 
    x_i, x_f : float
        Límites para la coordenada espacial (coordenada angular).
 
    t_i, t_f : float
        Límites para la coordenada temporal (coordenada radial).
    
    """
    
    datos = np.array([np.array(ui) for ui in u]).T

    r, theta = np.meshgrid(np.linspace(t_i, t_f, len(u)), np.radians(np.linspace(0, 360, len(u[0]))))
    
    plt.figure(dpi = 100)
    plt.polar()
    plt.contourf(theta, r, datos, 256, cmap = 'jet')
    plt.xticks(2*np.pi*np.arange(0, 1, 0.1), np.round(np.arange(x_i, x_f, 0.1),1))
    plt.yticks([])
    plt.savefig("Figuras/polar-"+nombre+".png")
    plt.show()
        
def grafica_gif(lista_nombres, archivo_salida):
    
    """ Arma un gif uniendo las imágenes guardadas en lista_nombres, y lo guarda en
    archivo_salida.

    Parámetros
    ----------
    lista_nombres : list
        Lista con los nombres de los archivos de las imágenes para unir. El directorio base
        es aquel donde se ejecuta el .py
 
    archivo_salida : str
        Nombre del archivo donde se va a guardar el gif. El directorio base es aquel donde
        se ejecuta el .py

    """    
    kargs = {'duration': 0.01}
    
    lista_fotos = []
    for nombre_imagen in lista_nombres:
        lista_fotos.append(imageio.imread(nombre_imagen))
    imageio.mimsave(archivo_salida, lista_fotos, fps=800,**kargs)

    Image(archivo_salida, format='png', height=500)
    
def turing(h_tim, h_esp, x_i, x_f, t_i, t_f, a):
    
    xn = list(np.arange(x_i, x_f+h_esp, h_esp))     # Se guarda la grilla espacial para graficar luego
    tn = list(np.arange(t_i, t_f+h_tim, h_tim))     # Se guarda la grilla temporal para graficar luego
    
    u_i = list(1+a*(2*np.random.random(len(xn))-1)) # Condiciones iniciales
    v_i = list(1+a*(2*np.random.random(len(xn))-1))
        
    plt.figure(figsize = (4.5, 3.8), dpi = 200)
    plt.plot(xn, u_i, color = 'r', label = r'$u(x,t)$')
    plt.plot(xn, v_i, color = 'b', label = r'$v(x,t)$')
    plt.title(r'$t = 0.000$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$u,\ v$')
    plt.legend()
    plt.grid()                          # Activa la grilla
    plt.ylim(0.70, 1.30)                # Limita el eje y
    plt.tight_layout()                  # Recorta la gráfica
    plt.savefig("Figuras/INICIAL.png")
    plt.close()
        
    for D in [0.01, 0.0025, 0.0015, 0.00075, 0.0005]:   # Coeficientes de difusión
        
        imagenes = ["Figuras/INICIAL.png"]   # Lista un nombres de archivos para gif
        
        f_mu = D*h_tim/(h_esp*h_esp)    # Factor para el término difusivo
        f_nu = D*h_tim/(2*h_esp*h_esp)  # Factor para el término difusivo
        
        un = u_i                        # un y vn se usarán como para guardar auxilarmente el dato anterior.
        vn = v_i
        
        u = [u_i]                       # u y v guardarán el estado del sistema en algunos instantes de interés.
        v = [v_i]
        
        for i in range(len(tn)):        # Bucle temporal (el primer instante es la CI)
            
            u_nuevo = []                # Se arma la nueva lista en el tiempo siguiente
            v_nuevo = []
            
            for j in range(len(xn)):    # Bucle espacial

                j_p = (j+1) % len(xn)   # Condición de contorno
            #   j_m = (j-1) % len(xn)   # No es necesario, python permite índices negativas: lista[-1] = lista[len(lista)-1]
                
                u_nuevo.append( un[j] + f_mu*(un[j_p]-2*un[j]+un[j-1]) + h_tim*(-7*un[j]*un[j] - 50*un[j]*vn[j] + 57)/32 )
                v_nuevo.append( vn[j] + f_nu*(vn[j_p]-2*vn[j]+vn[j-1]) + h_tim*(+7*un[j]*un[j] + 50*un[j]*vn[j] - 2*vn[j] - 55)/32 )
            
            un = u_nuevo                # Actualiza la nueva fila con los datos en el tiempo j
            vn = v_nuevo
            
            #if i in np.linspace(1000, int(t_f/h_tim), 100): 
            if i in np.logspace(0, 5, 100, dtype = int):        # Para algunos valores de t guarda una imagen de que sucedió
                
                u.append(un)    # Se guardan los datos para el gráfico polar
                v.append(vn)
                
                archivo = "Figuras/"+str(D)+"-"+str(round(tn[i],3))+".png"
                
                plt.figure(figsize = (4.5, 3.8), dpi = 200)
                plt.plot(xn, un, color = 'r', label = r'$u(x,t)$')
                plt.plot(xn, vn, color = 'b', label = r'$v(x,t)$')
                plt.title(rf'$t={str(round(tn[i], 3))}\ {str(int(i))}$')
                plt.xlabel(r'$x$')
                plt.ylabel(r'$u,\ v$')
                plt.legend()
                plt.grid()                          # Activa la grilla
                plt.tight_layout()                  # Recorta los gráficos
                plt.ylim(0.70, 1.30)                # Limita el eje y
                plt.savefig(archivo)
                plt.close()
                
                imagenes.append(archivo)                

        grafica_gif(imagenes, "Figuras/Evolucion-"+str(D)+"-"+str(a)+".gif")
        grafica_polar(u, x_i, x_f, t_i, t_f, "u"+str(D)+"-"+str(a))
        grafica_polar(v, x_i, x_f, t_i, t_f, "v"+str(D)+"-"+str(a))
   
def ejercicio_1():
    
    "Hace uso de lo implementado en turing()"
    
    h_tim = 0.001
    h_esp = 0.01
        
    x_i = 0
    x_f = 1
    t_i = 0
    t_f = 100
        
    a = 0.20
    
    turing(h_tim, h_esp, x_i, x_f, t_i, t_f, a)

""" Descomentar cada instrucción para obtener las gráficas """

#ejercicio_1()