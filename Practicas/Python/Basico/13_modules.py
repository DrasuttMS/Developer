## Modules ##
#para importar no debe iniciar con número ni tener espacios
#se recomienda usar nombres descriptivos
#No es necesario el .py al final del nombre del módulo

import module

module.sum(5, 7)

from module import sum

sum(10, 15)

import math

print(math.sqrt(16))  # Raíz cuadrada
print(math.pi)        # Valor de pi 
print(math.factorial(5))  # Factorial de 5
print(math.cos(math.pi))  # Coseno de pi

import random

print(random.randint(1, 100))  # Número aleatorio entre 1 y 100
print(random.choice(['manzana', 'banana', 'cereza']))  # Elección aleatoria de una lista
print(random.random())  # Número aleatorio entre 0.0 y 1.0

import datetime
now = datetime.datetime.now()
print("Fecha y hora actuales:", now)
print("Año:", now.year)
print("Mes:", now.month)
print("Día:", now.day)
