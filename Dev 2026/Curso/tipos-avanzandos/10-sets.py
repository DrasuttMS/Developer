# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo) # | operador de union
print(primer & segundo) # & interseccion los elemento que se encuentan en ambos set, listas
print(primer - segundo) # - elimina del primer set los datos del segundo set
print(primer ^ segundo) # Diferencia simetrica, elimina los iguales de ambos set


