lista_numeros = list(range(100))
print(len(lista_numeros))


#HACIENDO UN DICCIONARIO A PARTIR DE 2 LISTAS
student_uid = [1,2,3]
students = ['Juan','Jose','Larsen']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}

print(students_with_uid)

#LLENANDO UNA LISTA DE FORMA RANDOM
import random 
random_numbers= []
for i in range(10):
    random_numbers.append(random.randint(1,3))

print(random_numbers)
print(type(random_numbers))

non_repeated = {number for number in random_numbers}
print(non_repeated)
print(type(non_repeated))




