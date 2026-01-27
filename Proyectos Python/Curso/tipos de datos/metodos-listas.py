lista = list(["Max","salas","castillo"]) # Crea una lista con los elementos "Max", "salas", "castillo"
print(lista)

reultado = len(lista)  # Cuenta la cantidad de elementos en la lista
print(reultado)

agregar = lista.append("Python")  # Agrega "Python" al final de la lista
print(lista)

agregar_inicio = lista.insert(0, "Programacion")  # Inserta "Programacion" al inicio de la lista
print(lista)

agregar_varios = lista.extend(["Java", "C++"])  # Agrega varios elementos al final de la lista
print(lista)    

eliminar = lista.pop(4)  # Elimina el elemento de la lista
print(eliminar) 

eliminar = lista.pop(-1)  # Elimina el último elemento de la lista
print(eliminar) 

eliminar = lista.remove("Max")  # Elimina "Max" de la lista
print(lista)

eliminar_todo = lista.clear()  # Elimina todos los elementos de la lista
print(lista)

num = list([11,241,45,56,67,887,8,9])  # Crea una lista de números
print(num)  

ordenar = num.sort()  # Ordena la lista de números
print(num)
invertir = num.reverse()  # Invierte el orden de la lista de números
print(num)