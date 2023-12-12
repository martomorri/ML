#Los conjuntos o sets en python es una coleccion de datos que no se repiten y no se pueden modificar
set1 = {1,2,3,4,5}
set1.add(6)
#set1.clear()
set1.discard(2)     #discard no lo borra, lo descarta nada mas
set1.remove(5)
#print(set1)

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A | B)        #une todos los datos (pero no los repite) / union
print(A & B)        #es como un inner join (solo los datos que coincidan) / interseccion
print(A - B)        #es como el left o right join (trae los datos que no coinciden de alguno de los sets) / diferencia
print(B - A)
print(A ^ B)        #trae todos menos los que coinciden / diferencia simetrica