n = int(input("Ingrese la cantidad de numeros que debe tener el arreglo: "))
ejercicio1 = []
for i in range(0,n):
    eje1 = int(input("Ingrese un numero: "))
    ejercicio1.append(eje1)    
ordenar = sorted(ejercicio1, reverse=True)
print("El tercer numero mayor es el siguiente: ",ordenar[2])

cantidadImpar = 0
for i in range(0,n):
    if ejercicio1[i] % 2 == 1:
        cantidadImpar = cantidadImpar + 1
print("La cantidad de numeros impares de esta lista son: ",cantidadImpar)

cantidadMayor = 0
for i in range(0,len(ejercicio1) -1):
    if ejercicio1[i -1] > ejercicio1[i]  <ejercicio1[i +1]:
        cantidadMayor = cantidadMayor + 1
print("La cantidad de numeros que estan entre sus mayores son: ",cantidadMayor)