import random

def tirar_dados(veces):
    frecuencias = {i: 0 for i in range(1, 7)}
    if veces <= 0:
        return "Error: EL numero de lanzamientos debe ser mayor a 0."
    for _ in range(veces):
        resultado = random.randint(1, 6)
        frecuencias[resultado] += 1
    for cara, frecuencias in frecuencias.items():
        porcentaje = (frecuencias / veces) * 100
        print(f"Porcentaje de veces que salio la cara {cara}: {porcentaje: 2f}%")
        
tirar_dados(10000)
