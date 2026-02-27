numeros = [1, 2, 3]

# Manera poco practica
"""
primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]
"""

#primero, segundo, tercero = numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primero, segundo, *otros, penu, ultimo = numeros

print(primero)
print(primero, segundo, penu, ultimo, otros)
