lista = [1, 2, 3, 4]
print(lista)
print(*lista)

lista2 = [5, 6]

combinada = ["hola", *lista,"mundo", *lista2, "chanchito"]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2, "z": "mundo"}
print(nuevoPunto)