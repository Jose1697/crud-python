#ESTRUCTURAS DE DATOS-LISTAS
#Al igual que los strings, las LISTAS son secuencias de valores. Ejemplos:
#   [2,5,6]
#   ['Colombia','Mexico','Argentina']
#   ['tacos',3,'arepas',6,'chorizo',9]
#Las listas son mutables
import copy

countries = ['Mexico','Venezuela','Colombia','Argentina']
ages = [12,18,24,34,50]
receta = ['Ensalada', 2, 'lechugas', 5, 'jitomates']

countries[0]='Peru'
print(countries) #['Peru', 'Venezuela', 'Colombia', 'Argentina']

global_countries = countries  #SE COPIAN PERO AL MODIFICAR UNO EL OTRO TAMBIEN SE MODIFICA.

countries[0]='Guatemala'

print(countries) #['Guatemala', 'Venezuela', 'Colombia', 'Argentina']
print(global_countries) #['Guatemala', 'Venezuela', 'Colombia', 'Argentina']

#Como hacer para evitar eso?

paises = copy.copy(countries) #ASI SE COPIA LAS LISTAS PARA EVITAR EL PROBLEMA DE ARRIBA
print(paises) #['Guatemala', 'Venezuela', 'Colombia', 'Argentina']
countries[0] = 'Bolivia'
print(countries) #['Bolivia', 'Venezuela', 'Colombia', 'Argentina']
print(paises)  #['Guatemala', 'Venezuela', 'Colombia', 'Argentina']

#CICLAR EN UNA LISTA
for country in countries:
    print(country)





