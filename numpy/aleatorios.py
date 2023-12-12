import numpy as np
# creamos una matriz de 2 filas y 5 columnas de numeros enteros aleatorios del 0 al 10 (sin incluir)
r = np.random.randint(10, size=(2,5))
print(r)

# matrices con numeros decimales (del 0 al 1) aleatorios
matriz = np.random.rand(2,2)
print(matriz)

# devolver un solo valor aleatorio de una matriz ya creada
m = np.random.choice([1,2,3,4,5], size=(2,3))
print(m)

# podemos asignarle una probabilidad
matrix = np.random.choice([4,2,8,10], p=[0.4,0.3,0.2,0.1], size=[50])
print(matrix)