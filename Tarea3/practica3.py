from math import ceil, sqrt


def primo(n):
    if n < 4:
        return True
    if n % 2 == 0:
        #print(" ", n)
        return False
    for i in range(3, int(ceil(sqrt(n))), 2):
        if n % i == 0:
            #print(" ", n)
            return False
    return True

# Función para lectura de vectores
def lectura():
    datos2 = []
    with open('primes3.txt','r') as input:
        linea= input.readline()
        datos2=   [int (valor) for  valor  in linea.split(',') ]
    return datos2

def proporcionPrimos(Vector):
    contador=0
    for i in range(len(Vector)):
        if(primo(Vector[i-1])):
            contador=contador+1
    return contador


from scipy.stats import describe  # instalar con pip3
from random import shuffle
import multiprocessing
from time import time
from multiprocessing import Pool
from multiprocessing import cpu_count
if __name__ == "__main__":
    datos =[]
    # Se leen los datos de un archivo txt separaco en comas
    datos = lectura()
    desde = datos[0]
    # se disminuye el hasta, si solo queremos 1710 números
    #hasta = datos[0] + 1709 #MOVER A Chamba facil2, 1710 números
    #hasta = datos[ len(datos) - 1] # MOVER CUANDO SE NECESITE TODOS LOS Números Chamba facil3 desde el primer primo hasta el último primo
    # Con chambas "faciles", se usan los primos de cada documento de Primes.txt + los números entre el primo menor y primo mayor
    #datosIniciales = [x for x in range(desde, hasta + 1)]#Chamba facil 2, 3,
    # Solo chambas "dificiles", sólo usamos los primos de los documentos
    datosIniciales = datos.copy() #MOVER A Chamba dificil, 1710 números,
    invertido = datosIniciales[::-1]
    aleatorio = datosIniciales.copy()
    replicas = 10
    tiempos = {"ot": [], "it": [], "at": []}
    # Se realiza un ciclo usando desde "uno" hasta "n-1" nucleos, esto debido a la recomendación de la Dra.
    for r2 in range(cpu_count() - 1):
        print("Nucleos  ", r2+1)
        # Se usa en el "pool" el o los nucleos necesarios
        with Pool(r2+1) as p:
            # Se hacen la cantidad de replicas necesarios
            for r in range(replicas):
                t = time()
                # Se ejecuta la rutina en orden ascendente
                p.map(primo, datosIniciales)
                tiempos["ot"].append(time() - t)
                t = time()
                # Se ejecuta la rutina en orden descendente
                p.map(primo, invertido)
                tiempos["it"].append(time() - t)
                shuffle(aleatorio)
                t = time()
                # Se ejecuta la rutina en orden aleatorio
                p.map(primo, aleatorio)
                tiempos["at"].append(time() - t)
        for tipo in tiempos:
            print(describe(tiempos[tipo]))
    print("Proporcion Primos  ",proporcionPrimos(datosIniciales)/len( datosIniciales))
    print("Total de números  ", len(datosIniciales))