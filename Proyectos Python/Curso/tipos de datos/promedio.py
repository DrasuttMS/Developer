foro = []
tarea = []

f = int(input("Ingrese la cantodad de notas a evaluar del foro: "))
for i in range(int(f)):
    nota = float(input(f"Ingrese la nota {i + 1} del foro: "))
    foro.append(nota)

t = int(input("Ingrese la cantidad de notas a evaluar de la tarea: "))
for i in range(int(t)):
    nota = float(input(f"Ingrese la nota {i + 1} de la tarea: "))
    tarea.append(nota)

ef = float(input("Ingrese la nota del examen final: "))

por_foro = sum(foro) / len(foro) * (0.05 * len(foro))
por_tarea = sum(tarea) / len(tarea) * (0.15 * len(tarea))
por_ef = ef * 0.40
promedio = por_foro + por_tarea + por_ef
print(f"El promedio final es: {promedio:.1f}")