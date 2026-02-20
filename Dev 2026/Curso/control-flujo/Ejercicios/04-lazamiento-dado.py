import random
lanzamientos = int(input("¿Cuantas veces lanzaras el dado? "))

if lanzamientos <=0:
    print("EL numero de lanzamietnos debe ser mayor a 0")
    exit()

resultados = [0] * 6

for i in range(lanzamientos):
    cara = random.randint(1, 6)
    resultados[cara - 1] += 1

if lanzamientos == 1:
    print(f"Salio la cara: {cara}")
else:
    for i in range(6):
        porcentaje = (resultados[i] / lanzamientos) * 100
        print(f"Procentaje de veces que salio la cara {i+1}: {porcentaje:.2f}%")