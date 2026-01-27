import random

minimo = 1
maximo = 10

numero_secreto = random.randint(minimo, maximo)
intentos = 0
max_intentos = 5
print("¡Bienvenido al juego de adivinar el número!")
print(f"He seleccionado un número entre {minimo} y {maximo}. Tienes {max_intentos} intentos para adivinarlo.")
while intentos < max_intentos:
    intento = input(f"Intento {intentos + 1}: ¿Cuál es tu número? ")
    try:
        intento = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break