import random
resultado = []
ruleta = []

N = int(input("Cuantas veces ejecutaremos la ruleta?: "))
for i in range(0,N):
    numero = random.randint(0, 36)
    ruleta.append(numero)

def noHanSalido(ruleta):
    noSalieron = [i for i, cantidad in enumerate(ruleta) if cantidad == 0]
    print("Números que no han sido sorteados:", noSalieron)

def actualizarRuleta(ruleta, N):
    if 0 <= N <= 36:
        ruleta[N] += 1
    else:
        print(-1)

def obtenerPorcentaje(ruleta, N):
    total = sum(ruleta)
    if total == 0:
        return 0
    return (ruleta[N] / total) * 100
    print(total)
