temperatura = float(input("Ingresa una temperatura en Grados Celsius: "))

fahrenheit = (temperatura * 9 / 5) +32
kelvin = temperatura + 273.15

mensaje = f"""
La temperatura en grados Celsius es de {temperatura} grados,
La conversion de grados Celsius a fahrenheit es de {temperatura} grados -> {fahrenheit} grados y
La conversion de grados Celsius a kelvin es de {temperatura} grados -> {kelvin} grados
"""

print(mensaje)