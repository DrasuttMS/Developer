monto_solicitado = int(input("Ingresa el monto solicitado en: $ "))
tipo_credito = input("Ingrese el tipo de credito (A o B): ")
cuotas = int(input("Ingrese la cantidad de cuotas: "))

if monto_solicitado <1000000:
    if tipo_credito == 'A':
        tasa_interes = 7.0
    else:
        tasa_interes = 6.5
elif 100000 <= monto_solicitado <2000000:
    if tipo_credito == 'A':
        tasa_interes = 6.0
    else:
        tasa_interes = 6.5
else:
    if tipo_credito =='A':
        tasa_interes = 5.0
    else:
        tasa_interes = 5.5

valor_final = monto_solicitado + monto_solicitado* (tasa_interes / 100)

valor_cuota = valor_final / cuotas

print("\nMonto total a pagar: ${}".format(int(valor_final)))
print("valor de cada cuota: ${}".format(int(valor_cuota)))