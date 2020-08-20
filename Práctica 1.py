# -*- coding: utf-8 -*-

"""
Created on Sat Aug 15 15:57:52 2020

@author: Franco Caviglia

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time

def ejercicio_1():
    
    x_1 = np.float32(np.pi/6) # Punto de evaluación en simple precisión
    x_2 = np.float32(np.pi/6) # Punto de evaluación en doble precisión
    
    y_1 = np.cos(x_1)   # Valor que se desea estimar en simple precisión
    y_2 = np.cos(x_2)   # Valor que se desea estimar en doble precisión
    
    yA_1 = []
    yB_1 = []
    yC_1 = []
    
    yA_2 = []
    yB_2 = []
    yC_2 = []
    
    h_1 = []
    h_2 = []
    
    for i in range(100):
     
        h = np.float32(10**(-(i-10)/10))
        h_1.append(h)
        yA_1.append(abs( (np.sin(x_1+h)-np.sin(x_1))/h - y_1))
        yB_1.append(abs( (np.sin(x_1+2*h)-np.sin(x_1-2*h))/(2*h) - y_1))
        yC_1.append(abs( (-np.sin(x_1+2*h)+np.sin(x_1+h)-np.sin(x_1-1)+np.sin(x_1-2*h))/(12*h) - y_1))
        
        h = np.float64(10**(-(i-10)/10))
        h_2.append(h)
        yA_2.append(abs( (np.sin(x_2+h)-np.sin(x_2))/h - y_2))
        yB_2.append(abs( (np.sin(x_2+2*h)-np.sin(x_2-2*h))/(2*h) - y_2))
        yC_2.append(abs( (-np.sin(x_2+2*h)+np.sin(x_2-h)-np.sin(x_2-1)+np.sin(x_2-2*h))/(12*h) - y_2))

    plt.rc('text', usetex=True)
#    plt.rc('font', family='serif')
    
    plt.rc('font', size=9)       
    plt.rc('axes', titlesize=9)
    plt.rc('axes', labelsize=9)
    plt.rc('xtick', labelsize=9)
    plt.rc('ytick', labelsize=9)
    plt.rc('legend', fontsize=9)
    plt.rc('figure', titlesize=9)
    
    fig = plt.figure(figsize=(4.4, 3.2))

    if logx:
        plt.xscale('log')
        
    plt.plot(cord_x, cord_y, 'b')#, label=referencia)
    #plt.title(r'\textrm{'+encabezado+'}', fontsize=9)
    #plt.xlabel(r'\textrm{'+leyenda_x+'}', fontsize=9)
    #plt.ylabel(r'\textrm{'+leyenda_y+'}', fontsize=9)
    plt.margins(0.01)
    plt.grid()
    plt.tight_layout()
 
    
    plt.figure()
    plt.plot(h_1, yA_1, marker = "v", markersize = 2, color = 'b')
    plt.plot(h_1, yB_1, marker = "o", markersize = 2, color = 'b')
    plt.plot(h_1, yC_1, marker = "s", markersize = 2, color = 'b')
    plt.plot(h_2, yA_2, marker = "v", markersize = 2, color = 'r')
    plt.plot(h_2, yB_2, marker = "o", markersize = 2, color = 'r')
    plt.plot(h_2, yC_2, marker = "s", markersize = 2, color = 'r')
    plt.title("Ejercicio 1")
    plt.xlabel("Paso h")
    plt.ylabel("Error absoluto e")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid()
    plt.show()

#ejercicio_1()

def oscilador(x_0, p_0, h):
    
    x = [x_0]
    p = [p_0]
    t = [0]
    e = [(x_0**2+p_0**2)/2]
    
    for i in range(int(31/h)):
        
        x.append(x[-1]+h*p[-1])
        p.append(p[-1]-h*x[-1])
        e.append((x[-1]**2+p[-1]**2)/2)
        t.append(i*h)
        
    return x, p, e, t
    
def ejercicio_2():
    
    x_1, p_1, e_1, t_1 = oscilador(1, 1, 0.001)
    x_2, p_2, e_2, t_2 = oscilador(1, 1, 0.010)
    x_3, p_3, e_3, t_3 = oscilador(1, 1, 0.100)
    x_4, p_4, e_4, t_4 = oscilador(1, 1, 1.000)

    plt.figure()
    plt.plot(x_1, p_1, markersize = 0.5, color = 'b', label = "h=0.001")
    plt.plot(x_2, p_2, markersize = 1.0, color = 'r', label = "h=0.010")
    plt.plot(x_3, p_3, markersize = 1.5, color = 'g', label = "h=0.100")
    plt.plot(x_4, p_4, markersize = 2.0, color = 'm', label = "h=1.000")
    plt.title("Ejercicio 1")
    plt.xlabel("x(t)")
    plt.ylabel("p(t)")
    plt.legend()
    plt.grid()
    plt.show()    
    
    plt.figure()
    plt.plot(t_1, e_1, markersize = 0.5, color = 'b', label = "h=0.001")
    plt.plot(t_2, e_2, markersize = 1.0, color = 'r', label = "h=0.010")
    plt.plot(t_3, e_3, markersize = 1.5, color = 'g', label = "h=0.100")
    plt.plot(t_4, e_4, markersize = 2.0, color = 'm', label = "h=1.000")
    plt.title("Ejercicio 1")
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.legend()
    plt.grid()
    plt.show()  
    
def modelo(x_0, y_0, a, b, h, N):
    
    x = [x_0]
    y = [y_0]
     
    for i in range(N):
        
        k_1 = [h*( a-(b+1)*x[-1]           +(x[-1]**2)*y[-1]),                       h*(b*x[-1]-(x[-1]**2)*y[-1]) ]
        k_2 = [h*( a-(b+1)*(x[-1]+k_1[0]/2)+((x[-1]+k_1[0]/2)**2)*(y[-1]+k_1[1]/2)), h*(b*(x[-1]+k_1[0]/2)-((x[-1]+k_1[0]/2)**2)*(y[-1]+k_1[1]/2)) ]
        k_3 = [h*( a-(b+1)*(x[-1]+k_2[0]/2)+((x[-1]+k_2[0]/2)**2)*(y[-1]+k_2[1]/2)), h*(b*(x[-1]+k_2[0]/2)-((x[-1]+k_2[0]/2)**2)*(y[-1]+k_2[1]/2)) ]
        k_4 = [h*( a-(b+1)*(x[-1]+k_3[0])  +((x[-1]+k_3[0]  )**2)*(y[-1]+k_3[1])  ), h*(b*(x[-1]+k_3[0])  -((x[-1]+k_3[0]  )**2)*(y[-1]+k_3[1])  ) ]
        
        x.append(x[-1]+(k_1[0]+2*(k_2[0]+k_3[0])+k_4[0])/6)
        y.append(y[-1]+(k_1[1]+2*(k_2[1]+k_3[1])+k_4[1])/6)
                
    return x, y

def ejercicio_3_b():
    
    plt.figure()

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.10), 1000)
    plt.plot(x, y, markersize = 0.5, color = 'b', label = "h=0.10")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.15), 500)
    plt.plot(x, y, markersize = 1.0, color = 'r', label = "h=0.15")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.20), 200)
    plt.plot(x, y, markersize = 1.5, color = 'g', label = "h=0.20")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.25), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.25")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.30), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.30")
    
    plt.title("Ejercicio 3 - B")
    plt.xlabel("x(t)")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid()
    plt.show()  
        
    plt.figure()

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.10), 1000)
    plt.plot(x, y, markersize = 0.5, color = 'b', label = "h=0.10")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.15), 500)
    plt.plot(x, y, markersize = 1.0, color = 'r', label = "h=0.15")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.20), 200)
    plt.plot(x, y, markersize = 1.5, color = 'g', label = "h=0.20")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.25), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.25")
    
    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.30), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.30")
    
    plt.title("Ejercicio 3 - A")
    plt.xlabel("x(t)")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid()
    plt.show()  

    plt.figure()

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.10), 1000)
    plt.plot(x, y, markersize = 0.5, color = 'b', label = "h=0.10")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.15), 500)
    plt.plot(x, y, markersize = 1.0, color = 'r', label = "h=0.15")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.20), 200)
    plt.plot(x, y, markersize = 1.5, color = 'g', label = "h=0.20")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.25), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.25")

    x, y = modelo(np.float64(3.0), np.float64(3.0), 1, 3, np.float64(0.30), 100)
    plt.plot(x, y, markersize = 2.0, color = 'm', label = "h=0.30")

    plt.title("Ejercicio 3 - A")
    plt.xlabel("x(t)")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid()
    plt.show()  

def modelo_adapatativo(x_0, y_0, a, b, h, e, factor):
    
    x = [x_0]
    y = [y_0]
    t = [0]
    
    while t[-1] <= 10:
        
        x_1, y_1 = modelo(x[-1], y[-1], a, b,   h, 1)
        x_m, y_m = modelo(x[-1], y[-1], a, b, h/2, 1)
        x_2, y_2 = modelo(x_m[-1], y_m[-1], a, b, h/2, 1)
        
        delta_1 = abs(x_2[-1]-x_1[-1])
        delta_2 = abs(y_2[-1]-y_1[-1])            
        
        while delta_1 > e or delta_2 > e:
                        
            h = h/factor
            
            x_1, y_1 = modelo(x[-1], y[-1], a, b,   h, 1)
            x_m, y_m = modelo(x[-1], y[-1], a, b, h/2, 1)
            x_2, y_2 = modelo(x_m[-1], y_m[-1], a, b, h/2, 1)
            
            delta_1 = abs(x_2[-1]-x_1[-1])
            delta_2 = abs(y_2[-1]-y_1[-1])
        
        x.append(x_2[-1])
        y.append(y_2[-1])
        t.append(t[-1]+h)

        if delta_1 < e/2 and delta_2 < e/2:
            h = factor*h
        
    return x, y, t

"""
start_time = time.time()    
ejercicio_4(e = np.float64(0.00001))
end_time = time.time()

print("Tiempo de ejecución:", round(end_time - start_time, 3) )

start_time = time.time()    
ejercicio_4(e = np.float64(0.0001))
end_time = time.time()

print("Tiempo de ejecución:", round(end_time - start_time, 3) )

start_time = time.time()    
ejercicio_4(e = np.float64(0.001))
end_time = time.time()

print("Tiempo de ejecución:", round(end_time - start_time, 3) )

start_time = time.time()
ejercicio_4(e = np.float64(0.01))
end_time = time.time()

print("Tiempo de ejecución:", round(end_time - start_time, 3) )

"""

e_list = [np.float64(0.00000001), np.float64(0.00000002), np.float64(0.00000005), np.float64(0.00000008),
          np.float64(0.0000001),  np.float64(0.0000002),  np.float64(0.0000005),  np.float64(0.0000008),
          np.float64(0.000001),   np.float64(0.000002),   np.float64(0.000005),   np.float64(0.000008),
          np.float64(0.00001),    np.float64(0.00002),    np.float64(0.00005),    np.float64(0.00008),
          np.float64(0.0001),     np.float64(0.0002),     np.float64(0.0005),     np.float64(0.0008),
          np.float64(0.001),      np.float64(0.002),      np.float64(0.005),      np.float64(0.008),
          np.float64(0.01),       np.float64(0.02),       np.float64(0.05),       np.float64(0.08),
          np.float64(0.1),        np.float64(0.2),        np.float64(0.5),        np.float64(0.8)]

time_list = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
              [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(1600):
    for j in range(len(e_list)):
        
        start_time = time.time()    
        ejercicio_4(e=e_list[j])
        tiempo = time.time() - start_time
     
        time_list[j].append(tiempo)
            
e_list.reverse()

for i in range(1600):
    for j in range(len(e_list)):
        start_time = time.time()    
        ejercicio_4(e=e_list[j])
        tiempo = time.time() - start_time

        time_list[len(e_list)-1-j].append(tiempo)
 
print("e_list:",e_list)
print("time_list",time_list)
for i in range(len(time_list)):
    time_list[i] = sum(time_list[j])/len(time_list[j])
print("time_list 2", time_list)
"""
plt.figure()
plt.plot(e_list.reverse(), time_list)
plt.xscale('log')
plt.show()
"""