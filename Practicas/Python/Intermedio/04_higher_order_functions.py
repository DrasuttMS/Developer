### Higher Order Functions ##

# Las funciones de orden superior son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultados.
# Estas funciones permiten un enfoque más abstracto y funcional para resolver problemas.

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value, f_sum_one, f):
    return f_sum_one(f(first_value, second_value))
def multiply_values(first_value, second_value):
    return first_value * second_value

result = sum_two_values_and_add_one(2, 4, sum_one, multiply_values)
print(result)  # Output: 13

## Closures ##

# Un closure es una función que recuerda el entorno en el que fue creada, incluso cuando se ejecuta fuera de ese entorno.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

## csalas
## SALAS DE SARZOSA CLAUDIA