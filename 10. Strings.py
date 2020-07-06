country = 'Colombia'

print(country[0])  #C
print(country[-1])  #a
print(country[-2])  #i

print(len(country))  #8


second_letter = country[1]
print(second_letter)
print(id(second_letter)) #Nos lanza la direccio en memoria de la variable

other_var = 'o'
print(id(other_var)) #Nos lanza la misma direccion de memoria que second letter
#Aunque son variables diferentes estan apuntando al mismo lugar.
#La C mayuscula y minuscula se ubican en direcciones distintas



#Los strings son inmutables
country1 = 'mexico'
print(id(country1))
country1 += 's'
print(country1) #mexicos
print(id(country1))  #La direccion de memoria cambio 
#Significa que si modificamos un caracter el objeto cambia de lugar




