a = 2
b = 3
c = a + b
print(c)

nombre = "Max"
print(nombre)

# variables: corresponden a datos que se pueden modificar a lo largo del codigo, las variables siempre deben ser declaradas y se definen
numero = 10
numero += 1
print(numero)

# concatenacion
nombre = "Max "
bienvenida = "hola " + nombre + "¿Como estas?"
print(bienvenida)

# Concatenacion con f string, toma un dato y lo convierte a texto
nombre = "Max Salas"
bienvenida = f"Hola {nombre} ¿Como estas"
print(bienvenida)

# eliminar el contenido de una variable
# del bienvenida
print(bienvenida)

# buscar e imprimir verdadero o falso segun encuentre o no un texto en una variable, operadores de pertenencia (in / not in) verdadero o falso
print("Max" in bienvenida)

# camelCase nombreCompleto MaximilianoSalasCastillo
# snake_case nombre_completo Maximiliano_salas_castillo -> Recomendacion en Python