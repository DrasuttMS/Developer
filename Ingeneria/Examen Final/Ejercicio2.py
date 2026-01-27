agua = []

n = int(input("Ingrese el número de mediciones a ingresar: "))
while n <= 0:
    print("El número de mediciones debe ser mayor que 0")
    n = int(input("Ingrese el número de mediciones a ingresar: "))

for i in range(0,n):
    medicion = int(input(f"Ingrese la medición {i + 1}: "))
    
    while medicion < 0 or medicion > 150:
        print("Error, ingrese una medida en el intervalo de 0 a 150.")
        medicion = int(input(f"Ingrese la medición {i + 1}: "))
    agua.append(medicion)
print(f"El promedio de agua caída es: ", sum(agua)/n)
