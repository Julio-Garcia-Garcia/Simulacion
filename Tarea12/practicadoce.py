from random import randint
from math import floor, log
import pandas as pd
import numpy as np

valores = [ 0.3, 0.6, 0.9]
for negro in valores:
    for gris in valores:
        for blanco in valores:
            for numReplica in range(3):
                modelos = pd.read_csv('digits.txt', sep=' ', header=None)
                #modelos = modelos.replace({'n': 0.99, 'g': 0.97, 'b': 0.002})
                modelos = modelos.replace({'n': negro, 'g': gris, 'b': blanco})
                r, c = 5, 3
                dim = r * c

                tasa = 0.15
                tranqui = 0.99
                tope = 9
                k = tope + 1  # incl. cero
                contadores = np.zeros((k, k + 1), dtype=int)
                n = floor(log(k - 1, 2)) + 1
                neuronas = np.random.rand(n, dim)  # perceptrones
                for t in range(5000):  # entrenamiento
                    d = randint(0, tope)
                    pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                    correcto = '{0:04b}'.format(d)
                    for i in range(n):
                        w = neuronas[i, :]
                        deseada = int(correcto[i])  # 0 o 1
                        resultado = sum(w * pixeles) >= 0
                        if deseada != resultado:
                            ajuste = tasa * (1 * deseada - 1 * resultado)
                            tasa = tranqui * tasa
                            neuronas[i, :] = w + ajuste * pixeles

                for t in range(300):  # prueba
                    d = randint(0, tope)
                    pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                    correcto = '{0:04b}'.format(d)
                    salida = ''
                    for i in range(n):
                        salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                    r = min(int(salida, 2), k)
                    contadores[d, r] += 1

                score = 0
                for i in range(k):
                    score += contadores [i, i]                  #la diagonal principal tiene los aciertos

                print(negro,    gris,  blanco,  score,    sum(sum(contadores)),     numReplica+1)

                #c = pd.DataFrame(contadores)
                #c.columns = [str(i) for i in range(k)] + ['NA']
                #c.index = [str(i) for i in range(k)]
                #print(c)

