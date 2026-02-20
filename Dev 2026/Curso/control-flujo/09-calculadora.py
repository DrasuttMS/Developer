print("Bienvenidos a la calculadora")
print("Para salid escribe Salir")
print("Las operaciones son suma, multi, div y resta ")

operacion =""
n1 = 0

while operacion.lower() != "salir":
    if n1 == 0:
        n1 = int(input("Ingresa un numero: "))
    else:
        operacion = input("Ingrese operacion: ")
        if operacion.lower() == "suma":
            n2 = int(input("Ingrese el siguiente numero: "))
            n1 += n2
            print(f"El resultado es: {n1}")
        elif operacion.lower() == "resta":
            n2 = int(input("Ingrese el siguiente numero: "))
            n1 -= n2
            print(f"El resultado es: {n1}")
        elif operacion.lower() == "div":
            n2 = int(input("Ingrese el siguiente numero: "))
            n1 /= n2
            print(f"El resultado es: {n1}")
        elif operacion.lower() == "multi":
            n2 = int(input("Ingrese el siguiente numero: "))
            n1 *= n2
            print(f"El resultado es: {n1}")
        elif operacion.lower() == "salir":
            break
        else:
            print("Operacion no valida, intenta de nuevo")