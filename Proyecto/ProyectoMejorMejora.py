import numpy as np
import random
from time import time
# coding: utf-8
# Your code here!


# listas y objetos de la clase algoritmo
n = 0
P = [range(0) for i in range(0)]
c = 0
alpha = 0

nodos = 0
depot = 0
red = []
redSinDepot = []
solucion = []
solucionesParciales = [range(0) for i in range(0)]
totalDeSoluciones = 0
conjuntoSolucionesP = [range(0) for i in range(0)]
sizeP = 0
solucionTemporal = []

costo = [range(0) for i in range(0)]
costoCandidato = 0
funcionObjetivoConjuntoP = []
mejorCosto =[]
funcionObjetivoParcial=[]
posiciones=[]
funcionCostoParcial =[]
solucionParcial=[]
candidatos=[]
listaDeIndices=[]
listaFuncionesLRC=[]
listaCandidatos=[]



def funcionParcial(inicio, intermedio, final):
    distancia = costo[inicio][intermedio] + costo[intermedio][final] - costo[inicio][final];
    return distancia;


def inicializarSolucionesParciales():
    for i in range(totalDeSoluciones):  # read time matrix
        for j in range(nodos + 2):
            solucionesParciales[i][j] = -1;



# Evaluación de la función objetivo del conjunto P
def evaluacionFuncionObjetivoVersionDos():

    funcionObjetivoConjuntoP[0] = 0;
    # Se calcula la función objetivo de la solución actual
    sumaParcial = 0;
    for j in range(nodos + 1):
        j2 = j + 1;
        sumaParcial = sumaParcial + (nodos + 1 - j) * costo[solucion[j]][solucion[j2]];

    # Se calcula la función objetivo de la solución actual
    sumaParcial2 = 0;
    for j in range(nodos + 1):
        j2 = j + 1;
        sumaParcial2 = sumaParcial2 + (nodos + 1 - j) * costo[conjuntoSolucionesP[0][j]][conjuntoSolucionesP[0][j2]];

    if(sumaParcial<sumaParcial2):
        for k in range(nodos + 2):
            conjuntoSolucionesP[0][k] = solucion[k];
        funcionObjetivoConjuntoP[0]=sumaParcial;
    else:
        funcionObjetivoConjuntoP[0] = sumaParcial2;

#Imprimir solución
def imprimirSolucion():
    # print('SOLUCION:')
    for i in range(nodos + 2):
        print(solucion[i])

def imprimirConjuntoSolucionv2():
    print('SOLUCION:')
    for j in range(nodos + 2):
        print(conjuntoSolucionesP[0][j])


# Se definen los candidatos factibles de una red
def candidatosFactibles(candidatos):
    contador = 0;
    hayCandidatos = False;
    for i in range(nodos):
        estaEnSolucion = False;
        for j in range(nodos + 2):
            if (solucion[j] == redSinDepot[i] and solucion[j] != -1):
                estaEnSolucion = True;
                break;

        if (estaEnSolucion == False):
            candidatos[contador] = redSinDepot[i];
            contador = contador + 1

    if (contador > 0):
        hayCandidatos = True;

    return hayCandidatos;

# Se define la función de latencia
def funcionParcialLatencia(solucion, posicionInsertar, candidato, solucionParcialInsertada, indiceSolucionParcial):

    solucionParcialInsertada = [-1 for i in range(nodos+2)]
    sumaParcial = 0;
    # Vamos a suponer que los costos son asimetricos
    # Copiamos la solución
    for i in range(nodos + 2):
        solucionParcialInsertada[i] = solucion[i];

    if (posicionInsertar < nodos + 2):
        # Se inserta parcialmente el candidato
        solucionParcialInsertada[posicionInsertar + 1] = solucionParcialInsertada[posicionInsertar];
        solucionParcialInsertada[posicionInsertar] = candidato;
        # Cuenta cuantos clientes hay
        totalClientesActivos = 0;
        for i in range(nodos + 2):
            if (solucionParcialInsertada[i] != depot and solucionParcialInsertada[i] != -1):
                totalClientesActivos = totalClientesActivos + 1

        # Se calcula la función objetivo
        for i in range(nodos + 1):
            j = i + 1;
            if (solucionParcialInsertada[i] != -1 and solucionParcialInsertada[j] != -1):
                sumaParcial = sumaParcial + (totalClientesActivos + 1 - i) * costo[solucionParcialInsertada[i]][
                    solucionParcialInsertada[j]];

        for j in range(nodos + 2):
            solucionesParciales[indiceSolucionParcial][j] = solucionParcialInsertada[j];
            #print('   _', solucionesParciales[indiceSolucionParcial][j])

    return sumaParcial;


# Se realizan P-iteraciones para construir soluciones, con GRASP
def conjuntoPGRASP():
    start_time = time()
    for j0 in range(sizeP):
        # Inicializas el vector de solución
        for j in range(nodos + 2):
            solucion[j] = -1;

        # Agregas el origen de la solución
        solucion[0] = depot;
        solucion[1] = depot;
        solucionIncompleta = True;
        posicionPorInsertar = 1;
        while (solucionIncompleta):

            # Inicializamos arreglo de candidatos
            totalCandidatos = 0
            candidatos = [-1 for i in range(nodos)]
            funcionObjetivoParcial = [-1 for i in range(nodos)]
            posiciones = [-1 for i in range(nodos)]


            # Indicamos los candidatos que no han sido ingresados a la solución
            solucionIncompleta = candidatosFactibles(candidatos);
            # Inicializamos arreglo de soluciones
            inicializarSolucionesParciales();

            if (solucionIncompleta):
                indiceSolucionParcial = 0;
                # Se ingresan los candidatos a insertar uno por uno
                for i in range(nodos):

                    solucionParcial = [-1 for i in range(nodos+2)]

                    if (candidatos[i] != -1):
                        # cout<<"Candidato: "<<candidatos[i]<<endl;
                        funcionParcial = funcionParcialLatencia(solucion, posicionPorInsertar, candidatos[i],
                                                                solucionParcial, indiceSolucionParcial);
                        funcionObjetivoParcial[indiceSolucionParcial] = funcionParcial;
                        # cout<<"Funcion parcial: "<<funcionParcial<<endl;
                        # cout<<"Solucion Parcial: "<< indiceSolucionParcial<<endl;
                        indiceSolucionParcial = indiceSolucionParcial + 1

                posicion = seleccionLRC(funcionObjetivoParcial);
                # cout<<"Candidato: "<<posicion<<endl;
                if (posicion != -1):
                    for j in range(nodos + 2):
                        solucion[j] = solucionesParciales[posicion][j];

                #imprimirSolucion();
                posicionPorInsertar = posicionPorInsertar + 1

        # Llamamos a la mejora
        #mejoraLSII();
        mejoraLS_FM();
        #mejoraLS_PM();
        # Se guarada la solución mejorada
        if(j0==0):
            for k in range(nodos + 2):
                conjuntoSolucionesP[j0][k] = solucion[k];

        evaluacionFuncionObjetivoVersionDos();
    #evaluacionFuncionObjetivo();
    #imprimirConjuntoSolucionv2();
    elapsed_time = time() - start_time
    print(" Alpha:  ", alpha, " Iteraciones:  ", sizeP, 'Función objetivo:     ', funcionObjetivoConjuntoP[0], 'Tiempo Total:   ', elapsed_time, ' seg')

# Método de mejora, criterio de mejor mejora,
# Una sola pasada hacia enfrente
def mejoraLSII():
    # Suponemos que la solución ya esta construida
    for i in range(nodos + 1):
        # Comparamos el costo parcial de cambiar la pareja del índice "i", "i+1", con la solución actual
        # Costo (i-1, i) +  Costo (i, i +1)
        costU1 = 0
        costU2 = 0
        if (i + 2 >= nodos + 1):
            costU1 = 0;
            costU2 = 0;
        else:
            costU1 = costo[solucion[i + 1]][solucion[i + 2]];
            costU2 = costo[solucion[i]][solucion[i + 2]];

        if (costo[solucion[i - 1]][solucion[i]] + costo[solucion[i]][solucion[i + 1]] + costU1 >
                costo[solucion[i - 1]][solucion[i + 1]] + costo[solucion[i + 1]][solucion[i]] + costU2):
            # Se guarda variables auxiliares
            aux1 = solucion[i];
            aux2 = solucion[i + 1];
            # Se realiza el cambio de nodos
            solucion[i] = aux2;
            solucion[i + 1] = aux1;

# Método de mejora, criterio de mejor mejora,
# Una sola pasada hacia enfrente
def mejoraLS_FM():
    # Suponemos que la solución ya esta construida
    for i in range(nodos + 1):
        # Comparamos el costo parcial de cambiar la pareja del índice "i", "i+1", con la solución actual
        # Costo (i-1, i) +  Costo (i, i +1)
        solucion2 = [i + 1 for i in range(nodos+2)]
        # Igualamos, el cambio a la actual
        for k in range(nodos + 2):
            solucion2[k] = solucion[k];

        if(i>0 and i+1<nodos+1):
            # Se guarda variables auxiliares
            aux1 = solucion2[i];
            aux2 = solucion2[i + 1];
            # Se realiza el cambio de nodos
            solucion2[i] = aux2;
            solucion2[i + 1] = aux1;
            # Se calcula la función objetivo de la solución actual
            sumaParcial = 0;
            for j in range(nodos + 1):
                j2 = j + 1;
                sumaParcial = sumaParcial + (nodos + 1 - j) * costo[solucion[j]][solucion[j2]];

            # Se calcula la función objetivo de la solución actual
            sumaParcial2 = 0;
            for j in range(nodos + 1):
                j2 = j + 1;
                sumaParcial2 = sumaParcial2 + (nodos + 1 - j) * costo[solucion2[j]][solucion2[j2]];

            if(sumaParcial2<sumaParcial):
                for k in range(nodos + 2):
                    solucion[k] = solucion2[k];

#Método de mejora, a la primer mejora lo revienta
def mejoraLS_PM():
    # Suponemos que la solución ya esta construida
    sePudo =False;
    for i in range(nodos + 1):
        if(sePudo==True):
            break;
        # Comparamos el costo parcial de cambiar la pareja del índice "i", "i+1", con la solución actual
        # Costo (i-1, i) +  Costo (i, i +1)
        solucion2 = [i + 1 for i in range(nodos + 2)]
        # Igualamos, el cambio a la actual
        for k in range(nodos + 2):
            solucion2[k] = solucion[k];

        if (i > 0 and i + 1 < nodos + 1):
            # Se guarda variables auxiliares
            aux1 = solucion2[i];
            aux2 = solucion2[i + 1];
            # Se realiza el cambio de nodos
            solucion2[i] = aux2;
            solucion2[i + 1] = aux1;
            # Se calcula la función objetivo de la solución actual
            sumaParcial = 0;
            for j in range(nodos + 1):
                j2 = j + 1;
                sumaParcial = sumaParcial + (nodos + 1 - j) * costo[solucion[j]][solucion[j2]];

            # Se calcula la función objetivo de la solución actual
            sumaParcial2 = 0;
            for j in range(nodos + 1):
                j2 = j + 1;
                sumaParcial2 = sumaParcial2 + (nodos + 1 - j) * costo[solucion2[j]][solucion2[j2]];

            if (sumaParcial2 < sumaParcial):
                for k in range(nodos + 2):
                    solucion[k] = solucion2[k];
                sePudo=True;

def seleccionLRC(listaDeFuncionObj):
    # Se inicializan valores minimos y máximos
    minimo = 999999
    maximo = 0
    candidato = -1;
    # Lista de indices de la solución
    listaDeIndices= [i for i in range(totalDeSoluciones)]
    listaCandidatos=[-1 for i in range(totalDeSoluciones)]
    #for j in range(totalDeSoluciones):
    #    listaDeIndices[j] = j;

    #for j in range(totalDeSoluciones):
    #    listaCandidatos[j] = -1;

    # Encontrar el máximo y minimo
    for i in range(totalDeSoluciones):
        if (listaDeFuncionObj[i] > -1 and listaDeFuncionObj[i] < minimo):
            minimo = listaDeFuncionObj[i];

        if (listaDeFuncionObj[i] > -1 and listaDeFuncionObj[i] > maximo):
            maximo = listaDeFuncionObj[i];

    # Selección de lista de candidatos restrindigos
    conteo = 0;
    for i in range(totalDeSoluciones):
        if (listaDeFuncionObj[i] > -1 and listaDeFuncionObj[i] <= minimo + alpha * (maximo - minimo)):
            listaCandidatos[conteo] = i;
            conteo = conteo + 1

    seleccionado = random.randrange(conteo);
    if (seleccionado >= 0 and conteo > 0):
        candidato = seleccionado;
    else:
        candidato = -1;

    return candidato;


from scipy.stats import describe  # instalar con pip3
from random import shuffle
import multiprocessing
from time import time
from multiprocessing import Pool
from multiprocessing import cpu_count

if __name__ == "__main__":
    #leer_instancia()
    # LEER NODOS
    costo = np.loadtxt('instancia3.txt', skiprows=0)
    fic = open("instancia3.txt", "r")
    print(costo)

    nodos = np.shape(costo)[0] - 1
    print('nodos: ', nodos)
    replicas = 5;
    # Se inicializa la red, con depot
    for r2 in range(3):
        print("Nucleos  ", r2 + 1)
        with Pool(r2 + 1) as p:
            for r in range(replicas):
                alphaMuestra =0;
                while alphaMuestra <=1:
                    tamanoMuestra =1000;
                    while tamanoMuestra <=5000:
                        red = [i for i in range(nodos + 1)]

                        # Se inicializa la red, sin depot
                        redSinDepot = [i + 1 for i in range(nodos)]

                        # Se inicializa el arreglo solución
                        solucion = [-1 for i in range(nodos + 2)]

                        # Solucion temporal
                        solucionTemporal = [-1 for i in range(nodos + 2)]

                        # El depot es el nodo inicia
                        depot = red[0];

                        # Total de soluciones máximo
                        totalDeSoluciones = nodos;

                        # A lo más hay "total de Soluciones"

                        # time matrix
                        solucionesParciales = [ [-1 for i in range(nodos + 2)] for j in range(totalDeSoluciones)]
                        # Tamaña de P
                        sizeP = tamanoMuestra;
                        # Dimensión del conjunto P
                        conjuntoSolucionesP = [[-1 for i in range(nodos+2)] for j in range(2)]

                        # Funcion objetivo del conjunto "P"
                        funcionObjetivoConjuntoP = [0 for i in range(2)]

                        alpha = alphaMuestra;  # Entre cero y uno
                        #print("Replica:  ", r2 + 1, " Alpha:  ", alpha, " Iteraciones:  ", sizeP)
                        conjuntoPGRASP()
                        tamanoMuestra =tamanoMuestra+1000;
                    alphaMuestra=alphaMuestra+0.1;