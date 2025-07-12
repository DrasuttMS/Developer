miLista = [3,12,5,1,7,8,2,9,0,4,2,13,23,6]
print(miLista)
miLista.append(55) #Agrega el 55 al final
print(miLista)
suma = sum(miLista) #Suma todos los elementos de mi lista
print(suma) 
largo = len(miLista) #Guarda la cantidad de registros que tiene mi lista
print(largo)
miLista.pop() #Elimina el ultimo registro de mi lista
print(miLista)
miLista.pop(1) #Elimina el contenido del indice 1, en este caso con la lista original es el 12
print(miLista)
miLista.remove(2) #Elimina el primero registro que coincida con el dato proporcionado
print(miLista)
minimo = min(miLista) #Obtine el valor menor de la lista, en este caso 0
print(minimo)
maximo = max(miLista) #Obtinee el valor maximo de la lista, en este caso 23
print(maximo)