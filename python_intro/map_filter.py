# la funcion map genera una lista
def mult(n):
    return n*5

lista = [1,2,3,4,5,6,7]
lista_map = list(map(mult, lista))
print(lista_map)

def cursos(c):
    return c.upper()

tupla = ("php","python","java","csharp")
print(tuple(map(cursos, tupla)))

# filter genera una lista filtrada
def impares(n):
    if n % 2 == 1:
        return n

numeros = [1,2,3,4,5,6,7,8,9]
print(f"numeros impares: {list(filter(impares, numeros))}")