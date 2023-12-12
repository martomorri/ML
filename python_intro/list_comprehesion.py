# crear una lista a partir de otra

# como dividir una palabra con un for
lista = []
for char in 'python':
    lista.append(char)
print(lista)
# con list comprehesion
lista = [char for char in 'python']
print(lista)

# una lista con los multiplos de otra lista
lista_a = [1,2,3,4,5,6]
print(lista_a)
lista_b = [i * 2 for i in lista_a]
print(lista_b)