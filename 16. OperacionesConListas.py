# +  (suma)
a = [1,2]
b = [2,3]

print(a+b)  #[1,2,2,3]


# * (multiplicacion)
c = [5, 6]
print(c*3) #[5, 6, 5, 6, 5, 6]

#Añadir un elemento al final de la lista
d = [3,5,7]
d.append(9)
print(d) #[3, 5, 7, 9]
print(len(d)) #4 el tamaño de la lista

#Para sacar el ultimo elemento de la lista, tambien se puede utilizar un indice
e = [3,9,10,11]
f = e.pop() #Elimina el 11 y lo guarda en f
print(f)
print(e) #[3, 9, 10]

#Si quieres eliminar y sabes el indice puedes utilizar 'del'
g = [4,8,12,16,17.19]
del g[3] #se tendria que eliminar 16
print(g) #[4, 8, 12, 17.19]

#Si quieres eliminar y sabes que elemento quieres eliminar pero no su indice: 'remove'
paises = ['peru','chile','argentina','uruguay']
paises.remove('chile')

print(paises) #['peru', 'argentina', 'uruguay']

#ordenar en una lista: sorted
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0, 15))
print(random_numbers)   #[6, 13, 11, 12, 2, 6, 12, 13, 14, 5]
ordered_numbers = sorted(random_numbers) #Sirve para ordenar
print(ordered_numbers)  #[2, 5, 6, 6, 11, 12, 12, 13, 13, 14]

nombres = ['zeze','juanita','piero','alejo']
nombres_ordenados = sorted(nombres)
print(nombres_ordenados) #['alejo', 'juanita', 'piero', 'zeze']

#lista.sort  ----> ordena la lista



