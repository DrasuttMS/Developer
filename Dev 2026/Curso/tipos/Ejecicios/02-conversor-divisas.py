moneda = float(input("Ingrese la cantidad de moneda en de su moneda local: "))

usd = moneda * 0.050
eur = moneda * 0.047
gbp = moneda * 0.039
jpy = moneda * 7.71

mensaje =  f"""
El total de moneda local ingresado es de: {moneda},
la conversion a USD es de {moneda} -> {usd},
la conversion a EUR es de {moneda} -> {eur},
la conversion a GBP es de {moneda} -> {gbp} y
la conversion a JPY es de {moneda} -> {jpy}.
"""
print(mensaje)