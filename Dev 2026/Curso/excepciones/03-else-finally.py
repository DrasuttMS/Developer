try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un Error!!")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")