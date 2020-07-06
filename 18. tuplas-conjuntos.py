#-----TUPLAS------
#Tuplas: Inmutables
#Listas: Mutables
#Las tuplas son similares a las listas
tup = (1,1,1,4,2,3)
print(tup[0]) #1
print(tup[1]) #1
print(tup[2]) #1

print(tup.count(1)) #Botaria 3 ya q el 1 se repite 3 veces
print(tup.index(4)) #3 Nos da el indice del elemento 4
#tup[0] = 13 #Saldria error ya q es inmmutable

#Lo utilizamos para RETORNAR 2 O MÁS VALORES

#------CONJUNTOS-------
#Similares a las LISTAS, pero en CONJUNTOS no pueden existir elementos duplicados
#A diferencia de las TUPLAS, los CONJUNTOS si son mutables

a = {1,2,3}
b = {3,4,5}
 #Operaciones
print(a.intersection(b))  #{3}
print(a.difference(b))  #{1, 2}

c= set([1,2,3])
d={3,4,5}
print(type(c))
print(type(d))

#NO SE PUEDE ACCEDER A UN SET POR UN INDICE
#print(c[0]) saldria error

c.add(20)
print(c) #{1, 2, 3, 20}
d.remove(4)
print(d) #{3, 5}
print(dir(c))