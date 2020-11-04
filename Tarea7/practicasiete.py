import matplotlib.pyplot as plt
from random import uniform
import numpy as np
import math as ma 


# ligeros cambios con respecto al código de la Dra. Elisa,  agrego el término ma.sin(1000 * x * y) para meter ruido con la interacción de x con y.
# se eligió ese término porque si ponia solo el ma.sin(x * y) se estancaba muy fácil el mejor encontrado
def g(x, y):
    return (ma.sin(1000 * x * y) * ((x + 0.5) ** 4 - 30 * x ** 2 - 20 * x + (y + 0.5) ** 4 - 30 * y ** 2 - 20 * y) / 100)


low = -3
high = 3
step = 0.25
tmax = 15


if __name__ == "__main__":
    currx = uniform(low, high)
    curry = uniform(low, high)
    [bestx, besty] = [currx, curry]
    for iteracion in range(tmax):
        deltax = uniform(0, step)
        lx = currx - deltax  # left X
        lx = low if lx < low else lx  # mantenerse dentro del rango -3,3
        rx = currx + deltax  # right X
        rx = high if rx > high else rx  # mantenerse dentro del rango -3,3
        deltay = uniform(0, step)
        dy = curry - deltay  # down Y
        dy = low if dy < low else dy  # mantenerse dentro del rango -3,3
        uy = curry + deltay  # up Y
        uy = high if uy > high else uy  # mantenerse dentro del rango -3,3

        # Tarea 7 dice que hay 8 posiciones vecino, solo encontre 4 (izqArriba, izqAbajo, derArriba, derAbajo)
        [currx, curry] = [lx, dy] if g(lx, dy) > g(lx, uy) else [lx, uy]  # comparo los dos de lx
        [currx, curry] = [currx, curry] if g(currx, curry) > g(rx, uy) else [rx, uy]  # comparo el actual contra rx,uy
        [currx, curry] = [currx, curry] if g(currx, curry) > g(rx, dy) else [rx, dy]  # comparo el actual contra rx,dy, ya tengo las 4 comparaciones

        if g(currx, curry) > g(bestx, besty):  # MAXIMIZAR: se actualiza el mejor encontrado si el movimiento actual encontró un mejor valor de la función f
            [bestx, besty] = [currx, curry]

        #grafica
        p = np.arange(low - step, high + step, step)  # agregué -step, +step, para que el rango incluya en la grafica el low y el high
        n = len(p)
        z = np.zeros((n, n), dtype=float)    #La cuadrícula es de nxn, osea de [0,n] en x, de [0,n] en y
        for i in range(n):
            x = p[i]
            for j in range(n):
                y = p[n - j - 1]  # voltear la y ******
                z[i, j] = g(x, y)  # calcula el valor para cada punto de la cuadrícula

        icurrent = currx // step - low // step  # hay que transladar la x a que embone con la cuadricula de [0,n]
        jcurrent = curry // step - low // step  # hay que transladar la y a que embone con la cuadricula de [0,n]

        ibest = bestx // step - low // step
        jbest = besty // step - low // step

        t = range(0, n, 5)
        l = ['{:.1f}'.format(low + i * step) for i in t]
        fig, ax = plt.subplots(figsize=(6, 6), ncols=1)
        pos = ax.imshow(z)
        plt.xticks(t, l)
        plt.yticks(t, l[::-1])  # arriba-abajo
        ax.scatter(icurrent, n - jcurrent - 1, marker='d', color='deeppink', s=60.0)    # marca d diamante para el punto actual, voltear la y ******
        ax.scatter(ibest, n - jbest - 1, marker='*', color='r', s=100.0)           # marca * estrella para el punto mejor encontrado, voltear la y ******
        fig.colorbar(pos, ax=ax)
        plt.title('{:d} iteracion'.format(iteracion))
        fig.savefig('p7p_{:d}.png'.format(iteracion), bbox_inches='tight')
        plt.close()