#upper
#lower
#find
#starswith
#endswith
#capitalize

#Operadores de pertenencia
 #in
 #not in


a = 'josesito'

print(a.upper())
print(a.find('s'))
print(a.startswith('j'))  #true
print(a.startswith('x'))  #false
print(a.capitalize())

print(dir(a)) #Nos bota todos los metodos que podemos aplicar a 'a'

def my_function():
    """Este es un texto de ayuda de como utilizar esta fucion"""
    pass

help(my_function)
