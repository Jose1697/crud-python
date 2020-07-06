#Asociacion entre llaves y valores. Similar a un objeto
productos = {}
productos['leche'] = 23.50

#Para generar ciclos a traves de diccionarios
  #Podemos ciclar a lo largo de las llaves  ------> keys
  #Podemos ciclar a lo largo de los valores  -------> values
  #Podemos ciclar a lo largo de llaves y valores  ------> items


rae = {}

rae['pizza'] = 'La comida mas deliciosa del mundo'
print(rae)

rae['pasta'] = 'La comida mas sabrosa de italia'
print(rae)

print(rae['pizza']) #La comida mas deliciosa del mundo

#rae['helado'] #Error ya que no existe ello en el diccionario 
a = rae.get('helado',None) #Para manejar el error en caso helado no exista en el diccionario
print(a) #None


#Iterar a lo largo de diccionario
print(rae.keys())  #dict_keys(['pizza', 'pasta'])
print(rae.values())  #dict_values(['La comida mas deliciosa del mundo', 'La comida mas sabrosa de italia'])
print(rae.items()) #dict_items([('pizza', 'La comida mas deliciosa del mundo'), ('pasta', 'La comida mas sabrosa de italia')])

for key in rae.keys():
    print(key)


for value in rae.values():
    print(value)

for key, value in rae.items():
    print(key,value)


print(rae.__dir__())







