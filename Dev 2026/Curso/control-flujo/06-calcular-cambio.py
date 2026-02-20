total = float(input("Introduce el valor total del cobro: $"))
pago = float(input("Introduce el monto de pago: $"))

if total <= 0 or pago <= 0:
    print(f"El total de la cuenta y el pago deben ser mayor que 0.")
    exit()

if total > pago:
    print(f"El cliente ha pagado menos, aun falta {total - pago}")
elif total == pago:
    print(f"EL cliente ha pagado el monto exacto. No se requiere cambio")
else:
    print(f"El cliente ha pagado demas. El cambio es {pago - total} dolares")