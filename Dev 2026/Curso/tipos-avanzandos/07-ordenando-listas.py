numeros = [2, 4, 1, 6 , 46 ,22]

numeros.sort() #lista ordenada
print(numeros)

numeros.sort(reverse =True) #lista ordenada descendente
print(numeros)

numeros2 =sorted(numeros, reverse=True) # sorted genera una nueva lista y no orderna la lista 
print(numeros2)

usuarios = [
    [4, "Chanchito"], 
    [1, "Felipe"],
    [5, "Pulga"]
    ]

usuarios.sort()
print(usuarios)

usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1],
    ["Pulga", 5]
    ]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse=True)
print(usuarios)

usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)

#Funciones lambda son funciones anonimas