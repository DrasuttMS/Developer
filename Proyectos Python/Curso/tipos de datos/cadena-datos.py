valor1 = "Maximiliano Salas"
valor2 = "Maria Vargas"
valor3 = "Antonella Salas"

mayusc = valor1.upper() # Convierte valor1 a mayúsculas
print(mayusc)
minusc = valor2.lower() # Convierte valor2 a minúsculas
print(minusc)
camel = valor3.capitalize() # Convierte valor3 a formato capitalizado
print(camel)

busqueda_find = valor1.find("Salas") # Busca la posición de "Salas" en valor1
print(busqueda_find)

busqueda_index = valor2.index("Vargas") # Busca la posición de "Vargas" en valor2
print(busqueda_index)

numero = "1234567890"
numero.isnumeric()  # Verifica si es un número
print(numero.isnumeric())

dato = "MaxSalas"
dato.isalpha()  # Verifica si es alfabético
print(dato.isalpha())

contar = valor1.count("a") # Cuenta cuántas veces aparece 'a' en valor1
print(contar)

contar_caracteres = len(valor2) # Cuenta la longitud de valor2
print(contar_caracteres)

empieza_con = valor3.startswith("Antonella") # Verifica si valor3 empieza con "Antonella"
print(empieza_con)

termina_con = valor1.endswith("Salas") # Verifica si valor1 termina con "Salas"
print(termina_con)

reemplazar = valor1.replace("Maximiliano", "Max") # Reemplaza Maximiliano por Max en valor1
print(reemplazar)

separar = valor2.split(" ") # Separa valor2 por espacios
print(separar)
print(type(separar))
print(separar[0])  # Imprime el primer elemento de la lista resultante
print(separar[1])  # Imprime el segundo elemento de la lista resultante