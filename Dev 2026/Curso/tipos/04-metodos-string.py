animal = "   Chanchito feliz    "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.capitalize())  # Capitaliza la primera letra
print(animal.title())  # Capitaliza la primera letra de cada palabra
print(animal.strip())  # Elimina espacios en blanco al inicio y al final
print(animal.strip().capitalize())  # Elimina espacios en blanco al inicio y al final, luego capitaliza la primera letra
print(animal.lstrip())  # Elimina espacios en blanco al inicio
print(animal.rstrip())  # Elimina espacios en blanco al final
print(animal.find("feliz"))  # Devuelve el índice de la primera aparición de "feliz", si devuelve -1 si no se encuentra
print(animal.replace("Chanchito", "Perrito"))  # Reemplaza "Chanchito" por "Perrito"
print(animal.split())  # Divide la cadena en una lista de palabras
print("feliz" in animal)  # Verifica si "feliz" está en la cadena, devuelve True o False
print("feliz" not in animal)  # Verifica si "feliz" no está en la cadena, devuelve True o False