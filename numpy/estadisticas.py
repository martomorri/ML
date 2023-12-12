import numpy as np
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print()
# valor max en el eje 1
print(np.amax(m,1))
# valor min en el eje 0
print(np.amin(m,0))
# rango (max-min)
print(np.ptp(m, axis=1))
print(np.ptp(m, axis=0))
# percentil (q*(n+1)/100), solo funciona cuando N es impar
print(np.percentile(m, 50, axis=0))
# mediana ((n+1)/2)
print(np.median(m))
# media aritmetica ((x1+x2+...+xn)/n) --> promedio
print(np.mean(m))

matriz = np.array([1,2,3,4,5,6])
# promedio ponderado ((x1*p1+...xn*pn)/sum(p)) p por defecto es 1
print(np.average(matriz))

# desviacion estandar
print(np.std(matriz))