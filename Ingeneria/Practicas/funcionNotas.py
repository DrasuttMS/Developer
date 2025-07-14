n = int(input("Ingrese el numero de notas a evaluar: "))
def notas(notas):
    for i in range(0,n):
        nota = float(input("Ingrese nota: "))
        notas.append(nota)
        return notas
print(notas)    