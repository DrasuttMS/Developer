mascotas = [
    "Wolfgang", 
    "Pelusa", 
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"]

mascotas.insert(1, "Melvin") # Inserta en el indice proporcionado
mascotas.append("Chanchito triste") # Inserta al final del arreglo o lista

mascotas.remove("Pulga") # Elimina la primera incidencia con el valor proporcionado
mascotas.pop() #Elimina el ultimo elemento de la lista
mascotas.pop(1) # Elimina el elemento segun el indice proporcionado
del mascotas[0] # Elimina el elemento segun el indice proporcionado
mascotas.clear() # blanquea todo el arreglo
print(mascotas)