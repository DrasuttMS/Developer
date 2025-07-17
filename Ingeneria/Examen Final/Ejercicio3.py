import random
ruleta = []
resultado = []
noHanSalido = []

for i in range(0, 37):
    ruleta.append(i)
print("Ruleta: ", ruleta)

n = int(input("Cuantas veces ejecutaremos la ruleta?: "))
for i in range(0,n):
    numero = random.randint(0, 36)
    if numero in noHanSalido:
        noHanSalido.append(numero)
    else:
        resultado.append(numero)

print("Resultados: ", resultado)
print("No han salido: ", noHanSalido)   