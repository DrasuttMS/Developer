print("Bienvenido al conversor de divisas ")
cantidad = float(input("Introduce la cantidad a convertir: "))
divisa_origen = input("Introduce la divisa de origen (USD, EUR o MXN): ").upper()

if divisa_origen not in ["USD", "EUR", "MXN"]:
    print("Divisa de origen no valida")
    exit()

tasa_usd_a_eur = 0.95
tasa_usd_a_mxn = 20.28
tasa_eur_a_mxn = 21.36

if divisa_origen == "USD":
    cantidad_euros = cantidad * tasa_usd_a_eur
    cantidad_pesos = cantidad * tasa_usd_a_mxn
    print(f"La cantidad de Euros que obtendias segun tu {cantidad} de USD ingresados es: {cantidad_euros} \nLa cantidad de Pesos Mexicanos que obtendias segun tu {cantidad} de USD ingresados es: {cantidad_pesos}")
elif divisa_origen == "EUR":
    cantidad_pesos = cantidad * tasa_eur_a_mxn
    cantidad_dolar = cantidad / tasa_usd_a_eur
    print(f"La cantidad de dolares que obtendias segun tu {cantidad} de EUR ingresados es: {cantidad_dolar} \nLa cantidad de Pesos Mexicanos que obtendias segun tu {cantidad} de USD ingresados es: {cantidad_pesos}")
else:
    cantidad_euros = cantidad / tasa_eur_a_mxn
    cantidad_dolar = cantidad / tasa_usd_a_mxn
    print(f"La cantidad de dolares que obtendias segun tu {cantidad} de MXN ingresados es: {cantidad_dolar} \nLa cantidad de Pesos Euros que obtendias segun tu {cantidad} de MXN ingresados es: {cantidad_euros}")