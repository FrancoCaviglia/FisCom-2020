# -*- coding: utf-8 -*-

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


fig, (ax_1, ax_2) = plt.subplots(2,1, sharex = True, gridspec_kw={'height_ratios': [1, 1]})

fig.set_figheight(4)
fig.set_figwidth(7.2)
        
plt.sca(ax_1)

datos = np.loadtxt("2-1.450000-1-1312934972.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 0.2)

datos = np.loadtxt("2-1.500000-0-1477982928.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 1, label = r'$T=1.50\pm 0.05$')

datos = np.loadtxt("2-1.550000-0-1477782780.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 0.2)


datos = np.loadtxt("2-2.300000-0-1600899119.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 0.2)

datos = np.loadtxt("2-2.350000-0-1600899063.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 1, label = r'$T=2.35\pm 0.05$')

datos = np.loadtxt("2-2.400000-0-1341117432.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 0.2)


datos = np.loadtxt("2-4.400000-0-503344376.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 0.2)

datos = np.loadtxt("2-5.000000-0-503344376.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 1, label = r'$T=5.00\pm 0.60$')

datos = np.loadtxt("2-5.600000-0-503344376.txt", delimiter = ' ').T[1]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 0.2)

plt.ylabel(r'\textrm{Magnetizacion  }$M/N^{2}$')


plt.sca(ax_2)


datos = np.loadtxt("2-1.450000-1-1312934972.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 0.2)

datos = np.loadtxt("2-1.500000-0-1477982928.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 1, label = r'$T=1.50\pm 0.05$')

datos = np.loadtxt("2-1.550000-0-1477782780.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'b', alpha = 0.2)


datos = np.loadtxt("2-2.300000-0-1600899119.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 0.2)

datos = np.loadtxt("2-2.350000-0-1600899063.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 1, label = r'$T=2.35\pm 0.05$')

datos = np.loadtxt("2-2.400000-0-1341117432.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'g', alpha = 0.2)


datos = np.loadtxt("2-4.400000-0-503344376.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 0.2)

datos = np.loadtxt("2-5.000000-0-503344376.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 1, label = r'$T=5.00\pm 0.60$')

datos = np.loadtxt("2-5.600000-0-503344376.txt", delimiter = ' ').T[0]/16384
plt.plot(list(range(10000)), datos, color = 'r', alpha = 0.2)

plt.xlabel(r'\textrm{Tiempo }$t$')
plt.ylabel(r'\textrm{Energía }$E/N^{2}$')
plt.legend(loc = 'upper right')


plt.tight_layout(pad = 0.02)
plt.xlim((-100,10000))

plt.subplots_adjust(left = 0.10, right = 0.97, bottom = 0.09, top = 0.995, hspace = 0.029)
plt.savefig("evolucion.png", dpi = 600)
plt.show()
plt.close()



fig, ax = plt.subplots(3,3)

fig.set_figheight(7)
fig.set_figwidth(7)

#          ["G-1.550000-0-1477782780.txt", ax[2][0]],

for x in [["G-1.450000-1-1312934972.txt", ax[0][0]],
          ["G-1.500000-0-1477982928.txt", ax[1][0]],
          ["G-2.300000-0-1600899119.txt", ax[0][1]],
          ["G-2.350000-0-1600899063.txt", ax[1][1]],
          ["G-2.400000-0-1341117432.txt", ax[2][1]],
          ["G-4.400000-0-503344376.txt",  ax[0][2]],
          ["G-5.000000-0-503344376.txt",  ax[1][2]],
          ["G-5.600000-0-503344376.txt",  ax[2][2]]]:
    
    estado = np.loadtxt(x[0], delimiter = ' ')
    plt.sca(x[1])
    plt.imshow(estado, cmap = 'binary', vmin = -1, vmax = 1, extent = [0, 128, 0, 128])
    plt.xticks([])
    plt.yticks([])
    #plt.xlabel(r'\textrm{Coordenada }$x$')
    #plt.ylabel(r'\textrm{Coordenada }$y$')

estado = np.loadtxt("G-1.550000-0-1477782780.txt", delimiter = ' ')
plt.sca(ax[2][0])
plt.imshow(estado, cmap = 'binary', vmin = -1, vmax = 1, extent = [0, 128, 0, 128])
plt.xticks([0, 32, 64, 96, 128])
plt.yticks([0, 32, 64, 96, 128])
    
plt.subplots_adjust(hspace = 0, wspace = 0)
plt.tight_layout(pad = 0.18)
plt.savefig("estados.png", dpi = 600)
plt.show()
plt.close()
