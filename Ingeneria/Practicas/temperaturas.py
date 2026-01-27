n = int(input("Ingrese la cantidad de a temperaturas a registrar  --> "))
temperaturas = []
print("===")
for i in range(0,n):
    temp = float(input("Ingrese temperatura --> "))
    temperaturas.append(temp)
print("===")
suma = sum(temperaturas)
promedio = suma/n
print("El promedio de temperaturas es --> ",promedio)
print("===")
cantidad = 0
for i in range(0,n):
    if(temperaturas[i]<promedio):
        cantidad = cantidad + 1
print("Hay ",cantidad," temperaturas bajo el promerdio")
print("===")
