x = int(input("Ingrese el numero para la tabla de multiplicar: "))
n = int(input("Ingrese hasta que numero desea visualizar la tabla: "))

for i in range(1,n+1):
    resultado = x * i
    print(f"{x} * {i} = {resultado}")