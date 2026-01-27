def noHanSalido(ruleta):
    lista = []
    for i in range(0,len(ruleta)):
        if ruleta[i] == 0:
            lista.append(ruleta[i])
    return lista

def actualizarRuleta(ruleta, n):
    n = 0
    while (n < 0) or (n > 36):
        n = int(input("Ingrese un numero entre 0 y 36: "))
        if (n <0) or (n > 36):
            print("-1")
        else:
            for i in range(0, len(ruleta)):
                if ruleta[i] == n:
                    num = ruleta[i] + 1
    return num

def obtenerPorcentaje(ruleta, n):
    n = int(input("Ingrese un numero entre 0 y 36: "))
    for i in range(0, len(ruleta)):
        if ruleta[i] == n:
            porcentaje = ruleta[i] / total * 100/100
            total = sum(ruleta)
    return porcentaje

