cuenta = float(input("Ingrese el total de la cuenta: $"))
descuento = float(input("Ingrese el % descuento: %"))

def total(cuenta,descuento):
    descuento /= 100
    monto = cuenta * descuento
    final = cuenta - monto
    return final

resultado = total(cuenta,descuento)
print(resultado)