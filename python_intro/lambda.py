# lambda es una funcion anonima / sin nombre
doble = lambda x: x*2
print(doble(20))

# lambda con filter
lista = [1,2,3,2,4,56,8,65,43,2,9]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

# lambda con map
lista = [1,2,3,2,4,56,8,65,43,2,9]
dobles = list(map(lambda x: x * 2, lista))
print(dobles)