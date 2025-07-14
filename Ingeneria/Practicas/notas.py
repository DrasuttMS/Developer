acumulado_notas = 0
notas_validas = 0

for i in range(0,3):
    nota = float(input(f"Ingrese nota {i + 1}: "))

    while nota < 1.0 or nota > 7.0:
        print("Ingrese una nota valida. Reintente. ")
        nota = float(input(f"Ingrese nota {i +1 }: "))

    acumulado_notas += nota
    notas_validas += 1

if notas_validas >0:
    promedio = acumulado_notas / notas_validas
    print(f"El promedio de las tres notas validas ingresadas es: {promedio}")
else:
    print("No se ingresaron notas validas")
print(notas_validas)
