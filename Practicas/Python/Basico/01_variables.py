#Variables
#Por convencion se debiese utilizar letras minusculas y guion bajo para separar palabras

my_int_variable = 5
print(my_int_variable)

my_int_variable = str(my_int_variable) #Convertir a string
print(type(my_int_variable))

my_bool_variable = False
print(type(my_bool_variable))
my_bool_variable = int(my_bool_variable) #Convertir a entero
print(type(my_bool_variable))

#Concetenacion de variables
print("mi variable entera transformada a texto es: " + my_int_variable + " " + str(my_bool_variable))

firstname = "Maximiliano"
lastname = "Salas"

print("Mi nombre es: " + firstname + " " + lastname)

fullname = firstname + " " + lastname
print(fullname)

#Input, sirve para ingresar datos por consola
age = input("Ingrese su edad: ")
print("Mi nombre es: " + fullname + " y mi edad es: " + age)

