# la diferencia entre listas y arrays es que un array tiene datos del mismo tipo mientras que en una lista no es necesario
# lista: coleccion de elementos
# array: estructura de datos, independientes, que ocupan un determinado espacio de memoria, por esto no se les puede añadir elementos
# arrays puede manejar operaciones aritmeticas directas, lists no
# listas: pocos elementos // arrays: muchos elementos

# generando un array con el modulo array
import array as arr
matriz1 = arr.array('i',[1,2,3,4,5,6])
for arr in matriz1:
    print(arr)
    
# generando un array con el modulo numpy
import numpy as np
matriz = np.array([1,2,3,4,5,6])
print(matriz)

lista = [1,3,5]
array = np.array([2,4,6])
lista.append(7)
print(lista)
# array.append(8) no funciona
array += np.array([8])      # de esta manera le sumamos 8 a cada uno de los elementos del array x separado
print(array)

a = [1,2,3]
b = [4,5,6]
print(a+b)      #no suma las listas las junta

a1 = np.array([1,2,3])
b1 = np.array([4,5,6])
print(a1)
print(b1)
print(a1 + b1)
print(a1 * b1)
