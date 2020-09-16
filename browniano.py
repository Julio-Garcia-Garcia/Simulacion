from random import random, randint
import math

def paso(pos,dim):
    d=randint(0,dim-1)
    if (random()<0.5):
        pos[d] += -1
    else:
        pos[d] += 1
    return pos


def experimento(largo, dim, dimTotal, vectorPasos):
    pos = [0] * dim
    conteo=0
    for t in range(largo):
        pos=paso(pos,dim)
        conteo+=1
        if all([p==0 for p in pos]):
            vectorPasos[dimTotal]=conteo
            return True

    vectorPasos[dimTotal] = 0
    return False

dim=[]
largo=[]

total=50
for i in range(1, 9):
    regresos = 0
    contador=0
    contadorPasos = []
    for replica in range(total) :
        for larg in range(1,6):
            largo.append(larg)
            dim.append(i)
            contador+=1
            contadorPasos.append(contador)
            regresos += experimento(pow(2, largo[larg-1]+4), dim[i-1], contador-1, contadorPasos)
    print('Probabilidad de regresos: ', regresos / contador, dim[i - 1])
    print('Regresos: ', regresos)
    print('Dimension: ', i)
    print('Vector pasos ', contadorPasos)
    print('Minimo: ', min(contadorPasos))
    print('Maximo: ', max(contadorPasos))
    print('Promedio ', sum( contadorPasos)/len(contadorPasos))






