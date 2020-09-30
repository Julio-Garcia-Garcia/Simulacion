import numpy as np # hay que instalar numpy a parte con pip3 o algo similar
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt

dim = 20
num = dim**2
#valores = [round(random()) for i in range(num)]
# Población aleatoria con Distribución de probabilidad de 0.1 <= x <= 0.9;
# Aumenta de 0.1 en 0.1
valores = [0] * num
valAnterior = [0] * num
valNuevo = [0] * num
prob=0.1
for t in range(num):
    if random()<prob:
        valores[t]=1
    prob +=0.1
    if(prob>=1):
        prob=0.1

actual = np.reshape(valores, (dim, dim))
anterior = np.reshape(valores, (dim, dim))
contador = np.reshape(valAnterior, (dim, dim))


def mapeo(pos):
    fila = pos // dim
    columna = pos % dim
    return actual[fila, columna]

assert all([mapeo(x) == valores[x]  for x in range(num)])

def paso(pos):
    fila = pos // dim
    columna = pos % dim
    vecindad = actual[max(0, fila - 1):min(dim, fila + 2),
                      max(0, columna - 1):min(dim, columna + 2)]
    return 1 * (np.sum(vecindad) - actual[fila, columna] == 3)

print(actual)
# Función para contabilizar cuando una celda sigue viva, un contador de matrices
def conteo(matAnt, matNueva):
    for i in range(dim):
        for j in range(dim):
            if(matAnt[i-1,j-1]== matNueva[i-1,j-1] ==1):
                contador[i-1,j-1]= contador[i-1,j-1]+1
            else:
                contador[i, j] =0
    return np.amax(contador)

if __name__ == "__main__":
    fig = plt.figure()
    plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
    fig.suptitle('Estado inicial')
    plt.savefig('p2_t0_p.png')
    plt.close()
    maximo=0
    maximoAbsoluto=0
    for iteracion in range(50):
        print("Iter", iteracion)
        valores = [paso(x) for x in range(num)]
        vivos = sum(valores)
        print(iteracion, vivos)
        if vivos == 0:
            print('# Ya no queda nadie vivo.')
            break;
        actual = np.reshape(valores, (dim, dim))
        print(actual)
        maximo= conteo(anterior, actual)
        if(maximoAbsoluto<maximo):
            maximoAbsoluto=maximo
        print('Maximo Relativo ', maximo)
        # Copia el arreglo actual en el anterior
        for i in range(dim):
            for j in range(dim):
                anterior[i - 1, j - 1] = actual[i - 1, j - 1]
        #anterior = [x[:] for x in actual]
        fig = plt.figure()
        plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
        fig.suptitle('Paso {:d}'.format(iteracion + 1))
        plt.savefig('p2_t{:d}_p.png'.format(iteracion + 1))
        plt.close()
    print('Maximo Absoluto ', maximoAbsoluto)
# para crear un GIF, se puede usar ImageMagick con
# convert -delay 100 -size 300x300 -loop 0 p2_t*.png p2p.gif