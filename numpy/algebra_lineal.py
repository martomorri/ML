import numpy as np
# m = np.array([[1,-1,2],[3,2,0]])
# print(m)
# print()
# # matriz de una sola columna
# m1 = np.array([[1],[2],[3]])
# print(m1)
# # matriz transpuesta
# print(np.transpose(m1))

# # resolver sistemas de ecuaciones
# A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
# print(A)
# print()
# B = np.array([[-3],[5],[-2]])
# print(B)
# print(np.transpose(B))
# print()
# x = np.linalg.solve(A,B)
# print(x)
# # comprueba si la solucion es correcta
# print(np.allclose(np.dot(A,x),B))

m1 = np.array([[2,7,3],[2,8,2],[1,3,1]])
m2 = np.array([1,1,0])
# otra manera de cambiar la direccion de la matriz
m2.shape=(3,1)
print()
print(np.linalg.solve(m1,m2))