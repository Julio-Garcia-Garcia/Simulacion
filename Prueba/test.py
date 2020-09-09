import math
x=2
y=3
datos = [3,7,1,8]
print("3x2= ",x*y)
print(datos)
print("Primer dato de la lista: ",datos[0])
print("Ultimo dato de la lista: ",datos[-1])
print("Tamaño: ",len(datos))
print("Minimo: ",min(datos))
print("Maximo: ",max(datos))
print("Ordenados: ",sorted(datos))


data = [2,5,3,1,9,2,5]

print(math.pi)

def doble(x):
    return  2*x

print(doble(3))
from random import random
print(random())

muchos=[random() for i in range(2000)]
print(len(muchos))
print(muchos)
print(min(muchos))

x=12
y=8
if x<y:
    print('x es menor')
else:
    print('el menor es: ',y)
lista2=[1,4,7]
for elemento in lista2:
    print(2**elemento)