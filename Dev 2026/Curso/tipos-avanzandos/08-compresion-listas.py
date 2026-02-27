usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1],
    ["Pulga", 5]
    ]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

#Transaformar
nombres = [usuario[0] for usuario in usuarios]

#Filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

#Filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

#transformacion, Map
nombres = list(map(lambda usuario: usuario[0], usuarios))

#filter
menosUsuarios = list(filter(lambda usuario: usuario[1] >2, usuarios))
print(menosUsuarios)

