import numpy as np
m = np.array([[1,1],[1,1]])
m2 = np.array([[8,8],[8,8]])
print(m, "\n")
# axis significa el eje en el que ejecutaremos la funcion
# axis = 0 --> columna // axis = 1 --> fila
print(np.sum(m, axis=0))
print(np.sum(m, axis=1))
print()
print(np.concatenate([m, m2], axis=0))
print(np.concatenate([m, m2], axis=1))