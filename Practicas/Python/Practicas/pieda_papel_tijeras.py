import random
opciones = ['piedra', 'papel', 'tijeras']
print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
while True:
    eleccion_usuario = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
    if eleccion_usuario == 'salir':
        print("Gracias por jugar. ¡Hasta luego!")
        break
    if eleccion_usuario not in opciones:
        print("Elección inválida. Por favor, elige piedra, papel o tijeras.")
        continue

    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("¡Empate!")
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        