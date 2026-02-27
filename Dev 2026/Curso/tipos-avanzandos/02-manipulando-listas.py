mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas)
mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[:3])
print(mascotas[2:])
print(mascotas[-1])
print(mascotas[::2]) # toma de par en par desde el primer elemento
print(mascotas[1::2]) #toma de par en par desde el indice 1 como se indico
print(mascotas[1:2:2])

numeros = list(range( 21))
print(numeros[::2])
print(numeros[1::2])