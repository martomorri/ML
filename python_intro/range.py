# creamos un rango
print(list(range(0,7)))

# funcion range en un for
for i in range(0, 7):
    print(i, end = ' ')

# range con paso / step
for i in range(2,10,2):
    print("El valor de 'i' es:", i)

# generando un triangulo con range
for num in range(10):
    for i in range(num):
        print('*', end=' ')
    print()

# invirtiendo un rango / palabra reversed
for i in reversed(range(0,10)):
    print(i)

# convirtiendo range a lista
lista = list(range(1,8))
print("lista:", lista)