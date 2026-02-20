total = 0.0

while True:
    precio = input("Introduce el precio del producto o 'fin' para terminar: ")
    if precio.lower() == 'fin':
        break
    total += float(precio)
print(f"El total a pagar  es {total:.2f} dolares")