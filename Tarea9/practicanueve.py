# -*- coding: utf-8 -*
import numpy as np
import pandas as pd

n = 50
x = np.random.normal(size = n)
y = np.random.normal(size = n)
c = np.random.normal(size = n)
xmax = max(x)
xmin = min(x)
x = (x - xmin) / (xmax - xmin) # de 0 a 1
ymax = max(y)
ymin = min(y)
y = (y - ymin) / (ymax - ymin)
cmax = max(c)
cmin = min(c)
c = 2 * (c - cmin) / (cmax - cmin) - 1 # entre -1 y 1
g = np.round(5 * c).astype(int)

masaMax = 5
masaMin = 0.01
m = np.random.normal(size=n)                                                #Para generar la masa de cada partícula
mmax = max(m)
mmin = min(m)
m = masaMax * (m - mmin) / (mmax - mmin) + masaMin                          #masa entre masaMin y (masaMax + masaMin), no se permite masa 0

p = pd.DataFrame({'x': x, 'y': y, 'c': c, 'g': g, 'm': m})
paso = 256 // 10
niveles = [ i /256 for i in range(0, 256, paso)]
colores = [(niveles[i], 0, niveles[-(i + 1)]) for i in range(len(niveles))]

import matplotlib.pyplot as plt
import matplotlib.colorbar as colorbar
from matplotlib.colors import LinearSegmentedColormap

palette = LinearSegmentedColormap.from_list('tonos', colores, N = len(colores))

from math import fabs, sqrt, floor, log
eps = 0.001

alfaCarga = 1
alfaMasa = 1
def fuerza(i):
    pi = p.iloc[i]
    xi = pi.x
    yi = pi.y
    ci = pi.c
    fx, fy = 0, 0
    for j in range(n):
        pj = p.iloc[j]
        cj = pj.c
        dire = (-1) ** (1 + (ci * cj < 0))
        dx = xi - pj.x
        dy = yi - pj.y
        factor = dire * fabs(ci - cj) / (sqrt(dx ** 2 + dy ** 2) + eps)
        fx -= dx * factor * alfaCarga
        fy -= dy * factor * alfaCarga

    mi = pi.m
    for j in range(n):                                                                  #Agrego fuerza de atracción debido a la masa
        pj = p.iloc[j]
        mj = pj.m
        dire = 1                                                                        #Siempre hay atracción entre masas, por eso siempre positiva
        dx = xi - pj.x
        dy = yi - pj.y
        factor = dire * (mj*mi) / (sqrt(dx ** 2 + dy ** 2) + eps)                #Se multiplica por la fraccion de peso que representa la particula j con respecto a la suma total de las masas
        fx -= dx * factor * alfaMasa
        fy -= dy * factor * alfaMasa

    return (fx, fy)

from os import popen
tmax = 10
digitos = floor(log(tmax, 10)) + 1
fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = palette)
fig.colorbar(pos, ax=ax)
plt.title('Estado inicial')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
fig.savefig('p9p_t0.png')
plt.close()

def actualiza(pos, fuerza, de):
    return max(min(pos + de * fuerza, 1), 0)

import multiprocessing
from itertools import repeat

if __name__ == "__main__":
    for t in range(tmax):
        for j in range(n):
            f = map(fuerza, range(n))
            delta = 0.2 / max([max(fabs(fx), fabs(fy)) for (fx, fy) in f])
            pi = p.iloc[j]
            fj = fuerza(j)
            p.iloc[j, p.columns.get_loc('x')] = actualiza(pi.x, fj[0], delta)
            p.iloc[j, p.columns.get_loc('y')] = actualiza(pi.y, fj[1], delta)
            print('particula:', j + 1,'paso:', t + 1, 'AlfaCarga:  ', alfaCarga, '  AlfaMasa: ', alfaMasa, '   Velocidad:', sqrt(actualiza(pi.x, fj[0], delta)** 2 + actualiza(pi.y, fj[1], delta)** 2))

        fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
        pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = palette)
        fig.colorbar(pos, ax=ax)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        plt.title('Paso {:d}'.format(t + 1))
        fig.savefig('p9p_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
        plt.close()