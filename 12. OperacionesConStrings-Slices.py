#SLICES
#Permiten manipular secuencias.
#secuencia[comienzo:final:pasos]  La posicion final no lo considera.

my_name = 'David'
print(my_name[0]) #D
print(my_name[-1]) #d
print(my_name[0:3]) #Dav
print(my_name[::2]) #Dvd

fruit = 'banana'
print(fruit[3:3])  #No sale nada
print(fruit[:])  #banana
print(fruit[1:-1]) #anan
print(fruit[1:-1:2]) #aa

long_word = 'ferrocarril'
print(long_word[1:4])
print(long_word[1:8])
print(long_word[::-1]) #Se voltea el orden de una palabra
print(long_word[:8:3]) #fra
print(long_word[::2])


