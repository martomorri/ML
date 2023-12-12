import numpy as np
# matriz 2d
matriz2d = np.array([[1,2,3],[4,5,6]])
print(matriz2d)

# matriz con lista
lista = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(lista)
print(matriz)

# np.arange(cant_elementos).reshape(num_filas, num_columnas)
# el numero de filas y de columnas debe tener como producto el numero de elementos del array
m = np.arange(15).reshape(3,5)
# una matriz tiene sus metodos
# shape devuelve las filas y columnas de la matriz
print(m.shape)
# ndim devuelve el numero de dimensiones de la matriz
print(m.ndim)
# size devuelve el numero de elementos que contiene la matriz
print(m.size)
print(m)

# np.zeros(num_filas, num_columnas) rellena la matriz de ceros
zeros = np.zeros((3,4))
print(zeros)

# np.linspace(num_iniio, num_fin, num_elementos) genera una matriz con numeros aleatorios
linspace = np.linspace(99,88,25)
print(linspace)

matrix3d = np.arange(27).reshape(3,3,3)
print(matrix3d.ndim)
print(matrix3d)