my_string = 'Mi String'
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "Este es un string\tcon tabulación"
print(my_tab_string)

my_scape_string = "\\Este es un string \\n escapado"
print(my_scape_string)

#Formateo

name, surname, age = "Maximiliano", "Salas", 32

print("Mi nombre es {}, mi apellido es {} y tengo {} años".format(name, surname, age))
print("Mi nombre es %s, mi apellido es %s y tengo %d años" % (name, surname, age))
print(f"Mi nombre es {name}, mi apellido es {surname} y tengo {age} años")

#Desempaquetado de caracteres
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#División

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-3]
print(languaje_slice)


#Reverse 
languaje_reverse = languaje[::-1]
print(languaje_reverse)

#Funciones

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print(languaje.lower()) 
print(languaje.startswith("Py"))
print(languaje.replace("thon", "py"))
print(languaje.upper().isupper())