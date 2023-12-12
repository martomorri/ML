import numpy as np
# accediendo a un elemento del array
m = np.arange(24).reshape(4,6)
print(m[3][5])
print(m [3,5])
print(m)

# ordenando el array de manera ascendente
m1 = np.array([90,7,2,8,1,4])
print(np.sort(m1))

# encontrar los valores de una matriz elevados a una potencia
m2 = np.array([2,3])
print(np.power(m2,2))

# encontrar el cuadrado de todos los elementos
print(np.square(m2))
print(np.array(m2**2))

# clasificar datos
m3 = np.array([1,2,3,4,5,6])
print(np.array(m3 >= 4))

# encontrar el maximo y el minimo
m4 = np.array([90,2,57,4,2,2,2222,3,5])
print(m4.max())
print(m4.min())

# concatenando 2 matrices
matriz1 = np.array([1,2,3,4,5,6,7])
matriz2 = np.array([99,88,55,25,87])
print(np.concatenate((matriz1,matriz2)))

matriza = np.array([[1,2],[3,4]])
matrizb = np.array([[5,6],[7,8]])
print(matriza + matrizb)
print(matriza + 2)
print(np.add(matriza,matrizb))
print(np.subtract(matriza,matrizb))
print(np.multiply(matriza,matrizb))
print(np.divide(matriza,matrizb))
print(matriza.dot(matrizb))
