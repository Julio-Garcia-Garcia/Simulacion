import numpy as np
import pandas as pd
from random import random, randint, sample
from time import time
import matplotlib.pyplot as plt


def knapsack(peso_permitido, pesos, valores):
    assert len(pesos) == len(valores)
    peso_total = sum(pesos)
    valor_total = sum(valores)
    if peso_total < peso_permitido:
        return valor_total
    else:
        V = dict()
        for w in range(peso_permitido + 1):
            V[(w, 0)] = 0
        for i in range(len(pesos)):
            peso = pesos[i]
            valor = valores[i]
            for w in range(peso_permitido + 1):
                cand = V.get((w - peso, i), -float('inf')) + valor
                V[(w, i + 1)] = max(V[(w, i)], cand)
        return max(V.values())


def factible(seleccion, pesos, capacidad):
    return np.inner(seleccion, pesos) <= capacidad


def objetivo(seleccion, valores):
    return np.inner(seleccion, valores)


def normalizar(data):
    menor = min(data)
    mayor = max(data)
    rango = mayor - menor
    data = data - menor  # > 0
    return data / rango  # entre 0 y 1

#opcion 0 es lo original del código, cada opcion 1,2,3 son las de la tarea (respectivamente)
def generador_pesos(cuantos, low, high, opcion):
    if opcion == 0:
        return np.round(normalizar(np.random.normal(size=cuantos)) * (high - low) + low)
    elif opcion == 1 or opcion == 2 or opcion == 3:
         return np.round(normalizar(np.random.exponential(1, size=cuantos)) * (high - low) + low)                       #Dist exponencial

# opcion 0 es lo original del código, cada opcion 1,2,3 son las de la tarea (respectivamente)

def generador_valores(pesos, low, high, opcion):
    ruido = low / 2                                                                                                     #Para cuando se ocupa el ruido de baja magnitud
    n = len(pesos)
    valores = np.empty((n))
    if opcion == 0:
        for i in range(n):
            valores[i] = np.random.normal(pesos[i], random(), 1)
        return normalizar(valores) * (high - low) + low
    elif opcion == 1:
        for i in range(n):
            valores[i] = np.random.exponential(1,size=1)                                                                #Dist exponencial
        return normalizar(valores) * (high - low) + low
    elif opcion == 2:
        for i in range(n):
            valores[i] = np.random.normal(pesos[i], random(), 1)                                                        #correlacionada con los pesos
        return normalizar(valores) * (high - low) + low + ruido*np.random.normal(size=1)                               #reuido de baja magnitud
    elif opcion == 3:
        for i in range(n):
            valores[i] = np.random.normal(1 / pesos[i], random(), 1)                                                    #inversamente correlacionada con los pesos   (1 / peso)
        return normalizar(valores) * (high - low) + low + ruido*np.random.normal(size=1)                               #reuido de baja magnitud



def poblacion_inicial(n, tam):
    pobl = np.zeros((tam, n))
    for i in range(tam):
        pobl[i] = (np.round(np.random.uniform(size=n))).astype(int)
    return pobl


def mutacion(sol, n):
    pos = randint(0, n - 1)
    mut = np.copy(sol)
    mut[pos] = 1 if sol[pos] == 0 else 0
    return mut


def reproduccion(x, y, n):
    pos = randint(2, n - 2)
    xy = np.concatenate([x[:pos], y[pos:]])
    yx = np.concatenate([y[:pos], x[pos:]])
    return (xy, yx)

def seleccion_de_ruleta():
    suma = 0
    for i in range(tam):
        suma += objetivo(p[i], valores) + factible(p[i], pesos, capacidad) * min_
    num_random = np.random.uniform(0, suma)
    suma_actual = 0
    for i in range(tam):                                                                                    #seleccionar el primer padre
        suma_actual += objetivo(p[i], valores) + factible(p[i], pesos, capacidad) * max_
        if suma_actual > num_random:
            x=i
            y=i
            break
    while ( y==x ):                                                                                          #seleccionar el segundo padre
        num_random = np.random.uniform(0, suma)
        suma_actual = 0
        for i in range(tam):
            suma_actual += objetivo(p[i], valores) + factible(p[i], pesos, capacidad) * max_
            if suma_actual > num_random:
                y=i
                break
    return (x, y)



n = 50

for opcionPadres in range(2):
    print(opcionPadres)
    print(opcionPadres)
    for opcion in range(4):
        for p in range(5, 11):
            start_time = time()
            n = 2**p
            pesos = generador_pesos(n, 15, 80, opcion)
            min_ = 10
            max_ = 500
            valores = generador_valores(pesos, min_, max_,opcion)
            capacidad = int(round(sum(pesos) * 0.65))
            optimo = knapsack(capacidad, pesos, valores)
            init = 200
            p = poblacion_inicial(n, init)
            tam = p.shape[0]
            assert tam == init
            pm = 0.05
            rep = 50
            tmax = 50
            mejor = None
            mejores = []
            for t in range(tmax):
                for i in range(tam):  # mutarse con probabilidad pm
                    if random() < pm:
                        p = np.vstack([p, mutacion(p[i], n)])
                for i in range(rep):  # reproducciones

                    if opcionPadres == 0:
                        padres = sample(range(tam), 2)                                          #seleccion random de padres, original
                    else:
                        padres = seleccion_de_ruleta()                                          #llamado a seleccion de ruleta

                    hijos = reproduccion(p[padres[0]], p[padres[1]], n)
                    p = np.vstack([p, hijos[0], hijos[1]])
                tam = p.shape[0]
                d = []
                for i in range(tam):
                    d.append({'idx': i, 'obj': objetivo(p[i], valores),
                              'fact': factible(p[i], pesos, capacidad)})
                d = pd.DataFrame(d).sort_values(by=['fact', 'obj'], ascending=False)
                mantener = np.array(d.idx[:init])
                p = p[mantener, :]
                tam = p.shape[0]
                assert tam == init
                factibles = d.loc[d.fact == True,]
                mejor = max(factibles.obj)
                mejores.append(mejor)
            elapsed_time = time() - start_time
            print(optimo, mejor, (optimo - mejor) / optimo, opcion , n, elapsed_time)
